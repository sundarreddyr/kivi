# Working in Kivi

Read [the vision](README.md), [current handoff](docs/STATUS.md) and [architecture](ARCHITECTURE.md) first. Follow the links for the task at hand. Git is the durable project memory across sessions.

1. Check the current branch and working tree. Preserve changes you did not make.
2. Before changing behaviour, identify the relevant spec, the observable result and one example that would disprove correctness. Use a short execution plan for changes spanning modules or services.
3. Keep kitchen rules in the kitchen module. Keep transport and provider dependencies at the application boundary. Maintain one deployable until an accepted decision changes that.
4. Record lasting decisions with their rationale in docs/decisions. Mark proposals as open. Never silently convert a planning example into a household rule.
5. Keep diffs focused. Use synthetic fixtures only. Credentials, household chats, addresses, phone numbers, voice recordings and order receipts do not belong in Git.
6. Run the relevant checks. Report actual commands, results and anything unverified. Update the handoff when scope, decisions, evidence or next work changes. Link the authoritative document rather than copying its contents.

For this milestone, preserve the skeleton boundary. A future implementation session should begin with the domain questions in the handoff.
