---
name: playwright-interactive-browser
description: Use for persistent interactive browser debugging with Playwright.
---

# playwright-interactive-browser

## Activation
Activate only when the user task matches the description. Do not load for unrelated work.

## Workflow
Check interactive browser availability; reuse sessions if supported; inspect console/network/UI; fall back to regular Playwright if unavailable.

## Guardrails
Do not expose secrets, assume tools are installed, or claim tests were executed without evidence. Use synthetic data and preserve existing functionality.

## Deliverable
List changes, actual verification, outstanding risks and next steps.
