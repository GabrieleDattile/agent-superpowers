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

    # Sequence of animated terminal states
    timeline = [
        # Frame 1: Initial Prompt
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
        ], 1200),

        # Frame 2: Agent triggers Ghost-Runner
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Triggered Skill: ", TEXT_WHITE, False), ("ghost-runner", TEXT_YELLOW, True)],
            [("   Constraint: ", TEXT_MUTED, False), ("Source modification locked until red test proven.", TEXT_WHITE, False)],
        ], 1000),

        # Frame 3: Creating MRE
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Triggered Skill: ", TEXT_WHITE, False), ("ghost-runner", TEXT_YELLOW, True)],
            [("   Constraint: ", TEXT_MUTED, False), ("Source modification locked until red test proven.", TEXT_WHITE, False)],
            [("   Action: ", TEXT_MUTED, False), ("Generated minimal test_reproduce_vip.py", TEXT_CYAN, False)],
            [("   Running: ", TEXT_MUTED, False), ("python ghost_runner.py reproduce --test test_reproduce_vip.py", TEXT_WHITE, False)],
        ], 1000),

        # Frame 4: Red Confirmed
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Triggered Skill: ", TEXT_WHITE, False), ("ghost-runner", TEXT_YELLOW, True)],
            [("   Constraint: ", TEXT_MUTED, False), ("Source modification locked until red test proven.", TEXT_WHITE, False)],
            [("   Action: ", TEXT_MUTED, False), ("Generated minimal test_reproduce_vip.py", TEXT_CYAN, False)],
            [("   [PHASE 1] ", TEXT_YELLOW, True), ("✔ PROOF CONFIRMED (RED)", TEXT_RED, True), (" - AssertionError: 95.0 != 80.0", TEXT_MUTED, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Applying surgical fix to billing.py...", TEXT_WHITE, False)],
        ], 1300),

        # Frame 5: Green Confirmed
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Triggered Skill: ", TEXT_WHITE, False), ("ghost-runner", TEXT_YELLOW, True)],
            [("   [PHASE 1] ", TEXT_YELLOW, True), ("✔ PROOF CONFIRMED (RED)", TEXT_RED, True), (" - AssertionError: 95.0 != 80.0", TEXT_MUTED, False)],
            [("   [PHASE 2] ", TEXT_YELLOW, True), ("✔ VERIFICATION (GREEN)", TEXT_GREEN, True), (" - Test passed in 0.04s", TEXT_MUTED, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Activating Skill: ", TEXT_WHITE, False), ("adversarial-duelist", TEXT_YELLOW, True), (" (Pre-commit Audit)", TEXT_MUTED, False)],
        ], 1200),

        # Frame 6: Duelist Audit Results
        ([
            [("$ ", TEXT_MUTED, False), ("claude ", TEXT_CYAN, True), ("\"Fix VIP discount bug in billing.py\"", TEXT_WHITE, False)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Triggered Skill: ", TEXT_WHITE, False), ("ghost-runner", TEXT_YELLOW, True)],
            [("   [PHASE 1] ", TEXT_YELLOW, True), ("✔ PROOF CONFIRMED (RED)", TEXT_RED, True)],
            [("   [PHASE 2] ", TEXT_YELLOW, True), ("✔ VERIFICATION (GREEN)", TEXT_GREEN, True)],
            [(">> [AGENT] ", TEXT_CYAN, True), ("Activating Skill: ", TEXT_WHITE, False), ("adversarial-duelist", TEXT_YELLOW, True)],
            [("   Fuzzing: ", TEXT_MUTED, False), ("11 attack vectors (null byte, zero division, overflow)", TEXT_WHITE, False)],
            [("   [SECURITY] ", TEXT_CYAN, True), ("✔ DEFENSE PASSED: 0 crashes, 100% boundary proof", TEXT_GREEN, True)],
            [(">> [RESULT] ", TEXT_GREEN, True), ("Patch verified & committed with zero regressions! 🚀", TEXT_WHITE, True)],
        ], 3000),
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
