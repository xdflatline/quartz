---
title: "Wires-as-Context Graph"
details: "Architecture pattern where each node's prompt is assembled by walking the node's incoming edges in topological order — edges literally are the context the model sees. Editing the graph edits the model's memory. Same graph ⇒ same prompt, independent of how the graph was drawn."
tags:
  - concept
  - llm
  - agent
  - context-engineering
  - knowledge-management
  - architecture-pattern
created: 2026-08-15
updated: 2026-08-15
type: concept
sources:
  - .Raw/github-thoughtdag-readme-2026-08-15.md
---

# Wires-as-Context Graph

**Source:** [[Raw/github-thoughtdag-readme-2026-08-15.md]]
**Category:** Architecture Pattern
**Status:** Production-validated (shipped in ThoughtDAG v1.x, 2026; 410 commits)

---

## Overview

A wires-as-context graph treats **incoming edges as the source of truth for what an LLM node sees**. Concretely, a `buildContext()` routine walks every incoming edge of the target node in topological order and stitches the result into the prompt before send. The graph is intentionally **acyclic** — humans supply the loop, not a runtime scheduler. The same graph always produces the same prompt, regardless of the order the user drew it.

The pattern's defining claim is *editing the graph edits the model's memory*: deleting a single edge changes the next call's answer, with no other state to chase.

## Core Content

### The one rule

> *What the model sees is exactly what wires into the node. Editing the graph edits the model's memory.*

### Edge taxonomy (from ThoughtDAG)

| Edge | Visual | Behavior | Reasoning role |
|------|--------|----------|----------------|
| **Continue** | Solid purple | Inherits full ancestor context in topo order | Standard next-step |
| **Explore** | Solid orange | Select text on parent → branch with selection as seed | Cheap divergence / "what if" |
| **Reference** | Dashed | Quoted without dragging in conversation; toggle quote ⇄ full, depth as property | Inline citation, bypass of broadcast |
| **Reviewer** | Sliding red | Critic role, auto-critiques each step | Quality gate |
| **Archive** (state, not type) | Dimmed | Excluded from all context walks, restorable | Hide without losing |

The visual law: **solid = structural (must be in context), dashed = bypass (reference only)**. This is the single cue the user needs to predict what a node will do.

### Assembly order

`buildContext()` lays down layers in a fixed order, independent of how the user built the graph:

1. **Materials** (PDFs, attachments, file nodes) — pulled by reference, not chain.
2. **Reference blocks** (dashed edges at chosen depth) — quoted summaries.
3. **Conversation** (solid edges, topo-walked) — full ancestor chain.

This guarantees determinism: same graph topology ⇒ byte-identical prompt.

### Determinism by design

- **Acyclic by construction** — no infinite walks.
- **Topological ordering** instead of chronological — drawing order doesn't leak into context.
- **Same graph = same prompt** — replay reproduces answers; merging branches is meaningful.

### Adjacent primitives that share the shape

- **Typed takeaways** (display-only badges: ✕ ruled out · ⚖ decided · ↩ pivoted · ? open) — never enter context or fingerprints; they annotate, they don't bind.
- **Send preview** (`~N tok · M messages · K files`) — the user sees exactly what they're about to send before they send it, in the same taxonomy as `buildContext()`.
- **Archive vs. delete** — pruning edges without losing them; restores batch.
- **Staleness / replay** — invalidating a node marks descendants for replay in dependency order; replay runs with live token estimates.

### Comparison to chat and DAG runtimes

| Property | Chat terminal | DAG runtime (e.g. Airflow) | Wires-as-context graph |
|---|---|---|---|
| Truth | Append-only message log | Task results | Edge topology |
| Loop | Implicit (next user turn) | Explicit scheduler | Human (no scheduler) |
| Edit model memory by | Re-prompt / scroll past | Re-run pipeline | Delete / change edge |
| Determinism from graph | N/A | Limited (state-dependent) | Strong (topo order only) |
| Best for | Q&A loop | ETL/pipelines | Reasoning structure |

### Failure modes and how the pattern absorbs them

| Failure | How edges absorb it |
|---------|--------------------|
| Wrong context → wrong answer | Delete the offending edge; prompt reconstructs deterministically |
| Token bloat from full transcript | Archive (don't delete) noisy ancestors; restore if needed |
| Lost trail of decisions | Typed takeaway badges on every answer version |
| Branching chaos | Explore edges carry selection as seed, not full context |
| Hallucinated citation | Reference edges are dashed — explicit "bypass," auditable at a glance |

## Key Insights

1. **Topological ≠ chronological.** A node's prompt depends on the *ancestor edge set*, not the *insertion order*. This is what makes the pattern reproducible from a user-drawn graph without any runtime ordering state.
2. **Visual encoding is API.** Solid = contextual force, dashed = bypass. Encoding edge semantics into stroke style means the user never has to read configuration to predict behavior.
3. **Archive beats delete.** Removing an edge from context should not destroy it; dim-and-restore lets users prune without remorse and is what makes exploration tractable on large graphs.

## Related Concepts

- [[Concepts/coordinator-worker-task-dag-orchestration]] — DAG-orchestration lineage (closed loop, scheduler runs it); wires-as-context is the user-in-the-loop variant.
- [[Concepts/graph-based-workflow-engine]] — broader graph workflow engine category; this pattern specifies the LLM context use.
- [[Entities/thoughtdag]] — primary shipped implementation.

## References

- Raw Article: [[Raw/github-thoughtdag-readme-2026-08-15.md]]
- Original: https://github.com/chenxiachan/thoughtdag
- Features docs (esp. Context Engine section): https://raw.githubusercontent.com/chenxiachan/thoughtdag/main/docs/features.md
