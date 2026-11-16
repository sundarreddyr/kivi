---
created_at: "2026-11-14T11:56:05+05:30"
created_by: "Codex"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

> Original path: `docs/decisions/001-modular-monolith.md`. Creation attribution recovered from Git history.

> Historical artifact: retained for provenance only. Earlier acceptance/status wording is historical; this is not an active spec, plan, or current architecture decision. Re-adoption requires a new owner-approved spec and explicit decision.

# 001 — Start with a modular Quarkus application

Status: accepted for the skeleton.

The owner chose Java and Quarkus for household workflows. Use Maven, Java 21 and one application depending on a plain Java kitchen module. These are reversible starting defaults. MySQL is the intended first record store; defer migrations and entities to the modelling milestone.

A separate Python service would add a deployment boundary before a distinct runtime requirement exists. Offline experiments can use Python independently. Revisit extraction as a service if a measured workload requires separate scaling or local inference hardware.
