"""Tool-calling agent: the LLM routes between SQL and the filings; deterministic code adds guardrails.

Guardrails around the LLM's own routing:
- a regex pre-pass adds company / fiscal-year hints to the question,
- the first turn must call a tool (no answering from memory),
- coverage nudges: before accepting an answer, send the model back once if a narrative question never
  touched the filings, or a numeric question never touched SQL or a financial table,
- a tool-call budget, after which the model must answer from the evidence it has.

CLI: python -m app.agent "question" [--model ID] [--no-rerank]
"""

import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import app.retrieval
from app.config import CHAT_MODEL, MAX_TOKENS, MAX_TOOL_CALLS, MAX_TURNS, SEED, TEMPERATURE, TRACE_DIR
from app.llm import chat
from app.prompts import SYSTEM_PROMPT
from app.tools import TOOL_SCHEMAS, run_tool

COMPANY_RES = {
    "AAPL": re.compile(r"\b(apple|aapl)\b", re.I),
    "MSFT": re.compile(r"\b(microsoft|msft)\b", re.I),
    "GOOGL": re.compile(r"\b(alphabet|google|googl|goog)\b", re.I),
}
YEAR_RE = re.compile(r"\b(?:fy\s?'?)?(20(?:2[0-9]))\b|\bfy\s?'?(2[0-9])\b", re.I)
RECENT_RE = re.compile(r"\b(most recent|latest|last)\b.{0,20}\b(fiscal )?years?\b", re.I)
NARRATIVE_RE = re.compile(
    r"\b(why|explain\w*|reasons?|according to|10-k|filings?|risks?|strateg\w*|describe\w*|defin\w*|"
    r"commentary|management|discuss\w*|disclos\w*|say|says)\b", re.I)
NUMERIC_RE = re.compile(
    r"\b(how much|revenue|income|sales|margin|ratio|eps|earnings|assets|liabilities|debt|cash|percent\w*|"
    r"growth|rate|increase|decrease|change|calculate|highest|lowest|largest|fastest|billion|million)\b", re.I)

FILINGS_NUDGE = ("Before answering: this question asks about explanations or disclosures in the filings, but you "
                 "have not searched the 10-Ks yet. Use search_filings (and read_section if needed) to ground that "
                 "part, then answer.")
NUMERIC_NUDGE = ("Before answering: the question involves figures, but you have not checked the database or a "
                 "financial table in the filings. Verify the numbers with query_sql (or a filing table), then answer.")
FALLBACK_PROMPT = ("Tool budget reached. Answer now using only the evidence gathered above, in the required format, "
                   "and state briefly what could not be verified.")
THINK_RE = re.compile(r"<think>.*?</think>", re.S)


def hints(question: str) -> str:
    """Deterministic entity hints appended to the question. The model may override them."""
    companies = [t for t, r in COMPANY_RES.items() if r.search(question)]
    years = sorted({int(a) if a else 2000 + int(b) for a, b in YEAR_RE.findall(question)})
    parts = []
    if companies:
        parts.append("companies mentioned: " + ", ".join(companies))
    if years:
        parts.append("fiscal years mentioned: " + ", ".join(map(str, years)))
    if RECENT_RE.search(question):
        parts.append("'most recent fiscal year' = FY2025 for all three companies (two most recent = FY2024, FY2025)")
    return f"\n\n[Parser hints, verify against the question: {'; '.join(parts)}]" if parts else ""


def _nudge(question: str, evidence: dict, sent: set) -> str | None:
    if "filings" not in sent and not evidence["filings"] and NARRATIVE_RE.search(question):
        sent.add("filings")
        return FILINGS_NUDGE
    if "numeric" not in sent and not (evidence["sql"] or evidence["table"]) and NUMERIC_RE.search(question):
        sent.add("numeric")
        return NUMERIC_NUDGE
    return None


def _record_evidence(meta: dict, evidence: dict, sources: dict) -> None:
    kind = meta.get("type")
    if kind == "sql" and "rows" in meta:
        evidence["sql"] = True
        sources[("sql", meta["sql"])] = {"type": "sql", "sql": meta["sql"], "rows": meta["rows"]}
    elif kind == "search" and meta["hits"]:
        evidence["filings"] = True
        evidence["table"] |= any(h["is_table"] for h in meta["hits"])
        for h in meta["hits"]:
            sources.setdefault(("chunk", h["chunk_id"]), {"type": "filing", **{k: h[k] for k in (
                "citation", "doc", "page", "section", "chunk_id", "parent_id", "is_table", "text")}})
    elif kind == "section" and meta["parents"]:
        evidence["filings"] = True
        evidence["table"] |= any(p["has_table"] for p in meta["parents"])
        for p in meta["parents"]:
            sources.setdefault(("parent", p["parent_id"]), {"type": "section", **p})


