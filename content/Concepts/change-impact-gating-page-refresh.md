---
title: "Change-impact gating for knowledge-page refresh"
details: "Incremental page-update gate: before rewriting a knowledge page with new memories, ask of each memory whether it could change the page, and edit from the survivors only; when none can, the update makes no LLM call at all. Rebuilds still run the full reflect path. Reported page accuracy rose for five of seven LLMs while LLM calls per case roughly halved (8.5 to 4)."
tags:
  - concept
  - memory
  - knowledge-management
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Change-impact gating for knowledge-page refresh

**Category:** Knowledge Maintenance Pattern
**Status:** Production in Hindsight 1.2 (vendor-reported)

## Overview

Knowledge pages are living markdown documents a memory bank writes about itself ([[Concepts/hindsight-knowledge-pages-feature]]). They are refreshed incrementally as new memories arrive. The naive incremental design runs a reflect over the new memories and rewrites the page — an LLM-heavy operation on every batch, whether or not the batch matters.

Change-impact gating asks one question of each new memory before paying for any of that:

> **Could this memory change the page?**

Only the memories that pass are used to edit the page. When none pass, the update makes **no LLM call at all**.

## Relationship to rebuilds

- **Rebuild** = regenerate the page from its source observations. It runs reflect, so it inherits every optimization in [[Concepts/evidence-gated-reflect-loop]].
- **Refresh** = apply what is new. This is where the gate earns its keep, because most incremental batches do not change most pages.

The distinction matters: gating a rebuild would be wrong (the page must be regenerated from its sources), while gating a refresh is safe because the page is already believed correct and only deltas are in question.

## Reported results

- `gpt-6-luna`: 82.5 → 90.0 quality at less than half the cost ($7.33 → $3.16 per thousand cases).
- `gemini-3.1-flash-lite`: 85.0 → 90.0 at a third of the cost ($17 → $5.78).
- `gemini-3.8-flash`: 82.5 → 90.0 at 3.6x less cost ($65 → $18).
- Five of seven LLMs keep pages more accurately; the LLM makes about half the calls (≈8.5 → 4 per case) because a memory that cannot change the page never reaches it.

This is the operation where arrows point **up and left at once** — better quality and lower cost, not a trade.

## Why the quality improves too

Filtering noise out of a rewrite is not just cheaper, it is more accurate: a model asked to update a page with forty memories, thirty-eight of which are irrelevant, tends to either over-edit or drift. Restricting the edit to memories judged capable of changing the page keeps the update surgical.

## When this gate is not applicable

- **Pages with no durable prior state** — if the "page" is regenerated from scratch each time, there is nothing to gate against.
- **Adversarial or audit contexts** where every incoming memory must be visibly considered, even when judged irrelevant. Gating is a cost optimization, not a compliance trail.
- **A judge with poor change detection.** The vendor reports this as a strength of its own model — "telling whether a new memory changes a page" scored 79.5 against 56.0–72.0 for other open decision models — which is a warning that this gate is only as good as the model behind it.

## Related Concepts

- [[Concepts/knowledge-page-as-projected-view]] — pages as projections over processed memory
- [[Concepts/hindsight-knowledge-pages-feature]] — the feature this gate optimizes
- [[Concepts/evidence-gated-reflect-loop]] — the rebuild path
- [[Concepts/judgment-triage-before-consolidation]] — the same gate one tier earlier
- [[Concepts/decision-model-as-memory-judge]] — the general pattern

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Research: [[Research/decision-gated-agent-memory]]
