---
title: "ThoughtDAG — GitHub README + docs/features.md + docs/setup.md"
details: "Verbatim extraction of the ThoughtDAG GitHub project README plus the full features.md and setup.md docs. ThoughtDAG is an MIT-licensed infinite-canvas LLM tool where reasoning structure is an editable thought graph; edges are context."
tags:
  - raw
  - llm
  - agent
  - tooling
  - knowledge-management
created: 2026-08-15
updated: 2026-08-15
type: raw
source: "https://github.com/chenxiachan/thoughtdag"
---

# ThoughtDAG — Repository Extraction

**Source:** GitHub (chenxiachan/thoughtdag) — README, docs/features.md, docs/setup.md
**Date Retrieved:** 2026-08-15
**Type:** Open-source project / Tool docs

---

## README — Tagline & Core Idea

> **Your thinking deserves a map.** An infinite canvas where LLM conversations grow into an editable thought graph. **Wires are the context.**

> *The graph is acyclic. You are the loop.*

> **Wires are the context.** What the model sees is exactly what wires into the node. Editing the graph edits the model's memory.

> *"The human in the loop, the model on the wires."* No autonomous agent redraws your graph.

**Stats:** ⭐ 112 · 🍴 17 · 410 commits · MIT · © 2026 Xia Chen

### Feature demonstrations (from README)

| Feature | Description |
|---------|-------------|
| ✂️ **Delete one edge, get a different answer** | Model sees only what wires in. Delete noise edge, ask again → clean answer. Reproducible in chapter ③ of the example canvas. |
| 📖 **Read a paper into a map** | Select a PDF passage, ask right there. Answer lands on canvas with page number; `p.N` chip jumps back to the page. |
| 💎 **Thinking condenses in your hands** | Merge nodes into higher conclusion; weave highlights into summary. Graph folds inward instead of sprawling. |
| 🖍️ **Passages marked, woven into cited prose** | Highlights are your judgment, not the model's. Check any subset and weave one passage where every sentence traces back. |
| 🗺️ **Zoom out: thinking becomes a map** | Three semantic tiers: full cards, takeaway plaques, icon skeleton. Every step badged ✕ ⚖ ↩ ?. Detours are part of the map. |

### Quick start

**Desktop app is the primary way to run ThoughtDAG.**

```bash
npm install
npm run server    # LLM proxy :3001
npm run dev       # → localhost:5173
# No .env? Connect any OpenAI-compatible endpoint inside the app
```

Hosted demo: `app.thoughtdag.workers.dev` (browser-based; example canvas works without a key — feature subset; keyless web search, direct-connection tools, and subscription bridge are desktop/local-only).

### Desktop binaries

| Platform | File |
|----------|------|
| macOS, Apple Silicon (M1+) | `ThoughtDAG-x.y.z-arm64.dmg` |
| macOS, Intel | `ThoughtDAG-x.y.z.dmg` |
| Windows | `ThoughtDAG.Setup.x.y.z.exe` |
| Linux | `ThoughtDAG-x.y.z.AppImage` |

- macOS builds signed & notarized by Apple.
- Windows builds NOT signed — choose "More info → Run anyway" on SmartScreen.
- In-app auto-update.
- Latest release: `1ce5f68` (2026-08-13) — "Consent belongs in the browser you live in"

### Capabilities matrix (README selection)

| Capability | What it does |
|------------|--------------|
| 📤 **Read-only share** | One link carries the whole graph; no account, no server storage |
| 🧭 **Staleness & replay** | Upstream edits mark invalidated answers; replay in dependency order, token estimate first |
| ✂️ **Clipping** | Select a passage or drag a rectangle in reader; becomes canvas material with page provenance |
| 🔌 **Any model** | Per-node pins; text-only models read images through companion text |
| 🔒 **Local-first** | Automatic folder backup writes real files; point at synced folder for cross-device |
| 📄 **DOCX support** | Word documents drop straight in (browser-side extraction via `mammoth`) |
| 🔌 **MCP tool ecosystem** | `@ai-sdk/mcp` clients connect at startup (stdio or remote); tools merge into same loop |
| 💾 **Cited prose** | Highlights woven into cited passages with reference numbers |
| 🎨 **Visual law** | SOLID = structural (conversation, layout, cascade); DASHED = bypass (reference, watch) |

Full feature list: 60+ features across all areas → `docs/features.md`.

### Models & subscriptions

**Providers:** Zhipu · Qwen · OpenAI · Anthropic · Google · DeepSeek · Kimi · OpenRouter · Ollama · any OpenAI-compatible endpoint.

