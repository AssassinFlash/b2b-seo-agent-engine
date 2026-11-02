from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
HOOK = SCRIPTS / "hooks" / "publish_gate.py"
SETTINGS = ROOT / ".claude" / "settings.json"

GATE_ARTIFACTS = ["truth-qa.md", "information-gain-qa.md", "benchmark-drift-audit.md", "reader-qa.md"]

UPSTREAM_ARTIFACTS = [
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
    "enriched-draft.md",
    "image-plan.md",
    "visual-spec.md",
    "resources.md",
    "faq.md",
]


def load_validate_publish():
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location("validate_publish", SCRIPTS / "validate_publish.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load validate_publish.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_hook(file_path: str, env: dict[str, str] | None = None) -> tuple[int, dict | None]:
    payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": file_path}})
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input=payload,
        capture_output=True,
        text=True,
        env={**os.environ, **(env or {})},
    )
    stdout = result.stdout.strip()
    return result.returncode, (json.loads(stdout) if stdout else None)


class ValidatePublishTests(unittest.TestCase):
    SLUG = "solar-without-a-battery"

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.vp = load_validate_publish()

        self.project = self.root / "content-workspace" / "sunriver-inverter"
        self.article = self.project / "articles" / self.SLUG
        self.article.mkdir(parents=True)

        for name in ("project-profile.md", "topic-cluster.md"):
            (self.project / name).write_text("ok", encoding="utf-8")
        (self.project / "project-profile.json").write_text("{}", encoding="utf-8")
        self.write_state()
        for name in UPSTREAM_ARTIFACTS:
            (self.article / name).write_text("ok", encoding="utf-8")
        for name in GATE_ARTIFACTS:
            (self.article / name).write_text("# QA Gate\n\n**Status:** PASS\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_state(self, **overrides) -> None:
        state = {
            "projectSlug": "sunriver-inverter",
            "profileStatus": "locked",
            "lockedProfile": True,
            "currentStage": "article-faq",
            "nextCommand": "/article-publish-pack",
            "lastUpdated": "2026-06-26T10:00:00Z",
        }
        state.update(overrides)
        (self.project / "state.json").write_text(json.dumps(state), encoding="utf-8")

    def run_validate(self) -> tuple[int, list]:
        return self.vp.validate("content-workspace/sunriver-inverter", self.SLUG, self.root)

    def checks(self, blockers) -> set[str]:
        return {b.check for b in blockers}

    def test_complete_article_is_publishable(self) -> None:
        code, blockers = self.run_validate()
        self.assertEqual(blockers, [])
        self.assertEqual(code, 0)

        # Adding an unresolved <!-- html-visual: hv-99 --> marker with no matching .html file must block
        (self.article / "enriched-draft.md").write_text("# Post\n\n<!-- html-visual: hv-99 missing-card -->\n", encoding="utf-8")
        code_miss, blockers_miss = self.run_validate()
        self.assertEqual(code_miss, 1)
        self.assertIn("csp:missing-html-visual", self.checks(blockers_miss))

        # Writing a substantive faq.md (>20 chars) without merging FAQ into enriched-draft.md must block
        (self.article / "enriched-draft.md").write_text("# Post\n\nPlain body with no accordion.\n", encoding="utf-8")
        (self.article / "faq.md").write_text("# FAQ\n\nQ: Does 316 rust?\nA: No.\n", encoding="utf-8")
        code_unmerged, blockers_unmerged = self.run_validate()
        self.assertEqual(code_unmerged, 1)
        self.assertIn("merge:resources-or-faq", self.checks(blockers_unmerged))

        # Relative or http:// URLs inside schema.json (including image and sameAs[]) must be rejected by validate_article_schema_json
        errs_rel_schema = self.vp.validate_article_schema_json(
            '{"@context":"https://schema.org","@graph":[{"@type":"TechArticle","@id":"/post/#article","url":"http://insecure.com/post","image":"/local.webp","sameAs":["https://ok.org","http://bad.org"]}]}'
        )
        self.assertEqual(len(errs_rel_schema), 4)

        # Malformed keyword-record.csv without a Keyword/Phrase column must be rejected
        errs_bad_csv = self.vp.validate_keyword_record_csv("ColA,ColB\nval1,val2\n")
        self.assertEqual(len(errs_bad_csv), 1)

        # Early article stages (e.g. benchmark-candidates.md) must be blocked when intent-research.md is missing
        (self.article / "intent-research.md").unlink()
        code_early, blockers_early = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "benchmark-candidates.md", self.root
        )
        self.assertEqual(code_early, 1)
        self.assertIn("prereq:intent-research.md", self.checks(blockers_early))

        # resources.md must be blocked when visual-spec.md is missing
        (self.article / "visual-spec.md").unlink()
        code_res, blockers_res = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "resources.md", self.root
        )
        self.assertEqual(code_res, 1)
        self.assertIn("prereq:visual-spec.md", self.checks(blockers_res))

        # Gate 2 (information-gain-qa.md) must be blocked when Gate 1 (truth-qa.md) is BLOCK
        (self.article / "truth-qa.md").write_text("# Truth QA\n\n**Status:** BLOCK\n", encoding="utf-8")
        code_q2, blockers_q2 = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "information-gain-qa.md", self.root
        )
        self.assertEqual(code_q2, 1)
        self.assertIn("gate-order:truth-qa.md", self.checks(blockers_q2))

        # topic-cluster.md and topic-card.md must be blocked when neither project-profile.draft.md nor project-profile.md exists
        (self.project / "project-profile.md").unlink()
        code_tc, blockers_tc = self.vp.validate_profile_lock_write(
            "content-workspace/sunriver-inverter", "topic-cluster.md", self.root
        )
        self.assertEqual(code_tc, 1)
        self.assertIn("prereq:project-profile.draft.md", self.checks(blockers_tc))
        code_card, blockers_card = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "topic-card.md", self.root
        )
        self.assertEqual(code_card, 1)
        self.assertIn("prereq:project-profile.draft.md", self.checks(blockers_card))

        # Companion/publish files (publish-ready-body.md, h2-heading-strategy.md) must also be guarded
        code_prb, blockers_prb = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "publish-ready-body.md", self.root
        )
        self.assertEqual(code_prb, 1)
        self.assertIn("profile-lock", self.checks(blockers_prb))

        # Inline Schema JSON-LD inside publish-package.md must trigger schema:separation blocker
        (self.project / "project-profile.md").write_text("ok", encoding="utf-8")
        (self.article / "truth-qa.md").write_text("# Truth QA\n\n**Status:** PASS\n", encoding="utf-8")
        (self.article / "visual-spec.md").write_text("ok", encoding="utf-8")
        (self.article / "intent-research.md").write_text("ok", encoding="utf-8")
        (self.article / "publish-package.md").write_text('# Pack\n\n```json\n{"@context": "https://schema.org"}\n```\n', encoding="utf-8")
        code_sep, blockers_sep = self.run_validate()
        self.assertEqual(code_sep, 1)
        self.assertIn("schema:separation", self.checks(blockers_sep))

    def test_real_workspaces_pass_publish_gate(self) -> None:
        code1, blockers1 = self.vp.validate(
            "content-workspace/sunriver-inverter", "solar-without-a-battery", ROOT
        )
        self.assertEqual(blockers1, [])
        self.assertEqual(code1, 0)

        code2, blockers2 = self.vp.validate(
            "content-workspace/example-metal-divider", "metal-room-divider-design-guide", ROOT
        )
        self.assertEqual(blockers2, [])
        self.assertEqual(code2, 0)

    def test_missing_reader_qa_blocks_publish(self) -> None:
        (self.article / "reader-qa.md").unlink()
        code, blockers = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("gate:reader-qa", self.checks(blockers))

    def test_missing_upstream_stage_blocks_publish(self) -> None:
        (self.article / "faq.md").unlink()
        code, blockers = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("artifacts:article-faq", self.checks(blockers))

    def test_block_verdict_blocks_publish(self) -> None:
        (self.article / "truth-qa.md").write_text("# Truth QA\n\n**Status:** BLOCK\n", encoding="utf-8")
        code, blockers = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("gate:truth-qa", self.checks(blockers))

    def test_unfilled_template_verdict_blocks_publish(self) -> None:
        (self.article / "truth-qa.md").write_text(
            "# Truth QA\n\n**Status:** `PASS | PASS with watchlist | BLOCK`\n",
            encoding="utf-8",
        )
        code, blockers = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("gate:truth-qa", self.checks(blockers))

    def test_frontmatter_verdict_is_respected(self) -> None:
        (self.article / "reader-qa.md").write_text(
            "---\ngate: reader-qa\nverdict: BLOCK\n---\n# Reader QA\n",
            encoding="utf-8",
        )
        code, blockers = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("gate:reader-qa", self.checks(blockers))

    def test_stage_write_blocks_draft_without_skeleton(self) -> None:
        (self.article / "skeleton.md").unlink()
        code, blockers = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "draft.md", self.root
        )
        self.assertEqual(code, 1)
        self.assertIn("prereq:skeleton.md", self.checks(blockers))

    def test_stage_write_blocks_enrich_when_qa_gate_blocks(self) -> None:
        (self.article / "reader-qa.md").write_text("# Reader QA\n\n**Status:** BLOCK\n", encoding="utf-8")
        code, blockers = self.vp.validate_stage_write(
            "content-workspace/sunriver-inverter", self.SLUG, "enriched-draft.md", self.root
        )
        self.assertEqual(code, 1)
        self.assertIn("gate:reader-qa", self.checks(blockers))

    def test_profile_lock_write_guards_double_lock_and_prereqs(self) -> None:
        # Already locked -> double-lock guard blocks overwriting project-profile.md
        code, blockers = self.vp.validate_profile_lock_write(
            "content-workspace/sunriver-inverter", "project-profile.md", self.root
        )
        self.assertEqual(code, 1)
        self.assertIn("profile:double-lock", self.checks(blockers))

        # When unlocked, missing project-profile.research.md blocks locking
        self.write_state(lockedProfile=False)
        code2, blockers2 = self.vp.validate_profile_lock_write(
            "content-workspace/sunriver-inverter", "project-profile.md", self.root
        )
        self.assertEqual(code2, 1)
        self.assertIn("prereq:project-profile.research.md", self.checks(blockers2))


