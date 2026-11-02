#!/usr/bin/env python3
"""Dynamic Fact & Case Library manager with anti-footprint usage tracking.

Extracts verified claims/cases from truth-qa.md (both Draft-Born Claims and
Pack-Backed Claim Mapping tables/lists), deduplicates them into
`<project_dir>/knowledge/fact-library.json`, tracks `used_in_articles` and
`usage_count` to prevent cross-article case repetition (AI footprint), and
provides `--recommend` to surface least-used facts for new articles.

Usage:
    python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> <article-slug>
    python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> --recommend [--limit 15]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SECTION_PATTERNS = (
    re.compile(r"##\s*Draft-?[Bb]orn\s*Claims?(?:\s*Watchlist)?\s*\n(.*?)(?=\n\s*##?\s|\Z)", re.DOTALL),
    re.compile(r"##\s*Pack-?[Bb]acked\s*Claim\s*Mapping\s*\n(.*?)(?=\n\s*##?\s|\Z)", re.DOTALL),
)

HEADER_CELLS = {
    "claim",
    "draft claim",
    "draft claim family",
    "original wording",
    "source",
    "evidence",
    "status",
}


def _extract_claims_from_section(section_text: str) -> list[str]:
    claims: list[str] = []
    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("- ", "* ")):
            clean = line[2:].strip()
            if clean and "No issues" not in clean and "Draft-born" not in clean:
                claims.append(clean)
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|") if c.strip()]
            if not cells:
                continue
            if all(set(c) <= {"-", ":", " "} for c in cells):
                continue
            if len(cells) == 1:
                first = cells[0]
                if first.lower() not in HEADER_CELLS and "Draft-born" not in first:
                    claims.append(first)
                continue
            # Multi-column markdown table row: skip header row, skip rows whose first col is just a number
            first_col = cells[0].strip("`*_ ")
            if first_col.lower() in HEADER_CELLS or first_col == "#":
                continue
            candidate = cells[1].strip("` ") if first_col.isdigit() and len(cells) >= 2 else first_col
            if candidate.lower() in HEADER_CELLS or "---" in candidate:
                continue
            # Skip blocked/rejected/removed/strikethrough rows
            row_lower = line.lower()
            if (
                "| block" in row_lower
                or "| fail" in row_lower
                or "| remove" in row_lower
                or "| reject" in row_lower
                or candidate.startswith("~~")
            ):
                continue
            claims.append(candidate)
    return claims


def load_fact_library(project_dir: Path) -> list[dict[str, Any]]:
    project_dir = Path(project_dir)
    if not project_dir.is_absolute() and not project_dir.exists():
        candidate_dir = Path(__file__).resolve().parents[1] / project_dir
        if candidate_dir.exists():
            project_dir = candidate_dir
    fact_lib_path = project_dir / "knowledge" / "fact-library.json"
    if not fact_lib_path.exists():
        return []
    try:
        data = json.loads(fact_lib_path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def sync_claims(project_dir: Path, article_slug: str) -> list[dict[str, Any]]:
    project_dir = Path(project_dir)
    if not project_dir.is_absolute() and not project_dir.exists():
        candidate_dir = Path(__file__).resolve().parents[1] / project_dir
        if candidate_dir.exists():
            project_dir = candidate_dir
    article_dir = project_dir / "articles" / article_slug
    truth_qa_path = article_dir / "truth-qa.md"

    if not truth_qa_path.exists():
        print(f"No truth-qa.md found for {article_slug}")
        return []

    content = truth_qa_path.read_text(encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from workflow_status import EXPLICIT_STATUS_LINE_RE, read_qa_verdict

    verdict = read_qa_verdict(truth_qa_path)
    if (
        verdict == "BLOCK"
        or ("PASS |" in content and "| BLOCK" in content)
        or re.search(r"\b(?:TBD|TODO|PENDING)\b", content)
        or (verdict == "UNKNOWN" and EXPLICIT_STATUS_LINE_RE.search(content))
    ):
        print(f"Skipping {article_slug}: truth-qa.md is BLOCKED or an unfilled template.")
        return []

    extracted: list[str] = []
    for pattern in SECTION_PATTERNS:
        for match in pattern.finditer(content):
            block = match.group(1).strip()
            if block and "No issues" not in block:
                extracted.extend(_extract_claims_from_section(block))

    if not extracted:
        print("No draft-born claims section found.")
        return []

    knowledge_dir = project_dir / "knowledge"
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    fact_lib_path = knowledge_dir / "fact-library.json"
    facts = load_fact_library(project_dir)

    by_claim: dict[str, dict[str, Any]] = {}
    for item in facts:
        if isinstance(item, dict) and "claim" in item:
            used = list(item.get("used_in_articles") or [])
            src = item.get("source_article")
            if src and src not in used:
                used.append(src)
            item["used_in_articles"] = used
            item["usage_count"] = len(used)
            by_claim[item["claim"]] = item

    added_or_updated = 0
    for claim in extracted:
        if claim in by_claim:
            entry = by_claim[claim]
            used = entry.setdefault("used_in_articles", [])
            if article_slug not in used:
                used.append(article_slug)
                entry["usage_count"] = len(used)
                added_or_updated += 1
        else:
            entry = {
                "source_article": article_slug,
                "claim": claim,
                "status": "verified_draft_born",
                "used_in_articles": [article_slug],
                "usage_count": 1,
            }
            facts.append(entry)
            by_claim[claim] = entry
            added_or_updated += 1

    fact_lib_path.write_text(json.dumps(facts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Successfully synced {added_or_updated} claim(s) to fact-library.json (total: {len(facts)})")
    return facts


def recommend_facts(project_dir: Path, exclude_article: str | None = None, limit: int = 15) -> list[dict[str, Any]]:
    """Return verified facts ordered by lowest usage_count first (anti-footprint selection)."""
    facts = load_fact_library(Path(project_dir))
    candidates = []
    for item in facts:
        if not isinstance(item, dict) or not item.get("claim"):
            continue
        used = list(item.get("used_in_articles") or ([item["source_article"]] if item.get("source_article") else []))
        item["used_in_articles"] = used
        item["usage_count"] = len(used)
        if exclude_article and exclude_article in used:
            continue
        candidates.append(item)
    candidates.sort(key=lambda x: (x.get("usage_count", 0), x.get("claim", "")))
    return candidates[:limit]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="content-workspace/<project-slug>")
    parser.add_argument("article_slug", nargs="?", help="Article slug when syncing claims")
    parser.add_argument("--recommend", action="store_true", help="Recommend least-used facts to avoid cross-article repetition")
    parser.add_argument("--limit", type=int, default=15, help="Max facts to return in --recommend mode")
    args = parser.parse_args(argv)

    if args.recommend:
        recs = recommend_facts(args.project_dir, exclude_article=args.article_slug, limit=args.limit)
        print(json.dumps(recs, indent=2, ensure_ascii=False))
        return 0

    if not args.article_slug:
        print("Usage: python3 sync_draft_born_claims.py <project_dir> <article_slug>", file=sys.stderr)
        return 1

    sync_claims(args.project_dir, args.article_slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
