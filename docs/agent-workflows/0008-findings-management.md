---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Findings management and local security

Owner: discovering engineer; QA/Advisor help triage. Write unrelated debt to docs/findings/tech-debt/0001-name.md and bugs to docs/findings/bugs/0001-name.md. Each record: ID, status, severity/impact, actor/time, affected paths, evidence/reproduction, owner, related spec/plan, next action and closure evidence. Check for duplicates. Do not expand the current PR into unrelated fixes without replanning.

## Security is local-only
/docs/security/ is excluded by .gitignore, including its indexes, ledgers, evidence, reviews and handovers. Sensitive security findings must never enter docs/findings, public Git history, PR comments, shared logs, Library uploads or other published artifacts. Keep detailed security decision logs and session evidence inside docs/security/. Public instructions document handling policy only. Do not disclose local finding names or details in public indexes.

Never use git add -f for docs/security/, negate its ignore rule, or move/copy its contents to tracked locations. Before commit inspect `git check-ignore docs/security/index.md` and confirm `git ls-files -- docs/security` returns nothing. If already tracked material is found, stop before publishing and involve the owner; ignore rules do not remove tracked content or historical copies. Gitignore is a publication safeguard, not encryption, access control, or backup. This setup found no tracked security files.

Use SECURITY-0001 IDs within the local directory; keep local metadata there. Record public closure details only after explicit owner authorization and sanitization. Active serious findings that invalidate current acceptance block dependent work rather than being hidden as unrelated debt.
