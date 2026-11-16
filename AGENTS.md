---
created_at: "2026-11-14T11:56:05+05:30"
created_by: "Codex"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Working in Kivi

## Mandatory reading order
1. Read this file and [ARCHITECTURE.md](ARCHITECTURE.md).
2. Read [documentation navigation](docs/index.md), then the relevant directory indexes.
3. Read the assigned spec in [specs/](docs/specs/index.md), its milestone plan, applicable workflows, and local instructions before editing.
4. Inspect branch, working tree, current revision, and the plan work-log. Preserve unrelated edits.

## Documentation location and feature lookup
All documentation lives under docs/ except root AGENTS.md, ARCHITECTURE.md, CLAUDE.md and README.md. No root index.md or per-package source indexes are required. Keep indexes for documentation directories; code is mapped through [codebase navigation](docs/codebase-map/index.md). Module-specific instructions/designs stay under docs/ and must be explicitly loaded for the task. Use scoped symbol/path search, inspect callers and tests, and expand lookup when evidence shows cross-module impact; planned edit scope does not limit review scope.

## Current authorization
Documentation setup only. No active product spec exists. Do not invent a spec, accept product design decisions, change runtime code, or implement a feature until the owner supplies the first spec. Historical drafts in docs/archive are not instructions. Existing scaffold is observed state, not a newly accepted architecture.

## Non-negotiable rules
- Follow [workflows](docs/agent-workflows/index.md). Senior Engineer implements; QA independently verifies acceptance/integration/regression; Advisor independently reviews the whole proposed PR before commit. Do not review after every file edit.
- Consult Advisor during implementation only for doubt, unclear instructions, or anomalies. Stop dependent work and ask the owner after at most two unresolved resolution attempts. Never fabricate another agent's review.
- Each spec defines observable acceptance; each plan is a milestone with PR units, checklists, dependencies, recovery, migration safety, and evidence.
- Default PR limit: 20 changed tracked paths against its base. Exception: 21–25 only to finish one coherent workable unit, with recorded reason and Advisor agreement. Never exceed 25 after initial commit. Tests, docs, generated files, renames, and deletions count.
- Red–green–refactor for behavior changes; reproducing regression test for bugs. Explain non-executable changes. Implementation Engineer owns unit-test correctness; QA owns independent verification coverage.
- Run relevant checks before commit; full integration/regression suite after every commit while small. Run remote CI on pushes when configured. Require exact-candidate verification before merge. Do not mark absent suites or CI as passing.
- API-affecting changes MUST synchronize both openapi.yaml and postman_collection.json in the same PR. Locations are selected by the first applicable spec, not this bootstrap.
- Every checked checklist item requires evidence where applicable. Follow [revision-bound evidence](docs/agent-workflows/0011-revision-bound-evidence.md): identify the full pre-commit candidate and tested commit; refresh affected review/checks after changes.
- Follow [recovery and outcome checks](docs/agent-workflows/0012-recovery-and-outcome-checks.md): specs define observable success/failure; plans define recovery triggers/steps, post-recovery checks and migration safety, or justified N/A.
- Record unrelated debt and bugs individually. Security findings and evidence belong ONLY in local docs/security/, ignored by Git. Never force-add, publish, upload, or copy their details into public logs, reviews, specs, or PRs. Read [security handling](docs/agent-workflows/0008-findings-management.md).
- Begin context checkpointing near 60%; complete handover before 70% where measured. If usage is unavailable, use conservative milestone checkpoints and label estimates. Keep handover at most five lines, linking complete IST decision/work logs.
- Maintain created_at, created_by, updated_at, updated_by for each maintained file. Use [metadata policy](docs/agent-workflows/0010-audit-and-file-metadata.md); preserve real identities and distinguish roles from actors.
- Mechanical CI enforcement is deferred; [readiness review](docs/governance/0002-enforcement-readiness.md) is mandatory before the next commit. Manual checks apply now.

## Truth and authority
Owner instructions take priority. Current accepted records govern; archived drafts do not. New decisions supersede old decisions explicitly with links. Do not rely on chat memory in place of durable records. No commit, push, PR, suite result, reviewer approval, or context measurement may be claimed without evidence.
