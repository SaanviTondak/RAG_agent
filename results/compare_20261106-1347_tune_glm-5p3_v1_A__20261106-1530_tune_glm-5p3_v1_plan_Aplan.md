# Compare: 20261106-1347_tune_glm-5p3_v1_A (A) vs 20261106-1530_tune_glm-5p3_v1_plan_Aplan (B)

- A: `glm-5p3`, prompt v1 | B: `glm-5p3`, prompt v1 | 47 paired questions (run 0) | graded by `deepseek-v4p1-flash` / `deepseek-v4p1-flash`

| Metric | A | B |
|---|---|---|
| Passed | 47/47 | 45/47 |
| Mean score (fact coverage for llm_judge) | 0.994 | 0.978 |
| Fact coverage, llm_judge questions only | 0.988 | 0.959 |
| Opening paragraph alone passes | 29/47 | 32/47 |
| Opening-paragraph fact coverage (llm_judge) | 0.608 | 0.683 |
| Words: median / mean | 136 / 171 | 140 / 175 |
| Opening paragraph words: median | 28 | 26 |
| Words ÷ gold words (llm_judge, median) | 4.7x | 5.0x |
| Latency p50 / p95 | 9.8s / 40.9s | 9.7s / 29.5s |
| Agent cost per answer | $0.0112 | $0.0118 |

## Paired changes (B vs A, per question)

| Metric | B better | B worse | same | sign-test p |
|---|---|---|---|---|
| Pass | 0 | 2 | 45 | 0.500 |
| Score / fact coverage | 0 | 3 | 44 | 0.250 |
| Opening paragraph passes | 4 | 1 | 42 | 0.375 |
| Opening-paragraph coverage | 9 | 2 | 36 | 0.065 |
| Shorter answer (fewer words) | 18 | 24 | 5 | 0.441 |

**Blind preference** (`deepseek-v4p1-flash`, asked in both orders; inconsistent = tie): B preferred 19, A preferred 16, tie 11, judge error 1; sign-test p = 0.736; cost $0.2514

## Per question

| id | grader | pass A→B | score A→B | opening passes A→B | words A→B | preferred |
|---|---|---|---|---|---|---|
| q_001 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 26→44 | A |
| q_006 | llm_judge | ✅→❌ | 1.00→0.57 | ❌→❌ (0.29→0.29) | 495→438 | A |
| q_008 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 94→38 | B |
| q_011 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 103→102 | B |
| q_012 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.67→0.67) | 155→161 | tie |
| q_014 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.37→0.37) | 415→387 | tie |
| q_017 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 251→235 | B |
| q_018 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 85→85 | B |
| q_022 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.50→0.50) | 199→172 | B |
| q_025 | llm_judge | ✅→✅ | 0.83→0.83 | ❌→❌ (0.42→0.42) | 322→339 | B |
| x_001 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 51→42 | B |
| x_002 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 106→106 | A |
| x_003 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 43→77 | tie |
| x_004 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 64→61 | tie |
| x_007 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 109→99 | B |
| x_008 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 66→65 | tie |
| x_009 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 136→102 | B |
| x_011 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 35→35 | B |
| x_013 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→❌ (1.00→0.43) | 169→175 | A |
| x_014 | llm_judge | ✅→✅ | 1.00→0.83 | ❌→❌ (0.00→0.00) | 568→570 | A |
| x_015 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 115→161 | A |
| x_017 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 92→92 | tie |
| x_019 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 150→137 | A |
| x_020 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.62→0.75) | 230→231 | B |
| x_021 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→✅ (0.67→1.00) | 171→157 | B |
| x_022 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 121→140 | tie |
| x_025 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.17→0.67) | 151→191 | A |
| x_027 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 53→120 | A |
| x_028 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 70→74 | A |
| x_029 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 149→163 | A |
| x_030 | out_of_scope | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 78→57 | B |
| x_032 | out_of_scope | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 108→90 | A |
| x_033 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 86→83 | tie |
| x_034 | exact_match_entity | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 133→133 | tie |
| x_035 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→✅ (0.71→0.86) | 173→305 | A |
| x_036 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.44→0.33) | 355→401 | A |
| x_037 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 186→202 | B |
| x_038 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 143→155 | error |
| x_039 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.75→0.75) | 77→99 | A |
| x_040 | fuzzy_numeric | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 118→122 | tie |
| x_041 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.60→0.60) | 258→262 | tie |
| x_042 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.29→0.43) | 374→281 | B |
| x_043 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→✅ (0.40→0.80) | 146→178 | B |
| x_045 | llm_judge | ✅→✅ | 1.00→1.00 | ✅→✅ (1.00→1.00) | 203→236 | B |
| x_047 | llm_judge | ✅→❌ | 0.88→0.75 | ❌→❌ (0.25→0.50) | 517→526 | B |
| x_048 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→❌ (0.57→0.71) | 173→178 | A |
| x_049 | llm_judge | ✅→✅ | 1.00→1.00 | ❌→✅ (0.50→1.00) | 103→98 | B |
