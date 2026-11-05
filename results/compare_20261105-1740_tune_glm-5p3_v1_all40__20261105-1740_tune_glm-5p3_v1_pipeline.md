# Compare: 20261105-1740_tune_glm-5p3_v1_all40 (A) vs 20261105-1740_tune_glm-5p3_v1_pipeline (B)

- A: `glm-5p3`, prompt v1 | B: `glm-5p3`, prompt v1 | 18 paired questions (run 0) | graded by `deepseek-v4p1-flash` / `deepseek-v4p1-flash`

| Metric | A | B |
|---|---|---|
| Passed | 18/18 | 13/18 |
| Mean score (fact coverage for llm_judge) | 0.991 | 0.777 |
| Fact coverage, llm_judge questions only | 0.985 | 0.636 |
| Opening paragraph alone passes | 10/18 | 11/18 |
| Opening-paragraph fact coverage (llm_judge) | 0.650 | 0.556 |
| Words: median / mean | 143 / 190 | 151 / 170 |
| Opening paragraph words: median | 35 | 21 |
| Latency p50 / p95 | 9.8s / 36.9s | 30.6s / 74.8s |
| Agent cost per answer | $0.0140 | $0.0202 |

## Paired changes (B vs A, per question)

| Metric | B better | B worse | same | sign-test p |
|---|---|---|---|---|
| Pass | 0 | 5 | 13 | 0.062 |
| Score / fact coverage | 0 | 5 | 13 | 0.062 |
| Opening paragraph passes | 1 | 0 | 17 | 1.000 |
| Opening-paragraph coverage | 1 | 3 | 14 | 0.625 |
| Shorter answer (fewer words) | 7 | 11 | 0 | 0.481 |

## Per question

| id | grader | pass A→B | score A→B | opening passes A→B | words A→B | preferred |
|---|---|---|---|---|---|---|
| q_001 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 26→111 |  |
| q_006 | llm_judge | ✅→❌ | 1.00→0.57 | ❌→❌ (0.29→0.29) | 495→461 |  |
| q_008 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 94→102 |  |
| q_011 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 103→111 |  |
| q_012 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→✅ (0.67→1.00) | 155→260 |  |
| q_014 | llm_judge | ✅→❌ | 1.00→0.42 | ❌→❌ (0.37→0.37) | 415→339 |  |
| q_017 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 251→239 |  |
| q_018 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 85→151 |  |
| q_022 | llm_judge | ✅→❌ | 1.00→0.00 | ❌→❌ (0.50→0.00) | 199→5 |  |
| q_025 | llm_judge | ✅→❌ | 0.83→0.00 | ❌→❌ (0.42→0.00) | 322→5 |  |
| x_033 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 86→159 |  |
| x_034 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 133→184 |  |
| x_035 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.71→0.71) | 173→281 |  |
| x_036 | llm_judge | ✅→❌ | 1.00→0.00 | ❌→❌ (0.44→0.00) | 355→5 |  |
| x_037 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 186→184 |  |
| x_038 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 143→189 |  |
| x_039 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.75→0.75) | 77→141 |  |
| x_040 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 118→140 |  |
