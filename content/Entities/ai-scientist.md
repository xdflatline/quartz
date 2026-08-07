---
title: "AI Scientist"

details: "Foundational reference in [[Raw/lilianweng-harness-engineering-2026-07-04]] for workflow-level harness design. The pipeline demonstrates that an expert-designed harness can coordinate a large portion of an auto-research loop, but the Nature publication also documents the gap: a system can write a plausible manuscript while still having fabricated citations, implementation drift, or weak experimental results. Weng's critique: paper production is not identical to scientific discovery."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://www.nature.com/articles/s41586-026-00001-1
---

# AI Scientist

**Source:** Lu et al., "Towards end-to-end automation of AI research," Nature 651:914–919, 2026.

## Overview

A pipeline that **proposes research ideas → writes code → runs experiments → analyzes results → writes a manuscript → performs peer review**. One of the first end-to-end systems to attempt the full research loop. The Nature publication is the canonical reference for the "expert-designed auto-research harness" claim.

## The Pipeline

1. **Idea generation** — propose candidate research questions
2. **Code writing** — implement the proposed method
3. **Experimentation** — run the experiments, gather results
4. **Analysis** — interpret the results, generate plots
5. **Manuscript writing** — produce a paper draft
6. **Peer review** — score the paper against a reviewer rubric

![AI Scientist pipeline](assets/lilianweng-harness-2026-07-04/ai-scientist.png)
*AI Scientist pipeline. (Image source: Lu et al. 2026)*

## Weng's Critique

> Paper production is not identical to scientific discovery. A system can write a plausible manuscript while still having fabricated citations, implementation drift, or weak experimental results.

The AI Scientist line of work is a strong demonstration that an expert-designed harness can coordinate a large portion of auto-research loop. But it does NOT demonstrate that the system does science — it demonstrates that it produces papers.

## Related

- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
- [[Entities/scientistone]] — follow-up work that adds chain-of-evidence verification
- [[Concepts/open-rsi-bottlenecks]] — the structural challenges AI Scientist does not solve
- [[Entities/autodata]] — the data-generation sibling
