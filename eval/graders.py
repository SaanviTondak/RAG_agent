"""Graders that mirror the official ones, plus diagnostics that explain why an answer failed.

Fireworks names its grading methods (fuzzy_numeric, exact_match_entity, llm_judge) but doesn't publish
them, so these lean strict: if ours passes, the official one should too. out_of_scope is our addition
for "not in the data" questions.

Every grader returns {"pass", "score" (0-1), "reason", "details", "judge_usage"}.
"""

import json
import re
from functools import lru_cache

from app.config import INDEX_DIR, TICKERS
from app.llm import cached_tokens, chat, cost_usd
from app.numbers import (ABBREVIATIONS, body, number_matches, numbers_agree, parse_numbers,  # noqa: F401
                         ungrounded_numbers)

# ---------------------------------------------------------------- text


def first_sentence(answer: str) -> str:
    lines = [l for l in answer.strip().splitlines() if l.strip() and not l.lstrip().startswith("#")]
    text = ABBREVIATIONS.sub(lambda m: m.group(0).replace(".", "§"), lines[0] if lines else "")
    return re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0].replace("§", ".")


def lead(answer: str) -> str:
    """The opening paragraph: text before the first blank line, bullet, heading or table."""
    out = []
    for line in body(answer).strip().splitlines():
        if not line.strip() or re.match(r"\s*([-*+]\s|#|\||\d+\.\s)", line):  # "**Bold** text" is not a bullet
            if out:
                break
            continue
        out.append(line.strip())
    return " ".join(out)


def fuzzy_numeric(answer: str, gold: float) -> dict:
    nums = [n for n in parse_numbers(body(answer)) if not n["is_year"]]
    hit = next((n for n in nums if number_matches(n, gold)), None)
    head = [n for n in parse_numbers(first_sentence(answer)) if not n["is_year"]]
    strict = any(number_matches(n, gold) for n in head)
    reason = f"found {hit['text']!r}" if hit else f"no number matches {gold} (saw: {', '.join(n['text'] for n in nums[:8])})"
    return {"pass": bool(hit), "score": float(bool(hit)), "reason": reason,
            "details": {"first_sentence_pass": strict}, "judge_usage": None}


# ---------------------------------------------------------------- LLM judge

def _usage(model: str, resp) -> dict:
    u = resp.usage
    c = cached_tokens(u)
    return {"prompt_tokens": u.prompt_tokens, "completion_tokens": u.completion_tokens, "cached_tokens": c,
            "cost_usd": cost_usd(model, u.prompt_tokens, u.completion_tokens, c)}


def _add_usage(a: dict | None, b: dict) -> dict:
    return b if a is None else {k: a[k] + b[k] for k in b}


def judge_json(model: str, system: str, user: str) -> tuple[dict, dict]:
    """One JSON-mode judge call (retried once if the JSON doesn't parse). Returns (object, usage).
    max_tokens is high because deepseek reasons first; at 4096 it sometimes ran out mid-JSON."""
    usage = None
    for _ in range(2):
        resp = chat(model=model, messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                    temperature=0.0, seed=7, max_tokens=8192, response_format={"type": "json_object"})
        usage = _add_usage(usage, _usage(model, resp))
        text = re.sub(r"<think>.*?</think>", "", resp.choices[0].message.content or "", flags=re.S)
        m = re.search(r"\{.*\}", text, re.S)
        try:
            return json.loads(m.group(0) if m else text), usage
        except json.JSONDecodeError:
            continue
    raise ValueError(f"judge {model} returned invalid JSON twice")


SPLIT_SYSTEM = """You turn a reference answer into a checklist for grading.
Split the reference answer into the atomic facts a correct answer must contain: one checkable claim per
fact (a figure, an entity, a direction of change, a cause, a definition, one item of a list).
Keep numbers exactly as written. Do not add facts that are not in the reference. Do not split one figure
into several facts. Return JSON: {"facts": ["...", "..."]}"""


def split_facts(question: str, gold_answer: str, model: str) -> tuple[list[str], dict]:
    obj, usage = judge_json(model, SPLIT_SYSTEM, f"Question: {question}\n\nReference answer: {gold_answer}")
    return [str(f) for f in obj["facts"]], usage


JUDGE_SYSTEM = """You grade an answer from a financial research assistant against a checklist of reference facts.
For each fact decide:
- "covered": the answer states it or an equivalent (wording may differ; a list item may be phrased or
  grouped differently as long as its substance is there).
- "missing": the answer does not state it.
- "contradicted": the answer states something incompatible with it.
Numbers: rounding differences count as covered only if the two agree when rounded to the coarser
precision ($66.95 billion vs $67.0 billion: covered; 3.8% vs 3.9%: contradicted). Units and formats may differ.
Extra information not in the checklist is fine unless it contradicts a fact.
Return JSON: {"facts": [{"fact": "<fact>", "verdict": "covered|missing|contradicted", "evidence": "<short quote from the answer, or empty>"}]}"""

