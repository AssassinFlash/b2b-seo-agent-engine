from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError:
    jsonschema = None


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_STATUS_PATH = ROOT / "scripts" / "workflow_status.py"
VALIDATION_PATH = ROOT / "scripts" / "validate_discovery_profile_workflow.py"


def load_workflow_status_module():
    spec = importlib.util.spec_from_file_location("workflow_status", WORKFLOW_STATUS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load workflow_status.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorkflowStatusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "content-workspace").mkdir()
        (self.root / "config").mkdir()
        schema_src = ROOT / "config" / "state-schema.json"
        if schema_src.exists():
            (self.root / "config" / "state-schema.json").write_text(
                schema_src.read_text(encoding="utf-8"), encoding="utf-8"
            )
        self.workflow_status = load_workflow_status_module()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_json(self, path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def touch(self, path: Path, text: str = "ok") -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_no_projects_recommends_profile_discover(self) -> None:
        status = self.workflow_status.build_status(root=self.root)

        self.assertEqual(status["nextSafeCommand"]["command"], "/profile-discover")
        self.assertIn("No project workspace found", status["blockingIssues"])
        self.assertIn("Current Position", self.workflow_status.render_markdown(status))

    def test_multiple_projects_asks_for_project_path(self) -> None:
        (self.root / "content-workspace" / "alpha").mkdir()
        (self.root / "content-workspace" / "beta").mkdir()

        status = self.workflow_status.build_status(root=self.root)

        self.assertEqual(status["nextSafeCommand"]["command"], "/workflow-status content-workspace/<project-slug>")
        self.assertEqual(status["projectCandidates"], ["alpha", "beta"])

    def test_draft_profile_stays_in_profile_commands(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        self.touch(project / "project-profile.draft.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "draft",
                "lockedProfile": False,
                "currentStage": "profile-discover",
                "nextCommand": "/profile-answer",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": None,
            },
        )

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertFalse(status["lockedProfile"])
        self.assertEqual(status["nextSafeCommand"]["command"], "/profile-answer content-workspace/metal-screens")
        self.assertIn("Profile is not locked", status["blockingIssues"])

    def test_topic_card_before_lock_recommends_research_deep(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.draft.md")
        self.touch(article / "topic-card.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "draft",
                "lockedProfile": False,
                "currentStage": "article-cluster",
                "nextCommand": "/profile-research-deep",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertEqual(status["nextSafeCommand"]["command"], "/profile-research-deep content-workspace/metal-screens")
        self.assertIn("Profile is not locked", status["blockingIssues"])

    def test_article_after_benchmark_recommends_extract(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-benchmark",
                "nextCommand": "/article-benchmark-extract",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        for name in [
            "topic-card.md",
            "intent-research.md",
            "content-type-library.md",
            "benchmark-candidates.md",
        ]:
            self.touch(article / name)

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertEqual(status["selectedArticle"], "how-to-buy-metal-screens")
        self.assertEqual(
            status["nextSafeCommand"]["command"],
            "/article-benchmark-extract content-workspace/metal-screens how-to-buy-metal-screens",
        )
        self.assertIn("benchmark-success-formula.md", "\n".join(status["blockingIssues"]))

    def test_article_after_lock_recommends_intent_research(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.touch(article / "topic-card.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "profile-lock",
                "nextCommand": "/article-intent-research",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertEqual(
            status["nextSafeCommand"]["command"],
            "/article-intent-research content-workspace/metal-screens how-to-buy-metal-screens",
        )
        self.assertIn("intent-research.md", "\n".join(status["blockingIssues"]))

    def test_legacy_article_with_skeleton_skips_intent_and_benchmark(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.touch(article / "topic-card.md")
        self.touch(article / "skeleton.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-skeleton",
                "nextCommand": "/article-arc",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertEqual(
            status["nextSafeCommand"]["command"],
            "/article-benchmark-extract content-workspace/metal-screens how-to-buy-metal-screens",
        )
        self.assertNotIn("intent-research.md", "\n".join(status["blockingIssues"]))
        self.assertNotIn("content-type-library.md", "\n".join(status["blockingIssues"]))

    def test_qa_block_recommends_repair(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-benchmark-qa",
                "nextCommand": "/article-reader-qa",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        for name in [
            "topic-card.md",
            "intent-research.md",
            "content-type-library.md",
            "benchmark-candidates.md",
            "benchmark-success-formula.md",
            "benchmark-asset-ledger.md",
            "evidence-opinion-pack.md",
            "skeleton.md",
            "narrative-arc.md",
            "draft.md",
            "truth-qa.md",
            "information-gain-qa.md",
        ]:
            self.touch(article / name)
        self.touch(article / "benchmark-drift-audit.md", "Status: BLOCK\nForced FAQ damaged benchmark rhythm.")

        status = self.workflow_status.build_status("content-workspace/metal-screens", root=self.root)

        self.assertEqual(
            status["nextSafeCommand"]["command"],
            "/article-repair content-workspace/metal-screens how-to-buy-metal-screens",
        )
        self.assertIn("benchmark-drift-audit.md is blocking", "\n".join(status["blockingIssues"]))

    def test_workflow_next_locks_on_qa_block(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        
        # Touch preceding files to avoid missing artifact blocks
        self.touch(article / "topic-card.md")
        self.touch(article / "intent-research.md")
        self.touch(article / "content-type-library.md")
        self.touch(article / "benchmark-candidates.md")
        self.touch(article / "benchmark-success-formula.md")
        self.touch(article / "benchmark-asset-ledger.md")
        self.touch(article / "evidence-opinion-pack.md")
        self.touch(article / "skeleton.md")
        self.touch(article / "narrative-arc.md")
        self.touch(article / "draft.md")
        
        # QA is blocked
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-truth-qa",
                "nextCommand": "/article-information-gain-qa",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        self.touch(article / "truth-qa.md", "Status: BLOCK\nFake fact detected.")
        
        argv = [str(project), "--next", "--root", str(self.root)]
        self.workflow_status.main(argv)
        
        with open(project / "state.json", "r") as f:
            state = json.load(f)
        self.assertEqual(state["nextCommand"], "/article-repair")

    def test_workflow_rollback_cleans_downstream(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.touch(article / "draft.md")
        self.touch(article / "truth-qa.md")
        
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-truth-qa",
                "nextCommand": "/article-information-gain-qa",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        
        argv = [str(project), "--rollback", "Draft", "--root", str(self.root)]
        self.workflow_status.main(argv)
        
        with open(project / "state.json", "r") as f:
            state = json.load(f)
        self.assertEqual(state["currentStage"], "article-draft")
        self.assertEqual(state["nextCommand"], "/article-truth-qa")
        # truth-qa.md should be deleted because it is downstream of Draft
        self.assertFalse((article / "truth-qa.md").exists())
        # draft.md should be preserved because it is the target stage artifact
        self.assertTrue((article / "draft.md").exists())

    def test_workflow_status_fails_on_corrupted_state(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        self.touch(project / "project-profile.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "draft",
                # missing "lockedProfile" key
                "currentStage": "profile-discover",
                "nextCommand": "/profile-answer",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
            },
        )
        
        argv = [str(project), "--root", str(self.root)]
        exit_code = self.workflow_status.main(argv)
        self.assertEqual(exit_code, 2)

    def test_workflow_rollback_resets_profile_and_locked_state(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.touch(article / "topic-card.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-benchmark",
                "nextCommand": "/article-benchmark-extract",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        argv = [str(project), "--rollback", "profile-discover", "--root", str(self.root)]
        self.workflow_status.main(argv)
        
        with open(project / "state.json", "r") as f:
            state = json.load(f)
        self.assertFalse(state["lockedProfile"])
        self.assertEqual(state["profileStatus"], "draft")
        self.assertEqual(state["currentStage"], "profile-discover")
        self.assertFalse((project / "project-profile.md").exists())
        self.assertFalse((project / "project-profile.json").exists())
        self.assertFalse((project / "topic-cluster.md").exists())

    def test_workflow_rollback_rejects_forward_jump_and_cleans_research(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        self.touch(project / "project-profile.draft.md")
        self.touch(project / "project-profile.research.md")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "researched",
                "lockedProfile": False,
                "currentStage": "profile-research-deep",
                "nextCommand": "/profile-lock",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
                "articles": [{"slug": "how-to-buy-metal-screens", "status": "topic-card", "currentStage": "article-cluster"}],
            },
        )
        # Forward rollback must be rejected
        code_fwd = self.workflow_status.main([str(project), "--rollback", "article-draft", "--root", str(self.root)])
        self.assertEqual(code_fwd, 2)

        # Rollback to article-cluster (idx 2 < 3) must clean project-profile.research.md and set profileStatus=draft
        code_ok = self.workflow_status.main([str(project), "--rollback", "article-cluster", "--root", str(self.root)])
        self.assertEqual(code_ok, 0)
        self.assertFalse((project / "project-profile.research.md").exists())
        with open(project / "state.json", "r") as f:
            st = json.load(f)
        self.assertEqual(st["profileStatus"], "draft")
        self.assertEqual(st["articles"][0]["currentStage"], "article-cluster")

    def test_workflow_next_blocks_on_unfilled_qa_template(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        for f in ["project-profile.md", "topic-cluster.md"]:
            self.touch(project / f)
        self.touch(project / "project-profile.json", "{}")
        for f in [
            "topic-card.md",
            "intent-research.md",
            "content-type-library.md",
            "benchmark-candidates.md",
            "benchmark-success-formula.md",
            "benchmark-asset-ledger.md",
            "evidence-opinion-pack.md",
            "skeleton.md",
            "narrative-arc.md",
            "draft.md",
        ]:
            self.touch(article / f)
        self.touch(article / "truth-qa.md", "# Truth QA\n\n**Status:** `PASS | PASS with watchlist | BLOCK`\n")
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-truth-qa",
                "nextCommand": "/article-information-gain-qa",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        code = self.workflow_status.main([str(project), "how-to-buy-metal-screens", "--next", "--root", str(self.root)])
        self.assertEqual(code, 2)

    def test_workflow_next_advances_through_visual_resources_faq(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        for f in [
            "topic-card.md",
            "intent-research.md",
            "content-type-library.md",
            "benchmark-candidates.md",
            "benchmark-success-formula.md",
            "benchmark-asset-ledger.md",
            "evidence-opinion-pack.md",
            "skeleton.md",
            "narrative-arc.md",
            "draft.md",
            "truth-qa.md",
            "information-gain-qa.md",
            "benchmark-drift-audit.md",
            "reader-qa.md",
            "enriched-draft.md",
            "image-plan.md",
            "visual-spec.md",
            "resources.md",
            "faq.md",
            "publish-package.md",
            "keyword-record.csv",
        ]:
            self.touch(article / f)
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-enrich",
                "nextCommand": "/article-visual",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        for expected_stage, expected_next in [
            ("article-visual", "/article-resources"),
            ("article-resources", "/article-faq"),
            ("article-faq", "/article-publish-pack"),
            ("article-publish-pack", "/article-review"),
        ]:
            code = self.workflow_status.main([str(project), "--next", "--root", str(self.root)])
            self.assertEqual(code, 0)
            state = json.loads((project / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["currentStage"], expected_stage)
            self.assertEqual(state["nextCommand"], expected_next)

    def test_workflow_rollback_cleans_extract_evidence_and_post_enrich_files(self) -> None:
        project = self.root / "content-workspace" / "metal-screens"
        article = project / "articles" / "how-to-buy-metal-screens"
        self.touch(project / "project-profile.md")
        self.touch(project / "project-profile.json", "{}")
        self.touch(project / "topic-cluster.md")
        self.touch(article / "benchmark-candidates.md")
        for downstream in [
            "benchmark-success-formula.md",
            "benchmark-asset-ledger.md",
            "evidence-opinion-pack.md",
            "information-gain-qa.md",
            "visual-spec.md",
            "resources.md",
            "faq.md",
            "publish-package.md",
        ]:
            self.touch(article / downstream)
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "metal-screens",
                "profileStatus": "locked",
                "lockedProfile": True,
                "currentStage": "article-publish-pack",
                "nextCommand": "/article-review",
                "lastUpdated": "2026-05-21T10:00:00+08:00",
                "activeArticle": "how-to-buy-metal-screens",
            },
        )
        code = self.workflow_status.main([str(project), "--rollback", "article-benchmark", "--root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertTrue((article / "benchmark-candidates.md").exists())
        for downstream in [
            "benchmark-success-formula.md",
            "benchmark-asset-ledger.md",
            "evidence-opinion-pack.md",
            "information-gain-qa.md",
            "visual-spec.md",
            "resources.md",
            "faq.md",
            "publish-package.md",
        ]:
            self.assertFalse((article / downstream).exists(), f"{downstream} was not cleaned on rollback")

    def test_workflow_next_blocks_missing_profile_files_and_missing_article_dir(self) -> None:
        project = self.root / "content-workspace" / "empty-proj"
        project.mkdir(parents=True)
        self.write_json(
            project / "state.json",
            {
                "projectSlug": "empty-proj",
                "profileStatus": "draft",
                "lockedProfile": False,
                "currentStage": "profile-discover",
                "nextCommand": "/profile-answer",
                "activeArticle": "nonexistent-article",
                "lastUpdated": "2026-06-17T00:00:00",
            },
        )
        # Missing project-profile.draft.md must block --next at profile-discover
        code1 = self.workflow_status.main([str(project), "--next", "--root", str(self.root)])
        self.assertEqual(code1, 2)

        # Even if project-profile.draft.md and topic-cluster.md exist, missing articles/<slug> dir must block at article-cluster
        self.touch(project / "project-profile.draft.md")
        self.touch(project / "topic-cluster.md")
        st = json.loads((project / "state.json").read_text(encoding="utf-8"))
        st["currentStage"] = "article-cluster"
        self.write_json(project / "state.json", st)
        code2 = self.workflow_status.main([str(project), "--next", "--root", str(self.root)])
        self.assertEqual(code2, 2)

        # Status: TBD in truth-qa.md must be treated as "todo" by qa_status
        art = project / "articles" / "nonexistent-article"
        self.touch(art / "truth-qa.md", "# Truth QA\n\nStatus: TBD\n")
        qa = self.workflow_status.qa_status(art)
        self.assertEqual(qa["Truth QA"]["status"], "todo")


class SpecValidationTests(unittest.TestCase):
    def test_specs_are_loadable(self) -> None:
        with open(ROOT / "config" / "workflow-spec.yaml", encoding="utf-8") as f:
            spec = yaml.safe_load(f)
        with open(ROOT / "config" / "artifact-graph.yaml", encoding="utf-8") as f:
            graph = yaml.safe_load(f)
        with open(ROOT / "config" / "state-schema.json", encoding="utf-8") as f:
            schema = json.load(f)

        self.assertIn("stages", spec)
        self.assertIn("stages", graph)
        self.assertIn("required", schema)

    def test_example_state_matches_schema(self) -> None:
        schema_path = ROOT / "config" / "state-schema.json"
        with open(ROOT / "content-workspace" / "example-metal-divider" / "state.json", encoding="utf-8") as f:
            state = json.load(f)

        ws = load_workflow_status_module()
        self.assertIsNone(ws.validate_state(state, schema_path))
        # Also verify stdlib validator catches invalid enum/pattern/oneOf/nested status
        bad_enum = dict(state, profileStatus="INVALID_ENUM")
        self.assertIsNotNone(ws._validate_schema_node(bad_enum, json.loads(schema_path.read_text(encoding="utf-8"))))
        bad_pattern = dict(state, lastUpdated="not-a-date")
        self.assertIsNotNone(ws._validate_schema_node(bad_pattern, json.loads(schema_path.read_text(encoding="utf-8"))))

    def test_validation_script_passes(self) -> None:
        result = subprocess.run(
            ["python3", str(VALIDATION_PATH)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"Validation script failed:\n{result.stdout}\n{result.stderr}",
        )
        self.assertIn("Validation passed.", result.stdout)


if __name__ == "__main__":
    unittest.main()
