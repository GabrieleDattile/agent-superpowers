#!/usr/bin/env python3
"""
Token Squeezer: AST-Based Code & Context Compressor
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
import ast
import argparse
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

class InterfaceTransformer(ast.NodeTransformer):
    """Replaces function and method bodies with ellipsis (...) while keeping signatures."""
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        # Retain docstring if present (first line only)
        doc = ast.get_docstring(node)
        body = []
        if doc:
            body.append(ast.Expr(value=ast.Constant(value=doc.strip().split("\n")[0])))
        body.append(ast.Expr(value=ast.Constant(value=Ellipsis)))
        node.body = body
        return node

    def visit_AsyncFunctionDef(self, node):
        return self.visit_FunctionDef(node)

def estimate_tokens(text: str) -> int:
    """Rough heuristic token estimator (~4 chars per token)."""
    return max(1, len(text) // 4)

def compress_code(code_str: str, mode: str = "interface") -> str:
    tree = ast.parse(code_str)
    if mode == "interface":
        transformer = InterfaceTransformer()
        tree = transformer.visit(tree)
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)
    elif mode == "compact":
        # Simply unparse standard tree to strip comments & format
        return ast.unparse(tree)
    else:
        raise ValueError(f"Unknown mode: {mode}")

def main():
    parser = argparse.ArgumentParser(description="Token Squeezer: AST-Based Context Compressor")
    parser.add_argument("--file", required=True, help="Python source file to compress")
    parser.add_argument("--mode", choices=["interface", "compact"], default="interface", help="Compression mode")
    parser.add_argument("--output", help="Optional output destination file")
    args = parser.parse_args()

    target_path = Path(args.file)
    if not target_path.exists():
        console.print(f"[red]File not found:[/] {args.file}")
        sys.exit(1)

    original_text = target_path.read_text(encoding="utf-8")
    original_tokens = estimate_tokens(original_text)

    compressed_text = compress_code(original_text, mode=args.mode)
    compressed_tokens = estimate_tokens(compressed_text)

    savings = max(0, 100 - int((compressed_tokens / original_tokens) * 100))

    if args.output:
        Path(args.output).write_text(compressed_text, encoding="utf-8")

    console.print(Panel(
        f"[bold cyan]Mode:[/] {args.mode.upper()}\n"
        f"[bold white]Original Context:[/] ~{original_tokens:,} tokens ({len(original_text):,} chars)\n"
        f"[bold green]Compressed Context:[/] ~{compressed_tokens:,} tokens ({len(compressed_text):,} chars)\n"
        f"[bold yellow]Token Savings:[/] [bold green]{savings}% REDUCTION[/]",
        title="📉 Token Squeezer Telemetry",
        border_style="green"
    ))

    # Print first lines of preview
    preview = "\n".join(compressed_text.splitlines()[:25])
    console.print(f"\n[dim]--- Compressed Context Preview ---[/]\n{preview}\n[dim]...[/]")

if __name__ == "__main__":
    main()
