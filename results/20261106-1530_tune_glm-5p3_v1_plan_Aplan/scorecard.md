# Scorecard: 20261106-1530_tune_glm-5p3_v1_plan_Aplan

- System: agent + planner | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-06 16:56

## Headline

**45/47 passed (96%)**, 95% CI 86%–99%; mean score 0.98

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 92% | 0.95 |
| 2 | 22 | 100% | 1.00 |
| 3 | 12 | 92% | 0.97 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 90% | 0.94 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 7 | 86% | 0.94 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 5 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 9 | 78% | 0.91 |
| pdf+sql | 15 | 100% | 0.99 |
| sql | 21 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 25 | 92% | 0.96 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 90% | 0.94 |
| extra | 37 | 97% | 0.99 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 47/47 |
| Used a source that wasn't required | 8/47 |
| Saw a gold page (questions with gold pages) | 23/24 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/47 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 140 / 570 |
| Answer length ÷ gold answer length (llm_judge, median) | 5.0x |
| Opening paragraph alone would pass | 32/47 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.68 (full answer 0.96) |
| Latency p50 / p95 / max | 9.7s / 29.5s / 37.5s |
| Tokens in / out (agent) | 571,333 / 52,582 |
| Cost: agent / judge / per answer | $0.557 / $0.034 / $0.0118 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 3.3s | 0.0025 |
| q_006 | 1 | llm_judge | ❌ | 0.57 | 4/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 15.1s | 0.0142 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | 48.7% | 5.9s | 0.0050 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 7.4s | 0.0064 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 13.4s | 0.0145 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 26.0s | 0.0311 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 14.8s | 0.0155 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 3.3s | 0.0031 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 14.7s | 0.0121 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 29.5s | 0.0311 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 2.2s | 0.0024 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | pdf,sql |  | 7.5s | 0.0075 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | pdf,sql |  | 6.8s | 0.0066 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 2.2s | 0.0023 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 5.0s | 0.0051 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 2.3s | 0.0024 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 4.2s | 0.0043 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 4.3s | 0.0034 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 9.7s | 0.0103 |
| x_014 | 1 | llm_judge | ✅ | 0.83 | 5/6 facts covered; missing: Microsoft's FY2025 10-K discloses intense and rapidly evolving competition in AI, including from open AI models. | pdf | 22, 20 | 31.0s | 0.0347 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 8.6s | 0.0077 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 6.2s | 0.0054 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 5.8s | 0.0052 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 16.5s | 0.0138 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 12.5s | 0.0107 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 15.8s | 0.0190 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 14.8s | 0.0118 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 8.3s | 0.0073 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 6.0s | 0.0044 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 21.9s | 0.0166 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon is not covered by its data and provides no fabricated revenue figure. | sql |  | 4.8s | 0.0033 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Microsoft's current stock price is not available in its data sources and offers only related, verifiable per-share data without fabric | sql |  | 9.0s | 0.0073 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 9.3s | 0.0086 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 7.9s | 0.0066 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 17.2s | 0.0222 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 18.4s | 0.0148 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 14.3s | 0.0144 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 15.2s | 0.0182 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql | 85.1% | 8.3s | 0.0070 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 8.6s | 0.0099 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 18.2s | 0.0200 |
| x_042 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 18.7s | 0.0151 |
| x_043 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 17.9s | 0.0182 |
| x_045 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 19.1s | 0.0182 |
| x_047 | 3 | llm_judge | ❌ | 0.75 | 6/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 37.5s | 0.0283 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 25.7s | 0.0185 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 14.2s | 0.0101 |
