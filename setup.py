"""Setuptools build extension that stages skills, CLI, and MCP assets inside the wheel."""

from __future__ import annotations

import shutil
from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py

ROOT = Path(__file__).resolve().parent

EXCLUDED_VIDEO_SHOTCRAFT_DIRS = (
    "assets",
    "demos",
    "gallery",
    "template",
    "workbench",
)


def _should_skip(rel_parts: tuple[str, ...], name: str) -> bool:
    if name in ("__pycache__", ".pytest_cache", ".DS_Store") or name.endswith((".pyc", ".pyo")):
        return True
    if len(rel_parts) >= 4 and rel_parts[:3] == ("skills", "multimedia", "video-shotcraft"):
        return rel_parts[3] in EXCLUDED_VIDEO_SHOTCRAFT_DIRS
    return False


def _copy_tree_filtered(src_dir: Path, dst_dir: Path) -> None:
    for item in src_dir.rglob("*"):
        if not item.is_file():
            continue
        rel = item.relative_to(ROOT)
        if _should_skip(rel.parts, item.name):
            continue
        target = dst_dir / item.relative_to(src_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)


class BuildPyWithBundle(build_py):
    """Copy non-Python skill libraries, installers, and dashboard into agent_superpowers/_bundle."""

    def run(self) -> None:
        super().run()
        bundle_root = Path(self.build_lib) / "agent_superpowers" / "_bundle"
        if bundle_root.exists():
            shutil.rmtree(bundle_root)
        bundle_root.mkdir(parents=True, exist_ok=True)

        for folder in ("cli", "mcp", "dashboard", "skills"):
            src = ROOT / folder
            if src.is_dir():
                _copy_tree_filtered(src, bundle_root / folder)

        for filename in ("install.sh", "install.ps1", "LICENSE"):
            src_file = ROOT / filename
            if src_file.is_file():
                shutil.copy2(src_file, bundle_root / filename)


setup(cmdclass={"build_py": BuildPyWithBundle})
