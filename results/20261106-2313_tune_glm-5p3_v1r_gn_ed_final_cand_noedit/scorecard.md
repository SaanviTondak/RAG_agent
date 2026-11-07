# Scorecard: 20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand_noedit

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v1r | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 1 | graded 2026-11-06 23:48

Derived from `20261106-2313_tune_glm-5p3_v1r_gn_ed_final_cand` with the editor removed (drafts as answers; cost and latency include the editor call).

Grader fixes of 2026-11-07 applied (eval/apply_grader_fixes.py).

## Headline

**47/47 passed (100%)**, 95% CI 92%–100%; mean score 1.00

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 13 | 100% | 1.00 |
| 2 | 22 | 100% | 1.00 |
| 3 | 12 | 100% | 0.98 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 0 out of scope | 2 | 100% | 1.00 |
| 1 lookup | 10 | 100% | 1.00 |
| 2 calculation / comparison | 10 | 100% | 1.00 |
| 3 figure + explanation | 9 | 100% | 1.00 |
| 4 multi-part synthesis | 7 | 100% | 0.97 |
| 5 dependent multi-hop | 3 | 100% | 1.00 |
| 6 cross-check / data conflict | 5 | 100% | 1.00 |
| 7 follow-up | 1 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| none | 2 | 100% | 1.00 |
| pdf | 9 | 100% | 0.98 |
| pdf+sql | 15 | 100% | 0.99 |
| sql | 21 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 8 | 100% | 1.00 |
| fuzzy_numeric | 12 | 100% | 1.00 |
| llm_judge | 25 | 100% | 0.99 |
| out_of_scope | 2 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.99 |
| extra | 37 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 47/47 |
| Used a source that wasn't required | 7/47 |
| Saw a gold page (questions with gold pages) | 23/24 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/47 |
| Faithfulness: answers with a claim the tools did not return / contradicting them | 16/47 / 1/47 (697 claims checked) |
| Nudges / fallbacks | 1 / 0 |
| Answer length, words: median / max | 132 / 577 |
| Answer length ÷ gold answer length (llm_judge, median) | 4.6x |
| Opening paragraph alone would pass | 33/47 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.70 (full answer 0.99) |
| Latency p50 / p95 / max | 13.7s / 34.6s / 39.2s |
| Tokens in / out (agent) | 521,423 / 65,729 |
| Cost: agent / judge / per answer | $0.635 / $0.094 / $0.0135 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$416.2 billion' matches 416161000000 (usd) | sql |  | 3.2s | 0.0049 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 14 | 22.1s | 0.0247 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '51.3%' matches 51.3 (pct) | sql |  | 10.1s | 0.0107 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 5.8s | 0.0072 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 11.6s | 0.0148 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 27.6s | 0.0295 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 18.4s | 0.0150 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 4.1s | 0.0035 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql |  | 20.1s | 0.0145 |
| q_025 | 3 | llm_judge | ✅ | 0.92 | 11/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql |  | 34.6s | 0.0286 |
| x_001 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$101.8 billion' matches 101832000000 (usd) | sql |  | 2.4s | 0.0024 |
| x_002 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$10.81' matches 10.81 (plain) | pdf,sql |  | 7.6s | 0.0107 |
| x_003 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$31.4 billion' matches 31370000000 (usd) | sql |  | 3.7s | 0.0027 |
| x_004 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$619.0 billion' matches 619003000000 (usd) | sql |  | 2.0s | 0.0025 |
| x_007 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '45.6%' | sql |  | 5.6s | 0.0046 |
| x_008 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['AAPL', 'GOOGL'] (gold ['AAPL', 'GOOGL']) | sql |  | 3.3s | 0.0028 |
| x_009 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL', 'MSFT', 'AAPL'] (gold ['GOOGL', 'MSFT', 'AAPL']) | sql |  | 4.8s | 0.0048 |
| x_011 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '32.0%' matches 32.01422321660441 (pct) | sql |  | 5.8s | 0.0035 |
| x_013 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | sql |  | 15.5s | 0.0129 |
| x_014 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 38.1s | 0.0418 |
| x_015 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$91.4 billion' matches 91400000000 (usd) | pdf |  | 8.5s | 0.0096 |
| x_017 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$45.4 billion' matches 45400000000 (usd) | pdf |  | 7.5s | 0.0054 |
| x_019 | 1 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$168.9 billion' matches 168900000000 (usd) | pdf |  | 10.1s | 0.0073 |
| x_020 | 2 | llm_judge | ✅ | 1.00 | 8/8 facts covered | pdf,sql |  | 17.2s | 0.0175 |
| x_021 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 14.4s | 0.0158 |
| x_022 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 13.7s | 0.0104 |
| x_025 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 16.1s | 0.0108 |
| x_027 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '$240.3 billion' matches 240301000000 (usd) | pdf,sql |  | 15.1s | 0.0162 |
| x_028 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '$281.7 billion' | sql |  | 6.2s | 0.0060 |
| x_029 | 3 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf,sql |  | 25.5s | 0.0157 |
| x_030 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states Amazon's FY2025 revenue is not in its data, explains its coverage is limited to Apple, Microsoft, and Alphabet, and offers no fabricat | sql | 10 | 4.3s | 0.0028 |
| x_032 | 1 | out_of_scope | ✅ | 1.00 | The answer clearly states the current stock price is not available in its data and provides only related, sourced figures without fabricating a live quote. | pdf |  | 16.7s | 0.0128 |
| x_033 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['MSFT'] (gold ['MSFT']); number: found '15.3%' | sql |  | 6.2s | 0.0049 |
| x_034 | 3 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '4.21 percentage points' | sql |  | 6.6s | 0.0049 |
| x_035 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 22.7s | 0.0171 |
| x_036 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 24.6s | 0.0221 |
| x_037 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 23.2s | 0.0201 |
| x_038 | 2 | llm_judge | ✅ | 1.00 | 3/3 facts covered | pdf |  | 33.1s | 0.0278 |
| x_039 | 2 | llm_judge | ✅ | 1.00 | 4/4 facts covered | sql |  | 12.3s | 0.0083 |
| x_040 | 2 | fuzzy_numeric | ✅ | 1.00 | answer's figure '60.0%' matches 59.952293734293136 (pct) | pdf,sql |  | 13.6s | 0.0100 |
| x_041 | 3 | llm_judge | ✅ | 1.00 | 4/4 facts covered | pdf,sql |  | 24.9s | 0.0255 |
| x_042 | 3 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 24.9s | 0.0186 |
| x_043 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 18.6s | 0.0195 |
| x_045 | 2 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 24.6s | 0.0219 |
| x_047 | 3 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf |  | 39.2s | 0.0271 |
| x_048 | 3 | llm_judge | ✅ | 1.00 | 5/5 facts covered | pdf,sql |  | 17.2s | 0.0198 |
| x_049 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 13.7s | 0.0145 |
