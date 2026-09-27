---
title: "Chroma Context-1: A Small Specialized Retrieval Subagent"
details: "Synthesis of the Chroma Context-1 technical report (Bashir, Hong, Jiang, Shi; March 2026), which trains a 20B agentic search model that matches frontier LLMs on retrieval benchmarks at ~10x lower cost. Synthesizes five architectural and training concepts (agentic self-pruning, retrieval subagent separation, extraction-based task verification, F-β reward curriculum, trajectory-recall reward term) with the cross-domain generalization evidence and the open questions the paper itself flags. Pairs naturally with the earlier [[Research/llm-context-rot-evaluation-2026]] work — Context-1's self-pruning mechanism is a direct response to the context-rot phenomenon."
tags:
  - research
  - llm
  - agent
  - rag
  - training
created: 2026-09-27
updated: 2026-09-27
type: research
sources:
  - .Raw/chroma-context-1-2026-03.md
related:
  - "[[Raw/chroma-context-rot-2026-07]]"
  - "[[Research/llm-context-rot-evaluation-2026]]"
---

# Chroma Context-1: A Small Specialized Retrieval Subagent

**Source:** [[Raw/chroma-context-1-2026-03]]
**Authors:** Hammad Bashir, Kelly Hong, Patrick Jiang, Zhiyi Shi
**Publisher:** Chroma
**Date:** March 2026

## One-Sentence Summary

A 20B-parameter agentic search model — trained on synthetic multi-constraint tasks with SFT + CISPO RL — matches frontier LLMs on retrieval benchmarks at a fraction of the cost by operating as a retrieval subagent that self-edits its own context.

## The Three Underlying Claims

1. **Search quality and reasoning quality are different problems.** They can be measured independently and trained separately. Frontier models are good at both because they are large; a small model trained specifically for search can match the *search* quality without paying the *reasoning* cost.
2. **Self-editing context is sufficient for long-horizon retrieval.** A 20B model with a `prune_chunks` tool under a hard token budget, properly trained, can complete multi-hop searches that would otherwise fill the context. No external memory, no lossy summarization — selective document-level retention inside the prompt.
3. **Synthetic multi-constraint tasks with extraction-based verification scale.** Generating 8,000+ tasks across four domains is feasible without full human annotation, provided quote-pair grounding is used to verify supporting documents and distractors.

## Architecture in One Diagram

```
[Query]
   │
   ▼
┌──────────────────────────────────────────┐
│  Context-1 (20B gpt-oss-20b + LoRA)      │
│                                          │
│  Tools:                                  │
│   • search_corpus  (hybrid BM25+dense)   │
│   • grep_corpus    (regex)               │
│   • read_document  (chunked, reranked)   │
│   • prune_chunks   (self-edit context)   │
│                                          │
│  Budget: T_budget / S_budget searches    │
│   Soft threshold at T_budget/2           │
│   Hard cutoff near T_budget              │
└──────────────────────────────────────────┘
   │
   ▼
[Ranked documents]
   │
   ▼
┌──────────────────────────────────────────┐
│  Frontier Reasoning Model                │
│  (GPT-5.x / Claude / Gemini / Kimi)      │
└──────────────────────────────────────────┘
   │
   ▼
[Final answer]
```

## Five Concepts This Paper Introduces or Operationalizes

- **[Agentic self-pruning of context during retrieval]([[Concepts/agentic-self-pruning-context]])** — the agent decides which chunks to keep via a tool call, under a hard budget enforced by the harness. Distinct from summarization and external memory paging.
- **[Retrieval subagent architecture]([[Concepts/retrieval-subagent-architecture]])** — strict two-tier division of labor: a small specialized searcher feeds a frontier reasoner. Composes with subagent-as-tool composition patterns at a different scale.
- **[Extraction-based task verification]([[Concepts/extraction-based-task-verification]])** — synthetic task quality verified by quote-pair extraction rather than full human reading. >80% human-judge alignment across all four domains.
- **[F-β reward curriculum]([[Concepts/f-beta-reward-curriculum]])** — anneal β from 4 to 2 across training epochs, shifting the reward's bias from recall-heavy to moderately recall-leaning as the agent becomes competent.
- **[Trajectory-recall reward term]([[Concepts/trajectory-recall-reward]])** — credit the agent for documents encountered during search even if pruned. Composed with the outcome F-β at 30% weight. Made possible by the harness's split between the agent's pruned view and the reward's unpruned trajectory.

## Training Pipeline

```
Synthetic task generation (8,000+ tasks across 4 domains)
   │
   ▼
LLM-as-judge extraction-based verification (>80% alignment)
   │
   ▼
SFT (Kimi K2.5 rollouts, filtered by trajectory/output recall)
   │
   ▼
CISPO RL (8 rollouts per query, within-group normalization)
   │
   ▼
MXFP4 quantization-aware distillation for inference
   │
   ▼
vLLM serving on B200, 400-500 tok/s
```

