# Scorecard: 20261106-2329_tune_glm-5p3_v1r_gn_ed_final_rep

- System: agent + grounding nudge + answer editor | answer model: `glm-5p3` | prompt: v1r | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-06 23:41

## Headline

**24/26 passed (92%)**, 95% CI 76%–98%; mean score 0.97

**By question: 11/13 passed in every run**, 95% CI 58%–96% (the CI above treats repeated runs of a question as independent, so it is too narrow).

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 8 | 100% | 1.00 |
| 2 | 10 | 100% | 1.00 |
| 3 | 8 | 75% | 0.90 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 6 | 100% | 1.00 |
| 2 calculation / comparison | 6 | 100% | 1.00 |
| 3 figure + explanation | 6 | 100% | 1.00 |
| 4 multi-part synthesis | 8 | 75% | 0.90 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 8 | 88% | 0.95 |
| pdf+sql | 8 | 88% | 0.96 |
| sql | 10 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 4 | 100% | 1.00 |
| fuzzy_numeric | 4 | 100% | 1.00 |
| llm_judge | 18 | 89% | 0.96 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 20 | 95% | 0.98 |
| extra | 6 | 83% | 0.93 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 26/26 |
| Used a source that wasn't required | 4/26 |
| Saw a gold page (questions with gold pages) | 16/16 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 6/26 |
| Faithfulness: answers with a claim the tools did not return / contradicting them | 11/26 / 1/26 (490 claims checked) |
| Nudges / fallbacks | 2 / 1 |
| Answer length, words: median / max | 136 / 536 |
| Answer length ÷ gold answer length (llm_judge, median) | 4.6x |
| Opening paragraph alone would pass | 9/26 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.42 (full answer 0.96) |
| Latency p50 / p95 / max | 18.3s / 44.6s / 49.2s |
| Tokens in / out (agent) | 395,188 / 58,455 |
| Cost: agent / judge / per answer | $0.527 / $0.581 / $0.0203 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001#0 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 3.3s | 0.0048 |
| q_001#1 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 2.3s | 0.0022 |
| q_006#0 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 14 | 26.4s | 0.0179 |
| q_006#1 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 24.1s | 0.0164 |
| q_008#0 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 6.6s | 0.0064 |
| q_008#1 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 5.9s | 0.0063 |
| q_011#0 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 6.6s | 0.0071 |
| q_011#1 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 7.3s | 0.0076 |
| q_012#0 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 13.4s | 0.0184 |
| q_012#1 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 15.0s | 0.0139 |
| q_014#0 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 29.9s | 0.0317 |
| q_014#1 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 39.1s | 0.0362 |
| q_017#0 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 16.7s | 0.0180 |
| q_017#1 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 16.6s | 0.0175 |
| q_018#0 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 3.0s | 0.0030 |
| q_018#1 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 3.6s | 0.0032 |
| q_022#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 18.3s | 0.0137 |
| q_022#1 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 26.1s | 0.0209 |
| q_025#0 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 44.6s | 0.0447 |
| q_025#1 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql | 43x | 36.4s | 0.0277 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 39.2s | 0.0372 |
| x_014#1 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 31.7s | 0.0312 |
| x_036#0 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 29.1s | 0.0248 |
| x_036#1 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 30.8s | 0.0272 |
| x_047#0 | 3 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql | 41, 41, 41 | 49.2s | 0.0485 |
| x_047#1 | 3 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 39.7s | 0.0407 |

**Consistency:** 11/13 questions passed in every run; 11/13 gave the same result in every run. Inconsistent: q_025 (1/2), x_047 (1/2)

## Answer editor (paired: same research, unedited draft vs answer sent)

| Metric | Draft | Sent |
|---|---|---|
| Passed (all answers) | 25/26 | 24/26 |
| Edited answers: words, median | 332 | 251 |
| Edited llm_judge answers: words ÷ gold, median | 6.2x | 4.6x |
| Edited llm_judge answers: fact coverage, mean | 0.96 | 0.96 |
| Edited answers with an unsupported or contradicted claim | 10/18 | 10/18 |

Edited 18/26; left as written (under 120 words) 8; edit rejected by a check: none.
Draft passed, edited failed: q_025#0. Draft failed, edited passed: none.