**Subscription bridges:**
- ChatGPT plan → one-command local bridge (ThoughtDAG running locally)
- GLM Coding & Kimi Code → real API keys (pick preset, paste key, done)

**Vision handling:** Text-only models read already-indexed images through their companion text; unread images go to a vision model (announced).

### Cost & privacy

- ✅ Free model tier covers every feature; local Ollama runs fully offline
- ✅ Hosted demo: model traffic runs browser-direct — keys never touch the server
- ✅ PDFs never leave your machine; only extracted text travels when you ask
- ✅ Backup format stays backward compatible; Markdown export is the permanent escape hatch

### Tech stack

- **Frontend:** React 19, TypeScript
- **Build:** Vite
- **Canvas:** React Flow (infinite canvas)
- **Server:** Node.js (`server.mjs`) — LLM proxy on port 3001
- **Cloud/Edge:** Cloudflare Workers (hosted demo)
- **LLM SDK:** Vercel AI SDK (any OpenAI-compatible endpoint)

---

## docs/features.md — Extracted detail

### Core philosophy

> *"Chat terminals are harnesses for doing: they optimize for handing you an answer and hide everything else. ThoughtDAG is an instrument for thinking: the unit of value is the reasoning structure itself, kept legible, editable and repeatable."*

> *"Mind maps are drawn; this map grows. Chat leaves no map at all."*

> *"The graph is acyclic. You are the loop."*

**Key distinction:** Chat = hidden reasoning; ThoughtDAG = reasoning structure is the artifact.

### Canvas & context (One Rule system)

#### Context engine

- `buildContext()` walks all incoming edges, builds history in topological order
- Layered assembly: materials → reference blocks → conversation (ordering independent of wiring history — same graph = same prompt)

#### Edge types

| Edge | Color/Style | Behavior |
|------|-------------|----------|
| Continue | Purple | Inherits full ancestor context |
| Explore | Orange solid | Select text → branch right with selection as context |
| Reference | Dashed | Quoted without dragging in conversation; toggle quote ⇄ full |
| Reviewer | Sliding red | Critic role, auto-critiques each step |

> *Solid always means structural, dashed always means bypass (reference / watch).*

#### Reference edge details

- Depth is a first-class edge property
- Toggle quote ⇄ full on selected edge OR in panel's context tree
- Connect toast prices both options (silent when source has no chain)

#### Context management

- **Send preview**: live `~N tok · M messages · K files` + materials/references/conversation breakdown
- **Click-to-delete edges**: select edge → floating delete button (right-click menu too; Cmd+Z undoes)
- **Archive (prune-but-keep)**: dimmed, excluded from all context walks, restorable, batch via multi-select
- **Merge Synthesis**: box-select nodes → structured synthesis (conclusions / evidence / open questions)

#### Highlights

- Three downstream modes: Full text / Tag important / Highlights only
- Marks render across lists and tables
- Stale highlights auto-clean on edit
- All-highlights overview (by time / by node) with source-node pinpointing
- Export to Markdown; weave checked subsets into one cited passage

#### Node roles

- Per-node system prompt with three modes: inherit / set for next / reset here
- `appliedRole` recorded at generation time
- Radio picker for multi-parent conflicts
- Role library: built-ins + user-editable (editing built-in makes copy; restore anytime)
- Applied roles stay frozen on their nodes

### Reading & materials

#### PDF reader

- Original PDF rendering with selectable text layer (pdf.js)
- Select → ask lands branch node with `(p.N)` provenance
- Passage keeps anchor on page (highlight wash + bubble reopening thread)
- Canvas nodes carry `p.N` chip → jumps back to reader
- Extracted-text view for scanned PDFs
- Footer thread index tagging each conversation
- Per-material scroll memory

#### Annotation rail

- Answers stream beside document; follow-ups chain onto thread
- Selecting inside rail answer → explore (branch of THAT answer) or highlight
- Thread chips switch conversations; crosshair jumps to canvas

#### Reading loop

- Every response opens reading-size
- Select to highlight or branch from that passage
- Ask follow-ups below
- Viewer swaps to new node — whole chain of questions streams in place

#### Guided digest

- One click → material becomes short structured post in UI language
- `(p.N)` jump buttons back to original pages
- Digest = canvas node (versioned on rewrite, model-stamped, wireable downstream)
- Regenerating routes through digest prompt against full text

#### Content & recognition

- **Recognize (scanned PDFs)**: per-page vision rewrite to Markdown/LaTeX, editable
- **Content nodes**: notes (markdown), file nodes with PDF covers, link snapshots with timestamps
- **Image auto-reading**: picks strongest configured vision model
- **Material-first landing**: drop document → lands as material node with reader auto-opened

#### Attachments

