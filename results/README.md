# Results index

Every evaluation run behind [REPORT.md](../REPORT.md). Run directories hold `meta.json` (configuration),
`answers.jsonl` (answers with full traces), `scores.jsonl` (grades and diagnostics) and `scorecard.md`; the final
runs also have a readable `answers.md`. Run ids read `<date>-<time>_<set>_<model>_<prompt>[_gn grounding nudge]
[_ed answer editor][_plan planner]_<name>`. Decision rules and outcomes: [plans/final_eval.md](../plans/final_eval.md).

## Final system (prompt v1r, editor off, planner off)
| Claim in the report | Run |
|---|---|
| Holdout: 13/13 questions pass every run | `20261106-2346_holdout_glm-5p3_v1r_gn_final_holdout/` |
| Tuning set 47/47; diagnostics (tune) | `20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand_noedit/` (editor removed from the run below) |
| Dev and fragile questions over 3 runs: 38/39 | the run above + `20261106-2329_tune_glm-5p3_v1r_gn_ed_final_rep_noedit/` |
| Editor rejected (paired draft vs edited) | `20261106-2313_..._final_cand/`, `20261106-2329_..._final_rep/` (scorecard section "Answer editor") |
| Judge noise 0/57 | `robustness_20261106-2345.md` |
| Alternative grader definitions, second judge | `robustness_20261106-2356.md` |
| Failure analysis (hand-confirmed cause) | `failures_20261106-2355.md` |
| Grader fixes after the outside review: no result changed | `grader_fixes_20261107-1026.md` |
| `dev_answers.json` | `20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand_noedit/`, run 0 |

## Decisions along the way
| Question | Runs / files |
|---|---|
| Which answer model? | `model_comparison_20261105-1639.md` (7 models, 32 questions) and the `20261105-16xx_tune_<model>_v1/` runs |
| Agent vs non-agent baselines | `compare_20261105-1740_..._v1_all40__..._v1_pipeline.md`, `..._v1_rag.md` |
| Reranker on or off | `compare_20261105-1740_..._v1_all40__..._v1_norerank.md`; search-only recall: `retrieval_20261105-0131_extra.md`, `retrieval_20261104-2310_dev.md` |
| Item 1A rule (v1r) | `20261106-1747_tune_glm-5p3_v1r_riskfix/` |
| Planner (auto) | `compare_20261106-1347_..._v1_A__..._v1_plan_Aplan.md`, `20261106-1353_..._v4_plan_C_slowplanner/` (slow planner, timeouts), `..._C2/` |
| Grounding prompt v1g (rejected) | `20261107-1028_tune_glm-5p3_v1g_gn_g1/`, `20261107-1105_tune_glm-5p3_v1g_gn_g2/` |
| Grounding nudge | `20261105-1749_tune_glm-5p3_v1_gn_nudgetest/` |
| Conciseness (7 attempts) | see [docs/conciseness_experiments.md](../docs/conciseness_experiments.md): `compare_*` for v2–v4, `*_v5_plan_fragile/`, `*_v6_live_v6/`, `*_v1c_live_v1c/`, `concise_*/summary.md` (editor trials) |
| Judge calibration | `20261104-2305_dev_glm-5p3/judge_stress.md`, `faith_stress.md` |
