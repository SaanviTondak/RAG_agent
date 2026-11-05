"""Run the agent on a question set, grade every answer, and write a scorecard.

  python -m eval.run_eval --set dev                        # run, grade, scorecard
  python -m eval.run_eval --set dev --ids q_006,q_014      # only these questions
  python -m eval.run_eval --set tune --reuse <run_id>      # reuse matching answers from an earlier run
  python -m eval.run_eval --resume <run_id>                # finish an interrupted run
  python -m eval.run_eval --regrade <run_id> [--judge M]   # re-grade saved answers (no agent cost)
  python -m eval.run_eval --set dev --no-grade             # only collect answers (before hand-grading)

Sets: dev (official 10), extra (our tune questions), tune (dev + extra), holdout (needs --final).
Output: results/<run_id>/{answers.jsonl, scores.jsonl, summary.json, scorecard.md}
"""

import argparse
import json
import math
import statistics
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from app import agent, baseline
from app.config import CHAT_MODEL, GROUNDING_NUDGE, JUDGE_MODEL, PRICES, PROMPT_VERSION, RERANK, ROOT
from app.llm import cost_usd
from eval.graders import grade, split_facts

EVAL_DIR = ROOT / "eval"
RESULTS_DIR = ROOT / "results"
FACTS_PATH = EVAL_DIR / "gold_facts.json"
FACT_SPLIT_MODEL = "accounts/fireworks/models/kimi-k3"  # one-off; the human reviews the output
WORKERS = 4
EST_TOKENS = (11_800, 1_400)  # Day 2 average prompt / completion tokens per question, for estimates


def short(model: str) -> str:
    return model.rsplit("/", 1)[-1]


# ---------------------------------------------------------------- question sets

def load_set(name: str) -> list[dict]:
    dev_extra = json.loads((EVAL_DIR / "dev_gold.json").read_text())
    dev = [{**q, **dev_extra.get(q["id"], {}), "source": "dev"}
           for q in json.loads((ROOT / "questions/dev_questions_with_answers.json").read_text())]
    extra_path = EVAL_DIR / "extra_questions.json"
    extra = [{**q, "source": "extra"} for q in json.loads(extra_path.read_text())] if extra_path.exists() else []
    sets = {"dev": dev, "extra": [q for q in extra if q["split"] == "tune"],
            "holdout": [q for q in extra if q["split"] == "holdout"]}
    sets["tune"] = sets["dev"] + sets["extra"]
    return sets[name]


def ensure_facts(questions: list[dict]) -> tuple[dict[str, list[str]], float]:
    """Gold facts for llm_judge questions; splits (and saves, unreviewed) any that are missing."""
    store = json.loads(FACTS_PATH.read_text()) if FACTS_PATH.exists() else {}
    spent = 0.0
    for q in questions:
        if q["evaluation"] == "llm_judge" and q["id"] not in store:
            facts, usage = split_facts(q["question"], q["gold_answer"], FACT_SPLIT_MODEL)
            store[q["id"]] = {"facts": facts, "reviewed": False, "split_by": short(FACT_SPLIT_MODEL)}
            spent += usage["cost_usd"]
            FACTS_PATH.write_text(json.dumps(store, indent=2) + "\n")  # save as we go
            print(f"  split {q['id']} into {len(facts)} facts (unreviewed)", flush=True)
    unreviewed = [k for k, v in store.items() if not v["reviewed"] and k in {q["id"] for q in questions}]
    if unreviewed:
        print(f"  note: gold facts not yet human-reviewed: {', '.join(unreviewed)}")
    return {k: v["facts"] for k, v in store.items()}, spent


# ---------------------------------------------------------------- running the agent

def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in open(path)] if path.exists() else []


