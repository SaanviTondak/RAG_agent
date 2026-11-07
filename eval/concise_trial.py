"""Trial of fixes for long answers whose facts are spread out, on saved v1 answers (no new retrieval).

Each saved v1 answer comes with its full tool trace, so we can:
- replay_*: rebuild the conversation from the trace (same tool results) and regenerate only the final answer
  with a different answer-format prompt (zero extra calls in production, but the prompt also drives research,
  so a winner must be confirmed with live runs);
- edit*: give the saved v1 draft to a separate editor call that rewrites it shorter (one extra call in
  production; research is untouched, so this is the same as a live run). The prompts below are the trial
  versions, kept so earlier results can be reproduced; "app" runs the shipped editor (app/editor.py).

  python -m eval.concise_trial --variants replay_v1,edit --ids q_006,q_025 --drafts 20261106-1347_tune_glm-5p3_v1_A

Writes results/concise_<ts>/{rows.jsonl, summary.md}.
"""

import argparse
import json
import statistics
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from app.agent import THINK_RE, hints
from app.config import CHAT_MODEL, JUDGE_MODEL, MAX_TOKENS, SEED, TEMPERATURE
from app.llm import cached_tokens, chat, cost_usd
from app.editor import MIN_EDIT_WORDS, guard
from app.editor import edit as app_edit
from app.numbers import body
from app.prompts import _BASE, _UNITS_AND_SOURCES, ANSWER_FORMATS
from app.tools import TOOL_SCHEMAS
from eval.graders import grade
from eval.run_eval import RESULTS_DIR, ensure_facts, load_set, read_jsonl

FORMATS = ANSWER_FORMATS

EDIT_SYSTEM = """You edit a draft answer from a financial research assistant so an analyst can read it quickly.
The draft is your only source: you have no documents and must not add anything.
- Keep every specific thing the draft names that bears on the question: each risk, cause, driver, product,
  segment, region, company, figure and caveat. These are the facts; never drop or generalise one ("natural
  disasters and public health issues" must not become "disruptions"). If unsure whether one matters, keep it.
- Cut the explanation around them: how or why each thing matters, consequences ("could materially adversely
  affect..."), mechanism, background, examples beyond the first, hedging, and anything said twice.
- First sentence: the direct answer. Then one bullet per point, each one line (about 25 words at most) that is
  mostly the named things and their figures. Keep tables if the draft has them.
- Cut: restating the question, describing steps or tools, section headings, closing summaries.
- Copy numbers exactly as the draft writes them. Add no new numbers, facts, or claims.
- Keep short inline page references such as (p.10) where the draft has them.
- Do not write a Sources line."""

# edit cut q_025 facts by rewording: "subscriptions like Apple Music" -> "digital content", and dropping
# "margin-accretive" as explanation. edit_x shortens by deleting, keeping the draft's own words.
EDIT_X_SYSTEM = """You shorten a draft answer from a financial research assistant so an analyst can read it quickly.
The draft is your only source: you have no documents and must not add anything.
- Shorten by deleting words, clauses and sentences, not by rewording. Where you must join or trim a sentence,
  keep the draft's own terms ("subscriptions" stays "subscriptions", never "digital content").
- Keep every specific thing the draft names that bears on the question (each risk, cause, driver, product,
  segment, region, company, figure, caveat) and every conclusion or characterisation that answers the question
  (e.g. "key growth driver", "higher margins", "recurring revenue", the reason something changed). Never drop or
  generalise one. If unsure whether something matters, keep it.
- Delete: wording that restates the question, describes steps or tools, repeats a point or figure already given,
  legal hedging ("could materially adversely affect"), mechanism detail the question did not ask about, section
  headings, and closing summaries.
- First sentence: the direct answer. Then one bullet per point, one line each where possible. Keep tables.
- Copy numbers exactly as the draft writes them. Add no new numbers, facts, or claims.
- Keep short inline page references such as (p.10) where the draft has them.
- Do not write a Sources line."""

EDIT_X_LEAD_SYSTEM = EDIT_X_SYSTEM.replace(
    "- First sentence: the direct answer. Then one bullet",
    "- Opening (1-2 sentences): the direct answer, briefly naming every item or part the question asks for.\n"
    "- Then one bullet")

EDIT_LEAD_SYSTEM =EDIT_SYSTEM.replace(
    "- First sentence: the direct answer. Then one bullet",
    "- Opening (1-2 sentences): the direct answer, briefly naming every item or part the question asks for, so a\n"
    "  reader who stops there has the whole answer; the bullets then give the figures and specifics.\n- Then one bullet")

EDIT_CL_SYSTEM = EDIT_SYSTEM + """
First list every distinct point the draft makes that bears on the question, one short phrase each, then write the
edited answer so that it covers every listed point.
Return JSON: {"points": ["...", "..."], "answer": "<edited answer>"}"""


def usage_cost(model: str, u) -> float:
    return cost_usd(model, u.prompt_tokens, u.completion_tokens, cached_tokens(u)) if u else 0.0


# ---------------------------------------------------------------- replay

