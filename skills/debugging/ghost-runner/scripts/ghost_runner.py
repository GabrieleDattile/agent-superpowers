#!/usr/bin/env python3
"""
Ghost-Runner: Automated Test-Driven Bug Reproducer CLI
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
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_test(test_cmd: str):
    """Executes the test command and captures output and exit code."""
    result = subprocess.run(test_cmd, shell=True, capture_output=True, text=True)
    return {
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "passed": result.returncode == 0
    }

def main():
    parser = argparse.ArgumentParser(description="Ghost-Runner: Test-Driven Bug Reproducer")
    parser.add_argument("mode", choices=["reproduce", "verify"], help="Mode: 'reproduce' (expects FAIL) or 'verify' (expects PASS)")
    parser.add_argument("--test", required=True, help="Command to run the reproduction test")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    console.print(f"[bold cyan]🔬 Ghost-Runner:[/] Executing `{args.test}` in [yellow]{args.mode.upper()}[/] mode...")
    res = run_test(args.test)

    if args.mode == "reproduce":
        if not res["passed"]:
            # Success: It failed as expected!
            if not args.json:
                console.print(Panel(
                    f"[bold green]✔ REPRODUCTION SUCCESSFUL (RED CONFIRMED)[/]\n"
                    f"Exit code: {res['exit_code']}\n\n"
                    f"[dim]Output excerpt:[/]\n{res['stderr'][-300:] or res['stdout'][-300:]}",
                    title="Phase 1: Proof of Defect",
                    border_style="green"
                ))
            else:
                print(json.dumps({"status": "SUCCESS_RED", "details": res}))
            sys.exit(0)
        else:
            if not args.json:
                console.print(Panel(
                    "[bold red]❌ INVALID REPRODUCTION: Test PASSED unexpectedly.[/]\n"
                    "The test did not trigger the bug. Ghost-Runner strictly prohibits patching until a red test is achieved.",
                    title="Phase 1 Failed",
                    border_style="red"
                ))
            else:
                print(json.dumps({"status": "FAILED_MUST_BE_RED", "details": res}))
            sys.exit(1)

    elif args.mode == "verify":
        if res["passed"]:
            if not args.json:
                console.print(Panel(
                    f"[bold green]✔ VERIFICATION SUCCESSFUL (GREEN CONFIRMED)[/]\n"
                    f"The surgical fix successfully resolved the reproduction test!",
                    title="Phase 2: Fix Verified",
                    border_style="green"
                ))
            else:
                print(json.dumps({"status": "SUCCESS_GREEN", "details": res}))
            sys.exit(0)
        else:
            if not args.json:
                console.print(Panel(
                    f"[bold red]❌ VERIFICATION FAILED: Test is still FAILING.[/]\n\n"
                    f"{res['stderr'][-300:] or res['stdout'][-300:]}",
                    title="Fix Incomplete",
                    border_style="red"
                ))
            else:
                print(json.dumps({"status": "FAILED_STILL_RED", "details": res}))
            sys.exit(1)

if __name__ == "__main__":
    main()
