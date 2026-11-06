# Day 5 plan: server, API and UI

**Goal:** a reviewer runs one command, opens http://localhost:8000, asks questions, watches the agent work, and
checks every cited figure against its source; Fireworks' evaluator can call `POST /api/chat` reliably.

## Agreed decisions (2026-11-05)

| # | Decision |
|---|---|
| 1 | **FastAPI + uvicorn**, one process on 127.0.0.1:8000 (API, UI, PDFs). `python -m app.server`. Free API docs at `/docs`. |
| 2 | **API:** `POST /api/chat {"question", "history"?}`. JSON by default: `{"answer", "content" (same text), "sources", "steps", "usage"}`. SSE when `Accept: text/event-stream` or `?stream=true`: `step` events, then `answer` `{"content"}`, then `done`. `usage` stays in the JSON (developer-facing). |
| 3 | **Honest status codes** (Saanvi: a 200 on failure is misleading): 422 bad request, 502 model provider failed, 504 out of time, 500 our bug. SSE has already sent 200 when the stream starts, so mid-stream failures are an `error` event with the same code. |
| 4 | **Time budget 90s** (Saanvi: preserve answer quality; 55s was too tight). No new tool calls after 55s (leaves room for the slowest final writing call seen, 36s); every model call gets the remaining time as its timeout; past 90s -> 504. Configurable `AGENT_TIME_BUDGET_S`. None of the 90 measured answers would hit either limit (max 56s). |
| 5 | **Custom single page** (HTML + plain JS, no build step, no CDN), calling our own API, so every UI question also exercises the API. |
| 6 | **Steps streamed live, plain text, no emojis** ("Searching filings: ... (AAPL, FY2025 10-K)", "Querying database: ...", "Calculating: ..."). No token streaming of the answer. Steps collapse into "How I answered" once done. **No cost/time shown in the UI.** |
| 7 | **Evidence panel shows cited items only:** each cited filing page (snippet + link that opens the PDF at that page) and the SQL result for each `[SQL: table]` citation. Citations in the answer are links. "No sources cited" otherwise. |
| 8 | **Follow-ups:** the page keeps the last 3 exchanges and sends them as `history`; server stays stateless. "New chat" clears it. |
| 9 | Example question buttons; `GET /api/health`; search index loaded at startup (0.7s). |

## Status (2026-11-05): done
- `app/server.py`, `app/evidence.py` (cited evidence + plain step labels; citation regexes now shared with the eval),
  `app/static/index.html`, deadline support in `app/llm.py` / `app/agent.py` (`AGENT_TIME_BUDGET_S`, `TOOL_CUTOFF_S`).
- Tests: `python -m unittest tests.test_budget tests.test_server` -> 11 pass (fake agent, no cost).
- Real curls: JSON (answer + content), SSE (step -> answer {"content"} -> sources -> done), 422 on blank question.
- Playwright: live steps, answer + evidence with PDF page links, follow-up ("What about Japan?" -> correct x_024
  answer), click-to-switch evidence, phone layout. Screenshots in `docs/screenshots/`.
- Bugs found in the click-through and fixed: body scrolled under the header; hovering a citation switched the
  evidence panel to another answer; "How I answered" sat above the answer.
- Spend ~$0.08.

## Steps
1. `requirements.txt`: fastapi, uvicorn.
2. `app/llm.py` + `app/agent.py`: deadline support (time budget), provider-failure exception type.
3. `app/server.py`: endpoints, SSE, error mapping, evidence (cited sources) and step formatting.
4. `app/static/index.html`: the page.
5. Tests: `tests/test_server.py` with a fake agent (JSON fields, SSE events, 422/502/504/500); one real curl of each
   format; Playwright click-through + screenshots for the report. API cost ~$0.10.
