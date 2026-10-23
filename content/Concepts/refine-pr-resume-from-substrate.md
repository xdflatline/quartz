---
title: "Refine PR: Resume from Substrate, Not Transcript"
details: "Correction pattern in which human feedback on a generated pull request is applied by resuming the underlying work substrate — the codebase knowledge graph and the SCM — rather than by re-priming a chat transcript. Because the substrate preserves both what was done and what was intended, a refinement cycle preserves history and the outcome is judged only on its final state, not on the wasted intermediate work."
tags:
  - concept
  - coding-agent
  - agent
  - software-engineering
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Refine PR: Resume from Substrate, Not Transcript

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Correction / Iteration Pattern
**Status:** Production-validated (per [[Entities/blitzy]]; shipped as the "Refine PR" workflow)

---

## Overview

An agent-generated pull request is almost never right the first time. The human reviewer finds gaps, and the system must apply that feedback. The naive implementation appends the feedback to the conversation and asks the agent to fix it — which works only while the conversation still holds the work.

This pattern replaces the transcript with the **substrate**. The "Refine PR" workflow resumes the process *including the graph*, preserving history from both the graph and the SCM, and addressing the reviewer's feedback against that state.

The contrast with transcript-resume is the whole point: a long session has already blown past the effective context window, so re-priming it means the correction is applied by a model operating in its weakened regime, against a partially-lost history. See [[Concepts/context-wall-large-codebase-scale]].

## Two properties that follow from the substrate

**1. History is preserved.** The graph was updated on the fly as the work proceeded, corresponding to the branch. Resuming against it means the correction knows what was done, why, and what the plan said — the plan being the small artifact that survives, and the graph being the one that carries the bulk.

**2. Outcome is judged on final state, not effort.** The pricing model makes this structural rather than aspirational: Blitzy bills on the lines of code in the *resulting* pull request. If feedback causes the final PR to shrink, the customer is charged for the smaller result. "Everything that you give us feedback on is a mistake."

This is a design choice with teeth. It removes the incentive to "let it rip" and aligns vendor and customer toward *"let's write the right code, not all the possible code."* The generalisation: **price on the accepted artifact, not on the generation cost**, and both sides stop arguing about token economics.

## The review surface that makes refinement cheap

Refinement is only affordable if the reviewer can find the gaps quickly. The paired artifact is a **PR review experience** that walks the reviewer through the changes but foregrounds the key ones — the stated goal being that a reviewer inspects ~50 files rather than 500, on the reasoning that 100 files of green unit tests written in a known style do not need individual review.

This is the counterpart of the out-of-scope finding policy: findings that fall outside the job's scope are documented rather than fixed, and the project's guide records both what was done and what was deliberately not done.

## Related Concepts

- [[Concepts/context-wall-large-codebase-scale]]
- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/graph-anchored-agent-swarm-coordination]] — the two-tracker reconciliation that makes resume possible
- [[Concepts/builder-reviewer-task-granularity]]
- [[Concepts/idempotency-for-ai-agents]]
- [[Concepts/production-is-truth]]
- [[Concepts/post-incident-review-culture]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
