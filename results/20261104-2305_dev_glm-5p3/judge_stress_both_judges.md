# Judge stress test: 20261104-2305_dev_glm-5p3

Known edits to saved good answers. Planted errors must fail; harmless edits must pass.

| Judge | Planted errors caught | Harmless edits passed | Cost |
|---|---|---|---|
| kimi-k3 | 16/18 | 3/3 | $0.2596 |
| deepseek-v4p1-flash | 16/18 | 3/3 | $0.0316 |

| id | edit | expected | kimi-k3 | deepseek-v4p1-flash |
|---|---|---|---|---|
| q_012 | wrong number | fail | fail (0.83) | fail (0.83) |
| q_012 | swapped cause | fail | fail (0.67) | fail (0.67) |
| q_012 | dropped facts | fail | fail (0.67) | fail (0.67) |
| q_012 | harmless: cut extra context | pass | pass (1.00) | pass (1.00) |
| q_006 | dropped facts | fail | fail (0.71) | fail (0.57) |
| q_006 | contradiction | fail | pass (1.00) ⚠️ | pass (1.00) ⚠️ |
| q_022 | wrong company | fail | fail (0.88) | fail (0.88) |
| q_022 | wrong number | fail | fail (0.88) | fail (0.88) |
| q_022 | dropped facts | fail | fail (0.75) | fail (0.75) |
| q_022 | harmless: cut repetition | pass | pass (1.00) | pass (1.00) |
| q_025 | wrong number | fail | fail (0.83) | fail (0.75) |
| q_025 | dropped facts | fail | fail (0.67) | fail (0.58) |
| q_025 | reversed comparison | fail | fail (0.83) | fail (0.83) |
| q_017 | wrong number | fail | fail (0.86) | fail (0.86) |
| q_017 | dropped facts | fail | pass (0.86) ⚠️ | pass (0.86) ⚠️ |
| q_017 | wrong growth rate | fail | fail (0.86) | fail (0.86) |
| q_017 | harmless: other units | pass | pass (1.00) | pass (1.00) |
| q_014 | wrong number | fail | fail (0.95) | fail (0.95) |
| q_014 | dropped facts | fail | fail (0.68) | fail (0.68) |
| q_011 | wrong company | fail | fail (0.00) | fail (0.00) |
| q_018 | wrong company | fail | fail (0.00) | fail (0.00) |

## Judge reasons where it got the case wrong

- **q_006 contradiction / kimi-k3**: 7/7 facts covered
- **q_006 contradiction / deepseek-v4p1-flash**: 7/7 facts covered
- **q_017 dropped facts / kimi-k3**: 6/7 facts covered; missing: Google Services includes Google Network
- **q_017 dropped facts / deepseek-v4p1-flash**: 6/7 facts covered; missing: Google Services includes Google Network

## Follow-up: the two misses were planting mistakes

- **q_006 contradiction:** the edited answer still said "custom components available from only one source", so the fact was still stated. Fixed the case to remove that sentence too: both judges now **fail** it (contradicted).
- **q_017 dropped facts:** the opening sentence still named "Google subscriptions, platforms, and devices", so only 1 of 7 facts was removed; 6/7 = 86% is a correct pass under the 80% rule. Fixed the case to remove it from the opening too: both judges now **fail** it (5/7).

**Corrected totals: kimi-k3 18/18 caught, 3/3 harmless passed; deepseek-v4p1-flash 18/18 caught, 3/3 harmless passed.**
Deepseek labelled one removed fact "contradicted" instead of "missing" (same pass/fail). Decision: deepseek-v4p1-flash is the default judge; kimi-k3 grades any run where deepseek wrote the answers.
