---
name: backend-apis
description: Use for server architecture, REST APIs, authentication, integrations and observability.
---

# backend-apis

## Activation
Use for backend services, HTTP APIs, workers, authentication, authorization, queues, integrations and performance.
## Workflow
1. Trace the affected request flow, contracts, configuration and persistence.
2. Identify validation, error handling, idempotency, retry and timeout requirements.
3. Make small backward-compatible changes; version breaking contracts explicitly.
4. Add focused tests for success, invalid input, authorization failures and provider errors.
5. Run targeted tests, type checks and safe local checks; document untested external dependencies.
## Guardrails
Do not log secrets or sensitive payloads. Keep secrets in environment or approved secret managers. Never silently change production endpoints.
## Deliverable
Describe endpoint/contract impact, migration requirements, test evidence and operational risks.
