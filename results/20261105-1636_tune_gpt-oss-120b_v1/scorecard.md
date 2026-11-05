# Scorecard: 20261105-1636_tune_gpt-oss-120b_v1

- Answer model: `gpt-oss-120b` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-05 16:39

## Headline

**24/32 passed (75%)**, 95% CI 58%–87%; mean score 0.89

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 77% | 0.88 |
| 2 | 15 | 80% | 0.95 |
| 3 | 4 | 50% | 0.70 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 6 | 50% | 0.73 |
| pdf+sql | 7 | 29% | 0.73 |
| sql | 17 | 100% | 0.99 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 6 | 100% | 1.00 |
| fuzzy_numeric | 11 | 91% | 0.91 |
| llm_judge | 13 | 46% | 0.80 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 60% | 0.86 |
| extra | 22 | 82% | 0.90 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 30/32 |
| Used a source that wasn't required | 5/32 |
| Saw a gold page (questions with gold pages) | 10/13 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 12/32 |
| Nudges / fallbacks | 0 / 3 |
| Answer length, words: median / max | 61 / 266 |
| Opening paragraph alone would pass | 17/32 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.37 (full answer 0.80) |
| Latency p50 / p95 / max | 4.0s / 14.6s / 21.9s |
| Tokens in / out (agent) | 335,648 / 23,264 |
| Cost: agent / judge / per answer | $0.038 / $0.052 / $0.0012 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2\u202fbillion' | sql |  | 1.6s | 0.0005 |
| q_006 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from natural disasters as a risk factor.; missing: Apple disclosed supply chain disruptions | pdf | 10 | 12.7s | 0.0011 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | 144.5, 281.7 | 2.9s | 0.0007 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1\u202f%' | sql |  | 3.9s | 0.0009 |
| q_012 | 2 | llm_judge | ❌ | 0.67 | 4/6 facts covered; contradicted: Apple's Greater China revenue was $66.95 billion in FY2024; contradicted: The decline was approximately 3.8% | pdf,sql | $66.9 billion | 10.5s | 0.0011 |
| q_014 | 2 | llm_judge | ❌ | 0.79 | 15/19 facts covered; missing: Productivity and Business Processes includes LinkedIn.; missing: Productivity and Business Processes includes Dynamics.; missing:  | pdf,sql | 10, 10, 10, 10 | 14.6s | 0.0016 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 7.5s | 0.0014 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 2.8s | 0.0007 |
| q_022 | 3 | llm_judge | ✅ | 0.88 | 7/8 facts covered; missing: Alphabet's revenue increased by approximately $52.8B, from $350.0B to $402.8B | sql | $15.5 B, $37.8 B, $8.4 B, $13.0 B | 9.1s | 0.0022 |
| q_025 | 3 | llm_judge | ❌ | 0.58 | 7/12 facts covered; missing: Services revenue grew 12.9% from FY2023 to FY2024 ($85.2B to $96.2B); missing: The 10-K says Services has higher margins; missing:  | pdf,sql | 10, 10, 10, 10 | 21.9s | 0.0041 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8\u202fbillion' | sql |  | 1.4s | 0.0005 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 1.4s | 0.0002 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4\u202fbillion' | sql | 10 | 2.1s | 0.0005 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0\u202fbillion' | sql |  | 2.2s | 0.0005 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6\u202f%' | sql |  | 4.2s | 0.0007 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 1.8s | 0.0005 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 3.2s | 0.0008 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0\u202f%' | sql | 132.2, 100.1, 100.1, 100 | 2.2s | 0.0006 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 4.1s | 0.0013 |
| x_014 | 1 | llm_judge | ❌ | 0.67 | 4/6 facts covered; missing: Microsoft's FY2025 10-K discloses intense and rapidly evolving competition in AI, including from open AI models.; missing: Microsoft | pdf | 10 | 9.3s | 0.0025 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4\u202fbillion' | pdf |  | 2.8s | 0.0007 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4\u202fbillion' | pdf |  | 4.3s | 0.0008 |
| x_019 | 1 | fuzzy_numeric | ❌ | 0.00 | no number matches 168900000000 (saw: $106.3 billion, $106,265,000,000, $106.3 billion) | sql (missing pdf) |  | 1.6s | 0.0005 |
| x_020 | 2 | llm_judge | ❌ | 0.75 | 6/8 facts covered; contradicted: Server products and cloud services revenue increased 23%.; missing: Azure and other cloud services revenue growth was 34%. | pdf,sql | 10, 10, 10 | 7.0s | 0.0013 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql | 10 | 5.0s | 0.0011 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 14.2s | 0.0025 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 5.9s | 0.0011 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3\u202fbillion' | pdf,sql |  | 20.4s | 0.0065 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7\u202fbillion' | sql |  | 4.0s | 0.0005 |
| x_029 | 3 | llm_judge | ❌ | 0.33 | 1/3 facts covered; missing: The FY2024 10-K originally reported $105.4 billion for Intelligent Cloud.; missing: The $105.4 billion figure was reported under the | sql (missing pdf) |  | 1.4s | 0.0002 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue data is not available in its sources and provides no fabricated figure. | sql |  | 1.4s | 0.0004 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer correctly states that Microsoft's current stock price is not available in the provided data and does not invent a figure. | sql | 10 | 1.6s | 0.0005 |