def rebuild_messages(q: dict, result: dict, system: str) -> list[dict]:
    """The conversation up to (not including) the final answer, from the trace. Tool-call ids are synthetic."""
    msgs = [{"role": "system", "content": system}, *(q.get("history") or []),
            {"role": "user", "content": q["question"] + hints(q["question"])}]
    turn, n = None, 0
    for step in result["trace"]:
        if step["type"] == "llm":
            turn = None
        elif step["type"] == "tool":
            if turn is None:
                turn = {"role": "assistant", "content": "", "tool_calls": []}
                msgs.append(turn)
            n += 1
            turn["tool_calls"].append({"id": f"call_{n}", "type": "function",
                                       "function": {"name": step["tool"], "arguments": step["args"]}})
            msgs.append({"role": "tool", "tool_call_id": f"call_{n}", "content": step["result"]})
        elif step["type"] == "nudge":
            msgs += [{"role": "assistant", "content": "(draft answer)"}, {"role": "user", "content": step["text"]}]
            turn = None
        elif step["type"] == "fallback":
            msgs.append({"role": "user", "content": "Tool or time budget reached. Answer now using only the evidence "
                                                    "gathered above, in the required format."})
    return msgs


def replay(q: dict, result: dict, fmt: str, model: str) -> dict:
    msgs = rebuild_messages(q, result, _BASE + FORMATS[fmt] + _UNITS_AND_SOURCES)
    t, cost, tool_retry = time.time(), 0.0, False
    resp = chat(model=model, messages=msgs, tools=TOOL_SCHEMAS, tool_choice="auto", temperature=TEMPERATURE,
                seed=SEED, max_tokens=MAX_TOKENS)
    cost += usage_cost(model, resp.usage)
    if resp.choices[0].message.tool_calls:  # wanted more research; answer from the frozen evidence instead
        tool_retry = True
        resp = chat(model=model, messages=msgs, tools=TOOL_SCHEMAS, tool_choice="none", temperature=TEMPERATURE,
                    seed=SEED, max_tokens=MAX_TOKENS)
        cost += usage_cost(model, resp.usage)
    answer = THINK_RE.sub("", resp.choices[0].message.content or "").strip()
    return {"answer": answer, "extra_s": time.time() - t, "extra_usd": cost, "info": {"tool_retry": tool_retry}}


# ---------------------------------------------------------------- editor

def edit(q: dict, draft: str, model: str, checklist: bool, system: str | None = None) -> dict:
    if len(body(draft).split()) < MIN_EDIT_WORDS:
        return {"answer": draft, "extra_s": 0.0, "extra_usd": 0.0, "info": {"skipped": "short"}}
    t = time.time()
    kw = {"response_format": {"type": "json_object"}} if checklist else {}
    resp = chat(model=model, messages=[{"role": "system", "content": system or (EDIT_CL_SYSTEM if checklist else EDIT_SYSTEM)},
                                       {"role": "user", "content": f"Question: {q['question']}\n\nDraft answer:\n{body(draft).strip()}"}],
                temperature=0.0, seed=SEED, max_tokens=4096, reasoning_effort="low", **kw)
    cost, text = usage_cost(model, resp.usage), THINK_RE.sub("", resp.choices[0].message.content or "").strip()
    info = {}
    if checklist:
        try:
            obj = json.loads(text[text.find("{"): text.rfind("}") + 1])
            text, info["points"] = str(obj["answer"]), obj.get("points", [])
        except (ValueError, KeyError, TypeError):
            text = ""
    edited = body(text).strip()
    out, reason = guard(q["question"], draft, edited)
    info["fallback"] = reason
    return {"answer": out, "extra_s": time.time() - t, "extra_usd": cost, "info": info}


