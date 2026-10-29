---
name: memory-nexus
version: 1.0.0
description: Cross-session architectural memory ledger. Preserves technical decisions, conventions, and context across distinct agent sessions to eliminate repetitive questions and context loss.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, MCP]
tags: [memory, state, context, cross-session, architecture]
---

# 🧠 Skill: Memory Nexus (Cross-Session Context Ledger)

## 1. When to Trigger (Routing)
- **TRIGGER AT SESSION START**: At the start of any new session, query Memory Nexus to reload past architectural decisions and conventions.
- **TRIGGER AT DECISION TIME**: Whenever an architectural choice, library selection, or structural trade-off is finalized with the user.
- **TRIGGER ON QUERY**: When the user asks: "why did we build X this way?", "what conventions are we following?", or "what decisions have we made?".

---

## 2. Fundamental Philosophy
> *"Coding assistants suffer from session amnesia: closing the terminal wipes all context. Memory Nexus maintains a local, tamper-proof architectural ledger that persists across days, weeks, and agent restarts."*

---

## 3. Operational Protocol

### Phase 1: Ingest Past Context
At the beginning of a conversation, read the ledger:
```bash
python skills/memory/memory-nexus/scripts/nexus.py read
```
The agent absorbs all past architectural agreements (e.g. database choice, naming conventions, authentication strategy).

### Phase 2: Record New Decisions
Whenever a non-trivial architectural or technical choice is confirmed:
```bash
python skills/memory/memory-nexus/scripts/nexus.py record --decision "Use SQLite with WAL mode" --rationale "Simplicity for single-node deployment without extra daemon"
```

### Phase 3: Query Specific Context
When exploring a subsystem:
```bash
python skills/memory/memory-nexus/scripts/nexus.py query --topic "auth"
```

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** silently overwrite past recorded decisions without explicit user approval.
- ❌ **NEVER** store sensitive API secrets or private credentials in the memory ledger.
