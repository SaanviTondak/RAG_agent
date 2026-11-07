# Faithfulness stress test: 20261104-2305_dev_glm-5p3, judge `deepseek-v4p1-flash`

**9/9 cases right**; $0.1607


| id | edit | expected | flags (unedited -> edited) | result |
|---|---|---|---|---|
| q_012 | invented cause | flag | 0 -> 1 | ok |
| q_012 | wrong figure | flag | 0 -> 1 | ok |
| q_022 | invented metric | flag | 0 -> 1 | ok |
| q_017 | invented driver | flag | 0 -> 1 | ok |
| q_001 | invented trend | flag | 1 -> 2 | ok |
| q_018 | wrong input figure | flag | 1 -> 3 | ok |
| q_012 | harmless: rewording | same | 0 -> 0 | ok |
| q_022 | harmless: cut a sentence | same | 0 -> 0 | ok |
| q_017 | harmless: other units | same | 0 -> 0 | ok |

## Flags on the unedited answers (review by hand: real unsupported claims, or judge errors?)

- **q_001** (4 claims): unsupported: The figure is net sales as reported on the consolidated income statement.
- **q_006** (35 claims): unsupported: The FY2025 10-K discloses four primary supply-chain risk factors: dependence on outsourced manufacturing, single/limited-source component supply, trade restrictions and business interruptions, and inventory/purchase-commitment exposure.
- **q_008** (6 claims): none
- **q_011** (13 claims): none
- **q_012** (10 claims): none
- **q_014** (23 claims): none
- **q_017** (19 claims): none
- **q_018** (19 claims): unsupported: Apple's below-1.0 ratio is consistent with Apple's lean working-capital management
- **q_022** (17 claims): none
- **q_025** (20 claims): unsupported: Apple frames Services as both a growth and margin engine
