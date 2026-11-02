#!/usr/bin/env python3
"""Assemble the single-file copy-paste-ready article body, host-theme preview, and exact keyword counts.

Solves 7 real-world combat failures:
1. Strips internal `## Draft Control Metadata` so internal QA vectors never leak into publish copy.
2. Strips leading `# H1` title line (and optional duplicate hero cover image) in `publish-ready-body.md`
   so pasting into a host template like `#md-blog-single` (which already renders `<h1 class="md-blog-single-hero-title">`
   and `.reader-cover`) never produces duplicate H1s or stacked hero images.
3. Inlines Scoped HTML5 Snippets (`html-visuals/<id>.html`) while refusing full-page HTML (`<!DOCTYPE>`, `<html>`,
   `<body>`, `cdn.tailwindcss.com`) or wide >2-column grids that overflow a `68ch` reading column.
4. Verifies that `resources.md` and `faq.md` modules have been merged into `enriched-draft.md` (and supports
   `<!-- resource: ... -->` / `<!-- faq: ... -->` markers), warning if unmerged modules remain.
5. Detects `draft.md` > `enriched-draft.md` mtime drift and scans customer-facing text against `forbiddenTerms`
   from `project-profile.json` (e.g. forbidding `product/products/order/cart` when `pattern/inquiry` is mandated).
6. Computes exact mathematical keyword counts across H1, H2, and body paragraphs for `keyword-record.csv`.
7. Generates `preview-in-host-theme.html` replicating `#md-blog-single` (`68ch` prose measure, `--md-bg: #1a1a1a`,
   `--md-gold: #c9a962`, `.linker-article-check`, `.linker-article-comparison`) for instant real-Chrome inspection.

Usage:
    python3 scripts/assemble_publish_draft.py content-workspace/<project-slug> <article-slug>
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from pathlib import Path


FORBIDDEN_FULLPAGE_HTML_RE = re.compile(
    r"(?:<!DOCTYPE\s+html|<html\b|<head\b|<body\b|<link\b|<iframe\b|<object\b|<embed\b|<base\b|<meta\b|cdn\.tailwindcss\.com|fonts\.googleapis\.com|fonts\.gstatic\.com)",
    re.IGNORECASE,
)
FORBIDDEN_INLINE_JS_RE = re.compile(
    r"(?:<script\b|\bon(?:click|input|change|submit|keyup|keydown|mouseover|mouseenter|mouseleave|focus|blur|load|error)\s*=|(?:href|src|action)\s*=\s*[\"']?\s*javascript:)",
    re.IGNORECASE,
)
FORBIDDEN_CSS_IMPORT_OR_EXTERNAL_URL_RE = re.compile(
    r"(?:@import\b|url\(\s*[\"']?\s*https?://)",
    re.IGNORECASE,
)
CONTROL_METADATA_RE = re.compile(
    r"\n+#{1,3}\s+Draft Control Metadata\b.*?\Z",
    re.DOTALL | re.IGNORECASE,
)
HTML_MARKER_RE = re.compile(
    r"<!--\s*(?:html-visual|visual)\s*:\s*([a-zA-Z0-9_-]+)(?:[ \t]+(?:(?!-->).)*?)?\s*-->"
)
CITE_SLOT_RE = re.compile(
    r"\{\{CITE:\s*([^|}]+?)(?:\s*\|\s*([^}]+?))?\}\}"
)
RELATED_BLOCKQUOTE_RE = re.compile(r"^>\s*###\s*→\s*Related:", re.MULTILINE)
LEADING_FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n.*?\n---[ \t]*\n+", re.DOTALL)
LEADING_H1_RE = re.compile(r"\A\s*#\s+([^\n]+)\n+(?:\*Enriched draft[^\n]*\*\n+(?:---\n+)?)?", re.MULTILINE)


def _check_css_selectors_scoped(css_text: str) -> list[str]:
    """Ensure every selector (including comma-separated selectors) inside <style> is scoped to .b2b-mod- / .linker-article-."""
    unscoped: list[str] = []
    # Strip CSS comments
    cleaned = re.sub(r"/\*.*?\*/", "", css_text, flags=re.DOTALL)
    # Remove @keyframes blocks entirely so keyframe stops (from/to/0%/100%) are not treated as selectors
    cleaned = re.sub(r"@(?:-webkit-)?keyframes\s+[A-Za-z0-9_-]+\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", cleaned, flags=re.DOTALL)
    # Unwrap @media / @supports / @container headers, leaving inner rules
    cleaned = re.sub(r"@(?:media|supports|container)[^{]+\{", "", cleaned, flags=re.IGNORECASE)
    for match in re.finditer(r"([^{}@]+)\{[^{}]*\}", cleaned):
        selector_group = match.group(1).strip()
        if not selector_group:
            continue
        for sel in selector_group.split(","):
            s = sel.strip()
            if not s or s.startswith("@") or re.fullmatch(r"(?:from|to|\d+%)", s, re.IGNORECASE):
                continue
            if not (
                s.startswith(".b2b-mod-")
                or s.startswith(".linker-article-")
                or ".b2b-mod-" in s
                or ".linker-article-" in s
            ):
                unscoped.append(s)
    return unscoped


def _check_balanced_tags(html_text: str) -> list[str]:
    """Verify that container tags (div, details, summary, style, table, ul, ol) are balanced and properly closed."""
    errs: list[str] = []
    cleaned = re.sub(r"<!--.*?-->", "", html_text, flags=re.DOTALL)
    cleaned = re.sub(r"<style\b[^>]*>.*?</style>", "<style></style>", cleaned, flags=re.DOTALL | re.IGNORECASE)
    for tag in ("div", "details", "summary", "style", "table", "ul", "ol"):
        opens = len(re.findall(rf"<{tag}\b[^>]*>", cleaned, flags=re.IGNORECASE))
        closes = len(re.findall(rf"</{tag}\s*>", cleaned, flags=re.IGNORECASE))
        if opens != closes:
            errs.append(f"unbalanced <{tag}> tags ({opens} opening vs {closes} closing)")
    return errs


def _nh3_verify_no_executable_html(html_text: str) -> list[str]:
    """Use Cloudflare's Rust-backed `nh3` (Ammonia) HTML parser to detect hidden event attributes, <script>,<iframe>,<object>, or javascript:/data:text/html URIs."""
    issues: list[str] = []
    try:
        import nh3  # type: ignore

        # Strip <style>...</style> before nh3 check since scoped <style> is validated separately by _check_css_selectors_scoped
        without_style = re.sub(r"<style\b[^>]*>.*?</style>", "", html_text, flags=re.DOTALL | re.IGNORECASE)
        allowed_tags = {
            "div", "span", "p", "a", "ul", "ol", "li", "dl", "dt", "dd",
            "table", "thead", "tbody", "tfoot", "tr", "th", "td", "caption", "colgroup", "col",
            "details", "summary", "figure", "figcaption", "Picture", "picture", "source", "img",
            "svg", "path", "rect", "circle", "line", "polyline", "polygon", "g", "text", "defs", "linearGradient", "stop",
            "h2", "h3", "h4", "h5", "h6", "strong", "b", "em", "i", "code", "pre", "blockquote",
            "sup", "sub", "small", "mark", "del", "ins", "s", "u", "hr", "br", "abbr", "cite", "time", "kbd",
            "input", "label", "button", "meter", "progress",
        }
        # Compare tags against nh3's Rust HTML5 tokenizer by cleaning with dangerous tags stripped
        sanitized = nh3.clean(
            without_style,
            tags=allowed_tags,
            clean_content_tags={"script", "iframe", "object", "embed", "applet"},
            url_schemes={"http", "https", "mailto", "tel", "data"},
        )
        if "<script" in without_style.lower() and "<script" not in sanitized.lower():
            issues.append("nh3 AST parser detected <script> element")
        if re.search(r"\bon[a-z]+\s*=", without_style, re.IGNORECASE) and not re.search(r"\bon[a-z]+\s*=", sanitized, re.IGNORECASE):
            issues.append("nh3 AST parser detected inline DOM event handler attribute (on*=)")
        if re.search(r"(?:href|src|action)\s*=\s*[\"']?\s*(?:javascript|vbscript):", without_style, re.IGNORECASE):
            issues.append("nh3 AST parser detected executable javascript:/vbscript: URI scheme")
    except ImportError:
        pass
    return issues


