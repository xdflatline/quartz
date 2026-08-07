---
title: "File System as Agent Memory"
detail: "Pattern 2 from Weng's harness taxonomy: harness durable state in files (experiment logs, code diffs, error traces, paper summaries, past rollout trajectories) rather than carrying it in context, because artifacts routinely outgrow the model's context window."
details: "Files are the universal substrate for long-horizon agent memory. Reading, writing, and editing files via bash is a foundation skill that benefits directly from core model improvements, so this pattern ages well across model generations. The key design rule: structure state in inspectable, recoverable files; the model can re-read on demand with grep/cat instead of carrying it in context. The pattern underlies every self-improving harness that survives more than one task horizon (Meta-Harness, DGM, Self-Harness, AHE)."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# File System as Agent Memory

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Pattern
**Status:** Production-validated (universal across Claude Code, Codex, OpenCode, Cursor, AURA, Mastra)

---

## Overview

A harness should **NOT carry the entire workflow and all logs in context**; instead, it should keep **durable state in files**. In long-horizon agentic rollouts, artifacts (experiment logs, code diffs, paper summaries, error traces, past rollout trajectories) routinely grow much longer than the context window the model has trained for. The file system is the substrate that lets the agent survive context overflow, recover from interruptions, and reason over its own execution history.

## Core Content

### Why Files, Not Context

- **Volume:** A single multi-hour rollout can produce megabytes of trace data. Even the best long-context models have a 1M-token ceiling (~4 MB of text); file-backed state has no ceiling.
- **Inspectability:** Files are human-auditable. The operator can `cat` a log, `grep` for a failure pattern, and reason about what happened — without re-running the agent.
- **Recoverability:** If the agent crashes or context is evicted, the next session can resume by re-reading the file system.
- **Cross-session continuity:** The same workspace across sessions means the agent's memory compounds; transient context does not.

### What Goes in Files

| Category | Example | Why |
|----------|---------|-----|
| Experiment logs | `runs/2026-08-07-12-34/stdout.log` | Recover failure causes, compare runs |
| Code diffs | `patches/*.diff` | Re-apply, audit, branch |
| Error traces | `traces/*.json` | Mine failure patterns (see Self-Harness) |
| Paper summaries | `papers/<id>.md` | Compact long-context for grounding |
| Past trajectories | `rollouts/<task>/traj.jsonl` | Replay, retrain, eval |
| Scratch state | `scratch.md` | Hot working memory |
| Eval results | `benchmarks/<name>/results.csv` | Track progress over time |

### The Bash Foundation Skill

Reading, writing, and editing the file system is done through `bash` (and `PowerShell` on Windows). This is a **foundation skill** for LLMs — improving the model's ability to use `bash`, `grep`, `cat`, `sed`, `awk` is a leverage point that pays off across every harness built on top.

### Sub-agents and Inspectable Parallelism

When sub-agents run in parallel, their outputs MUST land in files (not just chat context). The parent agent becomes a small process manager that:

1. Launches jobs and writes launch records to disk
2. Polls logs (`tail -f`, `grep` for completion markers)
3. Cancels failed runs (`kill <pid>` + record outcome)
4. Merges results by reading the output files

This makes parallelism **explicit and inspectable** — the same property the OS analogy gives you for sequential execution.

### How Self-Improving Harnesses Use Files

Every self-improving harness in Weng's survey depends on the file-as-memory pattern:

- **Meta-Harness** (Lee et al. 2026): proposed harness is a dictionary in the file system containing source code, scores, trajectories, state updates.
- **DGM** (Zhang et al. 2025): the parent agent reads its own benchmark log and writes a new version of the harness codebase.
- **Self-Harness** (Zhang et al. 2026): failure records stored as files for clustering and pattern mining.
- **AHE** (Lin et al. 2026): raw trajectories stored in files, accessed via "Agent debugger" for per-task analysis.
- **ACE** (Zhang et al. 2025): context items persisted as `(id, description)` bullets, deduplicated and merged.
- **MCE** (Ye et al. 2026): skills and contexts instantiated as files in a dedicated directory.

Without file-backed memory, none of these loops would survive past one rollout.

## Key Insights

1. **Files are the universal substrate.** They outlast any specific tool, format, or context window. Investing in file ergonomics pays compound interest.
2. **The pattern is model-agnostic.** It benefits from core model improvements to bash, grep, and reading comprehension — not from any harness-specific trick.
3. **Inspectability is a safety property.** The same file structure that lets the model recover also lets a human operator audit, replay, or stop the loop.

## Related Concepts

- [[Concepts/harness-as-runtime-os-analog]] — the broader framing
- [[Concepts/parallel-subagent-process-manager]] — file-backed parallelism
- [[Concepts/observational-memory-pattern]] — adjacent pattern for in-context observation storage
- [[Concepts/durable-checkpoint-record-and-replay]] — durable execution substrate
- [[Concepts/provenance-preserving-memory-substrate]] — file-backed audit trail

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
