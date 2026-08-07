---
title: "Meta-Harness paper"

details: "Meta-Harness is the canonical 'harness-for-harnesses' method. The proposer reads execution history via grep/cat rather than shoveling everything into a single prompt context; the proposed harness is a dictionary in the file system containing its own source code, scores, rollout trajectories, and state updates. On TerminalBench-2, the search is initialized from Terminus-KIRA and Terminus-2 (two strong harnesses) and improves from there."
tags:
  - entities
  - harness
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2603.28052
---

# Meta-Harness paper

**Source:** Lee et al., "Meta-Harness: End-to-End Optimization of Model Harnesses," arXiv:2603.28052, 2026.

## Overview

A harness for optimizing harnesses. The optimized object is **the code that determines and optimizes what information should be stored, retrieved, and presented to the model**. The proposer is itself a coding agent; the output is a Pareto frontier of harness candidates.

## Key Mechanisms

- The proposer reads execution history via `grep` and `cat` rather than paste into context
- Each proposed harness is a dictionary in the file system with source code, scores, trajectories, state updates
- The loop iteratively creates new harnesses; only qualified ones are kept
- Output is a Pareto frontier — not a single winner

## Result

On TerminalBench-2, the search is initialized from Terminus-KIRA and Terminus-2 (two strong human-designed harnesses) and improves from there. This is the evidence that the harness design space has room above strong human design.

## Related

- [[Concepts/meta-harness-outer-loop]] — the concept
- [[Entities/terminus-2]], [[Entities/terminus-kira]] — the starting harnesses
- [[Concepts/darwin-godel-machine]] — concurrent related work
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
