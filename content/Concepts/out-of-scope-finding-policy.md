---
title: "Out-of-Scope Finding Policy"
details: "Policy for what an agent should do when a review or test stage uncovers a real problem that lies outside the current job's scope: document the finding in the project's completion record rather than expanding the change to fix it. This keeps the delivered surface area stable, preserves scope discipline, and converts the discovery into a durable artifact for a human to triage."
tags:
  - concept
  - agent
  - software-engineering
  - orchestration
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Out-of-Scope Finding Policy

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Policy / Scope Discipline
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

An agent that finds a real problem while doing bounded work faces a choice: fix it (and expand the change), or ignore it (and lose the finding). Both are bad. Fixing it inflates the surface area, the review burden, and the risk of the very job that was requested. Ignoring it means the next agent hits the same wall, and the discovery is lost.

The policy: **document it, don't fix it** — but record the documentation as a first-class artifact.

## The rule

When a stage (security review, adversarial testing, code review) surfaces a genuine issue that falls outside the job's agreed scope:

- **Out of scope → document.** The finding is recorded in the project's guide alongside what was done and what was deliberately not done.
- **In scope → adjust.** If the agent judges the finding is actually within the agreed scope of the job, it goes ahead and fixes it as part of the same job.

The judgement call is what makes the policy workable rather than a blanket "never fix anything."

## Why documentation is the deliverable

A project guide that records **all the work done and all the work that could not or was decided not to be done** serves three purposes:

1. **Human triage.** The reviewer sees the discovery and decides whether to schedule it.
2. **Completion accounting.** If the finding was in fact an in-scope item that was missed, the completion percentage reflects that — the finding is not free.
3. **Durability.** The finding becomes part of the codebase's knowledge rather than a transcript that gets compacted away.

## The motivating tension

The interviewer names the tension exactly: as you do work you often uncover future work. "I don't want to explode my scope. I don't want to explode my surface area. But I found this. We should really fix this."

The policy resolves it by separating *finding* from *fixing*, and giving the finding an artifact so it is not lost. The next step — self-filing tickets and self-scheduling follow-up work — is stated as in progress, not yet shipped.

## Related Concepts

- [[Concepts/pre-planned-checkpointed-review-stages]]
- [[Concepts/production-is-truth]]
- [[Concepts/post-incident-review-culture]]
- [[Concepts/explicit-instruction-over-implicit-inference]]
- [[Concepts/agent-self-improvement]]
- [[Concepts/slice-folder-spec-progress-proof]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
