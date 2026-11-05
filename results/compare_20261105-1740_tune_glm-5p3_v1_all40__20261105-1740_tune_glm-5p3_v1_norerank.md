# Compare: 20261105-1740_tune_glm-5p3_v1_all40 (A) vs 20261105-1740_tune_glm-5p3_v1_norerank (B)

- A: `glm-5p3`, prompt v1 | B: `glm-5p3`, prompt v1 | 18 paired questions (run 0) | graded by `deepseek-v4p1-flash` / `deepseek-v4p1-flash`

| Metric | A | B |
|---|---|---|
| Passed | 18/18 | 17/18 |
| Mean score (fact coverage for llm_judge) | 0.991 | 0.940 |
| Fact coverage, llm_judge questions only | 0.988 | 0.994 |
| Opening paragraph alone passes | 9/18 | 6/18 |
| Opening-paragraph fact coverage (llm_judge) | 0.656 | 0.616 |
| Words: median / mean | 171 / 234 | 173 / 247 |
| Opening paragraph words: median | 37 | 39 |
| Latency p50 / p95 | 13.3s / 48.1s | 14.0s / 31.7s |
| Agent cost per answer | $0.0151 | $0.0163 |

## Paired changes (B vs A, per question)

| Metric | B better | B worse | same | sign-test p |
|---|---|---|---|---|
| Pass | 0 | 1 | 17 | 1.000 |
| Score / fact coverage | 1 | 1 | 16 | 1.000 |
| Opening paragraph passes | 0 | 3 | 15 | 0.250 |
| Opening-paragraph coverage | 2 | 4 | 12 | 0.688 |
| Shorter answer (fewer words) | 6 | 12 | 0 | 0.238 |

## Per question

| id | grader | pass A→B | score A→B | opening passes A→B | words A→B | preferred |
|---|---|---|---|---|---|---|
| q_006 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.29→0.43) | 495→529 |  |
| q_012 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.67→0.67) | 155→141 |  |
| q_014 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.37→0.37) | 415→421 |  |
| q_017 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→❌ (1.00→0.57) | 251→275 |  |
| q_025 | llm_judge | ✅→✅ | 0.83→0.92 | ❌→❌ (0.42→0.42) | 322→343 |  |
| x_014 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.00→0.00) | 568→561 |  |
| x_015 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 115→117 |  |
| x_017 | fuzzy_numeric | ✅→❌ | 1.00→0.00 | ✅→❌ (1.00→0.00) | 92→167 |  |
| x_019 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 150→131 |  |
| x_020 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.62→0.75) | 230→215 |  |
| x_021 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.67→0.67) | 171→114 |  |
| x_022 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→❌ (1.00→0.71) | 121→129 |  |
| x_029 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 149→173 |  |
| x_035 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.71→0.71) | 173→271 |  |
| x_036 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.44→0.33) | 355→359 |  |
| x_037 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 186→240 |  |
| x_038 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 143→150 |  |
| x_040 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 118→104 |  |
