---
title: "Mental Model vs. Knowledge Page"
details: "Comparison of two artifact types in the Hindsight agent-memory system. A mental model is a standing answer to a question; flat, scoped by tags, sourced from all fact types by default, refreshed off by default, and typically consumed by application code or an agent via lookup. A knowledge page is a markdown document with frontmatter; organized in a folder tree; sourced from observations only by default; refreshed incrementally after each consolidation; and typically consumed by a person or agent that browses and reads. A knowledge page is a mental model with two additions: a place in a folder tree, and a set of defaults tuned for documents rather than answers. Anything you can configure on a mental model can be configured on a page."
tags:
  - concepts
  - memory
  - agent
  - rag
  - comparison
created: 2026-09-08
updated: 2026-09-08
type: concept
sources:
  - "Concepts/hindsight-knowledge-pages-feature"
---

# Mental Model vs. Knowledge Page

**Source:** Hindsight FAQ — [Mental model vs. knowledge page](https://hindsight.vectorize.io/faq#whats-the-difference-between-a-mental-model-and-a-knowledge-page) and [Knowledge Pages developer docs](https://hindsight.vectorize.io/developer/knowledge-pages)
**Category:** Comparison
**Status:** Current as of Hindsight 0.9.x (2026-09)

## Overview

A **knowledge page is a mental model** — the same engine, the same refresh behaviour — with two additions: a place in a folder tree, and a set of defaults tuned for documents rather than answers.

Both artifacts are *standing synthesized content* in a Hindsight memory bank. The difference is **how they are organized**, **where they pull from**, **how they refresh**, and **who reads them**. The defaults differ in those four axes; everything else (the underlying synthesis machinery, the bank config, the LLM call) is shared.

## Side-by-side

|  | Mental model | Knowledge page |
|---|---|---|
| **Shape** | A standing answer to a question | A markdown document with frontmatter |
| **Organization** | Flat list, scoped by tags | Nested folders and pages |
| **Sources** | All fact types by default (world, experience, observation, mental model) | Observations only by default |
| **Refresh** | Off by default (synthesized on demand or by trigger) | Delta refresh after each consolidation in scope |
| **Content budget** | Compact — designed to fit in a prompt or a lookup | Larger — designed to be browsed and read |
| **Typical consumer** | Your application or an agent, by lookup | A person or agent browsing and reading |
| **Cross-page influence** | Can read other mental models | Never reads other pages |

## When to use which

### Use a mental model when

- **Something in your system looks up the answer.** A mental model is the right shape when the consumer is a function call: `bank.recall_mental_model("user-preferences")` returns a synthesized paragraph.
- **The answer needs to be small and embeddable.** Mental models are sized for prompt insertion during `reflect`, not for human reading.
- **You want explicit refresh control.** Mental models let you choose the trigger (scheduled, on-demand, on a specific event). Pages run on a delta refresh loop tied to consolidation.

### Use a knowledge page when

- **The result is meant to be browsed and read directly, like a wiki.** Pages are documents — multi-section, with examples, tables, links.
- **You want a navigable structure.** Pages live in a folder tree. The tree is the API: agents can `ls` the directory to discover what exists.
- **You want the page to stay current without explicit refresh calls.** Pages edit themselves whenever consolidation produces new observations in scope.
- **The content should reflect only reconciled knowledge, never raw facts.** The observations-only default means the page can never contradict itself across refreshes — contradictions are reconciled at the observation layer.

## Same engine, different defaults

The mental model exposes its mechanics — what it reads, when it rebuilds, how it edits itself. Nobody should have to think about synthesis scope and refresh triggers to keep a wiki. So a knowledge page comes with those decisions already made:

- **Built from observations only** — consolidated, deduplicated beliefs, rather than raw conversational detail.
- **Refreshes incrementally** after each consolidation, editing the document rather than regenerating it.
- **Never reads other pages** — so pages cannot cite each other into a feedback loop.
- **Larger content budget** — it's a document rather than an answer.

You supply a name and a question. Everything else is a default you can override if you need to — **every mental-model setting still applies** to a knowledge page.

## A practical decision table

| Symptom / requirement | Pick |
|---|---|
| "What is the user's coding style preference?" — needs to flow into `reflect` context | Mental model |
| "What is the architecture of this codebase?" — needs to be a browsable wiki page | Knowledge page |
| "What did Alice say about Project Atlas last spring?" — fact lookup | Neither — use `recall` (memory search) |
| "Summarize our error-handling convention." — sits in a folder with other convention pages | Knowledge page |
| "What's the user's current mood, for the next LLM call?" — embedded in prompt | Mental model |
| "What changed in our deploy process last quarter?" — answered from reconciled observations | Knowledge page |

## Working pattern

For a Hindsight bank:

1. **Start with mental models for hot-path lookup.** Anything the agent or application reads on every turn belongs as a mental model — small, synthesized, cheap to recall.
2. **Promote to knowledge pages when consumers start browsing.** When you find yourself writing a viewer for a mental model's content, convert it to a page and let the consumer `cat` it instead.
3. **Use a folder tree to model taxonomy, not chronology.** Pages live in `Architecture/`, `Runbooks/`, `Decisions/`, not `2026-Q1/` — the tree organizes by what the page is *about*, not when it was last touched. The page renders current regardless of folder.
4. **Don't try to make a mental model do a page's job.** A mental model that grows beyond a few paragraphs is a page that hasn't been promoted yet.
5. **Don't try to make a page do a mental model's job.** A page that gets pulled into every `reflect` call is a mental model with extra cost.

## Anti-patterns

- **Using a knowledge page as a prompt fragment.** Page content is too large and too slow to refresh for that — use a mental model.
- **Using a mental model as a wiki.** Mental models are flat and not navigable; if you find yourself building a directory structure for them, switch to pages.
- **Letting pages read each other.** This breaks the "no feedback loop" invariant. The page must be a leaf over the observation substrate, not a node in a citation graph.
- **Configuring a page to read raw facts.** Defeats the reconciliation guarantee. If you need raw-fact coverage, the question is whether a mental model is more appropriate.
- **Forgetting that pages can have any mental-model setting overridden.** Pages are not second-class citizens — they are mental models with defaults. If a default doesn't fit, change it.

## Related Concepts

- [[Concepts/knowledge-page-as-projected-view]] — the deeper architectural pattern (projection over processed memory) that pages implement
- [[Concepts/hindsight-knowledge-pages-feature]] — the canonical Hindsight implementation, including `hindsight fs mount`
- [[Concepts/hindsight-memory-architecture]] — the TEMPR + observation consolidation substrate that both mental models and pages render over
- [[Concepts/agent-memory-layer-patterns]] — the broader agent-memory landscape where both artifacts fit

## References

- FAQ source: https://hindsight.vectorize.io/faq#whats-the-difference-between-a-mental-model-and-a-knowledge-page
- Developer docs: https://hindsight.vectorize.io/developer/knowledge-pages
- Mental Models API: https://hindsight.vectorize.io/developer/api/mental-models
