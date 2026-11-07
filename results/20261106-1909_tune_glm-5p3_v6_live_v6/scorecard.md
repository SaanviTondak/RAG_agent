# Scorecard: 20261106-1909_tune_glm-5p3_v6_live_v6

- System: agent | answer model: `glm-5p3` | prompt: v6 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 3 | graded 2026-11-06 19:14

## Headline

**16/21 passed (76%)**, 95% CI 55%–89%; mean score 0.84

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 6 | 83% | 0.90 |
| 2 | 3 | 100% | 1.00 |
| 3 | 12 | 67% | 0.76 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 6 | 83% | 0.90 |
| 3 figure + explanation | 3 | 100% | 1.00 |
| 4 multi-part synthesis | 12 | 67% | 0.76 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 9 | 56% | 0.69 |
| pdf+sql | 9 | 89% | 0.94 |
| sql | 3 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 21 | 76% | 0.84 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 12 | 83% | 0.90 |
| extra | 9 | 67% | 0.75 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 21/21 |
| Used a source that wasn't required | 0/21 |
| Saw a gold page (questions with gold pages) | 18/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 5/21 |
| Nudges / fallbacks | 0 / 6 |
| Answer length, words: median / max | 381 / 791 |
| Answer length ÷ gold answer length (llm_judge, median) | 7.7x |
| Opening paragraph alone would pass | 0/21 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.33 (full answer 0.84) |
| Latency p50 / p95 / max | 23.8s / 76.6s / 87.7s |
| Tokens in / out (agent) | 477,508 / 71,201 |
| Cost: agent / judge / per answer | $0.658 / $0.036 / $0.0313 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor.; missing: Apple disclosed supply chain disruptions | pdf |  | 14.3s | 0.0144 |
| q_006#1 | 1 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor. | pdf |  | 22.5s | 0.0220 |
| q_006#2 | 1 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor. | pdf |  | 22.4s | 0.0225 |
| q_014#0 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 20.6s | 0.0222 |
| q_014#1 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 32.9s | 0.0246 |
| q_014#2 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 18.5s | 0.0266 |
| q_022#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 16.3s | 0.0151 |
| q_022#1 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | −0.2%, −0.6% | 15.4s | 0.0151 |
| q_022#2 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | −0.2%, −0.6% | 18.3s | 0.0125 |
| q_025#0 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 31.5s | 0.0324 |
| q_025#1 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions Apple Music as part of Services; missin | pdf,sql | 20 | 35.4s | 0.0331 |
| q_025#2 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 43.7s | 0.0431 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 36.8s | 0.0404 |
| x_014#1 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf |  | 43.1s | 0.0347 |
| x_014#2 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 35.6s | 0.0450 |
| x_036#0 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 21.0s | 0.0204 |
| x_036#1 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 21.4s | 0.0179 |
| x_036#2 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 23.8s | 0.0199 |
| x_047#0 | 3 | llm_judge | ❌ | 0.00 | 0/8 facts covered; missing: Microsoft says scaling its AI infrastructure lowered its gross margin percentage; missing: Microsoft Cloud gross margin percentage d | pdf |  | 76.6s | 0.0646 |
| x_047#1 | 3 | llm_judge | ❌ | 0.75 | 6/8 facts covered; missing: Alphabet expects to significantly increase its investment in technical infrastructure in 2026; missing: Google Cloud's operating inc | pdf |  | 87.7s | 0.0818 |
| x_047#2 | 3 | llm_judge | ❌ | 0.00 | 0/8 facts covered; missing: Microsoft says scaling its AI infrastructure lowered its gross margin percentage; missing: Microsoft Cloud gross margin percentage d | pdf |  | 49.6s | 0.0500 |

**Consistency:** 5/7 questions gave the same result in every run. Inconsistent: q_006 (2/3), q_025 (2/3)
