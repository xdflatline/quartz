---
title: "Hindsight Knowledge Pages Feature"
details: "Canonical reference for Hindsight's knowledge-pages product feature (2026-09). Knowledge pages are living markdown documents a memory bank writes about itself, organized in a folder tree, sourced from consolidated observations by default, refreshed incrementally after each consolidation, and projected onto disk via `hindsight fs mount`. A knowledge page is a mental model with two additions: a place in a folder tree, and a set of defaults tuned for documents rather than answers. Searchable at the document level via hybrid BM25 + semantic search fused server-side, distinct from per-memory `recall`. Reachable through the HTTP API, the `hindsight fs` CLI, and `agent_knowledge_*` SDK tools."
tags:
  - concepts
  - memory
  - agent
  - rag
  - reference
created: 2026-09-08
updated: 2026-09-08
type: concept
sources:
  - "Raw/hindsight-vectorize-knowledge-graphs-vs-vector-search-2026-08-24"
---

# Hindsight Knowledge Pages Feature

**Source:** Hindsight developer docs — [Knowledge Pages](https://hindsight.vectorize.io/developer/knowledge-pages) and FAQ — [Mental model vs. knowledge page](https://hindsight.vectorize.io/faq#whats-the-difference-between-a-mental-model-and-a-knowledge-page)
**Category:** Product Feature / Reference
**Status:** Production in Hindsight 0.9.x (2026-09)

## Overview

Knowledge pages are the **document surface** of a Hindsight memory bank. They are living markdown documents the bank writes about itself, organized in a folder tree, kept current by a background refresh loop, and reachable through three surfaces (HTTP API, CLI, agent SDK).

The feature is Hindsight's answer to "the agent needs a wiki" — without giving up the reconciliation guarantees that the underlying memory engine provides. A knowledge page is the wiki shape; the memory engine underneath is what makes it not rot.

## What a page is

A knowledge page:

- Is a **markdown document with YAML frontmatter** (id, name, type, description, tags, timestamp, body)
- Lives in a **folder** of a knowledge-base tree (nesting is arbitrary; page names are unique within their folder; deleting a folder deletes its subtree)
- Answers **one question** — "What are the components here?", "What's our error-handling convention?", "Who is Alice and how does she relate to Project Atlas?"
- Is **built from the bank's observations only by default** — consolidated, deduplicated beliefs, not raw conversational detail
- **Refreshes incrementally after each consolidation** in scope — the document is *edited* rather than regenerated
- **Never reads other pages** — so pages cannot cite each other into a feedback loop
- Has a **larger content budget** than a mental model — it is a document rather than an answer
- Is **searchable at the document level** via hybrid BM25 + semantic matching, fused server-side, with no reranking step

The page type defaults to `knowledge-page` and can be set via a `type:<x>` tag.

## How pages differ from mental models

A knowledge page **is** a mental model — same engine, same refresh behaviour, same synthesis — with two additions:

|  | Mental model | Knowledge page |
|---|---|---|
| Shape | Standing answer to a question | Markdown document with frontmatter |
| Organization | Flat list, scoped by tags | Nested folders and pages |
| Sources | All fact types by default | Observations only by default |
| Refresh | Off by default | Delta refresh after each consolidation |
| Typical consumer | Application or agent, by lookup | Person or agent browsing and reading |

Anything you can configure on a mental model can be configured on a knowledge page. See [[Concepts/mental-model-vs-knowledge-page]] for the full comparison and decision table.

## The folder tree

Pages live in a tree of folders. The tree is what makes the knowledge base navigable rather than a flat list of synthesized blobs. A typical bank's tree might look like:

```
bank/
├── Architecture/
│   ├── components.md
│   └── data-flow.md
├── Runbooks/
│   ├── incident-response.md
│   └── deploy-process.md
└── Decisions/
    ├── adr-001-vector-db-choice.md
    └── adr-002-graph-strategy.md
```

Each page is a leaf. Pages cannot cite each other into a feedback loop; the tree is for navigation only.

## Surfaces

The feature is reachable through three surfaces:

### 1. HTTP API — Knowledge Base section

Full endpoint surface in the [API reference](https://hindsight.vectorize.io/api-reference#tag/Knowledge-Base):

| Endpoint | Method | Purpose |
|---|---|---|
| `/v1/default/banks/{bank_id}/knowledge-base/tree` | GET | Get the full knowledge-base tree |
| `/v1/default/banks/{bank_id}/knowledge-base/folders` | POST | Create a knowledge-base folder |
| `/v1/default/banks/{bank_id}/knowledge-base/pages` | POST | Create a knowledge-base page |
| `/v1/default/banks/{bank_id}/knowledge-base/search` | GET | Hybrid search over knowledge pages (BM25 + vector) |
| `/v1/default/banks/{bank_id}/knowledge-base/pages/{page_id}` | GET | Get a page as a markdown document (frontmatter + body) |
| `/v1/default/banks/{bank_id}/knowledge-base/nodes/{node_id}` | PATCH | Rename/move a node or update a page's options |
| `/v1/default/banks/{bank_id}/knowledge-base/nodes/{node_id}` | DELETE | Delete a node |

The `GET .../pages/{page_id}` response includes the full markdown document (YAML frontmatter + markdown body), ready to write to disk or feed to an LLM.

The `GET .../knowledge-base/export` endpoint returns the whole knowledge base as a portable markdown bundle.

### 2. CLI — `hindsight fs mount`

```bash
hindsight fs mount --bank my-bank
```

The folder tree becomes real directories on disk; each page becomes a real markdown file with YAML frontmatter, kept current by a background refresh loop. From there, every ordinary tool works — `ls`, `cat`, `grep`, `rg`, `fzf`, your editor, an agent's file tools. No SDK, no API client, no new vocabulary.

The CLI surface is what makes the feature usable for non-engineers and for agents that already know how to navigate a filesystem.

### 3. Agent SDK — `agent_knowledge_*` tools

The agent SDK exposes `agent_knowledge_*` tools so an agent can list, read, create, and update its own pages during a session. The exact tool names depend on the SDK (Python / TypeScript / Go), but the surface is consistent: list pages, read a page, create or update a page, move/rename a node.

This is the surface that lets an agent maintain its own wiki — it can read the current state of a page, notice it is missing something, and write an updated version back, all within the same session.

## Document-level search vs. memory-level recall

Pages are searchable at the **document level**: a query returns whole pages, ranked, with snippets. It combines full-text (BM25) and semantic matching, fused server-side, with no reranking step. Fast enough to be the first thing an agent reaches for.

This is a different surface from `recall`, which searches individual memories. Use page search to pick a document; use recall for a specific fact.

The agent *chooses* to call page search — visible in the transcript — rather than having it pushed into context on every turn. Retrieval the agent asked for informs what it is doing; retrieval it did not ask for tends to derail it.

## Working pattern

To use knowledge pages effectively:

1. **Pick the question each page answers.** A page that tries to cover everything becomes a wall of text; a page that answers one question is browsable. The bank does not enforce this — the developer does.
2. **Trust the observation-only default.** Letting a page read raw facts gives it access to material that has not been reconciled. The default keeps the page's output internally consistent across refreshes.
3. **Use folders for taxonomy, not chronology.** `Architecture/`, `Runbooks/`, `Decisions/` — what the page is *about*, not when it was last touched. Pages render current regardless of folder.
4. **Prefer `hindsight fs mount` for bulk editing.** Edit multiple pages with the tools you already know; the background refresh keeps them current.
5. **Use the HTTP API for programmatic creation.** When seeding a new bank with starter pages, the `POST .../pages` endpoint is the right surface.
6. **Use `agent_knowledge_*` for in-session maintenance.** When an agent notices a page is stale or wrong, it can fix the page without leaving the session.

## Anti-patterns

- **Writing pages that try to be everything.** A page that summarizes the whole codebase is a search surface in disguise. Keep pages narrow.
- **Letting pages read each other.** This breaks the no-feedback-loop invariant. Cross-references are fine for navigation; cross-reading is not.
- **Treating the page tree as the storage.** The moment you start editing files by hand to "fix" them, you have two sources of truth. The wiki stops healing.
- **Skipping the observation layer.** If the bank has not consolidated, the page renders whatever the raw stream produced. The reconciliation value of the projection is lost.
- **Pushing page content into the agent's context on every turn.** That defeats the agent's ability to choose what to read. Page search is a tool, not a system-prompt injection.

## Related Concepts

- [[Concepts/knowledge-page-as-projected-view]] — the deeper architectural pattern (projection over processed memory)
- [[Concepts/mental-model-vs-knowledge-page]] — the standing-answer vs. document split
- [[Concepts/scrapbook-graph-model]] — the underlying graph data model (memory units as pages, entities as stickers) that pages render over
- [[Concepts/hindsight-memory-architecture]] — TEMPR + observation consolidation substrate
- [[Concepts/hindsight-memory-system]] — the higher-level Hindsight framework
- [[Concepts/ai-curated-knowledge-wiki]] — the broader pattern of an AI-maintained wiki; pages are the memory-engine-backed instance
- [[Concepts/context-as-materialized-view]] — the database "materialized view" is the structural analog

## References

- Developer docs: https://hindsight.vectorize.io/developer/knowledge-pages
- FAQ: https://hindsight.vectorize.io/faq#whats-the-difference-between-a-mental-model-and-a-knowledge-page
- API reference: https://hindsight.vectorize.io/api-reference#tag/Knowledge-Base
- Mental Models API (same engine, different defaults): https://hindsight.vectorize.io/developer/api/mental-models
- Vectorize (vendor): [[Entities/vectorize]]
