---
title: "Graph Engineering (LunarResearcher, 2026)"
details: "Synthesis of LunarResearcher's 14-principle framework for designing multi-agent system topology. The thesis: once you have more than one agent, the bottleneck is no longer how smart the agent is but how the work itself moves — through nodes, dependencies, reducers, verification gates, failure domains, and human checkpoints."
tags:
  - research
  - agent
  - orchestration
  - multi-agent
created: 2026-09-02
updated: 2026-09-02
type: research
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Research Index: Graph Engineering (LunarResearcher, 2026)

**Updated:** 2026-09-02
**Source:** [Graph Engineering: The Complete Guide — LunarResearcher, Aug 10 2026](https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide)

## Overview

Synthesis of a single-source ingestion. The article presents **graph engineering** as a named discipline distinct from prompt engineering, tool use, and loops. The argument: in a multi-agent system, the bottleneck is topology, not model quality. The post delivers 14 named principles, 5 reusable shapes, 1 spec template, and a closing refutation of "more agents = better."

This research index groups the 14 principles into 4 themes for navigability, lists the cross-cutting slogans, and links the article's claims to the rest of the wiki.

## Concepts

### The Discipline (Umbrella)
- [[Concepts/graph-engineering-discipline|Graph Engineering]] — the named discipline; umbrella for the 14 principles
- [[Concepts/when-not-to-graph|When Not to Graph]] — the discipline includes refusal; single agent is correct for small or sequential work

### Diagnostics (test the existing graph)
- [[Concepts/order-vs-dependency|Order vs Dependency]] — a workflow is not a checklist; ask what data must exist
- [[Concepts/dependency-test-edge|Dependency Test for Edges]] — name the data that crosses every arrow, or delete the arrow
- [[Concepts/parallelism-width-budget|Parallelism Width Budget]] — width has costs; set a budget; optimize for useful independent coverage per dollar
- [[Concepts/critical-path-latency|Critical Path Latency]] — measure the longest path, not the box count

### Constructive Patterns (build these into the graph)
- [[Concepts/structured-graph-state|Structured Graph State]] — typed state objects, not chat transcripts
- [[Concepts/deterministic-reduce-before-synthesis|Deterministic Reduce Before Synthesis]] — code-based reducer before the reasoning node
- [[Concepts/asymmetric-verification|Asymmetric Verification]] — worker finds strongest, verifier finds reason to reject
- [[Concepts/failure-domain-policy|Failure Domain Policy]] — per-node ON FAILURE rules; degrade visibly
- [[Concepts/human-approval-as-graph-edge|Human Approval as a Graph Edge]] — approval is an edge, not a node; make unsafe transitions unreachable
- [[Concepts/frozen-graph-constraints|Frozen Graph Constraints]] — rules outside optimization (never publish without approval, etc.)

### Observability & Specification
- [[Concepts/graph-shaped-observability|Graph-Shaped Observability]] — 7 metrics: critical-path latency, node failure rate, retry rate, verifier kill rate, fan-out efficiency, compression ratio, human intervention rate
- [[Concepts/graph-shape-catalog|Five Graph Shapes]] — Fork/Join, Escalation Ladder, Tournament, Map→Reduce→Verify, Bounded Discovery Loop
- [[Concepts/graph-spec-template|Graph Spec Template]] — the 10-field spec: GOAL / INPUT / PARALLEL / EDGE / REDUCER / VERIFY / FAILURE / BUDGET / GATE / OUTPUT

## Tools & Projects

### People
- [[Entities/lunarresearcher|LunarResearcher]] — author of the source post

### Articles
- [[Entities/lunarresearcher-graph-engineering-post|Graph Engineering: The Complete Guide]] — the source post (entity entry)

## Raw Sources

- [[Raw/lunarresearcher-graph-engineering-2026-08-10]] — full extracted body of the Substack post, dated 2026-08-10, retrieved 2026-09-02

## Key Threads/Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [Graph Engineering (LunarResearcher, Substack)](https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide) | Multi-agent topology | 2026-08-10 | 14 principles, 5 shapes, 1 spec template, 7 metrics |

## Cross-Cutting Themes

### Theme 1: Topology is the next hard skill

The article positions graph engineering as the **fourth generation** of AI workflow design — after prompt engineering, tool use, and loops. Each generation solved a layer; orchestration is the next one. The slogan: **"More agents are not the answer. Better topology is."**

