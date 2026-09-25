---
title: "Graphwalks"
details: "Graphwalks (OpenAI, 2025; HuggingFace dataset) — long-context benchmark for graph traversal: the model is given a directed graph of hexadecimal hashes and asked to perform breadth-first search starting from a random node. Input length scales with the graph size, which makes it hard to disentangle input-length cost from task-difficulty cost."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://huggingface.co/datasets/openai/graphwalks
---

# Graphwalks

**Source:** OpenAI (2025). HuggingFace dataset: <https://huggingface.co/datasets/openai/graphwalks>

## Overview

**Graphwalks** is a long-context benchmark where the model must perform **breadth-first search (BFS)** on a directed graph. The graph is presented as a list of edges encoded with hexadecimal hash node identifiers, and the model is asked to walk the graph from a given start node and report the visited nodes in BFS order.

## Why it is hard to use for context rot analysis

Input length scales with graph size: a larger graph means more tokens. But a larger graph also means **a harder BFS** (more nodes, more edges to traverse, more state to track). The two variables are confounded.

Chroma cites Graphwalks in [[Raw/chroma-context-rot-2026-07]] as a cautionary example: any benchmark where input length scales with task complexity cannot cleanly attribute degradation to input length alone. Chroma's own experiments specifically avoid this confound (e.g. repeated-words task: input length scales but task complexity does not).

## Relation to other benchmarks

Graphwalks is one of the family of "task scales with context" benchmarks that includes:

- [[Entities/michelangelo|Michelangelo]] / Latent List (similar issue, mitigated by varying filler type)
- [[Entities/mrcr|MRCR]] (less confounded: fixed i-th-retrieval task across context lengths)
- [[Entities/longmemeval|LongMemEval]] (focused-vs-full design isolates retrieval cost)

For studying context rot, the *less confounded* of these are the more useful benchmarks.

## Related Pages

- Raw: [[Raw/chroma-context-rot-2026-07]] — the study that discusses the confound
- Concept: [[Concepts/repeated-words-task]] — the most-controlled Chroma task