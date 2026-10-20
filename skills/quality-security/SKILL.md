---
name: quality-security
description: Use for automated testing, regression analysis, secure code review and CI quality gates.
---

# quality-security

## Activation
Use for test strategy, QA, security reviews, CI failures, dependency risks or regression checks.
## Workflow
1. Define the change boundary, threat model and highest-risk user flows.
2. Select focused unit, integration and end-to-end tests based on actual code paths.
3. Check authorization boundaries, input validation, secrets handling, dependency trust and error exposure.
4. Run available tests and static analysis with reproducible commands; distinguish findings from hypotheses.
5. Report severity, affected code, reproduction, remediation and residual risk.
## Guardrails
Use synthetic test data. Never exfiltrate credentials or perform destructive tests against real services. Do not mark unexecuted tests as passing.
## Deliverable
Provide concise test matrix, findings with evidence and outstanding coverage gaps.
