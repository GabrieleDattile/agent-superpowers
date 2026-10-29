#!/usr/bin/env python3
"""
Agent Superpowers: Universal Model Context Protocol (MCP) Server
Allows Claude Desktop, Cursor, Zed, Antigravity, and OpenCode to dynamically invoke skills via MCP JSON-RPC.
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
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.parent

TOOLS = [
    {
        "name": "ghost_runner",
        "description": "Zero-assumption TDD bug reproducer. Requires test to FAIL before patching, and PASS after patching.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "mode": {"type": "string", "enum": ["reproduce", "verify"], "description": "'reproduce' expects failure, 'verify' expects success"},
                "test_cmd": {"type": "string", "description": "Shell command to run reproduction test"}
            },
            "required": ["mode", "test_cmd"]
        }
    },
    {
        "name": "adversarial_duelist",
        "description": "Offensive red-team fuzzer. Attacks a Python function with null-bytes, zero-divisions, overflow payloads, and SQLi vectors.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_file": {"type": "string", "description": "Path to Python file"},
                "function_name": {"type": "string", "description": "Name of function to attack"}
            },
            "required": ["target_file", "function_name"]
        }
    },
    {
        "name": "token_squeezer",
        "description": "AST-based context compressor. Shrinks Python source files by 50-70% by extracting structural interfaces and docstrings.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string", "description": "Path to Python file to compress"},
                "mode": {"type": "string", "enum": ["interface", "compact"], "default": "interface"}
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "api_synthesizer",
        "description": "Reverse-engineers raw cURL network traffic into a fully typed Python client SDK.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "curl_command": {"type": "string", "description": "Raw cURL string"},
                "client_name": {"type": "string", "default": "ApiClient"}
            },
            "required": ["curl_command"]
        }
    },
    {
        "name": "arch_archaeologist",
        "description": "Scans codebase AST to map module dependency graphs and detect uncalled zombie/dead functions.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dir_path": {"type": "string", "description": "Path to directory to analyze"}
            },
            "required": ["dir_path"]
        }
    },
    {
        "name": "git_worktree_sandbox",
        "description": "Creates, merges, or discards isolated git worktrees so agent experiments never corrupt main workspace.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["create", "merge", "discard", "list"]},
                "task_name": {"type": "string", "description": "Name of the sandbox task"}
            },
            "required": ["action"]
        }
    }
]

def handle_call_tool(name: str, args: dict):
    if name == "ghost_runner":
        cmd = f'python skills/debugging/ghost-runner/scripts/ghost_runner.py {args["mode"]} --test "{args["test_cmd"]}" --json'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
        return res.stdout or res.stderr

    elif name == "adversarial_duelist":
        cmd = f'python skills/security/adversarial-duelist/scripts/duelist.py --target "{args["target_file"]}" --func "{args["function_name"]}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
        return res.stdout or res.stderr

    elif name == "token_squeezer":
        from skills.optimization.token_squeezer.scripts.squeezer import compress_code, estimate_tokens
        p = Path(args["file_path"])
        orig = p.read_text(encoding="utf-8")
        compressed = compress_code(orig, mode=args.get("mode", "interface"))
        return f"Original: ~{estimate_tokens(orig)} tokens | Compressed: ~{estimate_tokens(compressed)} tokens\n\n{compressed}"

    elif name == "api_synthesizer":
        from skills.reverse_engineering.api_synthesizer.scripts.synthesizer import parse_curl, generate_sdk
        parsed = parse_curl(args["curl_command"])
        return generate_sdk(parsed, client_name=args.get("client_name", "ApiClient"))

    elif name == "arch_archaeologist":
        cmd = f'python skills/architecture/arch-archaeologist/scripts/archaeologist.py --dir "{args["dir_path"]}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
        return res.stdout or res.stderr

    elif name == "git_worktree_sandbox":
        action = args["action"]
        task = args.get("task_name", "")
        cmd = f'python skills/workflow/git-worktree-sandbox/scripts/worktree.py {action} {task}'.strip()
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
        return res.stdout or res.stderr

    return "Unknown tool"

def main():
    """Stdio JSON-RPC loop for Model Context Protocol."""
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except Exception:
            continue

        req_id = msg.get("id")
        method = msg.get("method")

        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "agent-superpowers", "version": "1.1.0"},
                    "capabilities": {"tools": {}}
                }
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

        elif method == "notifications/initialized":
            pass

        elif method == "tools/list":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": TOOLS}
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = msg.get("params", {})
            name = params.get("name")
            arguments = params.get("arguments", {})
            content = handle_call_tool(name, arguments)
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": str(content)}]
                }
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
