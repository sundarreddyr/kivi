---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:25:21+05:30"
updated_by: "Codex / pointer-instructions session"
---

# Proposed PR record template

ID: <plan-qualified PR unit>. Plan/spec: <links>. Status: planned / implementing / review / blocked / committed / merged.
Implementer / QA / Advisor: <actual identities, distinct review actor>. Base SHA: <sha>.
Candidate diff/content digest: <digest with reproducible command/scope covering new file contents and deletion/rename status>. Paths/count: <list/count>.
21–25 exception: <workable-unit justification + Advisor evidence, or N/A>.

## Checklist
- [ ] Acceptance and independently workable scope verified.
- [ ] Recovery triggers/steps, post-recovery checks and migration safety reviewed; evidence or justified N/A linked.
- [ ] TDD/unit evidence, independent QA and relevant pre-commit checks linked.
- [ ] API contracts synchronized or N/A explained.
- [ ] Metadata/docs/logs current; unrelated findings captured.
- [ ] Security ignore/tracked-path check passed.
- [ ] Enforcement readiness reviewed.
- [ ] Independent Advisor whole-diff review comments recorded and blockers resolved.
- [ ] Approved candidate unchanged before commit; subsequent edits trigger relevant review/check refresh.
- [ ] Actual committer/author, SHA and IST time recorded after commit.
- [ ] Full integration/regression post-commit results linked, or actual absence/blocker stated.
- [ ] Push actor/time, remote CI and exact merge-candidate checks linked when performed.

## Advisor comments
| Severity | Path/location | Evidence/consequence | Requested fix | Disposition |
| --- | --- | --- | --- | --- |
| <level> | <path> | <evidence> | <action> | <pending> |

## Commit and push audit
| Action | Actor | IST time | Revision | Command/result evidence |
| --- | --- | --- | --- | --- |
| <commit/push/test> | <actual> | <timestamp> | <sha> | <link> |

## Escalation
<Same issue: attempt 1, attempt 2, then owner blocker; preserve across sessions.>
