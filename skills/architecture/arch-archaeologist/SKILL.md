---
name: arch-archaeologist
version: 1.0.0
description: Codebase cartographer and architecture archaeologist. Traces inter-module dependencies, identifies dead zombie functions, and emits living Mermaid.js architectural diagrams.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [architecture, refactoring, dependency-graph, dead-code, mermaid]
---

# 🗺️ Skill: Architecture Archaeologist (Spaghetti Code Cartographer)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user asks to understand, explore, or refactor a legacy project or unfamiliar codebase.
  - The user asks: "map the architecture of this repo", "find dead/unused code", or "draw a diagram of how these modules interact".
- **DO NOT TRIGGER WHEN**:
  - The project is a single trivial script with fewer than 50 lines of code.

---

## 2. Fundamental Philosophy
> *"Developers waste weeks manually untangling spaghetti code. Architecture Archaeologist performs automated AST tomography across directories, exposing dependency graphs, isolated zombie code, and data flows instantly."*

---

## 3. Operational Protocol

### Phase 1: AST Tomography Scan
1. Run the Archaeologist engine on the target directory:
   ```bash
   python skills/architecture/arch-archaeologist/scripts/archaeologist.py --dir <target_directory> --output architecture_report.md
   ```

### Phase 2: Dependency & Zombie Code Analysis
The engine evaluates:
1. **Module Import Matrix**: Who imports whom, highlighting circular dependencies.
2. **Call Graph Traces**: Which functions are actually invoked across the codebase.
3. **Dead Code Isolation**: Functions and methods declared but never referenced (candidates for safe deletion).

### Phase 3: Living Diagram Generation
Emits an interactive **Mermaid.js flowchart** that visualizes:
- Entry points (API / CLI controllers)
- Service and Business logic layers
- Data models
- Dead zombie code (highlighted in red)

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** recommend deleting a function without verifying if it is dynamically loaded or part of a public external API.
- ❌ **NEVER** create diagrams with disconnected orphan components without clarifying their status.
