# Scorecard: 20261107-1105_tune_glm-5p3_v1g_gn_g2

- System: agent + grounding nudge | answer model: `glm-5p3` | prompt: v1g | judge: `deepseek-v4p1-flash` | rerank: True | set: tune | runs per question: 2 | graded 2026-11-07 11:11

x_036#0 was regraded once: its first grading failed (the judge returned invalid JSON twice).

## Headline

**13/14 passed (93%)**, 95% CI 69%–99%; mean score 0.94

**By question: 6/7 passed in every run**, 95% CI 49%–97% (the CI above treats repeated runs of a question as independent, so it is too narrow).

| Tier | n | pass | mean score |
|---|---|---|---|
| 1 | 4 | 100% | 0.96 |
| 2 | 2 | 100% | 1.00 |
| 3 | 8 | 88% | 0.90 |

| Complexity level | n | pass | mean score |
|---|---|---|---|
| 1 lookup | 4 | 100% | 0.96 |
| 3 figure + explanation | 2 | 100% | 1.00 |
| 4 multi-part synthesis | 8 | 88% | 0.90 |

| Sources needed | n | pass | mean score |
|---|---|---|---|
| pdf | 6 | 83% | 0.90 |
| pdf+sql | 6 | 100% | 0.94 |
| sql | 2 | 100% | 1.00 |

| Grader | n | pass | mean score |
|---|---|---|---|
| llm_judge | 14 | 93% | 0.94 |

| Question set | n | pass | mean score |
|---|---|---|---|
| dev | 8 | 100% | 0.94 |
| extra | 6 | 83% | 0.93 |

## Diagnostics

| Metric | Value |
|---|---|
| Routing correct (no required source missing) | 14/14 |
| Used a source that wasn't required | 2/14 |
| Saw a gold page (questions with gold pages) | 12/12 |
| Invalid citations (total) | 0 |
| Answers with numbers not found in any tool output | 5/14 |
| Faithfulness: answers with a claim the tools did not return / contradicting them | 4/14 / 1/14 (387 claims checked) |
| Nudges / fallbacks | 0 / 2 |
| Answer length, words: median / max | 397 / 718 |
| Answer length ÷ gold answer length (llm_judge, median) | 7.6x |
| Opening paragraph alone would pass | 0/14 |
| Opening-paragraph fact coverage (llm_judge, mean) | 0.34 (full answer 0.94) |
| Latency p50 / p95 / max | 32.6s / 48.5s / 57.8s |
| Tokens in / out (agent) | 326,390 / 48,984 |
| Cost: agent / judge / per answer | $0.391 / $0.261 / $0.0279 |

## Per question

| id | tier | grader | pass | score | reason | sources used | ungrounded numbers | time | $ |
|---|---|---|---|---|---|---|---|---|---|
| q_006#0 | 1 | llm_judge | ✅ | 1.00 | 7/7 facts covered | pdf |  | 28.3s | 0.0208 |
| q_006#1 | 1 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Apple disclosed component supply constraints affecting product availability as a risk factor. | pdf |  | 11.6s | 0.0091 |
| q_014#0 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 30.2s | 0.0292 |
| q_014#1 | 2 | llm_judge | ✅ | 1.00 | 19/19 facts covered | pdf,sql |  | 30.5s | 0.0257 |
| q_022#0 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | $2.44 | 16.3s | 0.0126 |
| q_022#1 | 3 | llm_judge | ✅ | 1.00 | 8/8 facts covered | sql | $18.8B, $14.0B, $3.8B, $13.0B | 17.1s | 0.0125 |
| q_025#0 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K highlights Services as a key growth driver; missing: The 10-K says Services has recurring revenue from subscriptions | pdf,sql |  | 40.9s | 0.0440 |
| q_025#1 | 3 | llm_judge | ✅ | 0.83 | 10/12 facts covered; missing: The 10-K says Services has recurring revenue from subscriptions; missing: The 10-K mentions iCloud as part of Services | pdf,sql | 43x | 34.8s | 0.0247 |
| x_014#0 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 20 | 39.3s | 0.0341 |
| x_014#1 | 1 | llm_judge | ✅ | 1.00 | 6/6 facts covered | pdf | 22, 20 | 32.6s | 0.0299 |
| x_036#0 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 33.5s | 0.0283 |
| x_036#1 | 3 | llm_judge | ✅ | 1.00 | 9/9 facts covered | pdf,sql |  | 38.0s | 0.0314 |
| x_047#0 | 3 | llm_judge | ✅ | 0.86 | 6/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering | pdf,sql |  | 48.5s | 0.0381 |
| x_047#1 | 3 | llm_judge | ❌ | 0.71 | 5/7 facts covered; missing: Microsoft's operating expenses rose on investments in cloud and AI engineering; missing: Google Cloud's operating income gains were  | pdf,sql |  | 57.8s | 0.0503 |

**Consistency:** 6/7 questions passed in every run; 6/7 gave the same result in every run. Inconsistent: x_047 (1/2)
