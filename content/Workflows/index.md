---
title: "Workflows"
details: "Repeatable workflows for agents — how-to procedures that codify the schema, conventions, and process for tasks the operator runs repeatedly (ingesting research, building catalogs, syncing external systems, etc.). Each workflow lives in its own subfolder named after the workflow itself (not SKILL.md), with a references/ folder and a scripts/ folder where needed."
tags:
  - workflows
  - index
  - wiki
created: 2026-08-07
updated: 2026-08-07
type: index
---

# Workflows

Repeatable workflows for agents. This folder is the home for **how-to procedures** that codify the schema, conventions, and process for tasks the operator runs repeatedly — primarily research ingestion, knowledge-base management, and other agent-driven operations on this wiki.

## What a workflow is (and isn't)

A workflow is **a procedure an agent follows**. It is not:

- a **skill** in the Hermes sense — those live in `~/jin/skills/` and are managed by the Hermes runtime
- a **note** about how something works — that belongs in `Concepts/`
- a **research synthesis** — that belongs in `Research/`

A workflow is the **operational manual** an agent reads when it needs to perform a task: the schema of the inputs, the rules of the process, the pitfalls to avoid, the scripts to run, and the verification steps to confirm success.

## Folder structure

Each workflow is a **subfolder named after the workflow itself**, not a `SKILL.md` file:

```
content/Workflows/
  index.md                                ← this file
  <workflow-name>/
    <workflow-name>.md                    ← the main workflow doc (named after the workflow)
    references/                           ← supporting reference docs (frontmatter rules, build verification, etc.)
    scripts/                              ← any Python/shell scripts the workflow runs
```

The workflow file is named after the workflow, not `SKILL.md` — workflows here are referenced by their actual name from anywhere in the wiki, and a name like `wiki-content-ingestion.md` is more discoverable than `SKILL.md` in a wiki context.

## Frontmatter

Every workflow file uses the same frontmatter shape as the rest of the wiki, with the **simplification** that the wiki uses only `details:` (not `detail:`):

```yaml
---
title: "Workflow Name"
details: "One-paragraph description of what this workflow is and when to use it."
tags:
  - workflow-tag-1
  - workflow-tag-2
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: guide
---
```

The `type:` for workflow files is `guide` (it is procedural documentation, not a concept or entity).

## Available workflows

| Workflow | Purpose |
|----------|---------|
| [[Workflows/wiki-content-ingestion/wiki-content-ingestion\|Wiki Content Ingestion]] | The four-tier Raw → Concept → Entity → Index protocol for ingesting external research into the wiki |
| [[Workflows/wiki-catalog-research/wiki-catalog-research\|Wiki Catalog Research]] | The catalog-style research pattern (closed enumerations of similar items, e.g. LLM model lists, vendor tool inventories) |

## When to add a new workflow

Add a new workflow when:

1. The task is **repeatable** — you'll do it again, or an agent will do it again
2. The task has a **schema** (defined inputs, expected outputs, validation rules) that benefits from being written down
3. The task has **pitfalls** that have already bitten the operator at least once
4. The task spans **multiple files or commands** — i.e. it's not a one-shot, it's a procedure

If the task is one-off and ad-hoc, it stays in chat or in a session memory. If it's a single file with no procedure, it's a note in `Concepts/`.

## When to update a workflow

Update when:

- A pitfall is discovered that the workflow should have caught (add it to the pitfalls section)
- The schema changes (a new tier, a new field, a new file location)
- A verification step is found to be insufficient (add a more thorough check)
- The operator's preferences change (e.g. a new naming convention, a new tag rule)

Do **not** update a workflow just because the underlying skill in `~/jin/skills/` changed — the workflow here is the wiki-specific distillation of the skill, and the source skill in jin is the source of truth. Update the workflow when the wiki-specific adaptation needs to change.
