---
title: "Ask HN: Thinking about memory for AI coding agents"

details: This thread discusses the implementation of persistent memory layers for AI coding agents. Users report that current methods for guiding AI agents—...
tags:
  - raw
created: 2026-06-13
updated: 2026-06-13
type: raw
---
# Ask HN: Thinking about memory for AI coding agents

**Source:** Hacker News (https://news.ycombinator.com/item?id=46742800)
**Date Retrieved:** 2025-06-13
**Type:** Community Discussion

---

## Summary

This thread discusses the implementation of persistent memory layers for AI coding agents. Users report that current methods for guiding AI agents—prompts and rules—are insufficient for long-term development.

---

## The Core Problem

- **Prompts:** Transient; disappear after each task
- **Rules:** Too narrow; often tied to specific files or patterns rather than project-wide logic
- **Context Pollution:** Long-term memory can overwhelm the model, while vague memory leads to poor performance
- **Deduplication:** Duplicate entries degrade retrieval quality

---

## Proposed Solutions & Frameworks

### 1. Typed Knowledge Architecture

Instead of flat text, categorize memory into distinct buckets to improve retrieval relevance:

- **Constraints:** Hard rules that must always be applied
- **Decisions:** Past choices with context on *why* they were made (e.g., "avoided this dependency because it caused X")
- **Heuristics:** Soft preferences used only when the task is ambiguous

> "Retrieval then becomes: constraints always injected, decisions pulled by similarity to current task, heuristics only when ambiguity is high." — dabaja

### 2. Empirical "Loss Functions"

To avoid the need for human-like emotions, developers can use "friction" metrics to help agents learn from mistakes:

- **Primary Metric:** Human correction rate (the most direct signal of a "bad path")
- **Secondary Metrics:** Iteration counts and revert frequency (noted as noisier/less reliable)
- **Implementation:** Log friction and weight memory retrieval based on past-friction-on-similar-tasks

### 3. Auto-maintained Documentation

Rather than manual upkeep of `CLAUDE.md` or `agents.md`, there is a push toward systems that auto-update documentation based on agent activity.

- **Experiment:** Squirrel (OSS experiment for auto-maintaining docs) — https://github.com/hakoniwaa/Squirrel

---

## Key Insights

- **Human-in-the-loop:** While agents are excellent at execution, they currently lack the judgment to decide *what* is worth remembering. Humans must curate the memory layer.
- **The "Why" vs. "What":** LLMs struggle with the nuance of software development because they lack the emotional experience of "bad hygiene" (the pain of fixing bugs). Using friction metrics acts as a proxy for this experience.
- **Deduplication Strategy:** One effective approach is hashing entries by `(topic, decision_type)` and forcing manual review when a collision occurs.

---

## Notable Mentions & Resources

- **Episodic Memory:** Beyond Vector Search: Why LLMs Need Episodic Memory — https://philippdubach.com/posts/beyond-vector-search-why-llms-need-episodic-memory/
- **Dev Logs:** Codeaholicguy - AI Devkit Experiment — https://codeaholicguy.com/2026/01/24/i-use-ai-devkit-to-develop-ai-devkit-features/
- **Tools:**
  - Versanova Tech (Memory and learning layer) — https://versanovatech.com
  - Squirrel (Auto-maintaining documentation) — https://github.com/hakoniwaa/Squirrel

---

## Summary of Best Practices

| Strategy | Benefit |
|----------|---------|
| **Typed Memory** | Prevents context pollution by injecting only relevant types |
| **Friction Logging** | Allows agents to "learn" from expensive mistakes without human intervention |
| **Manual Curation** | Ensures only high-value, non-duplicate information persists |
| **Standardized Files** | Using `CLAUDE.md` or `agents.md` remains a baseline for project-specific constraints |