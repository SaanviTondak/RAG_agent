# Scorecard: 20261105-1740_tune_glm-5p3_v1_rag

- System: rag | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 17:46

## Headline

**10/18 passed (56%)**, 95% CI 34%–75%; mean score 0.61

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 3 | 100% | 0.95 |
| 2 | 9 | 67% | 0.73 |
| 3 | 6 | 17% | 0.26 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 4 | 75% | 0.71 |
| pdf+sql | 6 | 33% | 0.52 |
| sql | 8 | 62% | 0.62 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 4 | 50% | 0.50 |
| fuzzy_numeric | 3 | 100% | 1.00 |
| llm_judge | 11 | 45% | 0.54 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 50% | 0.54 |
| extra | 8 | 62% | 0.70 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 4/18 |
| Used a source that wasn't required | 8/18 |
| Saw a gold page (questions with gold pages) | 9/10 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 2/18 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 152 / 518 |
| Opening paragraph alone would pass | 7/18 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.46 (full answer 0.54) |
| Latency p50 / p95 / max | 24.7s / 39.0s / 40.4s |
| Tokens in / out (agent) | 57,311 / 50,013 |
| Cost: agent / judge / per answer | $0.266 / $0.010 / $0.0148 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | pdf (missing sql) |  | 10.3s | 0.0072 |
| q_006 | 1 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor. | pdf | 11 | 23.8s | 0.0145 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | pdf (missing sql) |  | 13.2s | 0.0079 |
| q_011 | 2 | exact_match_entity | ❌ | 0.00 | answer names none (gold ['GOOGL']); number: no number matches 15.1 (saw: $33.2 billion, 16%, 23%, $168.9 billion, $14.0 billion, 13%, 365, $352.7 billion) | pdf (missing sql) |  | 25.9s | 0.0139 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf (missing sql) |  | 13.3s | 0.0082 |
| q_014 | 2 | llm_judge | ❌ | 0.53 | 10/19 facts covered; missing: Productivity and Business Processes includes Microsoft 365 Commercial/Consumer.; missing: Productivity and Business Processes incl | pdf (missing sql) |  | 24.7s | 0.0144 |
| q_017 | 2 | llm_judge | ❌ | 0.00 | 0/7 facts covered; missing: Google Services includes Google Search & other; missing: Google Services includes YouTube ads; missing: Google Services includes Goo | pdf |  | 36.7s | 0.0204 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | pdf (missing sql) |  | 19.3s | 0.0140 |
| q_022 | 3 | llm_judge | ❌ | 0.00 | 0/8 facts covered; missing: Alphabet had the largest absolute dollar increase in revenue among the three companies; missing: Alphabet's revenue increased by app | pdf (missing sql) |  | 40.4s | 0.0209 |
| q_025 | 3 | llm_judge | ❌ | 0.00 | 0/12 facts covered; missing: Services revenue grew 12.9% from FY2023 to FY2024 ($85.2B to $96.2B); missing: Services revenue grew 13.5% from FY2024 to FY2025 ($ | pdf (missing sql) |  | 35.4s | 0.0203 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | pdf (missing sql) |  | 32.2s | 0.0202 |
| x_034 | 3 | exact_match_entity | ❌ | 0.00 | answer names none (gold ['GOOGL']); number: no number matches 4.206206154062542 (saw: ) | pdf (missing sql) |  | 34.6s | 0.0205 |
| x_035 | 3 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: The FY2024 10-K cites a one-time income tax charge of $10.2 billion, net; missing: The charge related to the European Commission's S | pdf (missing sql) |  | 35.2s | 0.0205 |
| x_036 | 3 | llm_judge | ❌ | 0.00 | 0/9 facts covered; missing: Microsoft's operating income rose by $19.1 billion (about 17%); missing: Microsoft's operating income was $109.4 billion in FY2024 a | pdf (missing sql) |  | 39.0s | 0.0187 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 18.6s | 0.0095 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf | $43.9 billion, 42 | 9.2s | 0.0061 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | pdf (missing sql) |  | 31.2s | 0.0157 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf (missing sql) |  | 19.9s | 0.0135 |
