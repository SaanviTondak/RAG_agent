# Scorecard: 20261106-1500_tune_glm-5p3_v4_Brep

- System: agent | answer model: `glm-5p3` | prompt: v4 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-06 15:02

## Headline

**1/6 passed (17%)**, 95% CI 3%–56%; mean score 0.69

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 2 | 0% | 0.57 |
| 3 | 4 | 25% | 0.75 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 2 | 0% | 0.57 |
| 4 multi-part synthesis | 4 | 25% | 0.75 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 4 | 25% | 0.66 |
| pdf+sql | 2 | 0% | 0.75 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 6 | 17% | 0.69 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 4 | 0% | 0.66 |
| extra | 2 | 50% | 0.75 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 6/6 |
| Used a source that wasn't required | 0/6 |
| Saw a gold page (questions with gold pages) | 6/6 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 0/6 |
| Nudges / fallbacks | 0 / 1 |
| Answer length, words: median / max | 334 / 505 |
| Answer length ÷ gold answer length (llm_judge, median) | 4.3x |
| Opening paragraph alone would pass | 0/6 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.20 (full answer 0.69) |
| Latency p50 / p95 / max | 23.4s / 53.8s / 53.8s |
| Tokens in / out (agent) | 99,756 / 16,359 |
| Cost: agent / judge / per answer | $0.147 / $0.019 / $0.0245 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 13.7s | 0.0094 |
| q_006#1 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 15.1s | 0.0137 |
| q_025#0 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 34.3s | 0.0242 |
| q_025#1 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 53.8s | 0.0457 |
| x_047#0 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf |  | 24.6s | 0.0273 |
| x_047#1 | 3 | llm_judge | ❌ | 0.62 | 5/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Alphabet expects to significantly increase  | pdf |  | 23.4s | 0.0267 |

**Consistency:** 2/3 questions gave the same result in every run. Inconsistent: x_047 (1/2)
