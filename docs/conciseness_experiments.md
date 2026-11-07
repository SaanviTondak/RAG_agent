# Conciseness experiments

The brief prefers "concise but well-supported" answers to synthesis questions. The shipped prompt (v1, then v1r)
writes answers about 3–5× the length of the gold answers, usually with the direct answer in the first paragraph.
Seven attempts to shorten answers all lost facts, so none was adopted; the UI folds the supporting points instead.

**How each attempt was judged:** the same graders as everything else (fact checklists for synthesis questions),
plus words ÷ gold length, whether the opening paragraph alone would pass, and repeats of the "fragile" questions
whose answers are long lists (q_006 supply-chain risks, q_025 Services strategy, x_047 AI costs, …). An attempt was
kept only if it shortened answers *without* losing facts. Prompt texts are in `app/prompts.py` (`ANSWER_FORMATS`).

| # | Attempt | What changed | Result | Decision |
|---|---|---|---|---|
| 1 | v2 | Opening paragraph answers every part; bold-labelled bullets | Opening coverage 0.59 → 0.72, but full-answer coverage 0.99 → 0.95 and 32/32 → 30/32 (q_006, q_025 lost facts); answers got *longer* (median 115 → 138 words) | Rejected ([compare](../results/compare_20261105-1447_tune_glm-5p3_v1_fresh__20261105-1447_tune_glm-5p3_v2.md)) |
| 2 | v3 | v1 plus "the opening paragraph answers every part" | Opening coverage 0.65 → 0.75, but 39/39 → 37/39 (q_006 lost facts again) | Rejected ([compare](../results/compare_20261105-1740_tune_glm-5p3_v1_all40__20261105-1741_tune_glm-5p3_v3_gn.md)) |
| 3 | v4 | Scope rules: answer exactly what is asked, no unrequested breakdowns | Half the length (4.7× → 2.4× gold) and preferred 32–7 in a blind vote, but 45/47, and q_006 0/3, q_025 0/3 in repeats: "answer only what is asked" narrowed list questions | Rejected ([compare](../results/compare_20261106-1347_tune_glm-5p3_v1_A__20261106-1353_tune_glm-5p3_v4_B.md)) |
| 4 | v4 + planner | Scope rules with answers structured by an explicit plan | 44/47, 2.6× gold; q_006 1/3 | Rejected ([compare](../results/compare_20261106-1347_tune_glm-5p3_v1_A__20261106-1413_tune_glm-5p3_v4_plan_C2.md)) |
| 5 | v5 + planner | v4 variant | 10/14 on the fragile questions | Rejected ([scorecard](../results/20261106-1526_tune_glm-5p3_v5_plan_fragile/scorecard.md)) |
| 6 | v6, v1c | Compact one-line bullets (v6 also allows tables) | Fragile questions 16/21 and 15/21; q_006 0/3 with v1c | Rejected ([v6](../results/20261106-1909_tune_glm-5p3_v6_live_v6/scorecard.md), [v1c](../results/20261106-1909_tune_glm-5p3_v1c_live_v1c/scorecard.md)) |
| 7 | Answer editor | Research unchanged; one extra call rewrites a long finished answer shorter, with checks (no new numbers, lead company kept, must be shorter) | Words ÷ gold 4.8× → 3.4× (−29%), fewer unsupported claims (13 → 10 of 26), but 2 of 44 edited answers went from correct to wrong (dropped "iCloud"; kept the 10-K's rounded 21% instead of 21.5%), and repeat grading showed neither was judge noise | Rejected by the rule written before the run ([`plans/final_eval.md`](../plans/final_eval.md), code in `app/editor.py`, off) |
| – | UI folding | Display only: the opening answer is shown, the supporting points fold under "Details (N points)"; the API returns the full answer | No effect on grading | Adopted |

**Why prompt-only brevity kept failing.** Asking for brevity while the agent is still researching also makes it
*research* less: with "answer only what is asked", it read fewer risk sections for q_006. The editor avoided that
by editing only the finished answer, but its rewrites still occasionally swapped or dropped a specific fact, and
the checks catch added numbers, not missing ones.

**A testing pitfall found along the way.** A cheaper way to test prompts, rebuilding each saved conversation and
regenerating only the final answer ("replay"), turned out to be unfaithful: even the unchanged v1 prompt fell from
21/24 to 15/24 under replay. Replay results were discarded and only live runs used (`eval/concise_trial.py`,
`results/concise_20261106-1855_fragile/summary.md`).

**What would work better** (not done): have the model output structured facts with their sources, then render a
short answer from them, so a shorter answer cannot silently lose a fact.

Log of the whole investigation, day by day: [`plans/day3.md`](../plans/day3.md).
