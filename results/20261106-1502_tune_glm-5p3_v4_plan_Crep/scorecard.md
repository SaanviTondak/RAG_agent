# Scorecard: 20261106-1502_tune_glm-5p3_v4_plan_Crep

- System: agent + planner | answer model: `glm-5p3` | prompt: v4 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-06 15:03

## Headline

**4/6 passed (67%)**, 95% CI 30%–90%; mean score 0.83

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 2 | 50% | 0.86 |
| 3 | 4 | 75% | 0.82 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 2 | 50% | 0.86 |
| 4 multi-part synthesis | 4 | 75% | 0.82 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 4 | 50% | 0.83 |
| pdf+sql | 2 | 100% | 0.83 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 6 | 67% | 0.83 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 4 | 75% | 0.84 |
| extra | 2 | 50% | 0.81 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 6/6 |
| Used a source that wasn't required | 2/6 |
| Saw a gold page (questions with gold pages) | 6/6 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 0/6 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 326 / 492 |
| Answer length ÷ gold answer length (llm_judge, median) | 5.1x |
| Opening paragraph alone would pass | 0/6 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.33 (full answer 0.83) |
| Latency p50 / p95 / max | 30.2s / 40.4s / 40.4s |
| Tokens in / out (agent) | 137,553 / 17,109 |
| Cost: agent / judge / per answer | $0.176 / $0.015 / $0.0294 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor.; missing: Apple disclosed supply chain disruptions | pdf |  | 15.0s | 0.0130 |
| q_006#1 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 31.8s | 0.0282 |
| q_025#0 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 30.2s | 0.0396 |
| q_025#1 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 31.1s | 0.0329 |
| x_047#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 40.4s | 0.0374 |
| x_047#1 | 3 | llm_judge | ❌ | 0.62 | 5/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Alphabet expects to significantly increase  | pdf,sql |  | 27.5s | 0.0254 |

**Consistency:** 1/3 questions gave the same result in every run. Inconsistent: q_006 (1/2), x_047 (1/2)
