---
title: "Self-Harness Propose-Evaluate-Accept Loop"

details: "Self-Harness is a closed loop with three stages. Weakness mining produces a failure record of rich information: terminal verifier-level cause, causal status of the relevant agent behavior, and abstract agent mechanism exposed by the trace. Harness proposal gives the proposer a bounded context: (1) editable surfaces of the current harness, (2) verifier-grounded failure patterns, (3) records of passing behaviors to preserve, (4) summaries of previously attempted edits. Proposal validation evaluates edits on held-in (weakness resolved?) and held-out (no regressions?) splits; only edits that pass both are merged. When run on MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5 on Terminal-Bench-2, Self-Harness learned model-specific harness instructions that target different weaknesses of different base models."
tags:
  - concepts
  - harness
  - agent
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Self-Harness Propose-Evaluate-Accept Loop

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Learning Mechanism
**Status:** Experimental (Terminal-Bench-2 evidence on three base models)

---

## Overview

**Self-Harness (Zhang et al. 2026)** relies on LLM agents to improve their own harness via a **propose-evaluate-accept loop**. Unlike DGM (which edits harness code freely) or Meta-Harness (which searches the full design space), Self-Harness is **bounded**: edits target verified failure patterns, and every candidate must pass held-in and held-out regression tests before merge.

## Core Content

### The Loop

![Self-Harness loop](assets/lilianweng-harness-engineering-2026-07-04/self-harness.png)
*Self-Harness: weakness mining, bounded harness proposal, validation. (Image source: Zhang et al. 2026)*

### Stage 1: Weakness Mining

- The current harness $h_t$ evaluates tasks; execution traces are collected
- Cluster failures into **verifier-grounded failure patterns**
- A failure record must include:
  - **Terminal verifier-level cause** (timeout, missing artifact, assertion failure, etc.)
  - **Causal status** of the relevant agent behavior (which step is responsible)
  - **Abstract agent mechanism** exposed by the trace (what the agent was *trying* to do)
- Two runs can share the same verifier outcome (e.g., both timeouts) while having different causal mechanisms — without the rich failure record, the wrong fix gets applied

### Stage 2: Bounded Harness Proposal

- The same model is invoked under $h_t$ as a proposer
- The model receives a **bounded proposal context**:
  1. The **editable surfaces** of the current harness (what may be changed)
  2. The **verifier-grounded failure patterns** from stage 1
  3. **Records of passing behaviors** that should be preserved
  4. **Summaries of previously attempted edits** (so the proposer doesn't repeat them)
- Edits prefer:
  - **Recurrent** error patterns (not one-off)
  - **Addressable** patterns (not task-specific difficulty)
  - **Narrow** changes (one concern per edit)
- Candidates should be **distinct and diverse** — proposer is asked to produce several

### Stage 3: Proposal Validation

- Candidate edits are evaluated by regression tests on:
  - **Held-in** $D_\text{in}$ — does the weakness get resolved?
  - **Held-out** $D_\text{out}$ — were other unknown issues introduced?
- Accepted only if **no regression on both** splits
- Accepted candidates are merged to update the harness to $h_{t+1}$
- Rejected candidates are logged without changing the active harness

### Results

When run on `MiniMax M2.5`, `Qwen3.5-35B-A3B`, and `GLM-5` on Terminal-Bench-2, Self-Harness learned **model-specific harness instructions** that target different weaknesses of different base models and improved held-out pass rates. The model-specific nature of the edits is the interesting result: the same loop produces different harnesses for different base models, because the failure patterns are different.

### The Author's Concern

Weng flags a structural risk: **if a program is allowed to edit the OS system, abstraction boundaries are broken**. Self-Harness mitigates this by:

- Bounded editable surfaces (the proposer can only change what the harness declares editable)
- Held-out regression tests (every edit is falsifiable)
- Logging rejected candidates (so failed proposals are inspectable)

But the permission control and security layers still need to live **outside** this loop. The risk is that the proposer learns to game the held-out set, the verifier, or the rollback mechanism.

## Key Insights

1. **Bounded edits beat free edits.** DGM and Self-Harness are the two ends of a spectrum: DGM edits anything, Self-Harness only edits what is declared editable and survives regression tests. The bounded approach is safer; the free approach is more powerful.
2. **Failure record richness matters.** "Timeout" is not enough. Without the abstract mechanism, two failures look identical and get the same fix.
3. **Model-specific harnesses emerge naturally.** The same loop applied to three different base models produced three different harnesses. The harness is a function of the model it wraps.
4. **The held-out split is the safety net.** It catches the edits that overfit to the failure-mining distribution.

## Related Concepts

- [[Concepts/darwin-godel-machine]] — the more aggressive (less bounded) sibling
- [[Concepts/agentic-harness-engineering-ahe]] — concurrent work with a stricter observability discipline
- [[Concepts/meta-harness-outer-loop]] — the harness-for-harnesses variant
- [[Concepts/harness-updating-vs-harness-benefit-disentanglement]] — the foundational result that a 9B model can write harness edits as well as Opus
- [[Concepts/agent-self-improvement]] — the broader paradigm
- [[Concepts/reward-hacking-rsi]] — the failure mode the bounded edits help prevent

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Paper: Zhang et al., "Self-Harness: Harnesses That Improve Themselves," arXiv:2606.09498, 2026.
- Related Entity: [[Entities/self-harness-paper]]
