"""Re-apply the graders fixed after the outside review (2026-11-07) to saved runs, and list what changed.

  python -m eval.apply_grader_fixes --runs <run_id>[,<run_id>...]

Fixed: fuzzy_numeric (unit and direction must match; the judge picks the figure given as the answer) and the
number check in exact_match_entity; citation_check (every page of a cited range must have been seen). Only
those grades are redone; everything else in scores.jsonl is kept. Scorecards and answers.md are rewritten,
keeping any note above the headline. Writes results/grader_fixes_<ts>.md.
"""

import argparse
import json
from datetime import datetime

from eval import answers_report
from eval.graders import citation_check, grade_answer
from eval.run_eval import RESULTS_DIR, ensure_facts, load_set, read_jsonl, scorecard

FIXED = ("fuzzy_numeric", "exact_match_entity")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True)
    a = ap.parse_args()

    md = ["# Grader fixes re-applied to saved runs", "",
          "| run | answers | grade changed | citations invalid before -> after | details |", "|---|---|---|---|---|"]
    for rid in a.runs.split(","):
        run_dir = RESULTS_DIR / rid
        meta = json.loads((run_dir / "meta.json").read_text())
        questions = {q["id"]: q for q in load_set(meta["set"])}
        facts, _ = ensure_facts(list(questions.values()))
        answers = {(x["id"], x["run"]): x["result"] for x in read_jsonl(run_dir / "answers.jsonl")}
        scores, changed, bad_before, bad_after = [], [], 0, 0
        for s in read_jsonl(run_dir / "scores.jsonl"):
            q, r = questions[s["id"]], answers[(s["id"], s["run"])]
            if q["evaluation"] in FIXED:
                g = grade_answer(q, r["answer"], meta["judge"], facts)
                if g["pass"] != s["pass"]:
                    changed.append(f"{s['id']}#{s['run']}: {'pass' if s['pass'] else 'fail'} -> "
                                   f"{'pass' if g['pass'] else 'fail'} ({g['reason'][:120]})")
                s = {**s, **{k: g[k] for k in ("pass", "score", "reason", "details")}}
            if s.get("citations"):
                bad_before += len(s["citations"]["invalid"])
                s = {**s, "citations": citation_check(r)}
                bad_after += len(s["citations"]["invalid"])
            scores.append(s)
        with open(run_dir / "scores.jsonl", "w") as f:
            for s in scores:
                f.write(json.dumps(s) + "\n")
        old = (run_dir / "scorecard.md").read_text()
        note = "\n".join(l for l in old.split("\n## Headline")[0].splitlines()[1:] if not l.startswith("- System:"))
        card = scorecard(list(questions.values()), run_dir, scores, meta, None)
        card = card.replace("\n## Headline", note.rstrip() + "\n\nGrader fixes of 2026-11-07 applied "
                            "(eval/apply_grader_fixes.py).\n\n## Headline", 1) if note.strip() else card
        (run_dir / "scorecard.md").write_text(card)
        answers_report.write(rid)
        invalid = [f"{s['id']}#{s['run']}: {'; '.join(s['citations']['invalid'])}" for s in scores
                   if s.get("citations") and s["citations"]["invalid"]]
        md.append(f"| {rid} | {len(scores)} | {len(changed)} | {bad_before} -> {bad_after} | "
                  f"{'<br>'.join(changed + invalid) or '-'} |")
    out = RESULTS_DIR / f"grader_fixes_{datetime.now():%Y%m%d-%H%M}.md"
    out.write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
