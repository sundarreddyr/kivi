---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

# Testing and QA

Owner: QA for independent acceptance, integration and regression coverage; Senior Engineer for unit-test correctness and testability.

Behavior changes follow red–green–refactor. Record the expected failing test and actual failure before implementation, then passing result and refactor verification. Bug fixes require a regression test reproducing the bug. Documentation/config-only changes with no executable behavior record a reason and appropriate structural validation; do not invent unit tests to satisfy a checkbox.

Use independent expected outcomes, error paths, boundary cases and state transitions. Do not weaken acceptance or delete failing tests to achieve green. QA identifies coverage gaps and keeps regression coverage growing with relevant PRs, not meaningless tests for every edit.

Run relevant checks before commit. While the suite is small, run full integration and regression suites after every commit; record command, revision, result, duration and evidence. Remote CI runs on each push once configured. Required checks must pass on the exact candidate before merge. Missing tools/suites are blocked or not applicable with reason, never passing.

As suite cost grows, measure duration/flakiness and propose an explicit policy change for targeted checks plus broader scheduled checks. No silent relaxation of the current full-suite rule. Fix failures with bounded feedback; unresolved Advisor disagreements follow the two-attempt rule.

Current bootstrap: no runtime behavior changes or new test suites. Existing structural validation applies. Runtime suite/CI introduction belongs to a future authorized milestone.
