---
title: "KernelBench"
detail: "Ouyang et al., 2025. 250 PyTorch tasks to evaluate whether LLMs can write fast and correct GPU kernels. Metric: fast_p = the percentage of generated kernels that are correct and faster than baseline."
details: "The dual metric (correctness AND performance) catches overfitting to test cases. A 'correct but slow' kernel doesn't pass. The benchmark correlates with downstream RL/serving efficiency."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2502.10517
---

# KernelBench

**Source:** Ouyang et al., "KernelBench: Can LLMs Write Efficient GPU Kernels?" arXiv:2502.10517, 2025.

## Overview

250 PyTorch tasks to evaluate whether LLMs can write **fast and correct** GPU kernels. The dual metric distinguishes kernels that merely work from kernels that work AND beat the baseline.

## The Metric

$$
\text{fast}_p = \frac{|\{k : k \text{ is correct AND } k \text{ is faster than baseline}\}|}{|\text{total}|}
$$

This catches overfitting to test cases: a "correct but slow" kernel does not pass.

## Scale

- 250 PyTorch tasks
- Covers a range of kernel families (element-wise, reductions, matrix ops, attention, etc.)

## Why It Matters

A KernelBench result correlates with downstream RL/serving efficiency — agents that score well here are likely to produce kernels that improve real workloads. AlphaEvolve, ShinkaEvolve, and other evolutionary-search methods use KernelBench (or similar) as a fitness signal.

## Related

- [[Concepts/ai-research-engineering-benchmarks]] — the reference suite
- [[Entities/alphaevolve]] — the method that uses similar kernels as fitness
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
