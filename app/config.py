"""Central configuration: paths, model ids, and agent budgets.

Everything can be overridden with environment variables (or a .env file in the project root).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "financials.db"
PDF_DIR = DATA_DIR / "pdfs"
INDEX_DIR = DATA_DIR / "index"
TRACE_DIR = ROOT / "traces"

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY", "")
FIREWORKS_BASE_URL = os.getenv("FIREWORKS_BASE_URL", "https://api.fireworks.ai/inference/v1")

_M = "accounts/fireworks/models/"
# Dev default; the shipped model is chosen by the eval (eval/run_eval.py).
CHAT_MODEL = os.getenv("CHAT_MODEL", _M + "glm-5p3")
JUDGE_MODEL = os.getenv("JUDGE_MODEL", _M + "kimi-k3")
EMBED_MODEL = os.getenv("EMBED_MODEL", _M + "qwen3-embedding-8b")
RERANK_MODEL = os.getenv("RERANK_MODEL", _M + "qwen3-reranker-8b")
# Qwen3-Embedding embeds documents as-is and prefixes queries with a task instruction.
EMBED_QUERY_PREFIX = os.getenv(
    "EMBED_QUERY_PREFIX",
    "Instruct: Given a question about a company's 10-K filing, retrieve passages that answer it\nQuery: ",
)

TICKERS = {"AAPL": "Apple", "MSFT": "Microsoft", "GOOGL": "Alphabet"}

# Retrieval
RERANK = os.getenv("RERANK", "1") == "1"
SEARCH_TOP_K = 6

# Agent budgets and sampling
MAX_TOOL_CALLS = 8
MAX_TURNS = 10
MAX_TOKENS = 4096
TEMPERATURE = 0.0
SEED = 7
