---
name: git-worktree-sandbox
version: 1.1.0
description: Ephemeral git worktree sandbox isolation. Guarantees that agent experiments, aggressive refactoring, and test suites run in isolated worktrees without corrupting the primary working branch.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, MCP]
tags: [git, worktree, sandbox, safety, isolation]
---

# 📦 Skill: Git Worktree Sandbox (Workspace Isolation)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The agent begins a complex feature, invasive refactoring, or multi-file architectural change.
  - The user requests: "work in a sandbox", "use an isolated branch", or "don't break my current working tree".
- **DO NOT TRIGGER WHEN**:
  - The workspace is not a Git repository.
  - The edit is a trivial single-line typo fix in a documentation markdown file.

---

## 2. Fundamental Philosophy
> *"Coding agents often modify files prematurely, leaving half-finished edits, untracked garbage, or broken builds in the user's active editor. Git Worktree Sandbox forces all experimental work into a parallel, isolated workspace directory."*

---

## 3. Operational Protocol

### Phase 1: Create Isolated Sandbox
Execute the worktree helper:
```bash
python skills/workflow/git-worktree-sandbox/scripts/worktree.py create <task-name>
```
This automatically:
1. Creates a new branch `worktree/<task-name>`.
2. Checks it out in `.worktrees/<task-name>`.
3. Ensures your primary working tree remains 100% clean and untouched.

### Phase 2: Execute Work in Sandbox
- All file reads, edits, test runs, and commits take place strictly inside `.worktrees/<task-name>`.

### Phase 3: Finish & Clean Up
Once tests pass and the user confirms:
- **To merge and finish**:
  ```bash
  python skills/workflow/git-worktree-sandbox/scripts/worktree.py merge <task-name>
  ```
- **To discard on failure**:
  ```bash
  python skills/workflow/git-worktree-sandbox/scripts/worktree.py discard <task-name>
  ```

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** leave temporary `.worktrees/` directories checked into git (ensure `.gitignore` ignores `.worktrees/`).
- ❌ **NEVER** force-delete an active worktree without user consent if uncommitted changes exist.
