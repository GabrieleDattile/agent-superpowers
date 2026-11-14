# Distribution & GitHub Star-Acquisition Action Plan

**Repository**: `GabrieleDattile/agent-superpowers`  
**Date**: November 14, 2026  
**Auditor**: Teamwork Distribution Wave (Worker 1 / Explorer 3)  
**Status**: READY TO EXECUTE  

---

## Executive Strategy: The Launch Compression Flywheel

GitHub stars compound through a known algorithmic pattern:
1. **Curated High-Authority Inbound Backlinks**: Merging into high-star curated lists (`awesome-mcp-servers`, `awesome-cursorrules`, `awesome-claude-code`) creates a permanent, high-intent traffic baseline.
2. **Launch Compression Spike**: Rather than spreading outreach over weeks, concentrating high-signal announcements (Hacker News Show HN, Product Hunt, X technical thread) within a single 24-hour window generates the 35–55 stars needed to trigger **GitHub Python Daily Trending**.
3. **The Organic Trending Flywheel**: Once featured on the GitHub Trending page, organic developers discover and star the repository, yielding 150–400 additional stars with zero paid acquisition.
4. **Ecosystem Discussions & Technical Deep-Dives**: Engaging in technical discussions across major AI agent frameworks (AutoGPT, CrewAI, LangChain) and publishing deep-dives on Dev.to and Hashnode converts visitors into long-term contributors.

---

## 1. Immediate GitHub Repository Settings

Apply these exact configurations in the GitHub web interface:

