# Agentic RAG over 10-Ks: technical report

## 1. What I built

I built a research assistant for analysts comparing Apple, Microsoft and Alphabet across a SQLite database of annual financials (FY2023–FY2025) and six FY2024/FY2025 10-K filings. A Fireworks tool-calling agent, **glm-5p3**, combines financial figures with narrative disclosures and returns inspectable evidence through a local chat interface and HTTP API ([screenshots](docs/screenshots/)).

The final system passed **all 13 internal holdout questions across three runs**. Evaluation measures answer correctness and evidence support separately, so a high checklist score does not hide unsupported additions. The main design choices were tested through model comparisons, retrieval ablations and repeated answer-format experiments.

## 2. System structure and analyst experience

The core is a plain Python tool-calling loop with four tools: `query_sql`, `search_filings`, `read_section` and `calculate`. Independent calls run concurrently; dependent questions proceed iteratively. For example, identifying the company with the lowest current ratio requires a database comparison before retrieving its buybacks from the filings. Each result informs the next action. Avoiding an orchestration framework keeps the control flow easy to inspect, test and log.

The agent has an eight-tool-call limit and a 90-second question budget, reserving time to write from the evidence already gathered. Provider failures and timeouts are surfaced explicitly. A single FastAPI process on `localhost:8000` serves the UI, PDFs and `POST /api/chat`, returning JSON with a top-level `answer` or SSE with an `answer` event containing `content`.

The UI shows the direct answer first and folds supporting details into an expandable section. Beside it, analysts can inspect cited passages, open PDFs at the cited page, and see SQL queries with their returned rows. “How I answered” exposes the retrieval and calculation steps. The UI passes the last three exchanges for follow-ups; the API otherwise remains stateless. Storage, retrieval and serving run locally; inference uses Fireworks APIs.

## 3. Retrieval from SQL and PDFs

**Source selection.** The model receives the database schema, actual segment and region names, and source-coverage notes. It uses SQL for headline financials; filings for explanations, risks, strategy and figures absent from the database, such as capex and buybacks; and both for questions asking what changed and why. Wording alone is insufficient: “YouTube ad revenue” sounds like a structured lookup but is available only in the PDFs.

Deterministic guardrails support this routing. A regex pass supplies company and fiscal-year hints; the agent selects search filters. The first turn must call a tool. Before accepting an answer, coverage checks send the agent back once if a narrative question lacks filing evidence or a numeric question lacks SQL or table evidence. The prompt requires derived figures to use SQL or `calculate`; a further check flags percentages absent from tool output. These checks reduce shortcuts but do not guarantee grounding.

**SQL.** Queries use a read-only SQLite connection and return tabular results. Schema and distinct-value injection reduce invented columns and incorrect segment names. The prompt also explains data caveats: Apple’s database categories differ from its geographic reportable segments, Alphabet’s hedging rows are reconciling items, and Microsoft’s segment comparisons use restated definitions.

**PDFs.** `pymupdf4llm` converts pages to markdown, preserving tables. Search uses roughly 900-character child chunks; `read_section` expands relevant hits into parent subsections for context. Tables remain intact, with nearby short captions retained where available. BM25 captures exact names and numbers; qwen3-embedding-8b captures paraphrases. Reciprocal rank fusion combines candidates, then qwen3-reranker-8b reorders the top 30 before six passages are returned. On eight questions with annotated gold pages, recall@6 rose from **0.62 for BM25**, to **0.80 for hybrid search**, to **0.97 with reranking**. For complete risk lists, reading Item 1A instead of snippets resolved omissions on two questions, each passing three subsequent runs.

## 4. Evaluation and remaining failures

**Dataset and protocol.** I used the ten public dev questions and 50 additional questions covering lookups, calculations, narrative synthesis, dependent multi-hop reasoning, cross-checks, follow-ups and out-of-scope requests. Reference answers were verified against SQL or filing pages. The dev questions plus 37 additional questions formed the tuning set; 13 were reserved for the final answer evaluation. Their labels had previously informed an optional planner gate, so this is not a completely untouched holdout; that planner is disabled in the evaluated configuration. The final evaluation’s editor-selection rules were fixed before its runs ([protocol and results](plans/final_eval.md)).

**Grading.** I implemented local counterparts to the three named grading methods; the hidden implementations are unknown:

