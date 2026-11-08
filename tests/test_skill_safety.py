#!/usr/bin/env python3
"""Safety and routing invariants for all Open Steps skills."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "os-ask-simple", "os-check-work", "os-done-or-not",
    "os-say-simple", "os-step-by-step", "os-what-could-go-wrong",
    "os-whats-next",
}

class SkillSafetyTests(unittest.TestCase):
    def test_exactly_seven_skills(self):
        self.assertEqual({p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}, SKILLS)

    def test_headers_and_boundaries(self):
        for name in sorted(SKILLS):
            with self.subTest(skill=name):
                source = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(source.startswith("---\n"))
                self.assertEqual(source.count("\n---\n"), 1)
                header = source.split("\n---\n", 1)[0]
                self.assertIn("name: " + name, header)
                self.assertIn("description: >-", header)
                self.assertIn("allowed-tools:", header)
                self.assertIn("## Codex 6.x routing boundary", source)

    def test_no_automatic_merge_routing(self):
        routing = (ROOT / "docs" / "routing-block.md").read_text(encoding="utf-8")
        self.assertIn("Never merge a pull request unless", routing)
        self.assertIn("Never deploy or publish", routing)
        for name in SKILLS:
            self.assertIn(name, routing)

    def test_independent_verification_remains(self):
        check = (ROOT / "skills" / "os-check-work" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Never merge automatically", check)
        self.assertIn("Never accept on the strength of the report alone", check)

if __name__ == "__main__":
    unittest.main()