The curriculum has two axes operating together:

- **Difficulty curriculum** — query mix shifts from low-hop to high-hop over training phases.
- **Reward curriculum** — F-β weighting shifts from recall-heavy (β=4) to moderately recall-leaning (β=2).

## Results in Brief

| Benchmark | Context-1 (4x) | Frontier 200k-no-prune best |
| --- | --- | --- |
| Web (Diff. 2+) | 0.97 | 0.99 (opus-4.5, gpt-5.2) |
| Finance (Diff. 1+) | 0.82 | 0.90 (opus-4.5) |
| Legal | 0.95 | 0.98 (opus-4.5) |
| Email | 0.98 | 0.98 (all) |
| BrowseComp-Plus | 0.96 | 0.94 (gpt-5.2 200k) |
| LongSeal | 0.79 | 0.89 (gpt-5.2 200k) |
| Seal0 | 0.52 | 0.72 (opus-4.5 200k) |
| FRAMES | 0.96 | 0.97 (opus-4.5+) |
| HotpotQA | 0.99 | 0.99 (saturated) |

**Take-aways:**

- Context-1 (4x) is on the frontier for most benchmarks. Cost per query is substantially lower.
- The benchmarks where frontier models still win decisively are the ones where (a) the corpus is small enough that frontier context can hold it, or (b) the questions are adversarial in ways the synthetic training distribution didn't cover (Seal0).
- Generalization to the held-out email domain is strong — the model wasn't trained on email-style text but improved substantially there.
- HLE shows that adding any search subagent helps the baseline Opus-4.6 answerer; the variation across search-agent models is real but smaller than on other benchmarks, suggesting HLE's bottleneck is reasoning rather than retrieval.

## Relationship to the Earlier Context-Rot Work

The [Context Rot report]([[Research/llm-context-rot-evaluation-2026]]) (Hong, Troynikov, Huber; July 2026) documented that LLM performance degrades non-uniformly as input length grows — even on simple retrieval tasks. Context-1's [self-pruning context mechanism]([[Concepts/agentic-self-pruning-context]]) is the direct architectural response: by keeping the context window small and curated, the model operates in the regime where context rot is least severe. This is a **complementary pair of papers** — one characterizes the phenomenon, the other demonstrates the fix.

## Open Questions the Paper Itself Flags

- **Breadth vs depth queries.** All training tasks are depth-oriented (find one answer satisfying many criteria). Real search is often breadth-oriented (find every document matching one criterion). Different challenges around completeness, deduplication, and stopping conditions.
- **Structured data search.** The current tool set (search, grep, read, prune) is poor fit for tables, JSON, spreadsheets. Code execution tools are the obvious extension.
- **Metadata-aware queries.** Real corpora have schemas. The agent has no mechanism to discover or exploit metadata structure.
- **Hybrid context management.** Pure selective retention preserves evidence but rigidly. Hybrid approaches combining selective retention with targeted summarization may be needed for very long trajectories.
- **Joint retrieval + agent training.** Embedding model, reranker, and search agent are currently trained independently. Late-interaction architectures like ColBERT could let the retrieval stack co-adapt with the agent's query distribution.

## When the Pattern Does and Does Not Apply

**Applies:**

- Multi-hop retrieval over a large corpus.
- Cost or latency budget that rules out a frontier model doing the search.
- Multi-constraint queries where the agent must compose evidence across documents.
- Question-answering workloads where a frontier reasoning model already exists for the answerer.

**Does not apply:**

- Single-shot retrieval where stuffing the corpus in context is feasible.
- Breadth queries (need completeness guarantees, not depth exploration).
- Structured-data-heavy corpora where the right tool is code execution.
- Domains where the reasoning model itself is the bottleneck, not the search.

## Related Pages

- Raw: [[Raw/chroma-context-1-2026-03]]
- Raw: [[Raw/chroma-context-rot-2026-07]]
- Entity: [[Entities/chroma]]
- Entity: [[Entities/chroma-context-1]]
- Concepts: [[Concepts/agentic-self-pruning-context]], [[Concepts/retrieval-subagent-architecture]], [[Concepts/extraction-based-task-verification]], [[Concepts/f-beta-reward-curriculum]], [[Concepts/trajectory-recall-reward]]
- Related research: [[Research/llm-context-rot-evaluation-2026]]

## Citation

```bibtex
@techreport{bashir2026context1,
  title = {Chroma Context-1: Training a Self-Editing Search Agent},
  author = {Bashir, Hammad and Hong, Kelly and Jiang, Patrick and Shi, Zhiyi},
  year = {2026},
  month = {March},
  institution = {Chroma},
  url = {https://trychroma.com/research/context-1},
}
```
