---
name: blackbox-cloner
version: 1.0.0
description: Clean-room software reverse engineering engine. Deconstructs proprietary tools, desktop utilities, and SaaS features (e.g. Adobe tools, Figma canvas, background removers) into functional specs and synthesizes clean-room open-source implementations.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, Antigravity, MCP]
tags: [reverse-engineering, cleanroom, tool-cloning, architecture, scaffolding]
---

# 🕵️ Skill: Blackbox Cloner (Clean-Room Tool Replicator)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user asks to reverse engineer, clone, or replicate a proprietary tool or feature (e.g., "replicate this Adobe Photoshop layer blending tool", "clone the Figma auto-layout engine", "reverse engineer this SaaS background-removal widget").
  - The user wants a clean-room open-source alternative to a closed-source software component.
  - The user provides UI screenshots, functional descriptions, or sample input/output files and wants an equivalent standalone implementation.
- **DO NOT TRIGGER WHEN**:
  - The user only wants to capture network HTTP requests into an SDK (trigger `api-synthesizer` instead).
  - The task is simply reading an existing open-source repository's dead code (trigger `arch-archaeologist` instead).

---

## 2. Fundamental Philosophy & Clean-Room Doctrine
> *"True software replication does not copy proprietary source code or binaries. It observes black-box behaviors, formulates mathematical and state-machine abstractions, and implements an independent, clean-room solution using modern open standards."*

This doctrine guarantees:
1. **Zero Copyright Contamination**: No proprietary headers, decompiled assembly, or closed blobs are used.
2. **Modern Stack Upgrades**: Replaces legacy desktop architectures with WebAssembly, HTML5 Canvas, WebGL, Web Workers, or modern Python libraries (NumPy, Pillow).
3. **Auditability**: Every generated scaffold includes an independent Clean-Room Specification (`cleanroom-spec.md`).

---

## 3. Operational Protocol

### Phase 1: Black-Box Behavior Extraction
Analyze the target tool along four structural dimensions:
1. **State Machine & Data Model**:
   - Entities (e.g. Layers, Nodes, Canvas, Selection, History Stack).
   - Undo/Redo transactions and immutable state transitions.
2. **Event & Interaction Matrix**:
   - Pointer events (drag, hover, pan, pinch-zoom, multi-touch).
   - Keyboard hotkeys and shortcuts (e.g., Spacebar for Pan, V for Selection, Ctrl+Z).
3. **Core Processing Engine**:
   - Mathematical transformations (affine matrix 2D/3D, blending formulas, pixel filters).
   - Rendering strategy (Canvas 2D context, WebGL shaders, SVG DOM, or headless Python pipeline).
4. **Serialization & Formats**:
   - Input ingestion formats (raw images, vector paths, JSON, binary blobs).
   - Export pipelines (PNG, SVG, PDF, JSON state dumps).

### Phase 2: CLI Deconstruction & Scaffolding
Run the Blackbox Cloner CLI:
```bash
# Deconstruct and generate clean-room spec
python skills/reverse-engineering/blackbox-cloner/scripts/cloner.py deconstruct --tool "LayeredCanvasEditor" --category "graphics"

# Synthesize a ready-to-run clean-room web or python scaffold
python skills/reverse-engineering/blackbox-cloner/scripts/cloner.py scaffold --tool "LayeredCanvasEditor" --target "web" --out-dir "./scaffolds/canvas-editor"
```

### Phase 3: Verification & Independence Testing
1. Confirm the generated scaffold runs with zero external proprietary dependencies.
2. Verify all keyboard shortcuts, mouse drag-and-drop, and state mutations match the intended behavior.
3. Validate that generated code is fully typed (TypeScript or Python with Type Hints).

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** inspect or incorporate leaked, decompiled, or proprietary source code. The replication must strictly follow black-box observable behaviors.
- ❌ **NEVER** produce fragile monolithic scripts. Separate State, Interaction Handling, and Processing Engines into distinct modules.
- ❌ **ALWAYS** emit an immutable History Stack (`undo`/`redo`) for interactive tools.
