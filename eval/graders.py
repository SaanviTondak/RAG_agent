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
from app.evidence import CITE_RE, SQL_CITE_RE
from app.llm import cached_tokens, chat, cost_usd
from app.numbers import (ABBREVIATIONS, ENTITY_RES, body, entities_in, first_sentence, number_matches,  # noqa: F401
                         numbers_agree, parse_numbers, ungrounded_numbers)
from app.prompts import _BASE

# ---------------------------------------------------------------- text


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


def gold_unit(q: dict) -> str:
    """The unit of a question's numeric gold: "usd" (raw dollars), "pct" (percent or percentage points) or "plain"
    (ratio, per-share). Read from how the gold answer writes the gold figure."""
    gold = q["gold_answer_numeric"]
    if abs(gold) >= 1e5:
        return "usd"
    for n in parse_numbers(q["gold_answer"]):
        if number_matches(n, gold):
            return "pct" if n["pct"] else "plain"
    return "plain"


HEADLINE_SYSTEM = """You read an answer from a financial research assistant and report the figure it gives as its
answer to the question: the requested value itself, not comparison figures, inputs to a calculation, other years or
other companies. Copy the figure exactly as written, with its unit ("$416.2 billion", "15.1%", "2.01").
"negative" is true if the answer presents that figure as a decrease, decline, loss or negative value.
If the answer gives no figure, return an empty string. Return JSON: {"figure": "...", "negative": true|false}"""


def fuzzy_numeric(answer: str, gold: float, unit: str | None = None, question: str | None = None,
                  judge_model: str | None = None) -> dict:
    """Pass if the figure the answer gives as its answer equals the gold (unit, direction, and the rounding rule).
    With a judge, the judge picks that figure (as exact_match_entity picks the company) and a scan of the whole
    answer is the cross-check; without one, the scan decides (used for the opening paragraph and gold files)."""
    nums = [n for n in parse_numbers(body(answer)) if not n["is_year"]]
    hit = next((n for n in nums if number_matches(n, gold, unit)), None)
    head = [n for n in parse_numbers(first_sentence(answer)) if not n["is_year"]]
    details = {"first_sentence_pass": any(number_matches(n, gold, unit) for n in head), "scan_pass": bool(hit),
               "unit": unit}
    if not judge_model:
        reason = f"found {hit['text']!r}" if hit else f"no number matches {gold} (saw: {', '.join(n['text'] for n in nums[:8])})"
        return {"pass": bool(hit), "score": float(bool(hit)), "reason": reason, "details": details, "judge_usage": None}
    obj, usage = judge_json(judge_model, HEADLINE_SYSTEM, f"Question: {question}\n\nAnswer:\n{body(answer)}")
    figure = str(obj.get("figure") or "")
    parsed = [n for n in parse_numbers(figure) if not n["is_year"]]
    ok = bool(parsed) and number_matches({**parsed[0], "declining": parsed[0]["declining"] or bool(obj.get("negative"))},
                                         gold, unit)
    details.update(figure=figure, negative=bool(obj.get("negative")), checks_disagree=ok != bool(hit))
    reason = (f"answer's figure {figure!r} " + ("matches" if ok else "does not match") + f" {gold} ({unit})"
              if figure else "the answer gives no figure")
    return {"pass": ok, "score": float(ok), "reason": reason, "details": details, "judge_usage": usage}


# ---------------------------------------------------------------- LLM judge

def _usage(model: str, resp) -> dict:
    u = resp.usage
    c = cached_tokens(u)
    return {"prompt_tokens": u.prompt_tokens, "completion_tokens": u.completion_tokens, "cached_tokens": c,
            "cost_usd": cost_usd(model, u.prompt_tokens, u.completion_tokens, c)}


def _add_usage(a: dict | None, b: dict) -> dict:
    return b if a is None else {k: a[k] + b[k] for k in b}


def judge_json(model: str, system: str, user: str, max_tokens: int = 8192, **kw) -> tuple[dict, dict]:
    """One JSON-mode judge call (retried once if the JSON doesn't parse). Returns (object, usage).
    max_tokens is high because deepseek reasons first; at 4096 it sometimes ran out mid-JSON."""
    usage = None
    for _ in range(2):
        resp = chat(model=model, messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                    temperature=0.0, seed=7, max_tokens=max_tokens, response_format={"type": "json_object"}, **kw)
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

