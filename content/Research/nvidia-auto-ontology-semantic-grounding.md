---
title: "NVIDIA Auto Ontology: semantic grounding for agentic analytics"
details: "Synthesis of NVIDIA's Auto Ontology framework and the four disciplines it encodes: a semantic layer as the resolution target for agent queries, readiness separated from answerability, a modelling contract for measures and relationships, and post-execution answer validation. Frames the reliability-over-speed argument, contrasts the curated tool surface with the schema-exposed graph interface pattern already in the garden, and records what the source does and does not establish."
tags:
  - research
  - llm
  - agent
  - schema
  - knowledge-management
created: 2026-11-03
updated: 2026-11-03
type: research
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# NVIDIA Auto Ontology: semantic grounding for agentic analytics

**Primary source:** [[Raw/nvidia-auto-ontology-2026-11-03]] (README, `docs/mcp.md`, three agent skills, `AGENTS.md`)
**Repository:** https://github.com/NVIDIA/auto-ontology (Apache-2.0, public)
**Date:** 2026-11-03

---

## Why this matters here

The garden already holds the *argument* for semantic layers — [[Concepts/semantics-as-universal-interface]] and [[Concepts/agentic-ready-data-modeling]] state that agents need machine-consumable meaning, and [[Concepts/ontology-llm-data-modernization]] describes how such an ontology gets built from legacy sources. What was missing is a concrete, inspectable implementation that shows where the argument becomes engineering: which artefacts a definition must contain, which checks run before and after a query, and how the layer is exposed to a model without letting it escape.

Auto Ontology is that implementation. Its most useful contribution to this wiki is not the product but the **operational detail** — the four disciplines below, each of which is separable from NVIDIA's stack.

## The four disciplines

### 1. The layer is a resolution target, not a documentation surface

[[Concepts/semantic-layer-agent-grounding]] — the agent's vocabulary is terms and SQL attributes, each bound to physical columns. The layer answers six questions (where, what, whether, how, provenance, similar) and the generated SQL is checkable against the definitions it was built from. The architectural claim is that reliability, not latency, is what gates agentic analytics: a fast wrong number reaches a decision sooner.

The enforcement mechanism matters as much as the claim: the MCP surface has **no raw-schema tool**. The semantic layer is not optional advice to the model; it is the only path the model has.

### 2. Readiness and answerability are different questions

[[Concepts/answer-readiness-vs-answerability]] — a compiled layer plus a live connection is a property of the deployment; coverage of a specific question is a property of the question. The dangerous state is having one without the other, because it looks healthy: terms resolve, the glossary reads, and every question fails expensively. Two observations generalise well beyond this product — a named database in a catalog is not a working connection, and permission-scoped unverifiability should be reported as unverifiable rather than as a failure.

### 3. Definitions need contracts, not descriptions

[[Concepts/semantic-contract-for-measures]] — a measure carries expression, grain, unit (separate from time grain), additive dimensions, numerator/denominator, empty-population behaviour, and validity/supersession. A relationship carries cardinality, approved direction, observed join coverage, and fanout risk. The rules that a matching column name is not a join, that ratio-of-totals is not mean-of-ratios, and that a run-level total must not be summed after a one-to-many join are the concrete content behind the abstract demand for "semantics".

### 4. Execution success is not answer correctness

[[Concepts/grounded-answer-validation]] — validate the material question, the SQL, the rows, and the prose separately. Fanout preserves plausibility while destroying magnitude; truncation caps any completeness claim; observed/predicted/recommended/committed are distinct evidence states that answers drift up by accident. Fail closed with a receipt when a material constraint cannot be verified.

Underneath all four sits [[Concepts/agent-tool-surface-curation]]: the tool surface is designed so that the cheap check precedes the expensive one, the read path cannot mutate the glossary, and the evidence comes back as structured fields rather than rendered prose.

## Where this disagrees with prior art in the garden

