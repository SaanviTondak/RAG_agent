# Scorecard: 20261105-1740_tune_glm-5p3_v1_norerank

- System: agent | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: False | set: tune | runs per question: 1 | graded 2026-11-05 17:44

## Headline

**17/18 passed (94%)**, 95% CI 74%–99%; mean score 0.94

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 5 | 80% | 0.80 |
| 2 | 9 | 100% | 1.00 |
| 3 | 4 | 100% | 0.98 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 8 | 88% | 0.88 |
| pdf+sql | 10 | 100% | 0.99 |

| Grader | n | pass | mean score |
|---|---|---|---|
| fuzzy_numeric | 4 | 75% | 0.75 |
| llm_judge | 14 | 100% | 0.99 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 5 | 100% | 0.98 |
| extra | 13 | 92% | 0.92 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 18/18 |
| Used a source that wasn't required | 1/18 |
| Saw a gold page (questions with gold pages) | 16/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 0/18 |
| Nudges / fallbacks | 0 / 1 |
| Answer length, words: median / max | 173 / 561 |
| Opening paragraph alone would pass | 6/18 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.62 (full answer 0.99) |
| Latency p50 / p95 / max | 14.0s / 31.7s / 34.1s |
| Tokens in / out (agent) | 264,866 / 27,069 |
| Cost: agent / judge / per answer | $0.293 / $0.015 / $0.0163 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 19.9s | 0.0243 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 8.7s | 0.0108 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 24.8s | 0.0307 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 13.6s | 0.0144 |
| q_025 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 34.1s | 0.0335 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf |  | 31.7s | 0.0372 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 7.2s | 0.0073 |
| x_017 | 1 | fuzzy_numeric | ❌ | 0.00 | no number matches 45400000000 (saw: $45.7 billion, 31, 8, $45,709 million, $62,222 million, 26.5%, 11, 8) | pdf |  | 15.2s | 0.0186 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 4.5s | 0.0050 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 12.2s | 0.0118 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.4s | 0.0089 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 11.3s | 0.0082 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 14.0s | 0.0123 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 19.0s | 0.0198 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 17.7s | 0.0172 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 14.1s | 0.0127 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 15.2s | 0.0116 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 8.0s | 0.0088 |
