# Scorecard: 20261106-1353_tune_glm-5p3_v4_plan_C

- System: agent + planner | answer model: `glm-5p3` | prompt: v4 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-06 14:01

## Headline

**43/43 passed (100%)**, 95% CI 92%–100%; mean score 1.00

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 20 | 100% | 1.00 |
| 3 | 10 | 100% | 0.98 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 100% | 1.00 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 6 | 100% | 0.97 |
| 5 dependent multi-hop | 1 | 100% | 1.00 |
| 6 cross-check / data conflict | 4 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 8 | 100% | 1.00 |
| pdf+sql | 13 | 100% | 0.99 |
| sql | 20 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 21 | 100% | 0.99 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.98 |
| extra | 33 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 43/43 |
| Used a source that wasn't required | 3/43 |
| Saw a gold page (questions with gold pages) | 21/21 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 1/43 |
| Nudges / fallbacks | 0 / 2 |
| Answer length, words: median / max | 63 / 614 |
| Answer length ÷ gold answer length (llm_judge, median) | 2.8x |
| Opening paragraph alone would pass | 25/43 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.53 (full answer 0.99) |
| Latency p50 / p95 / max | 11.5s / 41.4s / 52.3s |
| Tokens in / out (agent) | 491,794 / 59,276 |
| Cost: agent / judge / per answer | $0.530 / $0.027 / $0.0123 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 2.8s | 0.0023 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 21.2s | 0.0234 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 4.4s | 0.0043 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 8.5s | 0.0093 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 23.2s | 0.0169 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 41.4s | 0.0310 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 28.7s | 0.0274 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 3.0s | 0.0025 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 16.3s | 0.0128 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 52.3s | 0.0406 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 1.4s | 0.0020 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 1.7s | 0.0019 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 2.2s | 0.0020 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 1.3s | 0.0018 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 11.3s | 0.0082 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 1.7s | 0.0021 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 3.4s | 0.0037 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 3.1s | 0.0032 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 15.2s | 0.0112 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 45.9s | 0.0608 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 3.8s | 0.0040 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 5.4s | 0.0048 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 4.3s | 0.0029 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 18.3s | 0.0158 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 24.6s | 0.0181 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 24.3s | 0.0176 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 13.6s | 0.0100 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | sql |  | 3.3s | 0.0034 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 11.5s | 0.0071 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 9.9s | 0.0067 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not available in its data, which covers only Apple, Microsoft, and Alphabet, and provides no fabricated fig | sql |  | 3.9s | 0.0023 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states that Microsoft's current stock price is not available in its sources and only provides a related historical repurchase price from the  | pdf |  | 16.3s | 0.0116 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 9.1s | 0.0077 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 5.8s | 0.0050 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 25.7s | 0.0230 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 20.9s | 0.0183 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 28.0s | 0.0194 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 12.7s | 0.0149 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 15.2s | 0.0122 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 6.1s | 0.0046 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 14.5s | 0.0152 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 17.8s | 0.0199 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 29.9s | 0.0186 |
