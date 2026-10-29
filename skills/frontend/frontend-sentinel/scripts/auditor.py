#!/usr/bin/env python3
"""
Frontend Sentinel: Production UI/UX & Component Auditor
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
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

CHECKS = [
    {
        "id": "IMG_ALT_MISSING",
        "severity": "CRITICAL",
        "pattern": r"<img\b(?![^>]*\balt=)[^>]*>",
        "message": "Image element is missing an 'alt' attribute (fails WCAG 1.1.1).",
        "fix": "Add an alt attribute: <img src=\"...\" alt=\"Descriptive label\" />"
    },
    {
        "id": "CLICKABLE_NON_INTERACTIVE",
        "severity": "CRITICAL",
        "pattern": r"<(div|span)\b[^>]*onClick=[^>]*>",
        "message": "Non-interactive element has an onClick handler without button semantics.",
        "fix": "Use a semantic <button> or add role=\"button\" tabIndex={0} and keyboard handler."
    },
    {
        "id": "HARDCODED_PIXEL_OVERFLOW",
        "severity": "WARNING",
        "pattern": r"(w-\[[4-9]\d{2,}px\]|width:\s*[4-9]\d{2,}px)",
        "message": "Fixed container width >= 400px risks breaking mobile viewports with horizontal scroll.",
        "fix": "Use responsive max-width classes: max-w-full or w-full md:max-w-xl."
    },
    {
        "id": "ICON_BUTTON_UNLABELED",
        "severity": "WARNING",
        "pattern": r"<button\b(?![^>]*aria-label=)[^>]*>\s*<(svg|[A-Z]\w*Icon)\b",
        "message": "Icon-only button has no visible text or aria-label for screen readers.",
        "fix": "Add aria-label: <button aria-label=\"Close modal\"><CloseIcon /></button>"
    },
    {
        "id": "SSR_HYDRATION_HAZARD",
        "severity": "WARNING",
        "pattern": r"(?<!typeof\s)localStorage\.(getItem|setItem)|(?<!typeof\s)window\.(innerWidth|innerHeight)",
        "message": "Direct access to browser globals during render may trigger SSR hydration mismatch.",
        "fix": "Wrap in useEffect() or guard with: if (typeof window !== 'undefined')"
    }
]

def scan_file(file_path: Path):
    findings = []
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()

    for check in CHECKS:
        regex = re.compile(check["pattern"])
        for i, line in enumerate(lines, start=1):
            if regex.search(line):
                findings.append({
                    "file": str(file_path),
                    "line": i,
                    "code": line.strip()[:60],
                    **check
                })
    return findings

def generate_html_report(findings, scanned_count, output_path: str = "ui-audit.html"):
    critical_count = sum(1 for f in findings if f["severity"] == "CRITICAL")
    warning_count = sum(1 for f in findings if f["severity"] == "WARNING")
    score = max(0, 100 - (critical_count * 25 + warning_count * 10))

    rows_html = ""
    for f in findings:
        badge_color = "red" if f["severity"] == "CRITICAL" else "yellow"
        rows_html += f"""
        <tr class="border-b border-gray-800">
            <td class="p-3"><span class="px-2 py-0.5 rounded text-xs font-bold bg-{badge_color}-900 text-{badge_color}-300">{f['severity']}</span></td>
            <td class="p-3 font-mono text-xs text-gray-300">{f['file']}:{f['line']}</td>
            <td class="p-3 font-semibold text-white">{f['message']}</td>
            <td class="p-3 font-mono text-xs text-gray-400 bg-black/40 rounded">{f['code']}</td>
            <td class="p-3 text-xs text-emerald-400 font-mono">{f['fix']}</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Frontend Sentinel UI Audit Report</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>body {{ background-color: #0d1117; color: #c9d1d9; }}</style>
</head>
<body class="p-8 max-w-6xl mx-auto space-y-6">
  <header class="flex justify-between items-center bg-[#161b22] p-6 rounded-xl border border-gray-800">
    <div>
      <h1 class="text-2xl font-bold text-white flex items-center space-x-2"><span>🎨</span><span>Frontend Sentinel Audit</span></h1>
      <p class="text-sm text-gray-400 mt-1">Scanned {scanned_count} component files</p>
    </div>
    <div class="text-right">
      <div class="text-3xl font-extrabold {'text-emerald-400' if score >= 80 else 'text-yellow-400' if score >= 50 else 'text-red-400'}">{score}%</div>
      <span class="text-xs text-gray-400 uppercase font-semibold">Production Health Score</span>
    </div>
  </header>

  <div class="bg-[#161b22] p-6 rounded-xl border border-gray-800 overflow-x-auto">
    <h2 class="text-lg font-bold text-white mb-4">Inspection Findings ({len(findings)})</h2>
    <table class="w-full text-left text-sm">
      <thead class="bg-black/50 text-gray-400 text-xs uppercase">
        <tr>
          <th class="p-3">Severity</th>
          <th class="p-3">Location</th>
          <th class="p-3">Issue</th>
          <th class="p-3">Snippet</th>
          <th class="p-3">Recommended Fix</th>
        </tr>
      </thead>
      <tbody>
        {rows_html if findings else '<tr><td colspan="5" class="p-6 text-center text-emerald-400 font-semibold">✔ No frontend defects detected! All components are production-ready.</td></tr>'}
      </tbody>
    </table>
  </div>
</body>
</html>"""
    Path(output_path).write_text(html, encoding="utf-8")
    return score

def main():
    parser = argparse.ArgumentParser(description="Frontend Sentinel: Production UI/UX Auditor")
    parser.add_argument("--path", default=".", help="File or directory to inspect")
    parser.add_argument("--html-report", help="Optional HTML report output file (e.g. ui-audit.html)")
    args = parser.parse_args()

    target = Path(args.path)
    files_to_scan = []
    if target.is_file():
        files_to_scan = [target]
    else:
        for ext in ("*.tsx", "*.jsx", "*.html", "*.vue"):
            files_to_scan.extend(target.rglob(ext))

    all_findings = []
    for f in files_to_scan:
        all_findings.extend(scan_file(f))

    table = Table(title=f"🎨 Frontend Sentinel Audit: {len(files_to_scan)} files scanned", show_lines=True)
    table.add_column("Severity", style="bold")
    table.add_column("Location", style="dim")
    table.add_column("Defect Message", style="white")

    for f in all_findings:
        color = "red" if f["severity"] == "CRITICAL" else "yellow"
        table.add_row(f"[{color}]{f['severity']}[/]", f"{Path(f['file']).name}:{f['line']}", f["message"])

    console.print(table)

    if args.html_report:
        score = generate_html_report(all_findings, len(files_to_scan), args.html_report)
        console.print(Panel(
            f"[bold green]✔ Interactive HTML Report generated:[/] {args.html_report}\n"
            f"[bold white]Health Score:[/] {score}%\n"
            f"[dim]Total issues detected: {len(all_findings)}[/]",
            title="Frontend Audit Complete",
            border_style="green"
        ))

if __name__ == "__main__":
    main()
