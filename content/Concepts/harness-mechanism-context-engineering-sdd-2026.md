---
title: "Harness Mechanism 1 — Context Engineering (SDD)"
details: "H1 of the Diaz et al. (2026) methodological harness. Context engineering governs what an agent knows within a session: the curated set of specifications, prior decisions, skills, and tool affordances injected into the agent's working context. It is the boundary-spanning mechanism — it lives in both the technical harness (per-agent session) and the methodological harness (per-team conventions). Worked example: the agent working on the e-commerce refund feature receives the relevant feature specification, the persistent-knowledge entry from a prior pricing decision, the executable spec test harness, and the autonomy-calibration record."
tags: [concept, software-engineering, agentic, harness, context-engineering]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 1 — Context Engineering (SDD)

H1 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to curating, for each agent invocation, **what the agent knows within the session**: which specifications are loaded, which prior decisions are referenced, which skills are available, which tools are reachable.

## Worked example (e-commerce refund)

The agent working on a refund operation receives:

- the active feature specification for the refund flow;
- the persistent-knowledge entry recording the team's earlier decision that refunds must remain idempotent under network retries;
- the executable-spec test harness;
- the autonomy-calibration record stating which sub-tasks the agent may complete without human consultation.

Without context engineering, the agent either receives too much (cost, distraction, stale guidance) or too little (it re-derives prior decisions or violates standing norms).

## Boundary role

Context engineering is the mechanism that bridges the **technical harness** (which assembles the per-agent prompt) and the **methodological harness** (which defines what the team considers in-scope). It is the only one of the eight mechanisms that lives in both. The other seven are methodological — they are conventions and processes the team adopts, not per-session prompt assembly.

## Related Concepts

- [[Concepts/spec-driven-development-sdd-2026]] — the discipline context engineering operationalizes.
- [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026]] — the persistent-knowledge entries context engineering consumes.
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — the autonomy-calibration record context engineering surfaces to the agent.