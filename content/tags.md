---
title: "Tag Index"
details: "The controlled tag vocabulary for the Quartz wiki. Each tag below has a scope, a when-to-use description, and a when-NOT-to-use description. Before introducing a new tag, check this page first; if a suitable tag exists, reuse it. Tags here are top-level categorical (llm, agent, tooling, schweiz) — they are NOT product names (no 'qwen', no 'claude-code', no 'gpt-4') and they are NOT specific concepts (no 'harness-engineering', no 'recursive-self-improvement'). For those, use wikilinks in the body of the page."
tags:
  - tags
  - index
  - wiki
created: 2026-08-07
updated: 2026-08-07
type: index
---

# Tag Index

The controlled tag vocabulary for the Quartz wiki. Before introducing a new tag, check this page first; if a suitable tag already exists, reuse it. Only invent a new tag when no existing tag fits.

## How to use this page

1. Pick a tag from the vocabulary below.
2. If none fits, propose a new tag — but first check whether the **wikilink** in the body of the page already covers the relationship. Tags are for **filtering and discovery**; wikilinks are for **relationships**.
3. Tags are **lowercase**, **singular** when the noun is uncountable (e.g. `tooling`, `wiki`, `protocol`), and **kebab-case** when multi-word (e.g. `agentic-system`, `knowledge-management`).
4. Tags are **NOT** product names. A page about Qwen3.5 gets `llm` (or `quantization` if it's about the quantized model), not `qwen`.
5. Tags are **NOT** specific concepts. A page about harness engineering gets `agent` and `harness`, not `harness-engineering`. The wikilinks in the body cover the specific concept.
6. Tags are **NOT** types (`raw`, `concept`, `entity`, `research`). The `type:` frontmatter field carries that information.

## LLM / ML

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `llm` | Pages about large language models in general, model families, model benchmarks, model cards | Specific model names (use `llm` for the family; wikilink the model in the body) |
| `quantization` | Pages about quantization schemes, GGUF, QAT, QLoRA, mobile quantization | Pages that just happen to mention a quantized model in passing |
| `inference` | Pages about inference systems, vLLM, batching, latency optimization | Pages that are mainly about training |
| `local-llm` | Pages about running LLMs on local hardware (CPU, Apple Silicon, consumer GPUs) | Pages about cloud inference providers |
| `rag` | Pages about retrieval-augmented generation patterns, vector search grounding, document chunking | Pages that mention RAG as one tool among many |
| `embedding` | Pages about embedding models, vector spaces, semantic search | Pages that just use embeddings under the hood |
| `fine-tuning` | Pages about LoRA, QLoRA, supervised fine-tuning, continued pretraining | Pages that fine-tune as one step in a larger pipeline |
| `training` | Pages about training methods in general (pre-training, RL, GRPO, SFT) | Pages that are mainly about inference or serving |
| `benchmark` | Pages about evaluating LLMs/agents (PaperBench, MLE-bench, KernelBench, RE-Bench) | Pages that report a single benchmark result |
| `evaluation` | Pages about eval methodology, LLM-as-judge, eval harnesses | Pages that happen to include an eval section |

## Agent

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `agent` | Pages about LLM-powered agents in general (autonomy, planning, tool use) | Pages that just mention "agent" in passing |
| `agentic-system` | Pages about multi-agent systems, agent orchestration, AHE, Meta-Harness | Pages about a single agent (use `agent`) |
| `mcp` | Pages about Model Context Protocol, MCP servers, MCP tool integration | Pages that just expose an MCP server as one feature |
| `tooling` | Pages about tools, tool calls, tool taxonomies, sandboxed execution | Pages that are mainly about a specific tool (use wikilink in the body) |
| `orchestration` | Pages about agent orchestration, coordinator/worker patterns, DAG-based workflows | Pages about a single-agent loop |
| `multi-agent` | Pages about multi-agent collaboration, role specialization, inter-agent communication | Pages about a single agent |
| `memory` | Pages about agent memory (short-term, long-term, episodic, semantic) | Pages that are mainly about a memory product |
| `context-engineering` | Pages about context management, ACE, MCE, scratchpads | Pages that are mainly about prompt engineering |
| `prompt-engineering` | Pages about prompt design, prompt templates, instruction following | Pages that are mainly about context or memory |
| `harness` | Pages about the harness layer, self-improving harnesses, harness engineering | Pages that are mainly about the model itself |

## Code / Dev

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `coding-agent` | Pages about coding agents (Claude Code, Codex, OpenCode, Cursor, Aider) | Pages that use a coding agent as a tool (no tag, just wikilink) |
| `runtime` | Pages about agent runtimes, process managers, VM-based sandboxes | Pages about a specific runtime instance (use wikilink) |
| `cli` | Pages about command-line tools, terminal UIs, REPLs | Pages that have a CLI as one feature among many |
| `sdk` | Pages about software development kits, API libraries | Pages that are mainly about a CLI |
| `kernel` | Pages about Linux kernel, syscalls, kernel-level isolation, eBPF | Pages that mention "kernel" in a different sense |
| `kubernetes` | Pages about K8s, k8s operators, k8s resource management | Pages that happen to deploy to k8s |
| `serverless` | Pages about serverless compute, FaaS, Lambda-style execution | Pages that use serverless as one option |
| `infrastructure` | Pages about cloud infrastructure, GPU providers, cost optimization | Pages that are mainly about a specific provider (use wikilink) |

## Knowledge / Wiki

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `wiki` | Pages about the wiki itself, Quartz, Obsidian, digital gardens | Pages that just happen to live in the wiki (no tag) |
| `protocol` | Pages about protocols (wiki ingest protocol, communication protocols) | Pages that are about a specific protocol instance (use wikilink) |
| `schema` | Pages about data schemas, YAML frontmatter, type definitions | Pages that are about a single schema (use wikilink) |
| `ingestion` | Pages about ingesting external content into the wiki | Pages that just happen to have been ingested (no tag) |
| `knowledge-management` | Pages about second brains, Zettelkasten, knowledge graphs | Pages that are about a specific tool (use wikilink) |
| `tags` | Pages that are tag indexes or about the tag taxonomy itself | (only on this page) |

## Format / Type

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `tutorial` | Pages that walk through a procedure step by step | Pages that describe a concept without steps |
| `reference` | Pages that are pure reference material (API docs, configuration tables) | Pages that mix reference and tutorial |
| `guide` | Pages that guide a procedure but aren't step-by-step | Pages that are pure concept or entity |
| `comparison` | Pages that compare multiple things side by side | Pages that are mainly about one thing |
| `index` | Pages that aggregate or index other pages (this page, the Workflows index, etc.) | Pages that are content-bearing |
| `survey` | Pages that survey a field or a set of papers (e.g. Lilian Weng's harness engineering post) | Pages that focus on one paper or one idea |
| `architecture-pattern` | Pages about a reusable architectural pattern | Pages about a specific instance (use wikilink) |

## Media

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `video` | Pages about video generation, video workflows, video backends (ComfyUI, Wan, OpenMontage) | Pages that just mention video as one capability among many |

## Source

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `blog-post` | Raw pages ingested from blog platforms (lilianweng.github.io, dev.to, etc.) | Pages that are original wiki content (use `type: research` or similar) |
| `paper` | Raw pages ingested from arXiv, Nature, ICML, etc. | Pages that summarize a paper (use `survey` or `type: research`) |
| `documentation` | Raw pages ingested from official docs (GitBook, Mintlify, vendor docs) | Pages that are about a doc (use `reference`) |
| `github-readme` | Raw pages ingested from GitHub READMEs | Pages that are about a GitHub project (use wikilink) |
| `hn-discussion` | Raw pages ingested from Hacker News discussions | Pages that are about HN (no tag) |

## Lifestyle / Geography

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `schweiz` | Pages about Switzerland in general (shopping, travel, tax, etc.) | Pages about a specific Swiss canton (use the canton name) |
| `niederlande` | Pages about the Netherlands in general | Pages about a specific Dutch city (use the city name or wikilink) |
| `zürich` | Pages specifically about Zürich | Pages about other Swiss cantons |
| `shopping` | Pages about buying things, product comparisons, receipts | Pages that are about a specific shop (use wikilink) |
| `wohnen` | Pages about housing, apartments, decor | Pages that are about a specific residence (no tag) |
| `kinderzimmer` | Pages about children's rooms, kids' products | Pages that just mention kids in passing |
| `aufbewahrung` | Pages about storage, organization, containers | Pages that are about a specific product (use wikilink) |
| `deko` | Pages about decoration, aesthetics | Pages that are about a specific decor item |
| `reise` | Pages about travel, day trips, itineraries | Pages that are about a specific location (use wikilink) |

## Topic (Schweiz / Recht / Einkauf)

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `recht` | Pages about legal topics (tax, inheritance, customs) | Pages that just mention a law in passing |
| `zoll` | Pages about customs, import/export duties | Pages about domestic purchases |
| `erbschaft` | Pages about inheritance, estate planning | Pages that mention inheritance in passing |
| `hypothek` | Pages about mortgages, property financing | Pages that are about buying a house (use `wohnen`) |
| `mehrwertsteuer` | Pages about VAT, sales tax | Pages about other taxes (use `recht`) |
| `lebensmittel` | Pages about food, groceries, recipes | Pages about a specific food product (use wikilink) |
| `käse` | Pages about cheese specifically (import, varieties, pairings) | Pages that are about general food (use `lebensmittel`) |
| `einfuhr` | Pages about importing things into Switzerland | Pages about exports or domestic-only purchases |

## Other

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `housekeeping` | Pages about wiki maintenance, schema migrations, tag normalization | Pages that are content-bearing |
| `plan` | Pages that are plans or in-progress task lists | Pages that are finished work |

## OS / Desktop

| Tag | Use for | Don't use for |
|-----|---------|---------------|
| `linux` | Linux-specific tooling, Linux ecosystem pages (distros, package managers, Wayland compositors, Linux-only apps) | General cross-platform tools that happen to support Linux |
| `desktop` | Desktop environment / shell composition, status bars, widgets, lockscreens, display managers, GUI panel/window managers | Pages about general GUI frameworks with no shell focus (use `tooling`) |
| `qt` | Pages about Qt, QML, QtQuick, the Qt ecosystem, qmlls language server | Pages that just embed a Qt control without discussing Qt |
| `widget` | UI widgets, status bars, system tray items, lockscreen widgets, panel components | Pages about general UI design with no widget/component focus |

## Reserved / Out of use

These tags appeared in the wild but are not in the controlled vocabulary. Pages that use them should be retagged during housekeeping (T3.4):

- `concepts`, `entities`, `raw`, `research` — these are the **tier** of the page; the `type:` frontmatter field already carries this. The tags are kept for backwards-compat and search but should NOT be the only tag on a page.
- `entitie` (typo, 53 files) — should be `entity` (the `type:` value); the **tag** itself should be `entities` (the tier tag).
- Product-name tags that may have leaked in (`qwen`, `claude-code`, `mastra`, `mezmo-aura` as tags rather than wikilinks) — should be replaced with `llm`, `coding-agent`, or `tooling`.

## Adding a new tag

When no existing tag fits, propose a new one by adding a row to the appropriate table above. The new tag must:

1. Be **lowercase** and **kebab-case** if multi-word
2. Be a **category** (not a specific thing) — e.g. `quantization` is a category, `gguf-q4` is a specific thing
3. Be a **plural** if the noun is naturally countable (e.g. `benchmarks`) — though the current vocabulary is mostly singular; consistency is more important than the rule
4. Have a **non-empty "Use for"** column entry
5. Have a **non-empty "Don't use for"** column entry that helps future agents avoid tag drift

After adding a tag, **commit this page with a state transition** per the plan's commit cadence.
