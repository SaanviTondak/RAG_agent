# Answer-model comparison (32 tune questions, prompt v1)

| Model | Passed | 95% CI | fuzzy_numeric | exact_match_entity | llm_judge | out_of_scope | Fact coverage (llm_judge) | Judge |
|---|---|---|---|---|---|---|---|---|
| glm-5p3 | **32/32** | 89%–100% | 11/11 | 6/6 | 13/13 | 2/2 | 0.99 | deepseek-v4p1-flash |
| glm-5p3 | **30/32** | 80%–98% | 11/11 | 6/6 | 11/13 | 2/2 | 0.95 | deepseek-v4p1-flash |

| Model | Latency p50 / p95 | Cost per answer | Cost (32 q) | Tool calls / q | Median words | Missing source | Ungrounded numbers | Invalid citations | Fallbacks |
|---|---|---|---|---|---|---|---|---|---|
| glm-5p3 | 8.4s / 40.9s | $0.0097 | $0.31 | 2.6 | 115 | 0 | 5 | 0 | 1 |
| glm-5p3 | 9.8s / 46.9s | $0.0119 | $0.38 | 2.7 | 138 | 0 | 6 | 0 | 2 |

## Failed questions

- **glm-5p3**: none
- **glm-5p3**: q_006, q_025

## Questions failed by more than one model

- none

Runs: `20261105-1447_tune_glm-5p3_v1_fresh`, `20261105-1447_tune_glm-5p3_v2`
