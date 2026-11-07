# Scorecard: 20261106-1413_tune_glm-5p3_v4_plan_C2

- System: agent + planner | answer model: `glm-5p3` | prompt: v4 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-06 14:51

## Headline

**44/47 passed (94%)**, 95% CI 83%–98%; mean score 0.98

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 92% | 0.97 |
| 2 | 22 | 100% | 1.00 |
| 3 | 12 | 83% | 0.95 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 90% | 0.95 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 7 | 71% | 0.91 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 5 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 9 | 78% | 0.91 |
| pdf+sql | 15 | 93% | 0.98 |
| sql | 21 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 25 | 88% | 0.96 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 80% | 0.95 |
| extra | 37 | 97% | 0.99 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 47/47 |
| Used a source that wasn't required | 5/47 |
| Saw a gold page (questions with gold pages) | 23/24 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 1/47 |
| Nudges / fallbacks | 0 / 0 |
| Answer length, words: median / max | 59 / 537 |
| Answer length ÷ gold answer length (llm_judge, median) | 2.6x |
| Opening paragraph alone would pass | 26/47 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.54 (full answer 0.96) |
| Latency p50 / p95 / max | 8.1s / 27.2s / 38.1s |
| Tokens in / out (agent) | 529,226 / 41,413 |
| Cost: agent / judge / per answer | $0.441 / $0.032 / $0.0094 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 2.9s | 0.0020 |
| q_006 | 1 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Apple disclosed supply chain disruptions from geopolitical tensions as a risk factor.; missing: Apple disclosed supply chain disrupt | pdf |  | 22.7s | 0.0201 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 3.9s | 0.0033 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 6.9s | 0.0059 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 10.0s | 0.0087 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 20.1s | 0.0194 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 12.8s | 0.0144 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql |  | 2.9s | 0.0028 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 14.1s | 0.0114 |
| q_025 | 3 | llm_judge | ❌ | 0.75 | 9/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions; miss | pdf,sql |  | 38.1s | 0.0288 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$101.8 billion' | sql |  | 1.5s | 0.0020 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$10.81' | sql |  | 5.5s | 0.0019 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$31.4 billion' | sql |  | 6.5s | 0.0020 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$619.0 billion' | sql |  | 1.3s | 0.0018 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 5.6s | 0.0054 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 1.8s | 0.0021 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 3.7s | 0.0037 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | found '32.0%' | sql |  | 3.8s | 0.0034 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 9.8s | 0.0078 |
| x_014 | 1 | llm_judge | ✅ | 0.83 | 5/6 facts covered; missing: Microsoft's FY2025 10-K discloses intense and rapidly evolving competition in AI, including from open AI models. | pdf | 20 | 34.3s | 0.0397 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$91.4 billion' | pdf |  | 3.6s | 0.0028 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$45.4 billion' | pdf |  | 5.1s | 0.0049 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$168.9 billion' | pdf |  | 5.0s | 0.0045 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 9.5s | 0.0095 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 8.6s | 0.0070 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 9.3s | 0.0085 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 8.0s | 0.0069 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | sql |  | 3.0s | 0.0033 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 5.5s | 0.0043 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 10.9s | 0.0073 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not available in its data and offers no fabricated figure. | sql |  | 3.5s | 0.0021 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data sources and offers no fabricated figure. | sql |  | 4.3s | 0.0027 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 8.1s | 0.0056 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.2 percentage points' | sql |  | 6.7s | 0.0063 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 17.0s | 0.0161 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 18.7s | 0.0150 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 17.3s | 0.0157 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 9.8s | 0.0116 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 7.6s | 0.0080 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | found '60.0%' | pdf,sql |  | 6.9s | 0.0063 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 17.1s | 0.0148 |
| x_042 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 11.7s | 0.0121 |
| x_043 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 14.4s | 0.0113 |
| x_045 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 13.6s | 0.0145 |
| x_047 | 3 | llm_judge | ❌ | 0.62 | 5/8 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Alphabet expects to significantly increase  | pdf,sql |  | 27.2s | 0.0239 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 13.0s | 0.0180 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.5s | 0.0111 |
