---
name: token-squeezer
version: 1.0.0
description: AST-based token and context optimizer. Compresses heavy source code and logs by 50-70% before feeding them into LLM context windows without semantic loss.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [optimization, token-compression, cost-reduction, llm-context]
---

# 📉 Skill: Token Squeezer (Context & Cost Optimizer)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The agent is about to load large source files, multi-module directories, or verbose logs into context.
  - The user requests: "optimize context", "compress this file for LLM", "reduce token cost", or "make prompt fit context limit".
- **DO NOT TRIGGER WHEN**:
  - Exact literal string matching or character-for-character formatting must be preserved (e.g. formatting linters).

---

## 2. Fundamental Philosophy
> *"LLM context windows are expensive and suffer from 'lost in the middle' syndrome. Token Squeezer distills codebases to their semantic essence: structural signatures, type annotations, and core logic, eliminating 60%+ of token waste."*

---

## 3. Operational Protocol

### Phase 1: Compression Strategy Selection
Select one of two modes based on agent needs:
1. **`interface` mode (Maximum Compression, ~70% reduction)**:
   - Preserves classes, function signatures, docstrings (first line only), and type hints.
   - Replaces function bodies with `...` (ellipsis).
   - Ideal for agent architecture exploration and cross-file API discovery.
2. **`compact` mode (Full Logic, ~40% reduction)**:
   - Preserves all logical execution.
   - Strips inline comments, trailing whitespace, empty lines, and normalizes imports.

### Phase 2: Execution
Run the Squeezer script:
```bash
python skills/optimization/token-squeezer/scripts/squeezer.py --file <path_to_code.py> --mode interface
```

### Phase 3: Telemetry & Injection
The script emits the compressed payload along with exact token reduction metrics:
- Original tokens vs Compressed tokens
- Percentage saved
- The compressed representation is then fed into the agent's prompt context.

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** discard type annotations or return types during interface compression.
- ❌ **NEVER** mutate runtime logic when using `compact` mode.
