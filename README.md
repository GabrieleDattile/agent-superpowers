<div align="center">

# ⚡ AGENT SUPERPOWERS
### Transform Your AI Coding Agent into a Battle-Tested Principal Staff Engineer

**Stop AI hallucinations, broken production commits, and 100k-token context bloat.**  
*A disciplined, deterministic 7-stage autonomous engineering framework natively compatible with **Claude Code, Cursor, Google Antigravity, Windsurf, Codex, and Model Context Protocol (MCP)**.*

<br/>

[![GitHub Stars](https://img.shields.io/github/stars/GabrieleDattile/agent-superpowers?style=for-the-badge&color=ffd700&logo=github)](https://github.com/GabrieleDattile/agent-superpowers/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Glama Score](https://glama.ai/mcp/servers/GabrieleDattile/agent-superpowers/badges/score.svg)](https://glama.ai/mcp/servers/GabrieleDattile/agent-superpowers)
[![Spec: v1.2.0](https://img.shields.io/badge/Spec-Agent%20Skills%20v1.2-brightgreen?style=for-the-badge)](docs/SPECIFICATION.md)
[![MCP Server](https://img.shields.io/badge/MCP-Compatible-purple?style=for-the-badge&logo=anthropic)](mcp/server.py)
[![Author](https://img.shields.io/badge/Author-Gabriele%20Dattile-orange?style=for-the-badge&logo=github)](https://github.com/GabrieleDattile)

<br/>

<a href="downloads/agent-superpowers-v1.2.0.zip?raw=true">
  <img src="https://img.shields.io/badge/📦%20Download%20Full%20Suite-ZIP%20Archive-success?style=for-the-badge&logo=github" alt="Download ZIP Archive" />
</a>
&nbsp;&nbsp;
<a href="#-quick-start-1-command">
  <img src="https://img.shields.io/badge/⚡%20Quick%20Install-1--Command-informational?style=for-the-badge" alt="Quick Install" />
</a>

<br/><br/>

<p align="center">
  <img src="assets/demo.gif" alt="Agent Superpowers Terminal Demo" width="860" style="border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);"/>
</p>

<sub><em>⚡ Autonomous 7-stage lifecycle execution: Ghost Runner isolating failing test (RED), Git Worktree sandbox isolation, and Adversarial red-team fuzzing.</em></sub>

<br/>

> **⭐ Found this useful? Please star the repository to support open-source development!**

</div>

---

## ⚡ The Difference: Chaotic AI vs. Agent Superpowers

Without guardrails, even the best LLMs behave like chaotic junior developers: they jump straight into editing files, hallucinate non-existent APIs, break existing tests, and push unverified changes.

| The Chaos of Default AI ❌ | With Agent Superpowers Protocol 🟢 |
| :--- | :--- |
| **Hallucinates bug fixes**: Edits production code based on guesswork | **Ghost Runner**: Strictly forbidden from editing source code until a minimal failing test reproduces the defect (`RED ➔ GREEN`) |
| **Corrupts your workspace**: Makes sweeping multi-file edits directly on your active working branch | **Git Worktree Sandbox**: Runs all experiments in ephemeral, isolated git worktrees; primary branch remains 100% clean |
| **Generates fragile edge-cases**: Writes happy-path code vulnerable to boundary crashes and exploits | **Adversarial Duelist**: Automated pre-commit red-team fuzzer injects null-bytes, SQLi payloads, and zero-divisions |
| **Blows token budgets**: Dumps full source files into context, hitting rate limits and burning money | **Token Squeezer**: Shrinks prompt context by 50–70% using AST extraction without losing architectural semantics |
| **Breaks frontend layouts**: Generates UI code that looks fine on desktop but breaks on mobile viewports | **Frontend Sentinel**: WCAG 2.1 accessibility and responsive breakpoint auditor with visual HTML reports |
| **Session amnesia**: Forgets past architectural decisions and conventions every time the CLI restarts | **Memory Nexus**: Append-only local decision ledger (`.superpowers/decisions.jsonl`) persists context cross-session |
| **Locked into closed ecosystems**: Inability to interface with proprietary tools and APIs | **Blackbox Cloner & API Synthesizer**: Clean-room tool replication and automatic cURL-to-SDK synthesis |

---

## 💬 See It in Action (Live Agent Conversation)

Here is what happens when you prompt an agent equipped with **Agent Superpowers**:

```text
User: "We have an intermittent crash in our payment checkout when users apply discount vouchers. Fix it."

AI (with Agent Superpowers):
⚡ [Stage 1: Brainstormer] Analyzing discount coupon code paths and error logs.
   ➔ Identified potential edge case: zero-value vouchers causing division-by-zero.

🔍 [Stage 2: Ghost Runner] Enforcing TDD Verification (Prohibiting code edits):
   ➔ Synthesizing reproduction test: `tests/repro_discount_crash.py`
   ➔ Executing test: FAILED (Exit Code 1, ZeroDivisionError).
   ✔ RED stage confirmed: Bug successfully reproduced under controlled isolation.

📦 [Stage 3: Git Worktree Sandbox] Instantiating isolated environment:
   ➔ Created worktree branch: `sandbox/fix-discount-crash` (primary tree protected).

🛠️ [Stage 4: Surgical Patch] Applying minimal fix in `services/checkout.py`:
   ➔ Added decimal voucher floor check and zero-guard.
   ➔ Re-running reproduction test: PASSED (GREEN).
   ➔ Re-running full regression suite: 42 passed, 0 failed.

🛡️ [Stage 5: Adversarial Duelist] Launching pre-commit security fuzzer:
   ➔ Fuzzing `calculate_discount()` with 11 boundary payloads (Negative, NaN, Null-Byte, Overflows)...
   ✔ All 11 attack vectors handled safely.

🚀 [Stage 6: Merge Gate] Worktree verified. Clean patch ready for main branch merge.
```

---

## 🔄 The 7-Stage Autonomous Lifecycle

Every coding task executes through an auditable, deterministic state machine:

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ 1. BRAINSTORM   │ ────> │ 2. WORKTREE     │ ────> │ 3. MAP &        │
│ Requirements    │       │ Sandbox Branch  │       │ Compress (AST)  │
└─────────────────┘       └─────────────────┘       └─────────────────┘
                                                              │
                                                              ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ 6. RED-TEAM     │ <──── │ 5. SURGICAL     │ <──── │ 4. TDD PROOF    │
│ Fuzzing & Audit │       │ Green Patch     │       │ Fail First (RED)│
└─────────────────┘       └─────────────────┘       └─────────────────┘
        │
        ▼
┌─────────────────┐
│ 7. SAFE MERGE   │ ────> Verified Production-Ready Artifact
│ & PR Gate       │
└─────────────────┘
```

---

## 📦 The 11 Autonomous Superpowers

| Superpower | Category | Primary Capability |
| :--- | :--- | :--- |
| [**`using-superpowers`**](skills/orchestration/using-superpowers/SKILL.md) | 🧠 Orchestration | Master bootstrap meta-skill; enforces the 7-stage engineering lifecycle |
| [**`feature-brainstormer`**](skills/workflow/feature-brainstormer/SKILL.md) | 💡 Workflow | Socratic requirements refiner; asks 3 clarifying questions before writing code |
| [**`git-worktree-sandbox`**](skills/workflow/git-worktree-sandbox/SKILL.md) | 📦 Workflow | Ephemeral git worktree isolation; zero risk of corrupting your active workspace |
| [**`frontend-sentinel`**](skills/frontend/frontend-sentinel/SKILL.md) | 🎨 Frontend | Production UI/UX auditor; checks a11y, mobile viewports & generates visual HTML reports |
| [**`memory-nexus`**](skills/memory/memory-nexus/SKILL.md) | 💾 Memory | Cross-session architecture ledger; eliminates agent amnesia between restarts |
| [**`ghost-runner`**](skills/debugging/ghost-runner/SKILL.md) | 🔍 Debugging | Zero-assumption bug reproducer; enforces strict RED ➔ GREEN TDD cycle |
| [**`adversarial-duelist`**](skills/security/adversarial-duelist/SKILL.md) | 🛡️ Security | Pre-commit red-team fuzzer; injects malicious edge-case payloads |
| [**`token-squeezer`**](skills/optimization/token-squeezer/SKILL.md) | ⚡ Optimization | AST-based context compressor; cuts LLM prompt token costs by 50–70% |
| [**`api-synthesizer`**](skills/reverse-engineering/api-synthesizer/SKILL.md) | 🔌 Integration | Network-to-SDK generator; converts cURL traffic into typed Python client SDKs |
| [**`blackbox-cloner`**](skills/reverse-engineering/blackbox-cloner/SKILL.md) | 🕵️ Reverse Engineering | Clean-room tool replicator; deconstructs proprietary software into open-source scaffolds |
| [**`arch-archaeologist`**](skills/architecture/arch-archaeologist/SKILL.md) | 🗺️ Architecture | Codebase cartographer; traces dependency graphs and isolates dead zombie functions |

---

## ⚡ Quick Start (1-Command Install)

### 📦 Direct ZIP Archive
Prefer manual drag-and-drop into your `.cursor/rules` or skills directory?  
👉 **[Download agent-superpowers-v1.2.0.zip](downloads/agent-superpowers-v1.2.0.zip?raw=true)**

### 🐧 macOS / Linux (Native Bash)
```bash
curl -fsSL https://raw.githubusercontent.com/GabrieleDattile/agent-superpowers/main/install.sh | bash
```

### 🪟 Windows (Native PowerShell)
```powershell
irm https://raw.githubusercontent.com/GabrieleDattile/agent-superpowers/main/install.ps1 | iex
```

### 📦 Node.js / NPX
```bash
npx agent-superpowers list
```

---

## 🛠️ Universal Platform Support

Agent Superpowers is designed to be completely runtime-agnostic. Drop it into your existing workflow with zero configuration:

* **🟣 Claude Code**: Native plugin manifest in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) with startup lifecycle hooks in [`hooks/`](hooks/).
* **🔵 Cursor**: Modern `.mdc` Project Rules in [`.cursor/rules/agent-superpowers.mdc`](.cursor/rules/agent-superpowers.mdc).
* **🟠 Google Antigravity & Gemini CLI**: Native workspace extension in [`extension.yaml`](extension.yaml).
* **🌊 Windsurf**: Native IDE rules in [`.windsurfrules`](.windsurfrules).
* **🟢 OpenAI Codex**: Configured via [`.codex/INSTALL.md`](.codex/INSTALL.md).
* **🔌 Model Context Protocol (MCP)**: Native stdio JSON-RPC server in [`mcp/server.py`](mcp/server.py). Compatible with Claude Desktop, Cursor, Antigravity, and Zed.

---

## 📊 Mission Control Dashboard

Agent Superpowers ships with an interactive local web dashboard with **zero external dependencies**. Visualize your skills, architecture dependency graphs, and test telemetry in real time:

```bash
python cli/superpowers.py dashboard
```

---

## 🚀 CLI Commands & Validation

Agent Superpowers includes a built-in verification suite:

```bash
# List all 11 registered superpowers
python cli/superpowers.py list

# Validate specification compliance
python cli/superpowers.py validate

# Run the automated unit test suite
python -m unittest tests/test_skills.py
```

---

## 🤝 Contributing

Contributions are warmly welcomed!
1. Check our formal [Agent Skill Specification](docs/SPECIFICATION.md).
2. Propose new skills via the [New Skill Template](.github/ISSUE_TEMPLATE/new_skill.yml).
3. Ensure CI verification passes (`python cli/superpowers.py validate`).

---

## 👤 Author

**Gabriele Dattile**  
* GitHub: [@GabrieleDattile](https://github.com/GabrieleDattile)  
* Repository: [https://github.com/GabrieleDattile/agent-superpowers](https://github.com/GabrieleDattile/agent-superpowers)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
