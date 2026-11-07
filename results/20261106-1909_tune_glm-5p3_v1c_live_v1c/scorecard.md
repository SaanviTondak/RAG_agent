# Scorecard: 20261106-1909_tune_glm-5p3_v1c_live_v1c

- System: agent | answer model: `glm-5p3` | prompt: v1c | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 3 | graded 2026-11-06 19:13

## Headline

**15/21 passed (71%)**, 95% CI 50%–86%; mean score 0.87

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 6 | 50% | 0.73 |
| 2 | 3 | 100% | 1.00 |
| 3 | 12 | 75% | 0.91 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 6 | 50% | 0.73 |
| 3 figure + explanation | 3 | 100% | 1.00 |
| 4 multi-part synthesis | 12 | 75% | 0.91 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 9 | 44% | 0.75 |
| pdf+sql | 9 | 89% | 0.95 |
| sql | 3 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 21 | 71% | 0.87 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 12 | 67% | 0.85 |
| extra | 9 | 78% | 0.91 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 21/21 |
| Used a source that wasn't required | 5/21 |
| Saw a gold page (questions with gold pages) | 18/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 9/21 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 337 / 554 |
| Answer length ÷ gold answer length (llm_judge, median) | 5.5x |
| Opening paragraph alone would pass | 0/21 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.31 (full answer 0.87) |
| Latency p50 / p95 / max | 24.4s / 33.1s / 35.5s |
| Tokens in / out (agent) | 430,132 / 47,575 |
| Cost: agent / judge / per answer | $0.490 / $0.043 / $0.0233 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ❌ | 0.43 | 3/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 14.9s | 0.0139 |
| q_006#1 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 13.9s | 0.0131 |
| q_006#2 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 13.2s | 0.0110 |
| q_014#0 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 20.7s | 0.0260 |
| q_014#1 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 26.3s | 0.0460 |
| q_014#2 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 20.1s | 0.0216 |
| q_022#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql | $26.4B | 35.5s | 0.0234 |
| q_022#1 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql | $26.4B | 24.4s | 0.0195 |
| q_022#2 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | 31 | 15.5s | 0.0141 |
| q_025#0 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql | 9.3 | 28.6s | 0.0228 |
| q_025#1 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql | $306.9B | 25.7s | 0.0228 |
| q_025#2 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K mentions iCloud as part of Services | pdf,sql | 9.3 | 22.4s | 0.0205 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 33.1s | 0.0372 |
| x_014#1 | 1 | llm_judge | ✅ | 0.83 | 5/6 facts covered; missing: Microsoft's FY2025 10-K discloses intense and rapidly evolving competition in AI, including from open AI models. | pdf | 20 | 24.6s | 0.0339 |
| x_014#2 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 27, 20 | 26.8s | 0.0342 |
| x_036#0 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 24.5s | 0.0233 |
| x_036#1 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 20.6s | 0.0182 |
| x_036#2 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 23.1s | 0.0228 |
| x_047#0 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql |  | 25.1s | 0.0251 |
| x_047#1 | 3 | llm_judge | ❌ | 0.75 | 6/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 29.0s | 0.0250 |
| x_047#2 | 3 | llm_judge | ❌ | 0.75 | 6/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 21.5s | 0.0155 |

**Consistency:** 5/7 questions gave the same result in every run. Inconsistent: q_025 (2/3), x_047 (1/3)
