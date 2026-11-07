"""Can the faithfulness check catch claims the tools never returned? Plant them in saved answers and see.

  python -m eval.faith_stress [--judge deepseek-v4p1-flash]

Same idea as judge_stress.py, for graders.faithfulness: each planted case adds one claim that is not in the
evidence (invented cause, wrong figure, invented metric) and must be flagged; its `marker` must appear in a
flagged claim. Harmless edits (rewording, cutting a sentence, other units) must not add flags. The unedited
answers are checked too, and their flags are listed for review by hand. Expected results are written below,
before any judge is run. Writes results/<run>/faith_stress.md.
"""

import argparse
import json
from concurrent.futures import ThreadPoolExecutor

from eval.graders import faithfulness
from eval.judge_stress import M, apply
from eval.run_eval import RESULTS_DIR, load_set, read_jsonl, short

CASES = [
    {"id": "q_012", "kind": "invented cause", "expect": "flag", "marker": "renminbi",
     "replace": [("partially offset by higher net sales of Mac.\"",
                  "partially offset by higher net sales of Mac.\" The 10-K also cites a weaker renminbi.")]},
    {"id": "q_012", "kind": "wrong figure", "expect": "flag", "marker": "25", "replace": [("Japan +15%", "Japan +25%")]},
    {"id": "q_022", "kind": "invented metric", "expect": "flag", "marker": "23.7",
     "replace": [("roughly 29.3% of the total increase.",
                  "roughly 29.3% of the total increase; Google Cloud's operating margin reached 23.7%.")]},
    {"id": "q_017", "kind": "invented driver", "expect": "flag", "marker": "shorts",
     "replace": [("both of which benefited from increased spending by advertisers.",
                  "both of which benefited from increased spending by advertisers, and to YouTube Shorts monetization "
                  "reaching parity with long-form video.")]},
    {"id": "q_001", "kind": "invented trend", "expect": "flag", "marker": "consecutive",
     "replace": [("- The figure is net sales", "- Revenue grew for the third consecutive year.\n- The figure is net sales")]},
    {"id": "q_018", "kind": "wrong input figure", "expect": "flag", "marker": "184",
     "replace": [("$148.0 billion current assets", "$184.0 billion current assets")]},
    {"id": "q_012", "kind": "harmless: rewording", "expect": "same",
     "replace": [("a decline of $2.6 billion (−3.8%", "down $2.6 billion (−3.8%")]},
    {"id": "q_022", "kind": "harmless: cut a sentence", "expect": "same",
     "replace": [("These components sum exactly to the $52.8 billion consolidated increase. ", "")]},
    {"id": "q_017", "kind": "harmless: other units", "expect": "same",
     "replace": [("Revenue rose from $36,147 million to $40,367 million",
                  "Revenue rose from $36.1 billion to $40.4 billion")]},
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="20261104-2305_dev_glm-5p3")
    ap.add_argument("--judge", default="deepseek-v4p1-flash")
    a = ap.parse_args()

    judge = M + a.judge
    run_dir = RESULTS_DIR / a.run
    questions = {q["id"]: q for q in load_set("dev")}
    saved = {x["id"]: x["result"] for x in read_jsonl(run_dir / "answers.jsonl") if x["run"] == 0}
    if any(r["model"] == judge for r in saved.values()):
        raise SystemExit(f"{a.judge} wrote these answers; pick another judge")
    jobs = [("base", i, saved[i]) for i in sorted(saved)]
    jobs += [("case", c, {**saved[c["id"]], "answer": apply(saved[c["id"]]["answer"], c)}) for c in CASES]

    def work(job):
        kind, key, result = job
        qid = key if kind == "base" else key["id"]
        return faithfulness(questions[qid]["question"], result, judge, questions[qid].get("history"))

    with ThreadPoolExecutor(4) as pool:
        out = list(pool.map(work, jobs))
    base = {key: r for (kind, key, _), r in zip(jobs, out) if kind == "base"}
    cost = sum(r["judge_usage"]["cost_usd"] for r in out if r["judge_usage"])

    md = [f"# Faithfulness stress test: {a.run}, judge `{a.judge}`", "",
          "| id | edit | expected | flags (unedited -> edited) | result |", "|---|---|---|---|---|"]
    right = 0
    for c, r in [(key, r) for (kind, key, _), r in zip(jobs, out) if kind == "case"]:
        b = base[c["id"]]
        if c["expect"] == "flag":
            ok = any(c["marker"].lower() in f["claim"].lower() for f in r["flagged"])
        else:
            ok = len(r["flagged"]) <= len(b["flagged"])
        right += ok
        md.append(f"| {c['id']} | {c['kind']} | {c['expect']} | {len(b['flagged'])} -> {len(r['flagged'])} | "
                  f"{'ok' if ok else 'WRONG'} |")
    md[1:1] = ["", f"**{right}/{len(CASES)} cases right**; ${cost:.4f}", ""]
    md += ["", "## Flags on the unedited answers (review by hand: real unsupported claims, or judge errors?)", ""]
    for i, r in base.items():
        md.append(f"- **{i}** ({r['n_claims']} claims): " + ("; ".join(f"{f['verdict']}: {f['claim']}" for f in r["flagged"])
                                                            or "none") + (" (evidence truncated)" if r["truncated"] else ""))
    (run_dir / "faith_stress.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    print(f"\nWritten {run_dir / 'faith_stress.md'}")


if __name__ == "__main__":
    main()
