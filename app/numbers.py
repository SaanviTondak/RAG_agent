"""Numbers in text, compared at their written precision. Shared by the agent (grounding nudge) and the eval."""

import re
from decimal import Decimal

SCALES = {"trillion": 1e12, "tn": 1e12, "t": 1e12, "billion": 1e9, "bn": 1e9, "b": 1e9,
          "million": 1e6, "mn": 1e6, "mm": 1e6, "m": 1e6, "thousand": 1e3, "k": 1e3}
NUM_RE = re.compile(
    r"(?<![\w.])(?!\d+-K\b)([-−]?)\$?\s?(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?"
    r"(?:\s?(%|percent\b|percentage points?\b|pp\b|x\b|trillion\b|billion\b|million\b|thousand\b"
    r"|tn\b|bn\b|mn\b|mm\b|[tbmk]\b))?", re.I)
ABBREVIATIONS = re.compile(r"\b(U\.S|Inc|Corp|Co|Ltd|vs|approx|e\.g|i\.e|No)\.", re.I)
SOURCES_RE = re.compile(r"^\W*sources?\W*:", re.I | re.M)


def parse_numbers(text: str) -> list[dict]:
    """Every number in `text` with its written precision: '$416.2 billion' -> value 416.2e9, step 0.1e9."""
    out = []
    for m in NUM_RE.finditer(text):
        sign, whole, frac, unit = m.groups()
        value = float(whole.replace(",", "") + (frac or ""))
        step = 10.0 ** -(len(frac) - 1) if frac else 1.0
        unit = (unit or "").lower()
        scale = SCALES.get(unit, 1.0)
        out.append({"value": -value if sign else value, "step": step, "scale": scale,
                    "pct": unit.startswith(("%", "percent", "pp")), "unit": unit,
                    "is_year": not frac and not unit and 1990 <= value <= 2035, "text": m.group(0).strip()})
    return out


def _step_of(x: float) -> float:
    exp = Decimal(str(x)).normalize().as_tuple().exponent
    return 10.0 ** min(exp, 0)


def numbers_agree(a: float, a_step: float, b: float, b_step: float) -> bool:
    """Equal once both are rounded to the coarser of the two precisions (sign ignored: 'fell 3.8%' = -3.8)."""
    return abs(abs(a) - abs(b)) <= max(a_step, b_step) / 2 * (1 + 1e-9) + 1e-9 * max(abs(b), 1)


def number_matches(n: dict, gold: float) -> bool:
    """Gold may be raw (416161000000) or already in the answer's unit (66.95 for '$66.95 billion')."""
    g_step = _step_of(gold)
    return (numbers_agree(n["value"] * n["scale"], n["step"] * n["scale"], gold, g_step)
            or numbers_agree(n["value"], n["step"], gold, g_step))


def body(answer: str) -> str:
    """The answer without its trailing Sources: line(s)."""
    m = None
    for m in SOURCES_RE.finditer(answer):
        pass
    return answer[: m.start()] if m else answer


TOOL_MULTIPLIERS = (1.0, 100.0, 1e3, 1e6, 1e9, 1e12)  # filing tables are in millions; ratios may become %
DATE_RE = re.compile(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)"
                     r"\s+\d{1,2}\b(?:,\s*\d{4})?")


def ungrounded_numbers(answer: str, tool_texts: list[str], percentages_only: bool = False) -> tuple[int, list[str]]:
    """Numbers in the answer that don't appear (to the answer's precision) in any tool output.

    Skips years, dates, small counts (<10, no unit), and the Sources line. A hit means the model probably
    did arithmetic in its head or invented a figure. Returns (numbers checked, ungrounded texts).
    """
    parsed = [n for t in tool_texts for n in parse_numbers(t)]
    tool_nums = [(n["value"] * n["scale"], n["step"] * n["scale"]) for n in parsed]
    tool_nums += [(n["value"], n["step"]) for n in parsed if n["scale"] != 1.0]
    checked, ungrounded = 0, []
    for n in parse_numbers(DATE_RE.sub("", re.sub(r"\[[^\]]*\]", "", body(answer)))):
        if n["is_year"] or (n["step"] == 1.0 and not n["unit"] and abs(n["value"]) < 10):
            continue
        if percentages_only and not n["pct"]:
            continue
        checked += 1
        a, a_step = n["value"] * n["scale"], n["step"] * n["scale"]
        if not any(numbers_agree(a, a_step, t * k, t_step * k) for t, t_step in tool_nums for k in TOOL_MULTIPLIERS):
            ungrounded.append(n["text"])
    return checked, ungrounded
