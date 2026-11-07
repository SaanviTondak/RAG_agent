# Final evaluation protocol (written 2026-11-06, before any of these runs)

The brief asks how we measured quality and where the system still fails. This protocol fixes, in advance, what
is run, what decides the one open choice (the answer editor), and what is reported. Nothing is tuned after
step 2.

## Candidate system
glm-5p3, prompt **v1r** (v1 + read Item 1A for risk questions), grounding nudge on, planner off by default
("Plan first" toggle in the UI), rerank on, 90s budget. Open choice: **answer editor on or off**.

## Grading (all in `eval/graders.py`)
- Pass/fail: fuzzy_numeric (rounded to the coarser precision, no % tolerance), exact_match_entity (judge extracts
  the answer's company; string check alongside), llm_judge (fact checklist, pass = at least 80% covered and no
  contradiction), out_of_scope. Judge: deepseek-v4p1-flash (glm never grades itself).
- Checklists: all 31 human-reviewed before step 1 (15 reviewed in `eval/review_checklists.md`; every number in
  them matched against a gold page or the database first).
- Diagnostics on every answer: routing, gold-page recall, citation validity, numbers not in any tool output,
  **faithfulness** (claims not backed by the tool output or the agent's data notes; stress test
  `eval/faith_stress.py`), opening-paragraph check, words ÷ gold, latency, cost.

## Steps
| # | Command | Est. cost |
|---|---|---|
| 1a | `python -m eval.run_eval --set tune --prompt v1r --editor --name final_cand --max-usd 1.2` (47 q) | ~$1.20 |
| 1b | `python -m eval.run_eval --set tune --ids q_001,q_006,q_008,q_011,q_012,q_014,q_017,q_018,q_022,q_025,x_014,x_036,x_047 --runs 2 --prompt v1r --editor --name final_rep --max-usd 0.8` | ~$0.80 |
| 1c | `python -m eval.robustness --runs <1a>,<1b> --noise 2` (judge noise on the same answers) | ~$0.10 |
| 2 | Editor decision (rule below), set defaults; then `python -m eval.run_eval --set holdout --final --runs 3 --prompt v1r [--editor]` | ~$0.90 |
| 3 | `python -m eval.robustness --runs <1a>,<2> --first-run-only --holistic --second-judge kimi-k3` | ~$0.15 |
| 4 | `python -m eval.failures --runs <1a>,<1b>,<2> --robustness <1c>`; causes confirmed by hand; `dev_answers.json`; report | $0 |
| | **Total** (agent ~$0.013-0.02 per answer; judging ~$0.008 per answer, mostly the faithfulness check) | **~$3.15** |

1b = the 10 dev questions plus the fragile ones not in dev (x_014, x_036, x_047); fragile set: q_006, q_014,
q_022, q_025, x_014, x_036, x_047. With 1a this gives 3 runs of each. `--max-usd` caps agent spend only.

## Editor decision rule (fixed now)
Every answer in 1a/1b keeps its unedited draft, and the scorecard grades both (same research, so the editor is
the only difference). **Keep the editor only if all hold:**
1. No answer whose draft passed fails after editing, except where 1c shows the same judge flips that answer's
   verdict on regrading (judge noise).
2. Pass rate of the sent answers on 1a is at least 46/47.
3. q_006 and x_014 pass in all their runs (checks the Item 1A rule; applies with or without the editor).
4. Median words ÷ gold on edited llm_judge answers drops by at least 20%.
5. Edited answers have no more faithfulness flags than their drafts.

Otherwise the editor is off, and the drafts' grades are the results (no rerun needed). If rule 3 fails, the
Item 1A rule is reported as not fixing q_006/x_014; it stays in only if those questions are no worse than v1.

## What is reported
- **Headline: holdout (step 2)**, 13 questions written before any tuning and never run until now; pass rate
  over 3 runs with 95% CI, and questions passing in all 3 runs.
- Dev and tune: in-sample (prompts were tuned on them); reported with the same metrics, clearly labelled.
- Robustness table (ours / strict / lenient / holistic / second judge), judge noise, faithfulness rate.
- Failure table with confirmed causes; the editor decision with its paired numbers; everything tried and dropped.
- If the holdout shows a problem, it is reported, not fixed.

## Known limits (go in the report)
- 60 questions, mostly written by us; the hidden set's graders are unknown (hence the robustness table).
- The number-grounding diagnostic matches numbers against tool output at any scale, so with large outputs it can
  find accidental matches (it is a hint, not proof); faithfulness covers claims of every kind.
- The planner gate was earlier tuned with holdout labels; the planner is off by default and the test now uses
  tuning questions only.

## Results (run 2026-11-06, as specified above)

Run ids: 1a `20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand`, 1b `20261106-2329_tune_glm-5p3_v1r_gn_ed_final_rep`,
editor-off views `..._noedit` (`eval/without_editor.py`), holdout `20261106-2346_holdout_glm-5p3_v1r_gn_final_holdout`,
robustness `results/robustness_20261106-2345.*` (1c) and the step-3 file, failures `results/failures_20261106-2355.md`.

**Editor decision: off.** Rules 2-5 held (46/47; q_006 and x_014 3/3; words ÷ gold 4.8x -> 3.4x, -29%;
faithfulness flags 13 -> 10 and 10 -> 10). Rule 1 failed: two passing drafts failed after editing, and 1c showed
neither was judge noise (0 of 57 judge-graded answers changed verdict on two regrades): x_020#0 kept the 10-K's
rounded "21%" and dropped 21.5%; q_025#0 dropped "iCloud". The checks catch added numbers, not dropped ones.

