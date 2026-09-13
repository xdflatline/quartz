---
title: "Data Model as Tool, Not Theory"
details: "William Kent's argument that data models should be evaluated as tools — useful, incomplete, economic, orthogonal to problems — rather than as theories that aim at completeness and distinction. The implication is that users adapt to tools (a conditioning of perception), not the reverse, and that requiring a tool to fit the mould of any theory is a category mistake."
tags:
  - knowledge-management
  - architecture-pattern
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "[[Raw/bkent-data-reality-excerpts-2026-09-13]]"
---

# Data Model as Tool, Not Theory

**Source:** William Kent, *Data and Reality* (1978/1998), Chapter 12: "Reality and Tools" ([[Raw/bkent-data-reality-excerpts-2026-09-13]])
**Category:** Architecture Pattern (epistemic / design philosophy)
**Status:** Fundamental

---

## Overview

Kent draws a sharp distinction between **theories** and **tools**, and argues that data models are tools, not theories. Theories tend toward analytic completeness and the careful separation of distinct phenomena; tools tend to intermingle fragments of theories to get a real job done. The economic justification for a tool is its problem-solving value vs. its production and maintenance cost — completeness and generality only matter to the extent that they cheaply cover many problems.

Conflating the two is a category mistake: requiring a tool to fit the mould of a theory produces brittle designs, and defending a tool as if it were a theory obscures its real limitations.

## Core Content

### Theories vs. tools — Kent's contrast

| Dimension | Theory | Tool |
|-----------|--------|------|
| Goal | Completeness, distinctness | Useful, profitable |
| Phenomena | Analytically separated | Intermingled |
| Justification | Accounts for all aspects | Problem-solving value vs. cost |
| Failure mode | Defective if it omits something | Defective only if it doesn't pay for itself |
| Behaviour | Predictable and idealised | Predictable and *versatile* — applicable across problems |

### What this means for data models

> "Data models are tools. They do not contain in themselves the 'true' structure of information."

When we present a hierarchical model to a user, we should not expect them to exclaim that their information "really is" hierarchical. They have to learn how to use it. Kent argues that what is usually called "learning" the model is in fact:

- a struggle to contort the problem to fit the tool,
- experimentation with different representations,
- sometimes abandonment of parts of the application the tool can't handle,
- and a *conditioning of perception* — the user comes to accept the model's assumptions as fact and to ignore the cases where it fails.

### Orthogonality

> "Tools are generally orthogonal to the problems they solve, in that a given tool can be applied to a variety of problems, and a given problem can be solved in different ways with different tools."

Versatility is a desirable property of a tool. It also follows that the characteristics of a tool should be understood *separately* from the problems to which it is applied — you cannot argue that a tool is bad because it doesn't solve one particular problem well, nor good because it solves that problem well.

### When this matters

Kent's claim is more radical than it sounds. Most database pedagogy treats the relational model as a theory with definite truth values ("is this in Third Normal Form?"). Kent argues the productive stance is to ask, *for this user and this purpose, what does the tool's incompleteness cost us?* The answer usually justifies the tool; the mistake is forgetting that the answer is conditional.

## Key Insights

1. **Models are tools; users adapt to tools.** Treating a model as a theory to be discovered produces misplaced reverence.
2. **Incompleteness is not a bug** — it's what makes a tool economically justifiable. Completeness is a property of theories, and tools are not theories.
3. **Orthogonality is a virtue**, not a deficiency. A tool that solves one problem only is less useful than one that solves many.
4. **"Learning" a data model is largely conditioning** — the user is being shaped to the model as much as the model is being applied to the user's problem.
5. **Beware the pseudo-exactness** of data models presented as if they captured the true structure of information.

## Related Concepts

- [[Concepts/map-vs-territory-data-modeling]] — the underlying analogy that makes the tool/theory distinction coherent
- [[Concepts/three-worlds-ontology-amorphous]] — the ontological claim that explains why models are necessarily incomplete
- [[Concepts/reconciliation-by-scope-and-purpose]] — the practical framework for choosing a tool's scope
- [[Concepts/linguistic-relativity-of-modeling]] — the language layer of the tool

## Related Entities

- [[Entities/william-kent]]
- [[Entities/data-and-reality]]

## References

- Raw Article: [[Raw/bkent-data-reality-excerpts-2026-09-13]]
- Original: https://bkent.net/Doc/darxrp.htm#Reality%20and%20Tools