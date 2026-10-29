#!/usr/bin/env python3
"""
Agent Superpowers: Unified CLI & Skill Orchestrator
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from pathlib import Path
import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

ROOT_DIR = Path(__file__).parent.parent
SKILLS_DIR = ROOT_DIR / "skills"

def load_skills():
    skills = []
    if not SKILLS_DIR.exists():
        return skills

    for skill_md in SKILLS_DIR.rglob("SKILL.md"):
        content = skill_md.read_text(encoding="utf-8")
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    metadata["path"] = skill_md
                    metadata["category"] = skill_md.parent.parent.name
                    skills.append(metadata)
            except Exception as e:
                console.print(f"[red]Error parsing {skill_md}:[/] {e}")
    return skills

def cmd_list():
    skills = load_skills()
    table = Table(title="⚡ Agent Superpowers: Registered Skills", show_lines=True)
    table.add_column("Skill Name", style="bold cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Version", style="dim")
    table.add_column("Description", style="white")

    for s in sorted(skills, key=lambda x: (x.get("category", ""), x.get("name", ""))):
        table.add_row(
            s.get("name", "Unknown"),
            s.get("category", "General"),
            s.get("version", "1.0.0"),
            s.get("description", "")[:80] + "..."
        )

    console.print(table)
    console.print(f"[dim]Total skills ready for deployment:[/] [bold green]{len(skills)}[/]")

def cmd_validate():
    skills = load_skills()
    console.print(f"[bold cyan]Validating {len(skills)} skills against Agent Specification...[/]")
    valid = True

    required_keys = ["name", "version", "description", "author", "compatibility", "tags"]
    for s in skills:
        missing = [k for k in required_keys if k not in s]
        if missing:
            console.print(f"[bold red]❌ {s.get('name', 'Unknown')}: Missing frontmatter keys: {missing}[/]")
            valid = False
        else:
            console.print(f"[bold green]✔ {s.get('name')}: Specification valid[/]")

    if not valid:
        sys.exit(1)
    else:
        console.print(Panel("[bold green]All skills passed specification checks successfully![/]", title="CI Validation"))

def cmd_mcp():
    from mcp.server import main as mcp_main
    mcp_main()

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "list":
        cmd_list()
    elif sys.argv[1] == "validate":
        cmd_validate()
    elif sys.argv[1] == "serve-mcp":
        cmd_mcp()
    else:
        console.print("[red]Unknown command. Available: `list`, `validate`, `serve-mcp`[/]")

if __name__ == "__main__":
    main()
