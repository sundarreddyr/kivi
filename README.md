---
created_at: "2026-11-14T11:56:05+05:30"
created_by: "Codex"
updated_at: "2026-11-16T14:29:54+05:30"
updated_by: "Codex / documentation-layout session"
---

# Kivi

Kivi is a household memory and chore-assistance project. Current work establishes repository context and engineering workflows. Product scope and architecture await the first owner-defined spec.

Start with [AGENTS.md](AGENTS.md), [ARCHITECTURE.md](ARCHITECTURE.md), and [documentation navigation](docs/index.md). Product specifications have their own [specs/](docs/specs/index.md) directory; none is active.

The existing Maven scaffold is preserved. Run `python3 scripts/check.py` for the existing XML/module/link check. Documentation validation is recorded in [setup audit](docs/governance/0003-documentation-setup-audit.md). Runtime tests and CI are not introduced in this change.

## Local-only security records
The `docs/security/` directory is intentionally excluded by `.gitignore`. It holds sensitive findings and evidence only on this machine. Do not force-add it or copy its contents into public artifacts. Git ignore does not protect tracked history or stop explicit force-adds; inspect tracked paths before committing.

[Archived drafts](docs/archive/index.md) preserve previous work but do not define active requirements.
