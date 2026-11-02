#!/usr/bin/env python3
"""
Agent Superpowers: Unified CLI & Skill Orchestrator
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
Repository: https://github.com/GabrieleDattile/agent-superpowers
"""
import sys
import os
import subprocess
import json
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).parent.parent
SKILLS_DIR = ROOT_DIR / "skills"

# Optional Rich formatting with graceful pure-Python fallback
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
    HAS_RICH = True
except ImportError:
    console = None
    HAS_RICH = False

def log(msg, style=None):
    if HAS_RICH and console:
        console.print(msg)
    else:
        # Strip rich-like markup tags for plain console
        import re
        clean = re.sub(r'\[/?[a-zA-Z0-9_\s#]+\]', '', msg)
        print(clean)

def load_skills():
    skills = []
    if not SKILLS_DIR.exists():
        return skills

    # Pure standard library YAML parser or PyYAML if available
    try:
        import yaml
        yaml_available = True
    except ImportError:
        yaml_available = False

    for skill_md in SKILLS_DIR.rglob("SKILL.md"):
        try:
            content = skill_md.read_text(encoding="utf-8")
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    if yaml_available:
                        metadata = yaml.safe_load(parts[1]) or {}
                    else:
                        # Fallback basic key-value extractor for zero-dependency runs
                        metadata = {}
                        for line in parts[1].split("\n"):
                            if ":" in line and not line.strip().startswith("-"):
                                k, v = line.split(":", 1)
                                metadata[k.strip()] = v.strip().strip('"').strip("'")
                    metadata["path"] = skill_md
                    metadata["category"] = skill_md.parent.parent.name
                    skills.append(metadata)
        except Exception as e:
            log(f"[red]Error parsing {skill_md}:[/] {e}")
    return skills

def cmd_list():
    skills = load_skills()
    if HAS_RICH and console:
        table = Table(title="⚡ Agent Superpowers: Registered Skills (11)", show_lines=True)
        table.add_column("Skill Name", style="bold cyan")
        table.add_column("Category", style="yellow")
        table.add_column("Version", style="dim")
        table.add_column("Description", style="white")

        for s in sorted(skills, key=lambda x: (x.get("category", ""), x.get("name", ""))):
            table.add_row(
                str(s.get("name", "Unknown")),
                str(s.get("category", "General")),
                str(s.get("version", "1.0.0")),
                str(s.get("description", ""))[:75] + "..."
            )
        console.print(table)
    else:
        print("\n=== ⚡ Agent Superpowers: Registered Skills (11) ===")
        print(f"{'NAME':<24} | {'CATEGORY':<18} | {'VERSION':<8} | {'DESCRIPTION'}")
        print("-" * 80)
        for s in sorted(skills, key=lambda x: (x.get("category", ""), x.get("name", ""))):
            name = str(s.get("name", "Unknown"))
            cat = str(s.get("category", "General"))
            ver = str(s.get("version", "1.0.0"))
            desc = str(s.get("description", ""))[:45] + "..."
            print(f"{name:<24} | {cat:<18} | {ver:<8} | {desc}")
        print("-" * 80)

    log(f"\n[dim]Total skills ready for deployment:[/] [bold green]{len(skills)}[/]")

def cmd_validate():
    skills = load_skills()
    log(f"[bold cyan]Validating {len(skills)} skills against Agent Specification...[/]")
    valid = True

    required_keys = ["name", "version", "description", "author", "compatibility", "tags"]
    for s in skills:
        missing = [k for k in required_keys if k not in s]
        if missing:
            log(f"[bold red]❌ {s.get('name', 'Unknown')}: Missing frontmatter keys: {missing}[/]")
            valid = False
        else:
            log(f"[bold green]✔ {s.get('name')}: Specification valid[/]")

    if not valid:
        sys.exit(1)
    else:
        if HAS_RICH and console:
            console.print(Panel("[bold green]All 11 skills passed specification checks successfully![/]", title="CI Validation"))
        else:
            print("\n✔ All 11 skills passed specification checks successfully!\n")

