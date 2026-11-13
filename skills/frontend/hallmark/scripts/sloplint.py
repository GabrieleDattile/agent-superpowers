#!/usr/bin/env python3
"""
Hallmark Sloplint: Autonomous Anti-AI-Slop Linter & Quality Auditor
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
Repository: https://github.com/GabrieleDattile/agent-superpowers

Detects common machine-generated design tells (purple gradients, predictable 3-card grids,
floating blur balls, generic copy clichés) in HTML, JSX, TSX, Svelte, and Vue files.
"""

import sys
import os
import re
import argparse
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Anti-pattern detection rules
SLOP_RULES = [
    {
        "id": "SLOP-001",
        "name": "Generic AI Purple/Violet Gradient",
        "severity": "HIGH",
        "weight": 25,
        "pattern": re.compile(
            r'(from-purple-\d+|to-indigo-\d+|from-violet-\d+|bg-gradient-to-[a-z]+.*(?:purple|indigo|violet)|linear-gradient\([^)]*(?:#8[a-f0-9]{5}|#7c3aed|#6366f1|#a855f7))',
            re.IGNORECASE
        ),
        "message": "Overused default AI gradient trope (Purple/Indigo linear gradient).",
        "fix": "Pick a deliberate palette from Hallmark themes (e.g. Cobalt, Atelier, Furrow) using solid tones or subtle grain."
    },
    {
        "id": "SLOP-002",
        "name": "Unanchored Floating Blur Orb",
        "severity": "HIGH",
        "weight": 20,
        "pattern": re.compile(
            r'(blur-[23]xl|filter\s+blur-\[\d+px\]|rounded-full\s+.*(?:blur|filter).*(?:purple|indigo|violet|pink))',
            re.IGNORECASE
        ),
        "message": "Lazy AI decorative floating blur orb/blob filling negative space.",
        "fix": "Replace decorative blobs with real editorial photography, technical diagrams, structured cards, or clean whitespace."
    },
    {
        "id": "SLOP-003",
        "name": "Generic AI Buzzword Copy",
        "severity": "MEDIUM",
        "weight": 15,
        "pattern": re.compile(
            r'\b(supercharge\s+your|unleash\s+the\s+power|elevate\s+your|game-changer|seamlessly\s+integrate|empower\s+your|transform\s+the\s+way|next-generation\s+solution|revolutionize\s+your)\b',
            re.IGNORECASE
        ),
        "message": "Generic AI marketing copy cliché devoid of product specifics.",
        "fix": "Write concrete, specific value propositions: state what the user can do, numbers, or specific problems solved."
    },
    {
        "id": "SLOP-004",
        "name": "Overused Uniform Border Radius",
        "severity": "LOW",
        "weight": 10,
        "pattern": re.compile(
            r'(rounded-2xl|rounded-3xl)',
            re.IGNORECASE
        ),
        "message": "Repetitive pill-like or bubbly rounding applied across every element.",
        "fix": "Use deliberate radius contrast: 0-4px for technical/editorial interfaces, or reserve large radii for specific hero pill badges."
    },
    {
        "id": "SLOP-005",
        "name": "Tracked Uppercase Overuse",
        "severity": "LOW",
        "weight": 10,
        "pattern": re.compile(
            r'(uppercase\s+tracking-(?:widest|wider|\[0\.[2-9]em\]))',
            re.IGNORECASE
        ),
        "message": "AI micro-label syndrome (excessive uppercase tracked small text).",
        "fix": "Use sentence-case headings or subtle muted text without forced full-caps tracking."
    },
    {
        "id": "SLOP-006",
        "name": "Symmetrical 3-Card AI Grid Cliché",
        "severity": "MEDIUM",
        "weight": 15,
        "pattern": re.compile(
            r'(grid-cols-1\s+md:grid-cols-3|grid-cols-3)',
            re.IGNORECASE
        ),
        "message": "Formulaic 3-card feature grid with cookie-cutter symmetry.",
        "fix": "Vary section density: use bento grids (2x1, 1x2 asymmetric layout), list-detail views, or interactive walkthroughs."
    }
]

