---
title: "Open Bottlenecks Toward Full Recursive Self-Improvement"
detail: "The seven structural bottlenecks Weng identifies between today's harness-evolution loops and full RSI: weak evaluators, context/memory lifecycle, negative results, diversity collapse, reward hacking, long-term success, and the role of humans."
details: "Weng's closing list of open problems is the most actionable part of the survey for harness designers. Each bottleneck is a structural limit of current self-improvement loops, not a fixable bug. Weak and fuzzy evaluators block taste, novelty, and scientific value measurement. Context/memory lifecycle management must become core intelligence, not stay in the software layer. Negative results are rare in training data, so LLMs are bad at abandoning hypotheses. Diversity collapse in evolutionary/RL loops means the population needs explicit diversity pressure. Reward hacking is unavoidable unless the evaluator and permission control sit outside the loop. Long-term success (maintainability, ownership boundaries, migration cost) is invisible to sandbox-based RLVR. Humans must move up the abstraction stack, not be removed from the loop."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Open Bottlenecks Toward Full Recursive Self-Improvement

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Constraint
**Status:** Fundamental

---

## Overview

Weng's closing list of seven open bottlenecks is the most actionable part of the survey for harness designers. Each is a **structural limit of current self-improvement loops, not a fixable bug**. The harness community has partial responses to each; the gaps remain open research.

## Core Content

### 1. Weak and Fuzzy Evaluators

Many research claims do not have a fast and precise verifier. The same is true for many real-world tasks. Current self-improvement loops work best for tasks with **measurable, objective metrics** — similar to how RL works.

**What is hard to measure:**

- **Research taste** — problem framing, experimental design, judgment about which surprising results are worth pursuing
- **Novelty** — distinguishing real new contribution from rephrasing
- **Long-term scientific value** — which papers will still matter in 10 years

**Harness response so far:** none. The harness can route around an absent verifier, but cannot create one.

### 2. Context and Memory Lifecycle

Memory grows as AI agents become more autonomous and independent. A useful harness needs to manage context and memory to complement long-context generation limitations while maximizing long-horizon task success.

**Weng's deeper claim:** since humans maintain memory through our lifetime, **context engineering should become a core part of intelligence**, not stay in the software system layer. This is a bet that the current separation (model = weights, context = harness) is not the long-term architecture.

**Harness response so far:** ACE ([[Concepts/context-as-evolving-playbook]]), MCE ([[Concepts/bi-level-context-skill-optimization]]), file-as-memory ([[Concepts/file-system-as-agent-memory]]).

### 3. Negative Results

Researchers are incentivized to publish successful results, so literature is biased toward successes. LLMs trained on human-created data (mostly) may be bad at deciding **when to abandon a hypothesis, report a negative result, or acknowledge a failure** due to the imbalance.

> A research harness should make failed attempts **easy to preserve** — learning from failure is the best way to trim the task search space.

**Harness response so far:** file-as-memory enables this; explicit "failure archive" patterns are rare. AHE ([[Concepts/agentic-harness-engineering-ahe]]) and Self-Harness ([[Concepts/self-harness-propose-evaluate-accept]]) treat failures as first-class signal, but the harness has to be designed to surface them.

### 4. Diversity Collapse

Evolutionary and RL loops tend to exploit known high-reward patterns. We need mechanisms to prevent the population from collapsing into variants of the same solution. **Critical for open-ended research** where the best path may initially look worse under the current evaluator.

**Harness response so far:** explicit diversity pressure in DGM (inverse-children weighting), ShinkaEvolve (code-novelty rejection), Self-Harness (diverse candidate generation), MCE (history-bounded crossover).

### 5. Reward Hacking

A self-improvement loop optimizes whatever signal it is given. If the reward comes from:

- **Unit tests** → the agent may overfit to tests
- **Judge model** → it may learn reward hacking tricks specific to this judge
- **Benchmark scores** → it may exploit benchmark artifacts

**The structural answer:** the evaluator and permission control should likely sit **outside the loop** that evolves the harness, with held-out tests, trace audits, and human review at decision points that matter. AHE's read-only constraints are a concrete instance.

**How much oversight can be scaled up and automated remains an open research area.**

### 6. Long-term Success

An extrinsic loop of optimization works on rewards outside of individual rollouts that we can simulate in a training sandbox.

**Example:** coding agents have increased daily productivity in software engineering, but many optimization goals are still too short-term. An agent can often complete the task at hand, but it's less obvious how it should protect the **long-term health of a repo** collectively maintained by hundreds or thousands of engineers. Standard sandbox-based RLVR-style training rarely captures:

- Maintainability
- Ownership boundaries
- Migration cost
- Backwards compatibility
- Future debugging burden

These are **external to the rollout** and visible only in a multi-agent, multi-year view. Current harnesses have no signal here.

### 7. The Role of Humans

Humans should **move up the stack, not be removed from the loop**. Humans should provide oversight at the right time, at the right abstraction level; system design should consider when and how to set up such touch points.

Many of the above challenges need human feedback and steering. Weng's closing line:

> "We are building the technology for better future of humanity, not other way around."

## Companion Pattern: The Six Recurring Failure Modes

Trehan & Chopra (2026) ran four autonomous research attempts with minimal scaffolding and observed **six recurring failure modes**:

1. **Bias toward training-data defaults** — old libraries, stale commands, standard formats, assumptions not grounded in the actual repository or dataset
2. **Implementation drift under execution pressure** — when implementation becomes complex, the model moves toward a common simpler solution rather than the proposed method
3. **Memory and context degradation** — long-horizon projects lose critical details unless logs are written as persistent artifacts
4. **Over-optimism** — the model declares success despite noisy or failed experiments (Bubeck et al. 2025 call this "p-hacking and eureka-ing"; the model introduces "numerical duct tape" and declares victory when signals are still noise)
5. **Insufficient domain intelligence** — the model lacks tacit craft knowledge (predicting implementation complexity, judging whether an experimental result is plausible, knowing which baselines matter)
6. **Weak scientific taste** — experiments may be executable but fail to answer the right question

These six failure modes map closely onto the seven bottlenecks above — failure modes 1, 4, 5, 6 are instances of bottleneck 1 (weak evaluators); 3 is bottleneck 2 (context/memory lifecycle); 2 is a meta-bottleneck about execution discipline.

## Key Insights

1. **Each bottleneck is structural.** None has a one-line fix; each is a research direction in its own right.
2. **Some bottlenecks are "outside the harness"** — the harness can route around them but not solve them. Weak evaluators and long-term success are the clearest cases.
3. **Human-in-the-loop is not optional** — at least at the decision points that matter. The question is where and how often, not whether.
4. **Negative results are first-class signal.** A harness that hides failures is a harness that cannot improve.

## Related Concepts

- [[Concepts/reward-hacking-rsi]] — bottleneck 5 in detail
- [[Concepts/diversity-collapse-rsi]] — bottleneck 4 in detail
- [[Concepts/weak-evaluator-rsi]] — bottleneck 1 in detail
- [[Concepts/harness-as-runtime-os-analog]] — the OS analogy; the evaluator must sit outside the kernel
- [[Concepts/agentic-harness-engineering-ahe]] — concrete response to bottlenecks 4 and 5
- [[Concepts/self-harness-propose-evaluate-accept]] — concrete response to bottleneck 3

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Cited: Trehan & Chopra, "Why LLMs Aren't Scientists Yet," arXiv:2601.03315, 2026; Bubeck et al., "Early science acceleration experiments with GPT-5," arXiv:2511.16072, 2025.
