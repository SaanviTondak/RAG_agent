#!/bin/bash

set -euo pipefail

echo "Setting up the Fireworks AI Agentic RAG take-home environment..."
echo ""

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is not installed."
    echo "Install instructions: https://github.com/astral-sh/uv"
    echo "Quick install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "Creating virtual environment..."
uv venv

# shellcheck disable=SC1091
source .venv/bin/activate

echo "Installing starter dependencies..."
uv pip install -r starter/requirements.txt

valid_pdf_count=$(python - <<'PY'
from pathlib import Path
import sys

sys.path.insert(0, "scripts")

from prepare_data import count_valid_pdfs

print(count_valid_pdfs(Path("data/pdfs")))
PY
)
valid_pdf_count=$(echo "$valid_pdf_count" | tail -n 1)  # a library warning on stdout must not break the count

if [ "$valid_pdf_count" -lt 6 ]; then
    echo "Installing Playwright Chromium browser (needed to render PDFs)..."
    playwright install chromium
fi

echo ""
echo "Preparing assignment data..."
python scripts/prepare_data.py --data-dir data

echo ""
if [ -f "data/financials.db" ]; then
    echo "Found data/financials.db"
else
    echo "Error: data/financials.db is missing after setup."
    exit 1
fi

pdf_count=0
for pdf in data/pdfs/*.pdf; do
    if [ -f "$pdf" ]; then
        pdf_count=$((pdf_count + 1))
    fi
done

if [ "$pdf_count" -eq 6 ]; then
    echo "Found $pdf_count PDF filings under data/pdfs/"
else
    echo "Error: expected 6 PDF filings under data/pdfs/ after setup, found $pdf_count."
    exit 1
fi

echo ""
echo "Installing the research assistant's dependencies..."
uv pip install -r requirements.txt

if [ -f "data/index/chunks.jsonl" ] && [ -f "data/index/embeddings.npy" ]; then
    echo "Found the prebuilt search index in data/index/"
else
    echo "Search index missing: build it with 'python -m app.ingest' after setting FIREWORKS_API_KEY (embeds the filings)."
fi

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo ""
    echo "Created .env from .env.example: add your Fireworks API key to it (FIREWORKS_API_KEY=...)."
fi

echo ""
echo "Setup complete."
echo ""
echo "Next steps:"
echo "  1. Put your Fireworks API key in .env (FIREWORKS_API_KEY=...)"
echo "  2. Start the app:   .venv/bin/python -m app.server"
echo "  3. Open http://localhost:8000, or POST to http://localhost:8000/api/chat"