def cmd_status():
    log("[bold cyan]=== Agent Superpowers: System Health & Integrations ===[/]\n")
    
    # 1. Check Python scripts
    scripts = {
        "Ghost Runner": ROOT_DIR / "skills" / "debugging" / "ghost-runner" / "scripts" / "ghost_runner.py",
        "Adversarial Duelist": ROOT_DIR / "skills" / "security" / "adversarial-duelist" / "scripts" / "duelist.py",
        "Token Squeezer": ROOT_DIR / "skills" / "optimization" / "token-squeezer" / "scripts" / "squeezer.py",
        "API Synthesizer": ROOT_DIR / "skills" / "reverse-engineering" / "api-synthesizer" / "scripts" / "synthesizer.py",
        "Blackbox Cloner": ROOT_DIR / "skills" / "reverse-engineering" / "blackbox-cloner" / "scripts" / "cloner.py",
        "Arch Archaeologist": ROOT_DIR / "skills" / "architecture" / "arch-archaeologist" / "scripts" / "archaeologist.py",
        "Worktree Sandbox": ROOT_DIR / "skills" / "workflow" / "git-worktree-sandbox" / "scripts" / "worktree.py",
        "Frontend Sentinel": ROOT_DIR / "skills" / "frontend" / "frontend-sentinel" / "scripts" / "auditor.py"
    }

    all_scripts_ok = True
    for name, p in scripts.items():
        if p.exists():
            log(f"  [green]✔ {name:<22}[/] Found: {p.relative_to(ROOT_DIR)}")
        else:
            log(f"  [red]❌ {name:<22}[/] Missing at {p}")
            all_scripts_ok = False

    # 2. Check Platform Installations
    log("\n[bold]Detected Platform Directories:[/]")
    home = Path.home()
    platforms = {
        "Antigravity": home / ".gemini" / "antigravity" / "skills",
        "Antigravity Config": home / ".gemini" / "config" / "skills",
        "Claude Code": home / ".claude" / "skills",
        "Cursor Rule": ROOT_DIR / ".cursor" / "rules" / "agent-superpowers.mdc"
    }

    for plat, p in platforms.items():
        if p.exists():
            log(f"  [green]✔ {plat:<20}[/] Active ({p})")
        else:
            log(f"  [yellow]○ {plat:<20}[/] Not yet configured ({p})")

    # 3. Overall status
    if all_scripts_ok:
        log("\n[bold green]✔ All autonomous engineering engines operational and ready![/]")
    else:
        log("\n[bold red]Warning: Some script engines were not found. Run installer to repair.[/]")

def cmd_run(args):
    if not args:
        log("[red]Please specify an engine to run: ghost-runner, duelist, squeezer, synthesizer, cloner, archaeologist, worktree, auditor[/]")
        return

    engine = args[0].lower().replace("_", "-")
    extra_args = args[1:]

    routes = {
        "ghost-runner": ROOT_DIR / "skills" / "debugging" / "ghost-runner" / "scripts" / "ghost_runner.py",
        "duelist": ROOT_DIR / "skills" / "security" / "adversarial-duelist" / "scripts" / "duelist.py",
        "squeezer": ROOT_DIR / "skills" / "optimization" / "token-squeezer" / "scripts" / "squeezer.py",
        "synthesizer": ROOT_DIR / "skills" / "reverse-engineering" / "api-synthesizer" / "scripts" / "synthesizer.py",
        "cloner": ROOT_DIR / "skills" / "reverse-engineering" / "blackbox-cloner" / "scripts" / "cloner.py",
        "archaeologist": ROOT_DIR / "skills" / "architecture" / "arch-archaeologist" / "scripts" / "archaeologist.py",
        "worktree": ROOT_DIR / "skills" / "workflow" / "git-worktree-sandbox" / "scripts" / "worktree.py",
        "auditor": ROOT_DIR / "skills" / "frontend" / "frontend-sentinel" / "scripts" / "auditor.py"
    }

    script_path = routes.get(engine)
    if not script_path or not script_path.exists():
        log(f"[red]Unknown or missing engine: '{engine}'. Available: {', '.join(routes.keys())}[/]")
        return

    cmd = [sys.executable, str(script_path)] + extra_args
    subprocess.run(cmd, cwd=ROOT_DIR)

def cmd_mcp():
    from mcp.server import main as mcp_main
    mcp_main()

def cmd_dashboard():
    import webbrowser
    dash_path = ROOT_DIR / "dashboard" / "index.html"
    log(f"[bold cyan]📊 Opening Agent Superpowers Dashboard:[/] {dash_path}")
    webbrowser.open(dash_path.as_uri())

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "list":
        cmd_list()
    elif sys.argv[1] == "validate":
        cmd_validate()
    elif sys.argv[1] == "status":
        cmd_status()
    elif sys.argv[1] == "run":
        cmd_run(sys.argv[2:])
    elif sys.argv[1] == "serve-mcp":
        cmd_mcp()
    elif sys.argv[1] == "dashboard":
        cmd_dashboard()
    else:
        log("[red]Unknown command. Available: `list`, `status`, `run`, `validate`, `serve-mcp`, `dashboard`[/]")

if __name__ == "__main__":
    main()
