# Scorecard: 20261106-2346_holdout_glm-5p3_v1r_gn_final_holdout

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v1r | judge: `deepseek-v4p1-flash` | rerank: True | set: holdout | runs per question: 3 | graded 2026-11-06 23:53

x_018#2 was regraded once: its first grading failed (the judge returned invalid JSON twice).

Grader fixes of 2026-11-07 applied (eval/apply_grader_fixes.py).

## Headline

**39/39 passed (100%)**, 95% CI 91%–100%; mean score 1.00

**By question: 13/13 passed in every run**, 95% CI 77%–100% (the CI above treats repeated runs of a question as independent, so it is too narrow).

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 12 | 100% | 1.00 |
| 2 | 21 | 100% | 1.00 |
| 3 | 6 | 100% | 1.00 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 3 | 100% | 1.00 |
| 1 lookup | 9 | 100% | 1.00 |
| 2 calculation / comparison | 9 | 100% | 1.00 |
| 3 figure + explanation | 6 | 100% | 1.00 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 6 | 100% | 1.00 |
| 7 follow-up | 3 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 3 | 100% | 1.00 |
| pdf | 6 | 100% | 1.00 |
| pdf+sql | 12 | 100% | 1.00 |
| sql | 18 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 3 | 100% | 1.00 |
| fuzzy_numeric | 15 | 100% | 1.00 |
| llm_judge | 18 | 100% | 1.00 |
| out_of_scope | 3 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| extra | 39 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 39/39 |
| Used a source that wasn't required | 7/39 |
| Saw a gold page (questions with gold pages) | 18/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 2/39 |
| Faithfulness: answers with a claim the tools did not return / contradicting them | 11/39 / 2/39 (399 claims checked) |
| Nudges / fallbacks | 7 / 0 |
| Answer length, words: median / max | 105 / 361 |
| Answer length ÷ gold answer length (llm_judge, median) | 3.4x |
| Opening paragraph alone would pass | 33/39 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.79 (full answer 1.00) |
| Latency p50 / p95 / max | 8.1s / 29.4s / 39.0s |
| Tokens in / out (agent) | 454,199 / 31,664 |
| Cost: agent / judge / per answer | $0.389 / $0.218 / $0.0100 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| x_005#0 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$112.4 billion' matches 112390000000 (usd) | pdf,sql |  | 9.0s | 0.0070 |
| x_005#1 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$112.4 billion' matches 112390000000 (usd) | sql |  | 3.2s | 0.0046 |
| x_005#2 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$112.4 billion' matches 112390000000 (usd) | sql | 112,390, 350,018 | 8.1s | 0.0076 |
| x_006#0 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '46.9%' matches 46.90516410716045 (pct) | sql |  | 4.7s | 0.0032 |
| x_006#1 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '46.9%' matches 46.90516410716045 (pct) | sql |  | 3.8s | 0.0033 |
| x_006#2 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '46.9%' matches 46.90516410716045 (pct) | sql |  | 5.1s | 0.0060 |
| x_010#0 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '0.13' matches 0.12562922332951942 (plain) | sql |  | 3.3s | 0.0042 |
| x_010#1 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '0.13' matches 0.12562922332951942 (plain) | sql |  | 3.5s | 0.0032 |
| x_010#2 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '0.13' matches 0.12562922332951942 (plain) | sql |  | 3.0s | 0.0033 |
| x_012#0 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion' | sql |  | 3.4s | 0.0032 |
| x_012#1 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion' | sql |  | 3.1s | 0.0027 |
| x_012#2 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL'] (gold ['AAPL']); number: found '$35.9 billion' | sql |  | 2.9s | 0.0027 |
| x_016#0 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '34%' matches 34 (pct) | pdf |  | 6.7s | 0.0080 |
| x_016#1 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '34%' matches 34 (pct) | pdf |  | 6.2s | 0.0053 |
| x_016#2 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '34%' matches 34 (pct) | pdf |  | 7.2s | 0.0055 |
| x_018#0 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 32.8s | 0.0511 |
| x_018#1 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 29.4s | 0.0352 |
| x_018#2 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql | 22 | 39.0s | 0.0539 |
| x_023#0 | 2 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 10.3s | 0.0094 |
| x_023#1 | 2 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 11.5s | 0.0097 |
| x_023#2 | 2 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 15.5s | 0.0110 |
| x_024#0 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 8.1s | 0.0077 |
| x_024#1 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 7.4s | 0.0080 |
| x_024#2 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 13.5s | 0.0080 |
| x_026#0 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$1.5 billion' matches 1537000000 (usd) | sql |  | 3.5s | 0.0053 |
| x_026#1 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$1.5 billion' matches 1537000000 (usd) | sql |  | 3.5s | 0.0029 |
| x_026#2 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$1.5 billion' matches 1537000000 (usd) | sql |  | 3.2s | 0.0025 |
| x_031#0 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related available data without fabricating a figure. | pdf,sql |  | 11.2s | 0.0096 |
| x_031#1 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related, sourced figures without fabricating the requested | pdf,sql |  | 9.1s | 0.0084 |
| x_031#2 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Apple's FY2020 net income is not available in its sources and provides only related, correctly-scoped data without fabricating a figur | pdf,sql |  | 9.9s | 0.0079 |
| x_044#0 | 3 | llm_judge | ✅ | 1.00 | 2/2 facts covered | pdf,sql |  | 12.0s | 0.0144 |
| x_044#1 | 3 | llm_judge | ✅ | 1.00 | 2/2 facts covered | pdf,sql |  | 11.1s | 0.0089 |
| x_044#2 | 3 | llm_judge | ✅ | 1.00 | 2/2 facts covered | pdf,sql |  | 9.4s | 0.0074 |
| x_046#0 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 8.9s | 0.0096 |
| x_046#1 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 11.7s | 0.0105 |
| x_046#2 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 12.7s | 0.0111 |
| x_050#0 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 10.8s | 0.0112 |
| x_050#1 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 6.9s | 0.0079 |
| x_050#2 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 9.2s | 0.0073 |

**Consistency:** 13/13 questions passed in every run; 13/13 gave the same result in every run.
