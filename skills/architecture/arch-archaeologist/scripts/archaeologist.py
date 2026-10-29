#!/usr/bin/env python3
"""
Architecture Archaeologist: AST-Based Codebase Cartographer & Dead Code Detector
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
import ast
import argparse
from pathlib import Path
from typing import Dict, Set, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class CodebaseInspector:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir).resolve()
        self.modules: Dict[str, ast.AST] = {}
        self.definitions: Dict[str, Set[str]] = {} # module -> set of function names
        self.calls: Dict[str, Set[str]] = {}       # module -> set of called names
        self.imports: Dict[str, Set[str]] = {}     # module -> set of imported modules

    def scan(self):
        for path in self.root_dir.rglob("*.py"):
            if any(part.startswith(".") or part in ("venv", "env", "__pycache__", "build", "dist") for part in path.parts):
                continue
            rel_name = path.relative_to(self.root_dir).as_posix()
            try:
                content = path.read_text(encoding="utf-8")
                tree = ast.parse(content)
                self.modules[rel_name] = tree
                self._analyze_module(rel_name, tree)
            except Exception as e:
                console.print(f"[dim yellow]Skipping {rel_name}: {e}[/]")

    def _analyze_module(self, mod_name: str, tree: ast.AST):
        defs = set()
        calls = set()
        imps = set()

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                defs.add(node.name)
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.add(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    calls.add(node.func.attr)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imps.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imps.add(node.module)

        self.definitions[mod_name] = defs
        self.calls[mod_name] = calls
        self.imports[mod_name] = imps

    def find_dead_code(self) -> Dict[str, List[str]]:
        all_calls = set()
        for c in self.calls.values():
            all_calls.update(c)

        dead_functions = {}
        for mod, defs in self.definitions.items():
            dead = [d for d in defs if d not in all_calls and not d.startswith("__")]
            if dead:
                dead_functions[mod] = dead
        return dead_functions

    def generate_mermaid(self) -> str:
        lines = ["flowchart TD", "    classDef dead fill:#ff4d4f,stroke:#d9363e,color:#fff;"]
        
        # Nodes for modules
        for i, mod in enumerate(self.modules.keys()):
            node_id = f"mod_{i}"
            lines.append(f'    {node_id}["📄 {mod}"]')

        # Edges between modules based on import matching
        mod_keys = list(self.modules.keys())
        for i, mod in enumerate(mod_keys):
            for imp in self.imports.get(mod, []):
                for j, target_mod in enumerate(mod_keys):
                    if i != j and (imp in target_mod or Path(target_mod).stem == imp):
                        lines.append(f"    mod_{i} -->|imports| mod_{j}")

        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Architecture Archaeologist: Codebase Cartographer")
    parser.add_argument("--dir", default=".", help="Root directory to analyze")
    parser.add_argument("--output", help="Optional markdown output report file")
    args = parser.parse_args()

    inspector = CodebaseInspector(args.dir)
    inspector.scan()

    dead_code = inspector.find_dead_code()
    mermaid_diagram = inspector.generate_mermaid()

    console.print(Panel(
        f"[bold cyan]Scanned Modules:[/] {len(inspector.modules)}\n"
        f"[bold white]Total Functions Analyzed:[/] {sum(len(d) for d in inspector.definitions.values())}\n"
        f"[bold red]Potential Dead/Zombie Functions:[/] {sum(len(f) for f in dead_code.values())}",
        title="🗺️ Architecture Archaeologist Scan Summary",
        border_style="cyan"
    ))

    if dead_code:
        table = Table(title="Potential Dead / Zombie Functions", show_lines=True)
        table.add_column("Module File", style="yellow")
        table.add_column("Uncalled Functions", style="red")
        for mod, funcs in dead_code.items():
            table.add_row(mod, ", ".join(funcs))
        console.print(table)

    report = f"""# 🗺️ Codebase Architecture Report

## Summary
- **Analyzed Directory**: `{Path(args.dir).resolve()}`
- **Modules Found**: {len(inspector.modules)}
- **Potential Dead Functions**: {sum(len(f) for f in dead_code.values())}

## Dependency Graph
```mermaid
{mermaid_diagram}
```

## Dead Code Candidates
| Module | Unreferenced Function |
| :--- | :--- |
"""
    for mod, funcs in dead_code.items():
        for f in funcs:
            report += f"| `{mod}` | `{f}()` |\n"

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        console.print(f"[green]✔ Report saved to {args.output}[/]")

if __name__ == "__main__":
    main()
