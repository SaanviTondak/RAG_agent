"""The agent's tools. Each returns (text for the model, metadata for sources/trace/guardrails)."""

import ast
import json
import operator
import re
import sqlite3

from app.config import DB_PATH, TICKERS
from app.retrieval import get_index

MAX_ROWS = 100
RESULT_CHARS = 12_000
ITEM_CHARS = 40_000

TICKER_ALIASES = {"GOOG": "GOOGL", "GOOGLE": "GOOGL", "ALPHABET": "GOOGL", "APPLE": "AAPL", "MICROSOFT": "MSFT"}


def _fmt(v) -> str:
    """Large numbers get thousands separators so the model doesn't miscount zeros; years stay as-is."""
    if isinstance(v, bool) or v is None:
        return str(v)
    if isinstance(v, int):
        return f"{v:,}" if abs(v) >= 100_000 else str(v)
    if isinstance(v, float):
        return f"{v:,.2f}" if abs(v) >= 100_000 else f"{v:.4f}".rstrip("0").rstrip(".")
    return str(v)


def _ticker(t: str | None) -> str | None:
    if not t:
        return None
    t = t.strip().upper()
    t = TICKER_ALIASES.get(t, t)
    if t not in TICKERS:
        raise ValueError(f"unknown ticker {t!r}; use one of {', '.join(TICKERS)}")
    return t


def _year(y) -> int | None:
    return int(str(y).upper().removeprefix("FY")) if y not in (None, "") else None


def query_sql(sql: str) -> tuple[str, dict]:
    meta = {"type": "sql", "sql": sql}
    stmt = sql.strip().rstrip(";").strip()
    if not re.match(r"^(select|with)\b", stmt, re.I) or ";" in stmt:
        return "Error: only a single read-only SELECT (or WITH ... SELECT) statement is allowed.", meta
    try:
        con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
        try:
            cur = con.execute(stmt)
            cols = [d[0] for d in cur.description]
            rows = cur.fetchmany(MAX_ROWS + 1)
        finally:
            con.close()
    except sqlite3.Error as e:
        return f"SQL error: {e}", meta
    meta["rows"] = len(rows[:MAX_ROWS])
    if not rows:
        return "0 rows. Check table/column names and exact string values (they are case-sensitive).", meta
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(_fmt(v) for v in r) + " |" for r in rows[:MAX_ROWS]]
    if len(rows) > MAX_ROWS:
        lines.append(f"(truncated to {MAX_ROWS} rows)")
    return "\n".join(lines), meta


def _cite(c: dict) -> str:
    return f"{c['ticker']} FY{c['fiscal_year']} 10-K, p.{c['page']}"


def search_filings(query: str, ticker: str | None = None, fiscal_year=None) -> tuple[str, dict]:
    hits = get_index().search(query, ticker=_ticker(ticker), fiscal_year=_year(fiscal_year))
    meta = {"type": "search", "query": query, "hits": [
        {"chunk_id": h["id"], "parent_id": h["parent_id"], "doc": h["doc"], "page": h["page"],
         "citation": _cite(h), "section": h["section"], "is_table": h["is_table"], "score": h["score"],
         "text": h["text"]} for h in hits]}
    if not hits:
        return "No matching passages (check ticker / fiscal_year).", meta
    blocks = [f"[{n}] {_cite(h)} | Item {h['item']}. {h['item_title']} > {h['section']} | parent_id={h['parent_id']}\n{h['text']}"
              for n, h in enumerate(hits, 1)]
    return "\n\n---\n\n".join(blocks)[:RESULT_CHARS], meta


def read_section(parent_id: str | None = None, ticker: str | None = None, fiscal_year=None,
                 item: str | None = None) -> tuple[str, dict]:
    index = get_index()
    if parent_id:
        p = index.parents.get(parent_id)
        if p is None:
            return f"Unknown parent_id {parent_id!r}.", {"type": "section", "parents": []}
        header = f"{p['ticker']} FY{p['fiscal_year']} 10-K | Item {p['item']}. {p['item_title']} | pages {p['page_start']}-{p['page_end']}"
        return f"{header}\n\n{p['text']}"[:RESULT_CHARS], {"type": "section", "parents": [_parent_meta(p)]}

    t, y, it = _ticker(ticker), _year(fiscal_year), (item or "").strip().upper().removeprefix("ITEM").strip(" .")
    if not (t and y and it):
        return "Provide either parent_id, or ticker + fiscal_year + item (e.g. item='1A').", {"type": "section", "parents": []}
    parents = [p for p in index.parents.values() if p["ticker"] == t and p["fiscal_year"] == y and p["item"] == it]
    if not parents:
        return f"No Item {it} found in the {t} FY{y} 10-K.", {"type": "section", "parents": []}
    out, used, skipped, size = [], [], [], 0
    for p in parents:
        if size + len(p["text"]) > ITEM_CHARS:
            skipped.append(p)
            continue
        out.append(p["text"])
        used.append(p)
        size += len(p["text"])
    header = f"{t} FY{y} 10-K | Item {it}. {parents[0]['item_title']} | {len(used)} of {len(parents)} sections"
    text = header + "\n\n" + "\n\n".join(out)
    if skipped:
        text += "\n\n[Not included because of length; read individually with parent_id if needed:]\n" + "\n".join(
            f"- {p['id']} (p.{p['page_start']}): {'; '.join(p['headings'][:2])[:150]}" for p in skipped)
    return text, {"type": "section", "parents": [_parent_meta(p) for p in used]}


