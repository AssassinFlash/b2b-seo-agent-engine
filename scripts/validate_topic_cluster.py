#!/usr/bin/env python3
"""Validate a topic-cluster.md against the project candidate-card contract.

Usage:
    python3 scripts/validate_topic_cluster.py content-workspace/<project-slug> [--min-cards 50]

Checks:
    - topic-cluster.md exists
    - contains at least --min-cards candidate cards
    - each card includes required bullet fields
    - at least one Tier 1 topic exists
    - warns if the file appears to be backfilled after /profile-lock
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_CARD_FIELDS = [
    "Seed Keyword",
    "Primary Keyword",
    "Long-tail Keywords",
    "User Search Intent",
    "Monthly Search Volume",
    "Traffic Potential",
    "Keyword Variations / LSI Terms",
    "SERP Top 5 Snapshot",
    "Dominant Content Formats",
    "Gaps & Opportunities",
    "Persona Fit",
    "Replication Feasibility",
    "Opportunity Score",
]


def find_cards(text: str) -> list[dict]:
    """Split topic-cluster.md into candidate topic blocks.

    Cards are detected by <details> blocks whose summary contains a numbered
    topic title, typically:
        <summary><strong>1. Solar Without a Battery ...</strong></summary>
    """
    cards: list[dict] = []
    details_pattern = re.compile(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", re.DOTALL | re.IGNORECASE)
    for m in details_pattern.finditer(text):
        summary = m.group(1)
        body = m.group(2)
        if re.search(r"^\s*(?:<strong>)?\d+\.", summary):
            cards.append({"summary": summary.strip(), "text": body})
    return cards


def check_card_fields(card_text: str) -> list[str]:
    """Return missing required bullet fields for a single card."""
    missing = []
    for field in REQUIRED_CARD_FIELDS:
        if not re.search(rf"^\s*-\s*\*?\*{re.escape(field)}(?:\s*\([^)\n]*\))?\*?\*?:", card_text, re.MULTILINE):
            missing.append(field)
    return missing


def extract_serp_urls(card_text: str) -> set[str]:
    """Extract normalized HTTP(S) URLs appearing inside the SERP Top 5 Snapshot block."""
    serp_block_match = re.search(
        r"^\s*-\s*\*?\*SERP Top 5 Snapshot\*?\*?:[ \t]*(.*?)(?=^\s*-\s*\*?\*[A-Z]|\Z)",
        card_text,
        flags=re.MULTILINE | re.DOTALL,
    )
    target_text = serp_block_match.group(1) if serp_block_match else ""
    urls = set()
    for match in re.findall(r"https?://[^\s\)\]>\"']+", target_text):
        cleaned = match.rstrip(".,;:").lower().rstrip("/")
        urls.add(cleaned)
    return urls


def check_serp_cannibalization(cards: list[dict]) -> list[str]:
    """Flag pairs of cards that share >60% of their explicitly listed SERP URLs (min 3 URLs)."""
    warnings: list[str] = []
    card_urls = [(idx, card["summary"][:50], extract_serp_urls(card["text"])) for idx, card in enumerate(cards, 1)]
    for i in range(len(card_urls)):
        idx_a, sum_a, urls_a = card_urls[i]
        if len(urls_a) < 3:
            continue
        for j in range(i + 1, len(card_urls)):
            idx_b, sum_b, urls_b = card_urls[j]
            if len(urls_b) < 3:
                continue
            overlap = len(urls_a & urls_b) / min(len(urls_a), len(urls_b))
            if overlap > 0.6:
                warnings.append(
                    f"SERP Cannibalization (>60% URL overlap: {overlap:.0%}) between Card {idx_a} ({sum_a}) and Card {idx_b} ({sum_b}); merge into one Deep SEO Card."
                )
    return warnings


def validate_topic_cluster(workspace: Path, min_cards: int = 50) -> list[str]:
    failures: list[str] = []
    workspace = Path(workspace)
    if not workspace.is_absolute() and not workspace.exists():
        candidate_ws = ROOT / workspace
        if candidate_ws.exists():
            workspace = candidate_ws
    topic_cluster = workspace / "topic-cluster.md"

    if not topic_cluster.exists():
        try:
            failures.append(f"Missing {topic_cluster.relative_to(ROOT)}")
        except ValueError:
            failures.append(f"Missing {topic_cluster}")
        return failures

    text = topic_cluster.read_text(encoding="utf-8")

    if "backfilled" in text.lower() and "profile-lock" in text.lower():
        try:
            rel = topic_cluster.relative_to(ROOT)
        except ValueError:
            rel = topic_cluster
        failures.append(
            f"{rel} appears to be backfilled after /profile-lock; "
            "run /article-cluster before /profile-lock in future projects"
        )

    cards = find_cards(text)
    if len(cards) < min_cards:
        failures.append(
            f"Expected at least {min_cards} candidate cards, found {len(cards)}. "
            "Expand the topic pool or pass --min-cards to approve a smaller shortlist."
        )

    tier_1_count = len(re.findall(r"Tier 1|\[x\]\s*Tier 1", text, re.IGNORECASE))
    if tier_1_count == 0:
        failures.append("No Tier 1 topics found")

    for i, card in enumerate(cards, start=1):
        card_text = card["text"]
        missing = check_card_fields(card_text)
        if missing:
            failures.append(f"Card {i} ({card['summary'][:60]}) is missing fields: {', '.join(missing)}")

    failures.extend(check_serp_cannibalization(cards))

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a topic-cluster.md")
    parser.add_argument("workspace", type=Path, help="Project workspace path (e.g., content-workspace/sunriver-inverter)")
    parser.add_argument("--min-cards", type=int, default=50, help="Minimum number of candidate cards")
    args = parser.parse_args()

    raw_ws = args.workspace.expanduser()
    if not raw_ws.is_absolute() and not raw_ws.exists() and (ROOT / raw_ws).exists():
        raw_ws = ROOT / raw_ws
    workspace = raw_ws.resolve()
    failures = validate_topic_cluster(workspace, min_cards=args.min_cards)

    if failures:
        print(f"Topic cluster validation failed for {workspace.name}:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"Topic cluster validation passed for {workspace.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
