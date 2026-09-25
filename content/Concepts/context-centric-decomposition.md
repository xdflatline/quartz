---
title: "Context-Centric Decomposition"
details: "Design rule for multi-agent systems: split work by context boundary (what each agent needs to know), not by problem type (planner vs implementer vs tester). Splitting by problem type creates a 'telephone game' where each handoff loses context and coordination tokens exceed execution tokens. The dominant design failure mode Anthropic reports in production multi-agent systems."
tags:
  - concept
  - multi-agent
  - orchestration
  - agentic-system
source: "[[Raw/claude-building-multi-agent-systems-2026-01-23]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Context-Centric Decomposition

**Source:** [[Raw/claude-building-multi-agent-systems-2026-01-23]] — Anthropic Claude blog (Jan 23, 2026)
**Category:** Architecture Pattern
**Status:** Production-validated (Anthropic engineering observation across multiple customer deployments)

---

## Overview

When dividing work between agents, **decompose by context boundary, not by problem type**. The agent that writes a feature should also write its tests, because it already possesses the necessary context. Work should only be split when context can be **truly isolated** — meaning the downstream agent does not need to know why upstream decisions were made.

## The failure mode: telephone game

Splitting by problem type (planner / implementer / tester / reviewer) creates constant coordination overhead. Each handoff loses context. The test-writing agent lacks knowledge of why certain implementation decisions were made; the code reviewer lacks the context of exploration and iteration.

In one Anthropic experiment with agents specialized by software development role, **subagents spent more tokens on coordination than on actual work**.

## Effective decomposition boundaries

Split work when:

- **Independent research paths.** "Market trends in Asia" vs "market trends in Europe" — no shared context, can run in parallel.
- **Separate components with clean interfaces.** With a well-defined API contract, frontend and backend work can proceed in parallel.
- **Blackbox verification.** A verifier that only needs to run tests and report results does not require implementation context.

## Problematic decomposition boundaries

Do NOT split when:

- **Sequential phases of the same work.** Planning, implementation, and testing of the same feature share too much context.
- **Tightly coupled components.** Components requiring constant back-and-forth belong in the same agent.
- **Work requiring shared state.** Agents that would need to frequently synchronize understanding should remain together.

## Why this matters more than it sounds

The cost asymmetry is brutal:

- **Splitting by problem type** pays a coordination tax on every handoff AND loses fidelity on every handoff — compounding harm.
- **Splitting by context boundary** pays the coordination tax only at the boundary (where context actually isolates cleanly) and preserves fidelity everywhere within each agent.

For multi-agent systems with 3–10x token overhead versus single-agent (Anthropic's number), the difference between a working and a failing multi-agent system is often just whether the decomposition boundary aligns with a context boundary.

## How to test if a decomposition is right

A simple diagnostic: **can you write the downstream agent's system prompt without referencing the upstream agent's choices?** If yes, the split is clean — context is genuinely isolatable. If the downstream prompt has to say "you'll receive context from the planner agent, pay attention to its rationale," the split is wrong — you have a handoff tax and a fidelity loss, not a context boundary.

## Key insights

1. **Context-centric ≈ "single-agent-as-far-as-possible."** The rule has a strong default to NOT split. Splitting must be earned by a clear context-isolation win.
2. **The "blackbox verifier" exception is the canonical legitimate split.** Verification needs minimal context transfer by nature — it's the pattern Anthropic uses as the worked example of context-centric decomposition done right (see [[Concepts/verification-subagent-pattern]]).
3. **Parallelization is NOT an automatic reason to split.** Parallelizable subtasks that share enough context (e.g., parallel investigation of the same codebase) still benefit from being one agent with multiple tool calls rather than multiple agents.

## Related Concepts

- [[Concepts/subagent-context-isolation]] — the mechanism that makes a context boundary exploitable
- [[Concepts/verification-subagent-pattern]] — the textbook example of a context-isolatable subagent
- [[Concepts/multi-agent-decision-framework]] — parent decision rule: only reach for multi-agent at all when one of three constraints applies
- [[Concepts/multi-agent-orchestration-patterns]] — production consensus in the broader HN community reinforces the same instinct: keep coordination bounded

## References

- Raw article: [[Raw/claude-building-multi-agent-systems-2026-01-23]]
- Original: <https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them>