def run(question: str, history: list[dict] | None = None, model: str = CHAT_MODEL, rerank: bool | None = None,
        on_step=None) -> dict:
    """Answer one question. `history` is prior chat turns ({role, content}) for UI follow-ups."""
    if rerank is not None:
        app.retrieval.rerank_enabled = rerank
    t0 = time.time()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, *(history or []),
                {"role": "user", "content": question + hints(question)}]
    trace, sources, nudges = [], {}, set()
    evidence = {"sql": False, "filings": False, "table": False}
    usage = {"prompt_tokens": 0, "completion_tokens": 0, "llm_calls": 0, "tool_calls": 0}
    answer = None

    def emit(step: dict) -> None:
        trace.append(step)
        if on_step:
            on_step(step)

    def call_llm(tool_choice: str):
        t = time.time()
        resp = chat(model=model, messages=messages, tools=TOOL_SCHEMAS, tool_choice=tool_choice,
                    temperature=TEMPERATURE, seed=SEED, max_tokens=MAX_TOKENS)
        usage["llm_calls"] += 1
        if resp.usage:
            usage["prompt_tokens"] += resp.usage.prompt_tokens
            usage["completion_tokens"] += resp.usage.completion_tokens
        emit({"type": "llm", "ms": int((time.time() - t) * 1000), "finish": resp.choices[0].finish_reason})
        return resp.choices[0].message

    for turn in range(MAX_TURNS):
        if usage["tool_calls"] >= MAX_TOOL_CALLS:
            break
        msg = call_llm("required" if turn == 0 else "auto")
        if msg.tool_calls:
            messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": [
                {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                for tc in msg.tool_calls]})
            budget = MAX_TOOL_CALLS - usage["tool_calls"]
            runnable, skipped = msg.tool_calls[:budget], msg.tool_calls[budget:]
            started = time.time()
            with ThreadPoolExecutor(max_workers=4) as pool:
                results = list(pool.map(lambda tc: run_tool(tc.function.name, tc.function.arguments), runnable))
            ms = int((time.time() - started) * 1000)
            for tc, (text, meta) in zip(runnable, results):
                usage["tool_calls"] += 1
                _record_evidence(meta, evidence, sources)
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": text})
                emit({"type": "tool", "tool": tc.function.name, "args": tc.function.arguments, "ms": ms,
                      "result": text[:2000], "meta": {k: v for k, v in meta.items() if k != "hits"},
                      "citations": [h["citation"] for h in meta.get("hits", [])]})
            for tc in skipped:
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": "Skipped: tool budget reached."})
            continue

        content = THINK_RE.sub("", msg.content or "").strip()
        nudge = _nudge(question, evidence, nudges)
        if nudge and usage["tool_calls"] < MAX_TOOL_CALLS:
            messages += [{"role": "assistant", "content": content}, {"role": "user", "content": nudge}]
            emit({"type": "nudge", "text": nudge})
            continue
        answer = content
        break

    if not answer:
        messages.append({"role": "user", "content": FALLBACK_PROMPT})
        emit({"type": "fallback"})
        answer = THINK_RE.sub("", call_llm("none").content or "").strip() or "No answer could be produced."

    result = {"question": question, "answer": answer, "sources": list(sources.values()), "trace": trace,
              "usage": {**usage, "latency_ms": int((time.time() - t0) * 1000)}, "model": model}
    _save_trace(result)
    return result


def _save_trace(result: dict) -> None:
    TRACE_DIR.mkdir(exist_ok=True)
    path = TRACE_DIR / f"{datetime.now():%Y%m%d}.jsonl"
    with open(path, "a") as f:
        f.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"), **result}, default=str) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question")
    ap.add_argument("--model", default=CHAT_MODEL)
    ap.add_argument("--no-rerank", action="store_true")
    a = ap.parse_args()

    def show(step):
        if step["type"] == "tool":
            print(f"  -> {step['tool']} {step['args'][:160]} ({step['ms']} ms)")
        elif step["type"] in ("nudge", "fallback"):
            print(f"  !! {step['type']}")

    r = run(a.question, model=a.model, rerank=False if a.no_rerank else None, on_step=show)
    u = r["usage"]
    print(f"\n{r['answer']}\n\n[{u['latency_ms'] / 1000:.1f}s | {u['llm_calls']} LLM calls | {u['tool_calls']} tool calls | "
          f"{u['prompt_tokens']} in / {u['completion_tokens']} out tokens]")


if __name__ == "__main__":
    main()