**Final config (v1r, editor off):**
| Set | Answers | Passed | All runs passed |
|---|---|---|---|
| Holdout (headline; never run before) | 13 q x 3 runs | **39/39** | **13/13** (95% CI 77-100%) |
| Tune (in-sample) | 47 q x 1 | 47/47 | - |
| Dev + fragile repeats (in-sample) | 13 q x 2 more | 25/26 | 12/13 (x_047 2/3) |

- The CI is per question: the 39 answers are 3 runs of 13 questions, not 39 independent samples (an answer-level
  CI, 91-100%, would overstate the precision).
- Holdout x_018#2 was regraded once: its first grading failed (the judge returned invalid JSON twice); regrade 6/6.
- Only failure in 112 answers: x_047#1, confirmed by hand as mixed: one fact on a page never retrieved
  (GOOGL p.39), one on a page read but left out (MSFT p.37-38).
- Robustness (run 0 of tune + holdout, 60 answers): ours 60/60, lenient 60/60, holistic judge 60/60,
  second judge kimi-k3 60/60, strict 58/60 (q_025, x_047 miss one checklist fact each). Judge noise 0/57.
- Faithfulness: answers with a claim no tool returned: tune 16/47, holdout 11/39; contradicting the tools:
  1/47 and 2/39 (to be read by hand for the report).
- Holdout latency p50 8.1s / p95 29.4s / max 39.0s; $0.010 per answer.
- Spend for the protocol ~$3.6 (step 0 ~$0.35, 1a $1.30, 1b $1.11, 1c $0.12, holdout $0.58, step 3 $0.39).
- Contradictions, read by hand (3 answers of 86; all three still passed their gold checks, so only the
  faithfulness check saw them): q_025#0 "Services margin on roughly half the revenue of Products" (database:
  $109.2B vs $307.0B, about a third: head arithmetic) and "growth driver across every geography" (the filing names
  four regions; Greater China declined); x_016#2 "Server products and cloud services revenue is not broken out"
  (it is, MSFT FY2025 10-K p.80); x_031#2 a minor overstatement about FY2020 data in an out-of-scope answer.
  Known weakness for the report: unprompted extra claims, which the gold checklists cannot catch.

## Addendum (2026-11-07, written before these runs): grounding fix v1g

**Why:** an outside review (Codex) pointed out that checklist passes hide unsupported claims: v1r's answers include a
claim no tool returned in 16/47 tune and 11/39 holdout answers, with contradictions in 1/47 and 2/39 (e.g.
q_025's "roughly half the revenue", really about a third). The grounding requirement in the brief makes this worth
one targeted attempt. The graders were fixed first (numeric: unit, direction, judge-picked headline figure;
citations: every cited page must be seen; search bookkeeping); re-applied to the saved v1r runs, nothing changed.

**v1g** = v1r + "Stay within the evidence": no characterisations the evidence does not state (use the filing's
words), comparisons and proportions only from a tool or `calculate`, no generalising from some items to all.
The prompt's examples are neutral phrases, not ones flagged in our answers.

**Runs:** G1 `--set tune --prompt v1g` (47 q); G2 the fragile set (q_006, q_014, q_022, q_025, x_014, x_036,
x_047) `--runs 2` more; G3 holdout `--runs 3` (a second look, reported as such) only if G1+G2 pass.

**Keep v1g only if all hold** (v1r baselines in brackets; tune latency/cost without the editor call):
1. Grounding: answers with an unsupported or contradicted claim on tune <= 10/47 [16/47]; contradictions <= 1/47 [1].
2. Correctness: tune pass >= 46/47 [47/47]; fragile set over 3 runs >= 20/21 [20/21], q_006 and x_014 3/3.
3. Tool use: routing 47/47 [47/47]; invalid citations 0 [0]; saw a gold page >= 22/24 [23/24].
4. Speed and cost: median latency <= +3s [11.9s], p95 <= +8s [27.5s]; cost per answer <= +25% [~$0.012].
5. Usefulness: opening paragraph alone passes >= 31/47 [33/47]; median answer words <= +15% [132].
6. G3 holdout: 13/13 questions pass every run [13/13] and answers with an unsupported/contradicted claim <= 11/39
   [11/39]. Otherwise ship v1r.
Whatever happens is reported; if v1g is rejected, the attempt and its numbers go in the report.

### Addendum results (2026-11-07): v1g rejected, v1r stays
Runs: G1 `20261107-1028_tune_glm-5p3_v1g_gn_g1`, G2 `20261107-1105_tune_glm-5p3_v1g_gn_g2` (x_036#0 regraded once
after a grader error: 9/9). Cost $1.55 (agent $0.95, judge $0.60). G3 (holdout) not run, as specified.
| Rule | v1g | v1r | Held? |
|---|---|---|---|
| 1 grounding | 7/47 with an unsupported claim, 1 contradiction | 16/47, 1 | yes |
| 2 correctness | tune 46/47; fragile 19/21 (x_047 1/3) | 47/47; 20/21 (x_047 2/3) | **no** |
| 3 tool use | routing 47/47, 0 invalid citations, gold page 23/24 | same | yes |
| 4 speed, cost | p50 11.5s, p95 33.0s, $0.0119 | 11.9s, 27.5s, ~$0.012 | yes |
| 5 usefulness | opening alone passes 28/47; median 136 words | 33/47; 132 | **no** |
The opening-paragraph loss is one-directional (5 lost: x_021, x_025, x_029, x_043, x_048; 0 gained): the
"no characterisation" rule also stripped explanation from openings (x_025's opening fell from 100% to 17% of its
facts). v1g did more than halve unsupported claims, so claim-level grounding stays the top item for future work.
