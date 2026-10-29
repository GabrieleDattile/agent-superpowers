---
name: frontend-sentinel
version: 1.0.0
description: Production frontend & UI/UX auditor. Scans React, Vue, Svelte, and HTML templates for accessibility defects, mobile viewport breaks, unhandled loading states, and hydration traps.
author: Gabriele Dattile (https://github.com/GabrieleDattile)
compatibility: [Claude Code, Cursor, Codex, Antigravity, Windsurf, Gemini CLI, MCP]
tags: [frontend, react, vue, ui-ux, accessibility, mobile-responsive, audit]
---

# 🎨 Skill: Frontend Sentinel (Production UI/UX Auditor)

## 1. When to Trigger (Routing)
- **TRIGGER WHEN**:
  - The user requests a review of frontend code, UI components, or web templates (`.tsx`, `.jsx`, `.vue`, `.html`, `.css`).
  - The user asks: "is this UI production ready?", "check accessibility (a11y)", "find mobile responsive issues", or "audit my frontend components".
- **DO NOT TRIGGER WHEN**:
  - The task is purely backend database or infrastructure related with zero user interface components.

---

## 2. Fundamental Philosophy
> *"AI assistants often produce components that look visually acceptable in isolation, but fail miserably in production: images without alt text, inputs without labels, broken mobile viewports, and missing keyboard navigation. Frontend Sentinel acts as a clinical UI/UX inspector before deployment."*

---

## 3. Operational Protocol

### Phase 1: Automated Static Inspection
Run the Frontend Sentinel engine on target files or directories:
```bash
python skills/frontend/frontend-sentinel/scripts/auditor.py --path <src_or_component_path> --html-report ui-audit.html
```

The engine systematically checks for 6 critical production flaws:
1. **Accessibility (a11y)**: Images without `alt`, icon buttons without `aria-label`, inputs without `<label>`.
2. **Mobile Viewport & Overflow**: Fixed pixel widths (e.g. `width: 800px` or `w-[900px]`) that trigger horizontal scrolling on mobile.
3. **Form & Input Resilience**: `<input>` elements without required types, missing autofocus traps, forms missing `onSubmit` handlers.
4. **Hydration & SSR Traps**: Premature references to `window`, `document`, or `localStorage` during initial component render.
5. **Interactive Element Semantics**: Clickable `<div>` or `<span>` elements used instead of `<button>` or `<a>`.
6. **Error & Loading States**: Network fetch calls lacking loading spinners or fallback error boundaries.

### Phase 2: Interactive HTML Report
The engine outputs a standalone, graphical **`ui-audit.html`** file:
- Health score (0 - 100%)
- Ranked findings (Critical, Warning, Optimization)
- Exact file paths and line numbers with ready-to-copy code fixes.

### Phase 3: Remediation & Verification
1. Review generated findings.
2. Apply surgical component refactors.
3. Re-run `auditor.py` until the health score reaches **100% PASS**.

---

## 4. Guardrails & Negative Constraints
- ❌ **NEVER** approve a component with interactive `<div>` tags lacking keyboard accessibility (`onKeyDown` + `role="button"`).
- ❌ **NEVER** ignore mobile layout breaks triggered by rigid pixel containers.
