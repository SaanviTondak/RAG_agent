"""Turn a run made with the answer editor into the same run without it: the unedited drafts become the answers.

  python -m eval.without_editor --run <run_id>

Every answer in an editor run keeps its draft, and the scorecard already graded the drafts, so no agent call is
needed. The main grade is redone on each draft to keep its fact-by-fact details (one cheap judge call; the
judge gave the same verdicts in 57/57 repeat gradings); the opening-paragraph and faithfulness grades are
copied; citations and number grounding are recomputed (no LLM). Writes results/<run_id>_noedit/. Token counts,
cost and latency still include the editor call (use a run made without the editor for those).
"""

import argparse
import json
from datetime import datetime

from eval.graders import citation_check, grade_answer, grounding_check
from eval.run_eval import RESULTS_DIR, ensure_facts, load_set, read_jsonl, scorecard


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    a = ap.parse_args()

    src = RESULTS_DIR / a.run
    meta = json.loads((src / "meta.json").read_text())
    questions = {q["id"]: q for q in load_set(meta["set"])}
    facts, _ = ensure_facts(list(questions.values()))
    scores = {(s["id"], s["run"]): s for s in read_jsonl(src / "scores.jsonl")}
    out = RESULTS_DIR / f"{a.run}_noedit"
    out.mkdir(exist_ok=True)
    answers, new_scores, regraded = [], [], 0
    for rec in read_jsonl(src / "answers.jsonl"):
        r, s = rec["result"], dict(scores[(rec["id"], rec["run"])])
        if r.get("draft"):
            r = {**r, "answer": r["draft"], "draft": None, "editor": False,
                 "trace": [t for t in r["trace"] if t["type"] != "edit"]}
            g = grade_answer(questions[rec["id"]], r["answer"], meta["judge"], facts)
            d = s.pop("draft")
            s.update(g, words=d["words"], lead=d["lead"], faithfulness=d["faithfulness"],
                     citations=citation_check(r), grounding=grounding_check(r))
            regraded += 1
        else:
            r = {**r, "editor": False, "trace": [t for t in r["trace"] if t["type"] != "edit"]}
        answers.append({**rec, "editor": False, "result": r})
        new_scores.append(s)
    for name, rows in (("answers.jsonl", answers), ("scores.jsonl", new_scores)):
        with open(out / name, "w") as f:
            for row in rows:
                f.write(json.dumps(row) + "\n")
    meta = {**meta, "editor": False, "derived_from": a.run, "graded_at": f"{datetime.now():%Y-%m-%d %H:%M}"}
    (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    md = scorecard(list(questions.values()), out, new_scores, meta, None)
    md = md.replace("\n## Headline", f"\nDerived from `{a.run}` with the editor removed (drafts as answers; "
                                    "cost and latency include the editor call).\n\n## Headline", 1)
    (out / "scorecard.md").write_text(md)
    print(f"{regraded} drafts regraded; {sum(s['pass'] for s in new_scores)}/{len(new_scores)} passed. Written {out}")


if __name__ == "__main__":
    main()
