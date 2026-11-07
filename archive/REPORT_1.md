# Agentic RAG over 10-Ks: technical report

## 1. What I built
A local research assistant that answers questions about Apple, Microsoft and Alphabet from a SQLite database of
annual financials (FY2023–FY2025) and their six FY2024/FY2025 10-Ks. A tool-calling agent on Fireworks
(**glm-5p3**) decides which source each question needs, gathers evidence over several steps, computes derived
figures with a calculator, and answers with checkable citations ([screenshots](docs/screenshots/)).

## 2. How the system is structured
**The agent** (`app/agent.py`) is a plain tool-calling loop on glm-5p3, written without a framework so every step
can be logged, tested and evaluated. Before the model sees a question, a regex pass adds the companies and fiscal
years it mentions. The model then works with four tools: `query_sql`, `search_filings`, `read_section` (a whole
subsection or 10-K Item) and `calculate`, calling several at once when they are independent. Multi-step questions,
such as "the company with the lowest current ratio: what did it spend on buybacks?", are handled by the loop itself:
the agent fetches, reads the result and decides its next call, within 8 tool calls and 90 s, after which it answers
from what it has. Small deterministic checks (§3) send it back when it takes a shortcut. An optional planner ("Plan
first" in the UI) writes out the sub-questions first, for users who want to see the plan.

**Grounding.** Every number must come from a tool, and every answer ends with its sources (`[SQL: table]`,
`[TICKER FY 10-K, p.N]`). Because the brief asks for evidence that is easy to inspect, the web page shows, beside
each answer, only what it cites: each cited filing page with the passages the agent actually read and an "Open PDF
at p.N" link, and each SQL citation with its exact query and rows. "How I answered" replays every search,
query and calculation.

**Serving.** One FastAPI process on `localhost:8000` serves the page, the PDFs and `POST /api/chat`, which returns
JSON (`answer` and `content`, plus `sources` and `steps`) or an SSE stream (`step` events, then `answer
{"content"}`). Failures return 422, 502, 504 or 500, never a misleading 200 (a stream already under way ends with an `error` event). The page shows each step live and keeps
the last three exchanges for follow-ups. The database, PDFs and a prebuilt search
index ship with the code, so a reviewer needs only a Fireworks key to run it locally.

**How it was built.** In measured stages: index → tools and agent → evaluation harness (before any tuning) → model
choice → API and UI → a final evaluation with its decision rules fixed in advance (`plans/`, `results/`).
**AI assistance:** Claude Code wrote most of the code and ran the experiments; I set the requirements, chose between
design options after evaluating trade-offs, hand-graded the dev answers, reviewed every grading checklist and
approved each change. Codex reviewed the finished system and found three grader bugs, now fixed.

## 3. Retrieval from SQL and PDFs
**Choosing the source.** The LLM routes through its tool calls. Its prompt holds what it needs to choose: the schema
and real segment and region names; rules (database for headline figures; filings for explanations, risks, strategy,
definitions and anything the database lacks; both when a question asks what changed *and* why); and a list of what the
database does *not* hold (sub-segments, cash flows, capex, buybacks). Deterministic code checks it rather than
replacing it: regex passes the company and year as search filters; the first turn must call a tool; and the agent is
sent back once if a "why/risk/explain" question never touched the filings, or a numeric one never touched SQL or a
table. I chose this over a rule-based router because wording does not reveal the source ("YouTube ad revenue" is only
in the PDFs), many questions need both, and there was no data to train a router.

**SQL.** One read-only `SELECT` per call, returned as a table. Every derived number (growth, shares, ratios) must
come from SQL or `calculate`; a check sends the agent back if a percentage in its draft appears in no tool result.

**PDFs**, each choice for a reason:
- *Conversion:* `pymupdf4llm` turns pages into markdown and keeps financial tables as tables.
- *Small-to-big chunks:* search runs over ~900-character chunks (2,747), which match a query precisely;
  `read_section` then returns the whole subsection around a hit (593 subsections) for context. A table is never
  split from its caption, so numbers keep their labels.
- *Agent-driven search:* the agent writes its own queries, filters by company and filing, and searches again when
  results are incomplete.
- *Hybrid search:* BM25 catches exact names and numbers ("Greater China", "Intelligent Cloud"); embeddings
  (qwen3-embedding-8b) catch paraphrase ("AI infrastructure costs"). Their candidate lists are merged with
  reciprocal rank fusion, which needs no score tuning, and a cross-encoder (qwen3-reranker-8b) reorders the top 30
  before the best 6 are returned. On 8 questions with marked gold pages, recall@6 was 0.62 (BM25), 0.72 (embeddings),
  0.80 (hybrid) and **0.97 with the reranker**, the largest single gain.
- *Complete lists:* "which risks does the 10-K disclose" questions read the whole Item 1A instead of snippets,
  which fixed two questions that had been dropping risks (3/3 runs each since).

## 4. How I evaluate it
**Test questions.** The 10 dev questions plus 50 of my own, tagged by complexity to match the brief's "increasingly
complex questions" and the prototype's failures (planning, multiple retrievals, narrative plus financials): 0 out of scope, 1 lookup, 2 calculation or comparison, 3 figure plus
explanation, 4 multi-part synthesis, 5 dependent multi-hop ("the company with the lowest current ratio: what did it
spend on buybacks?"), 6 cross-checking text against tables, 7 follow-ups. Gold answers come from SQL or the filing
page, never from the agent. 37 questions were used for tuning; **13 form a holdout that was never used for tuning
and first run on the final system**. Dev and tuning results are therefore in-sample.

**Graders**, mirroring the three official names and deliberately strict, so that passing ours should mean passing theirs:
*fuzzy_numeric* compares at the coarser of the two precisions with no percentage tolerance, requires the same unit
and direction, and has a judge pick the figure the answer gives *as its answer*, so a correct number used only as a
comparison does not pass. *exact_match_entity* has a judge extract the company given as the answer (runners-up do
not count), with a string check alongside. *llm_judge* checks a human-reviewed **list of facts** (pass: at least 80%
covered and none contradicted) rather than giving one overall score, so every failure names the missing fact.
The judge, deepseek-v4p1-flash, comes from a different model family from the answer model.

**Checking the graders.** The judge agreed with my hand grades 10/10, caught 22/22 errors planted in good answers
and passed 6/6 harmless edits, and changed 0 of 57 verdicts when regrading. Results hold under alternative grader
definitions (below). Codex's review found three grader bugs (units and signs in numbers, citation page ranges,
evidence bookkeeping); after the fixes and regression tests, no result changed.

**Diagnostics on every answer** explain *why* an answer passed or failed, and feed the failure analysis
(`eval/failures.py`) and the decision rules. Figures are tuning run / holdout. *Routing*: no required source was
ever skipped (an extra source was used in 7 answers in each set). *Gold-page recall*: retrieval reached a page holding
the answer for 23/24 and 18/18 questions. *Citation validity*: every cited page had been retrieved and every cited
table queried (0 invalid). *Number grounding*: 4 and 2 answers contained a number found in no tool output, usually
mental arithmetic. *Faithfulness*: 16/47 and 11/39 answers made a claim no tool returned, and 1 and 2 contradicted the
evidence (the check caught 6/6 planted claims). *Opening paragraph*: it alone would pass in 33/47 and 33/39 answers.
*Length*: median 4.6× and 3.4× the gold answer. *Consistency*: 12/13 dev and fragile questions and 13/13 holdout
questions passed in all 3 runs. *Speed and cost*: p50 / p95 11.9 s / 27.5 s and 8.1 s / 29.4 s; $0.010 per holdout
answer.

**Results** (final system, prompt v1r; run ids and decision rules in [`plans/final_eval.md`](plans/final_eval.md)):

| | Result |
|---|---|
| Holdout, 13 questions × 3 runs | **13/13 pass every run** (39/39 answers); 95% CI 77–100% per question |
| In-sample | Tuning set 47/47; dev and fragile questions over 3 runs 38/39 |
| By complexity | Every level passes in the tuning run and holdout, from lookups to multi-hop, cross-checks and follow-ups |
| Alternative graders (60 answers) | Lenient, whole-answer judge, second judge (kimi-k3): 60/60 each; strict: 58/60 |
| Fully backed by the evidence | 28/39 holdout answers; 2/39 contain a contradiction |

**Where it still fails.** (1) *Extra claims* (11 of 39 holdout answers, 2 with a contradiction): checklist-correct
answers sometimes add statements the evidence does not support, e.g. Services margin "on roughly half the revenue" of
Products (really about a third). (2) *Partial retrieval on open-ended questions* (the only failure in 112 final
answers): x_047 failed 1 of 3 runs because one page was never retrieved and one fact that was read was left out.
(3) *Length* (median 3.4× the gold answer on the holdout): answers are long, though the direct answer is usually first.

## 5. Trade-offs
- **An LLM agent routes; rules only check it.** A rule router fails because wording does not reveal the source, and a
  fixed plan-then-fetch pipeline cannot adjust after seeing results. With the same model and retrieval, the agent
  answered 18/18 questions, the pipeline 13/18 and single-search RAG 10/18, and the agent was faster (median 9.8 s
  vs 30.6 s).
- **glm-5p3 as the answer model.** Three of seven Fireworks models tied at 32/32. glm-5p3 was the most reliable of
  them (no invalid citations where deepseek-v4p1-flash had 6; p95 41 s vs 83 s) at about 40% of qwen3p8-max's cost.
- **A reranker on every search.** It adds a model call per search but raised recall@6 from 0.80 to 0.97; without it
  the agent lost 1 of 18 answers.
- **Completeness over brevity.** Seven attempts to shorten answers each did it by dropping facts. The best, an
  editor that rewrote finished answers, cut length 29% but turned 2 of 44 correct answers wrong
  ([details](docs/conciseness_experiments.md)). I prioritised accuracy and completeness while keeping answers easy to scan: the UI leads with a direct answer, with supporting details tucked into an expandable section so busy analysts can choose how much to read.
- **Faithfulness: measured and reported, not forced by a prompt.** The faithfulness check showed that answers
  which pass their checklist sometimes add claims no tool returned (16 of 47 tuning answers). A prompt forbidding
  unstated claims (v1g) cut that to 7/47, but it also stripped explanation from opening paragraphs (33 → 28
  answerable from the opening alone) and made a fragile question worse, so it failed the rule set before the run.
  The more complete prompt ships, faithfulness is reported as its own result, and per-claim checking is the first
  item below.
- **Planner off by default.** Planning first did not improve accuracy (45/47 vs 47/47) and was slower. It stays as a
  toggle because it makes the plan visible.
- **A 90 s budget** rather than 60 s, to protect multi-hop answers; in practice p95 is about 30 s.
- **Strict graders and a cheap judge.** Strict grading errs toward failing an answer, and deepseek-v4p1-flash matched
  kimi-k3's agreement with my grades at about an eighth of the cost.

## 6. What I would improve with more time
1. **Check every claim at answer time** (a source per sentence, verified before sending): a prompt rule alone lost completeness.
2. **Short answers by construction:** generate structured facts with sources, then render a short answer from them.
3. **A larger test set written by analysts**, to narrow the 77–100% interval.
4. **Cost and latency:** simple lookups on glm-5p3-flash (31/32 at a ninth of the cost); caching; token streaming.
5. **Table-aware retrieval:** index table rows and headers as fields; link the same table across years.
