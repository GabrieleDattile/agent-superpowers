<div align="center">

# ⚡ Agent Superpowers

**The universal, production-grade skills framework for autonomous AI software engineers.**  
*Plug-and-play compatibility across Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, and Model Context Protocol (MCP).*

[![GitHub Stars](https://img.shields.io/github/stars/GabrieleDattile/agent-superpowers?style=for-the-badge&color=yellow)](https://github.com/GabrieleDattile/agent-superpowers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Spec: v1.2.0](https://img.shields.io/badge/Spec-Agent%20Skills%20v1.2-brightgreen?style=for-the-badge)](docs/SPECIFICATION.md)
[![MCP Server](https://img.shields.io/badge/MCP-Compatible-purple?style=for-the-badge)](mcp/server.py)
[![Author](https://img.shields.io/badge/Created%20By-Gabriele%20Dattile-orange?style=for-the-badge)](https://github.com/GabrieleDattile)

<br/>

<a href="downloads/agent-superpowers-v1.2.0.zip?raw=true">
  <img src="https://img.shields.io/badge/📦%20Download%20All%20Skills-ZIP%20Archive-success?style=for-the-badge&logo=github" alt="Download ZIP Archive" />
</a>

<br/><br/>

<img src="assets/demo.gif" alt="Agent Superpowers Terminal Demo" width="820"/>

<br/>
<br/>

</div>

---

## 💡 Why Agent Superpowers?

Default AI coding assistants act like chaotic junior developers: they **guess fixes, edit production files prematurely, break mobile viewports, blow through token budgets, and forget past architectural choices**.

**Agent Superpowers** equips your AI agent with a disciplined **7-Stage Autonomous Engineering Lifecycle**:

```text
[1. BRAINSTORM] ──> [2. WORKTREE ISOLATE] ──> [3. MAP & COMPRESS]
       │                                              │
       ▼                                              ▼
[7. MERGE / PR] <── [6. RED-TEAM FUZZ] <── [5. SURGICAL PATCH] <── [4. TDD PROOF (RED)]
```

* 🧠 **Master Orchestration**: Automatically boots lifecycle hooks and coordinates multi-skill execution.
* 📦 **Zero-Risk Worktrees**: Ephemeral git worktrees guarantee your primary branch is never corrupted during agent experiments.
* 💾 **Cross-Session Memory**: Persists technical decisions and conventions in a local ledger across terminal restarts.
* 🎨 **Production Frontend Auditing**: Clinical inspection of React/Vue/HTML templates for a11y, mobile responsive breaks, and hydration traps with interactive HTML reports.
* 🔬 **Scientific TDD**: Prohibits editing source code until a minimal failing test reproduces the bug in isolation (`RED`).
* ⚔️ **Offensive Red-Teaming**: Attacks functions with null-bytes, SQLi vectors, and boundary overflows before allowing a merge.
* 📉 **60% Token Reduction**: AST interface compressor slashes LLM API costs while retaining 100% semantic clarity.
* 🔌 **Zero-Friction SDKs**: Transforms raw cURL network traffic and browser HAR dumps into typed client libraries in seconds.
* 🗺️ **Code Cartography**: Automatically diagrams spaghetti code dependencies and detects dead zombie functions.

---

## 📦 The 11 Superpowers

| Skill | Category | Primary Capability |
| :--- | :--- | :--- |
| [**`using-superpowers`**](skills/orchestration/using-superpowers/SKILL.md) | 🧠 Orchestration | Master bootstrap meta-skill; enforces the 7-stage engineering lifecycle |
| [**`feature-brainstormer`**](skills/workflow/feature-brainstormer/SKILL.md) | 💡 Workflow | Socratic requirements refiner; asks 3 clarifying questions before coding |
| [**`git-worktree-sandbox`**](skills/workflow/git-worktree-sandbox/SKILL.md) | 📦 Workflow | Ephemeral git worktree isolation; zero risk of breaking active workspace |
| [**`frontend-sentinel`**](skills/frontend/frontend-sentinel/SKILL.md) | 🎨 Frontend | Production UI/UX auditor; checks a11y, mobile viewports & generates visual HTML reports |
| [**`memory-nexus`**](skills/memory/memory-nexus/SKILL.md) | 💾 Memory | Cross-session architecture ledger; eliminates agent amnesia between restarts |
| [**`ghost-runner`**](skills/debugging/ghost-runner/SKILL.md) | 🔍 Debugging | Zero-assumption bug reproducer; enforces strict RED ➔ GREEN TDD cycle |
| [**`adversarial-duelist`**](skills/security/adversarial-duelist/SKILL.md) | 🛡️ Security | Pre-commit red-team fuzzer; injects malicious edge-case payloads |
| [**`token-squeezer`**](skills/optimization/token-squeezer/SKILL.md) | ⚡ Optimization | AST-based context compressor; cuts LLM prompt token costs by 50-70% |
| [**`api-synthesizer`**](skills/reverse-engineering/api-synthesizer/SKILL.md) | 🔌 Integration | Network-to-SDK generator; converts cURL traffic into typed Python clients |
| [**`blackbox-cloner`**](skills/reverse-engineering/blackbox-cloner/SKILL.md) | 🕵️ Reverse Engineering | Clean-room tool replicator; deconstructs proprietary software into open-source scaffolds |
| [**`arch-archaeologist`**](skills/architecture/arch-archaeologist/SKILL.md) | 🗺️ Architecture | Codebase cartographer; traces dependency graphs and isolates dead code |

---

## ⚡ Universal Installation (1-Command)

### 📦 Direct ZIP Download
Prefer manual drag-and-drop?  
👉 **[Download agent-superpowers-v1.2.0.zip](downloads/agent-superpowers-v1.2.0.zip?raw=true)** and unpack directly into your editor's skill directory.

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

## 📊 Mission Control Dashboard

Launch the interactive local visualizer to inspect architecture graphs, fuzzing telemetry, and token metrics:
```bash
python cli/superpowers.py dashboard
```

---

## 🛠️ Platform Integration

* **🟣 Claude Code**: Fully supported via native plugin manifest [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) and startup hooks in [`hooks/`](hooks/).
* **🔵 Cursor**: Native rules in [`.cursor/rules/agent-superpowers.mdc`](.cursor/rules/agent-superpowers.mdc).
* **🟠 Google Antigravity & Gemini CLI**: Native extension in [`extension.yaml`](extension.yaml).
* **🟢 OpenAI Codex**: Configured via [`.codex/INSTALL.md`](.codex/INSTALL.md).
* **🔌 Model Context Protocol (MCP)**: Run `python cli/superpowers.py serve-mcp` or plug [`mcp/server.py`](mcp/server.py) into Claude Desktop, Cursor, or Zed.

---

## 🚀 Quick CLI Verification

```bash
# List all 11 registered superpowers
python cli/superpowers.py list

# Validate specification compliance
python cli/superpowers.py validate

# Run the automated unit test suite
python -m unittest tests/test_skills.py
```

---

## 🤝 Contributing & Specification

Want to add a new superpower?
1. Follow our formal [Agent Skill Specification](docs/SPECIFICATION.md).
2. Submit a proposal using the [New Skill Template](.github/ISSUE_TEMPLATE/new_skill.yml).
3. Ensure CI checks pass (`python cli/superpowers.py validate`).

---

## 👤 Author

**Gabriele Dattile**  
* GitHub: [@GabrieleDattile](https://github.com/GabrieleDattile)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
