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
# Chosen by eval/calibrate_judge.py + eval/judge_stress.py: same agreement as kimi-k3 at ~1/8 the cost.
JUDGE_MODEL = os.getenv("JUDGE_MODEL", _M + "deepseek-v4p1-flash")
EMBED_MODEL = os.getenv("EMBED_MODEL", _M + "qwen3-embedding-8b")
RERANK_MODEL = os.getenv("RERANK_MODEL", _M + "qwen3-reranker-8b")
# Qwen3-Embedding embeds documents as-is and prefixes queries with a task instruction.
EMBED_QUERY_PREFIX = os.getenv(
    "EMBED_QUERY_PREFIX",
    "Instruct: Given a question about a company's 10-K filing, retrieve passages that answer it\nQuery: ",
)

# Fireworks serverless prices, USD per 1M tokens: (input, cached input, output). From fireworks.ai/pricing, 2026-11-04.
PRICES = {
    "glm-5p3": (1.40, 0.26, 4.40),
    "glm-5p3-flash": (0.15, 0.03, 0.50),
    "kimi-k3": (3.00, 0.30, 15.00),
    "deepseek-v4p1-flash": (0.30, 0.006, 1.20),
    "qwen3p8-max": (2.00, 0.25, 6.00),
    "gpt-oss-120b": (0.15, 0.015, 0.60),
    "minimax-m3": (0.30, 0.06, 1.20),
}

# Answer-format version in app/prompts.py; chosen by the eval. v1r = v1 + read Item 1A for risk-factor questions
# (q_006 and x_014 passed 3/3 each in the final tuning runs; plans/final_eval.md).
PROMPT_VERSION = os.getenv("PROMPT_VERSION", "v1r")
# Send the model back once if a percentage in its draft appears in no tool result (app/agent.py).
GROUNDING_NUDGE = os.getenv("GROUNDING_NUDGE", "1") == "1"  # on: fired 3/3 on q_008 and fixed it, ~no cost
# "auto": plan multi-part questions first (app/planner.py); "on": plan every question; "off": never plan.
# Off by default: on 47 tuning questions it did not improve accuracy (45/47 vs 47/47) and was slower. The UI's
# "Plan first" toggle turns it on per question.
PLANNER = os.getenv("PLANNER", "off")
# Shorten long final answers with one extra call (app/editor.py). Not EDITOR: that is the shell's text editor.
# Off: in the final tuning runs it cut length 29% but made 2 of 44 passing answers fail (dropped "iCloud"; kept the
# 10-K's rounded 21% instead of 21.5%), failing the rule fixed in plans/final_eval.md before the runs.
ANSWER_EDITOR = os.getenv("ANSWER_EDITOR", "0") == "1"

TICKERS = {"AAPL": "Apple", "MSFT": "Microsoft", "GOOGL": "Alphabet"}

# Retrieval
RERANK = os.getenv("RERANK", "1") == "1"
SEARCH_TOP_K = 6

# Agent budgets and sampling
MAX_TOOL_CALLS = 8
# Wall-clock budget per question. No new tool calls after TOOL_CUTOFF_S, leaving room for the final writing call
# (slowest seen: 36s); past the budget the server returns 504. None of 90 measured answers hit either (max 56s).
AGENT_TIME_BUDGET_S = float(os.getenv("AGENT_TIME_BUDGET_S", "90"))
TOOL_CUTOFF_S = AGENT_TIME_BUDGET_S - 35
MAX_TURNS = 10
MAX_TOKENS = 4096
TEMPERATURE = 0.0
SEED = 7