def _parent_meta(p: dict) -> dict:
    return {"parent_id": p["id"], "doc": p["doc"], "page_start": p["page_start"], "page_end": p["page_end"],
            "citation": f"{p['ticker']} FY{p['fiscal_year']} 10-K, pp.{p['page_start']}-{p['page_end']}",
            "has_table": "\n|" in p["text"]}


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}
_FUNCS = {"round": round, "abs": abs, "min": min, "max": max}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCS and not node.keywords:
        return _FUNCS[node.func.id](*[_eval(a) for a in node.args])
    raise ValueError("only numbers, + - * / **, parentheses, round/abs/min/max are allowed")


def calculate(expressions: dict) -> tuple[str, dict]:
    results, lines = {}, []
    for name, expr in expressions.items():
        clean = re.sub(r"(?<=\d),(?=\d{3}\b)", "", str(expr))  # 281,724 -> 281724
        try:
            value = _eval(ast.parse(clean, mode="eval"))
            results[name] = value
            lines.append(f"{name} = {_fmt(float(value))}")
        except Exception as e:  # noqa: BLE001 - any failure is reported back to the model
            lines.append(f"{name}: error ({e})")
    return "\n".join(lines), {"type": "calc", "expressions": expressions, "results": results}


TOOLS = {"query_sql": query_sql, "search_filings": search_filings, "read_section": read_section, "calculate": calculate}


def run_tool(name: str, raw_args: str) -> tuple[str, dict]:
    """Parse arguments and run a tool; every failure becomes text the model can react to."""
    if name not in TOOLS:
        return f"Error: unknown tool {name!r}.", {"type": "error"}
    try:
        args = json.loads(raw_args or "{}")
        return TOOLS[name](**args)
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        return f"Error calling {name}: {e}", {"type": "error"}


TOOL_SCHEMAS = [
    {"type": "function", "function": {
        "name": "query_sql",
        "description": "Run one read-only SQLite SELECT against the financials database (schema in the system prompt). "
                       "Returns a table; large numbers are shown with thousands separators. Use SQL for lookups, "
                       "filtering, aggregation and arithmetic on database figures.",
        "parameters": {"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]}}},
    {"type": "function", "function": {
        "name": "search_filings",
        "description": "Hybrid keyword + semantic search over the 10-K filings. Returns the top passages with "
                       "citation (ticker, fiscal year, page), section, and parent_id. Narrow with ticker and "
                       "fiscal_year (= which filing; the FY2025 10-K also discusses FY2024 comparisons).",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "What to look for, in natural language or key terms."},
            "ticker": {"type": "string", "enum": list(TICKERS)},
            "fiscal_year": {"type": "integer", "enum": [2024, 2025]}},
            "required": ["query"]}}},
    {"type": "function", "function": {
        "name": "read_section",
        "description": "Read a full filing section. Pass parent_id (from search results) to read the whole "
                       "subsection around a hit, or ticker + fiscal_year + item (e.g. '1A' Risk Factors, '7' MD&A) "
                       "to read an entire Item (long; capped at ~10K tokens).",
        "parameters": {"type": "object", "properties": {
            "parent_id": {"type": "string"},
            "ticker": {"type": "string", "enum": list(TICKERS)},
            "fiscal_year": {"type": "integer", "enum": [2024, 2025]},
            "item": {"type": "string", "description": "10-K item number, e.g. '1', '1A', '7', '8'."}}}}},
    {"type": "function", "function": {
        "name": "calculate",
        "description": "Evaluate named arithmetic expressions exactly (growth rates, shares, ratios, differences). "
                       "Example: {\"msft_growth_pct\": \"(281724 - 245122) / 245122 * 100\"}.",
        "parameters": {"type": "object", "properties": {
            "expressions": {"type": "object", "additionalProperties": {"type": "string"},
                            "description": "Map of result name -> expression."}},
            "required": ["expressions"]}}},
]