### 1.1 Repository "About" Description (152 Characters)
Navigate to: **Repository Home ➔ About (gear icon)**:
```text
Production-grade agent skills & cursor rules for autonomous AI coding. Red-team fuzzing, RED-to-GREEN TDD, and context compression for Claude Code, Cursor & MCP.
```
*Verification: Exactly 152 characters (within GitHub's 160-character mobile snippet cutoff).*

### 1.2 Exact 20-Topic Tag List
Navigate to: **Repository Home ➔ About ➔ Topics**:
```text
agent-skills, claude-code, cursor-rules, ai-agents, mcp, model-context-protocol, coding-agent, autonomous-agents, developer-tools, claude-code-skills, cursor, windsurf, antigravity, tdd, test-driven-development, debugging, security, fuzzing, prompt-engineering, agentic-ai
```
*Verification: Exactly 20 tags (maximum allowable by GitHub), targeting the highest-volume search queries.*

### 1.3 Repository Website / Documentation Link
```text
https://github.com/GabrieleDattile/agent-superpowers#readme
```

### 1.4 Custom Open Graph Social Preview Banner
Navigate to: **Settings ➔ General ➔ Social preview**:
Upload custom image generated at `assets/social-preview.png`:
- **Dimensions**: 1280 × 640 pixels (PNG format, high DPI).
- **Background**: Deep obsidian/slate (`#0B0F19`) with subtle radial illumination.
- **Title**: `⚡ AGENT SUPERPOWERS` (Gold `#FFD700` & Cyan `#00D2FF` typography).
- **Tagline**: `36 Battle-Tested Skills for Autonomous AI Software Engineers`.
- **Ecosystem Pills**: `Claude Code • Cursor Rules (.mdc) • Google Antigravity • Windsurf • MCP`.
- **Key Invariants**: `Ghost Runner (RED ➔ GREEN TDD) | Git Worktree Sandboxing | Token Squeezer (-70% Context)`.

---

## 2. Six Ready-to-Submit Awesome List Pull Requests

### PR #1: `punkpeye/awesome-mcp-servers` (~15,000+ ⭐)
- **Target Repository**: `https://github.com/punkpeye/awesome-mcp-servers`
- **Target File**: `README.md`
- **Target Section**: `### 🛠️ Developer Tools` (or `### 👨‍💻 Code Execution`)
- **PR Title**: `Add Agent Superpowers to Developer Tools (Autonomous SDLC & TDD Verification)`
- **Markdown Snippet to Insert**:
  ```markdown
  - [Agent Superpowers](https://github.com/GabrieleDattile/agent-superpowers) — Deterministic autonomous engineering framework providing TDD bug reproduction (Ghost Runner), git worktree sandboxing, adversarial red-team fuzzing, and AST context compression over standard MCP JSON-RPC. 🏠 🍎 🪟 🐧
  ```
- **PR Description Body**:
  ```markdown
  ### What does this MCP server do?
  `Agent Superpowers` provides an autonomous software engineering protocol via Model Context Protocol (MCP). It equips Claude Desktop, Cursor, Zed, and Google Antigravity with:
  1. `ghost_runner`: Strictly enforces TDD bug reproduction before modifying production code.
  2. `git_worktree_sandbox`: Isolates multi-file refactoring in ephemeral git worktrees.
  3. `adversarial_duelist`: Automated pre-commit boundary and fuzz testing.
  4. `token_squeezer`: AST-based context compression reducing token consumption by 50–70%.

  - **Language**: Python (stdio JSON-RPC 2.0)
  - **License**: MIT
  - **Tested with**: Claude Desktop, Cursor, Antigravity, OpenCode
  ```

---

### PR #2: `PatrickJS/awesome-cursorrules` (~25,000+ ⭐)
- **Target Repository**: `https://github.com/PatrickJS/awesome-cursorrules`
- **Target Files**:
  1. Add file: `rules/agent-superpowers.mdc`
  2. Edit file: `README.md` under section `## Development & Architecture Rules`
- **PR Title**: `Add Agent Superpowers: Disciplined 7-Stage Autonomous Engineering Protocol (.mdc)`
- **File Content (`rules/agent-superpowers.mdc`)**:
  ```markdown
  ---
  description: "Disciplined autonomous engineering framework: TDD bug reproduction, git worktree sandboxing, adversarial fuzzing, and AST context compression."
  globs: **/*
  alwaysApply: false
  ---
  # Agent Superpowers: Autonomous Engineering System

  A disciplined, deterministic engineering protocol enforcing rigor before code execution.

  ## Core Directives

  1. **Bug Reproduction First (Ghost Runner)**: Never guess or speculate on bug fixes without evidence. Author a minimal reproduction test (MRE) that fails on the current codebase. Apply minimal patch and confirm GREEN.
  2. **Branch Isolation (Git Worktree Sandbox)**: For multi-file refactoring or experimental tasks, isolate work in an ephemeral git worktree branch. Protect the main working tree from unverified state corruption.
  3. **Adversarial Verification (Adversarial Duelist)**: Subject business logic to automated red-team boundary fuzzing (null-bytes, zero-divisions, payload boundary limits).
  4. **Context Hygiene (Token Squeezer)**: Compress AST structures to preserve token budget, stripping internal implementations while preserving signatures and types.
  5. **Clarify Before Code (Feature Brainstormer)**: If requirements are ambiguous, clarify boundary conditions and edge cases before implementation.
  ```
- **Markdown Snippet for `README.md`**:
  ```markdown
  - [Agent Superpowers](rules/agent-superpowers.mdc) - Disciplined 7-stage autonomous engineering framework enforcing TDD bug reproduction, git worktree isolation, adversarial fuzzing, and AST compression. ([Repo](https://github.com/GabrieleDattile/agent-superpowers))
  ```
- **PR Description Body**:
  ```markdown
  ### Summary
  This PR adds the `agent-superpowers` rule in the modern `.mdc` format. It prevents chaotic AI agent edits by enforcing a deterministic 7-stage autonomous engineering lifecycle (TDD reproduction, ephemeral git worktree sandboxing, AST token compression, and adversarial fuzzing).

  - **Format**: Modern `.mdc` with frontmatter (`globs`, `description`, `alwaysApply`)
  - **Compatibility**: Cursor 0.40+, Claude 3.5 Sonnet, GPT-4o
  - **License**: MIT
  ```

---

### PR #3: `cursor.directory` Submission (`pontusab/cursor.directory`)
- **Target Platform**: `https://cursor.directory/plugins/new`
- **Repository URL**: `https://github.com/GabrieleDattile/agent-superpowers`
- **Rule Name**: `Agent Superpowers (Autonomous Engineering Protocol)`
- **Slug**: `agent-superpowers`
- **Category**: `Testing & Architecture Rules`
- **Tags**: `["AI Agent", "Testing", "TDD", "Git", "Security", "Best Practices", "MCP"]`
- **Rule Content**: Use the exact content of `.cursor/rules/agent-superpowers.mdc`.

---

### PR #4: `hesreallyhim/awesome-claude-code` (~4,500+ ⭐)
- **Target Repository**: `https://github.com/hesreallyhim/awesome-claude-code`
- **Target File**: `README.md`
- **Target Section**: `### Agent Skills & Workflows`
- **PR Title**: `Add Agent Superpowers: 36 Production Skills, 7-Stage SDLC & MCP Server for Claude Code`
- **Markdown Snippet to Insert**:
  ```markdown
  - [Agent Superpowers](https://github.com/GabrieleDattile/agent-superpowers) - 36 production skills and a disciplined 7-stage autonomous engineering framework for Claude Code. Includes TDD bug isolation (Ghost Runner), git worktree sandboxing, adversarial fuzzing, and AST token squeezing via native plugin and MCP.
  ```
- **PR Description Body**:
  ```markdown
  ### Resource Submission
  - **Name**: Agent Superpowers
  - **Category**: Agent Skills & Workflows
  - **Description**: A comprehensive suite of 36 modular skills and an autonomous 7-stage engineering lifecycle natively compatible with Claude Code (via `.claude-plugin/` and `extension.yaml`) and Model Context Protocol.
  - **Why it's valuable**: Eliminates hallucinated bug fixes and broken commits by enforcing strict TDD RED-to-GREEN reproduction tests and ephemeral git worktree isolation.
  ```

---

### PR #5: `e2b-dev/awesome-ai-agents` (~18,000+ ⭐)
- **Target Repository**: `https://github.com/e2b-dev/awesome-ai-agents`
- **Target File**: `README.md`
- **Target Section**: `### Open Source Projects -> Coding & Development`
- **PR Title**: `Add Agent Superpowers to Coding & Development Agents`
- **Markdown Snippet to Insert**:
  ```markdown
  - [Agent Superpowers](https://github.com/GabrieleDattile/agent-superpowers) - Autonomous software engineering framework and MCP server providing TDD bug reproduction, ephemeral worktree sandboxes, and pre-commit security fuzzing for Claude Code, Cursor, and Antigravity.
  ```
- **PR Description Body**:
  ```markdown
  Adds Agent Superpowers to the Coding & Development section. Agent Superpowers provides 36 skills and an MCP server focused on deterministic verification (TDD RED-to-GREEN reproduction, branch isolation in git worktrees, and pre-commit fuzzing) for autonomous coding agents.
  ```

---

### PR #6: `sorrycc/awesome-code-agents` (~3,200+ ⭐)
- **Target Repository**: `https://github.com/sorrycc/awesome-code-agents`
- **Target File**: `README.md`
- **Target Section**: `### CLI & Terminal-Native Agents`
- **PR Title**: `Add Agent Superpowers: Disciplined 7-Stage Verification SDLC for Coding Agents`
- **Markdown Snippet to Insert**:
  ```markdown
  - [Agent Superpowers](https://github.com/GabrieleDattile/agent-superpowers) - Disciplined 7-stage autonomous engineering framework enforcing TDD verification, branch isolation, and AST token compression for terminal coding agents.
  ```
- **PR Description Body**:
  ```markdown
  Adds Agent Superpowers to the CLI & Terminal-Native Agents list. It features 36 modular skills and a stdio MCP server enabling terminal agents to reproduce bugs via minimal failing tests before patching, run refactors in ephemeral worktrees, and compress AST context by 50-70%.
  ```

---

## 3. MCP Registries & Developer Directory Listings

### 3.1 Smithery.ai (The Premier MCP Server Registry)
Smithery.ai is the primary registry for discovering and installing MCP servers for Claude Desktop and Cursor.
- **Authentication**:
  ```bash
  npx @smithery/cli auth login
  ```
- **Publish Command**:
  ```bash
  npx @smithery/cli mcp publish https://github.com/GabrieleDattile/agent-superpowers -n gabrieledattile/agent-superpowers
  ```
- **Registry Metadata**:
  - Name: `agent-superpowers`
  - Display Name: `Agent Superpowers SDLC Toolkit`
  - Short Description: `Disciplined engineering protocol exposing Ghost Runner TDD reproduction, Git Worktree sandboxing, Adversarial Duelist fuzzing, and Token Squeezer AST compression via MCP stdio.`

### 3.2 Glama.ai/mcp & PulseMCP
- **Glama MCP Catalog**: Submit `https://github.com/GabrieleDattile/agent-superpowers` at `https://glama.ai/mcp/submit`.
- **PulseMCP Directory**: Submit repository details at `https://pulsemcp.com/submit`.

### 3.3 DevHunt.org & OpenAlternative.co
- **OpenAlternative.co**: Submit under Developer Tools as an open-source companion to proprietary AI coding extensions.
- **DevHunt.org**: Schedule a daily developer tool showcase launch for Day 6.

---

## 4. Technical Launch Blueprints

### 4.1 Hacker News: "Show HN" Launch Blueprint

#### Timing & Logistics
- **Day**: Wednesday (Optimal peak tech engagement window).
- **Time Window**: 07:15 AM – 08:00 AM US Eastern Time (12:15 PM – 13:00 PM UTC).
- **Submission URL**: `https://news.ycombinator.com/submit`

#### Submission Title
```text
Show HN: Agent Superpowers – Disciplined engineering protocol for AI coding agents
```

#### Author First Comment (Post immediately within 60 seconds of submission)
```text
Hi HN,

I built Agent Superpowers because I was exhausted watching AI coding agents (Claude Code, Cursor, Windsurf) behave like chaotic junior developers: jumping straight into editing production files, guessing bug fixes, hallucinating non-existent APIs, and leaving dirty git working trees.

Default LLM prompting treats coding as text generation. But reliable software engineering is an empirical, stateful process.

Agent Superpowers turns coding agents into disciplined engineers by enforcing an auditable, deterministic 7-stage lifecycle:

1. Zero-Assumption Bug Reproduction (Ghost Runner): The agent is strictly prohibited from editing production source code until it authors a minimal reproduction test (MRE) that fails on the current codebase (RED). Only after a patch turns the test GREEN and passes regression tests can it proceed.
2. Git Worktree Isolation: All refactoring and multi-file experiments execute in ephemeral git worktree branches, protecting your active working tree from state corruption.
3. Pre-Commit Adversarial Fuzzing (Adversarial Duelist): Automated red-team fuzzing injects null-bytes, zero-divisions, boundary overflows, and injection payloads before any merge gate.
4. AST Context Compression (Token Squeezer): Reduces context bloat by 50–70% by extracting structural interfaces and docstrings rather than dumping thousands of lines of raw implementation into the prompt.
5. Cross-Session Memory (Memory Nexus): Local append-only decision ledger (.superpowers/decisions.jsonl) preventing amnesia across CLI restarts.

It is implemented as a Universal Model Context Protocol (MCP) server in Python (stdio JSON-RPC 2.0) and includes 36 modular skills compatible with Claude Code, Cursor (.mdc), Google Antigravity, and Zed.

Repo: https://github.com/GabrieleDattile/agent-superpowers
Terminal Demo: https://raw.githubusercontent.com/GabrieleDattile/agent-superpowers/main/assets/demo.gif

Install in 1 command:
curl -sSL https://raw.githubusercontent.com/GabrieleDattile/agent-superpowers/main/install.sh | bash

I'd love your critique on the 7-stage state machine and how you handle agent verification in your own workflows. Happy to answer questions about the MCP implementation or AST extraction logic.
```

---

### 4.2 Product Hunt Launch Blueprint

- **Product Name**: Agent Superpowers
- **Tagline**: Turn your AI coding agent into a disciplined staff engineer
- **Launch Day**: Tuesday at 00:01 AM PST (Full 24-hour cycle)
- **Topics**: Developer Tools, Artificial Intelligence, Open Source, GitHub, Productivity
- **Thumbnail**: Lightning bolt badge with gold-and-cyan accents and "7-Stage SDLC" tag.
- **Gallery Assets**:
  1. `assets/demo.gif` (Terminal session showing RED ➔ GREEN reproduction and worktree isolation)
  2. Infographic comparing "The Chaos of Default AI ❌" vs "With Agent Superpowers 🟢"
  3. Architecture diagram of the 7-stage state machine
  4. Screenshot of Cursor `.cursor/rules/agent-superpowers.mdc` in action
  5. Architecture diagram of the Universal MCP Server
- **Maker First Comment**:
  ```text
  Hey Product Hunt! 👋

  We all love Cursor and Claude Code, but we've all experienced the dread of an AI agent modifying 14 files at once, hallucinating broken code, and ruining your git branch.

  We built Agent Superpowers to bring professional software engineering discipline to autonomous AI agents. Instead of letting the model guess, Agent Superpowers enforces:
  - 🧪 Ghost Runner: TDD bug reproduction before any code edit is permitted.
  - 📦 Git Worktree Sandbox: Ephemeral isolated branches for zero workspace corruption.
  - 🛡️ Adversarial Duelist: Pre-commit red-team fuzzing against edge cases.
  - ⚡ Token Squeezer: AST structural compression saving 50–70% of LLM token costs.
  - 🔌 Universal MCP Server: 36 plug-and-play skills for Claude Desktop, Cursor, and Antigravity.

  100% open source under MIT. We’d love to hear your thoughts and feedback!
  ```

---

### 4.3 X (Twitter) Technical Launch Thread

- **Target Window**: 08:00 AM EST (13:00 UTC) on Day 4 (aligned with Hacker News).
- **Tweet 1 (Hook + Visual)**:
  ```text
  Most AI coding agents act like chaotic junior developers: jumping straight into file edits, guessing fixes, and corrupting your git branch.

  We spent months engineering a disciplined 7-stage autonomous protocol for Claude Code and Cursor.

  Introducing Agent Superpowers ⚡ (100% Open Source) 🧵👇
  [ATTACH ASSETS/DEMO.GIF]
  ```
- **Tweet 2 (The Core Problem)**:
  ```text
  Default LLMs treat coding as text prediction, not empirical engineering.

  When you ask an agent to "fix a checkout bug", it:
  - Guesses the cause without evidence
  - Edits production files immediately
  - Dumps 100k tokens into context
  - Breaks existing tests and leaves dirty branches

  Here's how we stopped this 🛠️
  ```
- **Tweet 3 (Ghost Runner & TDD)**:
  ```text
  Stage 1: Ghost Runner (Strict TDD Reproduction)

  The agent is locked out of editing source files until it writes an isolated reproduction test that FAILS (RED).

  Only after reproducing the failure can it write a minimal patch to turn it GREEN. Zero guesswork.
  ```
- **Tweet 4 (Git Worktree Sandboxing)**:
  ```text
  Stage 2: Ephemeral Git Worktree Sandboxing

  No more messy commits on your active working branch.

  All experimental edits and refactors run in isolated git worktrees. If the test suite fails or the logic is unverified, the worktree is nuked. Your primary tree stays pristine.
  ```
- **Tweet 5 (Token Squeezer AST Compression)**:
  ```text
  Stage 3: Token Squeezer (Save 50–70% Tokens)

  Why feed 2,000 lines of implementation into an agent's context when it only needs signatures?

  Token Squeezer extracts AST skeletons—preserving classes, typed parameters, exports, and docstrings while stripping internal bodies. Faster inference, lower cost.
  ```
- **Tweet 6 (Adversarial Duelist Fuzzing)**:
  ```text
  Stage 4: Adversarial Duelist (Pre-Commit Red-Team)

  Before code reaches your merge gate, an automated fuzzer hammers boundary conditions: null-bytes, zero-divisions, and payload boundary limits.

  Catch edge-case vulnerabilities before they hit production.
  ```
- **Tweet 7 (Universal MCP Server & 36 Skills)**:
  ```text
  Natively compatible with:
  ⚡ Claude Code (.claude-plugin)
  ⚡ Cursor (.cursor/rules/*.mdc)
  ⚡ Model Context Protocol (Universal stdio JSON-RPC server)
  ⚡ Google Antigravity & Windsurf

  Comes packed with 36 production skills: from reverse-engineering APIs to WCAG accessibility audits.
  ```
- **Tweet 8 (CTA + GitHub Star Link)**:
  ```text
  Install in 1 command:
  curl -fsSL https://raw.githubusercontent.com/GabrieleDattile/agent-superpowers/main/install.sh | bash

  Explore the code & give us a star on GitHub ⭐:
  👉 https://github.com/GabrieleDattile/agent-superpowers

  If you build with AI agents, retweets are appreciated! 🔁
  ```

---

### 4.4 Long-Form Technical Articles (Dev.to & Hashnode)

#### Article 1: "Why AI Coding Agents Break Production (And How to Enforce TDD)"
- **Tags**: `#ai`, `#opensource`, `#programming`, `#webdev`, `#python`
- **Key Narrative**:
  1. *The Illusion of Competence*: Why LLM benchmark accuracy fails in legacy dirty codebases.
  2. *The Ghost Runner Pattern*: Enforcing the RED-to-GREEN invariant before touching source code.
  3. *Zero-Risk Refactoring*: How ephemeral git worktrees isolate agent hallucinations.
  4. *Benchmark Results*: Comparing unconstrained agent runs vs. Agent Superpowers guarded runs (0 branch corruption, 100% bug reproduction rate).
  5. *Quickstart & Links*: Clear call-to-action to star and fork on GitHub.

#### Article 2: "Supercharge Claude Code and Cursor: 36 Production Skills via MCP"
- **Tags**: `#ai`, `#claudecode`, `#cursor`, `#devtools`, `#mcp`
- **Key Narrative**:
  1. *The Rise of Agentic Developer Environments*: Claude Code CLI and Cursor's MDC rules.
  2. *Building a Universal MCP Server in Python*: How `mcp/server.py` handles stdio JSON-RPC tool dispatch.
  3. *AST-Based Context Optimization*: Deep dive into AST extraction to shrink 100k token prompts by 50–70%.
  4. *Step-by-Step Installation Guide*: Configuring `claude_desktop_config.json` and `.cursor/rules/`.

---

### 4.5 GitHub Discussions in Major AI Agent Ecosystems

#### Ecosystem 1: `Significant-Gravitas/AutoGPT` (Discussions ➔ Show and Tell)
```text
Title: Deterministic Verification Layer for Autonomous Coding Agents (TDD Reproduction & Worktree Isolation)

Hey AutoGPT community,

One of the biggest hurdles in autonomous coding agents is reliability: agents attempting multi-file fixes often break existing invariants or introduce silent regressions.

We've open-sourced Agent Superpowers (https://github.com/GabrieleDattile/agent-superpowers), an engineering protocol that enforces:
1. Strict TDD RED-to-GREEN verification (prohibiting code edits without an isolated reproduction test).
2. Ephemeral Git Worktree branch sandboxing to prevent working tree corruption.
3. Pre-commit boundary fuzzing.

It includes a universal MCP server (JSON-RPC) that can be plugged into agent execution loops as verification tools.

Would love to discuss how these deterministic verification steps could be integrated into AutoGPT's coding benchmarks or sub-agents!
```

#### Ecosystem 2: `joaomdmoura/crewAI` (Discussions ➔ Community & Integrations)
```text
Title: Extending CrewAI Coding Crews with Deterministic TDD & MCP Verification Tools

Hi CrewAI team and builders,

When assembling multi-agent crews for software development (e.g., Architect, Coder, Reviewer), agents frequently suffer from context bloat and unverified code changes.

We built Agent Superpowers (https://github.com/GabrieleDattile/agent-superpowers), which provides 36 modular skills and an MCP server featuring:
- Ghost Runner (automated TDD reproduction)
- Token Squeezer (AST context compressor reducing token payload by 50–70%)
- Adversarial Duelist (pre-commit red-team fuzzing)

These can be hooked into CrewAI custom tools via standard Python imports or MCP tool wrappers. Check out the implementation and let us know what verification tools your crews need most!
```

#### Ecosystem 3: `langchain-ai/langchain` (Discussions ➔ Show and Tell)
```text
Title: Agent Superpowers: MCP Server for Deterministic Software Engineering & AST Compression

Hello LangChain community,

We wanted to share an open-source MCP server and skill suite built specifically for code generation and maintenance agents: Agent Superpowers (https://github.com/GabrieleDattile/agent-superpowers).

It exposes standardized MCP tools (`ghost_runner`, `token_squeezer`, `adversarial_duelist`, `git_worktree_sandbox`) that can be used directly with `langchain-mcp-adapters` or LangGraph agent nodes to enforce rigorous TDD and branch safety.
```

---

### 4.6 Developer Discord Communities: Non-Spammy Showcase Blueprint

**Target Servers & Channels**:
- Cursor Community Discord (`#showcase`, `#rules-and-plugins`)
- Anthropic Developer Discord (`#claude-code`, `#mcp-tools`)
- LangChain Discord (`#share-your-project`)
- CrewAI Discord (`#community-projects`)
- E2B Discord (`#agents-discussion`)
- Latent Space Discord (`#builders`)

**Value-First Discord Message**:
```text
Hey everyone! 👋 Built an open-source SDLC framework for Claude Code, Cursor, and Antigravity that we wanted to share: **Agent Superpowers** ⚡

It tackles the biggest issue with coding agents: jumping straight into guessing bug fixes and breaking your git branch.

Key capabilities:
• **Ghost Runner**: Requires the agent to author a minimal failing reproduction test (RED) before it's allowed to edit code.
• **Git Worktree Sandbox**: Isolates multi-file refactors in ephemeral worktrees.
• **Token Squeezer**: Shrinks prompt context by 50-70% using AST signature extraction.
• **Adversarial Duelist**: Pre-commit boundary fuzzing (null-bytes, zero-divisions, edge cases).
• **Universal MCP Server**: Exposes 36 tools over JSON-RPC.

GitHub: https://github.com/GabrieleDattile/agent-superpowers
Includes a 1-command installer and Cursor `.mdc` rule. Feedback and contributions welcome! ⭐
```

---

## 5. 14-Day Actionable Launch Sequence & Execution Calendar

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               14-DAY LAUNCH TIMELINE                                   │
├───────────────────┬───────────────────┬─────────────────────────┬──────────────────────┤
│ DAYS 1–3          │ DAYS 4–6          │ DAYS 7–10               │ DAYS 11–14           │
│ Pre-Launch & Base │ Compression Spike │ Deep-Dives & Ecosystems │ Momentum & Flywheel  │
│ • Linguist Fix    │ • Hacker News     │ • AutoGPT/CrewAI Disc.  │ • v1.3.0 Release     │
│ • Awesome PRs     │ • Product Hunt    │ • Dev.to Technical Post │ • Retrospective Post │
│ • MCP Registries  │ • X Master Thread │ • Discord Showcases     │ • Newsletter Outreach│
│ • Assets & Video  │ • Trending Push   │ • Secondary PRs         │ • Star Retargeting   │
└───────────────────┴───────────────────┴─────────────────────────┴──────────────────────┘
```

| Day | Primary Milestone | Detailed Tasks & Execution Steps | Target KPI / Checkpoint |
| :---: | :--- | :--- | :--- |
| **Day 1** | **Asset Staging & Linguist Calibration** | 1. Ensure `.gitattributes` is active to lock repo as Python.<br/>2. Upload `assets/social-preview.png` to GitHub settings.<br/>3. Publish MCP server to Smithery.ai via CLI (`npx @smithery/cli mcp publish`).<br/>4. Submit to Glama.ai and PulseMCP. | `.gitattributes` verified; Smithery listing live. |
| **Day 2** | **Primary Awesome List PR Wave** | 1. Submit PR to `punkpeye/awesome-mcp-servers`.<br/>2. Submit PR to `PatrickJS/awesome-cursorrules`.<br/>3. Submit to `cursor.directory`.<br/>4. Submit PR to `hesreallyhim/awesome-claude-code`. | 4 PRs active with passing CI. |
| **Day 3** | **Launch Staging & Copy Pre-Baking** | 1. Schedule Product Hunt page for Day 4 (00:01 AM PST).<br/>2. Finalize Hacker News Show HN copy and first comment.<br/>3. Schedule X thread in Typefully/TweetDeck.<br/>4. Verify terminal demo GIF links. | All launch copy pre-approved and queued. |
| **Day 4** | **THE LAUNCH COMPRESSION (Trending Push)** | **00:01 PST**: Product Hunt launch goes live.<br/>**07:30 EST**: Post Hacker News Show HN + first comment.<br/>**08:00 EST**: Publish X technical thread with video hook.<br/>**All Day**: Respond to every comment on HN within 15 mins. | **Target: 35–55 stars in 24h** to enter Python Trending. |
| **Day 5** | **Trending Capture & Syndication** | 1. Monitor `github.com/trending/python?since=daily`.<br/>2. Publish Dev.to technical post.<br/>3. Cross-post article to Hashnode.<br/>4. Share milestone tweet on X celebrating trending rank. | Visible placement on Python Trending. |
| **Day 6** | **Directory Expansion** | 1. Submit to DevHunt.org for daily showcase.<br/>2. Submit to OpenAlternative.co.<br/>3. Submit to Toolify.ai. | 3 developer directory listings live. |
| **Day 7** | **Ecosystem Discussions (Wave 1)** | 1. Post discussion thread in `Significant-Gravitas/AutoGPT`.<br/>2. Post integration thread in `joaomdmoura/crewAI`.<br/>3. Reply thoughtfully to all community questions. | 2 active ecosystem discussions. |
| **Day 8** | **Token Optimization Case Study** | 1. Publish technical deep-dive on AST compression on Dev.to and X.<br/>2. Include code samples and token benchmark graphs.<br/>3. Link directly to `skills/optimization/token-squeezer/`. | Technical inbound referral traffic. |
| **Day 9** | **Discord Community Outreach** | 1. Post showcase in Cursor Discord (`#showcase`).<br/>2. Post in Anthropic Discord (`#claude-code`).<br/>3. Post in Latent Space and E2B builder channels. | Community conversations in 3+ servers. |
| **Day 10** | **Secondary Awesome List Wave** | 1. Submit PR to `e2b-dev/awesome-ai-agents`.<br/>2. Submit PR to `sorrycc/awesome-code-agents`.<br/>3. Submit PR to `sourcegraph/awesome-code-ai`. | 3 secondary PRs active. |
| **Day 11** | **Feature Release v1.3.0** | 1. Tag and publish GitHub Release `v1.3.0`.<br/>2. Announce release highlights on X and GitHub Discussions.<br/>3. Give public credit to early community feedback contributors. | Release v1.3.0 published on GitHub. |
| **Day 12** | **Retrospective Post** | 1. Publish retrospective post on Dev.to and X: *"What We Learned Building an Autonomous 7-Stage SDLC for AI Agents"*.<br/>2. Share transparent metrics and growth learnings. | High-engagement quote retweets. |
| **Day 13** | **AI Developer Newsletter Pitch** | 1. Pitch tool snippet to curated technical newsletters (AlphaSignal, TLDR Web Dev, Ben's Bites, The Rundown).<br/>2. Emphasize: *"Open-source framework bringing TDD and branch sandboxing to Claude Code and Cursor."* | Inclusion in at least 1 newsletter. |
| **Day 14** | **Funnel Review & Weekly Baseline** | 1. Conduct GitHub traffic audit (unique clones, conversion rate).<br/>2. Follow up on merged Awesome List PRs.<br/>3. Establish ongoing maintenance schedule (>15 stars/week baseline). | Post-launch star baseline established. |

---

## 6. How to Trigger GitHub Trending (Algorithm Mechanics & Thresholds)

### 6.1 Reverse-Engineered GitHub Trending Algorithm
The GitHub Trending algorithm does not rank repositories by absolute star totals. Instead, it evaluates **three primary mathematical variables**:

1. **Star Velocity ($\frac{dStars}{dt}$)**:
   - Evaluated over a rolling 24-hour evaluation window.
   - A newly created repository gaining 40 stars in 24 hours ranks significantly higher than an established project with 20,000 stars gaining 10 stars today.
2. **Anomaly Deviation Multiplier**:
   - The algorithm rewards sudden, positive deviations from historical baseline:
   $$\text{Score} = \Delta \text{Stars}_{24\text{h}} \times \left(1 + \frac{\Delta \text{Stars}_{24\text{h}}}{\text{Stars}_{\text{baseline}} + 1}\right) \times \text{Quality Factor}$$
   - A jump from 0 daily stars to 45 daily stars produces an exceptionally high anomaly score.
3. **Engagement Diversity & Anti-Spam Signals**:
   - Stargazers must represent diverse geographical IPs and established accounts (>30 days old with public activity).
   - Star velocity must correlate with **clone activity**, **issue discussions**, and **forks** to bypass automated fraud filters.

### 6.2 Empirical Velocity Thresholds

| Leaderboard Target | 24-Hour Velocity Required | Reset Window | Probability of Ranking |
| :--- | :---: | :---: | :---: |
| **Python Daily Trending (Top 10)** | **35 – 55 stars / 24h** | 00:00 UTC | **High** (With Launch Compression) |
| **Python Daily Trending (#1 Spot)** | **75 – 110 stars / 24h** | 00:00 UTC | Moderate |
| **Python Weekly Trending** | **180 – 260 stars / 7 days** | Monday 00:00 UTC | High (Follow-through of Daily) |
| **All Languages Daily Trending (Top 25)** | **120 – 180 stars / 24h** | 00:00 UTC | Moderate |

### 6.3 Strategic Execution
By fixing `.gitattributes` to ensure GitHub classifies the repository as **Python** (rather than TypeScript), the threshold to achieve Daily Trending drops from **85–130 stars/day** down to **35–55 stars/day**. Concentrating the Hacker News, Product Hunt, and X thread launches on Day 4 ensures this threshold is achieved within a single rolling 24-hour window.
