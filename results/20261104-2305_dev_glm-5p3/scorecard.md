# Scorecard: 20261104-2305_dev_glm-5p3

- Answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: dev | runs per question: 1 | graded 2026-11-05 15:06

## Headline

**10/10 passed (100%)**, 95% CI 72%–100%; mean score 0.98

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 3 | 100% | 1.00 |
| 2 | 5 | 100% | 1.00 |
| 3 | 2 | 100% | 0.92 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 2 | 100% | 1.00 |
| pdf+sql | 3 | 100% | 0.94 |
| sql | 5 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| exact_match_entity | 2 | 100% | 1.00 |
| fuzzy_numeric | 2 | 100% | 1.00 |
| llm_judge | 6 | 100% | 0.97 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 10 | 100% | 0.98 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 10/10 |
| Used a source that wasn't required | 1/10 |
| Saw a gold page (questions with gold pages) | 5/5 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 4/10 |
| Nudges / fallbacks | 0 / 1 |
| Answer length, words: median / max | 157 / 496 |
| Opening paragraph alone would pass | 4/10 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.49 (full answer 0.97) |
| Latency p50 / p95 / max | 10.5s / 56.4s / 56.4s |
| Tokens in / out (agent) | 118,699 / 12,632 |
| Cost: agent / judge / per answer | $0.162 / $0.007 / $0.0162 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_001 | 1 | fuzzy_numeric | ✅ | 1.00 | found '$416.2 billion' | sql |  | 4.3s | 0.0047 |
| q_006 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf | 14 | 19.7s | 0.0232 |
| q_008 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | 48.7%, $137.2 billion | 8.9s | 0.0080 |
| q_011 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '15.1%' | sql |  | 8.1s | 0.0097 |
| q_012 | 2 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf,sql |  | 10.5s | 0.0086 |
| q_014 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 28.3s | 0.0309 |
| q_017 | 2 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf,sql |  | 39.4s | 0.0191 |
| q_018 | 2 | exact_match_entity | ✅ | 1.00 | answer names ['GOOGL'] (gold ['GOOGL']); number: found '2.01' | sql | 1.0 | 4.0s | 0.0031 |
| q_022 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | $18.8B, $14.0B, $13.0B, $8.4B | 14.8s | 0.0139 |
| q_025 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql |  | 56.4s | 0.0405 |
