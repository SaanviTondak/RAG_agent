"""What the user sees of an agent result: the cited evidence and a plain-language list of steps.

Only items the answer actually cites are shown: each cited filing page (with the retrieved passages from
that page and a link that opens the PDF there) and the SQL result for each "[SQL: table]" citation.
"""

import json
import re

from app.retrieval import get_index

CITE_RE = re.compile(r"\b(AAPL|MSFT|GOOGL) FY(\d{4}) 10-K,?\s*pp?\.\s*(\d+)(?:\s*[-–]\s*(\d+))?")
SQL_CITE_RE = re.compile(r"\[SQL:\s*([^\]]+)\]", re.I)
TABLE_RE = re.compile(r"\b(?:from|join)\s+([a-z_]+)", re.I)
SNIPPETS_PER_CITATION = 3
SNIPPET_CHARS = 700


def _tool_steps(result: dict, name: str | None = None) -> list[dict]:
    return [s for s in result["trace"] if s["type"] == "tool" and (name is None or s["tool"] == name)]


def _snippets(result: dict, doc: str, first: int, last: int) -> tuple[list[str], str]:
    """Passages the agent saw on these pages: retrieved chunks first, then chunks of sections it read."""
    texts, section = [], ""
    for s in result["sources"]:
        if s["type"] == "filing" and s["doc"] == doc and first <= s["page"] <= last:
            texts.append(s["text"])
            section = section or s["section"]
    read = {s["parent_id"] for s in result["sources"] if s["type"] == "section" and s["doc"] == doc}
    if len(texts) < SNIPPETS_PER_CITATION and read:
        for c in get_index().chunks:
            if c["parent_id"] in read and first <= c["page"] <= last and c["text"] not in texts:
                texts.append(c["text"])
                section = section or c["section"]
                if len(texts) >= SNIPPETS_PER_CITATION:
                    break
    return [t[:SNIPPET_CHARS] + ("…" if len(t) > SNIPPET_CHARS else "") for t in texts[:SNIPPETS_PER_CITATION]], section


def cited_evidence(result: dict) -> list[dict]:
    answer, out, seen = result["answer"], [], set()
    for m in CITE_RE.finditer(answer):
        ticker, year, p1, p2 = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
        if (ticker, year, p1, p2) in seen:
            continue
        seen.add((ticker, year, p1, p2))
        doc = f"{ticker}_FY{year}_10-K"
        snippets, section = _snippets(result, doc, p1, p2)
        out.append({"type": "filing", "citation": f"{ticker} FY{year} 10-K, " + (f"p.{p1}" if p1 == p2 else f"pp.{p1}-{p2}"),
                    "doc": doc, "pages": [p1, p2], "url": f"/pdfs/{doc}.pdf#page={p1}", "section": section,
                    "snippets": snippets})
    cited_tables = {t.strip().lower() for m in SQL_CITE_RE.finditer(answer) for t in m.group(1).split(",")}
    sql_steps = [s for s in _tool_steps(result, "query_sql") if s["meta"].get("rows")]
    matched = [s for s in sql_steps if cited_tables & {t.lower() for t in TABLE_RE.findall(s["meta"]["sql"])}]
    for s in matched or (sql_steps if cited_tables else []):
        tables = sorted({t.lower() for t in TABLE_RE.findall(s["meta"]["sql"])})
        out.append({"type": "sql", "citation": "SQL: " + ", ".join(tables), "sql": s["meta"]["sql"],
                    "result": s["result"]})
    return out


def _args(step: dict) -> dict:
    try:
        args = json.loads(step.get("args") or "{}")
        return args if isinstance(args, dict) else {}
    except json.JSONDecodeError:
        return {}


NUDGE_LABELS = (("explanations or disclosures", "Checking the filings for the explanation"),
                ("involves figures", "Verifying the figures against the data"),
                ("percentages in your draft", "Recomputing a percentage with the calculator"))


def step_view(step: dict) -> dict | None:
    """One trace step as {"kind", "label", "detail"} for the UI and API; None for internal steps."""
    if step["type"] == "plan":
        return {"kind": "plan", "label": "Plan", "detail": "\n".join(
            f"{i}. {s['ask']}" for i, s in enumerate(step["steps"], 1))}
    if step["type"] == "nudge":
        label = next((l for k, l in NUDGE_LABELS if k in step["text"]), "Double-checking the evidence")
        return {"kind": "check", "label": label, "detail": ""}
    if step["type"] == "fallback":
        return {"kind": "check", "label": "Writing the answer from the evidence gathered so far", "detail": ""}
    if step["type"] == "edit":  # a rejected edit is internal: the answer is the draft, unchanged
        return None if step["fallback"] else {"kind": "check", "label": "Tightening the answer", "detail": ""}
    if step["type"] != "tool":
        return None
    args, meta, name = _args(step), step["meta"], step["tool"]
    if name == "search_filings":
        scope = ", ".join(x for x in (args.get("ticker"), f"FY{str(args['fiscal_year']).removeprefix('FY')} 10-K"
                                      if args.get("fiscal_year") else None) if x) or "all filings"
        cites = list(dict.fromkeys(step.get("citations", [])))
        return {"kind": "search", "label": f'Searching filings: "{args.get("query", "")}" ({scope})',
                "detail": ("Found: " + "; ".join(cites)) if cites else step["result"][:200]}
    if name == "read_section":
        parents = meta.get("parents") or []
        what = "; ".join(p["doc"].replace("_", " ").replace(" 10-K", " 10-K,") + (
            f" p.{p['page_start']}" if p["page_start"] == p["page_end"] else f" pp.{p['page_start']}-{p['page_end']}")
            for p in parents) or args.get("parent_id") or "section"
        return {"kind": "read", "label": f"Reading {what}", "detail": ""}
    if name == "query_sql":
        tables = sorted({t.lower() for t in TABLE_RE.findall(args.get("sql", ""))}) or ["database"]
        return {"kind": "sql", "label": "Querying database: " + ", ".join(tables),
                "detail": args.get("sql", "") + "\n\n" + step["result"]}
    if name == "calculate":
        names = list((args.get("expressions") or {}).keys()) if isinstance(args.get("expressions"), dict) else []
        return {"kind": "calc", "label": "Calculating" + (": " + ", ".join(names) if names else ""),
                "detail": step["result"]}
    return {"kind": "tool", "label": name, "detail": step["result"][:300]}


def steps_view(result: dict) -> list[dict]:
    return [v for v in map(step_view, result["trace"]) if v]
