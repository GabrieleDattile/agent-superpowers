---
name: ghost-runner
version: 1.0.0
description: Zero-assumption autonomous bug replicator. Prohibits touching production code until a minimal failing test reproduces the bug in isolation.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [debugging, tdd, automated-testing, reliability]
---

# 🔬 Skill: Ghost-Runner (Zero-Assumption Bug Reproducer)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user reports a bug, exception, stack trace, or failing pipeline.
  - The user asks to "fix this error", "why is this failing", or "resolve the bug".
- **DO NOT TRIGGER WHEN**:
  - The user is asking for a pure refactor or greenfield feature development where no regression or defect exists.

---

## 2. Fundamental Philosophy
> **"No code modification without scientific proof of defect."**
> AI agents frequently introduce regressions by hallucinating assumptions about what broke. Ghost-Runner forces a strict **Test-Driven Remediation (TDR)** loop.

---

## 3. Operational Protocol (Step-by-Step)

### Phase 1: Isolation & Minimal Reproducible Example (MRE)
1. **Analyze Bug Context**: Read the error message, logs, or user description.
2. **STRICT CONSTRAINT**: **DO NOT TOUCH THE TARGET SOURCE CODE YET.**
3. Create a minimal standalone test script (e.g. `test_reproduce_<issue>.py`).
4. Execute the test using the Ghost-Runner runner:
   ```bash
   python skills/debugging/ghost-runner/scripts/ghost_runner.py run --test <path_to_test>
   ```
5. **Phase Gate 1**: The test **MUST FAIL (RED)** with the exact symptom reported. If the test passes or errors out on syntax, the MRE is invalid. Refine until you have a genuine red test.

### Phase 2: Surgical Patch
1. Formulate the minimal surgical fix in the codebase.
2. Apply the change to the target file(s). Do not modify surrounding unrelated logic.

### Phase 3: Verification & Regression Check
1. Re-run the Ghost-Runner verification:
   ```bash
   python skills/debugging/ghost-runner/scripts/ghost_runner.py verify --test <path_to_test>
   ```
2. **Phase Gate 2**: The test **MUST PASS (GREEN)**.
3. Run the full existing test suite to confirm zero regressions were introduced.
4. Clean up temporary test files or persist the test into the project's official test directory.

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** edit source code files before observing the MRE fail.
- ❌ **NEVER** suppress errors with blanket `try...except: pass` or mock away the actual failure.
- ❌ **NEVER** conclude a bug is fixed without automated execution verification.
