"""Paired comparison of two graded runs on the same questions (e.g. prompt v1 vs v2).

  python -m eval.compare_runs A_RUN B_RUN [--prefer] [--judge M]

Per question: pass, score (fact coverage), whether the opening paragraph alone passes, length, latency,
cost. Sign tests say whether B's wins over A are more than chance. --prefer adds a blind pairwise vote:
the judge sees the reference and both answers (both orders, to cancel position bias) and picks the one
that is correct and complete first, then quickest to read. Writes results/compare_<A>__<B>.md.
"""

import argparse
import json
import math
import statistics
from concurrent.futures import ThreadPoolExecutor

from app.config import JUDGE_MODEL
from eval.graders import body, judge_json
from eval.run_eval import RESULTS_DIR, gold_ratio, load_set, percentile, read_jsonl, short

PREFER_SYSTEM = """You compare two answers from a financial research assistant to the same question. The reader is an
analyst who needs the answer quickly and must be able to trust it. A reference answer is given.
Decide in this order of priority:
1. Correctness and completeness against the reference: an answer with a wrong or missing key fact loses.
2. How quickly the reader finds the answer: is it stated up front, or buried?
3. Concise but well-supported (the customer's stated preference): the key facts with their supporting figures
   and sources, without filler, repetition, or detail the question did not ask for.
Return JSON: {"winner": "A" | "B" | "tie", "reason": "<one sentence>"}"""


