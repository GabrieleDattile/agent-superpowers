"""Console entrypoint for the `superpowers` and `agent-superpowers` commands."""

from __future__ import annotations

from agent_superpowers import run_bundled_main


def main() -> None:
    """Run the Agent Superpowers unified CLI."""
    run_bundled_main("cli/superpowers.py", "_agent_superpowers_cli")


if __name__ == "__main__":
    main()
