---
title: "Knowledge Page as Projected View"
details: "Architectural pattern for an agent memory system in which documents are not stored as files but rendered as a projection over processed memory. The page folder tree is a navigable shape; the underlying storage is the bank's consolidated observations and facts. Before a page is written, the memory engine has already extracted facts, deduplicated them, and reconciled contradictions — so the page reflects what holds, not what was said. Delete a page and nothing is lost; it re-projects from memory on the next refresh. Distinct from a hand-maintained wiki (which ages, accumulates contradictions, and needs human upkeep) and from raw files (which have no underlying memory engine to re-derive them)."
tags:
  - concepts
  - memory
  - agent
  - rag
  - architecture-pattern
created: 2026-09-08
updated: 2026-09-08
type: concept
sources:
  - "Concepts/hindsight-knowledge-pages-feature"
---

# Knowledge Page as Projected View

**Source:** Hindsight Knowledge Pages — [hindsight.vectorize.io/developer/knowledge-pages](https://hindsight.vectorize.io/developer/knowledge-pages)
**Category:** Architecture Pattern
**Status:** Production feature in Hindsight (2026-09)

## Overview

A knowledge page is a markdown document an agent's memory bank writes about itself. Each page answers one question — "What are the components here?", "What's our error-handling convention?" — and rewrites itself as the bank learns more. The shape is a wiki. The engine underneath is memory.

The pattern's distinguishing claim is that the page is **a projected view over processed memory**, the way a database view is not a table. The wiki tree, the markdown syntax, and the frontmatter are the rendering; the storage is the bank's consolidated observations and facts.

```
+-----------------------------------+
|  Wiki shape (folder tree, pages)  |  <- navigation & presentation
+-----------------------------------+
|  Markdown + YAML frontmatter      |  <- format
+-----------------------------------+
|  Projected view                   |  <- reconciliation layer
+-----------------------------------+
|  Processed memory                 |  <- observations, facts, entities
|  (extracted → dedup → reconciled) |
+-----------------------------------+
```

## The shape is a wiki

Pages live in a tree of folders (`Architecture/`, `Runbooks/`, `Decisions/`). Nesting is arbitrary; page names are unique within a folder; deleting a folder deletes its subtree. That is the whole structural model — a hierarchy, the way anyone would organize documents by hand.

The tree is what makes a knowledge base **navigable** rather than a flat list of synthesized blobs. Each page stays current on its own refresh schedule; nothing propagates across pages unless explicitly linked.

## The engine is memory

Underneath the wiki shape, every page is built from the bank's already-consolidated observations. Concretely:

1. **Sources are observations only by default** — not raw conversational detail. The bank has already done extract → dedupe → reconcile before the page is rendered. A page that contradicts itself across refreshes cannot happen, because the underlying observations are the reconciled truth.
2. **Refresh is incremental after each consolidation.** When new evidence lands and the bank produces new observations in the page's scope, the page is *edited* (not regenerated) to absorb them. Previous phrasing is preserved unless the underlying observation changed.
3. **Pages never read other pages.** They cannot cite each other into a feedback loop. Each page is a leaf over the observation substrate.
4. **Content budget is larger than a mental model.** A page is a document, not a standing answer — it can hold multi-section structure, tables, examples.

You supply a name and a question. Everything else is a default you can override if you need to — every mental-model setting still applies.

## Projected as real files

The CLI can mirror a bank's knowledge base onto disk:

```bash
hindsight fs mount --bank my-bank
```

The folder tree becomes real directories, each page a real markdown file with YAML frontmatter, kept current by a background refresh loop. From there, everything ordinary works — `ls`, `cat`, `grep`, `rg`, `fzf`, your editor, an agent's file tools. No SDK, no API client, no new vocabulary.

The same content is available as a portable markdown bundle over the API, for exporting or committing elsewhere.

## Why not just raw files?

If the answer is documents in a tree, haven't we reinvented files — the thing a memory system exists to replace?

The difference is what sits underneath.

|  | Hand-maintained wiki | Knowledge page (projected view) |
|---|---|---|
| Storage | Files edited by whoever wrote them | Consolidated observations in the memory bank |
| Contradictions | Accumulate quietly; nothing reconciles | Reconciled at the observation layer before the page renders |
| Aging | Rot — "where information goes to age" | Heals itself — re-projects from memory on refresh |
| Source of truth | Whoever wrote it last wins | The reconciled truth about *what holds* |
| Delete a page | Information is lost | Nothing is lost — re-projects from memory on next refresh |

A file is where information goes to age. Whoever wrote it last wins, contradictions accumulate quietly, and nothing ever reconciles them. Left alone, a hand-maintained wiki becomes a beautifully formatted lie — not because anyone lied, but because keeping it true is a chore, and chores lose.

A knowledge page is a **projected view over processed memory**, the way a database view is not a table. Your raw documents remain the source of truth about *what was said*. The pages are the reconciled truth about *what holds*. This is also why pages heal themselves rather than rot: they aren't the storage, they're the rendering.

## Searchable, but at document level

Pages are searchable at the **document level**: a query returns whole pages, ranked, with snippets. It combines full-text (BM25) and semantic matching, fused server-side, with no reranking step — fast enough to be the first thing an agent reaches for.

This is a different retrieval surface from `recall`, which searches individual memories. Use page search to pick a document; use recall for a specific fact.

The agent *chooses* to call page search — visible in the transcript — rather than having it pushed into context on every turn. Retrieval the agent asked for informs what it's doing; retrieval it didn't ask for tends to derail it.

## Working pattern

For an agent memory system that wants wiki-shaped artifacts:

1. **Pick the projection substrate first.** Memory pages only make sense if the underlying memory is consolidated (extracted → deduplicated → reconciled). Skip the consolidation layer and the page renders whatever the raw stream produced, including contradictions.
2. **Default to observations-only sources.** Letting a page read raw facts gives it access to material that the bank has not yet reconciled. The default should be the layer below raw, not raw itself.
3. **Refresh incrementally after each consolidation pass, not on a schedule.** Schedules age into obsolescence; consolidation triggers age into correctness. The page is a leaf over an event stream, not a periodic batch job.
4. **Never let pages cite each other.** Cross-references are fine for navigation, but a page that reads another page builds a feedback loop. Keep them as leaves over the shared observation substrate.
5. **Expose the tree through the file system.** A markdown mirror on disk makes the wiki navigable with tools the agent already knows (`ls`, `cat`, `rg`) without an SDK.
6. **Search documents, not facts, when the consumer is a person or an agent's first step.** Fact-level search is a recall surface; document-level search is a discovery surface.

## Anti-patterns

- **Treating the page tree as the storage.** The moment you start editing files by hand to "fix" them, you have two sources of truth. The wiki stops healing.
- **Regenerating pages from scratch on refresh.** Full regeneration loses the editor-like precision that makes a page stable and reviewable. Refresh should edit, not replace.
- **Cross-linking pages into a citation graph.** A page that reads another page re-derives its content from the other page's projection, not from the underlying observations. Contradictions hide there.
- **Skipping the consolidation layer.** If the bank stores raw facts and the page renders raw facts, the page is just an indexed dump. The reconciliation value is lost.
- **Pushing page content into the agent's context on every turn.** That defeats the agent's ability to choose what to read. Page search is a tool, not a system prompt injection.

## Related Concepts

- [[Concepts/hindsight-knowledge-pages-feature]] — the canonical Hindsight implementation of this pattern
- [[Concepts/mental-model-vs-knowledge-page]] — the standing-answer vs. document split; pages are mental models with two additions (folder tree, observations-only defaults)
- [[Concepts/scrapbook-graph-model]] — how Hindsight's graph (entities anchored to memory pages, no entity-to-entity edges) supports the reconciliation layer pages project from
- [[Concepts/ai-curated-knowledge-wiki]] — the broader pattern of an AI-maintained wiki; pages are a memory-engine-backed instance of this
- [[Concepts/context-as-materialized-view]] — the database "materialized view" is the structural analog: a precomputed artifact over processed data, not raw tables
- [[Concepts/hindsight-memory-architecture]] — the TEMPR + observation consolidation architecture pages project over

## References

- Source: Hindsight Knowledge Pages — https://hindsight.vectorize.io/developer/knowledge-pages
- FAQ: Mental model vs. knowledge page — https://hindsight.vectorize.io/faq#whats-the-difference-between-a-mental-model-and-a-knowledge-page
