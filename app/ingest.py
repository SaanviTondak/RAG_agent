"""Ingest the 10-K PDFs into parent sections and child chunks.

PDF -> per-page markdown (pymupdf4llm keeps tables as markdown tables) -> blocks (headings,
paragraphs, tables) -> parents -> children.

- Parents are 10-K subsections: split on "Item N." headings, then on markdown headings, then packed
  to a few thousand characters. `read_section` returns parents, so the agent can read a whole
  subsection once search has found it.
- Children are ~900-character pieces of a parent and are what search runs over. A table is never
  split; it becomes one child together with its short caption paragraph.

Outputs in data/index/: pages/<doc>.json (cached conversion), parents.jsonl, chunks.jsonl,
embeddings.npy (+ embedding_ids.json).
Run: python -m app.ingest
"""

import json
import re
import string
import time

import numpy as np
import pymupdf4llm

from app.config import INDEX_DIR, PDF_DIR

ITEM_RE = re.compile(r"^ITEM\s+(\d{1,2}[A-C]?)\.\s+(\S.*)$", re.I)
HTML_TAG_RE = re.compile(r"</?[a-z][^>]*>", re.I)
NOISE_RES = [
    re.compile(r"^table of contents$", re.I),
    re.compile(r"^items?\s+\d{1,2}[a-c]?(\s*,\s*\d{1,2}[a-c]?)*$", re.I),  # running headers: "Item 1", "Item 9, 9A"
    re.compile(r"^part\s+i{1,3}v?$", re.I),
    re.compile(r"^\d{1,3}\.?$"),  # bare page numbers
    re.compile(r"^.{0,40}\|\s*20\d\d form 10-k\s*\|\s*\d+$", re.I),  # "Apple Inc. | 2025 Form 10-K | 22"
    re.compile(r"^(apple inc\.|alphabet inc\.|microsoft corporation)$", re.I),
]

PARENT_TARGET_CHARS = 4000
PARENT_MAX_CHARS = 8000
CHILD_TARGET_CHARS = 900
CAPTION_MAX_CHARS = 500


def _plain(line: str) -> str:
    """Line text without markdown/HTML decoration, for matching headings and noise."""
    text = HTML_TAG_RE.sub(" ", line)
    text = re.sub(r"[#*_>]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _is_noise(text: str) -> bool:
    return any(r.match(text) for r in NOISE_RES)


def load_pages(doc: str) -> list[dict]:
    """Per-page markdown for one filing, converted once and cached."""
    cache = INDEX_DIR / "pages" / f"{doc}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    pages = pymupdf4llm.to_markdown(str(PDF_DIR / f"{doc}.pdf"), page_chunks=True, show_progress=False)
    out = [{"page": i + 1, "text": p["text"]} for i, p in enumerate(pages)]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(out))
    return out


def to_blocks(pages: list[dict]) -> list[dict]:
    """Flatten pages into item / heading / text / table blocks, dropping running headers."""
    blocks = []
    for pg in pages:
        cur = None
        for raw in pg["text"].splitlines():
            line = HTML_TAG_RE.sub(" ", raw).rstrip()
            text = _plain(line)
            kind = "table" if line.lstrip().startswith("|") else "text"
            if kind == "text" and (not text or _is_noise(text)):
                cur = None
                continue
            if kind == "text":
                item = ITEM_RE.match(text) if "**" in line else None
                if item or line.lstrip().startswith("#"):
                    blocks.append({"kind": "item" if item else "heading", "text": text, "page": pg["page"],
                                   "item": (item.group(1).upper(), _title(item.group(2))) if item else None})
                    cur = None
                    continue
            if cur and cur["kind"] == kind:
                cur["text"] += "\n" + line if kind == "table" else " " + line.strip()
            else:
                cur = {"kind": kind, "text": line if kind == "table" else line.strip(), "page": pg["page"]}
                blocks.append(cur)
    return blocks


def _title(title: str) -> str:
    title = title.strip().rstrip(".")
    return string.capwords(title) if title.isupper() else title


def to_sections(blocks: list[dict]) -> list[dict]:
    """Group blocks into raw sections: one per item heading or markdown heading."""
    sections = []
    item = ("0", "Cover and Forward-Looking Statements")
    cur = None
    for b in blocks:
        if b["kind"] in ("item", "heading"):
            if b["kind"] == "item":
                item = b["item"]
            cur = {"item": item, "heading": b["text"], "blocks": []}
            sections.append(cur)
            continue
        if cur is None:
            cur = {"item": item, "heading": "", "blocks": []}
            sections.append(cur)
        b["heading"] = cur["heading"]
        cur["blocks"].append(b)
    return [s for s in sections if s["blocks"]]


def _size(blocks: list[dict]) -> int:
    return sum(len(b["text"]) for b in blocks)


