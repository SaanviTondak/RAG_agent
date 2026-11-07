# Scorecard: 20261106-1353_tune_glm-5p3_v4_B

- System: agent | answer model: `glm-5p3` | prompt: v4 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-06 14:00

## Headline

**45/47 passed (96%)**, 95% CI 86%–99%; mean score 0.98

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 92% | 0.98 |
| 2 | 22 | 100% | 1.00 |
| 3 | 12 | 92% | 0.96 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 90% | 0.97 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 7 | 86% | 0.93 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 5 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 9 | 89% | 0.95 |
| pdf+sql | 15 | 93% | 0.98 |
| sql | 21 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 25 | 92% | 0.97 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 80% | 0.94 |
| extra | 37 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 47/47 |
| Used a source that wasn't required | 4/47 |
| Saw a gold page (questions with gold pages) | 23/24 |
| Invalid citations (total) | 1 |
| Answers with numbers not found in any tool output | 1/47 |
| Nudges / fallbacks | 1 / 1 |
| Answer length, words: median / max | 63 / 619 |
| Answer length ÷ gold answer length (llm_judge, median) | 2.4x |
| Opening paragraph alone would pass | 27/47 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.56 (full answer 0.97) |
| Latency p50 / p95 / max | 6.7s / 38.2s / 54.2s |
| Tokens in / out (agent) | 483,236 / 44,008 |
| Cost: agent / judge / per answer | $0.458 / $0.034 / $0.0097 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 2.6s | 0.0024 |
| q_006 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 14.7s | 0.0143 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 4.4s | 0.0044 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 5.5s | 0.0050 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 6.4s | 0.0075 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 38.2s | 0.0335 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 11.4s | 0.0133 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 2.7s | 0.0029 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 12.5s | 0.0107 |
| q_025 | 3 | llm_judge | ❌ | 0.67 | 8/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 54.2s | 0.0471 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 1.7s | 0.0022 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 2.2s | 0.0019 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 2.3s | 0.0021 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 1.4s | 0.0024 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 6.7s | 0.0041 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.2s | 0.0024 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 3.7s | 0.0042 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 3.9s | 0.0034 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 9.5s | 0.0100 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 39.2s | 0.0437 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 4.1s | 0.0051 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 5.5s | 0.0048 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 5.4s | 0.0049 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 11.9s | 0.0083 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.7s | 0.0059 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 10.9s | 0.0103 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 6.3s | 0.0060 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | sql |  | 3.3s | 0.0038 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 3.2s | 0.0032 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 10.2s | 0.0071 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not available in its data, which covers only Apple, Microsoft, and Alphabet, and provides no fabricated fig | sql |  | 3.1s | 0.0024 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states that Microsoft's current stock price is not available in its data sources and does not provide a made-up figure. | sql |  | 6.1s | 0.0035 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 5.4s | 0.0050 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 6.3s | 0.0059 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 14.3s | 0.0111 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 17.8s | 0.0147 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 13.2s | 0.0104 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 9.1s | 0.0109 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 6.7s | 0.0057 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 6.5s | 0.0083 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 15.2s | 0.0138 |
| x_042 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 14.2s | 0.0095 |
| x_043 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 12.5s | 0.0137 |
| x_045 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 14.7s | 0.0138 |
| x_047 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf |  | 27.5s | 0.0250 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 11.6s | 0.0160 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.5s | 0.0111 |