PASS_COVERAGE = 0.8


def llm_judge(question: str, answer: str, facts: list[str], model: str) -> dict:
    checklist = "\n".join(f"{i}. {f}" for i, f in enumerate(facts, 1))
    obj, usage = judge_json(model, JUDGE_SYSTEM,
                            f"Question: {question}\n\nReference facts:\n{checklist}\n\nAnswer to grade:\n{body(answer)}")
    verdicts = [str(f.get("verdict", "missing")).lower() for f in obj.get("facts", [])][: len(facts)]
    verdicts += ["missing"] * (len(facts) - len(verdicts))
    covered = verdicts.count("covered")
    contradicted = verdicts.count("contradicted")
    score = covered / len(facts) if facts else 0.0
    bad = [f"{v}: {f}" for f, v in zip(facts, verdicts) if v != "covered"]
    return {"pass": score >= PASS_COVERAGE and not contradicted, "score": round(score, 3),
            "reason": f"{covered}/{len(facts)} facts covered" + (f"; {'; '.join(bad)}" if bad else ""),
            "details": {"facts": obj.get("facts", [])}, "judge_usage": usage}


ENTITY_SYSTEM = f"""You read an answer from a financial research assistant and report which company or companies it
gives as its answer to the question. Ignore companies that are only mentioned for comparison or context:
for "which company has the highest X", return only the company the answer says is highest, even if the answer
also lists the others with their figures. Only when the question itself asks for several companies or a ranking
(e.g. "the top two", "rank the companies") return all of them, in the answer's order.
Use tickers: {", ".join(f"{t} ({n})" for t, n in TICKERS.items())}. Return JSON: {{"entities": ["TICKER", ...]}}"""

ENTITY_RES = {"AAPL": re.compile(r"\b(apple|aapl)\b", re.I), "MSFT": re.compile(r"\b(microsoft|msft)\b", re.I),
              "GOOGL": re.compile(r"\b(alphabet|google|googl|goog)\b", re.I)}


def entities_in(text: str) -> list[str]:
    found = [(m.start(), t) for t, r in ENTITY_RES.items() if (m := r.search(text))]
    return [t for _, t in sorted(found)]


def exact_match_entity(question: str, answer: str, gold_entities: list[str], ordered: bool,
                       gold_numeric: float | None, model: str) -> dict:
    obj, usage = judge_json(model, ENTITY_SYSTEM, f"Question: {question}\n\nAnswer:\n{body(answer)}")
    named = [t for t in (str(e).upper() for e in obj.get("entities", [])) if t in TICKERS]
    entity_ok = named == gold_entities if ordered else set(named) == set(gold_entities)
    num = fuzzy_numeric(answer, gold_numeric) if gold_numeric is not None else None
    string_ok = set(gold_entities) <= set(entities_in(first_sentence(answer)))
    ok = entity_ok and (num is None or num["pass"])
    reason = f"answer names {named or 'none'} (gold {gold_entities})" + (f"; number: {num['reason']}" if num else "")
    return {"pass": ok, "score": float(ok), "reason": reason,
            "details": {"entities": named, "entity_ok": entity_ok, "number_ok": None if num is None else num["pass"],
                        "string_check_ok": string_ok, "checks_disagree": string_ok != entity_ok},
            "judge_usage": usage}


OOS_SYSTEM = """You grade an answer from a financial research assistant whose data covers ONLY Apple, Microsoft
and Alphabet: a database of annual financials (FY2023-FY2025) and each company's FY2024 and FY2025 10-K.
The question asks for something outside that data. Pass if the answer clearly says the requested
information is not available in its data and does not present a made-up figure or fact for it.
Offering related information that IS available is fine.
Return JSON: {"pass": true|false, "reason": "<one sentence>"}"""


def out_of_scope(question: str, answer: str, model: str) -> dict:
    obj, usage = judge_json(model, OOS_SYSTEM, f"Question: {question}\n\nAnswer:\n{body(answer)}")
    ok = bool(obj.get("pass"))
    return {"pass": ok, "score": float(ok), "reason": str(obj.get("reason", "")), "details": {}, "judge_usage": usage}


# ---------------------------------------------------------------- diagnostics (no LLM)

@lru_cache(maxsize=1)
def _chunk_pages() -> dict[str, tuple[int, int]]:
    pages = {}
    for line in open(INDEX_DIR / "chunks.jsonl"):
        c = json.loads(line)
        pages[c["id"]] = (c["page"], c["page_end"])
    return pages


def _tool_steps(result: dict) -> list[dict]:
    return [s for s in result["trace"] if s["type"] == "tool"]


def used_modalities(result: dict) -> set[str]:
    used = set()
    for s in _tool_steps(result):
        if s["tool"] == "query_sql" and "rows" in s["meta"]:
            used.add("sql")
        elif (s["tool"] == "search_filings" and s.get("citations")) or (s["tool"] == "read_section" and s["meta"].get("parents")):
            used.add("pdf")
    return used


