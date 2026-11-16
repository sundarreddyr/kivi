---
created_at: "2026-11-16T12:49:36+05:30"
created_by: "Codex / primary implementation session"
updated_at: "2026-11-16T12:49:36+05:30"
updated_by: "Codex / primary implementation session"
---

# API contracts

Owner: implementation engineer; QA verifies independently; Advisor reviews compatibility.

For every API-affecting change update both openapi.yaml and postman_collection.json in the same PR. First applicable spec chooses locations and contract-generation strategy. Do not create fictional endpoints or empty API artifacts in this documentation setup.

Cover routes/methods, request and response shapes, status/error semantics, auth/permissions, pagination, idempotency and examples where relevant. Choose one contract authority to avoid competing truths. Generated Postman requests may be synchronized from OpenAPI, but preserve independently maintained assertions and scenario tests.

- [ ] Contract and Postman collection reflect the same candidate behavior.
- [ ] Positive, negative and compatibility cases verified.
- [ ] Breaking changes documented with migration/recovery implications.
- [ ] No credentials, real household data or sensitive security findings embedded.
- [ ] Contract validation and collection execution evidence linked, or limitation explicitly blocked.

Mechanical drift detection is deferred and listed in enforcement readiness; manual comparison remains mandatory.
