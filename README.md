<div align="center">

# ⚡ Agent Superpowers

**Production-grade, battle-tested skills for autonomous AI software engineers.**  
*Compatible with Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, and Model Context Protocol (MCP).*

[![GitHub Stars](https://img.shields.io/github/stars/GabrieleDattile/agent-superpowers?style=for-the-badge&color=yellow)](https://github.com/GabrieleDattile/agent-superpowers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Specification](https://img.shields.io/badge/Spec-Agent%20Skills%20v1.0-brightgreen?style=for-the-badge)](docs/SPECIFICATION.md)
[![Author](https://img.shields.io/badge/Created%20By-Gabriele%20Dattile-orange?style=for-the-badge)](https://github.com/GabrieleDattile)

<br/>

<img src="assets/demo.gif" alt="Agent Superpowers Terminal Demo" width="820"/>

<br/>
<br/>

</div>

---

## 💡 Why Agent Superpowers?

Most AI agents today **look at static code and guess fixes**. They hallucinate solutions, introduce silent regressions, blow through token budgets, and miss catastrophic edge cases.

**Agent Superpowers** transforms coding agents into **disciplined, scientific software engineers** through strict operational protocols and deterministic runtime tooling.

* 🔬 **No Guesswork**: Prohibits editing production code until a minimal failing test reproduces the bug in isolation.
* ⚔️ **Offensive Audit**: Pits an adversarial hacker AI against proposed PRs with extreme boundary payloads before merge.
* 📉 **Token Efficiency**: Compresses context and source files by 50-70% via AST parsing without semantic loss.
* 🔌 **Zero-Friction SDKs**: Turns raw network traffic (cURL or HAR logs) into typed client SDKs in seconds.
* 🗺️ **Codebase Cartography**: Maps spaghetti architectures and detects dead zombie functions automatically.

---

## 📦 The Skills Suite

Each skill is fully autonomous, self-contained, and follows the [Agent Skill Specification](docs/SPECIFICATION.md).

| Skill | Category | Description | Primary Capabilities |
| :--- | :--- | :--- | :--- |
| [**`ghost-runner`**](skills/debugging/ghost-runner/SKILL.md) | 🔍 Debugging | Zero-assumption bug replicator | Strict Test-Driven Remediation, auto-creates isolated MRE, verifies RED then GREEN |
| [**`adversarial-duelist`**](skills/security/adversarial-duelist/SKILL.md) | 🛡️ Security | Pre-commit red-team fuzzer | Injects null-bytes, zero-divisions, SQLi vectors, and boundary overflows against functions |
| [**`token-squeezer`**](skills/optimization/token-squeezer/SKILL.md) | ⚡ Optimization | AST-based context compressor | Shrinks codebase context by 50-70%, extracts pure type interfaces, cuts LLM API costs |
| [**`api-synthesizer`**](skills/reverse-engineering/api-synthesizer/SKILL.md) | 🔌 Integration | Reverse-engineer APIs to SDKs | Ingests cURL/HAR dumps, generates typed Python/TypeScript clients with session handling |
| [**`arch-archaeologist`**](skills/architecture/arch-archaeologist/SKILL.md) | 🗺️ Architecture | Monolith & dependency cartographer | Traces module call graphs, exposes dead/zombie functions, generates Mermaid.js diagrams |

---

## 🚀 Quick Start (60 Seconds)

### 1. Clone the repository
```bash
git clone https://github.com/GabrieleDattile/agent-superpowers.git
cd agent-superpowers
```

### 2. Verify installed skills
```bash
python cli/superpowers.py list
```

### 3. Run a quick check
Test the skills validator or run any skill engine directly:
```bash
# Validate specification compliance
python cli/superpowers.py validate

# Run Ghost-Runner on sample test
python skills/debugging/ghost-runner/scripts/ghost_runner.py reproduce --test "python skills/debugging/ghost-runner/examples/test_reproduce.py"

# Run Adversarial Duelist red-team audit
python skills/security/adversarial-duelist/scripts/duelist.py --target skills/security/adversarial-duelist/examples/vulnerable_auth.py --func process_transaction
```

---

## 🛠️ IDE & Agent Integration

### Claude Code
Add skills directly to your project's `.claude/skills/` directory. Claude Code will automatically index each `SKILL.md` and load it on matching user prompts.

### Cursor & Windsurf
Include the instructions from any target `SKILL.md` into your `.cursorrules` or `.windsurfrules`. See our [IDE Compatibility Guide](docs/COMPATIBILITY.md) for pre-built rule templates.

### Model Context Protocol (MCP)
All deterministic tools in `scripts/` can be registered as standard MCP servers. Run the CLI bridge:
```bash
python cli/superpowers.py serve-mcp
```

---

## 📖 Standard Architecture

All skills implement **Progressive Context Loading**:
```text
skills/<category>/<skill-name>/
├── SKILL.md            # Spec, triggers, system prompt, negative constraints
├── scripts/            # Deterministic Python/Bash tools (zero LLM hallucinations)
└── examples/           # Test targets, samples, and few-shot fixtures
```

Read the full [Agent Skill Specification](docs/SPECIFICATION.md) to author your own skills.

---

## 🤝 Contributing

We welcome community-contributed skills!
1. Read the [Contributing Guidelines](CONTRIBUTING.md).
2. Use the [Skill Proposal Template](.github/ISSUE_TEMPLATE/new_skill.yml).
3. Ensure all tests and specification checks pass (`python cli/superpowers.py validate`).

---

## 👤 Author

**Gabriele Dattile**
* GitHub: [@GabrieleDattile](https://github.com/GabrieleDattile)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
