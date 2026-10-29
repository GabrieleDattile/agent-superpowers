---
name: adversarial-duelist
version: 1.0.0
description: Adversarial red-team auditor. Generates malicious edge-case payloads, fuzzing vectors, and exploit scripts against proposed code before merge.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [security, red-team, fuzzing, audit, pr-review]
---

# ⚔️ Skill: Adversarial Duelist (The Code Arena)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user requests a security review, pre-commit audit, or PR evaluation.
  - The user asks "is this code safe?", "can this break?", or "find edge cases in this function".
- **DO NOT TRIGGER WHEN**:
  - The user is asking for simple formatting, docstrings, or boilerplate generation.

---

## 2. Fundamental Philosophy
> *"Standard AI code reviewers leave polite, superficial comments. Adversarial Duelist acts as an offensive red-teamer attempting to crash and break your logic."*

---

## 3. Operational Protocol

### Phase 1: Attack Surface Extraction
1. Inspect the function signature, argument types, and external dependencies.
2. Identify input boundaries: integers, strings, floats, collections, file descriptors.

### Phase 2: Autonomous Fuzzing & Exploit Generation
Execute the Duelist engine against the target module:
```bash
python skills/security/adversarial-duelist/scripts/duelist.py --target <path_to_file.py> --func <function_name>
```
The duelist systematically tests against 6 attack vectors:
1. **Integer & Float Boundaries**: `0`, `-1`, `-2^63`, `NaN`, `+Infinity`, `1e308`.
2. **String Explosions**: Null bytes (`\x00`), 100,000-char strings, SQL/Command injection snippets, Unicode right-to-left overrides, zero-width spaces.
3. **Type & Structural Poisoning**: Passing `None`, unexpected dicts, circular references.
4. **Concurrency & Race Conditions**: Rapid async invocations.
5. **Division & Underflow**: Zero division, precision loss.
6. **Resource Exhaustion**: Memory pressure payloads.

### Phase 3: Remediate or Defend
1. Review the generated exploit report.
2. If the function ungracefully crashed (`Unhandled Exception` / `Fatal Error`), the agent MUST harden the code with proper input sanitization, type guarding, and bounded constraints.
3. Re-run Duelist until the defense score is **100% PASS**.

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** approve code that throws raw unhandled exceptions on unexpected input.
- ❌ **NEVER** assume inputs are sanitized upstream without explicit assertions or Pydantic validation.
