# Scripts — Wiki Content Ingestion

This folder contains the supporting scripts for the [[wiki-content-ingestion|wiki-content-ingestion workflow]].

## What's here

| Script | Source | Purpose |
|--------|--------|---------|
| `quote-frontmatter.py` | jin skill | Bulk-quote `details:` values in markdown frontmatter to prevent YAML parse failures when the value contains a colon |
| `audit-garden.py` | jin skill | Audit the wiki for orphaned wikilinks, missing files, and other structural drift |

## When to run

- **`quote-frontmatter.py`** — run before any `npx quartz build` where a new file's `details:` value contains a colon. Idempotent.
- **`audit-garden.py`** — run periodically (e.g. before merging a chore branch into `publish`) to catch structural drift.

## Source-of-truth vs wiki copy

These scripts are copied from `~/jin/skills/software-development/wiki-content-ingestion/scripts/`. The jin version is the source of truth; the wiki copy is for the workflow to be self-contained.

If the operator updates the scripts in jin, this folder should be re-synced. The plan's Phase 6 (T6.1) handles the jin-side update; the wiki copy follows.

## Known issue

`audit-garden.py` currently checks for both `detail` and `details` in the `required_keys` list. After the 2026-08-07 housekeeping pass drops `detail:` entirely, this list needs to be updated to only `details`. This is a known issue; the fix is a single-line edit and will be done as part of T2.1 or the equivalent post-migration step.
