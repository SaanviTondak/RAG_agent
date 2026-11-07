"""Planning for multi-part questions: a cheap rule decides whether to plan, then one JSON-mode call writes it.

The plan is shown to the user as the first step, guides the agent (appended to the question), and tells the
routing check which sources the answer needs. Simple lookups skip planning, so they stay fast.
"""

import json
import re

from app.llm import chat
from app.prompts import _BASE

# An "ask" is a question word or instruction that starts a clause ("How much did ..." counts once, not twice).
ASK_RE = re.compile(r"(?:^|[,;:.?]\s*|\b(?:and|then)\s+)(?:by\s+)?(what|why|how|which|who|does|did|do|is|are|calculate|compare|"
                    r"find|explain|describe|break\w* down|list)\b", re.I)
DEPENDENT_RE = re.compile(r"\bthe company (?:with|that)\b|\bthat company'?s?\b|\bits (?:10-k|filing)\b|"
                          r"\b(?:compare|comparison|versus|vs\.?)\b|\bexplain any\b|\b(?:agree|match|consistent|add up)\b",
                          re.I)
COMPANY_RE = re.compile(r"\b(apple|microsoft|alphabet|google)\b", re.I)
SOURCES = ("database", "filings", "both", "calculation")
MAX_STEPS = 4
THINK_RE = re.compile(r"<think>.*?</think>", re.S)

PLAN_INSTRUCTIONS = """
## This step
Do not answer and do not call tools yet. Break the question into the smallest set of sub-questions (at most 4)
that together answer it, in the order they must be answered. Each sub-question is a question about the companies
or their data (what to find out), not an instruction about searching or reading. For each give "ask" (one short
question), "source" ("database", "filings", "both" or "calculation") and "depends_on" (numbers of earlier
sub-questions whose answers it needs). Return JSON: {"sub_questions": [{"ask": "...", "source": "...", "depends_on": []}]}
"""


def needs_plan(question: str) -> bool:
    """Multi-part or dependent questions: two or more asks, two or more named companies, or a comparison,
    cross-check or 'the company with ...' phrasing. Measured on the 60 eval questions: see tests/test_planner.py."""
    companies = {m.lower().replace("google", "alphabet") for m in COMPANY_RE.findall(question)}
    return len(ASK_RE.findall(question)) >= 2 or len(companies) >= 2 or bool(DEPENDENT_RE.search(question))


def make_plan(question: str, model: str, history: list[dict] | None = None,
              deadline: float | None = None) -> tuple[list[dict] | None, object]:
    """(sub_questions or None if planning failed, raw usage). Never raises for a bad plan."""
    resp = chat(model=model, messages=[{"role": "system", "content": _BASE + PLAN_INSTRUCTIONS}, *(history or []),
                                       {"role": "user", "content": question}],
                temperature=0.0, seed=7, max_tokens=2048, response_format={"type": "json_object"}, deadline=deadline,
                reasoning_effort="low")  # ~2s instead of ~10s; plans were as good or better in a side-by-side test
    text = THINK_RE.sub("", resp.choices[0].message.content or "")
    try:
        raw = json.loads(text[text.find("{"): text.rfind("}") + 1])["sub_questions"]
    except (ValueError, KeyError, TypeError):
        return None, resp.usage
    steps = []
    for s in raw[:MAX_STEPS]:
        if not isinstance(s, dict) or not str(s.get("ask", "")).strip():
            continue
        source = str(s.get("source", "")).lower()
        deps = [int(d) for d in s.get("depends_on") or [] if str(d).isdigit() and 0 < int(d) <= len(steps)]
        steps.append({"ask": str(s["ask"]).strip(), "source": source if source in SOURCES else "both",
                      "depends_on": deps})
    return (steps or None), resp.usage


def plan_text(steps: list[dict]) -> str:
    lines = []
    for i, s in enumerate(steps, 1):
        uses = f"; uses {', '.join(map(str, s['depends_on']))}" if s["depends_on"] else ""
        lines.append(f"{i}. {s['ask']} ({s['source']}{uses})")
    return "\n".join(lines)


def required_sources(steps: list[dict]) -> set[str]:
    """Which evidence the plan says the answer needs: 'filings' and/or 'database'."""
    need = set()
    for s in steps:
        if s["source"] in ("filings", "both"):
            need.add("filings")
        if s["source"] in ("database", "both"):
            need.add("database")
    return need