- **`fuzzy_numeric`:** checks the requested figure’s unit, direction and rounding at the coarser written precision. A judge identifies the answer’s figure so a correct comparator alone cannot pass.
- **`exact_match_entity`:** extracts the company or companies given as the answer, including ranking order when required, with a separate string check.
- **`llm_judge`:** checks human-reviewed fact lists; a pass requires at least 80% coverage and no reference fact contradicted. Failures identify missing or contradicted facts.

I added **`out_of_scope`** grading for appropriate abstention when the data cannot answer a question. The judge, deepseek-v4p1-flash, belongs to a different model family from the answering model.

**Validation.** The judge agreed with my ten hand-graded dev answers, caught 22/22 planted errors, accepted 6/6 harmless edits, and changed none of 57 verdicts on repeat grading. Review identified bugs in numeric grading, citation ranges and evidence bookkeeping; fixes and regression checks left the reported outcomes unchanged. Alternative grading definitions provide a sensitivity check rather than a guarantee of hidden-test performance.

| Final configuration: glm-5p3, prompt v1r, reranking on | Result |
|---|---|
| Internal holdout, 13 questions × 3 runs | **13/13 passed every run**; 39/39 answers; question-level 95% Wilson interval 77–100% |
| In-sample correctness | 47/47 tuning answers; dev and fragile subset 38/39 across three runs |
| Alternative graders, 60 answers | Lenient, holistic and second judge: 60/60 each; strict: 58/60 |
| Evidence judge, holdout | 28/39 answers had no faithfulness flags; 2/39 contained contradictions |
| Holdout latency and chat-model cost | Median 8.1 s; p95 29.4 s; $0.010 per answer, excluding embeddings and reranking |

Diagnostics separately measure source coverage, gold-page retrieval, citation validity, number grounding, answer length and consistency. The final holdout skipped no required source and had no invalid citations. These measurements distinguish retrieval success from factual support: retrieving a relevant page does not establish that every generated claim follows from it.

**Failures.** The only checklist failure in 112 final attempts was an AI-infrastructure comparison: one required fact was never retrieved, while another was retrieved but omitted. Separately, the evidence judge flagged at least one unsupported or contradictory claim in 11/39 holdout answers, including contradictions in two. These answers still passed their question-specific checks, demonstrating why faithfulness needs its own measure. A tuning example described Services revenue as “roughly half” Products’ revenue when the figures imply about one-third. Holdout synthesis answers were also long: median length was 3.4 times the reference. Most questions were authored within the project, limiting generalisation to analysts’ questions.

## 5. Trade-offs and decisions

- **Adaptive retrieval:** On 18 paired questions with the same model and retrieval, the agent passed 18/18, versus 13/18 for a fixed pipeline and 10/18 for single-search RAG. Median latency was 9.8 seconds versus the pipeline’s 30.6 seconds, supporting iterative tool use for this workload.
- **Model and retrieval cost:** Three of seven tested Fireworks models tied at 32/32. glm-5p3 combined zero invalid citations with lower tail latency than deepseek-v4p1-flash and approximately 40% of qwen3p8-max’s chat cost. Reranking adds a call per search, but improved recall and prevented one failure in an 18-question ablation.
- **Completeness and readability:** I tested seven conciseness approaches, including prompt variants, planner-assisted formats and a post-answer editor. None met the acceptance criteria of shorter answers without losing required facts. Even the editor, which shortened responses by 29%, caused two previously passing answers to fail. I therefore prioritised accuracy and completeness, while making answers easy to scan: the UI shows the direct answer first and folds supporting points into an expandable section for busy analysts ([experiments](docs/conciseness_experiments.md)).
- **Grounding:** A stricter prompt reduced tuning answers with unsupported claims from 16/47 to 7/47, but reduced checklist passes from 47/47 to 46/47 and worsened repeat consistency. It failed the predefined acceptance criteria. The baseline remains, with faithfulness reported separately and claim verification prioritised next.
- **Planning and evaluation overhead:** Explicit planning was slower and passed 45/47 versus 47/47 without it, so it is optional. The evidence judge runs offline; using it at answer time would add latency and cost.

## 6. Improvements with more time

First, generate structured claims with source references, verify each claim, and render concise answers from verified facts. This targets unsupported additions and verbosity together. Next, evaluate on a larger analyst-authored set and improve table retrieval by indexing row labels, headers and comparable years. Finally, test cheaper models for simple lookups, cache repeated retrievals, and stream answer tokens while measuring the full inference cost.

**AI assistance:** Claude Code wrote most code and ran experiments; Codex reviewed the system and report. I set requirements, chose designs, hand-graded dev answers, reviewed grading checklists and approved changes.