def exact_match_entity(question: str, answer: str, gold_entities: list[str], ordered: bool,
                       gold_numeric: float | None, model: str, unit: str | None = None) -> dict:
    obj, usage = judge_json(model, ENTITY_SYSTEM, f"Question: {question}\n\nAnswer:\n{body(answer)}")
    named = [t for t in (str(e).upper() for e in obj.get("entities", [])) if t in TICKERS]
    entity_ok = named == gold_entities if ordered else set(named) == set(gold_entities)
    num = fuzzy_numeric(answer, gold_numeric, unit) if gold_numeric is not None else None
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


HOLISTIC_SYSTEM = """You grade an answer to a financial question against a reference answer.
The answer is correct if it conveys the reference answer's key information and does not contradict it. Figures
may be rounded differently or written in other units; wording may differ. Additional correct detail is fine.
Return JSON: {"correct": true|false, "reason": "<one sentence>"}"""


def holistic_judge(question: str, answer: str, gold_answer: str, model: str) -> dict:
    """A one-verdict judge against the whole reference answer: the common way LLM judges are built, and a check
    that our fact-by-fact judge is not the only definition under which the system passes."""
    obj, usage = judge_json(model, HOLISTIC_SYSTEM, f"Question: {question}\n\nReference answer: {gold_answer}"
                                                    f"\n\nAnswer to grade:\n{body(answer)}")
    ok = bool(obj.get("correct"))
    return {"pass": ok, "score": float(ok), "reason": str(obj.get("reason", "")), "details": {}, "judge_usage": usage}


# ---------------------------------------------------------------- faithfulness: is every claim backed by the evidence?

FAITH_SYSTEM = """You check an answer from a financial research assistant against the evidence it had: the data notes
it was given (fiscal-year ends, data caveats), its tools' results (database query results and 10-K filing
excerpts) and any earlier conversation.
List every factual claim the answer makes about the companies: each figure, comparison, trend, cause, disclosure
and characterisation (e.g. "the dominant driver", "lean working-capital management"). For each claim decide:
- "supported": the evidence states it, or it follows from evidence figures by correct arithmetic or rounding.
- "unsupported": the evidence does not state it (even if it may be true in the real world).
- "contradicted": the evidence says something incompatible with it, or the arithmetic is wrong.
Ignore statements about the assistant's own process (what it searched, could not verify, or cites), and
general definitions (what a current ratio is). Units and formats may differ ($36,147 million = $36.1 billion).
Return JSON: {"claims": [{"claim": "<short paraphrase>", "verdict": "supported|unsupported|contradicted",
"evidence": "<short quote from the evidence, or empty>"}]}"""

FAITH_MAX_CHARS = 160_000  # largest evidence seen in a tuning run: 65k characters
# The agent's system prompt states fiscal-year ends and data caveats (Apple's segments are geographic, Alphabet's
# hedging line, Microsoft's restatement). Without them the stress test flagged those correct caveats as unsupported.
DATA_NOTES = _BASE[_BASE.index("- Fiscal year ends"): _BASE.index("## How to work")].strip()


def evidence_text(result: dict, history: list[dict] | None = None) -> tuple[str, bool]:
    """Everything the agent saw: earlier turns, then each tool call and its output. (text, truncated)."""
    parts = [f"[data notes the assistant was given]\n{DATA_NOTES}"]
    parts += [f"[earlier turn, {m['role']}]\n{m['content']}" for m in history or []]
    parts += [f"[{s['tool']} {s.get('args', '')[:300]}]\n{s['result']}" for s in _tool_steps(result)]
    text = "\n\n".join(parts)
    return text[:FAITH_MAX_CHARS], len(text) > FAITH_MAX_CHARS