# ---------------------------------------------------------------- trial

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--variants", default="draft,replay_v1,replay_v6,replay_v1c,edit,edit_cl")
    ap.add_argument("--drafts", required=True, help="comma-separated v1 run ids whose answers are the drafts")
    ap.add_argument("--ids", help="comma-separated question ids (default: all in the draft runs)")
    ap.add_argument("--model", default=CHAT_MODEL, help="model for replay and the editor")
    ap.add_argument("--judge", default=JUDGE_MODEL)
    ap.add_argument("--repeats", type=int, default=1, help="repeat each variant on each draft")
    ap.add_argument("--name", default="")
    a = ap.parse_args()

    questions = {q["id"]: q for q in load_set("tune")}
    wanted = set(a.ids.split(",")) if a.ids else None
    drafts = []
    for rid in a.drafts.split(","):
        scores = {(s["id"], s["run"]): s for s in read_jsonl(RESULTS_DIR / rid / "scores.jsonl")}
        for rec in read_jsonl(RESULTS_DIR / rid / "answers.jsonl"):
            if rec["id"] in questions and (wanted is None or rec["id"] in wanted):
                res = rec["result"]  # runs made with the editor on keep the unedited draft: use it as the draft
                res = {**res, "answer": res["draft"]} if res.get("draft") else res
                drafts.append({"src": f"{rid}#{rec['run']}", "id": rec["id"], "result": res,
                               "orig": scores.get((rec["id"], rec["run"]))})
    facts, _ = ensure_facts([questions[d["id"]] for d in drafts])
    variants = a.variants.split(",")
    jobs = [(v, d, r) for v in variants for d in drafts for r in range(a.repeats)]
    print(f"{len(drafts)} drafts x {len(variants)} variants x {a.repeats} = {len(jobs)} jobs")

    out_dir = RESULTS_DIR / f"concise_{datetime.now():%Y%m%d-%H%M}{'_' + a.name if a.name else ''}"
    out_dir.mkdir(parents=True, exist_ok=True)

    def work(job):
        v, d, r = job
        q, res = questions[d["id"]], d["result"]
        try:
            if v == "draft":  # the saved v1 answer, regraded: measures judge noise
                o = {"answer": res["answer"], "extra_s": 0.0, "extra_usd": 0.0, "info": {}}
            elif v == "app":
                ed = app_edit(q["question"], res["answer"], a.model)
                o = {"answer": ed["answer"] if ed else res["answer"], "extra_s": (ed or {}).get("ms", 0) / 1000,
                     "extra_usd": usage_cost(a.model, (ed or {}).get("usage")),
                     "info": {"skipped": "short"} if not ed else {"fallback": ed["fallback"], "points": ed["points"]}}
            elif v.startswith("replay_"):
                o = replay(q, res, v.split("_", 1)[1], a.model)
            else:
                o = edit(q, res["answer"], a.model, checklist=(v == "edit_cl"),
                         system={"edit_lead": EDIT_LEAD_SYSTEM, "edit_x": EDIT_X_SYSTEM,
                                 "edit_x_lead": EDIT_X_LEAD_SYSTEM}.get(v))
            g = grade(q, {**res, "answer": o["answer"]}, a.judge, facts)
        except Exception as e:  # noqa: BLE001
            print(f"  {v} {d['id']} FAILED: {type(e).__name__}: {e}")
            return None
        row = {"variant": v, "id": d["id"], "src": d["src"], "rep": r, "answer": o["answer"], "info": o["info"],
               "extra_s": round(o["extra_s"], 2), "extra_usd": round(o["extra_usd"], 5),
               "pass": g["pass"], "score": g["score"], "reason": g["reason"], "words": g["words"],
               "lead_pass": g["lead"]["pass"], "lead_score": g["lead"]["score"],
               "orig_pass": d["orig"]["pass"] if d["orig"] else None,
               "orig_words": d["orig"]["words"] if d["orig"] else None,
               "orig_lead_score": d["orig"]["lead"]["score"] if d["orig"] else None,
               "evaluation": q["evaluation"], "gold_words": len(q["gold_answer"].split())}
        print(f"  {v:11s} {d['id']} {'PASS' if g['pass'] else 'FAIL'} {g['score']:.2f} {g['words']}w "
              f"(orig {row['orig_words']}w) {o['info'].get('fallback') or ''}", flush=True)
        return row

    with ThreadPoolExecutor(4) as pool:
        rows = [r for r in pool.map(work, jobs) if r]
    with open(out_dir / "rows.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    md = summarize(rows, variants)
    (out_dir / "summary.md").write_text(md)
    print(md)
    print(f"Saved to {out_dir}")


def summarize(rows: list[dict], variants: list[str]) -> str:
    md = ["| variant | pass | lost vs draft | gained | median words (draft) | median x gold (judge q) | "
          "opening passes | opening coverage | fallbacks | +s median | +$ total |", "|" + "---|" * 11]
    for v in variants:
        rs = [r for r in rows if r["variant"] == v]
        if not rs:
            continue
        lost = [f"{r['id']}" for r in rs if r["orig_pass"] and not r["pass"]]
        gained = sum(1 for r in rs if r["orig_pass"] is False and r["pass"])
        jq = [r for r in rs if r["evaluation"] == "llm_judge"]
        ratio = statistics.median(r["words"] / r["gold_words"] for r in jq) if jq else 0
        fb = sum(1 for r in rs if r["info"].get("fallback"))
        md.append(f"| {v} | {sum(r['pass'] for r in rs)}/{len(rs)} | {len(lost)} {','.join(sorted(set(lost)))} | "
                  f"{gained} | {statistics.median(r['words'] for r in rs):.0f} "
                  f"({statistics.median(r['orig_words'] or 0 for r in rs):.0f}) | {ratio:.1f}x | "
                  f"{sum(r['lead_pass'] for r in rs)}/{len(rs)} | "
                  f"{statistics.mean(r['lead_score'] for r in jq) if jq else 0:.2f} "
                  f"({statistics.mean(r['orig_lead_score'] or 0 for r in jq) if jq else 0:.2f}) | {fb} | "
                  f"{statistics.median(r['extra_s'] for r in rs):.1f} | {sum(r['extra_usd'] for r in rs):.3f} |")
    md += ["", "Figures in brackets are the original v1 drafts. 'lost vs draft' = draft passed, variant failed."]
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    main()
