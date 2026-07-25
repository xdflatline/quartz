---
title: "Andrej Karpathy"
detail: "AI researcher; source of the LLM-wiki Pattern the Second Brain's AI-curated wiki is built on, and of the 'RAG is giving the graduate your documents before the exam' framing."
details: "Andrej Karpathy is a well-known AI researcher (formerly OpenAI, Tesla, Stanford; currently at Anthropic as of 2026). The Node AI cites two of his contributions in the Second Brain video: 1) the 'AI maintains its own knowledge wiki' pattern — a few paragraphs in which Karpathy describes how an LLM can write and update Markdown pages, read a small index first, and run check rules against contradictions and orphaned pages. This is the [[Concepts/three-reference-roles]]' Pattern role that the Second Brain's [[Concepts/ai-curated-knowledge-wiki]] is built on. 2) The RAG framing — 'today's LLMs are like a fresh graduate; they know a lot but they know nothing about your specific case. RAG is giving the graduate your documents before the exam.' This is the rationale for the [[Concepts/hybrid-local-search-pattern]]'s RAG pipeline. Karpathy's contribution is conceptual, not a tool: it is a short text that the speaker studied and adapted, not a piece of software the speaker integrated."
tags:
  - entities
created: 2026-07-25
updated: 2026-07-25
type: entitie
source: "[[Raw/thenodeai-second-brain-architecture-2026-07-25]]"
sources:
  - "Raw/thenodeai-second-brain-architecture-2026-07-25"
---

# Andrej Karpathy

**Category:** Person / AI researcher
**Affiliation (2026):** Anthropic
**Notable prior:** OpenAI co-founder, Tesla AI director, Stanford

---

## Overview

Andrej Karpathy is a well-known AI researcher. The Node AI cites two of his contributions in the Second Brain video: the LLM-wiki pattern and the RAG framing. Both contributions are conceptual, not tools: short texts the speaker studied and adapted, not pieces of software the speaker integrated. This is the canonical example of the [[Concepts/three-reference-roles]]' Pattern role: a few paragraphs, not a program.

## Contribution 1: The LLM-wiki pattern

A short text in which Karpathy describes how an AI can maintain its own knowledge wiki. The pattern:

- The AI writes and updates Markdown pages.
- There is a small index that is read first.
- There are check rules against contradictions and orphaned pages.

The remarkable thing about this reference is that it is not a program and not a finished tool. It is a few paragraphs, nothing more. But the idea in it — the AI maintains the knowledge itself according to fixed rules — is one-to-one the answer to capability 3 (Stay clean) of the Second Brain. The implementation is built entirely by the Node AI himself, fitting his vault.

The [[Concepts/ai-curated-knowledge-wiki]] concept page captures the Second Brain's implementation of the pattern: schema file, typed pages, ingest flow, conflict detection, 52 flagged conflicts on the first run.

## Contribution 2: The RAG framing

Paraphrased by the Node AI:

> Today's LLMs are like a fresh graduate. They know a lot, but they know nothing about your specific case. RAG is nothing more than giving the graduate your documents before the exam. Without RAG, the LLM answers from its general training, with RAG, it answers from your context. The same model, your data, the difference.

This is the single line that makes the [[Concepts/hybrid-local-search-pattern]]'s RAG pipeline obvious. The LLM is the graduate, the search engine is the librarian, the vault is the library, the human is the examiner. The pipeline just makes that metaphor literal.

## Why these contributions are Pattern, not Building Block

The Node AI explicitly takes neither code nor a finished product from Karpathy. He takes *ideas*, and he implements them himself, fitting his own system. The Building Block role (e.g. QMD) is a finished component he integrates as-is. The Pattern role is a description he adapts. The same distinction is what makes the [[Concepts/three-reference-roles]] typology useful: a reference can be evaluated for all three roles, and usually exactly one applies.

## How Karpathy's work shows up across the Second Brain

| Concept | Karpathy's contribution | Role |
|---------|--------------------------|------|
| [[Concepts/ai-curated-knowledge-wiki]] | LLM-wiki pattern (AI maintains the wiki under rules) | Pattern |
| [[Concepts/hybrid-local-search-pattern]] | RAG framing (LLM is a fresh graduate; RAG gives them your docs) | Pattern |
| [[Concepts/deterministic-first-architecture]] | Implicit — Karpathy's LLM-wiki keeps the AI in a narrow role, not a foundational one | Pattern (philosophical) |

## The "discarding is a research result" framing

The Node AI's typology also applies to Karpathy's work: he studied Karpathy's pattern, adapted it, and explicitly noted the rejection of the alternative (he could have used a finished tool, e.g. a SaaS wiki; he chose to build his own). Recording the rejection is part of the research result.

## Related Concepts

- [[Concepts/three-reference-roles]] — Karpathy is the Pattern example
- [[Concepts/ai-curated-knowledge-wiki]] — built on the LLM-wiki pattern
- [[Concepts/hybrid-local-search-pattern]] — built on the RAG framing
- [[Entities/thenodeai]] — the speaker who cited both contributions

## References

- Raw Article: [[Raw/thenodeai-second-brain-architecture-2026-07-25]]
- Original: https://m.youtube.com/watch?v=mHSOsy_usAg
- Karpathy's LLM-wiki pattern: a short text, paraphrased in the video
- Karpathy's RAG framing: widely cited, paraphrased in the video
