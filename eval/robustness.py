"""Would the results hold under other reasonable graders? Re-score saved answers several ways (no agent cost).

  python -m eval.robustness --runs <run_id>[,<run_id>...] [--second-judge kimi-k3] [--noise 2] [--holistic]

Fireworks names its graders but does not publish them, so one definition of "correct" is not enough. For each
saved, graded answer this reports pass/fail under:
- ours: the scorecard grade (scores.jsonl);
- strict: the number must be in the first sentence; the company must be named in the first sentence; every
  checklist fact covered (instead of 80%);
- lenient: 60% of checklist facts (no contradiction);
- holistic (--holistic): one verdict against the whole reference answer (llm_judge questions);
- second judge (--second-judge): the same graders with another judge model (judge-graded questions);
- judge noise (--noise N): the same judge on the same answer N more times; how many verdicts change.
Writes results/robustness_<ts>.md and .jsonl.
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from eval.graders import PASS_COVERAGE, grade_answer, holistic_judge
from eval.judge_stress import M
from eval.run_eval import RESULTS_DIR, ensure_facts, load_set, read_jsonl, short

JUDGED = ("llm_judge", "exact_match_entity", "out_of_scope")


def coverage_pass(s: dict, threshold: float) -> bool:
    verdicts = [str(f.get("verdict", "")).lower() for f in s["details"].get("facts", [])]
    return s["score"] >= threshold and "contradicted" not in verdicts


def strict(q: dict, s: dict) -> bool:
    d = s.get("details") or {}
    if q["evaluation"] == "fuzzy_numeric":
        return bool(d.get("first_sentence_pass"))
    if q["evaluation"] == "exact_match_entity":
        return s["pass"] and bool(d.get("string_check_ok"))
    if q["evaluation"] == "llm_judge":
        return coverage_pass(s, 1.0)
    return s["pass"]


def lenient(q: dict, s: dict) -> bool:
    return coverage_pass(s, 0.6) if q["evaluation"] == "llm_judge" else s["pass"]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True, help="comma-separated graded run ids")
    ap.add_argument("--first-run-only", action="store_true", help="only answers with run index 0 (cheaper)")
    ap.add_argument("--holistic", action="store_true")
    ap.add_argument("--second-judge", help="e.g. kimi-k3")
    ap.add_argument("--noise", type=int, default=0, help="extra gradings by the run's own judge")
    a = ap.parse_args()

    questions = {q["id"]: q for s in ("tune", "holdout") for q in load_set(s)}
    rows = []
    for rid in a.runs.split(","):
        meta = json.loads((RESULTS_DIR / rid / "meta.json").read_text())
        answers = {(x["id"], x["run"]): x for x in read_jsonl(RESULTS_DIR / rid / "answers.jsonl")}
        for s in read_jsonl(RESULTS_DIR / rid / "scores.jsonl"):
            if a.first_run_only and s["run"]:
                continue
            ans = answers[(s["id"], s["run"])]
            rows.append({"run_id": rid, "id": s["id"], "run": s["run"], "judge": meta["judge"],
                         "answer_model": ans["model"], "answer": ans["result"]["answer"], "score": s})
    facts, _ = ensure_facts([questions[r["id"]] for r in rows])
    second = M + a.second_judge if a.second_judge else None
    if second and any(r["answer_model"] == second for r in rows):
        raise SystemExit(f"{a.second_judge} wrote some of these answers; pick another second judge")

    def work(r):
        q, s = questions[r["id"]], r["score"]
        out = {"run_id": r["run_id"], "id": r["id"], "run": r["run"], "evaluation": q["evaluation"],
               "ours": s["pass"], "strict": strict(q, s), "lenient": lenient(q, s), "usd": 0.0}

        def judged(g):
            out["usd"] += (g["judge_usage"] or {}).get("cost_usd", 0.0)
            return g["pass"]
        try:
            if a.holistic:
                out["holistic"] = judged(holistic_judge(q["question"], r["answer"], q["gold_answer"], r["judge"])) \
                    if q["evaluation"] == "llm_judge" else s["pass"]
            if second:
                out["second_judge"] = judged(grade_answer(q, r["answer"], second, facts)) \
                    if q["evaluation"] in JUDGED else s["pass"]
            if a.noise and q["evaluation"] in JUDGED:
                out["noise"] = [judged(grade_answer(q, r["answer"], r["judge"], facts)) for _ in range(a.noise)]
        except Exception as e:  # noqa: BLE001 - recorded, not fatal
            out["error"] = f"{type(e).__name__}: {e}"
        return out

    with ThreadPoolExecutor(4) as pool:
        res = list(pool.map(work, rows))

    stamp = f"{datetime.now():%Y%m%d-%H%M}"
    with open(RESULTS_DIR / f"robustness_{stamp}.jsonl", "w") as f:
        for r in res:
            f.write(json.dumps(r) + "\n")
    defs = ["ours", "strict", "lenient"] + (["holistic"] if a.holistic else []) + (["second_judge"] if second else [])
    labels = {"ours": f"ours (scorecard; {PASS_COVERAGE:.0%} of facts)", "strict": "strict (first sentence; 100% of facts)",
              "lenient": "lenient (60% of facts)", "holistic": "holistic judge (whole reference)",
              "second_judge": f"second judge ({a.second_judge})"}
    md = [f"# Grader robustness: {a.runs}", "", f"{len(res)} answers" + (" (run 0 only)" if a.first_run_only else "")
          + f"; judge `{short(rows[0]['judge'])}`; cost ${sum(r['usd'] for r in res):.3f}.", "",
          "| Definition | Passed | Changed vs ours | Answers that change |", "|---|---|---|---|"]
    for d in defs:
        ok = [r for r in res if d in r and "error" not in r]
        flips = [f"{r['id']}#{r['run']} ({'pass' if r[d] else 'fail'})" for r in ok if r[d] != r["ours"]]
        md.append(f"| {labels[d]} | {sum(r[d] for r in ok)}/{len(ok)} | {len(flips)} | {', '.join(flips) or '-'} |")
    if a.noise:
        noisy = [r for r in res if "noise" in r]
        changed = [f"{r['id']}#{r['run']}" for r in noisy if any(v != r["ours"] for v in r["noise"])]
        md += ["", f"**Judge noise:** {len(noisy)} judge-graded answers graded {a.noise} more times by the same judge; "
               f"{len(changed)} changed verdict at least once" + (f": {', '.join(changed)}" if changed else "") + "."]
    errors = [f"{r['id']}#{r['run']}: {r['error']}" for r in res if "error" in r]
    if errors:
        md += ["", "Grader errors (excluded above): " + "; ".join(errors)]
    (RESULTS_DIR / f"robustness_{stamp}.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
