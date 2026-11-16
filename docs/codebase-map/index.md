---
created_at: "2026-11-16T14:29:54+05:30"
created_by: "Codex / documentation-layout session"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Codebase navigation

Owner: Senior Engineer. Status: observed scaffold only; no new feature scope or architecture is accepted. Read when locating code relevant to an owner-defined spec. Documentation indexes are required within docs/, not every Java/package/source directory. Root README and AGENTS route here; no root index is needed.

## Observed paths
| Path from repository root | Current contents / when to inspect |
| --- | --- |
| apps/backend/ | Existing Quarkus/Maven application scaffold; inspect for application wiring tasks. |
| modules/kitchen/ | Existing Java module scaffold; do not assume it owns a future feature until an accepted spec defines ownership. |
| pom.xml | Existing reactor/dependency configuration; inspect for build concerns. |
| scripts/check.py | Existing module/XML/local-link validation. |

## Feature lookup procedure
1. Read root instructions and architecture, then the relevant spec and milestone. Find any feature-to-code mapping here or in module docs; unassigned features remain unassigned.
2. List candidate paths with `rg --files <path>`; search endpoint names, symbols, config keys and domain terms with scoped `rg -n` queries. Do not read the entire repository by default.
3. Trace the entry point through relevant calls and state changes. Inspect callers, interfaces, persistence/migrations, contracts and related tests where they exist. Find missing coverage rather than assuming it exists.
4. Record expected edit paths, related read/review paths, acceptance/test scope and dependencies in the milestone/PR. Expand lookup for shared contracts/callers and record the reason; unrelated discoveries go into the proper findings ledger.
5. Verify actual source against documentation. Correct stale maps with the same change; maps aid navigation, source and accepted requirements establish current facts.

When features exist, add concise feature-to-entry-point/module/test/contract mappings under docs/codebase-map or docs/modules/<module>/, with links and ownership. Do not preassign features now. CLAUDE.md/AGENTS.md placement can support automatic directory scoping in some tools, but Kivi currently keeps guidance under docs/ per owner instruction: agents must load relevant scoped documents explicitly. An arbitrary index.md is not an automatically loaded instruction file.
