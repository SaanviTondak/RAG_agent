# Scorecard: 20261106-1458_tune_glm-5p3_v1_Arep

- System: agent | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-06 15:00

## Headline

**5/6 passed (83%)**, 95% CI 44%–97%; mean score 0.90

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 2 | 100% | 1.00 |
| 3 | 4 | 75% | 0.84 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 2 | 100% | 1.00 |
| 4 multi-part synthesis | 4 | 75% | 0.84 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 4 | 75% | 0.91 |
| pdf+sql | 2 | 100% | 0.88 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 6 | 83% | 0.90 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 4 | 100% | 0.94 |
| extra | 2 | 50% | 0.81 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 6/6 |
| Used a source that wasn't required | 2/6 |
| Saw a gold page (questions with gold pages) | 6/6 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 2/6 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 394 / 538 |
| Answer length ÷ gold answer length (llm_judge, median) | 6.4x |
| Opening paragraph alone would pass | 0/6 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.32 (full answer 0.90) |
| Latency p50 / p95 / max | 25.7s / 33.4s / 33.4s |
| Tokens in / out (agent) | 129,438 / 15,367 |
| Cost: agent / judge / per answer | $0.150 / $0.013 / $0.0250 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 14 | 18.1s | 0.0210 |
| q_006#1 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 22.9s | 0.0235 |
| q_025#0 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K mentions iCloud as part of Services | pdf,sql | 43x | 27.0s | 0.0266 |
| q_025#1 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 33.4s | 0.0286 |
| x_047#0 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql |  | 27.1s | 0.0283 |
| x_047#1 | 3 | llm_judge | ❌ | 0.75 | 6/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 25.7s | 0.0221 |

**Consistency:** 2/3 questions gave the same result in every run. Inconsistent: x_047 (1/2)
