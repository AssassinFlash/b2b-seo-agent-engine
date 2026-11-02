#!/usr/bin/env python3
"""HTML denoiser powered by `trafilatura` (with lightweight stdlib fallback).

Converts raw benchmark HTML pages into clean, structured Markdown for Linguistic DNA
and 21-dimension Success Formula extraction (`/article-benchmark-extract`).
Strips layout boilerplate (`<nav>`, `<footer>`, `<aside>`, `<header>`, `<script>`,
cookie banners, related-post widgets) while preserving `#..######` headings,
`| Markdown | Tables |`, `**bold**`, `*italic*`, inline links, and lists.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class _MinimalFallbackExtractor(HTMLParser):
    """Lightweight stdlib fallback used only if `trafilatura` is not yet installed."""

    NOISE = {"script", "style", "nav", "footer", "aside", "header", "form", "iframe", "noscript", "svg"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.noise_depth = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if t in self.NOISE:
            self.noise_depth += 1
            return
        if self.noise_depth > 0:
            return
        if t in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.chunks.append(f"\n\n{'#' * int(t[1])} ")
        elif t in {"p", "div", "tr", "li", "blockquote"}:
            self.chunks.append("\n\n")
        elif t in {"strong", "b"}:
            self.chunks.append("**")
        elif t in {"th", "td"}:
            self.chunks.append("| ")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t in self.NOISE:
            if self.noise_depth > 0:
                self.noise_depth -= 1
            return
        if self.noise_depth > 0:
            return
        if t in {"strong", "b"}:
            self.chunks.append("**")
        elif t == "tr":
            self.chunks.append(" |")

    def handle_data(self, data: str) -> None:
        if self.noise_depth == 0 and data:
            self.chunks.append(data)


def extract_markdown_from_html(html: str) -> str:
    try:
        import trafilatura  # type: ignore

        extracted = trafilatura.extract(
            html,
            output_format="markdown",
            include_tables=True,
            include_formatting=True,
            include_links=True,
            favor_recall=True,
        )
        if extracted and extracted.strip():
            # Ensure h1 from <main>/<article> is preserved if trafilatura dropped the top h1 as metadata
            h1_match = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, flags=re.IGNORECASE | re.DOTALL)
            if h1_match:
                h1_txt = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip()
                if h1_txt and f"# {h1_txt}" not in extracted:
                    extracted = f"# {h1_txt}\n\n{extracted}"
            # Normalize trailing spaces inside markdown table cells (`| Grade | Tolerance | ` -> `| Grade | Tolerance |`)
            extracted = re.sub(r"\|\s+\n", "|\n", extracted)
            return re.sub(r"\n{3,}", "\n\n", extracted).strip() + "\n"
    except ImportError:
        pass

    parser = _MinimalFallbackExtractor()
    parser.feed(html)
    parser.close()
    raw = "".join(parser.chunks)
    return re.sub(r"\n{3,}", "\n\n", raw).strip() + "\n"


def denoise_html(input_file: Path, output_file: Path) -> None:
    input_file = Path(input_file)
    output_file = Path(output_file)
    repo_root = Path(__file__).resolve().parents[1]
    if not input_file.is_absolute() and not input_file.exists() and (repo_root / input_file).exists():
        input_file = repo_root / input_file
    if (
        not output_file.is_absolute()
        and str(output_file).startswith("content-workspace")
        and not (Path.cwd() / "content-workspace").exists()
    ):
        output_file = repo_root / output_file
    if not input_file.exists():
        print(f"Error: {input_file} not found.", file=sys.stderr)
        sys.exit(1)

    html = input_file.read_text(encoding="utf-8", errors="ignore")
    text = extract_markdown_from_html(html)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding="utf-8")
    print(f"Successfully denoised {input_file.name} to {output_file.name}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 denoise_html.py <input_html_file> <output_md_file>")
        sys.exit(0 if len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help") else 1)
    denoise_html(Path(sys.argv[1]), Path(sys.argv[2]))
