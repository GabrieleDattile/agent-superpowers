#!/usr/bin/env python3
"""
Agent Superpowers: Universal 1-Click Platform Installer
Installs and configures Agent Superpowers across Claude Code, Cursor, Codex, Antigravity, and MCP.
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import os
import shutil
import argparse
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()
ROOT = Path(__file__).parent.resolve()
SKILLS_SRC = ROOT / "skills"

def install_claude():
    dest = Path.home() / ".claude" / "skills"
    dest.mkdir(parents=True, exist_ok=True)
    for skill_dir in SKILLS_SRC.rglob("SKILL.md"):
        target_name = skill_dir.parent.name
        target_dest = dest / target_name
        shutil.copytree(skill_dir.parent, target_dest, dirs_exist_ok=True)
    console.print(f"[bold green]✔ Installed into Claude Code:[/] {dest}")

def install_cursor():
    dest = Path.cwd() / ".cursor" / "rules"
    dest.mkdir(parents=True, exist_ok=True)
    rule_src = ROOT / ".cursor" / "rules" / "agent-superpowers.mdc"
    if rule_src.exists():
        shutil.copy2(rule_src, dest / "agent-superpowers.mdc")
    console.print(f"[bold green]✔ Installed into Cursor:[/] {dest}")

def install_antigravity():
    dest = Path.home() / ".gemini" / "antigravity" / "skills"
    dest.mkdir(parents=True, exist_ok=True)
    for skill_dir in SKILLS_SRC.rglob("SKILL.md"):
        target_name = skill_dir.parent.name
        target_dest = dest / target_name
        shutil.copytree(skill_dir.parent, target_dest, dirs_exist_ok=True)
    console.print(f"[bold green]✔ Installed into Antigravity:[/] {dest}")

def install_codex():
    dest = Path.cwd() / ".codex"
    dest.mkdir(parents=True, exist_ok=True)
    codex_src = ROOT / ".codex" / "INSTALL.md"
    if codex_src.exists():
        shutil.copy2(codex_src, dest / "INSTALL.md")
    console.print(f"[bold green]✔ Configured for Codex:[/] {dest}")

def main():
    parser = argparse.ArgumentParser(description="Agent Superpowers: Universal Platform Installer")
    parser.add_argument("--target", choices=["claude", "cursor", "antigravity", "codex", "all"], default="all", help="Target platform to install into")
    args = parser.parse_args()

    console.print(Panel(
        f"[bold cyan]⚡ Agent Superpowers: Universal Installer[/]\n"
        f"Targeting: [yellow]{args.target.upper()}[/]",
        title="Installer",
        border_style="cyan"
    ))

    if args.target in ("claude", "all"):
        install_claude()
    if args.target in ("cursor", "all"):
        install_cursor()
    if args.target in ("antigravity", "all"):
        install_antigravity()
    if args.target in ("codex", "all"):
        install_codex()

    console.print(Panel("[bold green]✔ Agent Superpowers successfully deployed across selected platforms![/]", title="Complete"))

if __name__ == "__main__":
    main()