def scan_file(file_path: Path):
    findings = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return findings

    lines = content.split("\n")
    for rule in SLOP_RULES:
        matches_in_file = 0
        for i, line in enumerate(lines, start=1):
            for match in rule["pattern"].finditer(line):
                findings.append({
                    "file": str(file_path),
                    "line": i,
                    "rule_id": rule["id"],
                    "rule_name": rule["name"],
                    "severity": rule["severity"],
                    "weight": rule["weight"],
                    "matched": match.group(0)[:60],
                    "message": rule["message"],
                    "fix": rule["fix"]
                })
                matches_in_file += 1
                if matches_in_file >= 4:  # Cap findings per rule per file to avoid noise
                    break
            if matches_in_file >= 4:
                break
    return findings

def calculate_slop_score(findings):
    if not findings:
        return 0
    total_penalty = sum(f["weight"] for f in findings)
    # Scaled to 0 - 100 with logarithmic dampening
    score = min(100, int(total_penalty * 0.8))
    return score

def main():
    parser = argparse.ArgumentParser(description="Hallmark Sloplint: Anti-AI-Slop Code & Design Linter")
    parser.add_argument("target", nargs="?", default=".", help="Target file or directory to scan (default: current directory)")
    parser.add_argument("--json", action="store_true", help="Output findings as JSON")
    parser.add_argument("--fail-under", type=int, default=25, help="Slop score threshold to exit with error code (default: 25)")
    args = parser.parse_args()

    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Error: Target path '{args.target}' does not exist.", file=sys.stderr)
        sys.exit(1)

    files_to_scan = []
    extensions = {".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".css"}

    if target_path.is_file():
        files_to_scan.append(target_path)
    else:
        for p in target_path.rglob("*"):
            if p.is_file() and p.suffix.lower() in extensions:
                # Ignore node_modules, dist, .git
                if any(part in p.parts for part in ["node_modules", "dist", ".git", "build", ".next", ".cache"]):
                    continue
                files_to_scan.append(p)

    all_findings = []
    for f in files_to_scan:
        all_findings.extend(scan_file(f))

    score = calculate_slop_score(all_findings)

    if args.json:
        import json
        print(json.dumps({
            "slop_score": score,
            "threshold": args.fail_under,
            "status": "PASS" if score < args.fail_under else "FAIL",
            "scanned_files_count": len(files_to_scan),
            "findings_count": len(all_findings),
            "findings": all_findings
        }, indent=2))
        sys.exit(0 if score < args.fail_under else 1)

    print("\n" + "=" * 65)
    print("🎨 Hallmark Sloplint: Autonomous Anti-AI-Slop Auditor")
    print("=" * 65)
    print(f"Scanned: {len(files_to_scan)} frontend files\n")

    if not all_findings:
        print("✔ No AI Slop detected! Clean, human-intentional design aesthetic.")
        print(f"Slop Index: 0 / 100 (Status: CLEAN)\n")
        sys.exit(0)

    # Print Findings
    print(f"Found {len(all_findings)} aesthetic tells:")
    for f in all_findings:
        sev_color = "🔴" if f["severity"] == "HIGH" else ("🟡" if f["severity"] == "MEDIUM" else "⚪")
        print(f"  {sev_color} [{f['rule_id']}] {f['rule_name']} (Line {f['line']} of {Path(f['file']).name})")
        print(f"     Match: '{f['matched']}'")
        print(f"     Why:   {f['message']}")
        print(f"     Fix:   {f['fix']}\n")

    print("-" * 65)
    status_label = "CLEAN" if score < args.fail_under else "FAIL (HIGH SLOP CONTENT)"
    print(f"Overall Slop Index: {score} / 100 [{status_label}]")
    print("Guidance: Adopt one of the 24 curated Hallmark material themes in references/themes.json")
    print("=" * 65 + "\n")

    sys.exit(0 if score < args.fail_under else 1)

if __name__ == "__main__":
    main()
