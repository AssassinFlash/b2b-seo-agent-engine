#!/usr/bin/env python3
"""Probe Alibaba product media with Chrome cookies kept in memory only.

This helper never prints or stores cookie values. It reports whether the URL is
readable and returns source-backed media URL candidates for operator review.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.request
from http.cookiejar import Cookie, CookieJar
from urllib.parse import urlparse


IMAGE_RE = re.compile(
    r"(?:https?:)?//[^\s\"'<>]+(?:alicdn|alibaba)[^\s\"'<>]+?"
    r"\.(?:jpg|jpeg|png|webp)(?:_[^\"'<>\\s]+)?",
    re.I,
)
VIDEO_RE = re.compile(
    r"(?:https?:)?//[^\s\"'<>]+videocdn\.alibaba\.com/[^\s\"'<>]+?"
    r"\.mp4[^\s\"'<>]*",
    re.I,
)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def normalize_media_url(url: str) -> str:
    cleaned = html.unescape(url).strip().rstrip("),;")
    if cleaned.startswith("//"):
        cleaned = "https:" + cleaned
    cleaned = cleaned.replace(".jpg.jpg", ".jpg")
    cleaned = cleaned.replace(".jpeg.jpeg", ".jpeg")
    cleaned = cleaned.replace(".png.png", ".png")
    return cleaned


def unique_urls(urls: list[str], limit: int) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for url in urls:
        normalized = normalize_media_url(url)
        if normalized in seen:
            continue
        seen.add(normalized)
        out.append(normalized)
        if len(out) >= limit:
            break
    return out


def marker_flags(text: str) -> dict[str, bool]:
    return {
        "has_login_marker": bool(
            re.search(r"Account:\s*\nPassword:|Forgot password|Create account|Sign in with:", text, re.I)
        ),
        "has_antibot_marker": bool(
            re.search(r"bxpunish|captcha|verify|robot|security|____tmd____", text, re.I)
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Alibaba product URL to probe")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    domains = [
        "alibaba.com",
        ".alibaba.com",
        "www.alibaba.com",
        "login.alibaba.com",
        "alicdn.com",
        ".alicdn.com",
    ]

    cookies = []
    try:
        import rookiepy  # type: ignore

        cookies = rookiepy.chrome(domains)
    except Exception:
        cookies = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Referer": "https://www.alibaba.com/",
    }

    try:
        import requests  # type: ignore

        session = requests.Session()
        for cookie in cookies:
            name = cookie.get("name")
            value = cookie.get("value")
            if not name or value is None:
                continue
            session.cookies.set(
                name,
                value,
                domain=cookie.get("domain") or ".alibaba.com",
                path=cookie.get("path") or "/",
            )
        response = session.get(args.url, headers=headers, allow_redirects=True, timeout=25)
        status_code = response.status_code
        final_url = response.url
        text = response.text or ""
    except ImportError:
        jar = CookieJar()
        for cookie in cookies:
            name = cookie.get("name")
            value = cookie.get("value")
            if not name or value is None:
                continue
            dom = cookie.get("domain") or ".alibaba.com"
            jar.set_cookie(
                Cookie(
                    version=0,
                    name=name,
                    value=value,
                    port=None,
                    port_specified=False,
                    domain=dom,
                    domain_specified=True,
                    domain_initial_dot=dom.startswith("."),
                    path=cookie.get("path") or "/",
                    path_specified=True,
                    secure=False,
                    expires=None,
                    discard=True,
                    comment=None,
                    comment_url=None,
                    rest={},
                )
            )
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
        req = urllib.request.Request(args.url, headers=headers)
        with opener.open(req, timeout=25) as resp:
            status_code = resp.getcode() or 200
            final_url = resp.geturl()
            text = resp.read().decode("utf-8", errors="replace")

    title_match = TITLE_RE.search(text)
    title = html.unescape(re.sub(r"\s+", " ", title_match.group(1)).strip()) if title_match else ""

    image_urls = unique_urls(IMAGE_RE.findall(text), args.limit)
    video_urls = unique_urls(VIDEO_RE.findall(text), min(args.limit, 10))

    result = {
        "url": args.url,
        "status": status_code,
        "final_url": final_url,
        "final_host": urlparse(final_url).netloc,
        "body_length": len(text),
        "cookie_count": len(cookies),
        "title": title,
        **marker_flags(text),
        "image_count": len(image_urls),
        "video_count": len(video_urls),
        "images": image_urls,
        "videos": video_urls,
        "cookie_values_printed": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
