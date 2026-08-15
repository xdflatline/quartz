---
title: "ThoughtDAG"
details: "MIT-licensed open-source desktop + web app (React 19, React Flow, Vercel AI SDK) that turns LLM conversations into an editable, acyclic thought graph on an infinite canvas; edges are the model's context."
tags:
  - entity
  - llm
  - agent
  - tooling
  - knowledge-management
created: 2026-08-15
updated: 2026-08-15
type: entity
sources:
  - .Raw/github-thoughtdag-readme-2026-08-15.md
---

# ThoughtDAG

**Source:** [[Raw/github-thoughtdag-readme-2026-08-15.md]]
**Category:** Tool / Open-source project
**Repository:** https://github.com/chenxiachan/thoughtdag
**Website:** https://chenxiachan.github.io/thoughtdag/
**Author:** Xia Chen (2026) · MIT · 112 stars · 410 commits

---

## Overview

ThoughtDAG is an infinite-canvas LLM tool where reasoning structure is the artifact. Instead of a chronological chat transcript, the user arranges nodes and edges on a canvas; each node is one model call, and **what the model sees is exactly what wires into the node**. Editing the graph edits the model's memory. The human is the loop ("the graph is acyclic; you are the loop"); no autonomous agent redraws the graph.

It is positioned against chat terminals ("harnesses for doing") as an "instrument for thinking," closer to a reasoning IDE than a chatbot.

## Key Details

### Product shape

- **Desktop app** is the primary surface — `.dmg` (signed/notarized), `.exe`, `.AppImage`. Bundles local LLM proxy (`server.mjs` on `:3001`); no Node or terminal needed.
- **Hosted demo** at `app.thoughtdag.workers.dev` (Cloudflare Workers) — feature subset (keyless web search, direct-connection tools, subscription bridge are desktop/local-only).
- **Local-first privacy:** PDFs never leave the machine; only extracted text travels when asked.
- **Local-first backup:** writes one `.json` per canvas to a chosen folder (observer-side, not in-app).

### Runtime stack

| Layer | Tech |
|-------|------|
| UI | React 19, TypeScript |
| Build | Vite |
| Canvas | React Flow (infinite canvas) |
| Server | Node.js (`server.mjs`) — LLM proxy on port 3001 |
| Cloud | Cloudflare Workers (hosted demo) |
| LLM SDK | Vercel AI SDK + any OpenAI-compatible endpoint |
| MCP | `@ai-sdk/mcp` clients (stdio or remote) merged into same tool loop |

### Model coverage

Nine provider presets: Zhipu GLM, Qwen (DashScope), OpenAI, Anthropic, Google, DeepSeek, Kimi (Moonshot), OpenRouter, Ollama — plus any OpenAI-compatible custom endpoint. Per-node model pins; free tier (Zhipu GLM, AnySearch) covers every feature. Text-only models read indexed images through their companion text; unread images hand off to a vision model.

### Subscription bridges

- **ChatGPT Plus/Pro** through community local bridge `npx openai-oauth@latest` (local-only, account-policy risk).
- **GLM Coding** and **Kimi Code** plans via real API keys against dedicated endpoints.

### The one-rule context system

- **`buildContext()`** walks incoming edges in topological order, lays down materials → references → conversation. Same graph ⇒ same prompt, independent of how it was drawn.
- **Four edge kinds:** Continue (purple), Explore (orange, carries selection as seed), Reference (dashed, depth-first, toggleable quote ⇄ full), Reviewer (critic role).
- **Archive ≠ delete:** archived edges dim and drop out of all context walks but stay restorable, batch-able.
- **Send preview:** live token / message / file count before every send.

### Canvas-native reading

- PDF reader (pdf.js) with selectable text layer; `Recognize` rewrites scanned pages to Markdown/LaTeX.
- Annotation rail streams answers beside the document; follow-ups chain onto the same thread; `p.N` chips jump back to the page.
- Guided digest turns a material into a structured post (itself a canvas node, versioned).
- Document formats: PDF, DOCX (`mammoth` browser-side), link snapshots with timestamps.

### Map & replay

- **Three-tier map mode** with hysteresis: full cards → takeaway plaques → glyph seals; counter-scale so the map tightens instead of shrinking on zoom-out.
- **Typed takeaways** auto-classified: ✕ ruled out · ⚖ decided · ↩ pivoted · ? open.
- **Staleness & replay:** invalidating an upstream node marks children; replay runs in dependency order with live token estimate.
- **Read-only share:** one URL hash carries the full graph; no server storage.

### Quantified scope

- 60+ features grouped by area (`docs/features.md`).
- 410 commits on `main` (Aug 2026 cut).
- Latest release `1ce5f68` (2026-08-13) — "Consent belongs in the browser you live in."

## Related Concepts

- [[Concepts/wires-as-context-graph]] — ThoughtDAG's defining architecture: edges carry the prompt, not messages.
- [[Concepts/graph-based-workflow-engine]] — adjacent lineage of canvas/DAG workflow tools.
- [[Research/canvas-based-reasoning-tools]] — index page covering canvas reasoning instruments.

## References

- Raw Article: [[Raw/github-thoughtdag-readme-2026-08-15.md]]
- Original: https://github.com/chenxiachan/thoughtdag
- Features docs: https://raw.githubusercontent.com/chenxiachan/thoughtdag/main/docs/features.md
- Setup docs: https://raw.githubusercontent.com/chenxiachan/thoughtdag/main/docs/setup.md
