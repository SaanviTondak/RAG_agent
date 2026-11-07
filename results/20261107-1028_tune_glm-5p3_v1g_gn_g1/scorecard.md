# Scorecard: 20261107-1028_tune_glm-5p3_v1g_gn_g1

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v1g | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-07 11:05

## Headline

**46/47 passed (98%)**, 95% CI 89%–100%; mean score 0.99

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 22 | 100% | 1.00 |
| 3 | 12 | 92% | 0.97 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 100% | 1.00 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 7 | 86% | 0.95 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 5 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 9 | 89% | 0.97 |
| pdf+sql | 15 | 100% | 0.99 |
| sql | 21 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 25 | 96% | 0.99 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.99 |
| extra | 37 | 97% | 0.99 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 47/47 |
| Used a source that wasn't required | 7/47 |
| Saw a gold page (questions with gold pages) | 23/24 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/47 |
| Faithfulness: answers with a claim the tools did not return / contradicting them | 7/47 / 1/47 (674 claims checked) |
| Nudges / fallbacks | 2 / 0 |
| Answer length, words: median / max | 136 / 645 |
| Answer length ÷ gold answer length (llm_judge, median) | 4.3x |
| Opening paragraph alone would pass | 28/47 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.61 (full answer 0.99) |
| Latency p50 / p95 / max | 11.5s / 33.0s / 52.1s |
| Tokens in / out (agent) | 564,742 / 54,753 |
| Cost: agent / judge / per answer | $0.561 / $0.335 / $0.0119 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$416.2 billion' matches 416161000000 (usd) | sql |  | 2.9s | 0.0050 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 14 | 13.2s | 0.0203 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '51.3%' matches 51.3 (pct) | sql |  | 6.1s | 0.0096 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 5.8s | 0.0102 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 7.8s | 0.0080 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 22.0s | 0.0191 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 14.4s | 0.0144 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 31 | 3.5s | 0.0038 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 52.1s | 0.0316 |
| q_025 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql |  | 31.8s | 0.0286 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$101.8 billion' matches 101832000000 (usd) | sql |  | 1.9s | 0.0023 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$10.81' matches 10.81 (plain) | pdf,sql |  | 10.5s | 0.0083 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$31.4 billion' matches 31370000000 (usd) | sql |  | 5.7s | 0.0030 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$619.0 billion' matches 619003000000 (usd) | sql |  | 2.2s | 0.0022 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 6.8s | 0.0056 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 4.1s | 0.0026 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql | 1.8x, 1.9x | 4.8s | 0.0048 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '32.0%' matches 32.01422321660441 (pct) | sql |  | 2.8s | 0.0036 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 11.9s | 0.0075 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 30.2s | 0.0365 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$91.4 billion' matches 91400000000 (usd) | pdf |  | 15.1s | 0.0085 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$45.4 billion' matches 45400000000 (usd) | pdf |  | 15.2s | 0.0119 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$168.9 billion' matches 168900000000 (usd) | pdf |  | 9.1s | 0.0080 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 13.9s | 0.0100 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 12.9s | 0.0099 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 11.0s | 0.0085 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.1s | 0.0075 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$240.3 billion' matches 240301000000 (usd) | pdf,sql |  | 9.3s | 0.0111 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 3.8s | 0.0031 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 17.5s | 0.0134 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not available in its data, offers no fabricated figure, and only notes the three companies it does cover. | sql |  | 4.8s | 0.0029 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data and only offers related historical figures without fabricating a live price. | pdf |  | 8.8s | 0.0063 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 9.1s | 0.0051 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.21 percentage points' | sql |  | 7.4s | 0.0061 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 18.4s | 0.0123 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 44.3s | 0.0348 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 12.2s | 0.0119 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 18.1s | 0.0245 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 11.5s | 0.0093 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '60.0%' matches 59.952293734293136 (pct) | pdf,sql |  | 11.7s | 0.0100 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 4/4 facts covered | pdf,sql |  | 28.4s | 0.0271 |
| x_042 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 18.0s | 0.0145 |
| x_043 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 17.4s | 0.0150 |
| x_045 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 14.2s | 0.0109 |
| x_047 | 3 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 33.0s | 0.0278 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 14.4s | 0.0175 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 7.2s | 0.0062 |
