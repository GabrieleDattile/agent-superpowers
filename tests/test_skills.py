import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from cli.superpowers import load_skills

class TestAgentSuperpowers(unittest.TestCase):
    def test_all_skills_specification(self):
        """Validates that all skills meet the Agent Skill Specification."""
        skills = load_skills()
        self.assertGreaterEqual(len(skills), 8, f"Expected at least 8 skills, found {len(skills)}")

        required_keys = ["name", "version", "description", "author", "compatibility", "tags"]
        for skill in skills:
            for k in required_keys:
                self.assertIn(k, skill, f"Skill {skill.get('name')} missing key: {k}")
            self.assertGreater(len(skill["description"]), 10, f"Skill {skill['name']} has too short description")

    def test_token_squeezer_compression(self):
        """Tests that token squeezer achieves compression on interface mode."""
        import importlib.util
        script_path = ROOT / "skills" / "optimization" / "token-squeezer" / "scripts" / "squeezer.py"
        spec = importlib.util.spec_from_file_location("squeezer", str(script_path))
        squeezer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(squeezer)

        code = """
class DataService:
    def fetch_records(self, limit: int = 100) -> list:
        # Long internal processing
        results = []
        for i in range(limit):
            results.append({"id": i, "val": i * 2})
        return results
"""
        compressed = squeezer.compress_code(code, mode="interface")
        self.assertIn("def fetch_records", compressed)
        self.assertIn("...", compressed)
        self.assertLessEqual(squeezer.estimate_tokens(compressed), squeezer.estimate_tokens(code))

if __name__ == "__main__":
    unittest.main()
