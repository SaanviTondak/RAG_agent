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

# Model ids are confirmed against the account's model list before being fixed here.
CHAT_MODEL = os.getenv("CHAT_MODEL", "")
JUDGE_MODEL = os.getenv("JUDGE_MODEL", "")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-ai/nomic-embed-text-v1.5")
# Some embedding models expect task prefixes (nomic does); set both to "" for models that don't.
EMBED_DOC_PREFIX = os.getenv("EMBED_DOC_PREFIX", "search_document: ")
EMBED_QUERY_PREFIX = os.getenv("EMBED_QUERY_PREFIX", "search_query: ")

TICKERS = {"AAPL": "Apple", "MSFT": "Microsoft", "GOOGL": "Alphabet"}
