# Scorecard: 20261105-1628_tune_kimi-k3_v1

- Answer model: `kimi-k3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:32

## Headline

**31/32 passed (97%)**, 95% CI 84%–99%; mean score 0.97

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 0.99 |
| 2 | 15 | 100% | 1.00 |
| 3 | 4 | 75% | 0.81 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 100% | 0.97 |
| pdf+sql | 7 | 86% | 0.89 |
| sql | 17 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 100% | 1.00 |
| llm_judge | 13 | 92% | 0.93 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.99 |
| extra | 22 | 95% | 0.96 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 32/32 |
| Used a source that wasn't required | 5/32 |
| Saw a gold page (questions with gold pages) | 12/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/32 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 116 / 513 |
| Opening paragraph alone would pass | 19/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.39 (full answer 0.93) |
| Latency p50 / p95 / max | 13.3s / 35.5s / 74.3s |
| Tokens in / out (agent) | 265,099 / 21,392 |
| Cost: agent / judge / per answer | $0.920 / $0.019 / $0.0288 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 10.0s | 0.0170 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 27.8s | 0.0576 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 8.1s | 0.0203 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql | 31, 30, 12 | 12.1s | 0.0238 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 17.1s | 0.0303 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 33.4s | 0.0476 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 23.0s | 0.0365 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 13.0s | 0.0212 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 66.1s | 0.0549 |
| q_025 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 74.3s | 0.0534 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 5.0s | 0.0168 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 4.3s | 0.0165 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 7.7s | 0.0163 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 7.0s | 0.0165 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 10.5s | 0.0196 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 7.4s | 0.0175 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 13.3s | 0.0229 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql | $32.1 billion | 9.9s | 0.0197 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 12.6s | 0.0236 |
| x_014 | 1 | llm_judge | ✅ | 0.83 | 5/6 facts covered; missing: Microsoft's FY2025 10-K discloses significant costs to build AI and cloud infrastructure that reduce operating margins. | pdf | 20, 22 | 35.5s | 0.0665 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 16.3s | 0.0259 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 11.5s | 0.0257 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 9.4s | 0.0238 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 17.0s | 0.0312 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 18.2s | 0.0321 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 17.9s | 0.0323 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 22.8s | 0.0339 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 19.1s | 0.0282 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 7.1s | 0.0192 |
| x_029 | 3 | llm_judge | ❌ | 0.33 | 1/3 facts covered; missing: The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud.; missing: The $105.4 billion figure was reported under the | pdf,sql |  | 13.6s | 0.0288 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not in its sources, explains the data covers only Apple, Microsoft, and Alphabet, and offers no fabricated  | sql |  | 11.4s | 0.0176 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Microsoft's current stock price is not available in its sources and offers only related available fundamentals without fabricating a f | sql |  | 13.7s | 0.0231 |
