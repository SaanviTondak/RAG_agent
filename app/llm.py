"""Thin Fireworks client: chat, embeddings, and rerank, with retries on transient errors."""

import time

import numpy as np
import requests
from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError

from app.config import EMBED_MODEL, FIREWORKS_API_KEY, FIREWORKS_BASE_URL, RERANK_MODEL

if not FIREWORKS_API_KEY:
    raise SystemExit("FIREWORKS_API_KEY is not set. Put it in .env or export it in your shell.")

client = OpenAI(api_key=FIREWORKS_API_KEY, base_url=FIREWORKS_BASE_URL, max_retries=0, timeout=120)

RETRIES = 4


def _retry(fn):
    for attempt in range(RETRIES):
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
            raise RuntimeError("Fireworks request failed after retries")
        time.sleep(2**attempt)


def chat(**kwargs):
    return _retry(lambda: client.chat.completions.create(**kwargs))


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
