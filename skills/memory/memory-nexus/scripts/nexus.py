#!/usr/bin/env python3
"""
Memory Nexus: Cross-Session Architecture & Context Ledger CLI
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import json
import time
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

LEDGER_DIR = Path(".superpowers")
LEDGER_FILE = LEDGER_DIR / "decisions.jsonl"

def record_decision(decision: str, rationale: str, author: str = "Agent"):
    LEDGER_DIR.mkdir(exist_ok=True)
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "epoch": time.time(),
        "decision": decision,
        "rationale": rationale,
        "author": author
    }
    with open(LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    console.print(Panel(
        f"[bold green]✔ DECISION RECORDED INTO MEMORY NEXUS[/]\n\n"
        f"[bold white]Decision:[/] {decision}\n"
        f"[bold cyan]Rationale:[/] {rationale}\n"
        f"[dim]Saved to {LEDGER_FILE}[/]",
        title="Cross-Session Memory",
        border_style="green"
    ))

def read_ledger():
    if not LEDGER_FILE.exists():
        console.print("[dim yellow]No prior decisions recorded in Memory Nexus. Starting fresh session.[/]")
        return

    table = Table(title="🧠 Memory Nexus: Architectural Decision Ledger", show_lines=True)
    table.add_column("Timestamp", style="dim")
    table.add_column("Decision", style="bold white")
    table.add_column("Rationale", style="cyan")

    count = 0
    with open(LEDGER_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line)
                    table.add_row(data.get("timestamp", ""), data.get("decision", ""), data.get("rationale", ""))
                    count += 1
                except Exception:
                    pass

    if count > 0:
        console.print(table)
    else:
        console.print("[dim]Memory ledger is currently empty.[/]")

def query_ledger(topic: str):
    if not LEDGER_FILE.exists():
        console.print("[dim yellow]No decisions found.[/]")
        return

    matches = []
    with open(LEDGER_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line)
                    text = (data.get("decision", "") + " " + data.get("rationale", "")).lower()
                    if topic.lower() in text:
                        matches.append(data)
                except Exception:
                    pass

    console.print(Panel(
        f"Found [bold green]{len(matches)}[/] decisions matching topic: [yellow]{topic}[/]",
        title="Query Results"
    ))
    for m in matches:
        console.print(f"- [bold white]{m['decision']}[/] ([dim]{m['timestamp']}[/]): {m['rationale']}")

def main():
    parser = argparse.ArgumentParser(description="Memory Nexus: Cross-Session Decision Ledger")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rec = sub.add_parser("record")
    p_rec.add_argument("--decision", required=True, help="Architectural choice made")
    p_rec.add_argument("--rationale", required=True, help="Reason or trade-off justification")
    p_rec.add_argument("--author", default="Agent", help="Entity making the decision")

    sub.add_parser("read")

    p_qry = sub.add_parser("query")
    p_qry.add_argument("--topic", required=True, help="Keyword or topic to search")

    args = parser.parse_args()

    if args.cmd == "record":
        record_decision(args.decision, args.rationale, args.author)
    elif args.cmd == "read":
        read_ledger()
    elif args.cmd == "query":
        query_ledger(args.topic)

if __name__ == "__main__":
    main()
