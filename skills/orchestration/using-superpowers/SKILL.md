---
name: using-superpowers
version: 1.1.0
description: The master orchestration meta-skill for Agent Superpowers. Governs the 7-stage autonomous engineering lifecycle across Claude Code, Cursor, Codex, Antigravity, and Gemini CLI.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, MCP]
tags: [orchestration, bootstrap, lifecycle, master-protocol]
---

# ⚡ Master Meta-Skill: Using Agent Superpowers

## 1. When to Trigger (Routing)
- **TRIGGER ALWAYS**: This is the bootstrap skill. It should remain active across all agent sessions.
- **SPECIAL TRIGGER**: When the user asks:
  - *"What are your superpowers?"*
  - *"Tell me about your superpowers"*
  - *"Run diagnostics"*
  - Respond by listing all active skills, their versions, and current operational readiness.

---

## 2. The 7-Stage Autonomous Engineering Lifecycle

Whenever tasked with building a feature, fixing a bug, or refactoring an architecture, you MUST orchestrate your skills through this disciplined lifecycle:

```text
[1. BRAINSTORM] ──> [2. WORKTREE ISOLATE] ──> [3. MAP & COMPRESS]
       │                                              │
       ▼                                              ▼
[7. MERGE / CLEANUP] <── [6. RED-TEAM FUZZ] <── [5. SURGICAL PATCH] <── [4. TDD PROOF (RED)]
```

### Stage 1: Brainstorming & Specification (`feature-brainstormer`)
- **Rule**: Never jump into code if the prompt leaves architectural ambiguity.
- Ask up to 3 clarifying questions, define acceptance criteria, and establish edge-case bounds.

### Stage 2: Workspace Isolation (`git-worktree-sandbox`)
- **Rule**: Never experiment on the user's primary working tree for multi-file tasks.
- Create an ephemeral worktree branch via `skills/workflow/git-worktree-sandbox/scripts/worktree.py create <task-name>`.

### Stage 3: Tomography & Context Compression (`arch-archaeologist` + `token-squeezer`)
- Run `arch-archaeologist` to map caller-callee graphs and dead functions.
- Run `token-squeezer` in `interface` mode to inspect large dependencies at 60% token reduction.

### Stage 4: Test-Driven Proof of Defect (`ghost-runner`)
- **STRICT PROHIBITION**: DO NOT TOUCH SOURCE CODE UNTIL A FAILING TEST IS WITNESSED.
- Write an isolated minimal test script (`MRE`). Verify it fails with exit code != 0 (`RED`).

### Stage 5: Surgical Implementation
- Apply the minimal necessary edits strictly within the isolated worktree.

### Stage 6: Adversarial Red-Team Fuzzing (`adversarial-duelist`)
- Run `adversarial-duelist` against your modified functions.
- Pass nulls, boundary overflows, SQL vectors, and zero divisions.
- Code merges ONLY if it achieves a 100% defense score.

### Stage 7: Verification & Worktree Cleanup
- Verify `ghost-runner` is `GREEN`.
- Merge the worktree back or prepare a clean Pull Request, then remove the ephemeral worktree.

---

## 3. Autonomous Arsenal Inventory

| Skill | Role | When Active |
| :--- | :--- | :--- |
| `using-superpowers` | 🧠 Master Orchestrator | Always active (boots the lifecycle) |
| `feature-brainstormer` | 💡 Requirements Guard | When requirements are vague or a feature starts |
| `git-worktree-sandbox` | 📦 Environment Isolation | Multi-file features or high-risk edits |
| `arch-archaeologist` | 🗺️ Code Cartographer | Exploring unfamiliar/legacy codebases |
| `token-squeezer` | 📉 Context Optimizer | Before loading large files/dependencies into memory |
| `ghost-runner` | 🔬 TDD Defect Prover | Any bug fix or regression remediation |
| `adversarial-duelist` | ⚔️ Offensive Red-Teamer | Pre-commit security and edge-case audit |
| `api-synthesizer` | 🔌 Network-to-SDK Engine | Integrating endpoints, cURL, or HAR traffic |

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** bypass Stage 4 (TDD Proof) when fixing defects.
- ❌ **NEVER** skip red-team fuzzing for public endpoints or auth logic.
- ❌ **NEVER** leave orphaned git worktrees behind after task completion.
