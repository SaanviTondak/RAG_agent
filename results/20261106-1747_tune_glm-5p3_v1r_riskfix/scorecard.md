# Scorecard: 20261106-1747_tune_glm-5p3_v1r_riskfix

- System: agent | answer model: `glm-5p3` | prompt: v1r | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 3 | graded 2026-11-06 17:49

## Headline

**6/6 passed (100%)**, 95% CI 61%–100%; mean score 1.00

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 6 | 100% | 1.00 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 6 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 6 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 6 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 3 | 100% | 1.00 |
| extra | 3 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 6/6 |
| Used a source that wasn't required | 0/6 |
| Saw a gold page (questions with gold pages) | 6/6 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/6 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 501 / 713 |
| Answer length ÷ gold answer length (llm_judge, median) | 8.1x |
| Opening paragraph alone would pass | 0/6 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.27 (full answer 1.00) |
| Latency p50 / p95 / max | 17.3s / 36.0s / 36.0s |
| Tokens in / out (agent) | 114,300 / 15,572 |
| Cost: agent / judge / per answer | $0.141 / $0.009 / $0.0235 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 17.3s | 0.0193 |
| q_006#1 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 16.9s | 0.0138 |
| q_006#2 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 13, 14 | 12.5s | 0.0091 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 17, 22, 20 | 28.7s | 0.0297 |
| x_014#1 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 31.1s | 0.0392 |
| x_014#2 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 36.0s | 0.0301 |

**Consistency:** 2/2 questions gave the same result in every run.