- Node-local attachments (drag/paste/upload)
- Inherited include/exclude control
- Fingerprint dedup
- Automatic Vision switching for images
- PDFs feed context as extracted text + first-page cover on file nodes
- Attachments to root question stay behind explicit paperclip

### Map & review

#### Map mode (3 tiers with hysteresis)

1. Full cards → 2. Takeaway plaques → 3. Glyph seals (one icon per node)
- Seals and edges counter-scale to fixed screen size (map-pin style)
- Zooming out tightens map instead of shrinking it
- Nodes awaiting human input keep working form

#### Typed takeaways

- One conclusion-first line per answer version
- Auto-classified: ✕ ruled out · ⚖ decided · ↩ pivoted · ? open (insight unmarked)
- Display layer only — never enters context or fingerprints

#### Staleness & replay

- Invalidating an upstream node marks children
- Stale markers ride along; send-preview and replay are dependency-aware
- Replay panel: rerun in dependency order, token estimate first, batch live; per-step bandwidth allocatable

### Backups & sharing

- Folder backup writes real files (one `.json` per canvas); observer-side, not in-app
- Plain JSON; legacy and current share schema
- **Read-only share**: one URL hash carries full graph; no server storage
- Markdown export = permanent escape hatch
- Backups may be deleted like normal files; format stable across upgrades

### Other notable features

- **Per-node model pins** with per-provider overrides
- **Cookie-free hosting** (no analytics, telemetry, cookies, accounts)
- **Local-first privacy**: PDFs never leave the machine
- **Reading & writing keyboard-first** (arrows, ⌘Z undo, ↩ send)

---

## docs/setup.md — Extracted detail

### Quick start

**Fastest path**: Live demo (`app.thoughtdag.workers.dev`) — click Connect OpenRouter (free-tier models included), paste any provider key, or browse the example canvas.

**Local installation:**

```bash
npm install
npm run server         # LLM proxy
npm run dev            # → http://localhost:5173
```

**No config needed to start:** If `.env` has no key, the app prompts to connect a model interface. Keys stay in localStorage & proxy memory (never on disk).

### Supported models

Built on the **Vercel AI SDK**. Toolbar picker switches models at any time.

> **Image handling**: Text-only models keep the wheel when images appear — an already-read image participates through its companion text; only unread images hand the request to a vision model. Pasted images are auto-read once by the strongest vision model configured into editable companion text.

| Provider | Default models | `.env` key | Notes |
|----------|---------------|------------|-------|
| **Zhipu GLM** | glm-4.5-flash · glm-4v-flash | `ZHIPU_API_KEY` | Free, CN-direct; powers web search. Intl: use in-app Z.ai preset |
| **Qwen** (DashScope) | qwen-plus · qwen-vl-plus | `DASHSCOPE_API_KEY` | CN-direct |
| **OpenAI** | gpt-5.1 · gpt-5-mini | `OPENAI_API_KEY` | override via `OPENAI_MODELS` |
| **Anthropic** | claude-sonnet-5 · claude-haiku-4-5 | `ANTHROPIC_API_KEY` | override via `ANTHROPIC_MODELS` |
| **Google** | gemini-2.5-pro · gemini-2.5-flash | `GOOGLE_API_KEY` | override via `GOOGLE_MODELS` |
| **DeepSeek** | deepseek-v4-flash · deepseek-v4-pro | `DEEPSEEK_API_KEY` | text-only (reads images via companion text) |
| **Kimi** (Moonshot) | kimi-k2-turbo-preview · kimi-latest | `MOONSHOT_API_KEY` | CN-direct |
| **OpenRouter** | openrouter/auto | `OPENROUTER_API_KEY` | gateway to 300+ models |
| **Ollama** | (yours) | `OLLAMA_MODELS=qwen3:8b,…` | fully local & offline |

### Web search tiers

- OpenRouter interfaces have it built-in (`:online` variant)
- Local runs: AnySearch anonymous tier keyless (per-IP daily quota)
- GLM interface (free) becomes the engine when connected
- Scholarly search (arXiv + Semantic Scholar) needs nothing

### Subscriptions

#### ChatGPT Plan (Plus/Pro)

Connects through a community local bridge (`npx openai-oauth@latest` → `127.0.0.1:10531`). **Local only.** Risk warning: provider policy on third-party use can change; public reports of accounts suspended for third-party plan access.

#### GLM Coding Plan / Kimi Code

Real API keys against dedicated endpoints; pick preset, paste key, done.

---

## Related entries

- [[Entities/thoughtdag]]
- [[Concepts/wires-as-context-graph]]
- [[Research/canvas-based-reasoning-tools]]
