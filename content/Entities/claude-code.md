---
title: "Claude Code"

details: "Claude Code is Anthropic's agentic coding assistant: a CLI / TUI that runs in the terminal, can read and edit files, run shell commands, and orchestrate subagents. In the Second Brain, Claude Code is the LLM agent that sits at the center of the architecture — the only 'big purple' in the colour-coded diagram. Its role is bounded by the [[Concepts/brain-first-search-ladder]] rulebook loaded from `CLAUDE.md` at every startup. It is the writer for the [[Concepts/ai-curated-knowledge-wiki]] ingest (maintaining `09 Wiki/` under schema), the executor of the build tasks in the [[Concepts/six-step-ai-build-process]], the sparring partner in the Create phase of the [[Concepts/capture-process-connect-create-workflow]], and the generator of rung-5 responses on the Brain-First ladder. The Node AI's framing: 'the decisive thing is not the AI, it is its rulebook'. Claude Code is the load-bearing component only at the response-generation step; everything else in the architecture is deterministic. Cost: ~$20/month for the Pro plan; per-task costs depend on usage but the local-search path never spends a token."
tags:
  - entities
  - coding-agent
  - agent
created: 2026-07-25
updated: 2026-07-25
type: entity
source: "[[Raw/thenodeai-second-brain-architecture-2026-07-25]]"
sources:
  - "Raw/thenodeai-second-brain-architecture-2026-07-25"
---

# Claude Code

**Category:** Tool / Agentic coding CLI
**Vendor:** Anthropic
**Platform:** Terminal (CLI / TUI), with sidebar plugins for editors (e.g. Claudian for Obsidian)
**Pricing:** Subscription ~$20/month (Pro plan as of the video)

---

## Overview

Anthropic's agentic coding assistant: a CLI / TUI that runs in the terminal, can read and edit files, run shell commands, and orchestrate subagents. In the Second Brain, Claude Code is the LLM agent that sits at the center of the architecture — the only "big purple" in the colour-coded diagram.

## The role in the Second Brain

The Node AI's framing: "the decisive thing is not the AI, it is its rulebook." Claude Code's job in the Second Brain is bounded by the rulebook loaded from `CLAUDE.md` at every startup. The rulebook encodes the [[Concepts/brain-first-search-ladder]] (5 rungs of retrieval) and the [[Concepts/ai-curated-knowledge-wiki]] schema. With that rulebook, Claude Code becomes:

- The writer for the wiki ingest. It maintains `09 Wiki/` under the schema's rules; the human does not touch the wiki.
- The executor of the build tasks in the [[Concepts/six-step-ai-build-process]]. For each of the 14 core tasks, a fresh Claude Code subagent is deployed with the task and the needed context.
- The sparring partner in the Create phase of the [[Concepts/capture-process-connect-create-workflow]]. It is *not* a ghostwriter; the user brings the intent, the AI brings the candidate phrasing.
- The generator of rung-5 responses on the Brain-First ladder. Rungs 1-4 are deterministic; rung 5 is the only place Claude Code is load-bearing on the read path.

## What it is not in the Second Brain

- Not the source of truth. The vault is the truth; Claude Code reads and writes it under rules.
- Not required to start. The [[Concepts/deterministic-first-architecture]] rule says: with no API key, the system should still work. The vault, the indexer, QMD, and the web app all work without Claude Code. Claude Code is the upgrade, not the foundation.
- Not the search engine. The hybrid search is QMD. Claude Code calls QMD at rung 3; it does not search itself.

## Where it is invoked

The Node AI's three-surface rule for the [[Concepts/ai-curated-knowledge-wiki]] ingest:

1. **Terminal** — direct CLI invocation. The most flexible; the most friction.
2. **Claude Code app (TUI)** — interactive session. The middle ground.
3. **Obsidian with the Claudian plugin** — Claude Code as a sidebar in the editor. Everything in one window.

The Node AI's specific recommendation for a single workflow: Obsidian + Claudian + Claude Code, so the editor, the AI, and the wiki are all visible at once. The ingest does *not* run in the web app; that is a conscious design decision (the web app is a pure read surface).

## The cost model

The Node AI's number: ~$20/month for the Claude Pro plan. The local-search path never spends a token (QMD runs on-device). Tokens are spent only at:

- The wiki ingest (one LLM call per source for restructuring + conflict detection)
- The Brain-First rung 5 (one LLM call per question to generate the response)
- The Create phase of the workflow (one LLM call per produced artefact)

In the speed-test benchmark (5 real workday questions), the Brain variant used 50% fewer tokens and 40% less time than vanilla Claude Code because the Brain-First ladder kept the context small. A single worst-case question cost >500K tokens without the Brain; the same question cost ~1/3 of that with the Brain.

## How it relates to the [[Concepts/six-step-ai-build-process]]

The Superpowers skill ([[Entities/superpowers]]) is a Claude Code skill that operationalises the build process. With Superpowers installed, Claude Code is forbidden from writing code before the brainstorming, specification, and plan steps are complete and approved. The Node AI's Second Brain was built end-to-end with Superpowers, and he credits the skill rather than the model for the success of the build.

## Related Concepts

- [[Concepts/brain-first-search-ladder]] — the rulebook Claude Code reads at startup
- [[Concepts/ai-curated-knowledge-wiki]] — Claude Code is the wiki writer
- [[Concepts/six-step-ai-build-process]] — Claude Code is the build executor
- [[Concepts/deterministic-first-architecture]] — Claude Code is the smallest purple, not the foundation
- [[Concepts/capabilities-first-system-design]] — the rules implement the capabilities

## References

- Raw Article: [[Raw/thenodeai-second-brain-architecture-2026-07-25]]
- Original: https://m.youtube.com/watch?v=mHSOsy_usAg