This connects to:
- [[Concepts/multi-agent-orchestration-patterns|Multi-Agent Orchestration Patterns]] — wiki's existing catalog
- [[Concepts/coordinator-worker-task-dag-orchestration|Coordinator-Worker Task DAG Orchestration]] — related role-based pattern
- [[Concepts/graph-based-workflow-engine|Graph-Based Workflow Engine]] — runtime implementations (Mastra, LangGraph, Kitaru)

### Theme 2: Strict outside, fuzzy inside

A recurring thread across the 14 principles: the **model** is allowed to be fuzzy; the **graph** is not. Structured state (2), typed edge data (3), deterministic reducers (6), and frozen constraints (10) are all implementations of the same discipline — the interface is the contract, not the model behavior.

This connects to:
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — strict interfaces around fuzzy models
- [[Concepts/deterministic-first-architecture|Deterministic-First Architecture]] — the broader principle
- [[Concepts/capability-first-tool-design|Capability-First Tool Design]] — design tools the same way

### Theme 3: Remove waste before adding capacity

Four of the 14 principles are diagnostic (1, 3, 4, 5) — they ask you to **remove** fake dependencies, empty edges, runaway width, and step counts. The article consistently argues that the first move is subtraction, not addition. Width is a budget, not a default.

This connects to:
- [[Concepts/capabilities-first-system-design|Capabilities-First System Design]] — design from what you need, not what you can build
- [[Concepts/k8s-resource-feedback-loop-discipline|K8s Resource Feedback Loop Discipline]] — same discipline in a different domain

### Theme 4: Architecture over wording for irreversible actions

Three principles (8, 9, 10) — failure domains, human approval, frozen constraints — make the same point: if an action is irreversible, the safety lives in the **graph topology**, not in the prompt. "The model was instructed to ask first" is not enough; the publish node should be unreachable without approval.

This connects to:
- [[Concepts/hitl-approval-gates-for-tool-calls|HITL Approval Gates for Tool Calls]] — runtime implementation
- [[Concepts/agent-turf-war-escalation|Agent Turf War Escalation]] — failure mode this design constrains
- [[Concepts/agent-low-variance-conformity|Agent Low-Variance Conformity]] — adjacent risk pattern

## Slogans Worth Keeping

The article is slogan-dense. The high-signal ones:

- **"A graph turns a pile of agents into a system."**
- **"The agent can improvise. The graph should not."**
- **"Use models for ambiguity. Use code for plumbing."**
- **"The goal is not to maximize parallelism. The goal is to remove fake synchronization."**
- **"Add width only when the extra worker increases coverage more than it increases reconciliation cost."**
- **"Use models for ambiguity. Use code for plumbing."**
- **"Prompts optimize nodes. The spec optimizes the system."**
- **"A graph buys width, isolation, and control flow. It does not automatically buy taste or truth."**
- **"Without a stopping rule, a loop is not architecture. It is a leak."**
- **"A smart optimizer inside weak boundaries becomes dangerous faster. Inside strong boundaries, useful faster."**

## Open Questions Raised by the Post

- How does the spec template map to existing frameworks (Mastra's createStep/createWorkflow, LangGraph's StateGraph, Kitaru's @checkpoint)? Each is a candidate for a per-framework mapping page.
- The 7 observability metrics are aspirational; which of them are actually instrumented in any current framework?
- The "Bounded Discovery Loop" is described as one of the five shapes, but its stop conditions (no new findings for N rounds, max spend, max time) are a separate design surface. Worth a dedicated concept page.
- The 14 principles overlap with the wiki's existing concepts (`failure-domain-policy` ↔ `idempotency-for-ai-agents`, `structured-graph-state` ↔ `observational-memory-pattern`). Cross-links are in place; consolidation is for a later housekeeping pass.

## Next Research Directions

- [ ] **Map the 14 principles to Mastra, LangGraph, and Kitaru primitives** — for each principle, name the runtime API that implements it (or note its absence).
- [ ] **Draft a "Graph Spec → Code" generator idea** — the spec template is framework-portable; could a small tool emit Mastra / LangGraph skeleton from the 10 fields?
- [ ] **Audit the existing multi-agent concepts in the wiki against the 14 principles** — flag gaps (e.g. is there a concept for "verifier kill rate" or "compression ratio" as a first-class metric?).
- [ ] **Write a per-framework mapping page for `graph-engineering-discipline`** — top of file: which framework implements which of the 14.
- [ ] **Compare to Anthropic's multiagent systems writeup (Aug 2026)** — overlapping territory; where do they agree, where do they differ?
