"""Can the judge catch bad answers? Plant known errors in saved good answers and check it fails them.

  python -m eval.judge_stress [--judges kimi-k3,deepseek-v4p1-flash]

The calibration in calibrate_judge.py only had passing answers, so a judge that always says "pass" would
score 10/10 there. Here each case edits one saved dev answer in a known way: planted errors (changed number,
swapped company or cause, dropped facts) must fail; harmless edits (reformatting, cutting repetition) must
still pass. Expected grades are written below, before any judge is run. Writes results/<run>/judge_stress.md.
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor

from eval.graders import grade
from eval.run_eval import EVAL_DIR, RESULTS_DIR, ensure_facts, load_set, read_jsonl, short

M = "accounts/fireworks/models/"

# replace: (old, new) pairs, every occurrence; drop: remove whole lines containing the marker.
CASES = [
    # q_012 Greater China
    {"id": "q_012", "kind": "wrong number", "expect": "fail", "replace": [("$64.38 billion", "$63.48 billion")]},
    {"id": "q_012", "kind": "swapped cause", "expect": "fail",
     "replace": [("lower net sales of iPhone, partially offset by higher net sales of Mac",
                  "lower net sales of Mac, partially offset by higher net sales of iPhone")]},
    {"id": "q_012", "kind": "dropped facts", "expect": "fail", "drop": ["**Why (per the 10-K"]},
    {"id": "q_012", "kind": "harmless: cut extra context", "expect": "pass",
     "drop": ["Greater China was the only one", "second consecutive annual decline"]},
    # q_006 Apple supply-chain risks
    {"id": "q_006", "kind": "dropped facts", "expect": "fail",
     "drop": ["**Trade restrictions, tariffs", "**Business interruptions"]},
    {"id": "q_006", "kind": "contradiction", "expect": "fail",
     "replace": [("single/limited-source component supply", "component supply (all components are multi-sourced)"),
                 ("Certain components come from single or limited sources, and even multi-source components are",
                  "Apple states that all of its components are available from multiple sources, though they are"),
                 ("because Apple relies on single or limited sources for many critical components, an interruption "
                  "affecting those sources would exacerbate the consequences",
                  "although Apple's multi-sourcing limits the consequences"),
                 ("custom components available from only one source", "custom components")]},
    # q_022 largest revenue increase
    {"id": "q_022", "kind": "wrong company", "expect": "fail",
     "replace": [("Alphabet (GOOGL) saw the largest", "Microsoft (MSFT) saw the largest")]},
    {"id": "q_022", "kind": "wrong number", "expect": "fail", "replace": [("$52.8 billion", "$58.2 billion")]},
    {"id": "q_022", "kind": "dropped facts", "expect": "fail",
     "replace": [(" — ahead of Microsoft's +$36.6 billion and Apple's +$25.1 billion", "")],
     "drop": ["For comparison, Microsoft's"]},
    {"id": "q_022", "kind": "harmless: cut repetition", "expect": "pass", "drop": ["For comparison, Microsoft's"]},
    # q_025 Apple Services vs iPhone
    {"id": "q_025", "kind": "wrong number", "expect": "fail", "replace": [("13.5%", "15.3%")]},
    {"id": "q_025", "kind": "dropped facts", "expect": "fail", "drop": ["**Strategic importance per the 10-K:**"]},
    {"id": "q_025", "kind": "reversed comparison", "expect": "fail",
     "replace": [("far outpacing iPhone growth", "trailing iPhone growth")]},
    # q_017 Google Services / YouTube ads
    {"id": "q_017", "kind": "wrong number", "expect": "fail",
     "replace": [("$40.4 billion", "$44.0 billion"), ("$40,367 million", "$44,037 million")]},
    {"id": "q_017", "kind": "dropped facts", "expect": "fail",
     "replace": [("Google advertising plus Google subscriptions, platforms, and devices", "Google advertising")],
     "drop": ["Google Network — revenues", "**Google subscriptions, platforms, and devices**"]},
    {"id": "q_017", "kind": "wrong growth rate", "expect": "fail", "replace": [("11.7%", "17.1%")]},
    {"id": "q_017", "kind": "harmless: other units", "expect": "pass",
     "replace": [("YouTube ads revenue grew $4.2 billion (11.7%) from $36.1 billion in FY2024 to $40.4 billion",
                  "YouTube ads revenue grew $4,220 million (11.7%) from $36,147 million in FY2024 to $40,367 million")]},
    # q_014 Microsoft segments
    {"id": "q_014", "kind": "wrong number", "expect": "fail", "replace": [("$106.3 billion", "$103.6 billion")]},
    {"id": "q_014", "kind": "dropped facts", "expect": "fail",
     "replace": [(", and More Personal Computing ($54.6 billion)", "")], "drop": ["**More Personal Computing —"]},
    # entity questions
    {"id": "q_011", "kind": "wrong company", "expect": "fail",
     "replace": [("Alphabet (GOOGL) had the fastest revenue growth", "Microsoft (MSFT) had the fastest revenue growth")]},
    {"id": "q_018", "kind": "wrong company", "expect": "fail",
     "replace": [("Alphabet (GOOGL) has the highest", "Microsoft (MSFT) has the highest")]},
    # added after the v1/v2 comparison: a correct winner followed by the runners-up must still pass
    {"id": "q_018", "kind": "harmless: runners-up in opening", "expect": "pass",
     "replace": [("Alphabet (GOOGL) has the highest current ratio in FY2025, at 2.01.",
                  "**Alphabet (GOOGL) has the highest current ratio in FY2025 at 2.01**, well above Microsoft's 1.35, "
                  "while Apple's ratio is below 1.0 at 0.89.")]},
    {"id": "q_011", "kind": "harmless: runners-up in opening", "expect": "pass",
     "replace": [("at 15.1% (FY2024 → FY2025).", "at 15.1% (FY2024 → FY2025), narrowly ahead of Microsoft (14.9%) "
                  "and well ahead of Apple (6.4%).")]},
    # numeric questions, added with the headline-figure judge (outside review: a wrong headline passed when the right
    # number appeared elsewhere as a comparison)
    {"id": "q_001", "kind": "wrong headline, right number as comparison", "expect": "fail",
     "replace": [("was **$416.2 billion**.", "was **$391.0 billion**, down from $416.2 billion a year earlier.")]},
    {"id": "q_001", "kind": "harmless: comparison added", "expect": "pass",
     "replace": [("was **$416.2 billion**.", "was **$416.2 billion**, up from $391.0 billion in fiscal year 2024.")]},
    {"id": "q_008", "kind": "wrong headline, gold as the remainder", "expect": "fail",
     "replace": [("51.3% of Microsoft's total revenue came from the United States", "48.7% of Microsoft's total revenue "
                  "came from the United States"), ("The remaining 48.7% ($137.2 billion)", "The remaining 51.3% ($137.2 billion)")]},
    {"id": "q_008", "kind": "wrong unit", "expect": "fail",
     "replace": [("51.3% of Microsoft's total revenue came from the United States",
                  "$51.3 billion of Microsoft's total revenue came from the United States")]},
    {"id": "q_011", "kind": "runners-up, wrong winner", "expect": "fail",
     "replace": [("Alphabet (GOOGL) had the fastest revenue growth between its two most recent fiscal years, at 15.1% "
                  "(FY2024 → FY2025).", "Microsoft (MSFT) had the fastest revenue growth between its two most recent "
                  "fiscal years, at 14.9%, narrowly ahead of Alphabet (15.1%) and Apple (6.4%).")]},
]


def apply(answer: str, case: dict) -> str:
    for old, new in case.get("replace", []):
        if old not in answer:
            raise ValueError(f"{case['id']} {case['kind']}: text not found: {old[:60]!r}")
        answer = answer.replace(old, new)
    for marker in case.get("drop", []):
        lines = answer.splitlines()
        if not any(marker in l for l in lines):
            raise ValueError(f"{case['id']} {case['kind']}: no line contains {marker!r}")
        answer = "\n".join(l for l in lines if marker not in l)
    return answer


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="20261104-2305_dev_glm-5p3")
    ap.add_argument("--judges", default="kimi-k3,deepseek-v4p1-flash")
    a = ap.parse_args()

    run_dir = RESULTS_DIR / a.run
    questions = {q["id"]: q for q in load_set("dev")}
    saved = {x["id"]: x for x in read_jsonl(run_dir / "answers.jsonl") if x["run"] == 0}
    facts, _ = ensure_facts(list(questions.values()))
    edited = [{**saved[c["id"]]["result"], "answer": apply(saved[c["id"]]["result"]["answer"], c)} for c in CASES]

    names, rows = [], [[] for _ in CASES]
    md_sum = ["| Judge | Planted errors caught | Harmless edits passed | Cost |", "|---|---|---|---|"]
    for judge in [M + j for j in a.judges.split(",")]:
        if any(x["model"] == judge for x in saved.values()):
            print(f"skipping {short(judge)}: it wrote these answers")
            continue
        with ThreadPoolExecutor(4) as pool:
            results = list(pool.map(lambda ce: grade(questions[ce[0]["id"]], ce[1], judge, facts, faith=False),
                                    zip(CASES, edited)))
        cost = sum((r["judge_usage"] or {}).get("cost_usd", 0.0) for r in results)
        bad = [(c, r) for c, r in zip(CASES, results) if c["expect"] == "fail"]
        ok = [(c, r) for c, r in zip(CASES, results) if c["expect"] == "pass"]
        caught = sum(not r["pass"] for _, r in bad)
        kept = sum(r["pass"] for _, r in ok)
        names.append(short(judge))
        for row, r in zip(rows, results):
            row.append(r)
        md_sum.append(f"| {short(judge)} | {caught}/{len(bad)} | {kept}/{len(ok)} | ${cost:.4f} |")
        print(f"{short(judge)}: caught {caught}/{len(bad)} planted errors, passed {kept}/{len(ok)} harmless edits, ${cost:.4f}")

    md = [f"# Judge stress test: {a.run}", "",
          "Known edits to saved good answers. Planted errors must fail; harmless edits must pass.", "", *md_sum, "",
          "| id | edit | expected | " + " | ".join(names) + " |", "|---|---|---|" + "---|" * len(names)]
    for c, row in zip(CASES, rows):
        cells = []
        for r in row:
            right = (not r["pass"]) if c["expect"] == "fail" else r["pass"]
            cells.append(f"{'pass' if r['pass'] else 'fail'} ({r['score']:.2f}){'' if right else ' ⚠️'}")
        md.append(f"| {c['id']} | {c['kind']} | {c['expect']} | " + " | ".join(cells) + " |")
    md += ["", "## Judge reasons where it got the case wrong", ""]
    for c, row in zip(CASES, rows):
        for j, r in zip(names, row):
            if r["pass"] == (c["expect"] == "fail"):
                md.append(f"- **{c['id']} {c['kind']} / {j}**: {r['reason'][:400]}")
    (run_dir / "judge_stress.md").write_text("\n".join(md) + "\n")
    print(f"Written {run_dir / 'judge_stress.md'}")


if __name__ == "__main__":
    main()
