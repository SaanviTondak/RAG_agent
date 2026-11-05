"""Search-only retrieval eval: does search_filings put a gold page in the top k? No LLM involved.

  python -m eval.retrieval_eval [--set tune] [--k 6]

The question text is the query. Filters mirror what the agent usually does: ticker when the question
names exactly one company, and the latest filing the question refers to (FY2025 unless only FY2024 is
mentioned, since the FY2025 10-K explains FY2024 -> FY2025 changes). Compares bm25, dense, hybrid and
hybrid + reranker.
"""

import argparse
from datetime import datetime

from app.agent import YEAR_RE
from eval.graders import _chunk_pages, entities_in
from eval.run_eval import RESULTS_DIR, load_set
from app.retrieval import get_index

CONFIGS = [("bm25", False), ("dense", False), ("hybrid", False), ("hybrid", True)]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", choices=["dev", "extra", "tune"], default="tune")
    ap.add_argument("--k", type=int, default=6)
    a = ap.parse_args()

    questions = [q for q in load_set(a.set) if q.get("gold_pages")]
    index, pages = get_index(), _chunk_pages()
    stats = {c: {"hit": 0, "recall": 0.0, "rr": 0.0} for c in CONFIGS}
    rows = []
    for q in questions:
        companies = entities_in(q["question"])
        ticker = companies[0] if len(companies) == 1 else None
        years = {int(y) if y else 2000 + int(yy) for y, yy in YEAR_RE.findall(q["question"])} & {2024, 2025}
        year = max(years, default=2025)
        gold = {(g["doc"], g["page"]) for g in q["gold_pages"]}
        cells = []
        for mode, rerank in CONFIGS:
            hits = index.search(q["question"], ticker=ticker, fiscal_year=year, k=a.k, mode=mode, use_rerank=rerank)
            found, first = set(), None
            for rank, h in enumerate(hits, 1):
                start, end = pages[h["id"]]
                hit_pages = {(h["doc"], p) for p in range(start, end + 1)} & gold
                if hit_pages and first is None:
                    first = rank
                found |= hit_pages
            s = stats[(mode, rerank)]
            s["hit"] += bool(found)
            s["recall"] += len(found) / len(gold)
            s["rr"] += 1 / first if first else 0.0
            cells.append(f"{len(found)}/{len(gold)}" + (f" (#{first})" if first else ""))
        rows.append(f"| {q['id']} | {ticker or 'all'} FY{year} | " + " | ".join(cells) + " |")

    n = len(questions)
    names = [f"{m}{' + rerank' if r else ''}" for m, r in CONFIGS]
    md = [f"# Retrieval eval ({a.set}, {n} questions with gold pages, k={a.k})", "",
          "| Config | Hit@k (any gold page) | Recall@k (share of gold pages) | MRR |", "|---|---|---|---|"]
    md += [f"| {name} | {stats[c]['hit']}/{n} | {stats[c]['recall'] / n:.2f} | {stats[c]['rr'] / n:.2f} |"
           for name, c in zip(names, CONFIGS)]
    md += ["", "Per question: gold pages found (rank of the first hit).", "",
           "| id | filter | " + " | ".join(names) + " |", "|---|---|" + "---|" * len(names), *rows]
    out = RESULTS_DIR / f"retrieval_{datetime.now():%Y%m%d-%H%M}_{a.set}.md"
    RESULTS_DIR.mkdir(exist_ok=True)
    out.write_text("\n".join(md) + "\n")
    print("\n".join(md[:8]))
    print(f"\nWritten {out}")


if __name__ == "__main__":
    main()
