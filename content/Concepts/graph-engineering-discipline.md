---
title: "Graph Engineering"
details: "Discipline of designing the topology of multi-agent systems — nodes, dependencies, parallel branches, reducers, verification gates, loops, failure domains, and human checkpoints — rather than just chaining agents together. Prompts optimize nodes; graph engineering optimizes the system around them."
tags:
  - concepts
  - agent
  - orchestration
  - multi-agent
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Graph Engineering

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10|LunarResearcher — Graph Engineering: The Complete Guide]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

The discipline of deciding **how the work itself should move** in a multi-agent system. The thesis: once you have more than one agent, the hardest problem is no longer making an individual agent smarter — it is designing the topology. The article frames the field as distinct from prompt engineering, tool use, and loop design; those layers optimize nodes. Graph engineering optimizes the system.

**"A graph turns a pile of agents into a system."**

## Core Content

### The 14 Principles (from the source)

The original article presents graph engineering as 14 named principles, each a self-contained diagnostic or rule:

1. **[[Concepts/order-vs-dependency|Order vs Dependency]]** — a workflow is not a checklist; ask what data must exist, not what comes next
2. **[[Concepts/structured-graph-state|Structured Graph State]]** — define explicit state objects, not chat transcripts
3. **[[Concepts/dependency-test-edge|Dependency Test for Edges]]** — name the data that crosses every arrow, or delete the arrow
4. **[[Concepts/parallelism-width-budget|Parallelism Width Budget]]** — parallelism reduces wall-clock, not work; set a width budget
5. **[[Concepts/critical-path-latency|Critical Path Latency]]** — measure the longest unavoidable path, not the box count
6. **[[Concepts/deterministic-reduce-before-synthesis|Deterministic Reduce Before Synthesis]]** — put a code-based reducer before the reasoning node
7. **[[Concepts/asymmetric-verification|Asymmetric Verification]]** — worker finds the strongest answer, verifier finds the reason to reject
8. **[[Concepts/failure-domain-policy|Failure Domain Policy]]** — each node has an explicit ON FAILURE rule; degrade visibly
9. **[[Concepts/human-approval-as-graph-edge|Human Approval as a Graph Edge]]** — model approval as topology, not a prompt instruction
10. **[[Concepts/frozen-graph-constraints|Frozen Graph Constraints]]** — rules outside optimization (never publish without approval, etc.)
11. **[[Concepts/graph-shaped-observability|Graph-Shaped Observability]]** — observe the graph, not the chat transcript
12. **[[Concepts/graph-shape-catalog|Five Graph Shapes]]** — Fork/Join, Escalation Ladder, Tournament, Map→Reduce→Verify, Bounded Discovery Loop
13. **[[Concepts/graph-spec-template|Graph Spec Template]]** — describe the system as GOAL / INPUT / PARALLEL / EDGE / REDUCER / VERIFY / FAILURE / BUDGET / GATE / OUTPUT
14. **[[Concepts/when-not-to-graph|When Not to Graph]]** — single agent is correct when the task is small, the steps are genuinely sequential, or the cost of coordination exceeds the work

### Diagnostic vs Constructive Principles

The 14 split into two flavors:

**Diagnostics** (3, 4, 5, 14) — tests you apply to remove waste, fake dependencies, and unnecessary parallelism
**Constructive** (1, 2, 6, 7, 8, 9, 10, 11, 12, 13) — patterns and structures you build into the graph

### The Three-Layer Claim

> "Prompts optimize nodes. The spec optimizes the system."

Graph engineering sits above two earlier layers:
- **Prompt engineering** (1st generation) — how to ask a model
- **Tool use** (2nd generation) — how a model calls out
- **Loops** (3rd generation) — how a model iterates
- **Orchestration / Graph engineering** (4th generation) — how multiple agents cooperate

## Key Insights

1. **Topology > agent count** — more agents is rarely the answer; better topology is.
2. **The graph should be strict, the agent can improvise** — fuzzy model inside, deterministic interface outside.
3. **The spec is more valuable than the prompts** — describing the system beats writing 20 node prompts.
4. **Parallelism is a budget, not a default** — every extra worker has a reconciliation cost.
5. **Irreversible actions belong in architecture, not in prompt wording** — the publish node should be unreachable without approval.

## Related Concepts

- [[Concepts/graph-based-workflow-engine|Graph-Based Workflow Engine]] — runtime implementations of these patterns (Mastra, LangGraph, Kitaru)
- [[Concepts/coordinator-worker-task-dag-orchestration|Coordinator-Worker Task DAG Orchestration]] — related role-based delegation pattern
- [[Concepts/multi-agent-orchestration-patterns|Multi-Agent Orchestration Patterns]] — broader pattern catalog
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — strict interfaces around fuzzy models
- [[Concepts/hitl-approval-gates-for-tool-calls|HITL Approval Gates for Tool Calls]] — human-in-the-loop implementations
- [[Entities/lunarresearcher|LunarResearcher]] — author

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