def validate_scoped_html_snippet(html_text: str, source_name: str = "") -> list[str]:
    """Verify an HTML snippet is safe to inline into WordPress / arch-dark-gold / 68ch reader columns under strict CSP."""
    errors: list[str] = []
    label = source_name or "HTML snippet"
    if FORBIDDEN_FULLPAGE_HTML_RE.search(html_text):
        errors.append(
            f"{label} contains full-page tags or external font/CDN links (<!DOCTYPE>, <html>, <head>, <body>, cdn.tailwindcss.com, fonts.googleapis.com) "
            "which violate CSP or corrupt host page styles. Use a scoped <div class=\"b2b-mod-...\"> container with self-contained styles."
        )
    if FORBIDDEN_INLINE_JS_RE.search(html_text) or _nh3_verify_no_executable_html(html_text):
        errors.append(
            f"{label} contains <script>, inline event handlers (onclick/oninput...), or javascript: URIs, "
            "which are blocked by the host Content-Security-Policy (`script-src 'self'`). Use Pure CSS State Machines (`<details>` or `<input type=\"radio\"> + :checked`)."
        )
    for tag_err in _check_balanced_tags(html_text):
        errors.append(f"{label} has {tag_err} — unclosed tags will swallow the rest of the WordPress page DOM.")

    if FORBIDDEN_CSS_IMPORT_OR_EXTERNAL_URL_RE.search(html_text):
        errors.append(
            f"{label} contains @import or external url(http...), which violates host CSP (`style-src`/`font-src`/`img-src 'self'`)."
        )
    if re.search(r"<style\b[^>]*>(.*?)</style>", html_text, re.DOTALL | re.IGNORECASE):
        for match in re.finditer(r"<style\b[^>]*>(.*?)</style>", html_text, re.DOTALL | re.IGNORECASE):
            css = match.group(1)
            unscoped = _check_css_selectors_scoped(css)
            if unscoped:
                errors.append(
                    f"{label} <style> block defines unscoped global selectors ({', '.join(unscoped[:4])}). "
                    "Prefix EVERY comma-separated CSS selector with `.b2b-mod-` or use inline styles."
                )
    has_wide_grid = bool(re.search(r"grid-template-columns\s*:\s*repeat\(\s*[3-9]\s*,", html_text, re.IGNORECASE))
    if not has_wide_grid:
        for gm in re.finditer(r"grid-template-columns\s*:\s*([^;}\"']+)", html_text, re.IGNORECASE):
            val = gm.group(1).strip()
            if "repeat(" not in val.lower() and "minmax(" not in val.lower():
                tracks = [t for t in val.split() if t and t != "/"]
                if len(tracks) >= 3:
                    has_wide_grid = True
                    break
    if has_wide_grid:
        errors.append(
            f"{label} hardcodes 3+ columns (`repeat(3+, ...)` or `1fr 1fr 1fr`), which overflows a 68ch reader column. "
            "Use at most 2 columns (`repeat(auto-fit, minmax(220px, 1fr))`) inside 68ch prose."
        )
    return errors


