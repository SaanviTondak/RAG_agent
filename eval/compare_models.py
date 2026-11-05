"""One table comparing graded runs of different answer models on the same question set.

  python -m eval.compare_models RUN_ID [RUN_ID ...]

Per model: pass rate with 95% CI, pass by grader, fact coverage, routing / grounding problems, length,
latency, cost, and which questions it failed. Writes results/model_comparison_<timestamp>.md.
"""

import argparse
import json
import statistics
from collections import defaultdict
from datetime import datetime

from eval.run_eval import RESULTS_DIR, load_set, pct, percentile, read_jsonl, short, wilson

GRADERS = ["fuzzy_numeric", "exact_match_entity", "llm_judge", "out_of_scope"]


def summarize(run_id: str, qs: dict) -> dict:
    d = RESULTS_DIR / run_id
    meta = json.loads((d / "meta.json").read_text())
    answers = {(a["id"], a["run"]): a["result"] for a in read_jsonl(d / "answers.jsonl")}
    scores = [s for s in read_jsonl(d / "scores.jsonl") if s["id"] in qs]
    res = [answers[(s["id"], s["run"])] for s in scores]
    n, k = len(scores), sum(s["pass"] for s in scores)
    by = defaultdict(list)
    for s in scores:
        by[qs[s["id"]]["evaluation"]].append(s["pass"])
    judged = [s["score"] for s in scores if qs[s["id"]]["evaluation"] == "llm_judge"]
    lat = [r["usage"]["latency_ms"] / 1000 for r in res]
    return {
        "model": short(meta["model"]), "judge": short(meta["judge"]), "run": run_id, "n": n, "k": k,
        "ci": wilson(k, n), "by": {g: (sum(v), len(v)) for g, v in by.items()},
        "coverage": statistics.mean(judged) if judged else None,
        "routing_miss": sum(1 for s in scores if s["routing"] and not s["routing"]["ok"]),
        "ungrounded": sum(1 for s in scores if s["grounding"] and not s["grounding"]["ok"]),
        "bad_cites": sum(len(s["citations"]["invalid"]) for s in scores if s["citations"]),
        "fallbacks": sum(any(t["type"] == "fallback" for t in r["trace"]) for r in res),
        "tools": statistics.mean(r["usage"]["tool_calls"] for r in res),
        "words": percentile([s["words"] for s in scores if s.get("words") is not None], .5),
        "p50": percentile(lat, .5), "p95": percentile(lat, .95),
        "usd": sum(r["usage"]["cost_usd"] for r in res),
        "failed": sorted(s["id"] for s in scores if not s["pass"]),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs", nargs="+")
    a = ap.parse_args()
    qs = {q["id"]: q for q in load_set("tune")}
    rows = sorted((summarize(r, qs) for r in a.runs), key=lambda x: (-x["k"], x["usd"]))

    md = [f"# Answer-model comparison ({len(qs)} tune questions, prompt v1)", "",
          "| Model | Passed | 95% CI | " + " | ".join(GRADERS) + " | Fact coverage (llm_judge) | Judge |",
          "|---|---|---|" + "---|" * len(GRADERS) + "---|---|"]
    for r in rows:
        lo, hi = r["ci"]
        cells = [f"{r['by'][g][0]}/{r['by'][g][1]}" if g in r["by"] else "-" for g in GRADERS]
        md.append(f"| {r['model']} | **{r['k']}/{r['n']}** | {pct(lo)}–{pct(hi)} | " + " | ".join(cells) +
                  f" | {r['coverage']:.2f} | {r['judge']} |")
    md += ["", "| Model | Latency p50 / p95 | Cost per answer | Cost (32 q) | Tool calls / q | Median words | "
           "Missing source | Ungrounded numbers | Invalid citations | Fallbacks |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['model']} | {r['p50']:.1f}s / {r['p95']:.1f}s | ${r['usd'] / r['n']:.4f} | ${r['usd']:.2f} | "
                  f"{r['tools']:.1f} | {r['words']:.0f} | {r['routing_miss']} | {r['ungrounded']} | {r['bad_cites']} | "
                  f"{r['fallbacks']} |")
    md += ["", "## Failed questions", ""]
    md += [f"- **{r['model']}**: {', '.join(r['failed']) or 'none'}" for r in rows]
    fails = defaultdict(list)
    for r in rows:
        for i in r["failed"]:
            fails[i].append(r["model"])
    md += ["", "## Questions failed by more than one model", ""]
    md += [f"- {i} ({qs[i]['evaluation']}): {', '.join(m)}" for i, m in sorted(fails.items(), key=lambda x: -len(x[1]))
           if len(m) > 1] or ["- none"]
    md += ["", "Runs: " + ", ".join(f"`{r['run']}`" for r in rows)]
    path = RESULTS_DIR / f"model_comparison_{datetime.now():%Y%m%d-%H%M}.md"
    path.write_text("\n".join(md) + "\n")
    print("\n".join(md))
    print(f"\nWritten {path}")


if __name__ == "__main__":
    main()
