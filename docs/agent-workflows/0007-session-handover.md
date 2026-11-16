---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Session handover

Owner: every active agent. Use IST timestamps with explicit +05:30 offset. Work-log records session/actor/role, start/end, branch/base/candidate, progress, decisions with rationale and alternatives, failed approaches, evidence, findings/blockers and next action. Keep security details solely in docs/security/; public notes may say restricted review pending without identifying vulnerabilities.

Start checkpointing near measured 60% context use and finish handover before 70%. Do not start a unit unlikely to fit in the remaining budget. If telemetry is unavailable, never fabricate a percentage: checkpoint after bounded units/before large reads and state usage is estimated. Tool/platform limits may prevent automatic fresh-session creation; leave a resumable state and explicitly hand control back for a new session.

Keep latest handover at most five lines, using links to complete logs; the full audit is not five-line-limited. Record dirty/uncommitted work honestly and identify files, do not commit just to satisfy a handover when review gates are unmet. Next agent rereads root instructions and verifies recorded revision/worktree before resuming.

1. Plan, branch, HEAD and working-tree state.
2. Completed acceptance items and evidence pointers.
3. Decision/failed-approach pointers.
4. Remaining items and blockers.
5. Exact next action and essential files.

Before any commit carrying a log update, refresh that log's own metadata. Preserve prior session entries; corrections are new timestamped entries.
