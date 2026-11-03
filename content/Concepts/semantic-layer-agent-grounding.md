---
title: "Semantic layer as the grounding contract for agentic analytics"
details: "The argument that an agent querying enterprise data needs a semantic layer between it and the physical schema: a machine-readable layer that says where data lives, what it means, whether it should be used, how it is derived, where it came from, and what is similar. Positions reliability, not speed, as the gate on agentic analytics, and treats deterministic query generation plus per-answer provenance as the properties that make an agent's numeric answer defensible."
tags:
  - concept
  - llm
  - agent
  - schema
  - knowledge-management
  - architecture-pattern
created: 2026-11-03
updated: 2026-11-03
type: concept
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Semantic layer as the grounding contract for agentic analytics

**Source:** NVIDIA Auto Ontology documentation ([[Raw/nvidia-auto-ontology-2026-11-03]])
**Category:** Architecture Pattern
**Status:** Implemented in an open-source framework; the reliability argument is the vendor's framing, not an independently measured result

---

## Overview

Agents can already retrieve documents and write SQL. What they cannot do reliably is know which of several plausible tables holds *revenue*, which of two same-named columns is the certified one, or whether the number they just produced is comparable to last quarter's. The claim behind this pattern is that the binding constraint on agentic analytics is not capability but **trust**, and that trust comes from a layer the agent is forced to query through rather than a better prompt.

The layer answers six questions about every piece of data it exposes:

1. **Where it lives** — the physical source binding behind a business term.
2. **What it means** — the business identity and population, not the column name.
3. **Whether to use it** — certification, validity, and supersession state.
4. **How to use it** — approved derivations, join paths, grain, and filters.
5. **Where it came from** — lineage and provenance attached to the answer.
6. **What is similar** — semantic neighbours and synonyms, so a question phrased in the user's vocabulary resolves to the same concept.

An agent that must resolve a question through this layer generates SQL *deterministically* from certified definitions instead of guessing from schema names. That is the mechanism behind the explainability claim: the generated query is checkable against the definitions it was built from, and the provenance travels with the result.

## Core Content

### The failure this addresses

The failure mode is not "the agent cannot write SQL". It is the plausible-but-wrong answer: a correct-looking aggregation over the wrong table, the wrong grain, or a same-named measure from a different system. Speed makes this worse — a fast wrong number reaches a decision sooner. Hence the framing that reliability, not latency, is the gate.

The pattern's response has three parts:

- **Reconcile before answering.** Definitions that disagree across systems are resolved once, in the layer, rather than at question time by whichever table the model happened to pick.
- **Constrain generation.** The model maps question → certified term/measure/join path → SQL, so the space of queries it can emit is bounded by what the layer knows.
- **Return evidence with the answer.** The SQL and the source identity are part of the result, not an audit log written afterwards.

### What the layer is made of

In the Auto Ontology implementation the layer is a glossary of **terms** (business concepts with descriptions, synonyms, and related terms), each bound to physical **columns**, plus **SQL attributes** (named, validated expressions defined under a term). Terms and attributes are the only vocabulary the agent is given. Tables appear only as a view onto the terms and attributes they participate in.

This is the significant design choice: the semantic layer is *not* a catalog browser with a chat front-end. It is a resolution target. The agent asks "what does an active customer mean here", gets a definition and the columns behind it, and then asks a question that the layer can answer — or is told it cannot.

### Relationship to existing semantic models

The layer is positioned as complementary to semantic models an organisation already owns (dbt-style metrics layers, BI semantic models, existing ontologies): the framework ingests or connects to them and exposes them to agent harnesses over MCP, CLI, and API. The value it claims to add is the *agent-facing* part — a curated tool surface, per-answer provenance, and a write path that keeps human-owned definitions authoritative.

### Boundaries

- The reliability argument is architectural, not empirical. The repository points at a separate text-to-SQL benchmark harness (BIRD) but publishes no results in the main repo, so "more reliable than raw text-to-SQL" is an unverified claim in this source.
- The layer is only as good as its curation. A stale or thin glossary produces confidently wrong answers with excellent provenance — provenance tells you which definition was used, not whether that definition is right.
- Reconciliation is a governance activity with a human owner; the framework provides the structure for it, not the authority to settle it.

## Key Insights

1. **Reliability gates agentic analytics, and the gate is semantic, not syntactic.** Correct SQL over the wrong definition is the dominant failure, and no amount of model quality removes it.
2. **A semantic layer earns its keep by being a resolution target, not a documentation surface.** If the agent can bypass it and read raw schema, the layer's guarantees are optional and therefore absent.
3. **Provenance must be part of the answer payload.** Attaching SQL and source identity to the response is what turns a number into a checkable claim.
4. **Deterministic generation is a scoping mechanism.** Bounding the query space to certified terms and join paths is what makes the output reviewable.
5. **Curation is the real cost centre.** The architecture shifts effort from prompt engineering to definition ownership — which is where the business already has accountability.

## Related Concepts

- [[Concepts/semantic-contract-for-measures]] — what a definition must record to be usable this way
- [[Concepts/answer-readiness-vs-answerability]] — the pre-flight check that the layer and the data are both actually available
- [[Concepts/grounded-answer-validation]] — what to verify after a query runs
- [[Concepts/agent-tool-surface-curation]] — how the layer is exposed to the agent without exposing the schema
- [[Concepts/semantics-as-universal-interface]] — the modelling argument this pattern operationalises
- [[Concepts/agentic-ready-data-modeling]] — the data-model-side requirements agents impose
- [[Concepts/ontology-llm-data-modernization]] — how such a layer gets built from legacy sources

## Related Entities

- [[Entities/auto-ontology]]
- [[Entities/nvidia]]

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]]
- Repository: https://github.com/NVIDIA/auto-ontology
