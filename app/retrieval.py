"""Hybrid search over child chunks.

BM25 (exact terms such as "Greater China") and dense embeddings (meaning) each propose candidates
within the requested filing(s); the two ranked lists are merged with reciprocal rank fusion and the
merged candidates are optionally rescored by a cross-encoder reranker.
"""

import json
import re
from functools import lru_cache

import numpy as np
from rank_bm25 import BM25Okapi

from app.config import EMBED_QUERY_PREFIX, INDEX_DIR, RERANK, SEARCH_TOP_K
from app.llm import embed, rerank

CANDIDATES = 30
RRF_K = 60
rerank_enabled = RERANK  # process-wide switch; the CLI / eval flip it for ablations
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[.,][0-9]+)*")  # keeps numbers like 416,161 and 15.1 intact


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


class Index:
    def __init__(self):
        self.chunks = [json.loads(line) for line in open(INDEX_DIR / "chunks.jsonl")]
        self.parents = {p["id"]: p for p in map(json.loads, open(INDEX_DIR / "parents.jsonl"))}
        ids = json.loads((INDEX_DIR / "embedding_ids.json").read_text())
        if ids != [c["id"] for c in self.chunks]:
            raise SystemExit("Embeddings are out of date with chunks.jsonl; run: python -m app.ingest")
        self.vecs = np.load(INDEX_DIR / "embeddings.npy").astype(np.float32)
        self.bm25 = BM25Okapi([tokenize(c["context"] + " " + c["text"]) for c in self.chunks])

    def search(self, query: str, ticker: str | None = None, fiscal_year: int | None = None,
               k: int = SEARCH_TOP_K, mode: str = "hybrid", use_rerank: bool | None = None) -> list[dict]:
        """Top-k chunks for `query` within the filings matching ticker / fiscal_year (None = all)."""
        idx = np.array([i for i, c in enumerate(self.chunks)
                        if (ticker is None or c["ticker"] == ticker)
                        and (fiscal_year is None or c["fiscal_year"] == fiscal_year)])
        if len(idx) == 0:
            return []
        ranked_lists = []
        if mode in ("hybrid", "bm25"):
            ranked_lists.append(self.bm25.get_scores(tokenize(query))[idx])
        if mode in ("hybrid", "dense"):
            ranked_lists.append(self.vecs[idx] @ embed([EMBED_QUERY_PREFIX + query])[0])

        fused: dict[int, float] = {}
        for scores in ranked_lists:
            for rank, j in enumerate(np.argsort(-scores)[:CANDIDATES]):
                fused[int(idx[j])] = fused.get(int(idx[j]), 0.0) + 1.0 / (RRF_K + rank + 1)
        candidates = sorted(fused, key=fused.get, reverse=True)[:CANDIDATES]
        scores = [fused[i] for i in candidates]

        if (rerank_enabled if use_rerank is None else use_rerank):
            scores = rerank(query, [self.chunks[i]["context"] + "\n\n" + self.chunks[i]["text"] for i in candidates])
            order = sorted(range(len(candidates)), key=lambda j: -scores[j])
            candidates, scores = [candidates[j] for j in order], [scores[j] for j in order]
        return [{**self.chunks[i], "score": round(float(s), 4)} for i, s in zip(candidates[:k], scores[:k])]


@lru_cache(maxsize=1)
def get_index() -> Index:
    return Index()
