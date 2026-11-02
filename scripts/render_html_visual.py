#!/usr/bin/env python3
"""Validate Scoped Inline HTML Snippets or render Canvas HTML visuals via Playwright DOM-selector cropping.

Two modes:
1. `--validate-snippet <file.html>`:
   Verifies that an inline HTML structural block (`<div class="b2b-mod-...">`) is self-contained,
   uses no `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, or external `cdn.tailwindcss.com`, and does
   not leak unscoped global CSS selectors (`body`, `html`, `*`, `h1`, `h2`, `p`, `a`).
2. `--render <file.html> --output <out.webp|out.png> [--selector .b2b-canvas-card]`:
   Uses local Chrome via Playwright to screenshot only the target DOM element (never the full viewport),
   avoiding black bars or margin cropping.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble_publish_draft import validate_scoped_html_snippet  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


def _resolve_repo_path(path: Path) -> Path:
    path = Path(path)
    if not path.is_absolute() and not path.exists() and (ROOT / path).exists():
        return ROOT / path
    return path


def render_dom_element(html_path: Path, output_path: Path, selector: str = ".b2b-canvas-card, body > div:first-of-type") -> dict:
    """Render a specific DOM container from html_path into output_path using Playwright real Chrome."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Playwright Python package is required for --render mode") from exc

    html_abs = _resolve_repo_path(html_path).resolve()
    if not html_abs.exists():
        raise FileNotFoundError(f"HTML file not found: {html_abs}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        # Strict real Chrome only (no bundled Chromium fallback per browser discipline)
        browser = p.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        try:
            page = context.new_page()
            page.goto(html_abs.as_uri(), wait_until="networkidle")
            loc = page.locator(selector).first
            loc.wait_for(state="visible", timeout=5000)
            box = loc.bounding_box()
            loc.screenshot(path=str(output_path))
        finally:
            context.close()
            browser.close()

    size_kb = round(output_path.stat().st_size / 1024, 1)
    return {
        "input": str(html_path),
        "output": str(output_path),
        "selector": selector,
        "dimensions": box,
        "size_kb": size_kb,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file", type=Path, help="Path to HTML snippet or canvas visual")
    parser.add_argument("--validate-snippet", action="store_true", help="Validate that HTML is a safe Scoped Inline Snippet")
    parser.add_argument("--render", type=Path, help="Output image path (.png or .webp) for DOM-selector screenshot")
    parser.add_argument("--selector", default=".b2b-canvas-card, body > div:first-of-type", help="CSS selector to crop")
    args = parser.parse_args(argv)

    if args.validate_snippet or not args.render:
        html_file = _resolve_repo_path(args.html_file)
        text = html_file.read_text(encoding="utf-8")
        errors = validate_scoped_html_snippet(text, html_file.name)
        result = {
            "file": str(html_file),
            "valid_scoped_snippet": len(errors) == 0,
            "errors": errors,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if not errors else 1

    info = render_dom_element(args.html_file, args.render, args.selector)
    print(json.dumps(info, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
