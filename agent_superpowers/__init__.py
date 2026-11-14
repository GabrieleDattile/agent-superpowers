"""Agent Superpowers Python package and bundled asset resolver."""

from __future__ import annotations

import importlib.util
from pathlib import Path

__version__ = "1.2.0"

_PACKAGE_DIR = Path(__file__).resolve().parent


def get_bundle_root() -> Path:
    """Return the root directory holding skills, CLI, and MCP scripts."""
    bundled = _PACKAGE_DIR / "_bundle"
    if (bundled / "skills").is_dir():
        return bundled
    return _PACKAGE_DIR.parent


def run_bundled_main(relative_script: str, module_alias: str) -> None:
    """Load a bundled Python script cleanly by path and invoke its main()."""
    script_path = get_bundle_root() / relative_script
    spec = importlib.util.spec_from_file_location(module_alias, str(script_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not locate bundled script at {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()
