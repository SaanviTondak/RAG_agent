# Scorecard: 20261105-1749_tune_glm-5p3_v1_gn_nudgetest

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v1 | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 3 | graded 2026-11-05 17:49

## Headline

**6/6 passed (100%)**, 95% CI 61%–100%; mean score 1.00

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 3 | 100% | 1.00 |
| 2 | 3 | 100% | 1.00 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| sql | 6 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| fuzzy_numeric | 6 | 100% | 1.00 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 3 | 100% | 1.00 |
| extra | 3 | 100% | 1.00 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 6/6 |
| Used a source that wasn't required | 4/6 |
| Saw a gold page (questions with gold pages) | 0/0 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 1/6 |
| Nudges / fallbacks | 3 / 0 |
| Answer length, words: median / max | 102 / 125 |
| Opening paragraph alone would pass | 6/6 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.00 (full answer 0.00) |
| Latency p50 / p95 / max | 8.2s / 13.4s / 13.4s |
| Tokens in / out (agent) | 68,427 / 4,591 |
| Cost: agent / judge / per answer | $0.049 / $0.000 / $0.0082 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_008#0 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql |  | 7.5s | 0.0076 |
| q_008#1 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | sql | $137.2 billion | 5.8s | 0.0060 |
| q_008#2 | 1 | fuzzy_numeric | ✅ | 1.00 | found '51.3%' | pdf,sql |  | 13.4s | 0.0120 |
| x_027#0 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 8.9s | 0.0090 |
| x_027#1 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 8.4s | 0.0072 |
| x_027#2 | 2 | fuzzy_numeric | ✅ | 1.00 | found '$240.3 billion' | pdf,sql |  | 8.2s | 0.0073 |

**Consistency:** 2/2 questions gave the same result in every run.