def strip_control_metadata(markdown_text: str) -> str:
    """Remove ## Draft Control Metadata from the end of draft/enriched-draft."""
    cleaned = CONTROL_METADATA_RE.sub("", markdown_text)
    return cleaned.rstrip() + "\n"


def compact_html_block_for_wpautop(html_text: str) -> str:
    """Remove internal blank lines inside an HTML block so CommonMark Type-6 / arch-dark-gold / wpautop never split it or inject <p> tags."""
    lines = [line.rstrip() for line in html_text.strip().splitlines() if line.strip() != ""]
    return "\n".join(lines)


def extract_balanced_b2b_modules(text: str) -> list[tuple[int, int, str]]:
    """Find top-level <div class="b2b-mod-... / linker-article-...">...</div> and <details>...</details> blocks with balanced nested tags."""
    results: list[tuple[int, int, str]] = []
    # Mask comments and <style> contents with equal-length spaces so inner text never confuses tag-depth counting
    masked = re.sub(
        r"<!--.*?-->|<style\b[^>]*>.*?</style>",
        lambda m: " " * len(m.group(0)),
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    start_re = re.compile(
        r"<(div)\s+[^>]*class=[\"'][^\"']*(?:b2b-mod-|linker-article-)[^\"']*[\"'][^>]*>|<(details)\b[^>]*>",
        re.IGNORECASE,
    )
    pos = 0
    n = len(text)
    while pos < n:
        m = start_re.search(masked, pos)
        if not m:
            break
        tag_name = (m.group(1) or m.group(2)).lower()
        start_idx = m.start()
        tag_re = re.compile(rf"<(/?){tag_name}\b[^>]*>", re.IGNORECASE)
        depth = 0
        end_idx = len(text)
        for tm in tag_re.finditer(masked, start_idx):
            is_close = tm.group(1) == "/"
            depth += -1 if is_close else 1
            if depth == 0:
                end_idx = tm.end()
                break
        results.append((start_idx, end_idx, text[start_idx:end_idx]))
        pos = end_idx
    return results


def compact_inline_b2b_modules_in_markdown(markdown_text: str) -> str:
    """Ensure any balanced <div class="b2b-mod-...">...</div> or <details>...</details> block has zero internal blank lines."""
    spans = extract_balanced_b2b_modules(markdown_text)
    if not spans:
        return markdown_text
    out = []
    last = 0
    for s, e, block in spans:
        out.append(markdown_text[last:s])
        out.append(compact_html_block_for_wpautop(block))
        last = e
    out.append(markdown_text[last:])
    return "".join(out)


def extract_and_strip_leading_h1(markdown_text: str) -> tuple[str, str]:
    """Strip optional YAML frontmatter and return (extracted_h1, body_without_leading_h1) so host templates don't double-render H1."""
    without_fm = LEADING_FRONTMATTER_RE.sub("", markdown_text)
    match = LEADING_H1_RE.match(without_fm)
    if not match:
        return "", without_fm
    raw_h1 = match.group(1).strip()
    h1_title = re.sub(r"^(?:Final\s+)?(?:Enriched\s+Draft|Draft)\s*[—–:\-]\s*", "", raw_h1, flags=re.IGNORECASE).strip()
    rest = without_fm[match.end():].lstrip()
    return h1_title, rest + ("\n" if not rest.endswith("\n") else "")


def extract_citation_slots(markdown_text: str) -> list[dict[str, str]]:
    """Find all {{CITE: claim | query}} placeholders with their current H2 section."""
    slots: list[dict[str, str]] = []
    current_h2 = "Opening / Above-the-Fold"
    for line in markdown_text.splitlines():
        h2_match = re.match(r"^##\s+(.+)$", line.strip())
        if h2_match:
            current_h2 = h2_match.group(1).strip()
        for m in CITE_SLOT_RE.finditer(line):
            claim = m.group(1).strip()
            query = (m.group(2) or claim).strip()
            slots.append(
                {
                    "section": current_h2,
                    "claim": claim,
                    "query": query,
                    "marker": m.group(0),
                }
            )
    return slots


def audit_structural_fatigue(markdown_text: str) -> list[str]:
    """Detect repetitive section templates (e.g. >2 identical '> ### → Related:' blocks)."""
    warnings: list[str] = []
    related_matches = RELATED_BLOCKQUOTE_RE.findall(markdown_text)
    if len(related_matches) > 2:
        warnings.append(
            f"Found {len(related_matches)} identical '> ### → Related:' blockquote callouts. "
            "Vary internal link containers across sections (inline anchors, Bento cards, split cards, or tab footers) to avoid template fatigue."
        )
    sections = re.split(r"(?m)^##\s+", markdown_text)[1:]
    prev_sig = None
    streak = 1
    for idx, sec in enumerate(sections, start=1):
        has_table = "| ---" in sec or "|---" in sec or "|:--" in sec
        has_html = "<div" in sec or "<details" in sec
        has_list = bool(re.search(r"(?m)^\s*[-*]\s+", sec))
        sig = (has_table, has_html, has_list)
        if sig == prev_sig and sig == (False, False, True):
            streak += 1
            if streak >= 3:
                warnings.append(
                    f"H2 section #{idx} is the {streak}th consecutive prose+bullet-list section without a table or scoped HTML module."
                )
        else:
            streak = 1
        prev_sig = sig
    # Check Markdown table column counts against #md-blog-single `table-layout: fixed` 320px/390px limit
    for line in markdown_text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|") and "---" in s:
            cols = [c.strip() for c in s.strip("|").split("|")]
            if len(cols) > 4:
                warnings.append(
                    f"Markdown table with {len(cols)} columns detected; under `#md-blog-single` `table-layout: fixed`, "
                    "5+ columns crush text on 320px/390px mobile screens. Keep Markdown tables <=4 columns or use a 2-column `.b2b-mod-*` / `.linker-article-comparison` card."
                )
                break
    return warnings


def check_unmerged_resources_and_faq(article_dir: Path, body: str) -> list[str]:
    """Warn if faq.md or resources.md exists with real content (>20 chars) but none of its accordions/cards appear in body."""
    warnings: list[str] = []
    faq_path = article_dir / "faq.md"
    if faq_path.exists() and len(faq_path.read_text(encoding="utf-8", errors="replace").strip()) > 20:
        faq_has_body_presence = (
            "[su_accordion]" in body
            or "<details" in body
            or "b2b-mod-faq" in body
            or "Quick Answers" in body
            or "FAQ" in body
        )
        if not faq_has_body_presence:
            warnings.append("faq.md exists but no FAQ accordion (<details> / [su_accordion]) was found in enriched-draft.md.")
    res_path = article_dir / "resources.md"
    if res_path.exists() and len(res_path.read_text(encoding="utf-8", errors="replace").strip()) > 20:
        res_has_body_presence = (
            "b2b-mod-" in body
            or "linker-article-" in body
            or "[su_box" in body
            or "Related:" in body
        )
        if not res_has_body_presence:
            warnings.append("resources.md exists but no resource/routing cards were found in enriched-draft.md.")
    return warnings


def scan_forbidden_terms(body: str, project_dir: Path) -> list[str]:
    """Scan customer-facing text (excluding URLs and HTML attributes) against forbiddenTerms in project-profile.json."""
    profile_json = project_dir / "project-profile.json"
    if not profile_json.exists():
        return []
    try:
        data = json.loads(profile_json.read_text(encoding="utf-8"))
    except Exception:
        return []
    forbidden = data.get("forbiddenTerms") or []
    preferred = data.get("preferredTerms") or {}
    if not forbidden:
        return []

    # Mask multi-line <style>...</style> and fenced ```...``` blocks while preserving exact line numbers
    masked_body = re.sub(
        r"(<style\b[^>]*>.*?</style>|```.*?```)",
        lambda m: re.sub(r"[^\n]", " ", m.group(0)),
        body,
        flags=re.DOTALL | re.IGNORECASE,
    )

    violations: list[str] = []
    for term in forbidden:
        term_re = re.compile(rf"\b{re.escape(term)}\b", flags=re.IGNORECASE)
        hit_lines: list[str] = []
        total_hits = 0
        for line_no, raw_line in enumerate(masked_body.splitlines(), start=1):
            # Strip URLs, markdown link targets, and HTML tags/attributes before scanning visible words
            clean_line = re.sub(r"https?://[^\s\)\"'>]+", "", raw_line)
            clean_line = re.sub(r"\(/[a-zA-Z0-9_./?=&%#-]+(?:\s+\"[^\"]*\")?\)", "()", clean_line)
            clean_line = re.sub(r"<[^>]+>", " ", clean_line)
            matches = term_re.findall(clean_line)
            if matches:
                total_hits += len(matches)
                if len(hit_lines) < 3:
                    snippet = clean_line.strip()[:80]
                    hit_lines.append(f"L{line_no}: \"{snippet}\"")
        if total_hits > 0:
            replacement = preferred.get(term.lower(), "the canonical glossary term")
            loc_str = "; ".join(hit_lines)
            violations.append(
                f"Forbidden glossary term '{term}' appears {total_hits} time(s) in customer-facing text ({loc_str}); use '{replacement}' instead."
            )

    # Also block retired legacy URL prefixes (/pages/... or /products/...) when canonicalDomain is archmetal-screens.example.com or 'product' is forbidden
    canonical_dom = str(data.get("canonicalDomain") or data.get("domain") or "").lower()
    if "archmetal-screens.example.com" in canonical_dom or "product" in [str(t).lower() for t in forbidden]:
        legacy_url_re = re.compile(r"(?:https?://archmetal-screens\.example\.com)?/(pages|products)/([a-zA-Z0-9_-]+)", re.IGNORECASE)
        for line_no, raw_line in enumerate(masked_body.splitlines(), start=1):
            for lm in legacy_url_re.finditer(raw_line):
                prefix_used = lm.group(1).lower()
                slug_part = lm.group(2)
                fix_route = f"/{slug_part}/" if prefix_used == "pages" else f"/pattern/{slug_part}/"
                violations.append(
                    f"Legacy retired URL path '/{prefix_used}/{slug_part}' on L{line_no}; use canonical '{fix_route}' instead."
                )
    return violations


def scan_external_image_hotlinks(body: str, project_dir: Path) -> list[str]:
    """Detect external HTTP(S) image URLs that do not match the project's canonicalDomain (violating CSP img-src 'self')."""
    profile_json = project_dir / "project-profile.json"
    canonical_host = ""
    if profile_json.exists():
        try:
            data = json.loads(profile_json.read_text(encoding="utf-8"))
            raw_dom = str(data.get("canonicalDomain") or data.get("domain") or "").strip().lower()
            canonical_host = re.sub(r"^https?://", "", raw_dom).split("/")[0]
        except Exception:
            pass
    if not canonical_host:
        return []

    no_code = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    img_urls: list[str] = []
    for m in re.finditer(r"!\[[^\]]*\]\((https?://[^)\s\"]+)", no_code):
        img_urls.append(m.group(1))
    for m in re.finditer(r"<img\b[^>]*\bsrc=[\"'](https?://[^\"']+)", no_code, flags=re.IGNORECASE):
        img_urls.append(m.group(1))
    for m in re.finditer(r"url\(\s*[\"']?(https?://[^)\"'\s]+)[\"']?\s*\)", no_code, flags=re.IGNORECASE):
        img_urls.append(m.group(1))

    external: list[str] = []
    for u in dict.fromkeys(img_urls):
        host = re.sub(r"^https?://", "", u.lower()).split("/")[0]
        if host and host != canonical_host and not host.endswith("." + canonical_host):
            external.append(
                f"External image hotlink '{u}' (host '{host}' != '{canonical_host}') will be blocked by CSP `img-src 'self' data:`; upload to local media library first."
            )
    return external


def compute_exact_keyword_counts(h1_title: str, body: str, article_dir: Path) -> list[dict[str, str]]:
    """Compute 100% mathematically accurate H1, H2, and visible body prose occurrence counts for keyword-record.csv."""
    csv_path = article_dir / "keyword-record.csv"
    if not csv_path.exists():
        return []
    # Strip <style>, fenced code blocks, headings, URLs, and HTML tags so body_count reflects pure visible prose
    prose_only = re.sub(r"(<style\b[^>]*>.*?</style>|```.*?```)", " ", body, flags=re.DOTALL | re.IGNORECASE)
    prose_only = re.sub(r"(?m)^#{1,6}\s+.*$", " ", prose_only)
    prose_only = re.sub(r"https?://[^\s\)\"'>]+", " ", prose_only)
    prose_only = re.sub(r"\(/[a-zA-Z0-9_./?=&%#-]+(?:\s+\"[^\"]*\")?\)", "()", prose_only)
    prose_only = re.sub(r"<[^>]+>", " ", prose_only)

    h2_headings = "\n".join(re.findall(r"(?m)^##\s+(.+)$", body))
    rows = []
    try:
        with csv_path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                kw = ""
                for k, v in row.items():
                    if k and any(tok in k.lower() for tok in ("keyword", "phrase")) and v and v.strip():
                        kw = v.strip()
                        break
                if not kw:
                    continue
                left_bound = r"\b" if kw[0].isalnum() else ""
                right_bound = r"\b" if kw[-1].isalnum() else ""
                pattern = re.compile(rf"{left_bound}{re.escape(kw)}{right_bound}", re.IGNORECASE)
                in_h1 = len(pattern.findall(h1_title))
                in_h2 = len(pattern.findall(h2_headings))
                in_body = len(pattern.findall(prose_only))
                rows.append(
                    {
                        "keyword": kw,
                        "h1_count": str(in_h1),
                        "h2_count": str(in_h2),
                        "body_count": str(in_body),
                    }
                )
    except Exception:
        return []
    return rows


def _inline_md_format(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^\*\n]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    # Render Markdown images ![alt](src "title") -> <img ...> (note html.escape turns " into &quot;)
    escaped = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)(?:[ \t]+(?:&quot;(.*?)&quot;|\"([^\"]*)\"))?\)",
        lambda m: (
            f'<img src="{m.group(2)}" alt="{m.group(1)}"'
            + (f' title="{m.group(3) or m.group(4)}"' if (m.group(3) or m.group(4)) else "")
            + ' loading="lazy">'
        ),
        escaped,
    )
    # Render Markdown links [anchor](href "title") or [anchor](href, "title") -> <a ...>
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^),\s]+),?(?:[ \t]+(?:&quot;(.*?)&quot;|\"([^\"]*)\"))?\)",
        lambda m: (
            f'<a href="{m.group(2)}"'
            + (f' title="{m.group(3) or m.group(4)}"' if (m.group(3) or m.group(4)) else "")
            + f">{m.group(1)}</a>"
        ),
        escaped,
    )
    return escaped


def _md_table_block_to_html(lines: list[str]) -> str:
    rows = []
    for ln in lines:
        s = ln.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    if not rows:
        return ""
    thead = "<thead><tr>" + "".join(f"<th>{_inline_md_format(c)}</th>" for c in rows[0]) + "</tr></thead>"
    tbody_rows = []
    for r in rows[1:]:
        tbody_rows.append("<tr>" + "".join(f"<td>{_inline_md_format(c)}</td>" for c in r) + "</tr>")
    tbody = "<tbody>" + "".join(tbody_rows) + "</tbody>"
    return f"<table>{thead}{tbody}</table>"


def _md_to_preview_html(md_text: str) -> str:
    """Lightweight Markdown + Scoped HTML renderer for local host-theme preview (tables, lists, headings, callouts, hr, code blocks)."""
    code_vault: list[str] = []

    def _stash_code(match: re.Match) -> str:
        idx = len(code_vault)
        inner = html.escape(match.group(2).strip("\n"))
        code_vault.append(
            f'<pre style="background:#0a0a0a;border:1px solid var(--journal-line);border-radius:8px;padding:16px;overflow-x:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;"><code>{inner}</code></pre>'
        )
        return f"\n\n@@CODE_VAULT_{idx}@@\n\n"

    vaulted = re.sub(r"```([a-zA-Z0-9_-]*)\n(.*?)```", _stash_code, md_text.strip(), flags=re.DOTALL)
    # Ensure headings, horizontal rules, Markdown tables, lists, and blockquotes followed/preceded by a single newline are separated into their own blocks
    normalized = re.sub(r"(?m)^(#{1,4}\s+[^\n]+)\n(?!\n)", r"\1\n\n", vaulted)
    normalized = re.sub(r"(?m)^(?:---|\*\*\*)\s*$", "\n\n<hr style=\"border:0;border-top:1px solid var(--journal-line);margin:32px 0;\">\n\n", normalized)
    normalized = re.sub(r"(?m)^([^\n|][^\n]*)\n(?=\|.+\|[ \t]*$)", r"\1\n\n", normalized)
    normalized = re.sub(r"(?m)^(\|.+\|[ \t]*)\n(?=[^\n|])", r"\1\n\n", normalized)
    normalized = re.sub(r"(?m)^(?![-*]\s+|\d+\.\s+|>\s+|\s*$)([^\n]+)\n(?=(?:[-*]\s+|\d+\.\s+|>\s+))", r"\1\n\n", normalized)
    chunks = []
    for block in re.split(r"\n{2,}", normalized.strip()):
        b = block.strip()
        if not b:
            continue
        vault_match = re.fullmatch(r"@@CODE_VAULT_(\d+)@@", b)
        if vault_match:
            chunks.append(code_vault[int(vault_match.group(1))])
            continue
        lines = [ln.strip() for ln in b.splitlines() if ln.strip()]
        if b.startswith(("<div", "<details", "<table", "<section", "<hr", "<pre")):
            chunks.append(b)
        elif len(lines) >= 2 and lines[0].startswith("|") and lines[0].endswith("|") and "---" in lines[1]:
            chunks.append(_md_table_block_to_html(lines))
        elif all(re.match(r"^[-*]\s+", ln) for ln in lines):
            items = "".join(f"<li>{_inline_md_format(re.sub(r'^[-*]\s+', '', ln))}</li>" for ln in lines)
            chunks.append(f"<ul>{items}</ul>")
        elif all(re.match(r"^\d+\.\s+", ln) for ln in lines):
            items = "".join(f"<li>{_inline_md_format(re.sub(r'^\d+\.\s+', '', ln))}</li>" for ln in lines)
            chunks.append(f"<ol>{items}</ol>")
        elif b.startswith("## "):
            chunks.append(f"<h2>{_inline_md_format(b[3:].strip())}</h2>")
        elif b.startswith("### "):
            chunks.append(f"<h3>{_inline_md_format(b[4:].strip())}</h3>")
        elif b.startswith("#### "):
            chunks.append(f"<h4>{_inline_md_format(b[5:].strip())}</h4>")
        elif b.startswith("> "):
            inner = _inline_md_format(re.sub(r"(?m)^>\s?", "", b))
            chunks.append(f'<blockquote class="linker-article-check">{inner}</blockquote>')
        else:
            chunks.append(f"<p>{_inline_md_format(b)}</p>")
    return "\n".join(chunks)


def generate_host_theme_preview(article_dir: Path, h1_title: str, body: str) -> Path:
    """Generate a self-contained preview-in-host-theme.html replicating #md-blog-single (68ch dark-gold theme + pure-CSS viewport switcher)."""
    preview_path = article_dir / "preview-in-host-theme.html"
    rendered_body = _md_to_preview_html(body)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(h1_title or article_dir.name)} — Host Theme Preview (68ch / 390px / 320px)</title>
  <style>
    :root {{
      color-scheme: dark;
      --md-bg: #1a1a1a;
      --md-bg-deep: #141414;
      --md-bg-darkest: #0a0a0a;
      --md-gold: #c9a962;
      --md-gold-light: #d4b878;
      --md-gold-dark: #a88a4a;
      --md-gold-ink: #85692e;
      --md-cream: #faf9f7;
      --md-font-display: "Playfair Display", Georgia, serif;
      --md-font-sans: "Inter", system-ui, -apple-system, sans-serif;
    }}
    body {{ margin: 0; background: var(--md-bg-deep); color: rgba(255,255,255,.92); font-family: var(--md-font-sans); }}
    .vp-switch-input {{ display: none; }}
    .vp-toolbar {{
      position: sticky; top: 0; z-index: 50; background: #0a0a0a; border-bottom: 1px solid rgba(255,255,255,.14);
      padding: 10px 20px; display: flex; align-items: center; justify-content: center; gap: 12px; font-size: 12px;
    }}
    .vp-toolbar label {{
      padding: 6px 12px; border-radius: 999px; border: 1px solid rgba(255,255,255,.2); cursor: pointer; color: rgba(255,255,255,.78);
    }}
    #vp-desktop:checked ~ .vp-toolbar label[for="vp-desktop"],
    #vp-390:checked ~ .vp-toolbar label[for="vp-390"],
    #vp-320:checked ~ .vp-toolbar label[for="vp-320"] {{
      background: var(--md-gold); color: var(--md-bg-darkest); border-color: var(--md-gold); font-weight: 700;
    }}
    #md-blog-single {{
      --journal-surface: var(--md-bg-deep);
      --journal-panel: var(--md-bg);
      --journal-ink: rgba(255, 255, 255, .92);
      --journal-muted: rgba(255, 255, 255, .58);
      --journal-line: rgba(255, 255, 255, .14);
      --journal-wash: rgba(201, 169, 98, .12);
      max-width: 1440px; margin: 0 auto; padding: 32px;
    }}
    #vp-390:checked ~ #md-blog-single {{ max-width: 390px; padding: 0; }}
    #vp-320:checked ~ #md-blog-single {{ max-width: 320px; padding: 0; }}
    #md-blog-single .md-blog-single-main-card {{ background: var(--journal-panel); border-radius: 12px; max-width: 820px; margin: 0 auto; }}
    #md-blog-single .reader-title {{ padding: 32px 32px 16px; border-bottom: 1px solid var(--journal-line); }}
    #md-blog-single .md-blog-single-hero-title {{ margin: 0; font: 400 clamp(30px, 3vw, 42px)/1.18 var(--md-font-display); color: var(--journal-ink); }}
    #md-blog-single .reader-body {{ max-width: 68ch; margin: 0 auto; padding: 32px; }}
    #vp-390:checked ~ #md-blog-single .reader-body,
    #vp-320:checked ~ #md-blog-single .reader-body {{ padding: 0 24px 32px; }}
    #md-blog-single .md-blog-single-content {{ font-size: 16px; line-height: 1.85; overflow-wrap: anywhere; }}
    #md-blog-single .md-blog-single-content :is(h2,h3,[id]) {{ scroll-margin-top: calc(var(--md-header-h, 73px) + 24px); }}
    #md-blog-single .md-blog-single-content h2 {{ margin: 48px 0 16px; font: 600 24px/1.4 var(--md-font-sans); color: var(--journal-ink); }}
    #md-blog-single .md-blog-single-content h3 {{ margin: 32px 0 12px; font: 600 18px/1.5 var(--md-font-sans); }}
    #md-blog-single .md-blog-single-content p {{ margin-block: 20px; }}
    #md-blog-single .md-blog-single-content a {{ color: var(--md-gold); text-decoration: underline; }}
    #md-blog-single .md-blog-single-content table {{ width: 100%; table-layout: fixed; border-collapse: collapse; font-size: 14px; line-height: 1.6; margin-block: 24px; }}
    #md-blog-single .md-blog-single-content :is(th,td) {{ padding: 12px; border: 1px solid var(--journal-line); text-align: left; }}
    #md-blog-single .md-blog-single-content .linker-article-comparison {{ display: grid; gap: 24px; margin-block: 24px; }}
    #md-blog-single .md-blog-single-content .linker-article-topic {{ padding-bottom: 24px; border-bottom: 1px solid var(--journal-line); }}
    #md-blog-single .md-blog-single-content .linker-article-check {{ margin-block: 24px; padding: 20px 24px; border-left: 3px solid var(--md-gold-dark); background: var(--journal-wash); }}
  </style>
