"""A readable page of a run's answers: question, gold answer, the system's answer, its grade and flags.

  python -m eval.answers_report --run <run_id>

Writes results/<run_id>/answers.md (no LLM calls). Failed answers come first.
"""

import argparse
import json

from eval.run_eval import RESULTS_DIR, load_set, read_jsonl


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    write(ap.parse_args().run)


def write(run_id: str) -> None:
    run_dir = RESULTS_DIR / run_id
    meta = json.loads((run_dir / "meta.json").read_text())
    questions = {q["id"]: q for q in load_set(meta["set"])}
    scores = {(s["id"], s["run"]): s for s in read_jsonl(run_dir / "scores.jsonl")}
    answers = sorted(read_jsonl(run_dir / "answers.jsonl"),
                     key=lambda x: (scores[(x["id"], x["run"])]["pass"], x["id"], x["run"]))
    n_pass = sum(s["pass"] for s in scores.values())
    md = [f"# Answers: {run_id}", "", f"{n_pass}/{len(scores)} passed. Failed answers first. "
          f"Scorecard: [scorecard.md](scorecard.md).", ""]
    for x in answers:
        q, s, r = questions[x["id"]], scores[(x["id"], x["run"])], x["result"]
        f = s.get("faithfulness") or {}
        flags = "; ".join(f"{c['verdict']}: {c['claim']}" for c in f.get("flagged", [])) or "none"
        u = r["usage"]
        md += [f"## {x['id']}#{x['run']}: {'PASS' if s['pass'] else 'FAIL'} ({q['evaluation']}, level {q.get('level')})", "",
               f"**Question:** {q['question']}", ""]
        if q.get("history"):
            md += [f"*Follow-up to:* {q['history'][0]['content']}", ""]
        md += [f"**Gold:** {q['gold_answer']}", "", f"**Grade:** {s['reason']}", "",
               f"**Claims the tools did not back:** {flags}", "",
               f"*{u['tool_calls']} tool calls, {u['latency_ms'] / 1000:.1f}s, ${u['cost_usd']:.4f}*", "",
               "**Answer:**", "", r["answer"], "", "---", ""]
    (run_dir / "answers.md").write_text("\n".join(md) + "\n")
    print(f"Written {run_dir / 'answers.md'}")


if __name__ == "__main__":
    main()
