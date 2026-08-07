---
title: Agent-First Pipeline Architecture

details: "Agent-first pipeline architecture is the structural pattern behind OpenMontage. There is no central Python orchestrator, no Python reviewer, no Python handlers. The AI agent reads pipeline manifests (YAML) and stage director skills (Markdown), then uses tools (Python BaseTool subclasses) to actually generate assets. The system is structured as a state machine: idea → script → scene_plan → assets → edit → compose → publish. Each stage has a director skill that teaches the agent HOW. Checkpoint policy lives in the pipeline manifest (human_approval_default per stage) plus a meta-skill (skills/meta/checkpoint-protocol.md). Reviewer is a meta-skill (skills/meta/reviewer.md) — advisory only, max 2 rounds. Cost tracker (tools/cost_tracker.py) provides budget governance via estimate → reserve → reconcile. Canonical artifacts are validated against JSON schemas in schemas/artifacts/."
tags:
  - concepts
created: 2026-07-02
updated: 2026-07-02
type: concept
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Agent-First Pipeline Architecture (No Python Orchestrator)

**Pattern source:** [[OpenMontage]]

## Overview

Agent-first pipeline architecture is the structural pattern where the AI agent **is** the orchestrator. There is no central Python orchestrator, no Python reviewer, no Python handlers. Production logic lives in YAML manifests and Markdown skills the agent reads. Tools are thin `BaseTool` subclasses that do nothing on their own.

> "Python = tools + persistence. No orchestration logic, creative decisions, review logic, or checkpoint policy in Python code." — PROJECT_CONTEXT.md

## The Pipeline State Machine

```
idea → script → scene_plan → assets → edit → compose → publish
```

Each stage has a **director skill** (`skills/pipelines/<pipeline>/<stage>-director.md`) that teaches the agent HOW to execute that stage. The pipeline manifest (`pipeline_defs/<pipeline>.yaml`) declares stages, tools, quality gates, and human-approval defaults.

## Tool Contract

Every tool inherits from `tools/base_tool.py` and exposes:
- A name and description
- An input/output schema
- A `cost` and `latency_estimate`
- An `agent_skills[]` list pointing to Layer 3 knowledge packs

Tools are discovered at runtime via the tool registry:

```python
from tools.tool_registry import registry
import json
registry.discover()
print(json.dumps(registry.support_envelope(), indent=2))
print(json.dumps(registry.provider_menu(), indent=2))
```

## Checkpoint Policy

- **Declared in manifest** — `human_approval_default: true` per stage
- **Enforced by meta-skill** — `skills/meta/checkpoint-protocol.md`
- **Persisted as JSON** — `lib/checkpoint.py` writes/reads checkpoint files for resumable sessions

## Reviewer

- **Meta-skill** — `skills/meta/reviewer.md`
- **Advisory only** — the human makes the final call
- **Max 2 rounds** — prevents infinite critique loops
- **Multi-point self-review** — `ffprobe`, frame sampling, audio analysis, delivery-promise verification, subtitle checks

## Cost Governance

`tools/cost_tracker.py` provides budget governance via:
1. `estimate` — preflight cost projection
2. `reserve` — commit budget before generation
3. `reconcile` — match actual spend to reservation

## Why This Architecture

- **Decoupled** — agents, tools, and skills can evolve independently
- **Swappable** — a new provider just adds a tool; the agent discovers it
- **Auditable** — every decision is in versioned text, not code paths
- **Bounded** — Rule Zero prevents ad-hoc workarounds
- **Testable** — contract tests on artifacts, QA integration tests on tool outputs

## Related

- [[instruction-driven-video-production|Instruction-Driven Video Production]]
- [[capability-first-tool-design|Capability-First Tool Design]]
- [[render-runtime-selection|Render Runtime Selection]]
- [[style-playbook|Style Playbooks]]
- [[OpenMontage]] — primary implementation
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
