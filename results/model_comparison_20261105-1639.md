# Answer-model comparison (32 tune questions, prompt v1)

| Model | Passed | 95% CI | fuzzy_numeric | exact_match_entity | llm_judge | out_of_scope | Fact coverage (llm_judge) | Judge |
|---|---|---|---|---|---|---|---|---|
| deepseek-v4p1-flash | **32/32** | 89%–100% | 11/11 | 6/6 | 13/13 | 2/2 | 0.99 | kimi-k3 |
| glm-5p3 | **32/32** | 89%–100% | 11/11 | 6/6 | 13/13 | 2/2 | 0.99 | deepseek-v4p1-flash |
| qwen3p8-max | **32/32** | 89%–100% | 11/11 | 6/6 | 13/13 | 2/2 | 0.99 | deepseek-v4p1-flash |
| glm-5p3-flash | **31/32** | 84%–99% | 11/11 | 6/6 | 12/13 | 2/2 | 0.94 | deepseek-v4p1-flash |
| kimi-k3 | **31/32** | 84%–99% | 11/11 | 6/6 | 12/13 | 2/2 | 0.93 | deepseek-v4p1-flash |
| minimax-m3 | **29/32** | 76%–97% | 11/11 | 6/6 | 10/13 | 2/2 | 0.91 | deepseek-v4p1-flash |
| gpt-oss-120b | **24/32** | 58%–87% | 10/11 | 6/6 | 6/13 | 2/2 | 0.80 | deepseek-v4p1-flash |

| Model | Latency p50 / p95 | Cost per answer | Cost (32 q) | Tool calls / q | Median words | Missing source | Ungrounded numbers | Invalid citations | Fallbacks |
|---|---|---|---|---|---|---|---|---|---|
| deepseek-v4p1-flash | 10.4s / 82.6s | $0.0027 | $0.09 | 3.6 | 150 | 0 | 8 | 6 | 3 |
| glm-5p3 | 8.4s / 40.9s | $0.0097 | $0.31 | 2.6 | 115 | 0 | 5 | 0 | 1 |
| qwen3p8-max | 11.2s / 37.8s | $0.0255 | $0.81 | 4.0 | 169 | 0 | 10 | 0 | 4 |
| glm-5p3-flash | 8.0s / 49.8s | $0.0011 | $0.04 | 2.6 | 115 | 1 | 6 | 0 | 0 |
| kimi-k3 | 13.3s / 35.5s | $0.0288 | $0.92 | 2.2 | 116 | 0 | 4 | 0 | 0 |
| minimax-m3 | 3.5s / 50.3s | $0.0018 | $0.06 | 2.3 | 112 | 1 | 9 | 0 | 0 |
| gpt-oss-120b | 4.0s / 14.6s | $0.0012 | $0.04 | 2.4 | 61 | 2 | 12 | 0 | 3 |

## Failed questions

- **deepseek-v4p1-flash**: none
- **glm-5p3**: none
- **qwen3p8-max**: none
- **glm-5p3-flash**: x_029
- **kimi-k3**: x_029
- **minimax-m3**: q_025, x_020, x_029
- **gpt-oss-120b**: q_006, q_012, q_014, q_025, x_014, x_019, x_020, x_029

## Questions failed by more than one model

- x_029 (llm_judge): glm-5p3-flash, kimi-k3, minimax-m3, gpt-oss-120b
- q_025 (llm_judge): minimax-m3, gpt-oss-120b
- x_020 (llm_judge): minimax-m3, gpt-oss-120b

Runs: `20261105-1632_tune_deepseek-v4p1-flash_v1`, `20261105-1447_tune_glm-5p3_v1_fresh`, `20261105-1628_tune_qwen3p8-max_v1`, `20261105-1635_tune_glm-5p3-flash_v1`, `20261105-1628_tune_kimi-k3_v1`, `20261105-1632_tune_minimax-m3_v1`, `20261105-1636_tune_gpt-oss-120b_v1`
