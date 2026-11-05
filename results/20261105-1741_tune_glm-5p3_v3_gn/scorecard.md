# Scorecard: 20261105-1741_tune_glm-5p3_v3_gn

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v3 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 17:48

## Headline

**39/40 passed (98%)**, 95% CI 87%–100%; mean score 0.99

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 92% | 0.97 |
| 2 | 19 | 100% | 1.00 |
| 3 | 8 | 100% | 0.98 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 8 | 88% | 0.95 |
| pdf+sql | 10 | 100% | 0.98 |
| sql | 20 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 18 | 94% | 0.97 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 90% | 0.94 |
| extra | 30 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 40/40 |
| Used a source that wasn't required | 8/40 |
| Saw a gold page (questions with gold pages) | 17/18 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 3/40 |
| Nudges / fallbacks | 0 / 1 |
| Answer length, words: median / max | 143 / 589 |
| Opening paragraph alone would pass | 32/40 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.74 (full answer 0.97) |
| Latency p50 / p95 / max | 10.0s / 30.9s / 56.3s |
| Tokens in / out (agent) | 397,396 / 43,045 |
| Cost: agent / judge / per answer | $0.413 / $0.019 / $0.0103 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql | 52 | 3.0s | 0.0024 |
| q_006 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 19.4s | 0.0156 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | pdf,sql |  | 8.2s | 0.0069 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 5.7s | 0.0045 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 16.2s | 0.0084 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 30.9s | 0.0256 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 19.1s | 0.0110 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 11.7s | 0.0032 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 29.7s | 0.0210 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 56.3s | 0.0393 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 2.4s | 0.0026 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 11.9s | 0.0078 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 4.1s | 0.0022 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 3.3s | 0.0023 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 5.6s | 0.0030 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.9s | 0.0027 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 5.4s | 0.0043 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 5.8s | 0.0034 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 11.8s | 0.0080 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 33.3s | 0.0342 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 7.3s | 0.0080 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 6.3s | 0.0054 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 5.9s | 0.0053 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 11.6s | 0.0115 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.6s | 0.0082 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 12.5s | 0.0095 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 9.8s | 0.0075 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 9.7s | 0.0091 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 3.5s | 0.0031 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 17.0s | 0.0133 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not in its data, names the covered companies, and offers no fabricated figure. | sql |  | 3.8s | 0.0026 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data and provides only related, sourced figures without fabricating a live price. | pdf |  | 12.9s | 0.0073 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 6.0s | 0.0050 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 8.0s | 0.0067 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 15.3s | 0.0126 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 28.7s | 0.0334 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 18.2s | 0.0130 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 14.4s | 0.0209 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | pdf,sql |  | 12.9s | 0.0124 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 10.0s | 0.0097 |
