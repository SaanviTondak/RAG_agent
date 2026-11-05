# Retrieval eval (extra, 8 questions with gold pages, k=6)

| Config | Hit@k (any gold page) | Recall@k (share of gold pages) | MRR |
|---|---|---|---|
| bm25 | 5/8 | 0.62 | 0.48 |
| dense | 6/8 | 0.72 | 0.49 |
| hybrid | 7/8 | 0.80 | 0.45 |
| hybrid + rerank | 8/8 | 0.97 | 0.73 |

Per question: gold pages found (rank of the first hit).

| id | filter | bm25 | dense | hybrid | hybrid + rerank |
|---|---|---|---|---|---|
| x_014 | MSFT FY2025 | 0/5 | 4/5 (#2) | 2/5 (#2) | 4/5 (#2) |
| x_015 | GOOGL FY2025 | 1/1 (#1) | 0/1 | 1/1 (#5) | 1/1 (#2) |
| x_017 | GOOGL FY2025 | 1/1 (#2) | 0/1 | 1/1 (#4) | 1/1 (#2) |
| x_019 | MSFT FY2025 | 1/1 (#3) | 1/1 (#1) | 1/1 (#2) | 1/1 (#1) |
| x_020 | MSFT FY2025 | 0/1 | 1/1 (#4) | 0/1 | 1/1 (#3) |
| x_021 | GOOGL FY2025 | 0/1 | 1/1 (#1) | 1/1 (#6) | 1/1 (#1) |
| x_022 | AAPL FY2025 | 1/1 (#1) | 1/1 (#1) | 1/1 (#1) | 1/1 (#1) |
| x_029 | MSFT FY2024 | 1/1 (#1) | 1/1 (#5) | 1/1 (#1) | 1/1 (#1) |
