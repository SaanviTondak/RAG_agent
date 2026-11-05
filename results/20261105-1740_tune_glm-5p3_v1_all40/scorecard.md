# Scorecard: 20261105-1740_tune_glm-5p3_v1_all40

- System: agent | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 17:41

## Headline

**40/40 passed (100%)**, 95% CI 91%–100%; mean score 1.00

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 19 | 100% | 1.00 |
| 3 | 8 | 100% | 0.98 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 8 | 100% | 1.00 |
| pdf+sql | 10 | 100% | 0.98 |
| sql | 20 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 18 | 100% | 0.99 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.98 |
| extra | 30 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 40/40 |
| Used a source that wasn't required | 7/40 |
| Saw a gold page (questions with gold pages) | 17/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 5/40 |
| Nudges / fallbacks | 0 / 1 |
| Answer length, words: median / max | 121 / 568 |
| Opening paragraph alone would pass | 28/40 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.64 (full answer 0.99) |
| Latency p50 / p95 / max | 8.7s / 40.9s / 56.0s |
| Tokens in / out (agent) | 389,674 / 40,390 |
| Cost: agent / judge / per answer | $0.408 / $0.027 / $0.0102 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 3.1s | 0.0046 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 36.9s | 0.0231 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | pdf,sql | 48.7% | 9.8s | 0.0106 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 6.1s | 0.0075 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 8.4s | 0.0083 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 48.1s | 0.0354 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 13.1s | 0.0121 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 4.0s | 0.0029 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 32.7s | 0.0214 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 33.3s | 0.0301 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 2.2s | 0.0024 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 7.5s | 0.0077 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 3.2s | 0.0023 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 2.5s | 0.0025 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 6.4s | 0.0052 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.4s | 0.0025 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 5.1s | 0.0042 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 5.0s | 0.0036 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 11.5s | 0.0083 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 24.0s | 0.0337 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 6.0s | 0.0057 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 56.0s | 0.0053 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 8.4s | 0.0072 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 40.9s | 0.0106 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.3s | 0.0072 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 10.5s | 0.0086 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.2s | 0.0074 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | sql | 59.7% | 5.0s | 0.0043 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 4.0s | 0.0032 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 13.3s | 0.0121 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its data sources and does not provide a made-up revenue figure. | sql | 10 | 4.1s | 0.0029 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data and provides only related historical/contextual figures without inventing a curre | pdf |  | 14.1s | 0.0092 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 6.9s | 0.0078 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 8.7s | 0.0099 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 15.3s | 0.0141 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 31.0s | 0.0238 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 22.5s | 0.0166 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 10.8s | 0.0107 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 6.5s | 0.0055 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 8.5s | 0.0074 |
