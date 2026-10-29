#!/usr/bin/env python3
"""
Git Worktree Sandbox: Automated Workspace Isolation CLI
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import subprocess
import argparse
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

WORKTREE_BASE = Path(".worktrees")

def run_cmd(cmd: str):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res

def create_worktree(name: str):
    branch = f"sandbox/{name}"
    target_dir = WORKTREE_BASE / name
    WORKTREE_BASE.mkdir(exist_ok=True)

    console.print(f"[bold cyan]📦 Git Worktree Sandbox:[/] Creating isolated sandbox `[yellow]{target_dir}[/]` on branch `[green]{branch}[/]`...")

    # Create worktree
    res = run_cmd(f"git worktree add -b {branch} {target_dir}")
    if res.returncode != 0:
        # If branch already exists
        res = run_cmd(f"git worktree add {target_dir} {branch}")
        if res.returncode != 0:
            console.print(f"[bold red]Failed to create worktree:[/] {res.stderr}")
            sys.exit(1)

    console.print(Panel(
        f"[bold green]✔ WORKTREE SANDBOX CREATED[/]\n\n"
        f"Path: {target_dir.resolve()}\n"
        f"Branch: {branch}\n\n"
        f"[dim]The agent must now perform all operations inside this directory.[/]",
        title="Environment Isolated",
        border_style="green"
    ))

def merge_worktree(name: str):
    branch = f"sandbox/{name}"
    target_dir = WORKTREE_BASE / name

    console.print(f"[bold cyan]📦 Git Worktree Sandbox:[/] Merging `[yellow]{branch}[/]` into current branch...")

    # First remove worktree
    run_cmd(f"git worktree remove {target_dir} --force")
    if target_dir.exists():
        shutil.rmtree(target_dir, ignore_errors=True)

    # Merge branch
    res = run_cmd(f"git merge {branch} --no-ff -m 'feat: merge {branch} from sandbox worktree'")
    if res.returncode != 0:
        console.print(f"[bold red]Merge conflicts or error:[/] {res.stderr}")
        sys.exit(1)

    # Delete sandbox branch
    run_cmd(f"git branch -d {branch}")

    console.print(Panel(
        f"[bold green]✔ SANDBOX MERGED & CLEANED UP[/]\n"
        f"Branch `{branch}` cleanly integrated into current HEAD.",
        title="Sandbox Closed",
        border_style="green"
    ))

def discard_worktree(name: str):
    branch = f"sandbox/{name}"
    target_dir = WORKTREE_BASE / name

    console.print(f"[bold yellow]📦 Git Worktree Sandbox:[/] Discarding `[red]{target_dir}[/]`...")
    run_cmd(f"git worktree remove {target_dir} --force")
    if target_dir.exists():
        shutil.rmtree(target_dir, ignore_errors=True)
    run_cmd(f"git branch -D {branch}")
    console.print(f"[green]✔ Worktree {target_dir} discarded and removed.[/]")

def list_worktrees():
    res = run_cmd("git worktree list")
    console.print(Panel(res.stdout or "No active worktrees", title="Active Worktrees"))

def main():
    parser = argparse.ArgumentParser(description="Git Worktree Sandbox Isolation")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create")
    p_create.add_argument("name", help="Name of the sandbox task")

    p_merge = sub.add_parser("merge")
    p_merge.add_argument("name", help="Name of the sandbox task")

    p_discard = sub.add_parser("discard")
    p_discard.add_argument("name", help="Name of the sandbox task")

    sub.add_parser("list")

    args = parser.parse_args()

    if args.cmd == "create":
        create_worktree(args.name)
    elif args.cmd == "merge":
        merge_worktree(args.name)
    elif args.cmd == "discard":
        discard_worktree(args.name)
    elif args.cmd == "list":
        list_worktrees()

if __name__ == "__main__":
    main()
