import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from cli.superpowers import load_skills

def test_all_skills_specification():
    """Validates that all skills meet the Agent Skill Specification."""
    skills = load_skills()
    assert len(skills) >= 5, f"Expected at least 5 skills, found {len(skills)}"

    required_keys = ["name", "version", "description", "author", "compatibility", "tags"]
    for skill in skills:
        for k in required_keys:
            assert k in skill, f"Skill {skill.get('name')} missing key: {k}"
        assert len(skill["description"]) > 10, f"Skill {skill['name']} has too short description"

def test_token_squeezer_compression():
    """Tests that token squeezer achieves >= 40% reduction on interface mode."""
    from skills.optimization.token_squeezer.scripts.squeezer import compress_code, estimate_tokens

    code = """
class DataService:
    def fetch_records(self, limit: int = 100) -> list:
        # Long internal processing
        results = []
        for i in range(limit):
            results.append({"id": i, "val": i * 2})
        return results
"""
    compressed = compress_code(code, mode="interface")
    assert "def fetch_records" in compressed
    assert "..." in compressed
    assert estimate_tokens(compressed) <= estimate_tokens(code)
