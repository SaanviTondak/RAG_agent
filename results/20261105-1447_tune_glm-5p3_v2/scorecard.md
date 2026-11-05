# Scorecard: 20261105-1447_tune_glm-5p3_v2

- Answer model: `glm-5p3` | prompt: v2 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 15:07

## Headline

**30/32 passed (94%)**, 95% CI 80%–98%; mean score 0.98

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 92% | 0.98 |
| 2 | 15 | 100% | 1.00 |
| 3 | 4 | 75% | 0.92 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 83% | 0.95 |
| pdf+sql | 7 | 86% | 0.95 |
| sql | 17 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 100% | 1.00 |
| llm_judge | 13 | 85% | 0.95 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 80% | 0.94 |
| extra | 22 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 32/32 |
| Used a source that wasn't required | 6/32 |
| Saw a gold page (questions with gold pages) | 12/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 6/32 |
| Nudges / fallbacks | 0 / 2 |
| Answer length, words: median / max | 138 / 972 |
| Opening paragraph alone would pass | 25/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.72 (full answer 0.95) |
| Latency p50 / p95 / max | 9.8s / 46.9s / 53.9s |
| Tokens in / out (agent) | 323,660 / 38,319 |
| Cost: agent / judge / per answer | $0.380 / $0.017 / $0.0119 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql | 52 | 3.8s | 0.0051 |
| q_006 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor.; missing: Apple disclosed supply chain disruptions | pdf |  | 16.0s | 0.0174 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | $137.2 billion, 48.7% | 3.9s | 0.0069 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 6.8s | 0.0054 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.8s | 0.0090 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 53.7s | 0.0360 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 13.3s | 0.0142 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 3.6s | 0.0041 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 41.6s | 0.0280 |
| q_025 | 3 | llm_judge | ❌ | 0.67 | 8/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 53.9s | 0.0440 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 2.0s | 0.0023 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 2.9s | 0.0023 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | pdf,sql |  | 36.9s | 0.0098 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 2.2s | 0.0023 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 6.3s | 0.0048 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.6s | 0.0026 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 6.2s | 0.0050 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql | $32.1 billion | 5.8s | 0.0064 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql | 48.7% | 10.8s | 0.0081 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 46.9s | 0.0614 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 8.4s | 0.0081 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 7.2s | 0.0079 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 35.7s | 0.0063 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 16.2s | 0.0150 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.5s | 0.0111 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 12.3s | 0.0092 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.4s | 0.0101 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 9.5s | 0.0090 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 4.7s | 0.0034 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 16.4s | 0.0141 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its data sources and declines to provide a figure, offering no fabricated information. | sql |  | 4.9s | 0.0031 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data sources and offers only related historical figures from the 10-K without fabricat | pdf |  | 13.8s | 0.0081 |
