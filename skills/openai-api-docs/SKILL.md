---
name: openai-api-docs
description: Use for current OpenAI API and SDK implementation guidance.
---

# openai-api-docs

## Activation
Activate only when the user task matches the description. Do not load for unrelated work.

## Workflow
Check SDK version and official documentation; verify endpoint contracts; use mocks unless live API testing is authorized.

## Guardrails
Do not expose secrets, assume tools are installed, or claim tests were executed without evidence. Use synthetic data and preserve existing functionality.

## Deliverable
List changes, actual verification, outstanding risks and next steps.
