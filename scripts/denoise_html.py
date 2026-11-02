#!/usr/bin/env python3
"""Zero-dependency HTML denoiser that converts main article DOM into structured Markdown.

Uses Python's standard-library `html.parser.HTMLParser` so it runs under any bare
`python3` interpreter without requiring `beautifulsoup4`. Strips layout noise
(`<script>`, `<style>`, `<nav>`, `<footer>`, `<aside>`, `<header>`, `<form>`, `<iframe>`,
`<noscript>`, `<svg>`) while preserving `#..######` headings, `| Markdown | Tables |`,
`**bold**`, `*italic*`, `` `code` ``, nested lists, blockquotes, and fenced code blocks.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path


NOISE_TAGS = {"script", "style", "nav", "footer", "aside", "header", "form", "iframe", "noscript", "svg"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


@dataclass
class DomNode:
    tag: str  # "#text" for text nodes
    attrs: dict[str, str] = field(default_factory=dict)
    children: list["DomNode"] = field(default_factory=list)
    text: str = ""

    def get_text(self) -> str:
        if self.tag == "#text":
            return self.text
        return "".join(c.get_text() for c in self.children)


class _TreeBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = DomNode("document")
        self.stack: list[DomNode] = [self.root]
        self.noise_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if t in NOISE_TAGS:
            self.noise_depth += 1
            return
        if self.noise_depth > 0:
            return
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        node = DomNode(t, attr_map)
        self.stack[-1].children.append(node)
        if t not in VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t in NOISE_TAGS:
            if self.noise_depth > 0:
                self.noise_depth -= 1
            return
        if self.noise_depth > 0 or t in VOID_TAGS:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == t:
                del self.stack[i:]
                break

    def handle_data(self, data: str) -> None:
        if self.noise_depth > 0 or not data:
            return
        self.stack[-1].children.append(DomNode("#text", text=data))


def _find_first(node: DomNode, predicate) -> DomNode | None:
    if predicate(node):
        return node
    for child in node.children:
        found = _find_first(child, predicate)
        if found is not None:
            return found
    return None


def _find_all(node: DomNode, tag_names: set[str], recursive: bool = True) -> list[DomNode]:
    out: list[DomNode] = []
    for child in node.children:
        if child.tag in tag_names:
            out.append(child)
        if recursive and child.tag != "#text":
            out.extend(_find_all(child, tag_names, recursive=True))
    return out


def _clean_inline_spacing(text: str) -> str:
    s = re.sub(r"[ \t\r\n]+", " ", text).strip()
    # Tighten spaces before punctuation like ?, ., ,, !, ), :, ;
    s = re.sub(r"\s+([?.,!:;\)])", r"\1", s)
    # Tighten space right after opening parenthesis
    s = re.sub(r"(\()\s+", r"\1", s)
    return s


def _inline_md(node: DomNode) -> str:
    if node.tag == "#text":
        return re.sub(r"[ \t\r\n]+", " ", node.text)
    name = node.tag
    if name == "br":
        return "\n"
    if name in ("ul", "ol"):
        return ""
    inner = "".join(_inline_md(c) for c in node.children).strip()
    if not inner:
        return ""
    if name in ("strong", "b"):
        return f"**{inner}**"
    if name in ("em", "i"):
        return f"*{inner}*"
    if name == "code":
        return f"`{inner}`"
    if name == "a" and node.attrs.get("href"):
        href = node.attrs["href"].strip()
        if href and not href.startswith("javascript:"):
            return f"[{inner}]({href})"
    return inner


def _table_to_md(table_node: DomNode) -> str:
    rows = []
    for tr in _find_all(table_node, {"tr"}):
        cells = [c for c in tr.children if c.tag in {"th", "td"}]
        if not cells:
            continue
        row = [
            _clean_inline_spacing("".join(_inline_md(c) for c in cell.children)).replace("|", "\\|")
            for cell in cells
        ]
        rows.append(row)
    if not rows:
        return ""
    col_count = max(len(r) for r in rows)
    normalized = [r + [""] * (col_count - len(r)) for r in rows]
    lines = [
        "| " + " | ".join(normalized[0]) + " |",
        "| " + " | ".join(["---"] * col_count) + " |",
    ]
    for r in normalized[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def _list_to_md(list_node: DomNode, indent: int = 0) -> str:
    lines: list[str] = []
    is_ordered = list_node.tag == "ol"
    li_children = [c for c in list_node.children if c.tag == "li"]
    for idx, li in enumerate(li_children, start=1):
        inline_parts = [c for c in li.children if c.tag not in ("ul", "ol")]
        item_txt = _clean_inline_spacing("".join(_inline_md(c) for c in inline_parts))
        prefix = f"{idx}." if is_ordered else "-"
        pad = "  " * indent
        if item_txt:
            lines.append(f"{pad}{prefix} {item_txt}")
        for sub in li.children:
            if sub.tag in ("ul", "ol"):
                sub_md = _list_to_md(sub, indent + 1)
                if sub_md:
                    lines.append(sub_md)
    return "\n".join(lines)


INLINE_TAGS = {"#text", "span", "strong", "b", "em", "i", "code", "a", "small", "sup", "sub", "mark", "br", "abbr", "cite", "q", "time", "u", "s", "del", "ins"}


def _blocks_to_md(root: DomNode) -> list[str]:
    blocks: list[str] = []
    inline_buf: list[DomNode] = []

    def _flush_inline() -> None:
        if not inline_buf:
            return
        merged = _clean_inline_spacing("".join(_inline_md(c) for c in inline_buf))
        inline_buf.clear()
        if merged:
            blocks.append(merged)

    for child in root.children:
        if child.tag in INLINE_TAGS:
            inline_buf.append(child)
            continue
        _flush_inline()
        name = child.tag
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            heading_text = _clean_inline_spacing("".join(_inline_md(c) for c in child.children))
            if heading_text:
                blocks.append(f"{'#' * level} {heading_text}")
        elif name == "p":
            para = _clean_inline_spacing("".join(_inline_md(c) for c in child.children))
            if para:
                blocks.append(para)
        elif name in ("ul", "ol"):
            list_md = _list_to_md(child, indent=0)
            if list_md:
                blocks.append(list_md)
        elif name == "table":
            md_table = _table_to_md(child)
            if md_table:
                blocks.append(md_table)
        elif name == "blockquote":
            quote_txt = _clean_inline_spacing("".join(_inline_md(c) for c in child.children))
            if quote_txt:
                blocks.append(f"> {quote_txt}")
        elif name == "pre":
            code_txt = child.get_text().strip("\n")
            if code_txt:
                blocks.append(f"```\n{code_txt}\n```")
        else:
            blocks.extend(_blocks_to_md(child))
    _flush_inline()
    return blocks


def denoise_html(input_file: Path, output_file: Path) -> None:
    input_file = Path(input_file)
    output_file = Path(output_file)
    repo_root = Path(__file__).resolve().parents[1]
    if not input_file.is_absolute() and not input_file.exists() and (repo_root / input_file).exists():
        input_file = repo_root / input_file
    if not output_file.is_absolute() and str(output_file).startswith("content-workspace") and not (Path.cwd() / "content-workspace").exists():
        output_file = repo_root / output_file
    if not input_file.exists():
        print(f"Error: {input_file} not found.", file=sys.stderr)
        sys.exit(1)

    html = input_file.read_text(encoding="utf-8", errors="ignore")
    builder = _TreeBuilder()
    builder.feed(html)
    builder.close()
    doc = builder.root

    main_content = (
        _find_first(doc, lambda n: n.tag == "main")
        or _find_first(doc, lambda n: n.tag == "article")
        or _find_first(doc, lambda n: n.tag == "div" and bool(re.search(r"content|main", n.attrs.get("id", ""), re.I)))
        or _find_first(doc, lambda n: n.tag == "div" and bool(re.search(r"content|main", n.attrs.get("class", ""), re.I)))
        or _find_first(doc, lambda n: n.tag == "body")
        or doc
    )

    blocks = _blocks_to_md(main_content)
    text = "\n\n".join(blocks) if blocks else _clean_inline_spacing(main_content.get_text())
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    output_file.write_text(text, encoding="utf-8")
    print(f"Successfully denoised {input_file.name} to {output_file.name}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 denoise_html.py <input_html_file> <output_md_file>")
        sys.exit(0 if len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help") else 1)
    denoise_html(Path(sys.argv[1]), Path(sys.argv[2]))
