---
title: "QMD"

details: "QMD is a local hybrid search engine that combines classical keyword (BM25-style) search with semantic search over embeddings. It runs fully on-device: a small embedding model produces vectors, the keyword index is built locally, and the combined score is computed locally. Created by Tobi Lütke, founder of Shopify. The Node AI integrated QMD into his Second Brain as the rung-3 component of the [[Concepts/brain-first-search-ladder]] (the search step) and as the search box in the web app. QMD is the canonical example of the [[Concepts/three-reference-roles]]'s Building Block role: a finished, maintained, free component the speaker did not build himself, and the lesson 'don't build anything yourself that already exists as a maintained, finished piece'. Cost story: ~2 seconds of processor work per query, no API token consumption, no cloud round-trip, works offline."
tags:
  - entities
created: 2026-07-25
updated: 2026-07-25
type: entity
source: "[[Raw/thenodeai-second-brain-architecture-2026-07-25]]"
sources:
  - "Raw/thenodeai-second-brain-architecture-2026-07-25"
---

# QMD

**Category:** Tool / Local search engine
**Author:** Tobi Lütke (Shopify founder)
**Platform:** Local (Mac, Linux, Windows)

---

## Overview

A local hybrid (keyword + semantic) search engine, integrated into the Second Brain as the rung-3 component of the [[Concepts/brain-first-search-ladder]] and as the search box in the web app. The Node AI's framing: "do you remember ability number 1, finding without the exact word? That's exactly what QMD delivers — installed as a plugin, integrated, ready to use."

## What it does

QMD indexes a folder of files (the vault) and provides two complementary lookup modes:

- **Keyword search** — classical BM25-style ranking. Fast, precise on exact terms, names, quotes.
- **Semantic search** — vector embeddings produced by a small local model. Matches by meaning, not by shared words. Finds "subtitle style" when the file says "caption formatting convention".

The two modes are combined into a single score and re-ranked. A third component (the fine ranker) can be added for higher precision; the Second Brain's fast variant skips it for latency, the full hybrid (used by Claude Code via the Brain-First ladder) uses it.

## The local-first design

QMD runs fully on-device. No cloud database, no API key, no per-query cost. The cost story from the video: ~2 seconds of processor work per search, ~100 searches per day, all free. The same searches through a cloud semantic-search service would cost real money per query.

This is what makes the [[Concepts/deterministic-first-architecture]] rule livable: the search is a free, deterministic, on-device component. The AI shows up only at the response-generation step, which is rung 5 of the ladder.

## Why it is the Building Block role, not a Pattern

QMD is finished, maintained, and free. The Node AI's lesson: "every hour you don't put into your own search, you put into what makes your system special". He explicitly chose not to write his own search. The hybrid-search architecture is the [[Concepts/three-reference-roles]] Pattern role, but the specific *implementation* is the Building Block role.

## The two-mode setup in the Second Brain

| Mode | Used by | Latency | Components |
|------|---------|---------|------------|
| Fast variant | Web app search box | ~2 s | Query understander + embedding + combined score, no fine ranker |
| Full hybrid | Claude Code Brain-First rung 3 | longer | Fast variant + fine ranker on top |

The two-mode split is also a [[Concepts/deterministic-first-architecture]] decision: the fast path is pure green; the full path adds a small purple at the end.

## What it is not

- Not an LLM. The embedding model is classical ML, not a language model. The "understanding" is shallow — vector similarity, not comprehension.
- Not a graph database. QMD is a search index, not a knowledge graph. The Second Brain's graph visualization is a separate component.
- Not a cloud service. Everything runs locally; there is no SaaS offering from QMD that the speaker uses.

## How to obtain it

The Node AI links to QMD in his video description. The tool is open and free.

## Related Concepts

- [[Concepts/hybrid-local-search-pattern]] — the architectural pattern QMD implements
- [[Concepts/brain-first-search-ladder]] — rung 3 is the QMD call
- [[Concepts/three-reference-roles]] — QMD is the Building Block example
- [[Concepts/deterministic-first-architecture]] — the green core of the search subsystem
- [[Concepts/capabilities-first-system-design]] — QMD serves capability 1 (Find)

## References

- Raw Article: [[Raw/thenodeai-second-brain-architecture-2026-07-25]]
- Original: https://m.youtube.com/watch?v=mHSOsy_usAg
- Linked in: [[Entities/thenodeai]] video description
