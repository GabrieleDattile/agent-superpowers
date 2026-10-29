#!/usr/bin/env python3
"""
Generates an animated dark-mode terminal GIF for GitHub README showcasing Agent Superpowers.
Author: Gabriele Dattile (https://github.com/GabrieleDattile)
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH, HEIGHT = 820, 480
BG_COLOR = (13, 17, 23)        # GitHub dark dim background
HEADER_COLOR = (22, 27, 34)    # Terminal header bar
BORDER_COLOR = (48, 54, 61)
TEXT_WHITE = (230, 237, 243)
TEXT_MUTED = (139, 148, 158)
TEXT_GREEN = (63, 185, 80)
TEXT_RED = (248, 81, 73)
TEXT_YELLOW = (210, 153, 34)
TEXT_CYAN = (88, 166, 255)

FONT_PATH = "C:\\Windows\\Fonts\\consola.ttf"
try:
    font_main = ImageFont.truetype(FONT_PATH, 16)
    font_bold = ImageFont.truetype("C:\\Windows\\Fonts\\consolab.ttf", 16)
    font_header = ImageFont.truetype(FONT_PATH, 13)
except Exception:
    font_main = ImageFont.load_default()
    font_bold = font_main
    font_header = font_main

def draw_terminal_base():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rounded_rectangle([0, 0, WIDTH - 1, HEIGHT - 1], radius=10, outline=BORDER_COLOR, width=1)

    # Window header bar
    draw.rounded_rectangle([0, 0, WIDTH - 1, 38], radius=10, fill=HEADER_COLOR)
    draw.rectangle([0, 28, WIDTH - 1, 38], fill=HEADER_COLOR)
    draw.line([(0, 38), (WIDTH, 38)], fill=BORDER_COLOR, width=1)

    # Terminal buttons
    draw.ellipse([14, 13, 26, 25], fill=(255, 95, 86))   # Red
    draw.ellipse([34, 13, 46, 25], fill=(255, 189, 46))  # Yellow
    draw.ellipse([54, 13, 66, 25], fill=(39, 201, 63))   # Green

    # Window title
    title = "gabriele@macbook: ~/project — agent-superpowers"
    draw.text((WIDTH // 2 - 140, 12), title, fill=TEXT_MUTED, font=font_header)

    return img

def create_frame(lines):
    img = draw_terminal_base()
    draw = ImageDraw.Draw(img)

    y = 52
    for line in lines:
        x = 22
        # Line is a list of tuples: (text, color, is_bold)
        for part in line:
            text, color, is_bold = part
            f = font_bold if is_bold else font_main
            draw.text((x, y), text, fill=color, font=f)
            # Advance x
            bbox = draw.textbbox((x, y), text, font=f)
            x += (bbox[2] - bbox[0])
        y += 24
    return img

def generate_gif(output_path: str = "assets/demo.gif"):
    frames = []
    durations = []

    # Upgraded timeline showcasing the 7-stage Autonomous Engineering Lifecycle
    timeline = [
        # Frame 1: User prompt
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix discount calculation in billing.py and audit security\"", TEXT_WHITE, False)],
        ], 1200),

        # Frame 2: Master Orchestrator Boots
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix discount calculation in billing.py and audit security\"", TEXT_WHITE, False)],
            [(">> [ORCHESTRATOR] ", TEXT_YELLOW, True), ("using-superpowers: ", TEXT_WHITE, False), ("7-Stage Lifecycle Engaged", TEXT_GREEN, True)],
            [("   Available: ", TEXT_MUTED, False), ("8 autonomous skills (TDD, Sandbox, Red-Team, Cartography)", TEXT_WHITE, False)],
        ], 1100),

        # Frame 3: Worktree Sandbox Isolation
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix discount calculation in billing.py and audit security\"", TEXT_WHITE, False)],
            [(">> [ORCHESTRATOR] ", TEXT_YELLOW, True), ("using-superpowers: ", TEXT_WHITE, False), ("7-Stage Lifecycle Engaged", TEXT_GREEN, True)],
            [("   [STAGE 1: ISOLATE] ", TEXT_CYAN, True), ("git-worktree-sandbox", TEXT_WHITE, True)],
            [("   Action: ", TEXT_MUTED, False), ("Created isolated sandbox branch in ", TEXT_WHITE, False), (".worktrees/fix-discount", TEXT_YELLOW, False)],
            [("   Guarantee: ", TEXT_MUTED, False), ("Primary workspace locked & protected from corruption.", TEXT_GREEN, False)],
        ], 1300),

        # Frame 4: Ghost-Runner TDD Proof (RED)
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix discount calculation in billing.py and audit security\"", TEXT_WHITE, False)],
            [("   [STAGE 1: ISOLATE] ", TEXT_CYAN, True), ("git-worktree-sandbox -> .worktrees/fix-discount", TEXT_MUTED, False)],
            [("   [STAGE 2: PROVE]   ", TEXT_CYAN, True), ("ghost-runner", TEXT_WHITE, True), (" (Zero-Assumption TDD)", TEXT_MUTED, False)],
            [("   Running MRE: ", TEXT_MUTED, False), ("python test_discount_reproduce.py", TEXT_WHITE, False)],
            [("   [PROOF RESULT] ", TEXT_YELLOW, True), ("✔ DEFECT CONFIRMED (RED)", TEXT_RED, True), (" - AssertionError: 95.0 != 80.0", TEXT_MUTED, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Applying surgical fix strictly within sandbox...", TEXT_WHITE, False)],
        ], 1400),

        # Frame 5: Ghost-Runner Fix Verified (GREEN)
        ([
            [("   [STAGE 1: ISOLATE] ", TEXT_CYAN, True), ("git-worktree-sandbox -> .worktrees/fix-discount", TEXT_MUTED, False)],
            [("   [STAGE 2: PROVE]   ", TEXT_CYAN, True), ("ghost-runner", TEXT_WHITE, True)],
            [("   [PROOF RESULT] ", TEXT_YELLOW, True), ("✔ DEFECT CONFIRMED (RED)", TEXT_RED, True)],
            [("   [STAGE 3: VERIFY]  ", TEXT_CYAN, True), ("ghost-runner", TEXT_WHITE, True)],
            [("   [VERIFY RESULT]", TEXT_YELLOW, True), ("✔ REMEDIATION CONFIRMED (GREEN)", TEXT_GREEN, True), (" - 0.03s, 100% passing", TEXT_MUTED, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Advancing to Stage 4: Offensive Red-Team Audit...", TEXT_WHITE, False)],
        ], 1300),

        # Frame 6: Adversarial Duelist Fuzzing
        ([
            [("   [STAGE 3: VERIFY]  ", TEXT_CYAN, True), ("ghost-runner: ", TEXT_MUTED, False), ("✔ GREEN confirmed", TEXT_GREEN, True)],
            [("   [STAGE 4: ATTACK]  ", TEXT_CYAN, True), ("adversarial-duelist", TEXT_WHITE, True), (" (Red-Team Fuzzer)", TEXT_MUTED, False)],
            [("   Fuzzing vectors: ", TEXT_MUTED, False), ("null-bytes, buffer overflows, SQLi, NaN, zero-div", TEXT_WHITE, False)],
            [("   Audit score: ", TEXT_MUTED, False), ("11/11 survived without unhandled crashes", TEXT_GREEN, False)],
            [("   [SECURITY PASS] ", TEXT_YELLOW, True), ("✔ 100% DEFENSE PROVEN: Zero vulnerabilities", TEXT_GREEN, True)],
        ], 1400),

        # Frame 7: Worktree Clean Merge & Wrap-up
        ([
            [("   [STAGE 4: ATTACK]  ", TEXT_CYAN, True), ("adversarial-duelist: ", TEXT_MUTED, False), ("✔ 100% defense score", TEXT_GREEN, True)],
            [("   [STAGE 5: FINISH]  ", TEXT_CYAN, True), ("git-worktree-sandbox: ", TEXT_WHITE, False), ("Merging into main...", TEXT_YELLOW, False)],
            [("   Pruning: ", TEXT_MUTED, False), ("Removed temporary .worktrees/fix-discount", TEXT_MUTED, False)],
            [("   Status: ", TEXT_MUTED, False), ("Clean fast-forward merge completed.", TEXT_GREEN, False)],
            [(">> [LIFECYCLE COMPLETE] ", TEXT_GREEN, True), ("Production-grade patch ready with ZERO regressions! 🚀", TEXT_WHITE, True)],
        ], 3200),
    ]

    for lines, duration in timeline:
        frame = create_frame(lines)
        frames.append(frame)
        durations.append(duration)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True
    )
    print(f"Animated GIF generated: {output_path}")

if __name__ == "__main__":
    generate_gif()
