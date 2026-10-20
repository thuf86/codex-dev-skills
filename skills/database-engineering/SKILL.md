---
name: database-engineering
description: Use for SQL schema design, migrations, indexes, transactions and query performance.
---

# database-engineering

## Activation
Use when a task changes SQL schemas, queries, migrations, indexes, transactions or data integrity.
## Workflow
1. Identify engine/version, current schema, affected tables, constraints and application queries.
2. Inspect migration history and create a reversible or safely forward-only migration plan.
3. Preserve data; use transactions and backups appropriate to the engine and change.
4. Verify constraints, index selectivity, locking, pagination and query plans where feasible.
5. Test migrations on disposable data, including failure and rollback paths.
## Guardrails
Do not run destructive SQL against production without explicit approval and a recovery plan. Never infer missing values as zero.
## Deliverable
Provide migration files, affected queries, compatibility notes, verification and rollback guidance.
