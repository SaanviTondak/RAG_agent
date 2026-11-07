"""Answer editor: one extra call that shortens a long draft answer without changing what it says.

Chosen by eval/concise_trial.py after six prompt-only attempts lost facts: asking for brevity while the agent
researches makes it research less, so research stays as it was and only the finished draft is edited.
The editor sees the question and the draft only (no documents), lists the draft's points first, then rewrites.
Deterministic checks send the draft unchanged if the edit adds a number, drops the company the answer leads
with, or is not shorter; so do a timeout or a provider failure. Drafts under MIN_EDIT_WORDS are left as they are.
"""

import json
import re
import time

from app.config import SEED
from app.llm import DeadlineExceeded, ProviderError, chat
from app.numbers import SOURCES_RE, body, entities_in, first_sentence, ungrounded_numbers

MIN_EDIT_WORDS = 120  # shorter drafts (most lookups) are sent as they are
MAX_EDIT_S = 20  # slowest edit seen in the trial: 9.6s (one outlier spent minutes in retries)
MIN_TIME_LEFT_S = 8  # skip the edit when the agent's time budget is nearly used up
THINK_RE = re.compile(r"<think>.*?</think>", re.S)

EDIT_SYSTEM = """You edit a draft answer from a financial research assistant so an analyst can read it quickly.
The draft is your only source: you have no documents and must not add anything.
- Keep every specific thing the draft names that bears on the question: each risk, cause, driver, product,
  segment, region, company, figure and caveat. These are the facts; never drop or generalise one ("natural
  disasters and public health issues" must not become "disruptions"). If unsure whether one matters, keep it.
- Keep every conclusion or characterisation that answers the question, in the draft's own words: what something
  is for the company (for example a growth driver, higher-margin, recurring), the main reason for a change, and
  the verdict of a comparison or cross-check.
- Cut the explanation around them: legal consequences ("could materially adversely affect..."), mechanism,
  background, examples beyond the first, hedging, and anything said twice.
- First sentence: the direct answer. Then one bullet per point, each one line (about 25 words at most) that is
  mostly the named things and their figures. Keep tables if the draft has them.
- Cut: restating the question, describing steps or tools, section headings, closing summaries.
- Copy numbers exactly as the draft writes them. Add no new numbers, facts, or claims.
- Keep short inline page references such as (p.10) where the draft has them.
- Do not write a Sources line.
First list every distinct point the draft makes that bears on the question (facts and conclusions), one short
phrase each, then write the edited answer so that it covers every listed point.
Return JSON: {"points": ["...", "..."], "answer": "<edited answer>"}"""

PAGE_REF_RE = re.compile(r"\b(?:pp?\.|pages?)\s*\d+(?:\s*[-–]\s*\d+)?|\b10\W?K\b", re.I)


def sources_line(answer: str) -> str:
    m = None
    for m in SOURCES_RE.finditer(answer):
        pass
    return answer[m.start():].strip() if m else ""


def guard(question: str, draft: str, edited: str) -> tuple[str, str | None]:
    """(answer to send, reason the edit was rejected or None). Any failed check sends the draft unchanged."""
    if not edited:
        return draft, "empty"
    _, new_nums = ungrounded_numbers(PAGE_REF_RE.sub("", edited), [PAGE_REF_RE.sub("", draft)])
    if new_nums:
        return draft, f"new numbers {new_nums[:4]}"
    # the company the draft leads with (unless the question already names it) must stay in the first sentence
    lost = set(entities_in(first_sentence(draft))[:1]) - set(entities_in(first_sentence(edited))) - set(entities_in(question))
    if lost:
        return draft, f"first sentence lost {sorted(lost)}"
    if len(edited.split()) >= len(body(draft).split()):
        return draft, "not shorter"
    src = sources_line(draft)
    return edited + ("\n\n" + src if src else ""), None


def edit(question: str, draft: str, model: str, deadline: float | None = None) -> dict | None:
    """None if the draft is short enough to send as it is (no call made), else
    {"answer", "fallback" (reason the draft was kept, or None), "points", "usage", "ms"}."""
    if len(body(draft).split()) < MIN_EDIT_WORDS:
        return None
    t = time.time()
    out = {"answer": draft, "fallback": None, "points": [], "usage": None}
    if deadline is not None and deadline - t < MIN_TIME_LEFT_S:
        return {**out, "fallback": "no time left", "ms": 0}
    try:
        resp = chat(model=model, messages=[{"role": "system", "content": EDIT_SYSTEM},
                                           {"role": "user", "content": f"Question: {question}\n\nDraft answer:\n{body(draft).strip()}"}],
                    temperature=0.0, seed=SEED, max_tokens=4096, reasoning_effort="low",
                    response_format={"type": "json_object"},
                    deadline=min(deadline or float("inf"), t + MAX_EDIT_S))
    except (DeadlineExceeded, ProviderError) as e:  # the edit is optional: send the draft
        return {**out, "fallback": type(e).__name__, "ms": int((time.time() - t) * 1000)}
    out["usage"] = resp.usage
    text = THINK_RE.sub("", resp.choices[0].message.content or "")
    try:
        obj = json.loads(text[text.find("{"): text.rfind("}") + 1])
        edited, out["points"] = body(str(obj["answer"])).strip(), list(obj.get("points") or [])
    except (ValueError, KeyError, TypeError):
        edited = ""
    out["answer"], out["fallback"] = guard(question, draft, edited)
    return {**out, "ms": int((time.time() - t) * 1000)}
