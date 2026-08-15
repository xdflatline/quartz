---
title: "Research Index: Canvas-Based Reasoning Tools"
details: "Research index covering open-source canvas tools that turn LLM reasoning into editable, traversable graphs rather than chat transcripts — anchored by ThoughtDAG and the wires-as-context graph architecture pattern."
tags:
  - research
  - llm
  - agent
  - tooling
  - knowledge-management
  - index
created: 2026-08-15
updated: 2026-08-15
type: index
sources:
  - .Raw/github-thoughtdag-readme-2026-08-15.md
---

# Research Index: Canvas-Based Reasoning Tools

**Updated:** 2026-08-15
**Source:** ThoughtDAG GitHub repo (README + docs/features.md + docs/setup.md), retrieved 2026-08-15.

---

## Overview

This index tracks tools and patterns that move LLM use **out of the chat transcript** and **into an editable canvas / graph**, where the reasoning structure itself is a first-class artifact the user can manipulate. The anchoring reference is ThoughtDAG (Xia Chen, MIT, 2026) and its defining pattern *wires-as-context graph*. Adjacent work — DAG runtime orchestration, graph workflow engines — is cross-referenced but lives in a different category (it runs the scheduler; the canvas tools let the human run it).

## Concepts

### Canonical architecture pattern

- [[Concepts/wires-as-context-graph]] — Each node's prompt is assembled by walking incoming edges in topological order; edges are the context. Same graph ⇒ same prompt.

### Adjacent / lineage

- [[Concepts/coordinator-worker-task-dag-orchestration]] — Closed-loop DAG orchestration; contrast: scheduler runs it, context comes from task results.
- [[Concepts/graph-based-workflow-engine]] — Broader category of graph workflow engines (e.g. workflow canvas products); wires-as-context is the LLM-specific instantiation.

## Tools & Projects

### Open-source

- [[Entities/thoughtdag]] — Infinite-canvas LLM tool (React 19 + React Flow + Vercel AI SDK, MIT). The primary shipped implementation of the wires-as-context pattern; desktop app + Cloudflare-hosted demo. 112 stars / 410 commits as of Aug 2026.

## Raw Sources

- [[Raw/github-thoughtdag-readme-2026-08-15.md]] — Verbatim extraction of ThoughtDAG's README, full `docs/features.md`, and `docs/setup.md` (2026-08-15).

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [chenxiachan/thoughtdag README](https://github.com/chenxiachan/thoughtdag) | ThoughtDAG tagline + quick start + desktop binaries | 2026-08-13 | "Wires are the context," one-rule system, MCP hooks |
| [thoughtdag/docs/features.md](https://raw.githubusercontent.com/chenxiachan/thoughtdag/main/docs/features.md) | Full feature deep-dive (60+ features) | 2026-08 | Edge taxonomy, context engine, map mode, staleness & replay |
| [thoughtdag/docs/setup.md](https://raw.githubusercontent.com/chenxiachan/thoughtdag/main/docs/setup.md) | Providers, subscriptions, web search tiers | 2026-08 | 9 providers incl. Ollama; ChatGPT/GLM/Kimi subscription bridges |

## Cross-Cutting Themes

### Reasoning structure as the artifact

1. **Reasoning ≠ transcript.** Chat optimizes for "answer in hand, everything else hidden" (ThoughtDAG's framing of "harnesses for doing"). Canvas tools treat the reasoning graph as the deliverable.
2. **Topological determinism.** Wires-as-context graphs use topological ordering, not chronological insertion, so the same graph yields the same prompt regardless of drawing order. This is what makes "edit and re-send" meaningful rather than racy.
3. **Visual encoding is the API.** Solid vs. dashed edges; takeaway badges (✕ ⚖ ↩ ?); tiered map mode with hysteresis. The user predicts behavior from the canvas, not from a config panel.

### Local-first privacy defaults

1. **PDFs stay local**; only extracted text travels. Browser-side DOCX via `mammoth`. Client-side vision OCR for scanned pages.
2. **No accounts, no telemetry, no cookies** on the hosted demo (Cloudflare Workers); browser-direct model traffic so keys never touch the server.
3. **Backup = real files.** One JSON per canvas written to a folder the user owns; observer-side, not in-app — compatible with synced folders (Syncthing, iCloud Drive, etc.).

### Model-as-router

1. **Any OpenAI-compatible endpoint** via the Vercel AI SDK; nine named presets plus custom. Per-node pins keep the choice where it matters.
2. **Subscription bridge pattern.** Where plan APIs include an OAuth path (ChatGPT), a *local-only* community bridge injects auth; where plans issue real keys (GLM Coding, Kimi Code), a preset captures the preset endpoint.
3. **Free tier covers every feature.** Zhipu GLM flash models (free with CN-direct or Z.ai international twin) plus Ollama for fully-offline use.

### MCP / tools without leaving the loop

1. **MCP clients** (`@ai-sdk/mcp`, stdio or remote) connect at startup and merge into the same tool loop — no separate "agent mode" needed.
2. **Web search as a togglable tier** rather than a separate product; scholarly search (arXiv + Semantic Scholar) keys-free.

## Open Questions Worth Investigating

- **Cross-project portability.** ThoughtDAG's share link carries the *whole graph in one URL hash*. What are the compression limits, and how does this scale to 1000+ node graphs?
- **Replay economics.** Staleness & replay runs in dependency order with a token estimate first — what is the empirical replay cost on multi-branch research canvases?
- **Map-mode cognition.** Three semantic tiers (cards → plaques → seals) with hysteresis is a strong UI bet. How do users actually navigate large reasoning maps; does the typed takeaway badge (✕ ⚖ ↩ ?) help or become noise?
- **MCP × canvas.** MCP clients merge into the same loop; do they need edge-aware context too, or do tool calls break the wires-as-context invariant?

## Next Research Directions

- [ ] **Prototype a wires-as-context variant in a tiny harness** — extract `buildContext()` semantics into a Python tool that walks incoming edges in topo order and emits the prompt; compare determinism to a transcript baseline.
- [ ] **Benchmark replay cost** — generate a 50-node branching canvas with intentional invalidations, measure replay tokens vs cold re-run, characterize the staleness marking overhead.
- [ ] **Survey the canvas-reasoning neighborhood** — search for other "thinking as canvas" products (tldraw-based, OpenMontage-style) and tag which ones exhibit wires-as-context vs. transcript-replay.
- [ ] **Test MCP and wires-as-context interaction** — stand up a small MCP server with a state-changing tool and run it from a ThoughtDAG-style local clone, observe whether tool outputs need a new edge type (e.g. "side-effect" edge) to keep the context invariant clean.
