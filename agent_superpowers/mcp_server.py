"""Console entrypoint for the Agent Superpowers stdio JSON-RPC MCP server."""

from __future__ import annotations

from agent_superpowers import run_bundled_main


def main() -> None:
    """Run the Agent Superpowers stdio MCP server."""
    run_bundled_main("mcp/server.py", "_agent_superpowers_mcp")


if __name__ == "__main__":
    main()
