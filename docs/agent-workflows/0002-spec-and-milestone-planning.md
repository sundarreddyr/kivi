---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Specifications and milestone planning

Owner: Senior Engineer; Advisor reviews uncertainty. Product specs live exclusively in docs/specs/. Do not create one until the owner decides the first spec. Templates define structure, not product choices.

Use SPEC-0001, PLAN-0001, ADR-0001, BUG-0001, DEBT-0001; module-local IDs must include the module prefix. Allocate the next unused four-digit number in that category; check concurrent work first. IDs never change or get reused. Filename: 0001-descriptive-kebab-case.md. Fixed entry names and indexes are exempt. Preserve legacy archive names.

A spec states problem, scope/non-goals, examples, observable acceptance IDs, constraints, open questions, verification, and linked milestones. A plan is one milestone implementing part of a spec, not a duplicate spec. Every milestone defines independently workable PR units where possible, dependency order where necessary, expected paths/file budget, acceptance mapping, test strategy, rollback/recovery, migration safety, risks, and completion evidence.

Plan directory: docs/exec-plans/active/0001-milestone-name/ with plan.md, work-log.md, index.md, and numbered PR records. Completed plan directories move intact into completed/; update links. Per-PR records identify base, scope, authors, reviewers, commit/push timing and verification. Checklist progress must link evidence; not-applicable items explain why. No split may leave main broken or defer tests needed for current behavior.

- [ ] Spec acceptance criteria defined before behavior work.
- [ ] Milestone/PR acceptance mapped and dependencies explicit.
- [ ] File budgets include docs/tests/audit records.
- [ ] Recovery/migration strategy or justified N/A recorded.
- [ ] Open uncertainties resolved or escalated before dependent edits.