def run_answers(questions, run_dir: Path, model: str, rerank: bool, prompt: str, runs: int, max_usd: float,
                reuse: list[str], system: str = "agent", gnudge: bool = False) -> None:
    path = run_dir / "answers.jsonl"
    done = {(a["id"], a["run"]) for a in read_jsonl(path)}
    by_id = {q["id"]: q for q in questions}
    with open(path, "a") as f:  # copy matching answers from earlier runs
        for rid in reuse:
            for a in read_jsonl(RESULTS_DIR / rid / "answers.jsonl"):
                if a["id"] in by_id and (a["id"], a["run"]) not in done and a["run"] < runs \
                        and a["model"] == model and a["rerank"] == rerank and a.get("prompt", "v1") == prompt \
                        and a.get("system", "agent") == system and a.get("grounding_nudge", False) == gnudge:
                    f.write(json.dumps(a) + "\n")
                    done.add((a["id"], a["run"]))
    jobs = [(q, r) for r in range(runs) for q in questions if (q["id"], r) not in done]
    if not jobs:
        return
    est = len(jobs) * cost_usd(model, *EST_TOKENS)
    print(f"Running {len(jobs)} answers with {short(model)} ({system}, rerank={rerank}, prompt {prompt}); "
          f"estimated ${est:.2f}, cap ${max_usd:.2f}")
    if est > max_usd:
        raise SystemExit("Estimated cost exceeds --max-usd; raise the cap or narrow --ids.")

    lock, spent = threading.Lock(), [0.0]

    def work(job):
        q, r = job
        if spent[0] >= max_usd:
            return None
        try:
            if system == "agent":
                result = agent.run(q["question"], model=model, rerank=rerank, prompt=prompt, grounding_nudge=gnudge)
            else:
                result = baseline.run(q["question"], system, model=model, prompt=prompt)
        except Exception as e:  # noqa: BLE001 - not saved, so --resume retries it
            print(f"  {q['id']} run {r}: FAILED ({type(e).__name__}: {e})")
            return None
        result.pop("question")
        rec = {"id": q["id"], "run": r, "model": model, "rerank": rerank, "prompt": prompt, "system": system,
               "grounding_nudge": gnudge, "result": result}
        u = result["usage"]
        with lock:
            spent[0] += u["cost_usd"]
            with open(path, "a") as f:
                f.write(json.dumps(rec, default=str) + "\n")
            print(f"  {q['id']} run {r}: {u['latency_ms'] / 1000:.1f}s, {u['tool_calls']} tools, "
                  f"${u['cost_usd']:.4f} (total ${spent[0]:.3f})")
        return rec

    with ThreadPoolExecutor(WORKERS) as pool:
        list(pool.map(work, jobs))
    if spent[0] >= max_usd:
        print(f"Stopped at the ${max_usd:.2f} cap; finish with --resume {run_dir.name} --max-usd <more>")


# ---------------------------------------------------------------- grading

def grade_all(questions, run_dir: Path, judge: str, facts: dict) -> list[dict]:
    by_id = {q["id"]: q for q in questions}
    answers = [a for a in read_jsonl(run_dir / "answers.jsonl") if a["id"] in by_id]
    if any(a["model"] == judge for a in answers):
        raise SystemExit(f"The judge ({short(judge)}) must differ from the answering model; pass --judge.")

    def work(a):
        q = by_id[a["id"]]
        try:
            g = grade(q, a["result"], judge, facts)
        except Exception as e:  # noqa: BLE001 - a grader failure is recorded, not fatal
            g = {"pass": False, "score": 0.0, "reason": f"grader error: {e}", "details": {}, "judge_usage": None,
                 "routing": None, "recall": None, "citations": None, "grounding": None, "lead": None, "words": None}
        return {"id": a["id"], "run": a["run"], **g}

    with ThreadPoolExecutor(WORKERS) as pool:
        scores = list(pool.map(work, answers))
    with open(run_dir / "scores.jsonl", "w") as f:
        for s in scores:
            f.write(json.dumps(s) + "\n")
    return scores


# ---------------------------------------------------------------- scorecard

def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return 0.0, 0.0
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def percentile(xs: list[float], p: float) -> float:
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p * (len(xs) - 1))))] if xs else 0.0


def modality(q: dict) -> str:
    return "+".join(sorted(q["required_modalities"])) or "none"


