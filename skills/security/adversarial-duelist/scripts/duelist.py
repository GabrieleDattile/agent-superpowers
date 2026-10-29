#!/usr/bin/env python3
"""
Adversarial Duelist: Automated Fuzzing & Red-Team Audit Engine
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
import argparse
import importlib.util
import inspect
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Universal Adversarial Payloads
MALICIOUS_PAYLOADS = {
    "null_byte": "\x00admin",
    "buffer_overflow_sim": "A" * 10000,
    "sql_injection_sim": "' OR '1'='1' --",
    "unicode_rtl": "\u202Ereversed_payload",
    "zero_division_candidate": 0,
    "negative_boundary": -1,
    "max_int_boundary": 2**63 - 1,
    "float_nan": float("nan"),
    "float_inf": float("inf"),
    "empty_collection": [],
    "none_pointer": None,
}

def load_function(filepath: str, func_name: str):
    path = Path(filepath).resolve()
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, func_name):
        raise AttributeError(f"Function '{func_name}' not found in {filepath}")
    return getattr(module, func_name)

def get_default_value(param: inspect.Parameter):
    if param.annotation == int:
        return 1
    elif param.annotation == float:
        return 1.0
    elif param.annotation == bool:
        return False
    elif param.annotation == list:
        return []
    elif param.annotation == dict:
        return {}
    return "test_val"

def duel(func):
    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    console.print(f"[bold red]⚔️  Adversarial Duelist:[/] Attacking function `[yellow]{func.__name__}({', '.join(p.name for p in params)})[/]`...")

    results = []
    crashes = 0

    defaults = [get_default_value(p) for p in params]

    for p_idx, param in enumerate(params):
        for payload_name, payload_val in MALICIOUS_PAYLOADS.items():
            test_args = list(defaults)
            test_args[p_idx] = payload_val
            test_label = f"{param.name} = {payload_name}"

            try:
                func(*test_args)
                results.append((test_label, "SURVIVED (Handled)", "green"))
            except ValueError as e:
                # Explicit validation error
                results.append((test_label, f"GUARDED (ValueError)", "yellow"))
            except Exception as e:
                # Ungraceful crash / unhandled failure
                crashes += 1
                results.append((test_label, f"CRASH: {type(e).__name__}: {str(e)[:35]}", "bold red"))

    return results, crashes

def main():
    parser = argparse.ArgumentParser(description="Adversarial Duelist: Automated Red-Team Engine")
    parser.add_argument("--target", required=True, help="Target Python file")
    parser.add_argument("--func", required=True, help="Function name to attack")
    args = parser.parse_args()

    try:
        target_fn = load_function(args.target, args.func)
    except Exception as e:
        console.print(f"[red]Error loading target:[/] {e}")
        sys.exit(1)

    results, crashes = duel(target_fn)

    table = Table(title=f"Red-Team Audit: {args.func}", show_lines=True)
    table.add_column("Attack Vector", style="cyan")
    table.add_column("Outcome", style="white")

    for attack, outcome, color in results:
        table.add_row(attack, f"[{color}]{outcome}[/]")

    console.print(table)

    if crashes > 0:
        console.print(Panel(
            f"[bold red]❌ DEFENSE FAILED: {crashes} attack vector(s) caused unhandled crashes![/]\n"
            f"Harden input validation or type guards before allowing this code to merge.",
            title="Red-Team Vulnerabilities Detected",
            border_style="red"
        ))
        sys.exit(1)
    else:
        console.print(Panel(
            "[bold green]✔ DEFENSE PASSED: Target survived all adversarial vectors gracefully.[/]",
            title="Audit Approved",
            border_style="green"
        ))
        sys.exit(0)

if __name__ == "__main__":
    main()
