---
title: "Self-Harness paper"

details: "When run on MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5 on Terminal-Bench-2, Self-Harness learned model-specific harness instructions that target different weaknesses of different base models and improved held-out pass rates. Weng's concern: if a program is allowed to edit the OS system, abstraction boundaries are broken — permission control and security layers must live outside this loop."
tags:
  - entities
  - harness
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2606.09498
---

# Self-Harness paper

**Source:** Zhang et al., "Self-Harness: Harnesses That Improve Themselves," arXiv:2606.09498, 2026.

## Overview

LLM agents improve their own harness via a **propose-evaluate-accept loop**. Distinct from DGM (free edits) and Meta-Harness (no validation) by being **bounded**: edits target verified failure patterns and every candidate must pass held-in and held-out regression tests before merge.

## Three Stages

1. **Weakness mining** — cluster failures into verifier-grounded failure patterns
2. **Bounded harness proposal** — edits to editable surfaces with regression-safe context
3. **Proposal validation** — held-in + held-out regression tests before accept

## Result

When run on `MiniMax M2.5`, `Qwen3.5-35B-A3B`, and `GLM-5` on Terminal-Bench-2, Self-Harness learned **model-specific harness instructions** that target different weaknesses of different base models and improved held-out pass rates.

## Weng's Concern

> If a program is allowed to edit the OS system, abstraction boundaries are broken. The editable surface needs to be properly designed; permission control and security layers need to live outside this loop.

## Related

- [[Concepts/self-harness-propose-evaluate-accept]] — the concept
- [[Concepts/darwin-godel-machine]] — the unbounded sibling
- [[Concepts/agentic-harness-engineering-ahe]] — concurrent work with stricter observability
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
