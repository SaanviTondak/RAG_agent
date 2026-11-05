"""Non-agentic baselines, to measure what the agent's routing and iteration add.

- rag: one filing search with the raw question (no filters), then one answer call. No SQL.
- pipeline: one call plans a SQL query and a filing search, both always run, then one answer call.
  No choosing between sources after seeing results, no follow-up searches, no calculate tool.

Same model, system prompt (schema, caveats, answer format) and retrieval as the agent; results have the
same shape as app.agent.run so the eval grades them identically.

CLI: python -m app.baseline rag|pipeline "question"
"""

import json
import sys
import time

from app.agent import THINK_RE, _record_evidence
from app.config import CHAT_MODEL, MAX_TOKENS, PROMPT_VERSION, SEED, TEMPERATURE
from app.llm import cached_tokens, chat, cost_usd
from app.prompts import SYSTEM_PROMPTS
from app.tools import run_tool

NO_TOOLS = ("\n## This mode\nYou cannot call tools. Answer only from the evidence in the user message. If it is "
            "not enough to answer part of the question, say what is missing instead of guessing.\n")
PLAN = ("\n## This step\nDo not answer yet. Plan the evidence to fetch for the question. Return JSON: "
        '{"sql": "<one SQLite SELECT for the database figures needed, or empty if the database cannot help>", '
        '"search_query": "<what to search for in the 10-K filings>", "ticker": "AAPL|MSFT|GOOGL or null", '
        '"fiscal_year": "2024|2025 or null (which filing to search)"}\n')


def run(question: str, mode: str, model: str = CHAT_MODEL, prompt: str = PROMPT_VERSION) -> dict:
    t0 = time.time()
    trace, sources = [], {}
    evidence = {"sql": False, "filings": False, "table": False}
    usage = {"prompt_tokens": 0, "cached_tokens": 0, "completion_tokens": 0, "llm_calls": 0, "tool_calls": 0}

    def llm(system: str, user: str, **kw) -> str:
        t = time.time()
        resp = chat(model=model, messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                    temperature=TEMPERATURE, seed=SEED, max_tokens=MAX_TOKENS, **kw)
        usage["llm_calls"] += 1
        usage["prompt_tokens"] += resp.usage.prompt_tokens
        usage["cached_tokens"] += cached_tokens(resp.usage)
        usage["completion_tokens"] += resp.usage.completion_tokens
        trace.append({"type": "llm", "ms": int((time.time() - t) * 1000), "finish": resp.choices[0].finish_reason})
        return THINK_RE.sub("", resp.choices[0].message.content or "").strip()

    def tool(name: str, args: dict) -> str:
        t = time.time()
        text, meta = run_tool(name, json.dumps(args))
        usage["tool_calls"] += 1
        _record_evidence(meta, evidence, sources)
        trace.append({"type": "tool", "tool": name, "args": json.dumps(args), "ms": int((time.time() - t) * 1000),
                      "result": text, "meta": {k: v for k, v in meta.items() if k != "hits"},
                      "citations": [h["citation"] for h in meta.get("hits", [])]})
        return f"### {name} {json.dumps(args)}\n{text}"

    if mode == "rag":
        blocks = [tool("search_filings", {"query": question})]
    elif mode == "pipeline":
        raw = llm(SYSTEM_PROMPTS[prompt] + PLAN, question, response_format={"type": "json_object"})
        try:
            plan = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
        except json.JSONDecodeError:
            plan = {}
        trace.append({"type": "plan", "plan": plan})
        blocks = []
        if (plan.get("sql") or "").strip():
            blocks.append(tool("query_sql", {"sql": plan["sql"]}))
        search = {"query": plan.get("search_query") or question}
        for key in ("ticker", "fiscal_year"):
            if plan.get(key) not in (None, "", "null"):
                search[key] = plan[key]
        blocks.append(tool("search_filings", search))
    else:
        raise ValueError(f"unknown baseline mode {mode!r}")

    answer = llm(SYSTEM_PROMPTS[prompt] + NO_TOOLS,
                 f"Question: {question}\n\nEvidence:\n\n" + "\n\n".join(blocks)) or "No answer could be produced."
    usage["cost_usd"] = round(cost_usd(model, usage["prompt_tokens"], usage["completion_tokens"],
                                       usage["cached_tokens"]), 6)
    return {"question": question, "answer": answer, "sources": list(sources.values()), "trace": trace,
            "usage": {**usage, "latency_ms": int((time.time() - t0) * 1000)}, "model": model, "prompt": prompt,
            "system": mode}


if __name__ == "__main__":
    r = run(sys.argv[2], sys.argv[1])
    print(r["answer"], f"\n\n[{r['usage']['latency_ms'] / 1000:.1f}s | ${r['usage']['cost_usd']:.4f}]")
