---
title: "Semantic contract for measures and relationships"
details: "The set of facts a semantic definition must record before an agent can use it safely: source binding, business identity and population, measure expression, unit separate from time grain, permitted grouping, denominator and zero-denominator behaviour, validity and supersession — plus, for relationships, cardinality, approved join direction, and known fanout risk. Encodes the rules that a matching column name is not a join, that ratio-of-totals is not mean-of-ratios, and that a run-level total must not be summed after a one-to-many detail join."
tags:
  - concept
  - schema
  - knowledge-management
  - architecture-pattern
created: 2026-11-03
updated: 2026-11-03
type: concept
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Semantic contract for measures and relationships

**Source:** NVIDIA Auto Ontology `references/modeling.md` ([[Raw/nvidia-auto-ontology-2026-11-03]])
**Category:** Modelling contract
**Status:** Shipped as modelling guidance in an open-source framework

---

## Overview

A term with a description is not a definition an agent can compute from. "Revenue" in a glossary tells a human what the word means; a *measure contract* tells a query generator exactly which expression, at which grain, over which population, in which unit, with which filters, produces the number — and what to do when the population is empty. The distinction matters because an agent will happily generate a plausible expression from a prose description, and the result will be wrong in ways prose cannot prevent.

The same holds for relationships. A relationship contract records not just "orders.customer_id → customers.id" but its expected multiplicity, its approved direction, its observed join coverage, and its known fanout risk. Those are precisely the facts that determine whether a join is safe, and precisely the facts a schema dump omits.

## Core Content

### Start with the question contract

Before modelling anything, record representative business questions and the constraints any correct answer must satisfy: population, measure, grouping, time range, comparison, exclusions. The model is then designed to make those questions answerable *without changing their material meaning*.

The source is explicit about what does **not** count as evidence of meaning:

- names are supporting evidence, not proof of identity or cardinality;
- small value samples are supporting evidence, not proof;
- equal current row sets do not make two concepts equivalent;
- a matching column name is not proof of a join.

### The measure contract

Every reusable measure records:

| Field | Why it is load-bearing |
|---|---|
| Expression and source evidence | What is actually computed, and the artefact proving it |
| Row grain and permitted query/grouping grain | Summing at the wrong grain is the classic silent error |
| Physical unit, separately from time grain | "Per month" and "in dollars" are independent facts |
| Additive dimensions and forbidden reaggregation | Which dimensions can be summed over at all |
| Numerator, denominator, weights, population filters | Ratios are only reproducible if all of these are fixed |
| Null, empty-population, and zero-denominator behaviour | Division by zero and missing rows are not zero |
| Effective time, availability time, revision, validity, supersession | Which version of the number a question is entitled to |

Two rules in that table deserve separation:

- **A quantity, fraction, period average, rate, and horizon total are different measures.** Substituting one for another produces an answer that is dimensionally plausible and factually wrong.
- **Ratio-of-totals is not generally mean-of-ratios.** The choice must be stated, not inferred from whichever formulation the generator reaches for.

### The relationship contract

For every relationship:

- source and target concepts and columns;
- direction and business role;
- expected multiplicity (one-to-one, one-to-many, many-to-many);
- key and null behaviour, and observed join coverage;
- approved query direction and known fanout risk;
- validity, version, and source evidence.

The verification instruction is to *test* rather than assume: duplicate and null keys, reverse joins, missing mappings, cardinality violations. And a boundary worth restating because it is easy to over-extend — **a semantic relationship is not automatically a prediction edge, a graph edge, or a solver coefficient.** The modelling layer describes joins and meaning; downstream uses need their own justification.

### Changing meaning is a different operation from fixing copy

The contract splits work by intent: metadata corrections patch an existing term or column attribute; a reusable derivation becomes a validated SQL attribute; concept-population or relationship changes go through a scoped model export/import. If a requested design cannot be expressed through the installed revision's public API, the instruction is to **return a model gap instead of weakening the design** — a rule that keeps the model honest at the cost of an explicit limitation.

### Handoff, not self-certification

A successful SQL execution, a 200 from an import, or a non-empty answer does not certify semantic correctness. The modelling workflow ends by handing a reviewed specification — versioned spec, exact source and ID mappings, relationship and measure contracts, approved join paths, positive and negative tests, unresolved gaps — to a separate publication workflow that handles backup, staged application, exact readback, and rollback.

## Key Insights

1. **Prose definitions and computable definitions are different artefacts.** An agent needs the second; most glossaries contain the first.
2. **Grain is the most consequential and least visible field in the contract.** Fanout and reaggregation errors survive every syntax check.
3. **Units and time grain are orthogonal.** Conflating them makes "monthly revenue" ambiguous in a way that silently changes the answer.
4. **Cardinality is a fact to be tested, not read off a schema.** Names and foreign-key declarations do not establish multiplicity or join coverage.
5. **An explicit model gap is a better outcome than a weakened model.** Silent simplification is how semantic layers decay into decoration.

## Related Concepts

- [[Concepts/semantic-layer-agent-grounding]] — the layer these contracts populate
- [[Concepts/grounded-answer-validation]] — where the contracts are checked against generated SQL
- [[Concepts/answer-readiness-vs-answerability]] — coverage is defined by whether these contracts exist
- [[Concepts/ontology-llm-data-modernization]] — the reconciliation process that produces such contracts across sources
- [[Concepts/semantics-as-universal-interface]] — the broader argument for explicit machine-consumable meaning

## Related Entities

- [[Entities/auto-ontology]]

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]] (`skills/nvidia-ontology-management/references/modeling.md`)
