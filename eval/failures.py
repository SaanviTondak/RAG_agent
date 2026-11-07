"""Where does the system still fail, and why? One row per failed answer, with a suggested cause.

  python -m eval.failures --runs <run_id>[,<run_id>...] [--robustness results/robustness_<ts>.jsonl]

The cause is suggested from the trace diagnostics, in this order: grader error, tool/time budget hit, a
required source never used (routing), no gold page retrieved (retrieval), a fact contradicting the gold (wrong
fact), only some gold pages retrieved (partial retrieval), every gold page seen but the fact left out (omission),
wrong company, a figure not found in any tool output (calculation). With --robustness, answers that passed when the same judge graded them again are marked
judge-borderline. The "confirmed" column is filled in by hand after reading each answer.
Writes results/failures_<ts>.md.
"""

import argparse
import json
from collections import Counter
from datetime import datetime

from eval.run_eval import RESULTS_DIR, load_set, read_jsonl


def suggest(q: dict, s: dict, result: dict) -> str:
    if s["reason"].startswith("grader error"):
        return "grader error"
    if any(t["type"] == "fallback" for t in result["trace"]):
        return "budget: answered from partial evidence"
    if s.get("routing") and s["routing"]["missing"]:
        return f"routing: never used {', '.join(s['routing']['missing'])}"
    if s.get("recall") and not s["recall"]["hit"]:
        return "retrieval: no gold page retrieved"
    method, d = q["evaluation"], s.get("details") or {}
    if method == "llm_judge":
        if any(str(f.get("verdict", "")).lower() == "contradicted" for f in d.get("facts", [])):
            return "wrong fact (contradicts the gold)"
        rec = s.get("recall")
        if rec and rec["recall"] < 1:
            seen = round(rec["recall"] * rec["n_gold"])
            return f"partial retrieval: {seen} of {rec['n_gold']} gold pages seen, fact not in the answer"
        return "omission: every gold page seen, fact not in the answer" if rec else "omission: fact not in the answer"
    if method == "exact_match_entity" and not d.get("entity_ok", True):
        return "wrong company"
    if method in ("fuzzy_numeric", "exact_match_entity"):
        return "calculation: figure not from a tool" if s.get("grounding") and not s["grounding"]["ok"] else "wrong figure"
    if method == "out_of_scope":
        return "answered an out-of-scope question"
    return "other"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True)
    ap.add_argument("--robustness", help="robustness_<ts>.jsonl with --noise regrades")
    a = ap.parse_args()

    questions = {q["id"]: q for s in ("tune", "holdout") for q in load_set(s)}
    noise = {}
    if a.robustness:
        for r in read_jsonl(RESULTS_DIR.parent / a.robustness if "/" in a.robustness else RESULTS_DIR / a.robustness):
            noise[(r["run_id"], r["id"], r["run"])] = r.get("noise") or []
    rows, n_answers = [], 0
    for rid in a.runs.split(","):
        answers = {(x["id"], x["run"]): x["result"] for x in read_jsonl(RESULTS_DIR / rid / "answers.jsonl")}
        for s in read_jsonl(RESULTS_DIR / rid / "scores.jsonl"):
            n_answers += 1
            if s["pass"]:
                continue
            q, result = questions[s["id"]], answers[(s["id"], s["run"])]
            cause = suggest(q, s, result)
            if any(noise.get((rid, s["id"], s["run"]), [])):
                cause += " (judge-borderline: passed on a regrade)"
            rows.append({"run_id": rid, "id": s["id"], "run": s["run"], "level": q.get("level"),
                         "evaluation": q["evaluation"], "reason": s["reason"], "cause": cause})

    md = [f"# Failure analysis: {a.runs}", "", f"{len(rows)} failed answers out of {n_answers}.", "",
          "| Suggested cause | Answers |", "|---|---|"]
    md += [f"| {c} | {n} |" for c, n in Counter(r["cause"] for r in rows).most_common()]
    md += ["", "| run | id | level | grader | grader's reason | suggested cause | confirmed cause (by hand) |",
           "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["id"], r["run_id"], r["run"])):
        md.append(f"| {r['run_id'].split('_')[0]} | {r['id']}#{r['run']} | {r['level']} | {r['evaluation']} | "
                  f"{r['reason'][:220].replace('|', '/')} | {r['cause']} | |")
    out = RESULTS_DIR / f"failures_{datetime.now():%Y%m%d-%H%M}.md"
    out.write_text("\n".join(md) + "\n")
    print("\n".join(md[:8 + len(set(r['cause'] for r in rows))]))
    print(f"Written {out}")


if __name__ == "__main__":
    main()
