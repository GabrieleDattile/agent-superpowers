---
name: api-synthesizer
version: 1.0.0
description: Autonomous API reverse-engineering engine. Converts raw network traffic (cURL commands or HAR files) into fully typed Python/TypeScript client SDKs.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Windsurf, Gemini CLI, Copilot, MCP]
tags: [reverse-engineering, api, sdk-generation, networking]
---

# 🔌 Skill: API Synthesizer (Network to SDK)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user provides a `curl` command, network log, or request payload from Chrome/Firefox DevTools.
  - The user says: "create an SDK for this API", "turn this curl into a typed client", or "reverse engineer this endpoint".
- **DO NOT TRIGGER WHEN**:
  - An official, maintained SDK already exists and is easily installable via pip/npm.

---

## 2. Fundamental Philosophy
> *"Developers waste hours copying endpoints, headers, and crafting request boilerplate. API Synthesizer automatically parses network traces and emits robust, typed, ready-to-run client libraries in seconds."*

---

## 3. Operational Protocol

### Phase 1: Ingest & Parse
1. Take the user's raw cURL string or network dump.
2. Run the Synthesizer CLI:
   ```bash
   python skills/reverse-engineering/api-synthesizer/scripts/synthesizer.py --curl "<curl_string>" --name "OrderClient"
   ```

### Phase 2: Structural Analysis
The synthesizer:
1. Extracts HTTP Method (`GET`, `POST`, `PUT`, etc.) and URL path.
2. Identifies Authentication headers (`Authorization: Bearer ...`, cookies, API keys) and abstracts them into configurable constructor parameters.
3. Analyzes JSON payload structures and automatically defines **Pydantic / TypedDict** schemas for request bodies.

### Phase 3: Code Generation & Test
1. Emits the generated Python client class with async or sync `requests`/`httpx` methods.
2. Emits a mock execution script to verify successful instantiation.

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** hardcode sensitive API keys or bearer tokens in the generated SDK. Always extract them as environment variables or constructor arguments.
- ❌ **NEVER** produce untyped `**kwargs` when payload fields can be statically inferred.
