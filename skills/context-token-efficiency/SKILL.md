---
name: context-token-efficiency
description: Use for reducing Codex context usage, scoped code searches, concise checkpoints and targeted tests.
---

# context-token-efficiency

## Activation
Use for large repositories, long sessions, expensive context, repeated searches or explicit token-efficiency requests. May be combined with one domain skill.
## Workflow
1. Restate task in one sentence and identify likely files before reading.
2. Search filenames and symbols first (rg --files, rg -n), then read only relevant ranges.
3. Avoid dumping whole repositories, generated files, minified assets, dependency trees or large logs.
4. Prefer minimal diffs and targeted tests; expand scope only when evidence requires it.
5. Maintain a short checkpoint: objective, decisions, changed files, tests, blockers, next step.
6. Respond with outcomes and concise evidence; do not repeat full tool output.
## Guardrails
Never trade correctness or required security checks for token savings. Do not hide failed tests or omit necessary context.
## Deliverable
Report a compact change summary and any material uncertainty.
