"""HTTP API + web UI on one port.

  python -m app.server            # http://localhost:8000  (API docs at /docs)

POST /api/chat {"question": "...", "history": [{"role": "user"|"assistant", "content": "..."}]?, "plan": bool?}
- JSON (default): {"answer", "content" (same text), "sources" (cited evidence), "steps", "usage"}
- SSE (Accept: text/event-stream, or ?stream=true): "step" events as tools run, then "answer" {"content"},
  then "sources" {"sources", "steps", "usage"}, then "done". Comment lines keep the stream alive.
Errors: 422 bad request, 502 model provider failed, 504 time budget exceeded, 500 bug. A stream has already
sent 200 when it starts, so a failure mid-stream is an "error" event {"status", "error"} instead.
"""

import asyncio
import json
import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

import uvicorn
from fastapi import FastAPI, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator

from app import agent
from app.config import AGENT_TIME_BUDGET_S, CHAT_MODEL, FIREWORKS_API_KEY, PDF_DIR
from app.evidence import cited_evidence, step_view, steps_view
from app.llm import MISSING_KEY, DeadlineExceeded, ProviderError
from app.numbers import body
from app.retrieval import get_index

log = logging.getLogger("app.server")
STATIC_DIR = Path(__file__).parent / "static"
HISTORY_MESSAGES = 6  # last 3 exchanges
HARD_TIMEOUT_S = AGENT_TIME_BUDGET_S + 2  # backstop if a tool call stalls past the agent's own budget
KEEPALIVE_S = 15


@asynccontextmanager
async def lifespan(_: FastAPI):
    get_index()  # load the search index now, not on the first question
    yield


app = FastAPI(title="Acme 10-K research assistant", lifespan=lifespan,
              description="Answers questions about Apple, Microsoft and Alphabet from a financials database and "
                          "their FY2024/FY2025 10-K filings, with cited evidence.")
app.mount("/pdfs", StaticFiles(directory=PDF_DIR), name="pdfs")


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, description="The question to answer.")
    history: list[Turn] = Field(default_factory=list, description="Earlier turns, for follow-up questions.")
    plan: bool | None = Field(None, description="true: write and show a plan before researching (slower); "
                                                "false: never; omitted: the server default (PLANNER).")

    @field_validator("question")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("question must not be blank")
        return v.strip()


def _history(req: ChatRequest) -> list[dict]:
    turns = req.history[-HISTORY_MESSAGES:]
    return [{"role": t.role, "content": body(t.content) if t.role == "assistant" else t.content} for t in turns]


def _agent_kwargs(req: ChatRequest) -> dict:
    return {} if req.plan is None else {"planner": "on" if req.plan else "off"}


def _payload(result: dict) -> dict:
    u = result["usage"]
    return {"answer": result["answer"], "content": result["answer"], "sources": cited_evidence(result),
            "steps": steps_view(result),
            "usage": {"latency_s": round(u["latency_ms"] / 1000, 1), "llm_calls": u["llm_calls"],
                      "tool_calls": u["tool_calls"], "prompt_tokens": u["prompt_tokens"],
                      "completion_tokens": u["completion_tokens"], "cost_usd": u["cost_usd"],
                      "model": result["model"].rsplit("/", 1)[-1]}}


def _error(exc: BaseException) -> tuple[int, str]:
    if isinstance(exc, (DeadlineExceeded, asyncio.TimeoutError, TimeoutError)):
        return 504, f"No answer within the {AGENT_TIME_BUDGET_S:.0f}s time budget."
    if isinstance(exc, ProviderError):
        return 502, "The model provider (Fireworks) failed repeatedly; try again shortly."
    log.exception("agent failed", exc_info=exc)
    return 500, f"Internal error: {type(exc).__name__}"


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "model": CHAT_MODEL.rsplit("/", 1)[-1], "chunks": len(get_index().chunks)}


@app.post("/api/chat")
async def chat(req: ChatRequest, request: Request):
    stream = "text/event-stream" in request.headers.get("accept", "") \
        or request.query_params.get("stream", "").lower() in ("1", "true", "yes")
    history = _history(req)
    if not stream:
        try:
            result = await asyncio.wait_for(run_in_threadpool(agent.run, req.question, history, **_agent_kwargs(req)),
                                            HARD_TIMEOUT_S)
        except Exception as e:  # noqa: BLE001 - mapped to an honest status code
            status, message = _error(e)
            return JSONResponse({"error": message}, status_code=status)
        return _payload(result)
    return StreamingResponse(_stream(req.question, history, _agent_kwargs(req)), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


async def _stream(question: str, history: list[dict], kwargs: dict):
    loop = asyncio.get_running_loop()
    queue: asyncio.Queue = asyncio.Queue()

    def on_step(step: dict) -> None:
        view = step_view(step)
        if view:
            loop.call_soon_threadsafe(queue.put_nowait, ("step", view))

    task = loop.run_in_executor(None, lambda: agent.run(question, history, on_step=on_step, **kwargs))
    deadline = loop.time() + HARD_TIMEOUT_S
    while True:
        if task.done() and queue.empty():
            break
        remaining = deadline - loop.time()
        if remaining <= 0:
            yield _sse("error", {"status": 504, "error": _error(TimeoutError())[1]})
            return
        getter = asyncio.ensure_future(queue.get())
        done, _ = await asyncio.wait({getter, task}, timeout=min(KEEPALIVE_S, remaining),
                                     return_when=asyncio.FIRST_COMPLETED)
        if getter in done:
            kind, data = getter.result()
            yield _sse(kind, data)
        else:
            getter.cancel()
            if not done:
                yield ": keepalive\n\n"
    try:
        result = task.result()
    except Exception as e:  # noqa: BLE001
        status, message = _error(e)
        yield _sse("error", {"status": status, "error": message})
        return
    payload = _payload(result)
    yield _sse("answer", {"content": payload["answer"]})
    yield _sse("sources", {k: payload[k] for k in ("sources", "steps", "usage")})
    yield _sse("done", {})


def main() -> None:
    if not FIREWORKS_API_KEY:
        raise SystemExit(MISSING_KEY)  # fail at start-up, not on the first question
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8000")))


if __name__ == "__main__":
    main()
