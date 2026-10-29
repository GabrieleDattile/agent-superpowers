# Agent Skill Specification (v1.0)

## Overview
An **Agent Skill** is an atomic, self-contained capability designed to be loaded by autonomous AI agents (such as Claude Code, Cursor, Windsurf, Gemini CLI, or MCP servers) strictly on-demand.

Following the principle of **Progressive Context Loading**, skills keep the agent's baseline working memory lean. The agent only loads instructions and auxiliary scripts when a user task explicitly triggers the skill.

---

## Directory Architecture

Every skill lives inside a categorized directory within `skills/` and adheres to this structure:

```text
skills/<category>/<skill-name>/
├── SKILL.md            # Mandatory: Spec, triggers, system prompt, guards
├── scripts/            # Executable code, CLI helpers, deterministic algorithms
└── examples/           # Few-shot prompts, test targets, input/output samples
```

---

## The `SKILL.md` Standard

Each `SKILL.md` must start with YAML frontmatter followed by structured operational sections:

```markdown
---
name: skill-name
version: 1.0.0
description: Clear, 1-2 sentence description including explicit trigger triggers.
author: Gabriele Dattile
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [debugging, security, devops]
---

# Skill: Skill Name

## 1. When to Trigger (Routing)
- **Trigger when**: Explicit situations where the agent MUST activate this skill.
- **Do NOT trigger when**: Negative boundary conditions to avoid unnecessary loading.

## 2. Prerequisites & Tools
- Required environment (Python 3.10+, Node.js, git, etc.)
- Tools required by the agent (Terminal/Shell, File Read/Write).

## 3. Operational Protocol (Step-by-Step)
1. **Phase 1: Discovery & Analysis**
2. **Phase 2: Execution**
3. **Phase 3: Verification**

## 4. Guardrails & Negative Constraints
- Explicit list of actions the agent is strictly prohibited from doing.

## 5. Input / Output Schema
- What data is expected and what artifact/result must be returned.
```

---

## Deterministic Code Separation (`scripts/`)
LLMs excel at reasoning, but struggle with deterministic tasks like token counting, AST traversal, and port scanning.
* **Complex logic belongs in `scripts/`**.
* The agent invokes the local script via shell execution and reads the parsed output, preserving context and eliminating hallucinations.