def routing(result: dict, required: list[str]) -> dict:
    used = used_modalities(result)
    missing, extra = sorted(set(required) - used), sorted(used - set(required))
    return {"used": sorted(used), "missing": missing, "extra": extra, "ok": not missing}


def pages_seen(result: dict) -> set[tuple[str, int]]:
    seen = set()
    for s in result["sources"]:
        if s["type"] == "filing":
            start, end = _chunk_pages().get(s["chunk_id"], (s["page"], s["page"]))
        elif s["type"] == "section":
            start, end = s["page_start"], s["page_end"]
        else:
            continue
        seen |= {(s["doc"], p) for p in range(start, end + 1)}
    return seen


def gold_page_recall(result: dict, gold_pages: list[dict]) -> dict | None:
    if not gold_pages:
        return None
    seen = pages_seen(result)
    hits = [g for g in gold_pages if (g["doc"], g["page"]) in seen]
    return {"hit": bool(hits), "recall": round(len(hits) / len(gold_pages), 3), "n_gold": len(gold_pages)}


CITE_RE = re.compile(r"\b(AAPL|MSFT|GOOGL) FY(\d{4}) 10-K,?\s*pp?\.\s*(\d+)(?:\s*[-–]\s*(\d+))?")
SQL_CITE_RE = re.compile(r"\[SQL:\s*([^\]]+)\]", re.I)


def citation_check(result: dict) -> dict:
    """Every filing page cited must have been retrieved; every [SQL: table] must have been queried."""
    seen = pages_seen(result)
    sql_run = " ".join(s["sql"].lower() for s in result["sources"] if s["type"] == "sql")
    cited, invalid = 0, []
    for m in CITE_RE.finditer(result["answer"]):
        ticker, year, p1, p2 = m.groups()
        doc, pages = f"{ticker}_FY{year}_10-K", range(int(p1), int(p2 or p1) + 1)
        cited += 1
        if not any((doc, p) in seen for p in pages):
            invalid.append(m.group(0))
    for m in SQL_CITE_RE.finditer(result["answer"]):
        for table in re.split(r"[,;/]|\band\b", m.group(1)):
            table = table.strip().lower()
            if table:
                cited += 1
                if table not in sql_run:
                    invalid.append(f"SQL: {table}")
    return {"n_cited": cited, "invalid": invalid, "ok": not invalid}


def grounding_check(result: dict) -> dict:
    """Answer numbers not found in any tool output (see app.numbers.ungrounded_numbers)."""
    checked, ungrounded = ungrounded_numbers(result["answer"], [s.get("result", "") for s in _tool_steps(result)])
    return {"n_checked": checked, "ungrounded": ungrounded, "ok": not ungrounded}


# ---------------------------------------------------------------- does the opening paragraph alone answer it?

def lead_check(q: dict, answer: str, judge_model: str, facts: dict[str, list[str]]) -> dict:
    """Grade only the opening paragraph. Entity questions use the string check here (no extra judge call)."""
    text, method = lead(answer), q["evaluation"]
    if method == "fuzzy_numeric":
        g = fuzzy_numeric(text, q["gold_answer_numeric"])
    elif method == "exact_match_entity":
        named, gold = entities_in(text), q["gold_entities"]
        ok = named[: len(gold)] == gold if q.get("ordered") else set(gold) <= set(named)
        if q.get("gold_answer_numeric") is not None:
            ok = ok and fuzzy_numeric(text, q["gold_answer_numeric"])["pass"]
        g = {"pass": ok, "score": float(ok), "judge_usage": None}
    elif method == "llm_judge":
        g = llm_judge(q["question"], text, facts[q["id"]], judge_model)
    else:
        g = out_of_scope(q["question"], text, judge_model)
    return {"pass": g["pass"], "score": g["score"], "words": len(text.split()), "judge_usage": g["judge_usage"]}


# ---------------------------------------------------------------- dispatch

def grade(q: dict, result: dict, judge_model: str, facts: dict[str, list[str]]) -> dict:
    """Grade one agent result for question `q` (official key fields + our gold_* fields)."""
    method, answer = q["evaluation"], result["answer"]
    if method == "fuzzy_numeric":
        g = fuzzy_numeric(answer, q["gold_answer_numeric"])
    elif method == "exact_match_entity":
        g = exact_match_entity(q["question"], answer, q["gold_entities"], q.get("ordered", False),
                               q.get("gold_answer_numeric"), judge_model)
    elif method == "llm_judge":
        g = llm_judge(q["question"], answer, facts[q["id"]], judge_model)
    elif method == "out_of_scope":
        g = out_of_scope(q["question"], answer, judge_model)
    else:
        raise ValueError(f"unknown evaluation method {method!r} for {q['id']}")
    return {**g, "lead": lead_check(q, answer, judge_model, facts), "words": len(body(answer).split()),
            "routing": routing(result, q["required_modalities"]),
            "recall": gold_page_recall(result, q.get("gold_pages") or []),
            "citations": citation_check(result), "grounding": grounding_check(result)}
