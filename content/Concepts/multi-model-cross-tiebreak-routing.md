---
title: "Multi-Model Cross-Tiebreak Routing"
details: "Routing pattern in which a job is passed through several specialised models and a stronger model is used as the final arbiter of contested decisions, most notably scope. Because each model arrives at the decision with a different context load and a different bias, the tiebreak is not a re-run of the same judgement but an independent second opinion — which is also a lever against the convergence problem where agents keep finding one more thing to do."
tags:
  - concept
  - llm
  - orchestration
  - agent
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Multi-Model Cross-Tiebreak Routing

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Routing / Decision Architecture
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

Multi-model routing is usually justified on cost: pick the cheapest model that can do the job. This pattern justifies it on **decision quality** — and specifically uses the diversity between models as a corrective against a known pathology: the convergence problem, where an agent that has just built something keeps finding one more thing to build.

## The convergence problem

Agents love to find one more thing to do. Build a thing, review it, discover a gap, fix it, discover another gap. Eventually the work is unbounded. The common fix is prompt tuning or effort tuning — "if you think it's doing too much, drop the effort level." That does not work, because the model's willingness to keep going is a *thought in the trajectory*: if there is a token sequence in there that decided to look for another problem, no effort setting removes it. Only genuinely editing the conversation would, and no regular user does that.

## The tiebreak mechanism

Because a single trajectory cannot be talked out of over-reach, the decision is re-made by a *different model with a different context load*:

- The implementer's model has the whole burden — it has implemented everything, its context is blown past the effective threshold, and it is operating in its weakened regime.
- The tiebreaker sees only the **agent action plan** (AAP) — the small artifact that states what is in scope. It has far fewer constraints to hold, so it judges scope more effectively.

The stated result: the second model says *"nope, that's not in scope. That's not what the agent action plan says."* And in general, a job is seen by **at least eight different models** before reaching the user, each specialised for the task it handles.

This is the point where the routing pattern diverges from plain model selection: the value is not that model B is better than model A in general, but that **model B is not carrying model A's history**.

## Tag-ranked ladders

Model choice is driven by internal evals and benchmarks, not by vendor claims. When a model launches, it is run internally, benchmarked in the platform, and scored; the results are distilled into **tags**, and the tags are **ranked** into ladders.

- Ladder axis: task domain (front end, back end, decision making, and so on).
- Within an axis, a complexity band selects the rung: "front end, very complex, choose this model. Front end, low complexity, choose this model. It's good enough."
- Vendor benchmark claims and web search are explicitly not used as the basis — the internal eval results are.

The optimisation target is stated as quality and speed jointly: *"you need to choose the fastest model that gives you the best quality."*

## Agent-chosen routing

The routing decision is itself delegated: the agent chooses the LLM for the next agent, chooses the system prompt, and chooses the tools. Per [[Entities/sid-pardeshi]]: "This is literally agent designed by agents." Routing is dynamic at runtime, switching on capacity, on measured intelligence, and on task specificity.

## Related Concepts

- [[Concepts/context-wall-large-codebase-scale]] — the reason a fresh model is a better tiebreaker than a loaded one
- [[Concepts/bundled-model-router]]
- [[Concepts/llm-routing-pool]]
- [[Concepts/model-selection-llm]]
- [[Concepts/language-routing-in-decision-models]]
- [[Concepts/agent-self-improvement]] — the routing engine's improving as its deciding agents improve
- [[Concepts/calibration-for-decision-models]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
