# Architecture

## Present structure

One Maven reactor builds two modules. `apps/backend` is the Quarkus application and composition root. It depends on `modules/kitchen`, a plain Java module for future kitchen behaviour. Kitchen has no dependency on Quarkus, persistence, an LLM or a messaging provider. No runtime endpoint or schema exists yet.

## First feature design

The [voice-to-record architecture](docs/specs/002-voice-to-record.md) traces an actual recording through interpretation, a MySQL commit, clarification and read-back. It is the proposed first implementation slice.

## Intended flow

A future input adapter identifies the household, actor and source message. Text goes straight to interpretation. A future speech adapter supplies a transcript and retains its relationship to the source according to household policy. The interpreter proposes operations. Domain code resolves conflicts, validates authority and asks for missing context. Persistence commits accepted changes and their evidence together. Current state and action outcomes must be retrievable by identifier.

Before a purchase, an executor will re-read the applicable plan version, permissions and budget, compare the live merchant cart, and handle changes during checkout. Merchant acknowledgement establishes the external outcome. A local database transaction alone cannot guarantee an external purchase happened once.

## Expansion points

Keep household identity and source attribution reusable across chores. Introduce another domain module when a second chore has distinct rules. Add provider interfaces alongside real integrations. Candidate channels include WhatsApp and voice, candidate model hosts include managed APIs and locally hosted weights, and grocery fulfilment may use Instamart. Model choice, deployment topology, payment policy and data modelling remain open.

## Memory boundaries

Repository documents preserve engineering intent and evidence. Future household storage preserves reported events, corrections and external outcomes subject to a retention policy. Semantic search may later index retained records by meaning. Exact queries must resolve to the underlying household records.
