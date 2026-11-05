# Scorecard: 20261105-1632_tune_minimax-m3_v1

- Answer model: `minimax-m3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:35

## Headline

**29/32 passed (91%)**, 95% CI 76%–97%; mean score 0.96

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 15 | 93% | 0.98 |
| 3 | 4 | 50% | 0.77 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 100% | 1.00 |
| pdf+sql | 7 | 57% | 0.84 |
| sql | 17 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 100% | 1.00 |
| llm_judge | 13 | 77% | 0.91 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 90% | 0.96 |
| extra | 22 | 91% | 0.96 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 31/32 |
| Used a source that wasn't required | 5/32 |
| Saw a gold page (questions with gold pages) | 12/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 9/32 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 112 / 480 |
| Opening paragraph alone would pass | 19/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.39 (full answer 0.91) |
| Latency p50 / p95 / max | 3.5s / 50.3s / 65.1s |
| Tokens in / out (agent) | 276,467 / 19,699 |
| Cost: agent / judge / per answer | $0.056 / $0.021 / $0.0018 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 1.4s | 0.0006 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 65.1s | 0.0045 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | $137.2 billion, 48.7% | 2.0s | 0.0016 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 3.0s | 0.0018 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 40.1s | 0.0022 |
| q_014 | 2 | llm_judge | ✅ | 0.90 | 17/19 facts covered; missing: Productivity and Business Processes includes LinkedIn.; missing: Productivity and Business Processes includes Dynamics. | pdf,sql |  | 9.0s | 0.0027 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 50.3s | 0.0029 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 2.4s | 0.0016 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql | $53.3B | 30.6s | 0.0045 |
| q_025 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions Apple Music as part of Services; missin | pdf,sql |  | 31.7s | 0.0038 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 1.1s | 0.0005 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 47.9s | 0.0017 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 1.5s | 0.0006 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 1.1s | 0.0006 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql | 13, 14 percentage points | 2.9s | 0.0011 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql | $13.3 billion, $134.4 billion | 1.6s | 0.0008 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 3.1s | 0.0013 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql | $32.1 billion | 1.9s | 0.0010 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 3.9s | 0.0017 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 18, 44 | 54.8s | 0.0045 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf | $164.8 billion | 27.1s | 0.0012 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 27.0s | 0.0014 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 3.2s | 0.0014 |
| x_020 | 2 | llm_judge | ❌ | 0.88 | 7/8 facts covered; contradicted: The increase was 21.5%. | pdf,sql |  | 22.9s | 0.0022 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 20.9s | 0.0017 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 19.5s | 0.0024 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | sql | 42.8%, 26.7%, 15.5%, 8.1% | 3.5s | 0.0012 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 10.0s | 0.0018 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 1.5s | 0.0007 |
| x_029 | 3 | llm_judge | ❌ | 0.33 | 1/3 facts covered; missing: The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud.; missing: The $105.4 billion figure was reported under the | sql (missing pdf) |  | 2.0s | 0.0008 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its data sources and provides no fabricated revenue figure. | sql |  | 1.5s | 0.0006 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Microsoft's current stock price is not available in the provided sources and does not present a made-up figure. | sql |  | 2.0s | 0.0008 |
