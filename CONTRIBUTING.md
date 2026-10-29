# Contributing to Agent Superpowers

Thank you for your interest in contributing to **Agent Superpowers**! We welcome new skills, bug fixes, and documentation improvements from the community.

---

## How to Add a New Skill

1. **Fork the Repository** and create your branch:
   ```bash
   git checkout -b skill/my-new-skill
   ```

2. **Create the Skill Directory**:
   Place your skill in the appropriate category under `skills/`:
   ```text
   skills/<category>/<skill-name>/
   ├── SKILL.md
   ├── scripts/
   └── examples/
   ```

3. **Follow the Standard Format**:
   - Every skill must have a valid `SKILL.md` following the [Skill Specification](SPECIFICATION.md).
   - Must include:
     - Clear YAML frontmatter (`name`, `description`, `compatibility`, `tags`).
     - Explicit trigger and non-trigger conditions.
     - Concrete negative constraints (what the agent must NOT do).
     - At least one working example or reproduction script.

4. **Verify Locally**:
   Run the test runner to validate formatting and frontmatter:
   ```bash
   python cli/superpowers.py validate
   ```

5. **Submit a Pull Request**:
   - Provide a clear summary of what problem the skill solves.
   - Attach a terminal output or screenshot demonstrating the skill in action.

---

## Community Guidelines
- Avoid generic prompt wrappers (e.g. "write an email"). We only accept **actionable, deterministic, high-impact agent skills**.
- Keep dependencies minimal. Prefer standard library when possible.
