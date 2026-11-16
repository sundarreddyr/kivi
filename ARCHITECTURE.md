---
created_at: "2026-11-14T11:56:05+05:30"
created_by: "Codex"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Kivi architecture

Status: awaiting the first owner-defined spec. No new product architecture or design choices are accepted by this documentation setup.

## Observed repository state
The existing Maven reactor contains apps/backend and modules/kitchen. The root pom currently declares Java release 21 and a Quarkus dependency. These are facts about the existing scaffold, not approval of future module boundaries, deployment topology, versions, schemas, or APIs. Reconcile the scaffold and the owner's Java 25 preference during the first applicable spec.

## Future maintenance
After the first spec, summarize accepted system boundaries, data flow, invariants, and dependency directions here. Link detailed cross-module designs under docs/design-docs and module-specific designs under docs/modules/<module>/. Keep current architecture concise; capture rationale in numbered ADRs.

Earlier proposals are in [the archive](docs/archive/index.md) and have no current implementation authority.
