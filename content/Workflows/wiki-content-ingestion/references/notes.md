# References — Wiki Content Ingestion

This folder contains the supporting reference docs for the [[wiki-content-ingestion|wiki-content-ingestion workflow]].

## What's here

| Reference | Source | Purpose |
|-----------|--------|---------|
| [mermaid-pitfalls.md](./mermaid-pitfalls.md) | jin skill | Mermaid diagram dark-mode artifacts: root cause, re-runnable cleanup, shell-safety lessons for destructive `sed -i` edits |

## What's not here (and why)

The jin skill ships three other references. They are NOT copied into the wiki because:

- **`gitbook-docs-extraction.md`** — recipe for GitBook-hosted docs (`*.gitbook.io`, `*.mintlify.app`). The operator's current research does not include those sources; if it does in the future, fetch the jin version. The recipe is in `~/jin/skills/software-development/wiki-content-ingestion/references/gitbook-docs-extraction.md`.
- **`filename-collision-recovery.md`** — the worked example of a `write_file` overwrite incident. The recovery pattern is already inlined in the workflow's Pitfalls section (Section 5).
- **`session-example-2026-06-13.md`** — an example session transcript from a single ingestion. Useful for jin, redundant for the wiki workflow (the workflow is the distillation).
