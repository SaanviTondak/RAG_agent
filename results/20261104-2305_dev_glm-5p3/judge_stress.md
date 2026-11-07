# Judge stress test: 20261104-2305_dev_glm-5p3

Known edits to saved good answers. Planted errors must fail; harmless edits must pass.

| Judge | Planted errors caught | Harmless edits passed | Cost |
|---|---|---|---|
| deepseek-v4p1-flash | 22/22 | 6/6 | $0.0635 |

| id | edit | expected | deepseek-v4p1-flash |
|---|---|---|---|
| q_012 | wrong number | fail | fail (0.83) |
| q_012 | swapped cause | fail | fail (0.67) |
| q_012 | dropped facts | fail | fail (0.67) |
| q_012 | harmless: cut extra context | pass | pass (1.00) |
| q_006 | dropped facts | fail | fail (0.57) |
| q_006 | contradiction | fail | fail (0.86) |
| q_022 | wrong company | fail | fail (0.75) |
| q_022 | wrong number | fail | fail (0.88) |
| q_022 | dropped facts | fail | fail (0.75) |
| q_022 | harmless: cut repetition | pass | pass (1.00) |
| q_025 | wrong number | fail | fail (0.75) |
| q_025 | dropped facts | fail | fail (0.58) |
| q_025 | reversed comparison | fail | fail (0.75) |
| q_017 | wrong number | fail | fail (0.86) |
| q_017 | dropped facts | fail | fail (0.71) |
| q_017 | wrong growth rate | fail | fail (0.86) |
| q_017 | harmless: other units | pass | pass (1.00) |
| q_014 | wrong number | fail | fail (0.95) |
| q_014 | dropped facts | fail | fail (0.68) |
| q_011 | wrong company | fail | fail (0.00) |
| q_018 | wrong company | fail | fail (0.00) |
| q_018 | harmless: runners-up in opening | pass | pass (1.00) |
| q_011 | harmless: runners-up in opening | pass | pass (1.00) |
| q_001 | wrong headline, right number as comparison | fail | fail (0.00) |
| q_001 | harmless: comparison added | pass | pass (1.00) |
| q_008 | wrong headline, gold as the remainder | fail | fail (0.00) |
| q_008 | wrong unit | fail | fail (0.00) |
| q_011 | runners-up, wrong winner | fail | fail (0.00) |

## Judge reasons where it got the case wrong

