"""Check candidate judge models against the human grades in eval/human_grades.json.

  python -m eval.calibrate_judge [--judges kimi-k3,deepseek-v4p1-flash]

Each judge grades the same saved answers; we report how often its pass/fail matches the human's
(human "partial" counts as not passing) and what it cost. Writes results/<run>/judge_calibration.md.
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor

from eval.graders import grade
from eval.run_eval import EVAL_DIR, RESULTS_DIR, ensure_facts, load_set, read_jsonl, short

M = "accounts/fireworks/models/"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--judges", default="kimi-k3,deepseek-v4p1-flash")
    a = ap.parse_args()

    human = json.loads((EVAL_DIR / "human_grades.json").read_text())
    grades = {k: v for k, v in human["grades"].items() if v["grade"]}
    if missing := [k for k, v in human["grades"].items() if not v["grade"]]:
        raise SystemExit(f"Hand grades missing for: {', '.join(missing)}")
    run_dir = RESULTS_DIR / human["run_id"]
    questions = {q["id"]: q for q in load_set("dev")}
    answers = [x for x in read_jsonl(run_dir / "answers.jsonl") if x["id"] in grades and x["run"] == 0]
    facts, _ = ensure_facts(list(questions.values()))

    table, summary = {}, []
    for judge in [M + j for j in a.judges.split(",")]:
        if any(x["model"] == judge for x in answers):
            print(f"skipping {short(judge)}: it wrote these answers")
            continue
        with ThreadPoolExecutor(4) as pool:
            results = list(pool.map(lambda x: grade(questions[x["id"]], x["result"], judge, facts), answers))
        cost = sum((r["judge_usage"] or {}).get("cost_usd", 0.0) for r in results)
        agree = 0
        for x, r in zip(answers, results):
            match = r["pass"] == (grades[x["id"]]["grade"] == "pass")
            agree += match
            table.setdefault(x["id"], {})[short(judge)] = (r["pass"], r["score"], match, r["reason"])
        summary.append((short(judge), agree, len(answers), cost))
        print(f"{short(judge)}: agrees with human on {agree}/{len(answers)}, judge cost ${cost:.4f}")

    names = [s[0] for s in summary]
    md = [f"# Judge calibration: {human['run_id']}", "", "| Judge | Agreement with human (pass/fail) | Cost |",
          "|---|---|---|", *[f"| {j} | {k}/{n} | ${c:.4f} |" for j, k, n, c in summary], "",
          "| id | grader | human | " + " | ".join(names) + " |", "|---|---|---|" + "---|" * len(names)]
    for qid in sorted(table):
        cells = [f"{'pass' if p else 'fail'} ({s:.2f}){'' if m else ' ⚠️'}" for p, s, m, _ in
                 (table[qid][j] for j in names)]
        md.append(f"| {qid} | {questions[qid]['evaluation']} | {grades[qid]['grade']} | " + " | ".join(cells) + " |")
    md += ["", "## Judge reasons where it disagrees with the human", ""]
    for qid in sorted(table):
        for j in names:
            p, s, m, reason = table[qid][j]
            if not m:
                md.append(f"- **{qid} / {j}** (human: {grades[qid]['grade']}, {grades[qid]['note'] or 'no note'}): {reason}")
    (run_dir / "judge_calibration.md").write_text("\n".join(md) + "\n")
    print(f"Written {run_dir / 'judge_calibration.md'}")


if __name__ == "__main__":
    main()
