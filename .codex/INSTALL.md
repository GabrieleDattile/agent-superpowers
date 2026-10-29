# Installing Agent Superpowers in Codex

Agent Superpowers can be loaded directly into OpenAI Codex environments.

### Automated Setup
Run the universal installer:
```bash
python install.py --target codex
```

### Manual Configuration
Add the skills directory to your `.codex/config.json`:
```json
{
  "skills": [
    "./skills/orchestration/using-superpowers",
    "./skills/debugging/ghost-runner",
    "./skills/security/adversarial-duelist",
    "./skills/optimization/token-squeezer",
    "./skills/workflow/git-worktree-sandbox",
    "./skills/workflow/feature-brainstormer",
    "./skills/reverse-engineering/api-synthesizer",
    "./skills/architecture/arch-archaeologist"
  ]
}
```
Codex will index the YAML frontmatter in each `SKILL.md` file and route queries automatically.