def faithfulness(question: str, result: dict, model: str, history: list[dict] | None = None) -> dict:
    """Claims in the answer that the evidence does not back. A diagnostic, not part of pass/fail: the gold
    checklist says whether the answer is right; this says whether it added anything the tools never returned."""
    evidence, truncated = evidence_text(result, history)
    # listing every claim of a long answer used all 8192 tokens on reasoning at default effort (q_006, q_014)
    obj, usage = judge_json(model, FAITH_SYSTEM, f"Question: {question}\n\nEvidence:\n{evidence or '(no tool output)'}"
                                                 f"\n\nAnswer to check:\n{body(result['answer'])}",
                            max_tokens=16384, reasoning_effort="low")
    claims = [c for c in obj.get("claims", []) if isinstance(c, dict)]
    verdict = lambda c: str(c.get("verdict", "")).lower()  # noqa: E731
    flagged = [{"claim": str(c.get("claim", "")), "verdict": verdict(c)} for c in claims
               if verdict(c) in ("unsupported", "contradicted")]
    return {"n_claims": len(claims), "flagged": flagged, "ok": not flagged,
            "contradicted": sum(f["verdict"] == "contradicted" for f in flagged), "truncated": truncated,
            "judge_usage": usage}


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




def citation_check(result: dict) -> dict:
    """Every filing page cited must have been retrieved (each page of a range, not just one of them); every
    [SQL: table] must have been queried."""
    seen = pages_seen(result)
    sql_run = " ".join(s["sql"].lower() for s in result["sources"] if s["type"] == "sql")
    cited, invalid = 0, []
    for m in CITE_RE.finditer(result["answer"]):
        ticker, year, p1, p2 = m.groups()
        doc, pages = f"{ticker}_FY{year}_10-K", range(int(p1), int(p2 or p1) + 1)
        cited += 1
        unseen = [p for p in pages if (doc, p) not in seen]
        if unseen:
            invalid.append(m.group(0) + ("" if len(unseen) == len(pages) else f" (p.{', '.join(map(str, unseen))} not seen)"))
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
        g = fuzzy_numeric(text, q["gold_answer_numeric"], gold_unit(q))
    elif method == "exact_match_entity":
        named, gold = entities_in(text), q["gold_entities"]
        ok = named[: len(gold)] == gold if q.get("ordered") else set(gold) <= set(named)
        if q.get("gold_answer_numeric") is not None:
            ok = ok and fuzzy_numeric(text, q["gold_answer_numeric"], gold_unit(q))["pass"]
        g = {"pass": ok, "score": float(ok), "judge_usage": None}
    elif method == "llm_judge":
        g = llm_judge(q["question"], text, facts[q["id"]], judge_model)
    else:
        g = out_of_scope(q["question"], text, judge_model)
    return {"pass": g["pass"], "score": g["score"], "words": len(text.split()), "judge_usage": g["judge_usage"]}


# ---------------------------------------------------------------- dispatch

def grade_answer(q: dict, answer: str, judge_model: str, facts: dict[str, list[str]]) -> dict:
    """The pass/fail grade alone (the question's grading method), without diagnostics."""
    method = q["evaluation"]
    if method == "fuzzy_numeric":
        return fuzzy_numeric(answer, q["gold_answer_numeric"], gold_unit(q), q["question"], judge_model)
    if method == "exact_match_entity":
        return exact_match_entity(q["question"], answer, q["gold_entities"], q.get("ordered", False),
                                  q.get("gold_answer_numeric"), judge_model,
                                  gold_unit(q) if q.get("gold_answer_numeric") is not None else None)
    if method == "llm_judge":
        return llm_judge(q["question"], answer, facts[q["id"]], judge_model)
    if method == "out_of_scope":
        return out_of_scope(q["question"], answer, judge_model)
    raise ValueError(f"unknown evaluation method {method!r} for {q['id']}")


def _sum_usage(*usages: dict | None) -> dict | None:
    total = None
    for u in usages:
        if u:
            total = _add_usage(total, u)
    return total


def grade(q: dict, result: dict, judge_model: str, facts: dict[str, list[str]], faith: bool = True) -> dict:
    """Grade one agent result for question `q` (official key fields + our gold_* fields).
    judge_usage covers every judge call made here (grader, opening-paragraph check, faithfulness)."""
    answer = result["answer"]
    g = grade_answer(q, answer, judge_model, facts)
    lead = lead_check(q, answer, judge_model, facts)
    fa = faithfulness(q["question"], result, judge_model, q.get("history")) if faith else None
    return {**g, "judge_usage": _sum_usage(g["judge_usage"], lead["judge_usage"], fa and fa["judge_usage"]),
            "lead": lead, "faithfulness": fa, "words": len(body(answer).split()),
            "routing": routing(result, q["required_modalities"]),
            "recall": gold_page_recall(result, q.get("gold_pages") or []),
            "citations": citation_check(result), "grounding": grounding_check(result)}
