/**
 * Agent Superpowers: Universal TypeScript SDK
 * Author: Gabriele Dattile (https://github.com/GabrieleDattile)
 */

export type SkillCategory =
  | "orchestration"
  | "workflow"
  | "frontend"
  | "memory"
  | "debugging"
  | "security"
  | "optimization"
  | "reverse-engineering"
  | "architecture"
  | "scraping"
  | "testing"
  | "multimedia";

export interface AgentSkill {
  name: string;
  version: string;
  description: string;
  category: SkillCategory;
  compatibility: string[];
  tags: string[];
}

export const SUPERPOWERS_CATALOG: AgentSkill[] = [
  {
    "name": "adversarial-duelist",
    "version": "1.0.0",
    "description": "Adversarial red-team auditor. Generates malicious edge-case payloads, fuzzing vectors, and exploit scripts against proposed code before merge.",
    "category": "security",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "security",
      "red-team",
      "fuzzing",
      "audit",
      "pr-review"
    ]
  },
  {
    "name": "agent-reach",
    "version": "1.0.0",
    "description": "\u53ea\u8bfb\u8bfb\u53d6\u5404\u5e73\u53f0\u5185\u5bb9\uff1a\u641c\u7d22\u3001\u8bfb\u5e16\u3001\u770b\u8bc4\u8bba\u3001\u53d6\u5b57\u5e55\u3001\u67e5\u884c\u60c5\u548c\u804c\u4f4d\u3002 Use when \u7528\u6237\u63d0\u5230\u6216\u8d34\u51fa\u94fe\u63a5\uff1a\u5c0f\u7ea2\u4e66/xiaohongshu\u3001B\u7ad9/bilibili\u3001Twitter/X\u3001Reddit\u3001 YouTube\uff08\u5b57\u5e55\u3001\u8f6c\u5f55\uff09\u3001GitHub\u3001V2EX\u3001\u96ea\u7403/\u80a1\u7968\u884c\u60c5\u3001LinkedIn/Boss\u76f4\u8058 \u804c\u4f4d\u3001 Insta...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "social",
      "search",
      "web",
      "reading"
    ]
  },
  {
    "name": "api-synthesizer",
    "version": "1.0.0",
    "description": "Autonomous API reverse-engineering engine. Converts raw network traffic (cURL commands or HAR files) into fully typed Python/TypeScript client SDKs.",
    "category": "reverse-engineering",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "reverse-engineering",
      "api",
      "sdk-generation",
      "networking"
    ]
  },
  {
    "name": "arch-archaeologist",
    "version": "1.0.0",
    "description": "Codebase cartographer and architecture archaeologist. Traces inter-module dependencies, identifies dead zombie functions, and emits living Mermaid.js archite...",
    "category": "architecture",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "architecture",
      "refactoring",
      "dependency-graph",
      "dead-code",
      "mermaid"
    ]
  },
  {
    "name": "blackbox-cloner",
    "version": "1.0.0",
    "description": "Clean-room software reverse engineering engine. Deconstructs proprietary tools, desktop utilities, and SaaS features (e.g. Adobe tools, Figma canvas, backgro...",
    "category": "reverse-engineering",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "Antigravity",
      "MCP"
    ],
    "tags": [
      "reverse-engineering",
      "cleanroom",
      "tool-cloning",
      "architecture",
      "scaffolding"
    ]
  },
  {
    "name": "caveman",
    "version": "1.0.0",
    "description": "Terse caveman voice: answer first, fluff gone, every technical fact kept. Use for /caveman, 'caveman mode', 'talk like caveman', 'be brief', 'less tokens'. S...",
    "category": "optimization",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "optimization",
      "tokens",
      "conciseness",
      "prompt"
    ]
  },
  {
    "name": "caveman-commit",
    "version": "1.0.0",
    "description": "Write a Conventional Commits message compressed to intent only. Use for 'write a commit', 'commit message', /commit or /caveman-commit.",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "git",
      "commits",
      "semantic"
    ]
  },
  {
    "name": "caveman-compress",
    "version": "1.0.0",
    "description": "Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. Sends the file's text to the con...",
    "category": "optimization",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "optimization",
      "tokens",
      "compression",
      "context"
    ]
  },
  {
    "name": "feature-brainstormer",
    "version": "1.1.0",
    "description": "Socratic feature brainstorming and requirement refiner. Prevents premature code generation by teasing out specifications, clarifying architectural tradeoffs,...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "planning",
      "brainstorming",
      "specification",
      "requirements"
    ]
  },
  {
    "name": "figma-designer",
    "version": "1.0.0",
    "description": "Design inside Figma the way this designer does: real variables, text styles, auto layout and components, on a fixed visual system (Tailwind type and radius s...",
    "category": "frontend",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "frontend",
      "design",
      "figma",
      "design-tokens"
    ]
  },
  {
    "name": "firecrawl-build",
    "version": "1.0.0",
    "description": "Integrate Firecrawl into application code whenever a product, agent, or workflow needs web data inside the app \u2014 web search, live search results, page scrapi...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "scraping",
      "web",
      "markdown",
      "firecrawl"
    ]
  },
  {
    "name": "firecrawl-build-interact",
    "version": "1.0.0",
    "description": "Integrate Firecrawl `/interact` into product code for dynamic pages and browser actions after scraping. Use when a feature needs clicks, form fills, paginati...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "browser",
      "actions",
      "automation",
      "firecrawl"
    ]
  },
  {
    "name": "firecrawl-build-onboarding",
    "version": "1.0.0",
    "description": "Get Firecrawl credentials and SDK setup into a project. Use when an application needs `FIRECRAWL_API_KEY`, when an agent should add Firecrawl to `.env`, when...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "onboarding",
      "auth",
      "setup",
      "firecrawl"
    ]
  },
  {
    "name": "firecrawl-build-scrape",
    "version": "1.0.0",
    "description": "Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, m...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "scraping",
      "web",
      "markdown",
      "extraction"
    ]
  },
  {
    "name": "firecrawl-build-search",
    "version": "1.0.0",
    "description": "Integrate Firecrawl `/search` into product code and agent workflows. Use when an app needs discovery before extraction, when the feature starts with a query ...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "search",
      "web",
      "discovery",
      "firecrawl"
    ]
  },
  {
    "name": "frontend-sentinel",
    "version": "1.0.0",
    "description": "Production frontend & UI/UX auditor. Scans React, Vue, Svelte, and HTML templates for accessibility defects, mobile viewport breaks, unhandled loading states...",
    "category": "frontend",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "frontend",
      "react",
      "vue",
      "ui-ux",
      "accessibility",
      "mobile-responsive",
      "audit"
    ]
  },
  {
    "name": "ghost-runner",
    "version": "1.0.0",
    "description": "Zero-assumption autonomous bug replicator. Prohibits touching production code until a minimal failing test reproduces the bug in isolation.",
    "category": "debugging",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "debugging",
      "tdd",
      "automated-testing",
      "reliability"
    ]
  },
  {
    "name": "git-worktree-sandbox",
    "version": "1.1.0",
    "description": "Ephemeral git worktree sandbox isolation. Guarantees that agent experiments, aggressive refactoring, and test suites run in isolated worktrees without corrup...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "git",
      "worktree",
      "sandbox",
      "safety",
      "isolation"
    ]
  },
  {
    "name": "graphify",
    "version": "1.0.0",
    "description": "Use for any question about a codebase, its architecture, file relationships, or project content \u2014 especially when graphify-out/ exists, where the question sh...",
    "category": "architecture",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "architecture",
      "knowledge-graph",
      "ast",
      "dependencies"
    ]
  },
  {
    "name": "hallmark",
    "version": "1.0.0",
    "description": "Anti-AI-slop design engine and UI audit toolkit. Overrides generic LLM aesthetic defaults (purple gradients, predictable rounded cards, unopinionated typogra...",
    "category": "frontend",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "frontend",
      "design",
      "anti-ai-slop",
      "themes",
      "sloplint",
      "ui-ux",
      "styling"
    ]
  },
  {
    "name": "hindsight-architect",
    "version": "1.0.0",
    "description": "Expert memory architect. Understands your application, identifies where memory adds value, and produces an implementation plan with bank config, tag schema, ...",
    "category": "architecture",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "architecture",
      "design",
      "memory",
      "decisions"
    ]
  },
  {
    "name": "hindsight-coding-agent",
    "version": "1.0.0",
    "description": "How this machine's Hindsight coding-agent memory works \u2014 the plugin behind the \ud83e\udde0 banner. Use when the user says 'store/remember this in hindsight', asks what...",
    "category": "memory",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "memory",
      "long-term",
      "learning",
      "context"
    ]
  },
  {
    "name": "landing-page-design",
    "version": "1.0.0",
    "description": "Complete system for building high converting landing pages: intake questions, page structure, layout selection, conversion copywriting, SEO, plus strict visu...",
    "category": "frontend",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "frontend",
      "design",
      "landing-page",
      "ui-ux"
    ]
  },
  {
    "name": "memory-nexus",
    "version": "1.0.0",
    "description": "Cross-session architectural memory ledger. Preserves technical decisions, conventions, and context across distinct agent sessions to eliminate repetitive que...",
    "category": "memory",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "memory",
      "state",
      "context",
      "cross-session",
      "architecture"
    ]
  },
  {
    "name": "ponytail",
    "version": "1.0.0",
    "description": "Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixi...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "yagni",
      "minimalist",
      "clean-code"
    ]
  },
  {
    "name": "ponytail-audit",
    "version": "1.0.0",
    "description": "Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. R...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "audit",
      "bloat",
      "yagni"
    ]
  },
  {
    "name": "ponytail-debt",
    "version": "1.0.0",
    "description": "List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for 'ponytail debt', 'what did ponytail d...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "tech-debt",
      "shortcuts",
      "cleanup"
    ]
  },
  {
    "name": "ponytail-review",
    "version": "1.0.0",
    "description": "Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. ...",
    "category": "workflow",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "workflow",
      "code-review",
      "yagni",
      "quality"
    ]
  },
  {
    "name": "prompt-optimizer",
    "version": "1.0.0",
    "description": "Systematically optimize, evaluate, and iterate LLM prompts. Use when designing system prompts, refining user instructions, generating few-shot exemplars, sco...",
    "category": "optimization",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "optimization",
      "prompt-engineering",
      "few-shot",
      "eval"
    ]
  },
  {
    "name": "review-frontend-production",
    "version": "1.0.0",
    "description": "\u5ba1\u67e5 Vibe Coding\u3001AI \u751f\u6210\u6216\u539f\u578b\u524d\u7aef\uff0c\u6309\u8bf7\u6c42\u6267\u884c\u5feb\u901f\u4f53\u68c0\u6216\u9010\u9875\u9010\u7ec4\u4ef6\u5b8c\u6574\u5ba1\u67e5\uff0c\u8f93\u51fa\u6709\u8bc1\u636e\u7684\u95ee\u9898\u3001\u4fee\u590d\u65b9\u6848\u4e0e\u9a8c\u6536\u6761\u4ef6\u3002\u9002\u7528\u4e8e\u524d\u7aef\u4f53\u68c0\u3001\u5168\u7ad9 review \u548c\u4e0a\u7ebf\u524d\u5de5\u7a0b\u4ea4\u63a5\uff1b\u660e\u786e\u8981\u6c42\u4fee\u590d\u65f6\u624d\u5b9e\u65bd\u3002",
    "category": "frontend",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "frontend",
      "review",
      "audit",
      "quality"
    ]
  },
  {
    "name": "scrapling-official",
    "version": "0.5.1",
    "description": "Scrape web pages using Scrapling with HTTP requests, stealth browsers, JavaScript rendering, browser actions, API response capture, concurrent spiders, and a...",
    "category": "scraping",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "scraping",
      "web",
      "anti-bot",
      "crawlers"
    ]
  },
  {
    "name": "testsprite-ci",
    "version": "1.0.0",
    "description": "Configure TestSprite continuous integration testing pipelines and automated test runs.",
    "category": "testing",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "testing",
      "ci",
      "automation",
      "pipeline"
    ]
  },
  {
    "name": "testsprite-verify",
    "version": "1.0.0",
    "description": "Run automated tests via the TestSprite CLI against deployed or local environments to catch regressions before shipping code.",
    "category": "testing",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "testing",
      "verification",
      "e2e",
      "qa"
    ]
  },
  {
    "name": "token-squeezer",
    "version": "1.0.0",
    "description": "AST-based token and context optimizer. Compresses heavy source code and logs by 50-70% before feeding them into LLM context windows without semantic loss.",
    "category": "optimization",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "Copilot",
      "MCP"
    ],
    "tags": [
      "optimization",
      "token-compression",
      "cost-reduction",
      "llm-context"
    ]
  },
  {
    "name": "using-superpowers",
    "version": "1.1.0",
    "description": "The master orchestration meta-skill for Agent Superpowers. Governs the 7-stage autonomous engineering lifecycle across Claude Code, Cursor, Codex, Antigravit...",
    "category": "orchestration",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "orchestration",
      "bootstrap",
      "lifecycle",
      "master-protocol"
    ]
  },
  {
    "name": "video-shotcraft",
    "version": "1.0.0",
    "description": "Create cinematic product videos from shot recipe cards, a validated template, and code/audio assets (Remotion + real page screenshots + 2.5D camera moves + b...",
    "category": "multimedia",
    "compatibility": [
      "Claude Code",
      "Cursor",
      "Codex",
      "Antigravity",
      "Windsurf",
      "Gemini CLI",
      "MCP"
    ],
    "tags": [
      "multimedia",
      "video",
      "remotion",
      "shotcraft"
    ]
  }
];

export function listSuperpowers(): AgentSkill[] {
  return SUPERPOWERS_CATALOG;
}

export function getSkill(name: string): AgentSkill | undefined {
  return SUPERPOWERS_CATALOG.find((s) => s.name === name);
}

export function getSkillsByCategory(category: SkillCategory): AgentSkill[] {
  return SUPERPOWERS_CATALOG.filter((s) => s.category === category);
}
