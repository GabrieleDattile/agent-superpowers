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
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent

def _load_module(module_name: str, rel_path: str):
    """Dynamically load Python module from path containing hyphens or special chars."""
    file_path = ROOT / rel_path
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module specification from {file_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

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
    },
    {
        "name": "frontend_sentinel",
        "description": "Audits React, Vue, and HTML templates for accessibility defects, mobile viewport breaks, and hydration hazards.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Path to file or folder to audit"},
                "html_report": {"type": "string", "description": "Optional output path for HTML report"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "blackbox_cloner",
        "description": "Clean-room reverse engineering engine. Deconstructs proprietary tools and SaaS widgets into independent open-source specs and scaffolds.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["deconstruct", "scaffold"], "description": "'deconstruct' analyzes architecture, 'scaffold' builds clean-room prototype"},
                "tool_name": {"type": "string", "description": "Name or concept of tool to replicate"},
                "category": {"type": "string", "enum": ["graphics", "vector", "utility"], "default": "graphics"}
            },
            "required": ["action", "tool_name"]
        }
    },
    {
        "name": "hallmark_sloplint",
        "description": "Anti-AI-slop design auditor. Scans HTML, JSX, TSX, Svelte, and Vue files for generic AI tells (purple gradients, predictable 3-card grids, unanchored blur orbs, corporate buzzwords).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Path to file or directory to scan", "default": "."},
                "fail_under": {"type": "integer", "description": "Slop score failure threshold (default: 25)", "default": 25}
            }
        }
    }
]

def handle_call_tool(name: str, args: dict):
    try:
        if name == "ghost_runner":
            cmd = f'python skills/debugging/ghost-runner/scripts/ghost_runner.py {args["mode"]} --test "{args["test_cmd"]}" --json'
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
            return res.stdout or res.stderr

        elif name == "adversarial_duelist":
            cmd = f'python skills/security/adversarial-duelist/scripts/duelist.py --target "{args["target_file"]}" --func "{args["function_name"]}"'
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
            return res.stdout or res.stderr

        elif name == "token_squeezer":
            squeezer_mod = _load_module("squeezer", "skills/optimization/token-squeezer/scripts/squeezer.py")
            p = Path(args["file_path"])
            orig = p.read_text(encoding="utf-8")
            compressed = squeezer_mod.compress_code(orig, mode=args.get("mode", "interface"))
            return f"Original: ~{squeezer_mod.estimate_tokens(orig)} tokens | Compressed: ~{squeezer_mod.estimate_tokens(compressed)} tokens\n\n{compressed}"

        elif name == "api_synthesizer":
            synth_mod = _load_module("synthesizer", "skills/reverse-engineering/api-synthesizer/scripts/synthesizer.py")
            parsed = synth_mod.parse_curl(args["curl_command"])
            return synth_mod.generate_sdk(parsed, client_name=args.get("client_name", "ApiClient"))

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

        elif name == "frontend_sentinel":
            path = args["path"]
            rep = f'--html-report "{args["html_report"]}"' if args.get("html_report") else ""
            cmd = f'python skills/frontend/frontend-sentinel/scripts/auditor.py --path "{path}" {rep}'.strip()
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
            return res.stdout or res.stderr

        elif name == "blackbox_cloner":
            action = args["action"]
            tool_name = args["tool_name"]
            cat = args.get("category", "graphics")
            if action == "deconstruct":
                cmd = f'python skills/reverse-engineering/blackbox-cloner/scripts/cloner.py deconstruct --tool "{tool_name}" --category "{cat}"'
            else:
                cmd = f'python skills/reverse-engineering/blackbox-cloner/scripts/cloner.py scaffold --tool "{tool_name}"'
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
            return res.stdout or res.stderr

        elif name == "hallmark_sloplint":
            target = args.get("target", ".")
            fail_under = args.get("fail_under", 25)
            cmd = f'python skills/frontend/hallmark/scripts/sloplint.py "{target}" --json --fail-under {fail_under}'
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
            return res.stdout or res.stderr

        return "Unknown tool"
    except Exception as e:
        return {
            "content": [{"type": "text", "text": f"Error executing tool {name}: {str(e)}"}],
            "isError": True
        }

def _write_response(payload: dict) -> None:
    """Write a single JSON-RPC 2.0 message to stdout and flush."""
    sys.stdout.write(json.dumps(payload) + "\n")
    sys.stdout.flush()


def main():
    """Stdio JSON-RPC loop for Model Context Protocol."""
    static_results = {
        "ping": {},
        "prompts/list": {"prompts": []},
        "resources/list": {"resources": []},
        "resources/templates/list": {"resourceTemplates": []},
    }

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
            _write_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "agent-superpowers", "version": "1.2.0"},
                    "capabilities": {"tools": {}}
                }
            })

        elif method and method.startswith("notifications/"):
            pass

        elif method == "tools/list":
            _write_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": TOOLS}
            })

        elif method in static_results:
            _write_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": static_results[method]
            })

        elif method == "tools/call":
            params = msg.get("params", {})
            name = params.get("name")
            arguments = params.get("arguments", {})
            try:
                res = handle_call_tool(name, arguments)
                if isinstance(res, dict) and "content" in res:
                    result = res
                else:
                    result = {
                        "content": [{"type": "text", "text": str(res)}],
                        "isError": False
                    }
            except Exception as e:
                result = {
                    "content": [{"type": "text", "text": f"Error executing tool {name}: {str(e)}"}],
                    "isError": True
                }
            _write_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": result
            })

        elif req_id is not None:
            _write_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}
            })

if __name__ == "__main__":
    main()
