---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

# Engineering roles and escalation

Senior Engineer implements the assigned milestone, writes testable code, owns unit-test correctness, and records decisions/findings. QA independently derives acceptance, integration, and regression tests from the spec and failure cases; QA must not merely mirror implementation assumptions. Advisor is an independent Staff/Principal-style reviewer of the whole proposed PR before commit.

Use distinct agent sessions/identities where tools permit. Delegate bounded responsibilities; avoid concurrent writes to the same file. If independent review is unavailable, record that limitation and do not claim the review gate passed. The implementer cannot sign their own independent approval.

During implementation, consult Advisor for doubts, ambiguous instructions, contradictory evidence, scope mismatch, or an anomaly. Record question, evidence, alternatives, response and disposition in the plan. Count at most two resolution cycles for the same unresolved issue. If still unresolved, stop dependent work, mark a blocker, and wait for owner input. Do not reset the counter in a new session. Unaffected authorized work may continue. No per-file reviewer loop.

Review feedback may trigger fixes and a refreshed final review. Reviewers identify severity, path/location, reproducible evidence, consequence, and requested resolution; distinguish blockers from suggestions.
