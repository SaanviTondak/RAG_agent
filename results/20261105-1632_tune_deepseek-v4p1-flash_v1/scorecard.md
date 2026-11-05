# Scorecard: 20261105-1632_tune_deepseek-v4p1-flash_v1

- Answer model: `deepseek-v4p1-flash` | prompt: v1 | judge: `kimi-k3` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:36

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
| Used a source that wasn't required | 9/32 |
| Saw a gold page (questions with gold pages) | 13/13 |
| Invalid citations (total) | 6 |
| Answers with numbers not found in any tool output | 8/32 |
| Nudges / fallbacks | 0 / 3 |
| Answer length, words: median / max | 150 / 618 |
| Opening paragraph alone would pass | 23/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.61 (full answer 0.99) |
| Latency p50 / p95 / max | 10.4s / 82.6s / 140.7s |
| Tokens in / out (agent) | 472,486 / 26,386 |
| Cost: agent / judge / per answer | $0.086 / $0.172 / $0.0027 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 4.4s | 0.0004 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 40.8s | 0.0042 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 6.1s | 0.0009 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | pdf,sql |  | 84.2s | 0.0032 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 140.7s | 0.0085 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 82.6s | 0.0038 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 35.1s | 0.0024 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 5.8s | 0.0010 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql | 30 | 46.7s | 0.0058 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql | 45x | 62.9s | 0.0068 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql | 36.1% | 2.8s | 0.0006 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 27.3s | 0.0017 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 4.2s | 0.0005 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 3.5s | 0.0005 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | pdf,sql |  | 18.1s | 0.0028 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql | 12 | 4.0s | 0.0005 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql | 31 | 7.2s | 0.0015 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql | $32.1 billion | 4.3s | 0.0006 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 16.3s | 0.0037 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 29 | 30.3s | 0.0133 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 10.4s | 0.0027 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 7.7s | 0.0021 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 9.7s | 0.0024 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 10.5s | 0.0021 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.5s | 0.0024 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 10.5s | 0.0025 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 13.7s | 0.0020 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 9.6s | 0.0016 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 3.6s | 0.0008 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 12.8s | 0.0034 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by the available data, provides no fabricated figure, and offers related information for the covered companies i | sql |  | 3.3s | 0.0004 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states that Microsoft's current stock price is not available in its data sources, explains why, and does not fabricate any figure. | sql | 10 | 4.9s | 0.0007 |
