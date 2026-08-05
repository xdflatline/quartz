---
title: "spaCy NER"
detail: "spaCy's Named Entity Recognition pipeline — a non-generative, statistical NER system used in Zero-Mem to build the entity–context graph over agent memory traces."
details: "spaCy is an industrial-strength open-source NLP library for Python. Its Named Entity Recognition (NER) pipeline is a non-generative, statistical system that detects and classifies named entities (people, organizations, locations, dates, products, etc.) in running text. In Zero-Mem, spaCy NER is the non-generative NER pipeline that detects entities in each context unit to build the entity–context graph. Each detected entity becomes a graph node; each co-occurrence in a context unit becomes an edge with weight equal to the normalized occurrence frequency. Because the NER is statistical and not LLM-based, it is permitted under the zero-token memory regime — there are no LLM calls, no LLM input or output tokens, and the pipeline is deterministic given the same model checkpoint and text."
tags:
  - entities
created: 2026-08-05
updated: 2026-08-05
type: entitie
source: "[[Raw/arxiv-zero-mem-2026-08-05]]"
sources:
  - "Raw/arxiv-zero-mem-2026-08-05"
---

# spaCy NER

**Source:** [[Raw/arxiv-zero-mem-2026-08-05]] — Xiao et al., 2026
**Category:** Tool (NLP library)
**Website:** https://spacy.io

## Overview

spaCy is an industrial-strength open-source NLP library for Python. Its Named Entity Recognition (NER) pipeline is a non-generative, statistical system that detects and classifies named entities (people, organizations, locations, dates, products, monetary values, etc.) in running text. The pipeline combines a tok2vec embedding, a transition-based parser, and statistical models trained on annotated corpora (OntoNotes, CoNLL, etc.).

In Zero-Mem, spaCy NER is the non-generative NER pipeline that detects entities in each context unit to build the entity–context graph. Each detected entity becomes a graph node; each co-occurrence in a context unit becomes an edge with weight equal to the normalized occurrence frequency.

## Why spaCy Specifically

The paper's choice is illustrative, not load-bearing. The key property is **non-generative**: spaCy NER is a statistical classifier, not an LLM. It does not invoke a language model to produce tokens; it applies a trained neural architecture to identify spans and label them. This is what permits it under the zero-token memory regime — no LLM calls, no LLM input or output tokens, deterministic given the same model checkpoint and text.

A functionally equivalent alternative would be any non-generative NER system: Stanza, Flair, HuggingFace token classifiers (`xlm-roberta-base-finetuned-ner-panx` for multilingual), or a domain-specific regex + gazetteer hybrid. The architectural argument does not depend on spaCy; it depends on the non-generative property.

## Role in Zero-Mem

For every context unit di, the NER pipeline produces a set of detected entities E(di). The pipeline then builds the graph G = (Vd ∪ Ve, Ede ∪ Edd):

- Vd = context nodes (one per context unit)
- Ve = entity nodes (one per distinct detected entity, possibly with surface-form variants clustered)
- Ede = entity–context co-occurrence edges with weight `w(di, e) = c(e, di) / Σ(e' ∈ E(di)) c(e', di)`
- Edd = adjacency edges between neighboring context units (preserves local continuity; not driven by NER)

The graph records observed co-occurrence, not inferred relations. There is no step where an LLM proposes "subject–relation–object" triples; the edges exist because the same entity string was detected in the same context.

## How It Differs from LLM-Based Extraction

| Property | spaCy NER (statistical) | LLM-based NER (extractive prompt) |
|----------|--------------------------|------------------------------------|
| Output | Span + label, deterministically | Span + label, sampled from a distribution |
| Cost | One forward pass through a small encoder | At least one LLM call (often two: extract + verify) |
| Latency | Milliseconds per 1k tokens | Seconds per 1k tokens |
| Reproducibility | Identical for the same model + text | May vary across runs even with temperature=0 |
| Token cost | 0 LLM tokens | Hundreds to thousands of LLM tokens |
| Permitted in zero-token regime | Yes | No |

The last row is the decisive one. A system that uses an LLM for NER has already left the zero-token regime, regardless of what comes after.

## Limitations and Trade-offs

- **Domain sensitivity.** Off-the-shelf spaCy models are trained on web news and may miss domain-specific entities (e.g. internal product names, custom acronyms). A production system may need to fine-tune or supplement with a gazetteer.
- **Coreference resolution.** Out-of-the-box spaCy NER does not resolve pronouns or aliases to entities. If "the company" and "Acme Corp" refer to the same entity, the NER will produce two distinct surface forms. Zero-Mem's graph records both, and downstream propagation may link them via co-occurrence; but explicit coreference is a separate step.
- **Multilingual coverage.** spaCy has separate models per language. For multilingual agent memory, a multilingual model (XLM-RoBERTa-based) or per-language pipelines are required.

None of these limitations are unique to spaCy — they apply to any statistical NER system. The paper uses spaCy as a stand-in for "any non-generative NER".

## Related Concepts

- [[Concepts/zero-token-memory-operations]] — the operating regime spaCy NER supports without violating
- [[Concepts/provenance-preserving-memory-substrate]] — the substrate spaCy NER helps build without rewriting
- [[Concepts/dual-view-evidence-retrieval]] — the retrieval design that uses the entity–context graph spaCy NER produces
- [[Concepts/agent-memory-layer-patterns]] — the broader memory landscape

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- Paper: [[Papers/zero-mem-zero-token-agent-memory]]
- arXiv: https://arxiv.org/html/2607.29377v1
- spaCy: https://spacy.io
