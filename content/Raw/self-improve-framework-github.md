---
title: "Self-Improve: Pluggable AI Agent Evolution System"

details: A production-ready self-evolution system for AI agents that automatically learns from mistakes, corrections, and feedback to continuously improve e...
tags:
  - raw
  - agent
  - github-readme
created: 2026-05-25
updated: 2026-05-25
type: raw
source_url: "https://github.com/don068589/self-improve"
ingested: 2026-05-25
sha256: dc95cda4ff42f6e32a2e64b8965af6fbf4243d0a686aca933ef01f1601da15b7
---
# Self-Improve: Pluggable AI Agent Evolution System

A production-ready self-evolution system for AI agents that automatically learns from mistakes, corrections, and feedback to continuously improve execution quality.

## Features

- **Automated Memory Scanning**: Scans agent memory logs and transcripts to extract learning signals.
- **Rule Extraction and Classification**: Identifies repetitive patterns, extracts reusable rules, and groups them by theme.
- **Three-Tiered Memory Management (HOT/WARM/COLD)**:
  - **HOT**: Frequently used active rules (<= 100 lines) stored in `data/hot.md`.
  - **WARM**: Theme-based rules (<= 200 lines each) stored in `data/themes/`.
  - **COLD**: Demoted/archived rules that haven't been triggered recently.
- **Proposals & Approval Workflow**: Proposes changes to system files or knowledge base entries in `proposals/PENDING.md` which requires manual user approval.
- **Self-Reflection**: Evaluates its own execution performance and updates `reflections.md` to guide future self-improvement loops.

## System Architecture

The core pipeline runs on a scheduled cron task (every 3 days by default) and executes the following modules sequentially:

1. **feedback-collector**: Scans chat history, terminal inputs/outputs, and logs to extract raw feedback, errors, and success signals.
2. **distill-classifier**: Categorizes learning signals and evaluates value density.
3. **memory-layer**: Applies tiered rules (e.g., promote a rule to HOT if triggered 3 times; demote after 30 days of inactivity).
4. **proposer**: Compiles lessons learned into actionable proposals in `proposals/PENDING.md`.
5. **reflector**: Reviews the run and writes metadata to a self-reflection file.
6. **profiler**: Generates an agent capability profile describing strengths and weaknesses.
7. **notify**: Alerts the user about pending proposals.
8. **execution**: Applies approved changes to system config files and prompt templates.

## Why it Matters

The `self-improve` framework decouples learning from a single agent instance. What one subagent learns can be written back, approved, and immediately shared team-wide or system-wide, moving from isolated episodic interactions to compounding systemic experience.
