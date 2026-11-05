# Scorecard: 20261105-1635_tune_glm-5p3-flash_v1

- Answer model: `glm-5p3-flash` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:38

## Headline

**31/32 passed (97%)**, 95% CI 84%–99%; mean score 0.97

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 15 | 100% | 1.00 |
| 3 | 4 | 75% | 0.79 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 100% | 1.00 |
| pdf+sql | 7 | 86% | 0.88 |
| sql | 17 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 100% | 1.00 |
| llm_judge | 13 | 92% | 0.94 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.98 |
| extra | 22 | 95% | 0.97 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 31/32 |
| Used a source that wasn't required | 10/32 |
| Saw a gold page (questions with gold pages) | 10/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 6/32 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 115 / 641 |
| Opening paragraph alone would pass | 21/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.54 (full answer 0.94) |
| Latency p50 / p95 / max | 8.0s / 49.8s / 88.6s |
| Tokens in / out (agent) | 324,719 / 25,075 |
| Cost: agent / judge / per answer | $0.035 / $0.017 / $0.0011 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql | 52 | 3.3s | 0.0006 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 31.9s | 0.0024 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | 48.7% | 4.3s | 0.0007 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 4.4s | 0.0007 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 28.7s | 0.0009 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 88.6s | 0.0025 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 49.6s | 0.0013 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 3.5s | 0.0004 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 49.8s | 0.0024 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 52.7s | 0.0026 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | pdf,sql |  | 25.4s | 0.0007 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 10.9s | 0.0009 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 19.6s | 0.0008 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 3.1s | 0.0003 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql | 13.6 percentage points | 4.3s | 0.0005 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.9s | 0.0003 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 4.0s | 0.0008 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql | $32.1 billion, 132.2, − 100.1, 100.1 | 3.5s | 0.0004 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 10.6s | 0.0011 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 17, 22, 22, 20 | 24.2s | 0.0043 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf,sql |  | 7.8s | 0.0012 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf,sql |  | 6.5s | 0.0008 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 6.8s | 0.0008 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 16.2s | 0.0014 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 8.0s | 0.0007 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 8.2s | 0.0014 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 10.3s | 0.0013 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 10.0s | 0.0012 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 3.2s | 0.0006 |
| x_029 | 3 | llm_judge | ❌ | 0.33 | 1/3 facts covered; missing: The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud.; missing: The $105.4 billion figure was reported under the | sql (missing pdf) |  | 4.5s | 0.0004 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its data, provides no fabricated revenue figure, and only offers related information about the three companie | sql |  | 5.8s | 0.0005 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Microsoft's current stock price is not available in its sources and offers only related fundamentals, without presenting any made-up f | sql |  | 3.9s | 0.0003 |