def to_parents(sections: list[dict]) -> list[dict]:
    """Pack consecutive small sections of the same item together; split oversized ones."""
    packed = []
    for s in sections:
        prev = packed[-1] if packed else None
        if prev and prev["item"] == s["item"] and _size(prev["blocks"]) + _size(s["blocks"]) <= PARENT_TARGET_CHARS:
            prev["blocks"] += s["blocks"]
            prev["headings"].append(s["heading"])
        else:
            packed.append({"item": s["item"], "headings": [s["heading"]], "blocks": list(s["blocks"])})

    parents = []
    for p in packed:
        part, size = [], 0
        for b in p["blocks"]:
            if part and size + len(b["text"]) > PARENT_MAX_CHARS:
                parents.append({**p, "blocks": part})
                part, size = [], 0
            part.append(b)
            size += len(b["text"])
        parents.append({**p, "blocks": part})
    return parents


def _render(blocks: list[dict]) -> str:
    """Parent text with headings and [p.N] page markers so the agent can cite pages."""
    out, page, heading = [], None, None
    for b in blocks:
        if b["page"] != page:
            page = b["page"]
            out.append(f"[p.{page}]")
        if b["heading"] and b["heading"] != heading:
            heading = b["heading"]
            out.append(f"## {heading}")
        out.append(b["text"])
    return "\n\n".join(out)


def to_children(blocks: list[dict]) -> list[list[dict]]:
    """Split a parent's blocks into child groups: tables (with caption) alone, text packed."""
    children, buf = [], []
    for i, b in enumerate(blocks):
        if b["kind"] == "table":
            caption = []
            if buf and buf[-1]["kind"] == "text" and len(buf[-1]["text"]) <= CAPTION_MAX_CHARS:
                caption = [buf.pop()]
            if buf:
                children.append(buf)
            children.append(caption + [b])
            buf = []
            continue
        if buf and (_size(buf) + len(b["text"]) > CHILD_TARGET_CHARS or b["heading"] != buf[-1]["heading"]):
            children.append(buf)
            buf = []
        buf.append(b)
    if buf:
        children.append(buf)
    return children


def ingest_doc(doc: str) -> tuple[list[dict], list[dict]]:
    ticker, fy, _ = doc.split("_")
    fiscal_year = int(fy[2:])
    parents, chunks = [], []
    for pi, p in enumerate(to_parents(to_sections(to_blocks(load_pages(doc))))):
        item_no, item_title = p["item"]
        parent_id = f"{doc}#p{pi}"
        meta = {"doc": doc, "ticker": ticker, "fiscal_year": fiscal_year, "item": item_no, "item_title": item_title}
        parents.append({
            "id": parent_id, **meta,
            "headings": [h for h in p["headings"] if h],
            "page_start": p["blocks"][0]["page"], "page_end": p["blocks"][-1]["page"],
            "text": _render(p["blocks"]),
        })
        for ci, group in enumerate(to_children(p["blocks"])):
            section = group[0]["heading"] or item_title
            page = group[0]["page"]
            context = f"{ticker} FY{fiscal_year} 10-K > Item {item_no}. {item_title} > {section} (p.{page})"
            chunks.append({
                "id": f"{parent_id}.c{ci}", "parent_id": parent_id, **meta,
                "section": section, "page": page, "page_end": group[-1]["page"],
                "is_table": any(b["kind"] == "table" for b in group),
                "context": context,
                "text": "\n\n".join(b["text"] for b in group),
            })
    return parents, chunks


def main() -> None:
    all_parents, all_chunks = [], []
    for pdf in sorted(PDF_DIR.glob("*_10-K.pdf")):
        t = time.time()
        parents, chunks = ingest_doc(pdf.stem)
        all_parents += parents
        all_chunks += chunks
        print(f"{pdf.stem}: {len(parents)} parents, {len(chunks)} chunks ({time.time() - t:.1f}s)")
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    for name, rows in (("parents", all_parents), ("chunks", all_chunks)):
        with open(INDEX_DIR / f"{name}.jsonl", "w") as f:
            f.writelines(json.dumps(r) + "\n" for r in rows)
    print(f"total: {len(all_parents)} parents, {len(all_chunks)} chunks -> {INDEX_DIR}")
    embed_chunks(all_chunks)


def embed_chunks(chunks: list[dict]) -> None:
    """Embed each chunk with its context header; skipped when embeddings for these chunks exist."""
    from app.llm import embed  # needs the API key, so imported only when embedding

    path, ids_path = INDEX_DIR / "embeddings.npy", INDEX_DIR / "embedding_ids.json"
    ids = [c["id"] for c in chunks]
    if path.exists() and ids_path.exists() and json.loads(ids_path.read_text()) == ids:
        print("embeddings up to date")
        return
    t = time.time()
    vecs = embed([c["context"] + "\n\n" + c["text"] for c in chunks])
    np.save(path, vecs.astype(np.float16))
    ids_path.write_text(json.dumps(ids))
    print(f"embedded {len(ids)} chunks, dim {vecs.shape[1]} ({time.time() - t:.0f}s)")


if __name__ == "__main__":
    main()