def scorecard(questions, run_dir: Path, scores: list[dict], meta: dict, compare: str | None) -> str:
    by_id = {q["id"]: q for q in questions}
    answers = {(a["id"], a["run"]): a for a in read_jsonl(run_dir / "answers.jsonl")}
    rows = [(by_id[s["id"]], s, answers[(s["id"], s["run"])]["result"]) for s in scores]
    n, k = len(rows), sum(s["pass"] for _, s, _ in rows)
    lo, hi = wilson(k, n)
    agent_usd = sum(r["usage"]["cost_usd"] for _, _, r in rows)
    judge_usd = sum((s["judge_usage"] or {}).get("cost_usd", 0.0) for _, s, _ in rows) + meta.get("fact_split_usd", 0.0)
    lat = [r["usage"]["latency_ms"] / 1000 for _, _, r in rows]

    def group_table(title, key):
        groups = defaultdict(list)
        for q, s, _ in rows:
            groups[key(q)].append(s)
        out = [f"| {title} | n | pass | mean score |", "|---|---|---|---|"]
        for g in sorted(groups, key=str):
            ss = groups[g]
            out.append(f"| {g} | {len(ss)} | {pct(sum(x['pass'] for x in ss) / len(ss))} | "
                       f"{sum(x['score'] for x in ss) / len(ss):.2f} |")
        return "\n".join(out)

    graded = [s for _, s, _ in rows if s["routing"]]
    routing_ok = sum(s["routing"]["ok"] for s in graded)
    over = sum(bool(s["routing"]["extra"]) for s in graded)
    rec = [s["recall"] for s in graded if s["recall"]]
    bad_cites = sum(len(s["citations"]["invalid"]) for s in graded)
    ungrounded = [s for s in graded if not s["grounding"]["ok"]]
    nudges = sum(any(t["type"] == "nudge" for t in r["trace"]) for _, _, r in rows)
    fallbacks = sum(any(t["type"] == "fallback" for t in r["trace"]) for _, _, r in rows)
    words = [s["words"] for s in graded if s.get("words") is not None]
    leads = [s["lead"] for s in graded if s.get("lead")]
    lead_cov = [s["lead"]["score"] for q, s, _ in rows if s.get("lead") and q["evaluation"] == "llm_judge"]
    full_cov = [s["score"] for q, s, _ in rows if s.get("lead") and q["evaluation"] == "llm_judge"]

    md = [f"# Scorecard: {run_dir.name}", "",
          f"- System: {meta.get('system', 'agent')}{' + grounding nudge' if meta.get('grounding_nudge') else ''} | answer model: `{short(meta['model'])}` | prompt: {meta.get('prompt', 'v1')} | judge: `{short(meta['judge'])}` | "
          f"rerank: {meta['rerank']} | "
          f"set: {meta['set']} | runs per question: {meta['runs']} | graded {meta['graded_at']}", "",
          "## Headline", "",
          f"**{k}/{n} passed ({pct(k / n if n else 0)})**, 95% CI {pct(lo)}–{pct(hi)}; "
          f"mean score {sum(s['score'] for _, s, _ in rows) / max(n, 1):.2f}", "",
          group_table("Tier", lambda q: q["tier"]), "", group_table("Sources needed", modality), "",
          group_table("Grader", lambda q: q["evaluation"]), "", group_table("Question set", lambda q: q["source"]), "",
          "## Diagnostics", "",
          "| Metric | Value |", "|---|---|",
          f"| Routing correct (no required source missing) | {routing_ok}/{len(graded)} |",
          f"| Used a source that wasn't required | {over}/{len(graded)} |",
          f"| Saw a gold page (questions with gold pages) | {sum(r['hit'] for r in rec)}/{len(rec)} |",
          f"| Invalid citations (total) | {bad_cites} |",
          f"| Answers with numbers not found in any tool output | {len(ungrounded)}/{len(graded)} |",
          f"| Nudges / fallbacks | {nudges} / {fallbacks} |",
          f"| Answer length, words: median / max | {percentile(words, .5):.0f} / {max(words, default=0)} |",
          f"| Opening paragraph alone would pass | {sum(l['pass'] for l in leads)}/{len(leads)} |",
          f"| Opening-paragraph fact coverage (llm_judge, mean) | "
          f"{statistics.mean(lead_cov) if lead_cov else 0:.2f} (full answer {statistics.mean(full_cov) if full_cov else 0:.2f}) |",
          f"| Latency p50 / p95 / max | {percentile(lat, .5):.1f}s / {percentile(lat, .95):.1f}s / {max(lat, default=0):.1f}s |",
          f"| Tokens in / out (agent) | {sum(r['usage']['prompt_tokens'] for _, _, r in rows):,} / "
          f"{sum(r['usage']['completion_tokens'] for _, _, r in rows):,} |",
          f"| Cost: agent / judge / per answer | ${agent_usd:.3f} / ${judge_usd:.3f} / ${agent_usd / max(n, 1):.4f} |",
          "", "## Per question", "",
          "| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for q, s, r in sorted(rows, key=lambda x: (x[1]["id"], x[1]["run"])):
        used = ",".join(s["routing"]["used"]) if s["routing"] else "?"
        if s["routing"] and s["routing"]["missing"]:
            used += f" (missing {','.join(s['routing']['missing'])})"
        ung = ", ".join(s["grounding"]["ungrounded"][:4]) if s["grounding"] else ""
        label = s["id"] if meta["runs"] == 1 else f"{s['id']}#{s['run']}"
        md.append(f"| {label} | {q['tier']} | "
                  f"{q['evaluation']} | {'✅' if s['pass'] else '❌'} | {s['score']:.2f} | "
                  f"{s['reason'][:160].replace('|', '/')} | {used} | {ung} | "
                  f"{r['usage']['latency_ms'] / 1000:.1f}s | {r['usage']['cost_usd']:.4f} |")
    if meta["runs"] > 1:
        per_q = defaultdict(list)
        for _, s, _ in rows:
            per_q[s["id"]].append(s["pass"])
        flaky = {i: v for i, v in per_q.items() if 0 < sum(v) < len(v)}
        md += ["", f"**Consistency:** {len(per_q) - len(flaky)}/{len(per_q)} questions gave the same result in every run."
               + (f" Inconsistent: {', '.join(f'{i} ({sum(v)}/{len(v)})' for i, v in flaky.items())}" if flaky else "")]
    if compare:
        old = defaultdict(list)
        for s in read_jsonl(RESULTS_DIR / compare / "scores.jsonl"):
            old[s["id"]].append(s["pass"])
        new = defaultdict(list)
        for _, s, _ in rows:
            new[s["id"]].append(s["pass"])
        flips = [(i, statistics.mean(old[i]), statistics.mean(new[i])) for i in new if i in old
                 and statistics.mean(old[i]) != statistics.mean(new[i])]
        md += ["", f"## Compared with {compare}", ""]
        md += [f"- {i}: {pct(a)} → {pct(b)} {'⬆️' if b > a else '⬇️'}" for i, a, b in sorted(flips)] or ["- No changes."]
    return "\n".join(md) + "\n"


# ---------------------------------------------------------------- CLI

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", choices=["dev", "extra", "tune", "holdout"], default="dev")
    ap.add_argument("--ids", help="comma-separated question ids to include")
    ap.add_argument("--model", default=CHAT_MODEL)
    ap.add_argument("--judge", default=JUDGE_MODEL)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--no-rerank", action="store_true")
    ap.add_argument("--prompt", default=PROMPT_VERSION, help="answer-format version in app/prompts.py")
    ap.add_argument("--system", choices=["agent", "rag", "pipeline"], default="agent",
                    help="the agent, or a non-agentic baseline from app/baseline.py")
    ap.add_argument("--grounding-nudge", action=argparse.BooleanOptionalAction, default=GROUNDING_NUDGE,
                    help="agent: send the model back once if a percentage in its draft is in no tool result")
    ap.add_argument("--max-usd", type=float, default=1.00, help="stop running the agent once this much is spent")
    ap.add_argument("--reuse", default="", help="comma-separated run ids whose matching answers are copied")
    ap.add_argument("--resume", help="continue an existing run directory")
    ap.add_argument("--regrade", help="re-grade an existing run without running the agent")
    ap.add_argument("--compare", help="run id to diff against")
    ap.add_argument("--name", help="suffix for the run id")
    ap.add_argument("--final", action="store_true", help="required for --set holdout")
    ap.add_argument("--no-grade", action="store_true", help="only collect answers (e.g. before hand-grading)")
    a = ap.parse_args()

    existing = a.resume or a.regrade
    if existing:
        run_dir = RESULTS_DIR / existing
        meta = json.loads((run_dir / "meta.json").read_text())
        meta["judge"] = a.judge if a.regrade else meta["judge"]
    else:
        if a.set == "holdout" and not a.final:
            raise SystemExit("The holdout set is run once, on the final config. Pass --final to confirm.")
        if short(a.model) not in PRICES:
            print(f"warning: no price for {short(a.model)}; costs will show as $0")
        run_id = f"{datetime.now():%Y%m%d-%H%M}_{a.set}_{short(a.model)}_{a.prompt}" \
            + ("" if a.system == "agent" else f"_{a.system}") + ("_gn" if a.grounding_nudge else "") \
            + ("_norerank" if a.no_rerank else "") \
            + (f"_{a.name}" if a.name else "")
        run_dir = RESULTS_DIR / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        meta = {"set": a.set, "ids": a.ids, "model": a.model, "judge": a.judge, "runs": a.runs,
                "rerank": RERANK and not a.no_rerank, "prompt": a.prompt, "system": a.system,
                "grounding_nudge": a.grounding_nudge}
        (run_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")

    questions = load_set(meta["set"])
    if meta.get("ids"):
        wanted = set(meta["ids"].split(","))
        questions = [q for q in questions if q["id"] in wanted]
    if not a.regrade:
        run_answers(questions, run_dir, meta["model"], meta["rerank"], meta.get("prompt", "v1"), meta["runs"], a.max_usd,
                    [r for r in a.reuse.split(",") if r], meta.get("system", "agent"), meta.get("grounding_nudge", False))
    if a.no_grade:
        print(f"Answers saved in {run_dir / 'answers.jsonl'}; grade later with --regrade {run_dir.name}")
        return

    facts, meta["fact_split_usd"] = ensure_facts(questions)
    print(f"Grading with {short(meta['judge'])} ...")
    scores = grade_all(questions, run_dir, meta["judge"], facts)
    meta["graded_at"] = f"{datetime.now():%Y-%m-%d %H:%M}"
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    md = scorecard(questions, run_dir, scores, meta, a.compare)
    (run_dir / "scorecard.md").write_text(md)
    summary = {"run_id": run_dir.name, **meta, "n": len(scores), "passed": sum(s["pass"] for s in scores)}
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(md.split("## Per question")[0])
    print(f"Full scorecard: {run_dir / 'scorecard.md'}")


if __name__ == "__main__":
    main()
