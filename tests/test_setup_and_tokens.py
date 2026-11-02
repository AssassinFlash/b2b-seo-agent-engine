import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import apify_research  # noqa: E402
import setup_env  # noqa: E402


class SetupAndTokenPoolTestCase(unittest.TestCase):
    def test_persistent_token_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            local_env = tmp_path / ".env.apify.local"
            global_env = tmp_path / ".config" / "b2b-seo-agent" / "apify.env"
            legacy_env = tmp_path / ".config" / "b2b-seo-agent" / "apify.env"

            with (
                mock.patch.object(apify_research, "LOCAL_ENV_PATH", local_env),
                mock.patch.object(apify_research, "GLOBAL_ENV_PATH", global_env),
                mock.patch.object(apify_research, "LEGACY_GLOBAL_ENV_PATH", legacy_env),
            ):
                # 1. Initial set-tokens (--no-verify)
                rc = apify_research.main(
                    ["set-tokens", "apify_api_TokenAlpha123456", "apify_api_TokenBeta654321", "--no-verify"]
                )
                self.assertEqual(rc, 0)
                self.assertTrue(local_env.exists())
                self.assertTrue(global_env.exists())
                self.assertEqual(local_env.stat().st_mode & 0o777, 0o600)
                self.assertEqual(global_env.stat().st_mode & 0o777, 0o600)

                tokens = apify_research.load_tokens()
                self.assertEqual(
                    tokens,
                    [(1, "apify_api_TokenAlpha123456"), (2, "apify_api_TokenBeta654321")],
                )

                # 2. Mid-session add-token with --prepend
                rc2 = apify_research.main(
                    ["add-token", "apify_api_TokenGamma999999", "--prepend", "--no-verify"]
                )
                self.assertEqual(rc2, 0)
                tokens2 = apify_research.load_tokens()
                self.assertEqual(
                    [t for _, t in tokens2],
                    [
                        "apify_api_TokenGamma999999",
                        "apify_api_TokenAlpha123456",
                        "apify_api_TokenBeta654321",
                    ],
                )

                # 3. Remove token by slot index
                rc3 = apify_research.main(["remove-token", "2"])
                self.assertEqual(rc3, 0)
                tokens3 = apify_research.load_tokens()
                self.assertEqual(
                    [t for _, t in tokens3],
                    ["apify_api_TokenGamma999999", "apify_api_TokenBeta654321"],
                )

    def test_workspace_init_and_doctor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            with mock.patch.object(setup_env, "ROOT", tmp_path):
                res = setup_env.init_workspace("acme-industrial")
                ws = tmp_path / "content-workspace" / "acme-industrial"
                self.assertTrue((ws / "state.json").exists())
                self.assertTrue((ws / "knowledge" / "fact-library.json").exists())
                self.assertTrue((ws / "knowledge" / "site-link-graph.json").exists())
                state = json.loads((ws / "state.json").read_text(encoding="utf-8"))
                self.assertEqual(state["projectSlug"], "acme-industrial")
                self.assertFalse(state["lockedProfile"])
                self.assertIn("/profile-discover", res["next_command"])


if __name__ == "__main__":
    unittest.main()
