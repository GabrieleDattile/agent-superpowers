---
name: prompt-optimizer
description: Systematically optimize, evaluate, and iterate LLM prompts. Use when
  designing system prompts, refining user instructions, generating few-shot exemplars,
  scoring against evaluation rubrics, or reducing ambiguity and prompt tokens.
version: 1.0.0
author: linshenkx (https://github.com/linshenkx/prompt-optimizer)
compatibility:
- Claude Code
- Cursor
- Codex
- Antigravity
- Windsurf
- Gemini CLI
- MCP
tags:
- optimization
- prompt-engineering
- few-shot
- eval
---

# Prompt Optimizer

A structured framework and toolset for engineering, optimizing, and evaluating LLM system and user prompts to achieve higher determinism, fewer hallucinations, and lower token usage.

## Core Capabilities

1. **User Prompt Optimization (`optimize-user-prompt`)**:
   - Converts ambiguous user requests into clear, structured, contextual instructions.
   - Decomposes complex multi-part tasks into step-by-step reasoning sequences.
   - Specifies explicit negative constraints (what NOT to do) to eliminate hallucinations.

2. **System Prompt Engineering (`optimize-system-prompt`)**:
   - Defines strict persona, role, tone, and operational boundaries.
   - Embeds few-shot input/output examples with realistic edge cases.
   - Enforces deterministic output formats (JSON schemas, Markdown structures).
   - Optimizes instruction density to prevent model attention degradation.

3. **Iterative Prompt Refinement (`iterate-prompt`)**:
   - Tests candidate prompts against edge-case inputs.
   - Evaluates outputs against rubric criteria: correctness, conciseness, instruction following, and safety.
   - Performs ablation: trims redundant verbiage while preserving functional semantics.

## Systematic Prompt Optimization Workflow

```text
[Input Prompt] ──> [Task Clarification] ──> [Format & Constraint Enforcement]
      │                                                │
      ▼                                                ▼
[Final Prompt] <── [Token Trimming] <── [Few-Shot Exemplar Synthesis]
```

### Step 1: Clarify Intent & Objectives
- Identify primary goal, target audience/model, and expected input variables.
- Eliminate vague adjectives ("good", "detailed") in favor of specific criteria ("includes time complexity, 3 test cases").

### Step 2: Establish Constraints & Guardrails
- **Positive Instructions**: Define exactly what steps the model must execute.
- **Negative Constraints**: Explicitly prohibit common model tendencies (e.g., "Do not apologize", "Do not include placeholder comments").
- **Error Handling**: Instruct the model on how to handle missing data or ambiguous queries.

### Step 3: Few-Shot Exemplar Engineering
- Include 2-3 high-quality input/output pairs demonstrating desired output formatting and reasoning depth.
- Ensure at least one example covers a non-standard or edge-case input.

### Step 4: Token Optimization
- Compress repetitive phrasing without changing instruction meaning.
- Use bullet points and hierarchical markdown headers for high attention retention.
