---
created_at: "2026-11-16T14:25:21+05:30"
created_by: "Codex / pointer-instructions session"
updated_at: "2026-11-16T14:25:21+05:30"
updated_by: "Codex / pointer-instructions session"
---

# Revision-bound evidence

Owner: Senior Engineer records candidate identity; QA identifies the tested state; Advisor identifies the reviewed state. This rule applies to code, contracts, tests and documentation.

## Before commit
A commit SHA alone cannot identify uncommitted changes. Record the base SHA, proposed path list, staged/worktree scope, and a deterministic candidate digest. The digest must cover final contents of every proposed added/modified file and the paths/statuses of removals/renames, including newly created files; `git diff` alone omits untracked files. Document the digest command and scope so another agent can reproduce it. Exclude local security contents from public evidence.

Record each verification command, result, IST time, actor, candidate identity and evidence location. Advisor approval names that same candidate. A passing test or review of an earlier candidate is historical evidence, not approval of the current one.

## After commit and before merge
Record the resulting commit SHA, actual author/committer and time. Run required post-commit checks against that SHA with a clean test worktree, or record all additional inputs/dirty changes and do not call it a clean-SHA result. Before merge verify the candidate against its intended current base/merge result. Changes in dependencies, build inputs or environment that affect validity require relevant revalidation even if source SHA is unchanged.

## Changes invalidate relevant evidence
After code, tests, contracts or documentation change, identify affected acceptance checks and repeat relevant verification; refresh Advisor review for affected content and interactions. Record why any earlier evidence remains applicable. Never carry approval forward silently. Preserve the existing full-suite post-commit rule; selective rechecks do not replace it. Documentation-only changes need structural evidence, not fabricated runtime tests.

- [ ] Final candidate includes new/untracked paths and deletion/rename status.
- [ ] Each review/test result identifies its precise scope and candidate.
- [ ] Changed content and affected interactions reverified.
- [ ] Required checks pass on the actual merge candidate.

See [PR workflow](0004-pr-review-and-commit.md) for commit gates and audit updates without self-referential commit loops.
