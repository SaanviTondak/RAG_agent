# Scorecard: 20261106-1526_tune_glm-5p3_v5_plan_fragile

- System: agent + planner | answer model: `glm-5p3` | prompt: v5 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-06 15:30

## Headline

**10/14 passed (71%)**, 95% CI 45%–88%; mean score 0.85

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 4 | 50% | 0.82 |
| 2 | 2 | 100% | 1.00 |
| 3 | 8 | 75% | 0.82 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 4 | 50% | 0.82 |
| 3 figure + explanation | 2 | 100% | 1.00 |
| 4 multi-part synthesis | 8 | 75% | 0.82 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 6 | 67% | 0.84 |
| pdf+sql | 6 | 67% | 0.81 |
| sql | 2 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 14 | 71% | 0.85 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 8 | 50% | 0.76 |
| extra | 6 | 100% | 0.96 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 14/14 |
| Used a source that wasn't required | 2/14 |
| Saw a gold page (questions with gold pages) | 12/12 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/14 |
| Nudges / fallbacks | 0 / 2 |
| Answer length, words: median / max | 400 / 740 |
| Answer length ÷ gold answer length (llm_judge, median) | 6.3x |
| Opening paragraph alone would pass | 0/14 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.30 (full answer 0.85) |
| Latency p50 / p95 / max | 24.1s / 49.8s / 69.9s |
| Tokens in / out (agent) | 298,590 / 46,485 |
| Cost: agent / judge / per answer | $0.447 / $0.026 / $0.0319 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor.; missing: Apple disclosed supply chain disruptions | pdf |  | 18.9s | 0.0179 |
| q_006#1 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 13.6s | 0.0143 |
| q_014#0 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 21.3s | 0.0252 |
| q_014#1 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 24.1s | 0.0258 |
| q_022#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 17.3s | 0.0146 |
| q_022#1 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 21.1s | 0.0164 |
| q_025#0 | 3 | llm_judge | ❌ | 0.42 | 5/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has higher margins; missing: The 10-K says Ser | pdf,sql |  | 49.8s | 0.0525 |
| q_025#1 | 3 | llm_judge | ❌ | 0.42 | 5/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has higher margins; missing: The 10-K says Ser | pdf,sql | 9.3 | 29.5s | 0.0350 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 28.4s | 0.0380 |
| x_014#1 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 25.0s | 0.0354 |
| x_036#0 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 23.2s | 0.0243 |
| x_036#1 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 44.4s | 0.0409 |
| x_047#0 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql | 44 | 69.9s | 0.0688 |
| x_047#1 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql |  | 47.4s | 0.0376 |

**Consistency:** 7/7 questions gave the same result in every run.
