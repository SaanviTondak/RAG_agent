"""Thin Fireworks client: chat, embeddings, and rerank, with retries on transient errors."""

import time

import numpy as np
import requests
from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError

from app.config import EMBED_MODEL, FIREWORKS_API_KEY, FIREWORKS_BASE_URL, PRICES, RERANK_MODEL

MISSING_KEY = "FIREWORKS_API_KEY is not set. Put it in .env or export it in your shell."
# The key is checked when a model is called, not on import, so the tests and tools that make no calls run without it.
client = OpenAI(api_key=FIREWORKS_API_KEY or "unset", base_url=FIREWORKS_BASE_URL, max_retries=0, timeout=120)

RETRIES = 4


class ProviderError(RuntimeError):
    """Fireworks kept failing (rate limits, server errors, timeouts) after all retries."""


class MissingKeyError(RuntimeError):
    """No Fireworks API key is configured."""


class DeadlineExceeded(TimeoutError):
    """The caller's time budget ran out before Fireworks answered."""


#retries when Fireworks is rate-limited or has a temporary server error, 
# with increasing waits, and fails immediately on mistakes like a bad request.


def _retry(fn, deadline: float | None = None):
    if not FIREWORKS_API_KEY:
        raise MissingKeyError(MISSING_KEY)
    for attempt in range(RETRIES):
        if deadline is not None and time.time() >= deadline:
            raise DeadlineExceeded("time budget exhausted waiting for Fireworks")
        try:
            return fn()
        except (RateLimitError, APIConnectionError, requests.ConnectionError, requests.Timeout):
            pass
        except APIStatusError as e:
            if e.status_code < 500:
                raise
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code < 500 and e.response.status_code != 429:
                raise
        if attempt == RETRIES - 1:
            raise ProviderError("Fireworks request failed after retries")
        wait = 2**attempt
        if deadline is not None:
            wait = min(wait, max(0.0, deadline - time.time()))
        time.sleep(wait)


def chat(deadline: float | None = None, **kwargs):
    """Chat completion. With a deadline (epoch seconds), each attempt may only use the time left."""

    def call():
        if deadline is not None:
            kwargs["timeout"] = max(1.0, deadline - time.time())
        return client.chat.completions.create(**kwargs)

    return _retry(call, deadline)


def cached_tokens(usage) -> int:
    details = getattr(usage, "prompt_tokens_details", None)
    return (getattr(details, "cached_tokens", None) or 0) if details else 0


def cost_usd(model: str, prompt_tokens: int, completion_tokens: int, cached: int = 0) -> float:
    """LLM cost from token counts; unknown models are priced as 0 (and flagged by callers)."""
    p_in, p_cached, p_out = PRICES.get(model.rsplit("/", 1)[-1], (0.0, 0.0, 0.0))
    return ((prompt_tokens - cached) * p_in + cached * p_cached + completion_tokens * p_out) / 1e6


def embed(texts: list[str], batch_size: int = 64) -> np.ndarray:
    """Unit-normalised embeddings, shape (len(texts), dim)."""
    out = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        resp = _retry(lambda: client.embeddings.create(model=EMBED_MODEL, input=batch))
        out += [d.embedding for d in resp.data]
    vecs = np.asarray(out, dtype=np.float32)
    return vecs / np.linalg.norm(vecs, axis=1, keepdims=True)


def rerank(query: str, documents: list[str]) -> list[float]:
    """Relevance score per document, in the original order."""

    def call():
        r = requests.post(
            f"{FIREWORKS_BASE_URL}/rerank",
            headers={"Authorization": f"Bearer {FIREWORKS_API_KEY}"},
            json={"model": RERANK_MODEL, "query": query, "documents": documents},
            timeout=60,
        )
        r.raise_for_status()
        return r.json()["data"]

    scores = [0.0] * len(documents)
    for d in _retry(call):
        scores[d["index"]] = d["relevance_score"]
    return scores
