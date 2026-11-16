---
created_at: "2026-11-16T14:25:21+05:30"
created_by: "Codex / pointer-instructions session"
updated_at: "2026-11-16T14:25:21+05:30"
updated_by: "Codex / pointer-instructions session"
---

# Recovery and outcome checks

Owner: Senior Engineer plans recovery; QA independently verifies observable outcomes; Advisor reviews failure and migration implications.

## Specification requirements
Every spec defines observable success and failure through acceptance IDs: starting state, action, expected result, and independent verification. State invariants that must survive failure. Describe recovery expectations and data preservation requirements without choosing an unapproved architecture. A checklist or successful compilation alone is not product acceptance.

## Milestone plan requirements
Each plan implements a spec milestone. Before implementation, specify:
- Acceptance IDs, commands/scenarios, expected observations, and evidence locations.
- What failures trigger stopping or recovery, who performs it, and the scope affected.
- Concrete rollback or forward-repair steps, prerequisites and any irreversible actions; never assume reverting code also reverses data or external actions.
- How to verify recovery restored the required behavior and preserved the required data.
- For migrations: old/new version compatibility, rollout order, backup/restore prerequisites where needed, partial-failure handling, and recovery when rollback is unsafe. Backups alone are not evidence of successful restore.

Choose a strategy proportional to the change. Documentation-only work may use restoring prior file content plus link/metadata checks. If recovery or migration safety is not applicable, record a specific reason; do not silently omit the sections. Do not execute destructive recovery drills or production actions without appropriate authorization.

## PR and QA gate
QA covers relevant failure/recovery cases with independent expected outcomes. Advisor checks acceptance mapping, irreversible effects and recovery feasibility before commit. Link rehearsed recovery evidence where applicable; clearly distinguish a written procedure from a procedure actually tested. An unresolved unsafe migration or unverified mandatory recovery criterion blocks progression and follows the two-attempt escalation rule.

- [ ] Observable success/failure and invariants defined.
- [ ] Recovery trigger, actor, procedure and post-recovery checks defined.
- [ ] Migration compatibility/data-preservation/partial-failure plan or justified N/A recorded.
- [ ] Required acceptance and recovery evidence linked, with candidate identity.
