# Scorecard: 20261105-1740_tune_glm-5p3_v1_pipeline

- System: pipeline | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 17:43

## Headline

**13/18 passed (72%)**, 95% CI 49%–88%; mean score 0.78

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 3 | 67% | 0.86 |
| 2 | 9 | 89% | 0.94 |
| 3 | 6 | 50% | 0.50 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 4 | 75% | 0.89 |
| pdf+sql | 6 | 50% | 0.57 |
| sql | 8 | 88% | 0.88 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 4 | 100% | 1.00 |
| fuzzy_numeric | 3 | 100% | 1.00 |
| llm_judge | 11 | 55% | 0.64 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 60% | 0.70 |
| extra | 8 | 88% | 0.88 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 16/18 |
| Used a source that wasn't required | 9/18 |
| Saw a gold page (questions with gold pages) | 10/10 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 2/18 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 151 / 461 |
| Opening paragraph alone would pass | 11/18 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.56 (full answer 0.64) |
| Latency p50 / p95 / max | 30.6s / 74.8s / 78.3s |
| Tokens in / out (agent) | 90,697 / 67,623 |
| Cost: agent / judge / per answer | $0.364 / $0.011 / $0.0202 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | pdf,sql |  | 10.9s | 0.0078 |
| q_006 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 22.0s | 0.0163 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | pdf,sql |  | 10.7s | 0.0092 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | pdf,sql |  | 15.0s | 0.0117 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 37.8s | 0.0221 |
| q_014 | 2 | llm_judge | ❌ | 0.42 | 8/19 facts covered; missing: Productivity and Business Processes includes LinkedIn.; missing: Productivity and Business Processes includes Dynamics.; missing: I | pdf,sql |  | 30.6s | 0.0173 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 30.1s | 0.0173 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | pdf,sql |  | 14.5s | 0.0115 |
| q_022 | 3 | llm_judge | ❌ | 0.00 | 0/8 facts covered; missing: Alphabet had the largest absolute dollar increase in revenue among the three companies; missing: Alphabet's revenue increased by app | pdf (missing sql) |  | 74.8s | 0.0394 |
| q_025 | 3 | llm_judge | ❌ | 0.00 | 0/12 facts covered; missing: Services revenue grew 12.9% from FY2023 to FY2024 ($85.2B to $96.2B); missing: Services revenue grew 13.5% from FY2024 to FY2025 ($ | pdf,sql |  | 48.2s | 0.0263 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | pdf,sql | 32.9%, 8.6% | 38.2s | 0.0233 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | pdf,sql |  | 35.5s | 0.0220 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 44.0s | 0.0255 |
| x_036 | 3 | llm_judge | ❌ | 0.00 | 0/9 facts covered; missing: Microsoft's operating income rose by $19.1 billion (about 17%); missing: Microsoft's operating income was $109.4 billion in FY2024 a | pdf (missing sql) |  | 78.3s | 0.0372 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 45.4s | 0.0248 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf | $43.9 billion | 30.1s | 0.0152 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | pdf,sql |  | 42.9s | 0.0247 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 19.9s | 0.0122 |
