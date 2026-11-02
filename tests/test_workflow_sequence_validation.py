from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = ROOT / "scripts" / "validate_discovery_profile_workflow.py"


def load_validation_module():
    spec = importlib.util.spec_from_file_location("validation", VALIDATION_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load validate_discovery_profile_workflow.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorkflowSequenceValidationTests(unittest.TestCase):
    """Regression tests for the sequence-order validator (closes the P0-5 blind spot).

    These tests encode the two exact failure modes the reorder introduced:
      - P0-1: physical stage list order diverges from the next-chain order.
      - P0-3: a chain stage is omitted from AGENTS.md.
    """

    def setUp(self) -> None:
        self.module = load_validation_module()
        with open(ROOT / "config" / "workflow-spec.yaml", encoding="utf-8") as f:
            self.spec = yaml.safe_load(f)
        self.agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    def test_current_config_is_consistent(self) -> None:
        """The real, fixed config must pass both checks."""
        failures = self.module.validate_workflow_sequence(self.spec, self.agents_md)
        self.assertEqual(failures, [], f"Unexpected sequence failures: {failures}")

    def test_detects_physical_order_mismatch(self) -> None:
        """P0-1: moving a chain stage out of chain order in the physical list is caught."""
        tampered = copy.deepcopy(self.spec)
        stages = tampered["stages"]
        intent = next(s for s in stages if s.get("name") == "article-intent-research")
        stages.remove(intent)
        # Insert it physically after article-benchmark (wrong: chain says before benchmark).
        idx = next(i for i, s in enumerate(stages) if s.get("name") == "article-benchmark")
        stages.insert(idx + 1, intent)
        failures = self.module.validate_workflow_sequence(tampered, self.agents_md)
        self.assertTrue(
            any("physical stage order does not match" in f for f in failures),
            f"Expected physical-order mismatch detection, got: {failures}",
        )

    def test_detects_undocumented_chain_stage(self) -> None:
        """P0-3: a chain stage missing from AGENTS.md is caught."""
        tampered_agents = self.agents_md.replace("/article-intent-research", "/article-intent-research-REMOVED")
        failures = self.module.validate_workflow_sequence(self.spec, tampered_agents)
        self.assertTrue(
            any("article-intent-research" in f and "AGENTS.md" in f for f in failures),
            f"Expected undocumented-stage detection, got: {failures}",
        )


if __name__ == "__main__":
    unittest.main()