</head>
<body>
  <input class="vp-switch-input" type="radio" name="vp" id="vp-desktop" checked>
  <input class="vp-switch-input" type="radio" name="vp" id="vp-390">
  <input class="vp-switch-input" type="radio" name="vp" id="vp-320">
  <div class="vp-toolbar">
    <span style="color:var(--md-gold);font-weight:700;">#md-blog-single Viewport Audit:</span>
    <label for="vp-desktop">Desktop 1440px (68ch)</label>
    <label for="vp-390">Mobile 390px</label>
    <label for="vp-320">Compact 320px</label>
  </div>
  <article id="md-blog-single">
    <div class="md-blog-single-main-card">
      <header class="reader-title">
        <div style="font-size:12px;color:var(--md-gold);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:8px;">68ch Host-Theme Sandbox Preview (#md-blog-single)</div>
        <h1 class="md-blog-single-hero-title">{html.escape(h1_title or article_dir.name)}</h1>
      </header>
      <section class="reader-body">
        <div class="md-blog-single-content">
{rendered_body}
        </div>
      </section>
    </div>
  </article>
</body>
</html>
"""
    preview_path.write_text(doc, encoding="utf-8")
    return preview_path


def assemble_article(project_dir: Path, article_slug: str) -> dict:
    project_dir = Path(project_dir)
    if not project_dir.is_absolute() and not project_dir.exists():
        candidate_dir = Path(__file__).resolve().parents[1] / project_dir
        if candidate_dir.exists():
            project_dir = candidate_dir
    article_dir = project_dir / "articles" / article_slug
    enriched_path = article_dir / "enriched-draft.md"
    draft_path = article_dir / "draft.md"
    source_path = enriched_path if enriched_path.exists() else draft_path
    if not source_path.exists():
        raise FileNotFoundError(f"Neither enriched-draft.md nor draft.md exists in {article_dir}")

    drift_warnings: list[str] = []
    if enriched_path.exists() and draft_path.exists():
        if draft_path.stat().st_mtime > enriched_path.stat().st_mtime + 2.0:
            drift_warnings.append(
                "draft.md was modified more recently than enriched-draft.md; verify no prose edits in draft.md were left out of enriched-draft.md."
            )

    raw_body = source_path.read_text(encoding="utf-8")
    body = strip_control_metadata(raw_body)
    h1_title, body_no_h1 = extract_and_strip_leading_h1(body)

    html_dir = article_dir / "html-visuals"
    inlined_snippets: list[str] = []
    snippet_errors: list[str] = []

    def _replace_marker(match: re.Match) -> str:
        vis_id = match.group(1)
        candidate = html_dir / f"{vis_id}.html"
        if not candidate.exists():
            matches = list(html_dir.glob(f"{vis_id}*.html")) if html_dir.exists() else []
            candidate = matches[0] if matches else candidate
        if not candidate.exists():
            return match.group(0)
        html_text = candidate.read_text(encoding="utf-8")
        errs = validate_scoped_html_snippet(html_text, candidate.name)
        if errs:
            snippet_errors.extend(errs)
            return match.group(0)
        inlined_snippets.append(candidate.name)
        return compact_html_block_for_wpautop(html_text)

    body_no_h1 = HTML_MARKER_RE.sub(_replace_marker, body_no_h1)
    # Protect fenced ```...``` code blocks in a vault before stripping HTML comments or compacting/validating .b2b-mod-* blocks
    fenced_vault: list[str] = []

    def _stash_fenced(m: re.Match) -> str:
        idx = len(fenced_vault)
        fenced_vault.append(m.group(0))
        return f"@@FENCED_CODE_BLOCK_{idx}@@"

    body_vaulted = re.sub(r"```.*?```", _stash_fenced, body_no_h1, flags=re.DOTALL)
    unresolved_visual_markers = [m.group(0) for m in HTML_MARKER_RE.finditer(body_vaulted)]
    # Strip any remaining HTML comments outside fenced code blocks so HtmlComments::MAX_SHIPPED_BYTES = 64 is never tripped
    body_vaulted = re.sub(r"<!--.*?-->", "", body_vaulted, flags=re.DOTALL)
    # Normalize any accidental comma before link title `[anchor](url, "title")` -> valid CommonMark `[anchor](url "title")`
    body_vaulted = re.sub(r'\[([^\]]+)\]\(([^),\s"]+),[ \t]+"([^"]*)"\)', r'[\1](\2 "\3")', body_vaulted)
    body_vaulted = compact_inline_b2b_modules_in_markdown(body_vaulted)
    # Validate all inline balanced .b2b-mod-* / .linker-article-* modules outside fenced code blocks
    for _, _, mod_html in extract_balanced_b2b_modules(body_vaulted):
        if mod_html.lower().startswith("<div"):
            snippet_errors.extend(validate_scoped_html_snippet(mod_html, "inline .b2b-mod-* module"))
    # Restore fenced code blocks intact
    body_no_h1 = re.sub(
        r"@@FENCED_CODE_BLOCK_(\d+)@@",
        lambda m: fenced_vault[int(m.group(1))],
        body_vaulted,
    )
    citation_slots = extract_citation_slots(body_no_h1)
    fatigue_warnings = audit_structural_fatigue(body_no_h1)
    merge_warnings = check_unmerged_resources_and_faq(article_dir, body_no_h1)
    glossary_violations = scan_forbidden_terms(body_no_h1, project_dir)
    external_image_hotlinks = scan_external_image_hotlinks(body_no_h1, project_dir)
    keyword_counts = compute_exact_keyword_counts(h1_title, body_no_h1, article_dir)

    ready_body_path = article_dir / "publish-ready-body.md"
    ready_body_path.write_text(body_no_h1, encoding="utf-8")
    preview_path = generate_host_theme_preview(article_dir, h1_title, body_no_h1)

    pub_pack_path = article_dir / "publish-package.md"
    if pub_pack_path.exists():
        pack_text = pub_pack_path.read_text(encoding="utf-8")
        pack_text = re.sub(
            r"\n*<!-- BEGIN ASSEMBLED PUBLISH BODY -->.*?<!-- END ASSEMBLED PUBLISH BODY -->\n*",
            "\n",
            pack_text,
            flags=re.DOTALL,
        )
        cite_lines = [
            "<!-- BEGIN ASSEMBLED PUBLISH BODY -->",
            "---",
            "",
            "## External Tool Citation & Reference Handoff Slots (工具站补引用速查表)",
            "",
        ]
        if citation_slots:
            cite_lines.extend(
                [
                    "| # | Section (H2) | Claim Requiring External Citation | Recommended Search Query | In-Text Slot |",
                    "|---|---|---|---|---|",
                ]
            )
            for idx, slot in enumerate(citation_slots, start=1):
                cite_lines.append(
                    f"| {idx} | {slot['section']} | {slot['claim']} | `{slot['query']}` | `{slot['marker']}` |"
                )
        else:
            cite_lines.append(
                "_No unresolved `{{CITE: ...}}` slots detected in body (all external citations already inline or listed in External Citation Checklist)._"
            )

        cite_lines.extend(
            [
                "",
                "---",
                "",
                "## Full Assembled Article Body (Copy-Paste Ready — Top H1 Stripped for Host Template)",
                "",
                f"> Extracted H1 (for CMS Title Field): **{h1_title or '(see SEO Metadata)'}**  ",
                "> Single-file assembled copy (also saved standalone at `publish-ready-body.md` and previewable at `preview-in-host-theme.html`) with `Draft Control Metadata` and duplicate leading `# H1` stripped.",
                "",
                body_no_h1.strip(),
                "",
                "<!-- END ASSEMBLED PUBLISH BODY -->",
                "",
            ]
        )
        pub_pack_path.write_text(pack_text.rstrip() + "\n\n" + "\n".join(cite_lines), encoding="utf-8")

    return {
        "article": article_slug,
        "extracted_h1": h1_title,
        "ready_body_path": str(ready_body_path),
        "host_preview_path": str(preview_path),
        "inlined_snippets": inlined_snippets,
        "unresolved_visual_markers": unresolved_visual_markers,
        "snippet_errors": snippet_errors,
        "citation_slots_count": len(citation_slots),
        "fatigue_warnings": fatigue_warnings,
        "merge_warnings": merge_warnings,
        "drift_warnings": drift_warnings,
        "glossary_violations": glossary_violations,
        "external_image_hotlinks": external_image_hotlinks,
        "keyword_counts": keyword_counts,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path, help="Path to content-workspace/<project-slug>")
    parser.add_argument("article_slug", help="Article slug under articles/")
    args = parser.parse_args(argv)

    result = assemble_article(args.project_dir, args.article_slug)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if (
        result["snippet_errors"]
        or result["glossary_violations"]
        or result["unresolved_visual_markers"]
        or result["external_image_hotlinks"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
