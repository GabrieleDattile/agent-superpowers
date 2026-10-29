---
name: feature-brainstormer
version: 1.1.0
description: Socratic feature brainstorming and requirement refiner. Prevents premature code generation by teasing out specifications, clarifying architectural tradeoffs, and establishing non-goals.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, MCP]
tags: [workflow, planning, brainstorming, specification, requirements]
---

# 💡 Skill: Feature Brainstormer (Socratic Requirements Refiner)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user requests a brand-new feature, component, tool, or architecture with open-ended or ambiguous wording.
  - The user says: "help me design X", "how should we build Y", or "brainstorm a solution for Z".
- **DO NOT TRIGGER WHEN**:
  - The user provided a hyper-specific, line-by-line task instruction with no architectural ambiguity.
  - The task is an urgent bug fix (route directly to `ghost-runner`).

---

## 2. Fundamental Philosophy
> *"The cost of fixing a bad assumption in code is 100x higher than asking a clarifying question upfront. Feature Brainstormer forces the agent to pause, probe for architectural constraints, and define acceptance criteria before touching an editor."*

---

## 3. Operational Protocol

### Step 1: Clarification & Trade-Off Interview
Before writing any code, formulate **up to 3 high-impact clarifying questions** covering:
1. **Target Persona & Usage Pattern**: CLI, Web, API, background worker?
2. **Persistence & State**: Ephemeral in-memory, SQLite, PostgreSQL, JSON files?
3. **Non-Goals & Scope Limits**: What should this feature explicitly *NOT* do in v1?

### Step 2: Architecture & Flow Proposal
Draft a concise Markdown specification including:
- Input/Output data schema.
- Expected error modes and fallback behaviors.
- Dependency impacts on existing code modules.

### Step 3: Phase Gate Confirmation
- Ask the user for explicit approval: *"Does this plan match your vision? Once confirmed, I will instantiate an isolated worktree and proceed with implementation."*

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** output full code files during the brainstorming phase.
- ❌ **NEVER** ask trivial questions that can be answered by inspecting the current repository.