def sign_test(wins: int, losses: int) -> float:
    """Two-sided exact sign test p-value (ties dropped)."""
    n = wins + losses
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(min(wins, losses) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def prefer(q: dict, ans_a: str, ans_b: str, judge: str) -> tuple[str, float]:
    """Ask twice with the answers swapped; only a consistent choice counts. Returns ('A'|'B'|'tie', cost)."""
    votes, cost = [], 0.0
    for first, second, flip in ((ans_a, ans_b, False), (ans_b, ans_a, True)):
        try:
            obj, usage = judge_json(judge, PREFER_SYSTEM,
                                    f"Question: {q['question']}\n\nReference answer: {q['gold_answer']}\n\n"
                                    f"Answer A:\n{body(first)}\n\nAnswer B:\n{body(second)}")
        except ValueError:  # unparseable vote: recorded, not fatal
            return "error", cost
        cost += usage["cost_usd"]
        w = str(obj.get("winner", "tie")).strip().upper()
        votes.append({"A": "B", "B": "A"}.get(w, "tie") if flip else (w if w in ("A", "B") else "tie"))
    return (votes[0] if votes[0] == votes[1] else "tie"), cost


def load(run_id: str) -> tuple[dict, dict, dict]:
    d = RESULTS_DIR / run_id
    meta = json.loads((d / "meta.json").read_text())
    answers = {a["id"]: a for a in read_jsonl(d / "answers.jsonl") if a["run"] == 0}
    scores = {s["id"]: s for s in read_jsonl(d / "scores.jsonl") if s["run"] == 0}
    return meta, answers, scores


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--prefer", action="store_true", help="add the blind pairwise preference vote")
    ap.add_argument("--judge", default=JUDGE_MODEL)
    args = ap.parse_args()

    (ma, aa, sa), (mb, ab, sb) = load(args.a), load(args.b)
    if args.prefer and short(args.judge) in (short(ma["model"]), short(mb["model"])):
        raise SystemExit("The preference judge must differ from both answering models; pass --judge.")
    qs = {q["id"]: q for q in load_set("tune") + load_set("holdout")}
    ids = sorted(set(sa) & set(sb))
    rows = [(qs[i], sa[i], sb[i], aa[i]["result"], ab[i]["result"]) for i in ids]

    prefs, pref_cost = {}, 0.0
    if args.prefer:
        with ThreadPoolExecutor(4) as pool:
            out = list(pool.map(lambda r: prefer(r[0], r[3]["answer"], r[4]["answer"], args.judge), rows))
        for (q, *_), (w, c) in zip(rows, out):
            prefs[q["id"]] = w
            pref_cost += c

    def side(i):  # metric -> value, for run A (i=1) or B (i=2)
        ss = [r[i] for r in rows]
        res = [r[i + 2] for r in rows]
        judged = [s for r, s in zip(rows, ss) if r[0]["evaluation"] == "llm_judge" and s.get("lead")]
        return {
            "Passed": f"{sum(s['pass'] for s in ss)}/{len(ss)}",
            "Mean score (fact coverage for llm_judge)": f"{statistics.mean(s['score'] for s in ss):.3f}",
            "Fact coverage, llm_judge questions only": f"{statistics.mean(s['score'] for s in judged):.3f}" if judged else "-",
            "Opening paragraph alone passes": f"{sum(s['lead']['pass'] for s in ss if s.get('lead'))}/{len(ss)}",
            "Opening-paragraph fact coverage (llm_judge)":
                f"{statistics.mean(s['lead']['score'] for s in judged):.3f}" if judged else "-",
            "Words: median / mean": f"{percentile([s['words'] for s in ss], .5):.0f} / "
                                    f"{statistics.mean(s['words'] for s in ss):.0f}",
            "Opening paragraph words: median": f"{percentile([s['lead']['words'] for s in ss], .5):.0f}",
            "Words ÷ gold words (llm_judge, median)":
                f"{percentile([x for r, s in zip(rows, ss) if (x := gold_ratio(r[0], s)) is not None], .5):.1f}x",
            "Latency p50 / p95": f"{percentile([r['usage']['latency_ms'] / 1000 for r in res], .5):.1f}s / "
                                 f"{percentile([r['usage']['latency_ms'] / 1000 for r in res], .95):.1f}s",
            "Agent cost per answer": f"${statistics.mean(r['usage']['cost_usd'] for r in res):.4f}",
        }

    A, B = side(1), side(2)

    def paired(f):
        up = sum(f(r[2]) > f(r[1]) for r in rows)
        down = sum(f(r[2]) < f(r[1]) for r in rows)
        return up, down, len(rows) - up - down, sign_test(up, down)

    tests = [("Pass", lambda s: s["pass"]), ("Score / fact coverage", lambda s: s["score"]),
             ("Opening paragraph passes", lambda s: s["lead"]["pass"]),
             ("Opening-paragraph coverage", lambda s: s["lead"]["score"]),
             ("Shorter answer (fewer words)", lambda s: -s["words"])]
    md = [f"# Compare: {args.a} (A) vs {args.b} (B)", "",
          f"- A: `{short(ma['model'])}`, prompt {ma.get('prompt', 'v1')} | B: `{short(mb['model'])}`, prompt "
          f"{mb.get('prompt', 'v1')} | {len(rows)} paired questions (run 0) | graded by "
          f"`{short(ma['judge'])}` / `{short(mb['judge'])}`", "",
          "| Metric | A | B |", "|---|---|---|", *[f"| {k} | {A[k]} | {B[k]} |" for k in A], "",
          "## Paired changes (B vs A, per question)", "",
          "| Metric | B better | B worse | same | sign-test p |", "|---|---|---|---|---|"]
    for name, f in tests:
        up, down, same, p = paired(f)
        md.append(f"| {name} | {up} | {down} | {same} | {p:.3f} |")
    if prefs:
        wb, wa = list(prefs.values()).count("B"), list(prefs.values()).count("A")
        md += ["", f"**Blind preference** (`{short(args.judge)}`, asked in both orders; inconsistent = tie): "
               f"B preferred {wb}, A preferred {wa}, tie {list(prefs.values()).count('tie')}, "
               f"judge error {list(prefs.values()).count('error')}; sign-test p = {sign_test(wb, wa):.3f}; "
               f"cost ${pref_cost:.4f}"]
    md += ["", "## Per question", "",
           "| id | grader | pass A→B | score A→B | opening passes A→B | words A→B | preferred |",
           "|---|---|---|---|---|---|---|"]
    yn = {True: "✅", False: "❌"}
    for q, s1, s2, *_ in rows:
        md.append(f"| {q['id']} | {q['evaluation']} | {yn[s1['pass']]}→{yn[s2['pass']]} | "
                  f"{s1['score']:.2f}→{s2['score']:.2f} | {yn[s1['lead']['pass']]}→{yn[s2['lead']['pass']]} "
                  f"({s1['lead']['score']:.2f}→{s2['lead']['score']:.2f}) | {s1['words']}→{s2['words']} | "
                  f"{prefs.get(q['id'], '')} |")
    path = RESULTS_DIR / f"compare_{args.a}__{args.b}.md"
    path.write_text("\n".join(md) + "\n")
    print("\n".join(md[: md.index("## Per question")]))
    print(f"Written {path}")


if __name__ == "__main__":
    main()
