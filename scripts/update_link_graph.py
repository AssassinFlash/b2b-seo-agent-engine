#!/usr/bin/env python3
"""Bi-directional Site Link Graph manager (new->old outbound + old->new retro-links).

Scans an article's enriched-draft.md (or draft.md) and topic-card.md, records its
outbound internal links in `<project_dir>/knowledge/site-link-graph.json`, and
computes an Inbound Retro-Link Checklist (《旧文回链清单》): existing published/drafted
articles in the project that share topic keywords/entities with this article but do
not yet link to it.

Usage:
    python3 scripts/update_link_graph.py content-workspace/<project-slug> <article-slug>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


MARKDOWN_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^),\s"]+),?(?:\s+"([^"]*)")?\)')
HTML_LINK_RE = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
H1_RE = re.compile(r"(?m)^#\s+(.+)$")
STOPWORDS = {
    "the", "and", "for", "with", "without", "how", "what", "why", "when", "which",
    "can", "you", "your", "are", "from", "that", "this", "into", "guide", "best",
}


def _tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]{3,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def _extract_article_meta(article_dir: Path, slug: str) -> dict[str, Any]:
    body_path = article_dir / "enriched-draft.md"
    if not body_path.exists():
        body_path = article_dir / "draft.md"
    raw_body = body_path.read_text(encoding="utf-8", errors="replace") if body_path.exists() else ""
    # Strip ## Draft Control Metadata, <style> blocks, and fenced ```...``` code blocks before extracting H1 and outbound links
    body = re.sub(r"(?ms)^##\s+Draft Control Metadata\b.*$", "", raw_body)
    body = re.sub(r"(<style\b[^>]*>.*?</style>|```.*?```)", "", body, flags=re.DOTALL | re.IGNORECASE)

    topic_path = article_dir / "topic-card.md"
    topic_text = topic_path.read_text(encoding="utf-8", errors="replace") if topic_path.exists() else ""

    h1_match = H1_RE.search(body) or H1_RE.search(topic_text)
    title = h1_match.group(1).strip() if h1_match else slug.replace("-", " ").title()

    outbound: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for match in MARKDOWN_LINK_RE.finditer(body):
        anchor, url, title_attr = match.group(1).strip(), match.group(2).strip(), (match.group(3) or "").strip()
        if url.startswith(("mailto:", "tel:", "#")):
            continue
        if url not in seen_urls:
            seen_urls.add(url)
            outbound.append({"anchor": anchor, "url": url, "title": title_attr})

    for match in HTML_LINK_RE.finditer(body):
        url = match.group(1).strip()
        anchor = re.sub(r"<[^>]+>", "", match.group(2)).strip()
        if url.startswith(("mailto:", "tel:", "#")):
            continue
        if url not in seen_urls:
            seen_urls.add(url)
            outbound.append({"anchor": anchor, "url": url, "title": ""})

    tokens = sorted(_tokenize(f"{slug.replace('-', ' ')} {title} {topic_text[:1000]}"))
    return {
        "slug": slug,
        "title": title,
        "url_path": f"/{slug}/",
        "keywords": tokens[:25],
        "outbound_links": outbound,
    }


def update_link_graph(project_dir: Path, article_slug: str) -> dict[str, Any]:
    project_dir = Path(project_dir)
    if not project_dir.is_absolute() and not project_dir.exists():
        candidate_dir = Path(__file__).resolve().parents[1] / project_dir
        if candidate_dir.exists():
            project_dir = candidate_dir
    articles_root = project_dir / "articles"
    target_dir = articles_root / article_slug
    if not target_dir.exists():
        raise FileNotFoundError(f"Article directory not found: {target_dir}")

    knowledge_dir = project_dir / "knowledge"
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    graph_path = knowledge_dir / "site-link-graph.json"

    graph: dict[str, Any] = {"articles": {}, "retro_link_recommendations": {}}
    if graph_path.exists():
        try:
            loaded = json.loads(graph_path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                graph.update(loaded)
        except json.JSONDecodeError:
            pass

    articles_map: dict[str, Any] = graph.setdefault("articles", {})

    # Refresh all articles present in the workspace so cross-article links are up to date
    if articles_root.exists():
        for subdir in sorted(articles_root.iterdir()):
            if subdir.is_dir() and not subdir.name.startswith("."):
                articles_map[subdir.name] = _extract_article_meta(subdir, subdir.name)

    target_meta = articles_map[article_slug]
    target_tokens = set(target_meta.get("keywords", []))
    target_slug_re = re.compile(
        rf"(?:^|/){re.escape(article_slug.lower())}(?:/|$|[?#])"
    )

    retro_recommendations: list[dict[str, Any]] = []
    for other_slug, other_meta in articles_map.items():
        if other_slug == article_slug:
            continue
        already_links = any(
            bool(target_slug_re.search(link.get("url", "").lower()))
            for link in other_meta.get("outbound_links", [])
        )
        if already_links:
            continue
        overlap = sorted(target_tokens & set(other_meta.get("keywords", [])))
        retro_recommendations.append(
            {
                "from_article": other_slug,
                "from_title": other_meta.get("title", other_slug),
                "to_article": article_slug,
                "to_url": target_meta.get("url_path", f"/{article_slug}/"),
                "shared_topics": overlap[:8],
                "suggested_anchor": target_meta.get("title", article_slug),
            }
        )

    retro_recommendations.sort(key=lambda r: len(r["shared_topics"]), reverse=True)
    graph.setdefault("retro_link_recommendations", {})[article_slug] = retro_recommendations

    graph_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "article": article_slug,
        "outbound_count": len(target_meta.get("outbound_links", [])),
        "retro_link_recommendations": retro_recommendations,
        "graph_path": str(graph_path),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="content-workspace/<project-slug>")
    parser.add_argument("article_slug", help="Target article slug")
    args = parser.parse_args(argv)

    result = update_link_graph(args.project_dir, args.article_slug)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
