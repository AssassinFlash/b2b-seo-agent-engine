"""Unit tests for scripts/assemble_publish_draft.py and scripts/render_html_visual.py."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.assemble_publish_draft import (
    _md_to_preview_html,
    assemble_article,
    audit_structural_fatigue,
    compact_html_block_for_wpautop,
    compact_inline_b2b_modules_in_markdown,
    extract_and_strip_leading_h1,
    extract_balanced_b2b_modules,
    extract_citation_slots,
    strip_control_metadata,
    validate_scoped_html_snippet,
)


def test_validate_scoped_html_snippet_rejects_full_page_and_global_css():
    bad_fullpage = "<!DOCTYPE html><html><head><script src='https://cdn.tailwindcss.com'></script></head><body>Hi</body></html>"
    errs = validate_scoped_html_snippet(bad_fullpage, "v-03.html")
    assert any("full-page tags" in e for e in errs)

    bad_global_css = '<div class="b2b-mod-x"><style>body { background: #000; }</style></div>'
    errs2 = validate_scoped_html_snippet(bad_global_css, "v-04.html")
    assert any("unscoped global selectors" in e for e in errs2)

    bad_wide_grid = '<div class="b2b-mod-x" style="display:grid;grid-template-columns:repeat(3, 1fr);"></div>'
    errs3 = validate_scoped_html_snippet(bad_wide_grid, "v-05.html")
    assert any("overflows a 68ch reader column" in e for e in errs3)

    bad_expanded_grid = '<div class="b2b-mod-x" style="display:grid;grid-template-columns: 1fr 1fr 1fr;"></div>'
    errs3b = validate_scoped_html_snippet(bad_expanded_grid, "v-05b.html")
    assert any("overflows a 68ch reader column" in e for e in errs3b)

    bad_inline_js = '<div class="b2b-mod-x"><button onclick="alert(1)">Click</button></div>'
    errs4 = validate_scoped_html_snippet(bad_inline_js, "v-06.html")
    assert any("Content-Security-Policy" in e for e in errs4)

    bad_google_font = '<div class="b2b-mod-x"><link href="https://fonts.googleapis.com/css2?family=Space+Mono"></div>'
    errs5 = validate_scoped_html_snippet(bad_google_font, "v-07.html")
    assert any("full-page tags" in e for e in errs5)

    bad_iframe = '<div class="b2b-mod-x"><iframe src="https://example.com/embed"></iframe></div>'
    errs5b = validate_scoped_html_snippet(bad_iframe, "v-07b.html")
    assert any("full-page tags" in e for e in errs5b)

    bad_unclosed_div = '<div class="b2b-mod-x"><div class="inner">hello</div>'
    errs6 = validate_scoped_html_snippet(bad_unclosed_div, "v-08.html")
    assert any("unbalanced <div> tags" in e for e in errs6)

    bad_css_import = '<div class="b2b-mod-x"><style>@import url("https://evil.com/a.css");</style></div>'
    errs7 = validate_scoped_html_snippet(bad_css_import, "v-09.html")
    assert any("@import" in e for e in errs7)

    bad_js_href = '<div class="b2b-mod-x"><a href="javascript:alert(1)">click</a></div>'
    errs8 = validate_scoped_html_snippet(bad_js_href, "v-10.html")
    assert any("javascript: URIs" in e for e in errs8)

    bad_comma_selector = '<div class="b2b-mod-x"><style>.b2b-mod-x p, h2 { color: red; }</style></div>'
    errs9 = validate_scoped_html_snippet(bad_comma_selector, "v-11.html")
    assert any("unscoped global selectors" in e for e in errs9)

    bad_inline_style_url = '<div class="b2b-mod-x" style="background-image: url(\'https://evil.cdn.com/bg.jpg\');">Hi</div>'
    errs10 = validate_scoped_html_snippet(bad_inline_style_url, "v-12.html")
    assert any("url(http" in e for e in errs10)

    good_scoped = (
        '<div class="b2b-mod-spec" style="padding:16px;">'
        "<style>.b2b-mod-spec .card { border: 1px solid #333; }</style>"
        '<div class="card">316L ±0.15 mm</div></div>'
    )
    assert validate_scoped_html_snippet(good_scoped, "hv-01.html") == []


def test_strip_control_metadata_and_extract_citation_slots():
    raw = (
        "# Title\n\n"
        "## How Much Does PVD Coating Cost?\n\n"
        "Vacuum PVD adds 18-25% over brushed 304 {{CITE: PVD vs powder coat cost delta | architectural PVD stainless steel cost per sqm}}.\n\n"
        "## Draft Control Metadata\n\n"
        "| Control | Value |\n|---|---|\n| Imitation | 40% |\n"
    )
    cleaned = strip_control_metadata(raw)
    assert "Draft Control Metadata" not in cleaned
    slots = extract_citation_slots(cleaned)
    assert len(slots) == 1
    assert slots[0]["section"] == "How Much Does PVD Coating Cost?"
    assert "PVD vs powder coat cost delta" in slots[0]["claim"]
    assert "architectural PVD stainless steel cost per sqm" in slots[0]["query"]


def test_audit_structural_fatigue_flags_repetitive_related_blocks():
    repetitive = (
        "## H2 1\n> ### → Related: A\n\n"
        "## H2 2\n> ### → Related: B\n\n"
        "## H2 3\n> ### → Related: C\n\n"
        "| C1 | C2 | C3 | C4 | C5 |\n|---|---|---|---|---|\n| 1 | 2 | 3 | 4 | 5 |\n"
    )
    warnings = audit_structural_fatigue(repetitive)
    assert any("identical '> ### → Related:'" in w for w in warnings)
    assert any("5 columns" in w for w in warnings)


def test_assemble_article_inlines_scoped_html_and_updates_publish_package(tmp_path: Path):
    proj = tmp_path / "content-workspace" / "demo"
    art = proj / "articles" / "test-article"
    html_dir = art / "html-visuals"
    html_dir.mkdir(parents=True)

    snippet = '<div class="b2b-mod-bento" style="padding:12px;">Bento Spec ±0.15 mm</div>'
    (html_dir / "hv-01.html").write_text(snippet, encoding="utf-8")

    (art / "enriched-draft.md").write_text(
        "# Enriched Draft — Demo Article\n\n"
        "## Why Does Tolerance Matter?\n\n"
        "It prevents field gaps {{CITE: 0.15mm laser tolerance standard | ISO 9013 laser cutting tolerance}}.\n"
        'See [Custom Screens](/custom-metal-divider-screens/, "Custom Stainless Steel Screens") for details.\n\n'
        "<!-- html-visual: hv-01 material-choice-decision-card -->\n\n"
        "## Draft Control Metadata\nSecret QA notes\n",
        encoding="utf-8",
    )
    (art / "publish-package.md").write_text("# Publish Package\n\n## SEO Metadata\n", encoding="utf-8")

    res = assemble_article(proj, "test-article")
    assert res["snippet_errors"] == []
    assert res["inlined_snippets"] == ["hv-01.html"]
    assert res["citation_slots_count"] == 1

    ready_text = (art / "publish-ready-body.md").read_text(encoding="utf-8")
    assert "b2b-mod-bento" in ready_text
    assert "Draft Control Metadata" not in ready_text
    assert '(/custom-metal-divider-screens/ "Custom Stainless Steel Screens")' in ready_text
    assert '(/custom-metal-divider-screens/, ' not in ready_text

    pack_text = (art / "publish-package.md").read_text(encoding="utf-8")
    assert "External Tool Citation & Reference Handoff Slots" in pack_text
    assert "ISO 9013 laser cutting tolerance" in pack_text
    assert "Full Assembled Article Body" in pack_text
    assert (art / "preview-in-host-theme.html").exists()
    assert res["extracted_h1"] == "Demo Article"
    # Verify leading H1 was stripped from publish-ready-body.md to prevent double H1 in #md-blog-single
    assert not ready_text.lstrip().startswith("# Demo Article")


def test_forbidden_glossary_terms_and_keyword_counts(tmp_path: Path):
    proj = tmp_path / "content-workspace" / "metal-divider"
    art = proj / "articles" / "screen-guide"
    art.mkdir(parents=True)

    (proj / "project-profile.json").write_text(
        '{"projectSlug":"metal-divider","companyName":"Metal Divider","canonicalDomain":"https://archmetal-screens.example.com",'
        '"forbiddenTerms":["product","products","cart"],"preferredTerms":{"product":"pattern","products":"patterns","cart":"inquiry"}}',
        encoding="utf-8",
    )
    (art / "keyword-record.csv").write_text(
        "#,Keyword / Phrase,Type\n1,stainless steel screen,Primary\n2,laser cut pattern,Secondary\n",
        encoding="utf-8",
    )
    (art / "enriched-draft.md").write_text(
        "# Stainless Steel Screen Guide\n\n"
        "## Why Choose a Laser Cut Pattern?\n\n"
        '<div class="b2b-mod-x" data-product-id="99">\n'
        "  <style>\n"
        "    .b2b-mod-x .product { color: gold; }\n"
        "  </style>\n"
        "  Safe attribute\n"
        "</div>\n"
        "Each stainless steel screen pattern is fabricated to ±0.15 mm. Screening and stainless steel screens plural should not inflate singular count. Do not call this a product in copy. See [Legacy](/pages/outdoor-screens) and [Old PDP](/products/md-r001).\n",
        encoding="utf-8",
    )

    res = assemble_article(proj, "screen-guide")
    assert len(res["glossary_violations"]) == 3
    assert "Forbidden glossary term 'product' appears 1 time(s)" in res["glossary_violations"][0]
    assert "L9:" in res["glossary_violations"][0]
    assert any("Legacy retired URL path '/pages/outdoor-screens'" in v for v in res["glossary_violations"])
    assert any("Legacy retired URL path '/products/md-r001'" in v for v in res["glossary_violations"])
    kw_map = {r["keyword"]: r for r in res["keyword_counts"]}
    assert kw_map["stainless steel screen"]["h1_count"] == "1"
    assert kw_map["stainless steel screen"]["body_count"] == "1"
    assert kw_map["laser cut pattern"]["h2_count"] == "1"
    assert kw_map["laser cut pattern"]["body_count"] == "0"


def test_wpautop_zero_blank_lines_compaction():
    html_with_blank_lines = (
        '<div class="b2b-mod-card">\n\n'
        "  <style>\n\n"
        "    .b2b-mod-card p { margin: 0; }\n\n"
        "  </style>\n\n"
        "  <div>Content</div>\n\n"
        "</div>"
    )
    compacted = compact_html_block_for_wpautop(html_with_blank_lines)
    assert "\n\n" not in compacted
    assert compacted.startswith('<div class="b2b-mod-card">')
    assert compacted.endswith("</div>")


def test_nested_div_balanced_extraction_and_preview_table_rendering():
    md_with_nested_divs = (
        "Intro paragraph.\n\n"
        '<div class="b2b-mod-env-tabs">\n\n'
        '  <div class="b2b-grid">\n\n'
        '    <div class="b2b-card">First child</div>\n\n'
        '    <div class="b2b-card" onclick="evil()">Second child after first closing div</div>\n\n'
        "  </div>\n\n"
        "</div>\n\n"
        "| Grade | Open Area |\n"
        "|---|---|\n"
        "| **316** | 33% |\n"
    )
    modules = extract_balanced_b2b_modules(md_with_nested_divs)
    assert len(modules) == 1
    _, _, full_mod = modules[0]
    assert 'onclick="evil()"' in full_mod
    errs = validate_scoped_html_snippet(full_mod, "nested")
    assert any("Content-Security-Policy" in e for e in errs)

    compacted_md = compact_inline_b2b_modules_in_markdown(md_with_nested_divs)
    # Blank lines inside the nested .b2b-mod-env-tabs block must all be gone
    _, _, compacted_mod = extract_balanced_b2b_modules(compacted_md)[0]
    assert "\n\n" not in compacted_mod

    preview_html = _md_to_preview_html(
        md_with_nested_divs
        + '\n\n![Panel Close-Up](/wp-content/uploads/panel.webp "316L Panel")\n\n'
        + '[Browse Patterns](/patterns/ "Pattern Library")\n'
    )
    assert "<table><thead><tr><th>Grade</th><th>Open Area</th></tr></thead>" in preview_html
    assert "<td><strong>316</strong></td><td>33%</td>" in preview_html
    assert '<img src="/wp-content/uploads/panel.webp" alt="Panel Close-Up" title="316L Panel" loading="lazy">' in preview_html
    assert '<a href="/patterns/" title="Pattern Library">Browse Patterns</a>' in preview_html

    h1, stripped = extract_and_strip_leading_h1("---\ntitle: X\n---\n\n# Real H1 Title\n\nFirst paragraph.\n")
    assert h1 == "Real H1 Title"
    assert stripped == "First paragraph.\n"

    # Single-newline heading + horizontal rule --- + tight single-newline table & list must render as <h2> + <p> + <table> + <ul> + <hr>
    hr_and_single_nl = (
        "## Heading With `Code`\n"
        "Paragraph right below with *italic emphasis*.\n"
        "| Col A | Col B |\n"
        "|:---|---:|\n"
        "| 304 | 316 |\n"
        "Line right after table:\n"
        "- Bullet item 1\n"
        "- Bullet item 2\n\n---\n\nNext section."
    )
    rendered_hr = _md_to_preview_html(hr_and_single_nl)
    assert "<h2>Heading With <code>Code</code></h2>" in rendered_hr
    assert "<p>Paragraph right below with <em>italic emphasis</em>.</p>" in rendered_hr
    assert "<table><thead><tr><th>Col A</th><th>Col B</th></tr></thead>" in rendered_hr
    assert "<p>Line right after table:</p>" in rendered_hr
    assert "<ul><li>Bullet item 1</li><li>Bullet item 2</li></ul>" in rendered_hr
    assert "<hr " in rendered_hr
    assert "<p>---</p>" not in rendered_hr


def test_apify_launch_run_with_failover_switches_slots(monkeypatch):
    from scripts import apify_research as ar

    calls = []

    def fake_api(token, path, payload=None):
        calls.append((token, path))
        if token == "tok_slot1":
            if path == "/users/me":
                return {"data": {"id": "u1"}}
            if path == "/users/me/limits":
                # Slot 1 passes /users/me, and even if limits look slightly under, POST /runs returns 402!
                return {"data": {"current": {"monthlyUsageUsd": 4.99}, "limits": {"maxMonthlyUsageUsd": 5.0}}}
            if "/runs?" in path:
                raise ar.ApiError(402, "Monthly usage hard limit exceeded")
            return {"data": {"defaultRunOptions": {"build": "latest"}}}
        if token == "tok_slot2":
            if path == "/users/me":
                return {"data": {"id": "u2"}}
            if path == "/users/me/limits":
                return {"data": {"current": {"monthlyUsageUsd": 5.0}, "limits": {"maxMonthlyUsageUsd": 5.0}}}
        if token == "tok_slot3":
            if path == "/users/me":
                return {"data": {"id": "u3"}}
            if path == "/users/me/limits":
                return {"data": {"current": {"monthlyUsageUsd": 0.5}, "limits": {"maxMonthlyUsageUsd": 5.0}}}
            if path.startswith("/acts/") and "/runs?" not in path:
                return {"data": {"defaultRunOptions": {"build": "latest"}}}
            if "/runs?" in path:
                return {"data": {"id": "run_ok_slot3", "status": "READY", "defaultDatasetId": "ds_3"}}
        raise AssertionError(f"Unexpected call: {token} {path}")

    monkeypatch.setattr(ar, "api", fake_api)
    tokens = [(1, "tok_slot1"), (2, "tok_slot2"), (3, "tok_slot3")]
    slot, tok, meta = ar.launch_run_with_failover(tokens, "apify~rag-web-browser", {"query": "test"})
    assert slot == 3
    assert tok == "tok_slot3"
    assert meta["id"] == "run_ok_slot3"


def test_fenced_code_block_vault_preserves_comments_and_skips_csp(tmp_path: Path):
    proj = tmp_path / "content-workspace" / "demo"
    art = proj / "articles" / "code-article"
    art.mkdir(parents=True)
    md = (
        "# Code Example Article\n\n"
        "## How to Embed\n\n"
        "```html\n"
        "<!-- keep this comment inside code block -->\n"
        '<div class="b2b-mod-demo">\n\n'
        "  <script>console.log(1)</script>\n"
        "</div>\n"
        "```\n"
    )
    (art / "enriched-draft.md").write_text(md, encoding="utf-8")
    res = assemble_article(proj, "code-article")
    assert res["snippet_errors"] == []
    ready = (art / "publish-ready-body.md").read_text(encoding="utf-8")
    assert "<!-- keep this comment inside code block -->" in ready
    preview = (art / "preview-in-host-theme.html").read_text(encoding="utf-8")
    assert "<pre " in preview and "<code>" in preview


def test_external_image_hotlinks_detected(tmp_path: Path):
    proj = tmp_path / "content-workspace" / "metal-divider"
    art = proj / "articles" / "hotlink-test"
    art.mkdir(parents=True)
    (proj / "project-profile.json").write_text(
        '{"projectSlug":"metal-divider","canonicalDomain":"https://archmetal-screens.example.com"}',
        encoding="utf-8",
    )
    (art / "enriched-draft.md").write_text(
        "# Hotlink Check\n\n"
        "![Local OK](https://archmetal-screens.example.com/wp-content/uploads/ok.webp)\n\n"
        "![External Blocked](https://cdn.other-site.org/blocked.jpg)\n\n"
        '<div class="b2b-mod-img" style="background-image:url(\'https://bg-cdn.net/x.webp\');"><img src="https://untrusted.io/pic.png" alt="x"></div>\n',
        encoding="utf-8",
    )
    res = assemble_article(proj, "hotlink-test")
    assert len(res["external_image_hotlinks"]) == 3
    assert any("cdn.other-site.org" in h for h in res["external_image_hotlinks"])
    assert any("untrusted.io" in h for h in res["external_image_hotlinks"])
    assert any("bg-cdn.net" in h for h in res["external_image_hotlinks"])


def test_extract_google_paa_handles_exceptions_and_url_encoding():
    from scripts import extract_google_paa as paa

    class FailingPage:
        def goto(self, *args, **kwargs):
            raise TimeoutError("Playwright navigation timed out")

    rec = paa.extract_one(FailingPage(), "#4 finish & 33% open area", "en", "us")
    assert rec["error"] == "navigation timeout"
    assert "%234+finish+%26+33%25+open+area" in rec["query_url"]


class AssembleAndRenderTestCase(unittest.TestCase):
    def test_all(self):
        test_validate_scoped_html_snippet_rejects_full_page_and_global_css()
        test_strip_control_metadata_and_extract_citation_slots()
        test_audit_structural_fatigue_flags_repetitive_related_blocks()
        test_wpautop_zero_blank_lines_compaction()
        test_nested_div_balanced_extraction_and_preview_table_rendering()
        test_extract_google_paa_handles_exceptions_and_url_encoding()
        with tempfile.TemporaryDirectory() as td1:
            test_assemble_article_inlines_scoped_html_and_updates_publish_package(Path(td1))
        with tempfile.TemporaryDirectory() as td2:
            test_forbidden_glossary_terms_and_keyword_counts(Path(td2))
        with tempfile.TemporaryDirectory() as td3:
            test_fenced_code_block_vault_preserves_comments_and_skips_csp(Path(td3))
        with tempfile.TemporaryDirectory() as td4:
            test_external_image_hotlinks_detected(Path(td4))







