---
created_at: "2026-11-14T11:56:05+05:30"
created_by: "Codex"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

> Original path: `docs/specs/001-kitchen-capture.md`. Creation attribution recovered from Git history.

> Historical artifact: retained for provenance only. Earlier acceptance/status wording is historical; this is not an active spec, plan, or current architecture decision. Re-adoption requires a new owner-approved spec and explicit decision.

# 001 — Capture a kitchen update

Status: exploration; implementation and data model deferred.

Outcome: a person can report something once, see what the household recorded, correct it, and later trace a decision back to that report. Persist what was reported, including uncertainty. Physical stock may change without a report.

Use paired audio and typed transcripts with source time, actor and household. The [voice-to-record plan](002-voice-to-record.md) describes the first slice. Use the same intent fixtures to isolate speech errors from interpretation errors.

| Synthetic input or sequence | Expected behaviour to evaluate |
| --- | --- |
| “Eggs over?” versus “Eggs over.” | A question leaves stock unchanged; a report records the observation. |
| “Two milk pouches”; “I bought one of those.” | One remains outstanding. Re-delivery of the same message leaves the result unchanged. |
| “Get tomatoes if guests come.” | Keep the condition pending until an update resolves it. |
| “Just one” replying to a message with eggs and bananas | Leave ambiguous changes pending until clarified. |
| “Skip eggs” after a draft, before purchase | Re-read latest state and remove Kivi’s pending egg request. Preserve unrelated real cart items. |

Evaluate the resulting record changes and retrieval, later the cart delta. Track incorrect writes, missing updates, unnecessary questions, human time and tokens. Label failures by transcription, extraction, domain resolution or merchant integration. A draft is distinct from a submitted order and merchant confirmation. Pilot spending remains a later design decision.
