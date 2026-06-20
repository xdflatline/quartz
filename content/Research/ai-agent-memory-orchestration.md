---
title: "Research Index: AI Agent Memory & Orchestration"
detail: "This index collects concepts, tools, and patterns from recent discussions on:"
details: "This index collects concepts, tools, and patterns from recent discussions on:"
tags:
  - research
created: 2026-06-17
updated: 2026-06-17
type: research
---
# Research Index: AI Agent Memory & Orchestration

**Updated:** 2025-06-13
**Source:** Hacker News Discussions (June 2025) + DEV Community Benchmarks

---

## Overview

This index collects concepts, tools, and patterns from recent discussions on:
1. **Multi-agent orchestration in production** (HN Item 47660705)
2. **Memory layers for AI coding agents** (HN Item 46742800)
3. **Memori dual-mode memory layer** (HN Item 44821941, Show HN)
4. **Local LLM Hardware Requirements** (DEV Community, 2026 Benchmarks)

---

## Concepts

### Orchestration Patterns
- [[multi-agent-orchestration-patterns]] — Centralized coordinator, explicit task graphs, agent isolation
- [[typed-knowledge-architecture]] — Constraints/Decisions/Heuristics three-tier memory

### Memory & Learning
- [[agent-memory-layer-patterns]] — Typed knowledge, friction logging, human curation
- [[friction-logging-for-agents]] — Human correction rate as loss function proxy

### Local LLM Infrastructure
- [[llm-quantization-reference]] — Q4_K_M sweet spot, 6 quantization levels with GB/1B params
- [[ram-vs-vram-llm-inference]] — VRAM 10–30x faster; split = CPU speed; unified memory exception
- [[local-llm-hardware-requirements]] — Tiered recs: 8GB (1.5B), 16GB (7B sweet spot), 24GB+ GPU (32B)

---

## Tools & Projects

### Memory Layers
- [[memori-memory-layer]] — Dual-mode (SQL FTS), multi-agent internal, zero-config
- [[versanovatech]] — Commercial memory/learning layer

### Auto-Documentation
- [[squirrel-auto-docs]] — OSS auto-maintains `CLAUDE.md`/`agents.md` from agent activity

### Observability
- [[wayfound-ai]] — Production observability for multi-agent workflows

---

## Raw Sources

- [[hn-multiagent-orchestration-production.md]] — Full HN thread on production orchestration
- [[hn-memory-ai-coding-agents.md]] — Full HN thread on memory for coding agents
- [[devto-llm-local-ram-benchmarks-2026.md]] — DEV Community 2026 benchmarks for local LLM RAM/VRAM

---

## Key Threads

| Thread | Topic | Date | Items |
|--------|-------|------|-------|
| [47660705](https://news.ycombinator.com/item?id=47660705) | Multi-agent orchestration in production | Recent | Custom orchestrators, Redis/Mongo state, git worktrees |
| [46742800](https://news.ycombinator.com/item?id=46742800) | Memory for AI coding agents | Recent | Typed memory, friction logging, Squirrel |
| [44821941](https://news.ycombinator.com/item?id=44821941) | Memori Show HN | 10 months ago | Dual-mode memory, SQL FTS, multi-agent internals |
| [dev.to/...3kd2](https://dev.to/pavelespitia/how-much-ram-do-you-really-need-to-run-llms-locally-2026-benchmarks-3kd2) | Local LLM RAM/VRAM benchmarks | 2026 | Quantization table, hardware tiers, tok/s benchmarks |

---

## Cross-Cutting Themes

### Agent Architecture
1. **Roll Your Own** — Frameworks (LangGraph, CrewAI) deemed insufficient for production
2. **Explicit > Emergent** — Define task graphs, don't let agents self-decompose
3. **Structure Memory** — Flat text fails; typed buckets (constraints/decisions/heuristics) work
4. **Quantify Learning** — Friction metrics as proxy for human experience
5. **Human Curation Essential** — Agents can't judge what's worth remembering
6. **Observability First** — Log everything; eval frameworks required

### Local LLM Infrastructure
7. **VRAM is King** — GPU memory 10–30x system RAM; prioritize VRAM over RAM
8. **Q4_K_M is Default** — Universal sweet spot for quality/memory
9. **16GB RAM = Dev Sweet Spot** — Runs 7B models + tooling without GPU
10. **Apple Silicon Unique** — Unified memory eliminates RAM/VRAM split penalty

---

## Next Research Directions

### Agent Memory & Orchestration
- [ ] Evaluate Memori for integration feasibility
- [ ] Prototype typed knowledge architecture in Hermes
- [ ] Experiment with friction logging in agent delegation
- [ ] Compare Squirrel vs manual `CLAUDE.md` maintenance
- [ ] Benchmark SQL FTS vs vector stores for agent memory retrieval

### Local LLM Infrastructure
- [ ] Map Hermes agent workloads to hardware tiers (1.5B vs 7B vs 16B MoE)
- [ ] Test Q4_K_M vs Q5_K_M quality on coding tasks
- [ ] Evaluate Apple Silicon unified memory for Hermes local development
- [ ] Benchmark Ollama GPU offload performance on available hardware