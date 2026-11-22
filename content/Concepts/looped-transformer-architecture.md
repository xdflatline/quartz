---
title: "Looped transformer architecture (weight-shared middle blocks)"
details: "Architecture pattern that reuses the same middle-layer weights for several passes per token, raising serial depth without adding parameters. Inkling 2 Mini runs four blocks of six layers with the middle two blocks executed three times, giving 48 layer applications per token from 24 stored layers; attention residuals plus a learned, initially-closed gate pass a message between passes so looping can be introduced mid-training without destabilising it."
tags:
  - concept
  - llm
  - architecture-pattern
  - local-llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Looped transformer architecture (weight-shared middle blocks)

**Category:** Model Architecture
**Status:** Shipped in Inkling 2 Mini and TML-d24-varloop-research (2026-11)

## Overview

A standard transformer applies each layer once per token, so the amount of sequential computation available before the model must emit a token is fixed by its depth. A **looped transformer** runs a subset of its layers more than once per token, reusing the same weights. Serial depth goes up; parameter count does not.

Inkling 2 Mini's layout:

- **24 layers**, split into four blocks of six.
- **Blocks 2 and 3 run three times** per token; the prelude (block 1) and final block run once.
- **48 layer applications per token** from 24 stored layers.

## Why the middle layers

The design rests on a division of labour the authors observed empirically: middle layers carry abstract reasoning, while the first and last layers spend capacity translating between token embeddings and internal representations. Looping the middle should therefore buy more reasoning per additional pass.

Their measurement supports it. At training step 2,000, the no-loop baseline needed an estimated **1.51–1.91× the compute** to match the middle-loop loss, versus **1.24–1.36×** to match a last-12-layers loop. Looping the middle twelve layers produced larger accuracy gains than looping the last twelve on **27 of 28 evaluations**.

## Attention residuals and the inter-pass message

Naive looping has a stability problem: each pass would see the same input and could collapse into repeating computation. The design borrows two mechanisms:

- **Attention residuals** ([Kimi Team, 2026](https://arxiv.org/abs/2603.15031)) — instead of summing every layer's output into one running state, each layer reads the outputs of earlier blocks and learns its own mix. Every pass starts from the prelude's output rather than from the previous pass's residual stream.
- **A message between passes** — the second and third passes also read the middle blocks' outputs from the previous pass. Each previous pass's message is merged through a **learned gate** alongside the prelude output; the gate starts fully closed, so the first training steps behave exactly like a non-looping model, and opens as training proceeds.

That gate is what makes looping something you can turn on **during** training rather than only from initialization.

## Cost shape

Looping moves cost from parameters to compute:

- A non-looping sibling cost **7.5% less compute to train**, but needed **140% more inference compute** to match the looped model's loss on 512k-token agentic traces.
- The looping is repeated weight reads, so decode bandwidth scales with passes — the reported theoretical decode ceiling accounts for repeated reads across loops.
- Memory footprint is unchanged by looping; only the stored 24 layers need to fit.

This is why the pattern pairs naturally with local deployment: the deployable object stays small while the reasoning depth grows ([[Concepts/local-agent-model-economics]]).

## Capacity is not depth

The authors are explicit that looping adds **reasoning steps, not knowledge**. Factuality on AA-Omniscience is in line with other models of the same parameter count, and closed-book QA is nearly invariant to loop passes, while multi-hop reasoning, long-context retrieval and long-horizon agentic tasks improve. Knowledge remains a function of total parameters.

## Related Concepts

- [[Concepts/latent-reasoning-and-cot-monitorability]] — the oversight consequence of more compute per token
- [[Concepts/expert-pruning-and-healing]] — how the model got small enough to deploy
- [[Concepts/native-low-precision-training]] — the precision side of the same efficiency story
- [[Concepts/local-agent-model-economics]] — why a looped small model is locally attractive
- [[Concepts/chain-of-thought-prompting]] — the explicit-reasoning alternative that looping partly substitutes for

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Research: [[Research/looped-transformers-and-local-frontier]]
- Universal Transformers (Dehghani et al., 2018): https://arxiv.org/abs/1807.03819
- Attention Residuals (Kimi Team, 2026): https://arxiv.org/abs/2603.15031
