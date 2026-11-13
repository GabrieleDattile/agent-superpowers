---
name: hallmark
version: 1.0.0
description: Anti-AI-slop design engine and UI audit toolkit. Overrides generic LLM aesthetic defaults (purple gradients, predictable rounded cards, unopinionated typography) with 24 distinct visual material themes, purpose-driven layout verbs (build, audit, redesign, study), and automated sloplint verification.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, Copilot, MCP]
tags: [frontend, design, anti-ai-slop, themes, sloplint, ui-ux, styling]
---

# 🎨 Skill: Hallmark (Anti-AI-Slop Design Engine)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user asks to build a web page, landing page, app screen, or UI component.
  - The user says "don't make it look like AI generated it", "avoid generic AI design", or mentions "AI slop".
  - The user requests an aesthetic audit or wants to redesign an existing UI without breaking functionality.
  - The user asks to run `sloplint` or check against design anti-patterns.
- **DO NOT TRIGGER WHEN**:
  - The task is purely backend, database querying, or non-visual terminal scripting.

---

## 2. The Anti-AI-Slop Manifesto

Large language models naturally converge on a predictable "slop attractor" due to statistical training defaults:
1. **The Purple/Indigo Linear Gradient**: `bg-gradient-to-r from-purple-600 to-indigo-600` on dark `#0f172a`.
2. **The Symmetrical 3-Card Feature Grid**: 3 identical boxes with generic Lucide icons and placeholder buzzwords.
3. **The Unanchored Floating Blur Orb**: Giant `blur-3xl` purple blobs dumped in the background to hide empty space.
4. **The Dual Primary Button Dilemma**: Two filled bright buttons side-by-side causing visual decision fatigue.
5. **The Micro-Label Uppercase Disease**: `uppercase tracking-widest text-xs` on every random paragraph.
6. **The Inter Font Monoculture**: Zero typographic personality, identical weights, and no serif or display contrast.

**Hallmark enforces a hard floor against these defaults.** Every page must look intentional, hand-crafted, and culturally distinct.

---

## 3. The 4 Operational Verbs

### 🔨 `build` (Purpose-Driven Macrostructure)
1. **Define the Primary Action**: Every screen is built around the ONE thing the visitor came to do (book, buy, search, read).
2. **Select a Material Theme**: Do NOT invent colors on the fly. Pick a curated theme from `references/themes.json` (e.g. *Atelier*, *Furrow*, *Cobalt*, *Studio*, *Midnight*, *Newsprint*, *Cyber-Nordic*).
3. **Build the Hero First**: Create and review the hero section cold before generating sub-sections.
4. **Vary Density**: Break the 3-card pattern. Use asymmetrical bento boxes (2x1, 1x2), interactive calculators, full-bleed images, or typography-led lists.

### 🔍 `audit` (Sloplint Verification)
Runs the automated `sloplint.py` scanner over proposed or existing files to detect the 6 critical slop tells.
```bash
python skills/frontend/hallmark/scripts/sloplint.py <file-or-dir>
```

### 🔄 `redesign` (Visual Uplift with Zero Breakage)
When redesigning an existing page:
- **`--kept` Invariant**: 100% of existing `<form>`, `<input>`, `<a>`, buttons, IDs, and event handlers MUST be preserved verbatim.
- Upgrade typography, color palettes, spacing rhythm, and border-radius consistency while leaving functional DOM wires intact.

### 🔬 `study` (Style DNA Extraction)
Extracts typographic hierarchy, palette tokens, and border radii from external reference designs to assemble a custom theme.

---

## 4. Curated Hallmark Material Themes

| Theme | Mood | Display Font | Body Font | Accent Color | Border Radius |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Atelier** | Editorial, gallery warmth | Playfair Display | Plus Jakarta Sans | `#c25e36` (Terracotta) | `4px` |
| **Cobalt** | High-density engineering | Space Grotesk | JetBrains Mono | `#00f0ff` (Cyan) | `2px` |
| **Furrow** | Grounded agricultural-tech | Fraunces (serif) | IBM Plex Sans | `#dda15e` (Gold) | `6px` |
| **Studio** | Swiss high-contrast minimal | Syne | Inter Tight | `#ff3b00` (Vermillion) | `0px` |
| **Midnight** | Deep luxury obsidian | Cinzel | Geist | `#d4af37` (Champagne) | `8px` |
| **Newsprint** | Dense journalism | Newsreader | Lora | `#a63a24` (Crimson) | `0px` |
| **Cyber-Nordic** | Clean Scandinavian arctic | Cabinet Grotesk | Manrope | `#38bdf8` (Ice Blue) | `4px` |
| **Dose** | Surgical bio-tech clarity | DM Sans | IBM Plex Mono | `#14b8a6` (Teal) | `8px` |

---

## 5. Automated Sloplint Quality Gate

Before marking any UI task complete, run:
```bash
# Verify a single file
python skills/frontend/hallmark/scripts/sloplint.py src/components/Hero.tsx

# Or run via Agent Superpowers CLI
python cli/superpowers.py run sloplint src/
```

If the Slop Score exceeds **25**, refactor the layout using Hallmark theme tokens and re-run until the score returns `0 / 100 (CLEAN)`.
