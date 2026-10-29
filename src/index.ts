/**
 * Agent Superpowers: Universal TypeScript SDK
 * Author: Gabriele Dattile (https://github.com/GabrieleDattile)
 */

export interface AgentSkill {
  name: string;
  version: string;
  description: string;
  category: "orchestration" | "workflow" | "frontend" | "memory" | "debugging" | "security" | "optimization" | "reverse-engineering" | "architecture";
  compatibility: string[];
  tags: string[];
}

export const SUPERPOWERS_CATALOG: AgentSkill[] = [
  {
    name: "using-superpowers",
    version: "1.1.0",
    description: "Master orchestration meta-skill enforcing the 7-stage engineering lifecycle.",
    category: "orchestration",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["orchestration", "lifecycle", "bootstrap"]
  },
  {
    name: "feature-brainstormer",
    version: "1.1.0",
    description: "Socratic requirements refiner that asks up to 3 clarifying questions before code generation.",
    category: "workflow",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["workflow", "planning", "brainstorming"]
  },
  {
    name: "git-worktree-sandbox",
    version: "1.1.0",
    description: "Ephemeral git worktree isolation ensuring zero risk to the primary working branch.",
    category: "workflow",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["git", "worktree", "sandbox", "isolation"]
  },
  {
    name: "memory-nexus",
    version: "1.0.0",
    description: "Cross-session architecture ledger eliminating agent amnesia across restarts.",
    category: "memory",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["memory", "state", "context"]
  },
  {
    name: "frontend-sentinel",
    version: "1.0.0",
    description: "Production UI/UX auditor scanning components for accessibility and mobile responsive breaks.",
    category: "frontend",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["frontend", "ui-ux", "accessibility", "react"]
  },
  {
    name: "ghost-runner",
    version: "1.0.0",
    description: "Zero-assumption bug reproducer enforcing strict RED -> GREEN TDD cycle.",
    category: "debugging",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["debugging", "tdd", "reproducibility"]
  },
  {
    name: "adversarial-duelist",
    version: "1.0.0",
    description: "Pre-commit red-team fuzzer bombarding functions with boundary and exploit payloads.",
    category: "security",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["security", "fuzzing", "red-team"]
  },
  {
    name: "token-squeezer",
    version: "1.0.0",
    description: "AST-based context compressor reducing token costs by 50-70% for large prompts.",
    category: "optimization",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["optimization", "tokens", "compression"]
  },
  {
    name: "api-synthesizer",
    version: "1.0.0",
    description: "Network-to-SDK generator converting cURL and HAR traffic into typed clients.",
    category: "reverse-engineering",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["reverse-engineering", "api", "sdk"]
  },
  {
    name: "arch-archaeologist",
    version: "1.0.0",
    description: "Codebase cartographer tracing dependency call graphs and detecting dead zombie code.",
    category: "architecture",
    compatibility: ["Claude Code", "Cursor", "Codex", "Antigravity", "Windsurf", "MCP"],
    tags: ["architecture", "dependencies", "dead-code"]
  }
];

export function listSuperpowers(): AgentSkill[] {
  return SUPERPOWERS_CATALOG;
}
