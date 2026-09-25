---
title: "Multi-Agent Decision Framework"
details: "Anthropic's decision rule for when multi-agent systems are worth the 3–10x token overhead. Multi-agent consistently beats single-agent only in three situations: (1) context pollution degrading the main agent's reasoning, (2) parallelizable search/research subtasks, (3) specialization across domains with separable toolsets. Outside these, improved prompting of a single agent usually wins."
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

# Multi-Agent Decision Framework

**Source:** [[Raw/claude-building-multi-agent-systems-2026-01-23]] — Anthropic Claude blog (Jan 23, 2026)
**Category:** Architecture Pattern
**Status:** Production-validated (Anthropic engineering recommendation; reinforced by HN community consensus)

---

## Overview

Multi-agent systems are powerful but not universally appropriate. The decision rule Anthropic articulates is: **multi-agent is justified only when a single agent cannot solve the problem, where "cannot" is defined by three specific constraints** — context pollution, parallelizable subtasks, or separable specialization. Outside these, improved prompting of a single agent typically achieves equivalent results at a fraction of the cost.

## The cost floor

Every multi-agent implementation pays a tax:

- **3–10x more tokens** than a single-agent approach for equivalent tasks (Anthropic's number, from production deployments)
- Each agent has its own context window
- Agents must exchange messages to coordinate
- Results must be summarized when passed between agents
- Latency is often *higher* than sequential execution despite parallelism, because total computation grows faster than wall-clock savings

The tax is real and unavoidable. Multi-agent is only justified when the benefit (one of the three constraints below) exceeds it.

## The three legitimate cases

### 1. Context protection

A subtask generates high context volume (>1000 tokens) that would pollute the main agent's reasoning. The fix is [[Concepts/subagent-context-isolation]] — run the subtask in a separate agent, return only a compact summary.

**Signal:** the agent's response quality is degrading as the conversation grows; or a specific subtask is the obvious context-volume bottleneck.

### 2. Parallelization

Tasks naturally decompose into independent pieces (research across multiple sources, tests for multiple components). Run subagents concurrently and stitch the results.

**Signal:** the work is independent enough that one agent could investigate facet A while another investigates facet B with zero overlap.

**Caveat:** the primary benefit is **thoroughness, not speed**. Multi-agent often takes longer in wall-clock time than a sequential single-agent approach despite parallelism.

### 3. Specialization

Different tasks need different toolsets, system prompts, or domain expertise that conflict when combined.

**Signals:**
- Quantity: 20+ tools in one agent; the agent struggles to pick the right one
- Domain confusion: tools span unrelated domains (DB + API + FS) and the agent confuses which applies
- Degraded performance: adding tools degrades existing performance
- Conflicting behavioral modes: support (empathetic) vs code review (critical) vs compliance (rigid) in one system prompt

**Caveat:** specialization introduces routing complexity. The orchestrator must classify correctly, and misrouting produces poor results.

## When to NOT reach for multi-agent

- **Single-agent with better prompting would work.** Anthropic reports teams that built elaborate multi-agent architectures only to discover that improved prompting on a single agent achieved equivalent results.
- **The work is sequential phases of the same task.** Planning → implementing → testing a single feature shares too much context to split (see [[Concepts/context-centric-decomposition]]).
- **The cost asymmetry is unclear.** If you can't articulate which of the three constraints you'd remove by going single-agent, the split is probably premature.

## Concrete signals you've outgrown single-agent

Beyond the abstract decision rule, three signals suggest a concrete need:

- **Approaching context limits.** Performance degrades as context grows. (Mitigation first: try [[Concepts/context-engineering]] / compaction before multi-agent.)
- **Managing 15–20+ tools.** Before multi-agent, try the [Tool Search Tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/tool-search-tool) — reduces token usage by up to 85% while improving tool selection accuracy.
- **Parallelizable subtasks.** Independent research facets, isolated test components.

These thresholds shift as models improve. Current limits are practical guidelines, not fundamental constraints.

## The "try simpler first" rule

Anthropic's closing advice: **"Start with the simplest approach that works, and add complexity only when evidence supports it."** This is the same [[Concepts/explicit-instruction-over-implicit-inference|minimum-necessary-structure principle]] applied to architecture: longer/more complex is not better, the right architecture is the smallest one that meets the constraints.

## Distinction from related concepts

- **[[Concepts/multi-agent-orchestration-patterns]]** — the broader production consensus from the HN community (custom orchestration layers, explicit task graphs, agent isolation). Complementary; this Anthropic framework is more recent and more prescriptive about *when*, the HN patterns are more about *how*.
- **[[Concepts/agent-collusion-pattern]]** — failure mode that arises *inside* multi-agent systems once you've decided to use them; this framework decides whether to use them at all.
- **[[Concepts/agent-turf-war-escalation]]** — another intra-multi-agent failure mode (specialist agents refusing to coordinate).

## Key insights

1. **The default is single-agent.** The decision framework has a strong default to NOT use multi-agent. Multi-agent must be earned by one of three specific constraints.
2. **Improved prompting is often the right answer.** Many "we need multi-agent for this" claims dissolve under better single-agent prompting. This is the same lesson as the prompt-engineering principle "don't over-engineer."
3. **The cost is not negotiable.** 3–10x more tokens is not a tunable parameter; it's a structural consequence of duplicated contexts and coordination messages. The benefit must exceed the tax or the system is a net loss.

## Related Concepts

- [[Concepts/subagent-context-isolation]] — case 1 implementation
- [[Concepts/context-centric-decomposition]] — the *how* once you've decided *when*
- [[Concepts/verification-subagent-pattern]] — the canonical legitimate subagent, useful regardless of which of the three cases applies
- [[Concepts/multi-agent-orchestration-patterns]] — production patterns that flesh out *how* to implement once the decision is made

## References

- Raw article: [[Raw/claude-building-multi-agent-systems-2026-01-23]]
- Original: <https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them>