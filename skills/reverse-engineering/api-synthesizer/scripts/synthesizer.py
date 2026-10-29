#!/usr/bin/env python3
"""
API Synthesizer: Network Traffic to Typed Python Client SDK
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
import re
import json
import shlex
import argparse
from urllib.parse import urlparse
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()

def parse_curl(curl_cmd: str):
    tokens = shlex.split(curl_cmd)
    method = "GET"
    url = ""
    headers = {}
    data = None

    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok in ("-X", "--request") and i + 1 < len(tokens):
            method = tokens[i+1].upper()
            i += 2
        elif tok in ("-H", "--header") and i + 1 < len(tokens):
            header_str = tokens[i+1]
            if ":" in header_str:
                k, v = header_str.split(":", 1)
                headers[k.strip()] = v.strip()
            i += 2
        elif tok in ("-d", "--data", "--data-raw") and i + 1 < len(tokens):
            method = "POST" if method == "GET" else method
            data = tokens[i+1]
            i += 2
        elif tok.startswith("http://") or tok.startswith("https://"):
            url = tok
            i += 1
        elif tok == "curl":
            i += 1
        else:
            i += 1

    return {"method": method, "url": url, "headers": headers, "data": data}

def generate_sdk(parsed: dict, client_name: str = "GeneratedApiClient") -> str:
    url = parsed["url"]
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    endpoint = parsed_url.path or "/"
    method = parsed["method"]
    headers = parsed["headers"]
    data = parsed["data"]

    # Filter out authorization for dynamic injection
    auth_header = None
    clean_headers = {}
    for k, v in headers.items():
        if k.lower() in ("authorization", "x-api-key"):
            auth_header = k
        else:
            clean_headers[k] = v

    default_payload = json.dumps(json.loads(data), indent=16) if (data and data.strip().startswith("{")) else "None"

    sdk_code = f'''"""
Auto-generated SDK by API Synthesizer
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import os
import requests
from typing import Dict, Any, Optional

class {client_name}:
    """Typed client for {base_url}"""

    def __init__(self, api_token: Optional[str] = None):
        self.base_url = "{base_url}"
        self.api_token = api_token or os.getenv("API_TOKEN", "")
        self.session = requests.Session()
        self.session.headers.update({json.dumps(clean_headers, indent=12)})
        if self.api_token:
            self.session.headers["{auth_header or 'Authorization'}"] = f"Bearer {{self.api_token}}"

    def execute_{method.lower()}_{endpoint.strip("/").replace("/", "_") or "root"}(self, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Auto-generated method for {method} {endpoint}"""
        url = f"{{self.base_url}}{endpoint}"
        response = self.session.request(
            method="{method}",
            url=url,
            json=payload if payload is not None else {default_payload}
        )
        response.raise_for_status()
        return response.json()
'''
    return sdk_code

def main():
    parser = argparse.ArgumentParser(description="API Synthesizer: Network to Typed SDK")
    parser.add_argument("--curl", required=True, help="Raw cURL command string")
    parser.add_argument("--name", default="ApiClient", help="Name of client class")
    parser.add_argument("--output", help="Optional output .py file path")
    args = parser.parse_args()

    parsed = parse_curl(args.curl)
    if not parsed["url"]:
        console.print("[red]Could not parse a valid URL from the cURL command.[/]")
        sys.exit(1)

    sdk = generate_sdk(parsed, client_name=args.name)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(sdk)
        console.print(f"[green]✔ SDK generated and saved to {args.output}[/]")
    else:
        console.print(Panel(
            Syntax(sdk, "python", theme="monokai", line_numbers=True),
            title=f"🔌 Generated SDK: {args.name}",
            border_style="cyan"
        ))

if __name__ == "__main__":
    main()
