---
title: "Karpathy autoresearch"

details: "Referenced in [[Raw/lilianweng-harness-engineering-2026-07-04]] as a clean example of a workflow-automation harness: the model can operate, test, and iterate on its own work in a goal-oriented loop. The repository provides a minimal scaffold that a harness designer can fork to prototype a research-loop workflow."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://github.com/karpathy/autoresearch
---

# Karpathy autoresearch

**Source:** <https://github.com/karpathy/autoresearch>
**Author:** [[Entities/andrej-karpathy]]

## Overview

Andrej Karpathy's open-source reference implementation of an autonomous-research workflow loop. The repo provides a minimal scaffold for the **plan → execute → observe/test → improve → repeat** pattern that Weng names as Pattern 1 of her harness taxonomy.

## What It Demonstrates

- A goal-oriented loop the model can operate, test, and iterate within
- Proactive user requests for clarity in task specification or execution preference
- Iteration on trajectories and failure cases through an "agent runtime" rather than a static prompt template

## How It Differs from a Coding Agent

Karpathy's autoresearch is a **workflow scaffold**, not a full coding agent. It does not ship a tool belt; it ships a loop structure. Coding-agent harnesses (Claude Code, Codex, OpenCode) can be wrapped around autoresearch's loop, or autoresearch's loop can be used as the inner pattern of a larger harness.

## Related

- [[Concepts/harness-as-runtime-os-analog]] — the broader harness framing
- [[Concepts/coding-agent-tool-taxonomy]] — the tool groups that wrap such loops
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
