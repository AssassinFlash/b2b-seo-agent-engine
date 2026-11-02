"""Tests for scripts/validate_topic_cluster.py"""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_topic_cluster import validate_topic_cluster


def _sample_card() -> str:
    return (
        "<details>\n<summary><strong>1. Example Topic</strong></summary>\n\n"
        "- **Seed Keyword:** example\n"
        "- **Primary Keyword:** example keyword\n"
        "- **Long-tail Keywords:** a, b\n"
        "- **User Search Intent:** Informational\n"
        "- **Monthly Search Volume:** 100\n"
        "- **Traffic Potential:** Low\n"
        "- **Keyword Variations / LSI Terms:** x, y\n"
        "- **SERP Top 5 Snapshot:** Blogs\n"
        "- **Dominant Content Formats:** Guide\n"
        "- **Gaps & Opportunities:** None\n"
        "- **Persona Fit:** High\n"
        "- **Replication Feasibility:** High\n"
        "- **Opportunity Score:** 5.0\n"
        "</details>\n\n"
        "- [x] Tier 1\n"
    )


def test_missing_topic_cluster():
    with tempfile.TemporaryDirectory() as tmp:
        failures = validate_topic_cluster(Path(tmp), min_cards=1)
        assert any("Missing" in f for f in failures)


def test_min_cards_enforced():
    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / "topic-cluster.md").write_text(_sample_card(), encoding="utf-8")
        failures = validate_topic_cluster(workspace, min_cards=2)
        assert any("Expected at least 2" in f for f in failures)


def test_valid_topic_cluster():
    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / "topic-cluster.md").write_text(_sample_card(), encoding="utf-8")
        failures = validate_topic_cluster(workspace, min_cards=1)
        assert not failures


def test_missing_fields_reported():
    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / "topic-cluster.md").write_text(
            "<details>\n<summary><strong>1. Example Topic</strong></summary>\n\n"
            "- **Seed Keyword:** example\n"
            "- **Primary Keyword:** example keyword\n"
            "- **Opportunity Score:** 5.0\n"
            "</details>\n",
            encoding="utf-8",
        )
        failures = validate_topic_cluster(workspace, min_cards=1)
        assert any("missing fields" in f for f in failures)


def test_serp_cannibalization_detected():
    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        workspace.mkdir(parents=True, exist_ok=True)
        shared_serp = "https://a.com/1 https://b.com/2 https://c.com/3 https://d.com/4 https://e.com/5"
        card1 = _sample_card().replace("Blogs", shared_serp)
        card2 = (
            _sample_card()
            .replace("1. Example Topic", "2. Duplicate Intent Topic")
            .replace("Blogs", "https://a.com/1 https://b.com/2 https://c.com/3 https://d.com/4 https://f.com/6")
        )
        (workspace / "topic-cluster.md").write_text(card1 + "\n" + card2, encoding="utf-8")
        failures = validate_topic_cluster(workspace, min_cards=2)
        assert any("SERP Cannibalization" in f for f in failures)

        # Shared URLs outside SERP Top 5 Snapshot (e.g. in Gaps & Opportunities) must NOT trigger false cannibalization
        card3 = _sample_card().replace("None", shared_serp)
        card4 = (
            _sample_card()
            .replace("1. Example Topic", "2. Distinct Topic")
            .replace("None", shared_serp)
            .replace("- **Persona Fit:** High", "- **Persona Fit (Buying Committee: Specifier + Approver):** High")
        )
        (workspace / "topic-cluster.md").write_text(card3 + "\n" + card4, encoding="utf-8")
        failures2 = validate_topic_cluster(workspace, min_cards=2)
        assert not failures2


class ValidateTopicClusterTestCase(unittest.TestCase):
    def test_all(self):
        test_missing_topic_cluster()
        test_min_cards_enforced()
        test_valid_topic_cluster()
        test_missing_fields_reported()
        test_serp_cannibalization_detected()


