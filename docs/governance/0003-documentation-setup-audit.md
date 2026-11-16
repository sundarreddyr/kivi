---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:30:40+05:30"
updated_by: "Codex / documentation-layout session"
---

# Documentation setup audit

Status: prepared, uncommitted. Scope: owner-authorized independent documentation only; no new product spec, milestone plan, API, schema or architecture decision. Actor: Codex / primary implementation session. Started at: 2026-11-16T12:49:36+05:30.

## Session decisions
- Root specs/ is the sole active specification directory; only its index exists until owner defines a spec.
- Earlier drafts moved intact in substance into docs/archive with inactive banners; existing source/build scaffold is preserved.
- Root security/ is local-only and ignored, including indexes, ledgers and evidence. Its contents must not be published or copied to public audit records.
- Metadata uses Markdown front matter and a fallback registry for syntax-sensitive/existing non-Markdown files; no runtime-source edits required.
- No commit/push or CI setup performed. Two-attempt escalation and independent pre-commit review apply.

## Proposed reviewable commit/PR batches
This existing repository is not eligible for the initial-commit exemption. Before any commit, assign exact path lists, count the diff against each proposed base, and obtain independent Advisor review. Keep batches at most 20; include metadata/index follow-ups in each budget. Proposed order: (1) archived drafts and archive indexes; (2) root entry points/spec navigation and findings indexes; (3) ten workflow documents and workflow index; (4) seven templates and template index; (5) governance and remaining navigation. Redistribute boundaries if actual counts exceed 20; every intermediate batch must pass link checks. These are documentation packaging notes, not product execution plans.

## Verification
Baseline HEAD: `1570156fcfe79a5e22ebdead30e3aad009be081b`. Results apply to the uncommitted working tree, not a committed SHA.

- Existing `python3 scripts/check.py`: PASS (Maven XML/module paths and documentation links).
- Independent QA agent `qa_verification`: PASS. Additional read-only validation covered 75 public maintained files, 66 Markdown files; all local links, four-field metadata/registry coverage, and maintained directory indexes passed.
- Active root specs/ and docs/exec-plans/active/: indexes only, no specs/plans added.
- Tracked runtime/source/POM/check.py changes: none.
- `git check-ignore -v security/index.md`: PASS; `/security/` applies. `git ls-files -- security`: empty. Local security contents were excluded from QA/Advisor review.
- Runtime suites and CI: not run/introduced; no runtime behavior changes. Future behavior work still requires the documented testing gates.
- Advisor `advisor_review` initial review identified incorrect creation attribution for four archived records. Corrected using first Git author/time from original paths; original paths retained in archive banners. Final review pending.
- Documentation maintenance remains manual. Readiness review is pending before any commit; automation deferred per owner.

## Commit audit
Not committed or pushed. Independent Advisor final review pending after provenance fix. Pre-commit readiness checklist remains pending.

## Latest handover
1. Documentation setup only; worktree uncommitted; no active spec.
2. Policies and templates prepared; verification results follow below.
3. Decisions are in this audit; old drafts are inactive under docs/archive/.
4. Commit requires reviewed <=20-file batches and readiness gate completion.
5. Owner supplies first spec; no product architecture/implementation work yet.

## Follow-up session: explicit pointer instructions — 2026-11-16T14:25:21+05:30

Owner authorized adding revision-bound evidence and recovery/outcome instructions. Scope: two workflow documents, root links, workflow index and three template updates; no active spec, product plan, runtime code or architecture decision added. Actor: Codex / pointer-instructions session.

Decisions: pre-commit identity must include new files and deletion/rename status; tests bind to the actual tested state, and changes require affected revalidation. Specs define observable success/failure and invariants; milestone plans include recovery triggers, actors, steps, verification and migration safety or justified N/A. Keep full-suite post-commit policy and pending commit gates unchanged.

Validation: `python3 scripts/check.py` passed (Maven module/XML and Markdown links); `git diff --check` passed. Runtime tests are not applicable to these documentation-only edits. Independent Advisor review of this follow-up remains pending. No commit/push performed. Final review outcome will be reported to the owner without recursively editing the reviewed candidate.

## Layout revision — 2026-11-16T14:29:54+05:30

Owner supersedes the earlier root specs/security and per-source-directory index layout. All documentation now lives under docs/ except root AGENTS.md, ARCHITECTURE.md, CLAUDE.md and README.md. specs moved to docs/specs/, private security directory moved wholesale to ignored docs/security/, root index removed, and earlier boilerplate source indexes removed. Source/build/tool files are preserved. Earlier entries above describe the previous layout, not current instructions.

Codebase lookup now uses docs/codebase-map/index.md with scoped symbol/path searches and caller/test tracing; no feature ownership or product design is assigned. Structural verification passed: existing scripts/check.py, git diff --check, public Markdown locations/metadata/docs-directory indexes, empty docs/specs, and docs/security ignore/untracked checks. Independent Advisor review pending; no commit/push performed. All future commits remain subject to file-budget/readiness gates.