[[Concepts/agent-facing-graph-query-interface]] describes the opposite interface choice: give the agent the **schema** of its knowledge substrate plus query tools, and let it formulate its own traversals, because schema exposure is what turns a graph into an instrument the agent reasons against. Auto Ontology deliberately withholds exactly that, on the grounds that a catalog browser invites an agent to reason about raw tables instead of business meaning.

Both positions are defensible, and the difference is informative:

- **Schema-exposed traversal** suits substrates where the agent's job is discovery and the schema itself is trustworthy, small enough to hold, and cheap to query — code graphs, personal knowledge bases.
- **Curated semantic surface** suits substrates where the agent's job is to produce a *number someone will act on*, the schema is large and politically contested, and the failure mode is a plausible wrong answer rather than a missing one.

The discriminator is not product taste; it is what happens when the agent gets it wrong. Where wrongness is cheap and exploration is the point, expose the schema. Where wrongness is expensive and the vocabulary is contested, expose only the settled meaning. The garden's existing pages sit on both sides of that line, and the line itself is worth naming as a design question rather than treating one pattern as the default.

## What the source establishes, and what it does not

**Established by inspection:** the component topology, the tool list, the check sequence, the contract fields, the deployment paths, the authentication model, and the validation workflow. These are documented in the repository and are checkable against the code.

**Not established:**

- **Accuracy.** The repository points to a separate BIRD benchmark harness (`NVIDIA/ontology-sql-eval`) but publishes no results. The reliability claim is architectural, not measured, in this source.
- **Cost.** `ask_question` is described as "many sequential model calls, typically tens of seconds". No token or latency figures are given, and the pre-flight checks exist precisely because the expensive path is expensive.
- **Curation effort.** The framework supplies the structure for reconciliation; the human cost of producing good definitions is acknowledged implicitly (governance, SME validation) but never quantified.
- **Maturity.** The project is roughly six months old, has twelve contributors, and explicitly refuses external contributions — which bounds how much independent scrutiny the design has received.
- **Internal/external status.** The README calls it an open library under Apache-2.0; `docs/mcp.md` still says Auto Ontology is "NVIDIA-internal today". The public repo and license suggest the latter is stale, but the install instructions retain the caveat. Treat the "internal" statement as documentation drift, not as a current fact.

## Open questions for this garden

1. **Does a curated semantic surface survive contact with open-ended analysis?** Every omitted tool is a question the agent cannot answer without a human. The design bets that the questions outside the layer are not worth answering automatically; that bet is untested here.
2. **Who owns the layer when the definitions conflict?** The modelling workflow can detect and classify disagreement, but the authority to settle "what is revenue" is organisational. The framework's governance story is thinner than its technical story.
3. **Is provenance sufficient for trust?** Provenance identifies which definition was used. It does not establish that the definition is current, correct, or the one the business would choose today — that is what the validity and supersession fields are for, and they are only as good as their maintenance.
4. **What is the cheapest viable version of this pattern?** The full stack is heavy. The transferable subset — a glossary bound to columns, a readiness check, a grain/fanout validation pass — could be applied to any text-to-SQL agent without adopting the framework.

## Related Pages

- [[Entities/auto-ontology]] — the project and its technical shape
- [[Concepts/semantic-layer-agent-grounding]]
- [[Concepts/answer-readiness-vs-answerability]]
- [[Concepts/semantic-contract-for-measures]]
- [[Concepts/grounded-answer-validation]]
- [[Concepts/agent-tool-surface-curation]]
- [[Concepts/agent-facing-graph-query-interface]] — the contrasting interface choice
- [[Concepts/ontology-llm-data-modernization]] — how ontologies get built from legacy sources
- [[Concepts/semantics-as-universal-interface]] — the modelling argument this operationalises
- [[Concepts/agentic-ready-data-modeling]] — the data-model requirements agents impose

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]]
- Repository: https://github.com/NVIDIA/auto-ontology
- Benchmark harness: https://github.com/NVIDIA/ontology-sql-eval
