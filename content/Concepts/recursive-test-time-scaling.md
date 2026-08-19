---
title: "Recursive Test-Time Scaling (Self-as-Worker Orchestration)"
details: "Test-time scaling technique introduced in Sakana AI's Conductor (Nielsen et al., arXiv:2512.04388, 2026): the orchestrator is allowed to call *itself* as one of the worker agents. After producing a coordination strategy and observing the response, the orchestrator decides whether to accept the result or design a new strategy that revises it. Unlike fixed best-of-N (fixed rounds) or single-model self-refine, the orchestrator itself learns when to stop iterating — a new form of dynamic, online test-time scaling."
tags: [concepts, llm, agent, orchestration, inference]
sources:
  - Papers/conductor-rl-orchestrator.md
  - Raw/conductor-rl-orchestrator-arxiv.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# Recursive Test-Time Scaling (Self-as-Worker Orchestration)

**Source:** [[Papers/conductor-rl-orchestrator]] · [[Raw/conductor-rl-orchestrator-arxiv]]
**Category:** Inference Pattern / Test-Time Scaling
**Status:** Production-validated

---

## Overview

Recursive test-time scaling extends the [[Concepts/rl-conductor-trained-orchestrator|Conductor pattern]] by adding the orchestrator itself to the worker pool. After the first round, the orchestrator sees its own response and decides whether to accept the result, allocate additional agents to verify or refine, or design an entirely new coordination strategy.

Unlike prior test-time scaling techniques (best-of-N with fixed rounds, self-refine within a single model, majority voting), recursive Conductor is **dynamic and adaptive** — the orchestrator itself decides how much compute to spend, and *learns* a sensible stopping policy during training.

## How It Works

### The recursive prompt

When recursion is enabled, the orchestrator is prompted (Appendix E, Figure 14 in the Raw paper) with:

1. The current state — its previous coordination strategy and the worker's final response.
2. The decision — accept the response, or design a new coordination strategy that revises it.

If the orchestrator decides to iterate, it outputs a new set of `subtasks[]`, `model_id[]`, `access_list[]` (see [[Concepts/coordination-topology-in-natural-language]]) — now with access to the previous round's worker responses. The new strategy may:

- Allocate additional agents to verify the previous answer.
- Add a format-checker step.
- Try a different decomposition.
- Or — if the orchestrator judges the original answer sound — pass through without modification.

### What the Conductor learns

The recursive Conductor learns three things that prior test-time scaling techniques do not:

1. **Adaptive stopping** — on MMLU (simpler tasks) the orchestrator typically accepts the first round; on LiveCodeBench (harder tasks) it iterates 2-3 times. The stopping policy is emergent, not hard-coded.
2. **Worker redistribution** — Figure 10 shows that recursive rounds shift worker selection toward Claude and Gemini for coding tasks, away from Qwen. The orchestrator learns which workers to trust on which subtasks.
3. **Verification strategies** — recursive rounds often add a verifier or aggregator step that wasn't in the initial strategy.

## Comparison to Prior Test-Time Scaling

| Technique | Who decides rounds? | Adaptive? | Multi-model? |
|-----------|---------------------|-----------|--------------|
| Best-of-N | User (fixed N) | No | Optional |
| Self-refine | Single model | Implicit (saturation heuristic) | No |
| Majority vote | User (fixed N) | No | Yes |
| Debate | User (fixed rounds) | No | Yes |
| **Recursive Conductor** | **The orchestrator itself** | **Yes (learned)** | **Yes** |

The key novelty is **adaptive rounds decided by the orchestrator** — the user supplies a compute budget and the Conductor spends it where it judges additional rounds will help.

## Empirical Gains

Table 2 of the Raw paper reports that test-time recursion delivers:

- Marginal gains on simpler tasks (MMLU, MATH-500) where one round is usually enough.
- Significant gains on the hardest tasks (LiveCodeBench, BigCodeBench), where 2-3 rounds are typical.

## When to Use This Pattern

- The base orchestration problem has a verifiable reward (so the orchestrator can learn when iterating helps).
- You can afford multiple rounds of inference on the orchestrator *itself* (the orchestrator becomes the bottleneck).
- The task difficulty varies significantly per query — simple queries should not pay for recursion, hard ones should.

## When NOT to Use

- Latency-critical settings — recursion is serial.
- Tasks where the orchestrator cannot observe a useful signal for whether to iterate (e.g. open-ended generation without a verifier).
- The orchestrator is much cheaper than the workers — then running the orchestrator multiple times is fine, but you lose the benefit of having a learned stopping policy.

## Related Concepts

- [[Concepts/rl-conductor-trained-orchestrator]] — the base pattern that recursion extends
- [[Concepts/coordination-topology-in-natural-language]] — the output format that makes recursive strategies verifiable
- [[Concepts/agent-self-improvement]] — recursive revision as a form of self-improvement

## References

- Paper: [[Papers/conductor-rl-orchestrator]]
- Raw extraction: [[Raw/conductor-rl-orchestrator-arxiv]]
- Original: https://arxiv.org/html/2512.04388v5 (Section 3.2, Appendix D)
