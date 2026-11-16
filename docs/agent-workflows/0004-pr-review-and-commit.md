---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

# PR review and commit

Owner: Senior Engineer; independent Advisor approval required before commit. PR means the complete proposed merge unit, even before a remote PR exists. Review the whole diff against its intended base, including tests/contracts/docs and cross-file behavior.

20 changed tracked paths normally; 21–25 only when the additional files complete one coherent workable unit, with Advisor agreement and rationale. Above 25 must split. Initial repository commit alone is exempt; an existing repo's new documentation setup is not an initial commit. Count all changed paths including tests/docs/generated/deleted files; a rename counts once as a changed path. Declare base and dependencies for stacked PRs; each intermediate state must work.

- [ ] Spec/plan authorization and acceptance mapping confirmed.
- [ ] Proposed file list/budget and exception evidence recorded.
- [ ] Relevant checks pass; no behavior change or absent suites stated accurately.
- [ ] API artifacts updated together, or N/A justified.
- [ ] Metadata, indexes, findings, session log and checklists current.
- [ ] Security ignore/tracked-path checks pass without exposing contents.
- [ ] Pre-commit enforcement-readiness review completed.
- [ ] Advisor reviews final candidate and records comments/dispositions.
- [ ] Candidate identified by base SHA plus deterministic diff/content digest before commit.
- [ ] Commit author/committer, SHA and IST time recorded after commit.
- [ ] Post-commit suites run and recorded for that SHA.
- [ ] Push/remote CI results recorded when configured; unavailable is not pass.
- [ ] Exact candidate passes required verification before merge; merge-base changes trigger relevant revalidation.

Any post-review candidate edit invalidates approval for affected content. Audit-only follow-up changes need their own review; do not amend a reviewed commit merely to insert its own SHA into a file. Record SHA and post-commit evidence in the subsequent audit update or external PR record. Do not recursively create commits just to log logging commits. Roll back/recover a failed local commit or fix it before further progression; never claim success from a failed post-commit run.
