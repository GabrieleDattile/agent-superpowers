# Agent & IDE Compatibility Guide

`agent-superpowers` is engineered to be platform-agnostic. The skills can be loaded into any modern agentic IDE or autonomous CLI.

---

## 1. Claude Code
Claude Code natively supports agent skills via markdown definitions:
1. Copy the skill folder into your project's `.claude/skills/` or reference it in your workspace.
2. Claude Code automatically detects the `SKILL.md` frontmatter and loads the skill whenever your prompt matches the trigger phrase.

---

## 2. Cursor
To use with Cursor:
1. Copy the contents of the target `SKILL.md` into your `.cursorrules` or create a `.cursor/rules/` file (e.g. `.cursor/rules/ghost-runner.mdc`).
2. Cursor will activate the rules when working in Composer or Chat mode.

---

## 3. Windsurf (Cascade)
1. Add the skill rules to `.windsurfrules`.
2. Cascade will respect the negative constraints and step-by-step phases defined in the skill protocol.

---

## 4. Model Context Protocol (MCP)
All skills that expose a Python script in `scripts/` can be wrapped into a standard MCP server tool:
```json
{
  "mcpServers": {
    "agent-superpowers": {
      "command": "python",
      "args": ["cli/superpowers.py", "serve-mcp"]
    }
  }
}
```

---

## 5. Gemini CLI / OpenAI Assistants / LangGraph
Use the provided `cli/superpowers.py` or read the JSON/Pydantic schemas in each skill's `scripts/` folder to expose them as native Function Calling / Tools.
