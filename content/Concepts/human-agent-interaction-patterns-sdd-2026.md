---
title: "Human–Agent Interaction Patterns under SDD"
details: "The five recurring interaction patterns through which humans and agents collaborate under Spec-Driven Development, as characterized by Diaz et al. (arXiv:2609.00252, 2026): specification authoring (human writes the contract), specification interpretation (agent reads it), specification validation (human audits evidence against it), specification enrichment (team updates it as new cases accumulate), and specification reuse (next agent or team member reads it). Each pattern operates on the shared specification substrate, forming a continuous improvement cycle. Worked example: the refund flow goes through all five stages — authored as a feature spec, interpreted by the implementing agent, validated via executable specs, enriched by the persistent-knowledge entry, reused by the next agent working on dispute resolution."
tags: [concept, software-engineering, agentic, harness, collaboration]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Human–Agent Interaction Patterns under SDD

The five recurring interaction patterns identified by [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]] as the recurring forms human–agent collaboration takes under [[Concepts/spec-driven-development-sdd-2026|SDD]].

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 7]] summarizes them. Rather than isolated activities, they form a continuous collaboration cycle centered on the shared specification substrate.

## The five patterns

### 1. Specification authoring

The human writes (or revises) a specification — system, feature, normative, or skill. The act of authoring is itself an act of governance: the author is committing to a contract that downstream agents and reviewers will reference.

### 2. Specification interpretation

The agent reads the specification, asks clarification consultations on clauses it cannot resolve, and produces candidate output against it. Under SDD this is a typed operation: every sub-task references the clauses it implements or amends.

### 3. Specification validation

The human (or an automated check) audits the agent's evidence against the specification. Under [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026|evidence-backed acceptance]], this means reviewing test outputs and contract checks, not re-deriving correctness from the diff.

### 4. Specification enrichment

The team (human or automated) updates the specification as new cases accumulate: edge cases discovered, normative clarifications added, dead clauses retired. Under [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026|persistent shared knowledge]], enrichment is recorded with attribution and evidence.

### 5. Specification reuse

The next agent (or the next team member, or the future you) reads the specification and the persistent-knowledge entries and begins where the last one left off. This is what makes the work belong to a team rather than to an individual.

## N-to-N topology

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 8]] shows the topology these patterns enable: multiple humans collaborate with multiple agents through the specification substrate, with persistent shared knowledge as the medium that lets them act as one team rather than as disconnected sessions. Three operational implications follow:

- **Cross-human handover**: a consultation raised by one agent may be resolved by a different human than the one who authored the brief.
- **Cross-agent handover**: an agent may invoke a specialist agent for a sub-task.
- **Hybrid composition**: specialist functions may be filled by humans, agents, or pairs — team composition becomes a design variable.

## Worked example (e-commerce refund)

The refund flow traverses all five patterns:

1. **Authoring**: a developer writes the feature specification for the refund flow.
2. **Interpretation**: an agent reads the spec, raises a consultation about the idempotency clause, and produces a candidate implementation.
3. **Validation**: a human reviewer audits the property-based test output and contract-test output against the spec.
4. **Enrichment**: the persistent-knowledge store captures the decision rationale and a cautionary example for future variants.
5. **Reuse**: the next agent working on dispute resolution reads the spec and the persistent-knowledge entry, and begins without re-deriving the idempotency rationale.

## Related Concepts

- [[Concepts/spec-driven-development-sdd-2026]] — the discipline that hosts these patterns.
- [[Concepts/specifications-as-contract-substrate-agentic-se]] — the substrate every pattern operates on.
- [[Concepts/agentic-harness-team-governance-sdd-2026]] — the harness that operationalizes the patterns at team scale.
- [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026]] — the loop-closing mechanism that lets patterns compound across sessions.