class PublishGateHookTests(unittest.TestCase):
    def test_ordinary_files_are_allowed(self) -> None:
        code, output = run_hook(str(ROOT / "scripts" / "workflow_status.py"))
        self.assertEqual(code, 0)
        self.assertIsNone(output)

    def test_settings_registers_pre_tool_use_hook(self) -> None:
        settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
        entries = settings["hooks"]["PreToolUse"]
        matched = [e for e in entries if e["matcher"] == "Write|Edit"]
        self.assertEqual(len(matched), 1)
        self.assertIn("scripts/hooks/publish_gate.py", matched[0]["hooks"][0]["command"])

    def test_publishable_real_article_is_allowed_by_hook(self) -> None:
        target = (
            ROOT
            / "content-workspace"
            / "sunriver-inverter"
            / "articles"
            / "solar-without-a-battery"
            / "publish-package.md"
        )
        code, output = run_hook(str(target))
        self.assertEqual(code, 0)
        self.assertIsNone(output)

    def test_partial_edit_on_b2b_mod_is_allowed_while_inline_js_is_denied(self) -> None:
        enriched = (
            ROOT
            / "content-workspace"
            / "sunriver-inverter"
            / "articles"
            / "solar-without-a-battery"
            / "enriched-draft.md"
        )
        # Partial Edit changing only the opening <div class="b2b-mod-arch-strip"...> line must be allowed
        payload_ok = json.dumps(
            {
                "tool_name": "Edit",
                "tool_input": {
                    "file_path": str(enriched),
                    "old_string": '<div class="b2b-mod-arch-strip"',
                    "new_string": '<div class="b2b-mod-arch-strip" data-test="1"',
                },
            }
        )
        proc_ok = subprocess.run([sys.executable, str(HOOK)], input=payload_ok, text=True, capture_output=True, check=False)
        self.assertEqual(proc_ok.returncode, 0)
        self.assertEqual(proc_ok.stdout.strip(), "")

        # Writing a .linker-article-check snippet with onclick= to html-visuals/ must be denied
        hv_target = (
            ROOT
            / "content-workspace"
            / "sunriver-inverter"
            / "articles"
            / "solar-without-a-battery"
            / "html-visuals"
            / "hv-99.html"
        )
        payload_bad = json.dumps(
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": str(hv_target),
                    "content": '<div class="linker-article-check" onclick="evil()">Bad</div>',
                },
            }
        )
        proc_bad = subprocess.run([sys.executable, str(HOOK)], input=payload_bad, text=True, capture_output=True, check=False)
        self.assertEqual(proc_bad.returncode, 0)
        parsed = json.loads(proc_bad.stdout)
        self.assertEqual(parsed["hookSpecificOutput"]["permissionDecision"], "deny")

        # Writing schema-violating state.json must be denied by PreToolUse hook
        state_target = ROOT / "content-workspace" / "sunriver-inverter" / "state.json"
        payload_bad_state = json.dumps(
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": str(state_target),
                    "content": '{"projectSlug": "sunriver-inverter", "bogusField": 123}',
                },
            }
        )
        proc_state = subprocess.run([sys.executable, str(HOOK)], input=payload_bad_state, text=True, capture_output=True, check=False)
        self.assertEqual(proc_state.returncode, 0)
        parsed_state = json.loads(proc_state.stdout)
        self.assertEqual(parsed_state["hookSpecificOutput"]["permissionDecision"], "deny")

        # Writing invalid schema.json (missing @context or containing TBD placeholder) must be denied
        schema_target = (
            ROOT
            / "content-workspace"
            / "sunriver-inverter"
            / "articles"
            / "solar-without-a-battery"
            / "schema.json"
        )
        payload_bad_schema = json.dumps(
            {
                "tool_name": "Write",
                "tool_input": {
                    "file_path": str(schema_target),
                    "content": '{"@context": "https://schema.org", "@graph": []}',
                },
            }
        )
        proc_schema = subprocess.run([sys.executable, str(HOOK)], input=payload_bad_schema, text=True, capture_output=True, check=False)
        self.assertEqual(proc_schema.returncode, 0)
        parsed_schema = json.loads(proc_schema.stdout)
        self.assertEqual(parsed_schema["hookSpecificOutput"]["permissionDecision"], "deny")

        # Edit with a repo-relative path from an external CWD must still resolve against REPO_ROOT and deny invalid state/CSP
        with tempfile.TemporaryDirectory() as ext_cwd:
            payload_rel_edit = json.dumps(
                {
                    "tool_name": "Edit",
                    "tool_input": {
                        "file_path": "content-workspace/sunriver-inverter/state.json",
                        "old_string": '"lockedProfile": true',
                        "new_string": '"lockedProfile": "NOT_A_BOOL"',
                    },
                }
            )
            proc_rel = subprocess.run(
                [sys.executable, str(HOOK)],
                input=payload_rel_edit,
                text=True,
                capture_output=True,
                cwd=ext_cwd,
                check=False,
            )
            self.assertEqual(proc_rel.returncode, 0)
            parsed_rel = json.loads(proc_rel.stdout)
            self.assertEqual(parsed_rel["hookSpecificOutput"]["permissionDecision"], "deny")


if __name__ == "__main__":
    unittest.main()
