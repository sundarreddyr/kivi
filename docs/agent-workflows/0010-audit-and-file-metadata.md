---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# File metadata and execution audit

Every maintained repository file must have created_at, created_by, updated_at and updated_by, using ISO-8601 IST (+05:30). Markdown uses front matter; new source files may use valid comments when supported. Preserve syntax-sensitive formats with a sidecar entry in docs/governance/0001-file-metadata.yaml. That registry is authoritative fallback for existing source/config/generated/binary files; no unnecessary runtime edits just to add comments. Local security file metadata stays only inside docs/security/.

Use actual actor/session identity separately from role. Do not attribute an agent edit to the owner. Existing file provenance bootstrapped from Git commit author/time must be labeled as Git attribution, not asserted to identify the actual past tool/operator. Unknown provenance stays unknown. Preserve creation fields on edits/renames; update edit fields only for files actually changed. Imported legacy numbering remains historical.

The metadata registry stores its own four attributes at top level, avoiding recursive self-entry. Existing front matter is authoritative for Markdown; do not duplicate those entries. No handwritten source-file changelog is required beyond the four fields.

Plan audit records who started it and when, who implemented/reviewed/tested each proposed PR, commit author and actual committer, SHA, IST commit/push times, CI/check results and linked session decisions. Unperformed actions remain pending. Use real runtime IDs if exposed; otherwise a stable locally declared session label and say it is local. Do not invent provider agent IDs, percentages, approvals or commit evidence.

For a pre-commit review identify base SHA and deterministic diff/content digest because the commit does not exist yet. After commit bind tests to its SHA. Later changes require renewed relevant verification. Store machine command/result evidence concisely and keep sensitive outputs local.
