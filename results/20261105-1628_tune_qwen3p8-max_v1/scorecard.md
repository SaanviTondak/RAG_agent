# Scorecard: 20261105-1628_tune_qwen3p8-max_v1

- Answer model: `qwen3p8-max` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:32

## Headline

**32/32 passed (100%)**, 95% CI 89%–100%; mean score 0.99

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 15 | 100% | 1.00 |
| 3 | 4 | 100% | 0.96 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 100% | 1.00 |
| pdf+sql | 7 | 100% | 0.98 |
| sql | 17 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 100% | 1.00 |
| llm_judge | 13 | 100% | 0.99 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.98 |
| extra | 22 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 32/32 |
| Used a source that wasn't required | 12/32 |
| Saw a gold page (questions with gold pages) | 12/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 10/32 |
| Nudges / fallbacks | 0 / 4 |
| Answer length, words: median / max | 169 / 794 |
| Opening paragraph alone would pass | 23/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.56 (full answer 0.99) |
| Latency p50 / p95 / max | 11.2s / 37.8s / 78.9s |
| Tokens in / out (agent) | 586,930 / 37,337 |
| Cost: agent / judge / per answer | $0.815 / $0.018 / $0.0255 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | pdf,sql |  | 12.3s | 0.0171 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 32.3s | 0.0909 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | 48.7% | 5.3s | 0.0098 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql | 0.16 percentage points | 5.8s | 0.0108 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 27.7s | 0.0628 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 18.5s | 0.0360 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 12.0s | 0.0226 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.5x | 8.2s | 0.0128 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 53.9s | 0.0320 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql | 43x | 78.9s | 0.0666 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 3.6s | 0.0091 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 16.2s | 0.0206 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | pdf,sql |  | 24.4s | 0.0151 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 4.7s | 0.0096 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql | 13.6 percentage points | 6.1s | 0.0119 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql | $121.1 billion | 3.3s | 0.0079 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 8.7s | 0.0141 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | pdf,sql |  | 37.1s | 0.0191 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 34.4s | 0.0311 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20, 26 | 37.8s | 0.0912 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 9.5s | 0.0198 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 8.9s | 0.0220 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf,sql | $31.2 billion | 9.6s | 0.0168 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 13.3s | 0.0252 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 10.1s | 0.0192 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 10.4s | 0.0197 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql | 42.6 | 11.2s | 0.0214 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 10.3s | 0.0182 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 6.6s | 0.0125 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 16.7s | 0.0252 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its sources and offers no fabricated revenue figure, only related available alternatives. | sql | 10 | 2.4s | 0.0072 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states that current stock price is not available in its data and only provides related historical information without fabricating a current p | pdf,sql |  | 13.0s | 0.0165 |
