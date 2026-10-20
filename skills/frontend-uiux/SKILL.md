---
name: frontend-uiux
description: Use for web frontend, UI/UX, accessibility, responsive layouts and design systems.
---

# frontend-uiux

## Activation
Use when the request concerns browser UI, React, Next.js, CSS, visual layout, components or accessibility. Do not activate for backend-only changes.
## Workflow
1. Inspect the relevant page, components, styling and existing design tokens before changing code.
2. Identify the exact UX defect and define visual and functional acceptance criteria.
3. Reuse components and tokens; preserve routing, API calls, state, keyboard behavior and semantics.
4. Implement responsive mobile/tablet/desktop states, focus visibility, contrast and loading/error/empty states.
5. Run targeted lint/typecheck/tests and available browser checks; report what was not verified.
## Guardrails
Do not replace entire screens without a concrete reason. Avoid unnecessary dependencies. Never claim screenshot or visual validation unless actually performed.
## Deliverable
Summarize files changed, before/after behavior, checks performed and remaining risks.
