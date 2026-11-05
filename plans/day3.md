# Day 3 plan: evaluation harness

**Goal:** one command runs the agent on a question set, grades every answer, and writes a scorecard
showing what failed, why, and what it cost.

**Exit criterion:** `python -m eval.run_eval --set tune` produces `results/<run>/scorecard.md` for
dev + 20 tuning questions, graded by a judge that was checked against the human (Saanvi's) grades.

**Budget:** $10 total. Day 3 spend ≈ $1.40.

## Agreed decisions

| # | Decision |
|---|---|
| 1 | **Numbers:** pass only if the answer and gold agree when both are rounded to the coarser precision of the two (|a − g| ≤ half a unit of the last shown digit). No % tolerance. |
| 2 | **Entities:** gold is a list (ordered when the question asks for a ranking). The judge model extracts the companies the answer gives as its answer; sets must match, and the gold number (if any) must pass rule 1. A string-search check runs alongside as a cross-check. |
| 3 | **LLM judge:** fact by fact. Gold split into atomic facts once (saved, human-reviewed); each fact marked covered / missing / contradicted. Pass = ≥80% covered and no contradiction. |
| 4 | **Judge calibration:** human hand-grades the 10 dev answers; kimi-k3 and deepseek-v4p1-flash both grade them; keep the cheaper one if it agrees as well. |
| 5 | **Judge independence:** the judge never grades its own answers. If the judge model is also an answering candidate, a second judge grades those answers. |
| 6 | **~30 extra questions:** 20 tune, 10 holdout. Holdout is run once, on the final config. |
| 7 | **Out-of-scope questions:** 2–3 included, graded by an `out_of_scope` rule: answer says the data doesn't cover it and gives no made-up figure. |
| 8 | **Diagnostics:** routing (missing source = fail; extra = logged), recall@6 on gold pages, citation validity, number grounding, latency p50/p95, $ per question. |
| 9 | **Budget safeguards:** $ tracked per run from token usage, `--max-usd` hard stop, saved answers (re-grade free), quote before any run > $0.50. |
| 10 | **Model comparison (Day 4):** screen 7 models on dev, confirm top 2–3 on the tune set. |

## Files

```
eval/
  graders.py           # fuzzy_numeric, exact_match_entity, llm_judge, out_of_scope + diagnostics
  run_eval.py          # run agent -> save answers -> grade -> scorecard
  retrieval_eval.py    # search-only recall@6 per retrieval mode (no LLM)
  make_gold.py         # numeric gold for extra questions, computed from SQL
  calibrate_judge.py   # judge vs human agreement
  dev_gold.json        # dev questions + gold_entities / gold_pages (official key left untouched)
  extra_questions.json # ~30 questions
  gold_facts.json      # llm_judge golds split into facts (human-reviewed)
  human_grades.json    # human grades of the 10 dev answers
results/<run_id>/
  answers.jsonl, scores.jsonl, scorecard.md
```

## Steps

| Step | Who | What | Cost |
|---|---|---|---|
| 1 | Claude | Deterministic graders + tests on hand-written answers | $0 |
| 2 | Claude | Split dev llm_judge golds into facts -> `gold_facts.json` | ~$0.05 |
| 2b | Saanvi | Review fact lists (~10 min) | — |
| 3 | Claude | `run_eval.py`: parallel, saved answers, resume, cost tracking, `--max-usd`, scorecard | $0 |
| 4 | Claude | Dev run on current config (glm-5p3) | ~$0.25 |
| 5 | Saanvi | Hand-grade the 10 dev answers in `human_grades.json` **before** seeing judge scores (~15 min) | — |
| 6 | Claude | Judge calibration: kimi-k3 vs deepseek-flash vs human; pick judge | ~$0.30 |
| 7 | Claude | Write ~30 extra questions; numeric gold via `make_gold.py`, PDF gold from pages; fix the 20/10 split before any results | ~$0.05 |
| 7b | Saanvi | Review questions + gold (~30 min) | — |
| 8 | Claude | `retrieval_eval.py`: recall@6 for bm25 / dense / hybrid / hybrid+rerank | ~$0.05 |
| 9 | Claude | First tune scorecard (dev answers reused + 20 tune questions) | ~$0.70 |

## Status (2026-11-05)
- Done: steps 1, 2, 3, 4 (run `20261104-2305_dev_glm-5p3`, $0.16), 7 (32 questions: 22 tune, 10 holdout), 8.
- Waiting on Saanvi: 2b + 7b (`eval/review_sheet.md`), 5 (`eval/hand_grading_sheet.md` -> `eval/human_grades.json`).
- Then: 6 (`python -m eval.calibrate_judge`), 9 (`python -m eval.run_eval --set tune --reuse 20261104-2305_dev_glm-5p3`).
- Spent on Day 3 so far: ~$0.29.

## Extra question mix (~30)

| Type | # | Examples |
|---|---|---|
| Simple DB lookups (tier 1) | 6 | MSFT net income, GOOGL diluted EPS, AAPL R&D, total assets |
| Calculations / comparisons (tier 2–3) | 7 | operating-margin ranking, R&D intensity, debt-to-equity, top-two revenue (multi-entity) |
| PDF only | 6 | MSFT / GOOGL risk factors, AI strategy, capex, buybacks, Azure growth |
| SQL + PDF | 5 | segment change + the filing's explanation (MSFT, GOOGL) |
| Data-caveat traps | 4 | Apple "segments", Alphabet hedging, MSFT restatement, fiscal-year mismatch |
| Out of scope | 2–3 | Amazon revenue, Apple FY2022 |

## Scorecard
- Headline pass rate: overall, by tier, by modality, by grader, with the margin of error.
- Per question: pass/fail + reason, tools used, routing correct?, latency, cost.
- Diagnostics: routing accuracy, recall@6, invalid citations, ungrounded numbers, p50/p95 latency, total $.
- Diff vs a previous run.

## Day 4 preview
Fix failures; screen 7 models on dev (~$1.30), confirm top 2–3 (~$1.20); agent vs baseline (~$0.40);
end-to-end rerank ablation only if search-only shows a gap; choose final config.
