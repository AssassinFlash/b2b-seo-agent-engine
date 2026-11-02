import json
import tempfile
import unittest
from pathlib import Path
from scripts.sync_draft_born_claims import recommend_facts, sync_claims
from scripts.update_link_graph import update_link_graph


def test_sync_claims(tmp_path: Path):
    project_dir = tmp_path / "project"
    article_slug = "stainless-steel-screens"
    article_dir = project_dir / "articles" / article_slug
    article_dir.mkdir(parents=True, exist_ok=True)

    truth_qa_content = """
    # Truth QA Report

    ## Verified Claims
    - Standard claims

    ## Draft-born Claims
    - We achieve a tension threshold of 45 N/mm for architectural screens.
    * Real-world case: Beijing Airport T3 partition project used our AISI 316 screens.
    | Spec parameter: Wire width is 0.5mm with 80% open area.

    ## Ignored Section
    - Random claim
    """

    truth_qa_file = article_dir / "truth-qa.md"
    truth_qa_file.write_text(truth_qa_content, encoding="utf-8")

    sync_claims(project_dir, article_slug)

    fact_lib_path = project_dir / "knowledge" / "fact-library.json"
    assert fact_lib_path.exists()

    with open(fact_lib_path, "r", encoding="utf-8") as f:
        facts = json.load(f)

    assert len(facts) == 3
    assert facts[0]["claim"] == "We achieve a tension threshold of 45 N/mm for architectural screens."
    assert facts[0]["source_article"] == article_slug
    assert facts[0]["status"] == "verified_draft_born"
    assert facts[0]["used_in_articles"] == [article_slug]
    assert facts[0]["usage_count"] == 1
    assert facts[1]["claim"] == "Real-world case: Beijing Airport T3 partition project used our AISI 316 screens."
    assert facts[2]["claim"] == "Spec parameter: Wire width is 0.5mm with 80% open area."


def test_anti_footprint_usage_tracking_and_recommendation(tmp_path: Path):
    project_dir = tmp_path / "project"
    for slug, claims in [
        (
            "article-1",
            "| Claim | Evidence | Status |\n|---|---|---|\n| SAJ H2 supports 180-800V LiFePO4 | T1.1 | PASS |\n| SAJ R6 reaches 98.8% peak efficiency | T1.3 | PASS |\n",
        ),
        (
            "article-2",
            "| Claim | Evidence | Status |\n|---|---|---|\n| SAJ H2 supports 180-800V LiFePO4 | T1.1 | PASS |\n",
        ),
    ]:
        art = project_dir / "articles" / slug
        art.mkdir(parents=True, exist_ok=True)
        (art / "truth-qa.md").write_text(f"# Truth QA\n\n## Pack-Backed Claim Mapping\n\n{claims}", encoding="utf-8")
        sync_claims(project_dir, slug)

    recs = recommend_facts(project_dir)
    assert len(recs) == 2
    assert recs[0]["claim"] == "SAJ R6 reaches 98.8% peak efficiency"
    assert recs[0]["usage_count"] == 1
    assert recs[1]["claim"] == "SAJ H2 supports 180-800V LiFePO4"
    assert recs[1]["usage_count"] == 2
    assert recs[1]["used_in_articles"] == ["article-1", "article-2"]


def test_bidirectional_site_link_graph(tmp_path: Path):
    project_dir = tmp_path / "project"
    art1 = project_dir / "articles" / "hybrid-inverter-sizing"
    art2 = project_dir / "articles" / "solar-without-a-battery"
    art1.mkdir(parents=True)
    art2.mkdir(parents=True)

    (art1 / "enriched-draft.md").write_text(
        "# Hybrid Inverter Sizing Guide\n\nSee our [product line](/products/h2) for solar battery backup.",
        encoding="utf-8",
    )
    (art2 / "enriched-draft.md").write_text(
        "# Can You Run Solar Panels Without a Battery?\n\n"
        "```markdown\n[Fake Code Block Link](/do-not-count-me/)\n```\n\n"
        "Read our [sizing guide](/hybrid-inverter-sizing/ \"Sizing\") and [H2 series](/products/h2).\n"
        '<div class="b2b-mod-strip"><a href="/can-hybrid-inverter-work-without-battery/">HTML Link</a></div>\n',
        encoding="utf-8",
    )

    res = update_link_graph(project_dir, "solar-without-a-battery")
    assert res["outbound_count"] == 3

    # Also verify that section-level BLOCK verdict in truth-qa.md blocks sync_claims
    blocked_art = project_dir / "articles" / "blocked-article"
    blocked_art.mkdir(parents=True)
    (blocked_art / "truth-qa.md").write_text(
        "# Truth QA\n\n## Executive Verdict\nBLOCK\n\n## Draft-born Claims\n- Fake claim must not be synced\n",
        encoding="utf-8",
    )
    assert sync_claims(project_dir, "blocked-article") == []
    assert len(res["retro_link_recommendations"]) == 1
    retro = res["retro_link_recommendations"][0]
    assert retro["from_article"] == "hybrid-inverter-sizing"
    assert retro["to_article"] == "solar-without-a-battery"


class SyncDraftBornClaimsTestCase(unittest.TestCase):
    def test_all(self):
        with tempfile.TemporaryDirectory() as td1:
            test_sync_claims(Path(td1))
        with tempfile.TemporaryDirectory() as td2:
            test_anti_footprint_usage_tracking_and_recommendation(Path(td2))
        with tempfile.TemporaryDirectory() as td3:
            test_bidirectional_site_link_graph(Path(td3))

