---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:25:21+05:30"
updated_by: "Codex / pointer-instructions session"
---

# Milestone plan template

ID: PLAN-<number>. Spec: <link/acceptance IDs>. Status: draft / active / blocked / completed.
Started by: <actual actor + role>. Started at: <IST>. Owner: <identity>.

## Goal, scope, non-goals and dependencies
<One spec milestone; list prerequisite plans and independently workable PRs.>

## Acceptance, tests and recovery
- [ ] AC mapping and independently observable results specified. Evidence: <pending>.
- [ ] Red/green evidence and QA cases planned. Evidence: <pending>.
- [ ] Rollback/recovery steps and observable recovery check specified, or N/A justified.
- [ ] Migration backward compatibility, data preservation and forward repair addressed, or N/A justified.

## Recovery procedure and migration safety
Trigger/stop condition: <observable failure>. Recovery actor: <identity/role>.
Procedure/prerequisites: <concrete rollback or forward-repair steps, irreversible effects and authorization>.
Recovery verification: <command/scenario, expected observation, data-preservation evidence>.
Migration safety: <old/new compatibility, rollout order, backup/restore requirements, partial failure and forward repair; or justified N/A>.
Procedure status: <planned / rehearsed with evidence; never equate documentation with tested recovery>.

## Evidence identity
<Record base SHA, candidate scope and reproducible content/status digest including new files, then actual tested commit SHA and relevant environment. Refresh affected evidence after edits. See [revision-bound evidence](../agent-workflows/0011-revision-bound-evidence.md) and adjust relative links when copying into an active milestone directory.>

## PR units
| PR record | Goal | Base/dependencies | Expected paths/count | Acceptance | Status |
| --- | --- | --- | --- | --- | --- |
| <link> | <goal> | <base> | <paths; <=20> | <IDs> | <pending> |

## Completion
- [ ] Every PR checklist and exact-candidate evidence linked.
- [ ] Unrelated findings recorded; blockers resolved.
- [ ] Docs/metadata current; QA and Advisor outcomes recorded.
- [ ] Commit/push actors and IST times in PR records.
- [ ] Work-log and at-most-five-line handover updated.

Work log: <work-log.md>. Decisions: <links>. Failed approaches: <links>.
