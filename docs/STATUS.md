# Current handoff

Stage: repository skeleton. Accepted: Java 21, Quarkus, Maven modules, one deployable and MySQL as the intended first operational store. Model, schema and integration choices are open. The repository contains no household data.

Evaluation target: replay a synthetic day with two parents, two children, a cook and a household helper. Score the resulting household state before testing how a merchant maps requested quantities to available packs. This repository contains the evaluation brief. Measured accuracy, token usage and merchant results need a reproducible run.

Next discussion: [first capture spec](specs/001-kitchen-capture.md). Decide these before designing the first schema:

- When a parent requests six eggs, does it mean buy six or bring total stock to six? How should the household clarify or set a default?
- Who can report, request, override or approve spending? How does a cook choose between multiple homes?
- Which evidence should be retained: original audio, transcript, corrected transcript, or only the accepted update? For how long and visible to whom?
- At the cutoff, which changes reopen a draft, and what happens once the merchant has accepted the order?

Future work should add measured model results and actual token counts separately from interpretation examples.

Scaffold validation: module paths, Maven XML and local documentation links checked. Full build pending: JDK and Maven were unavailable in the creation environment.
