---
title: Instruction-Driven Video Production

details: "Instruction-driven video production is the architectural pattern at the heart of OpenMontage. The AI agent is the orchestrator. Pipeline manifests (YAML) declare stages, tools, and quality gates. Stage director skills (Markdown) teach the agent HOW to execute each stage. Tools are thin Python BaseTool subclasses that do nothing on their own. The agent reads instructions, invokes tools, self-reviews, and checkpoints. There is no Python orchestrator, no Python reviewer, no Python handlers. The intelligence is in the skills, not in improvised code. Compared to LangGraph / CrewAI / AutoGen-style frameworks, instruction-driven systems make the production policy auditable, version-controllable, and editable by humans in plain text — without redeploying code. This is the same pattern as CLAUDE.md / AGENTS.md for coding agents, extended to video production."
tags:
  - concepts
created: 2026-07-02
updated: 2026-07-02
type: concept
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Instruction-Driven Video Production

**Pattern source:** [[OpenMontage]]

## Overview

Instruction-driven video production is the architectural pattern where the AI agent is the orchestrator and all production decisions live in declarative instructions (YAML manifests + Markdown skills), not in imperative code. The Python layer is reduced to thin, single-purpose tool executors that do nothing on their own — every creative decision, every review, every checkpoint transition happens in instructions the agent reads.

## The Core Loop

```text
Agent reads pipeline manifest (YAML)
  → reads stage director skill (MD)
  → uses tools (Python BaseTool subclasses)
  → self-reviews (meta skill)
  → checkpoints (Python utility)
  → presents to human for approval
```

## The Three-Layer Knowledge Stack

```
Layer 1: tools/ + pipeline_defs/    "What exists" — executable tools + YAML manifests
Layer 2: skills/                     "How to use it" — project conventions
Layer 3: .agents/skills/             "How the technology works" — external tech knowledge packs
```

Each tool's `agent_skills[]` field bridges Layer 1 → Layer 3. The agent MUST read the Layer 3 skill before calling the tool.

## Why This Pattern

- **Auditable** — every decision is in a versioned text file, not buried in code
- **Editable by humans** — non-engineers can change a `pipeline_defs/talking-head.yaml` without redeploying
- **Self-reviewing** — the meta-skill (`skills/meta/reviewer.md`) catches issues without code-side linting
- **Checkpointed** — every stage produces a JSON artifact (validated against `schemas/artifacts/`) so work survives session restarts
- **Bounded** — Rule Zero prevents ad-hoc Python; the agent cannot improvise past the manifest

## Compared to Other Agent Patterns

| Pattern | Orchestration | Intelligence Location |
|---|---|---|
| **LangGraph / CrewAI / AutoGen** | Code (DAGs, frameworks) | In the framework's runtime + your glue code |
| **OpenMontage** | Instructions (YAML + MD) | In the skills and manifests |
| **Hermes Agent** | Instructions (Markdown skills) | In skills and memory |

The same family of patterns powers Hermes Agent (skill files, `AGENTS.md`, `CLAUDE.md`) and the broader "agentic engineering" trend. The video production domain just makes the pattern explicit with YAML pipeline manifests instead of pure prose.

## Rule Zero (OpenMontage)

> *"Every video production request MUST go through the pipeline system. No exceptions."*

1. Identify the pipeline — match request to one in `pipeline_defs/`.
2. Read the pipeline manifest.
3. Run preflight — discover tools via registry.
4. Execute stage by stage, reading the stage director skill BEFORE doing any work.
5. Read Layer 3 skills before calling any tool.

**Do NOT** write ad-hoc Python scripts to call tools directly, skip the pipeline, or bypass preflight.

## Related

- [[agent-first-pipeline-architecture|Agent-First Pipeline Architecture (no Python orchestrator)]]
- [[capability-first-tool-design|Capability-First Tool Design (selector + provider)]]
- [[render-runtime-selection|Render Runtime Selection (Remotion vs HyperFrames vs FFmpeg)]]
- [[style-playbook|Style Playbooks (Design Tokens)]]
- [[OpenMontage]] — primary implementation
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
