---
title: "Coordination Topology in Natural Language (Python-List Output Format)"
details: "Output format introduced in Sakana AI's Conductor (Nielsen et al., arXiv:2512.04388, 2026): an agentic workflow is encoded as three parallel Python lists — model_id, subtasks, access_list — that the orchestrator emits after its chain-of-thought. This format makes coordination strategies trivially parseable, executable, and verifiable, enabling end-to-end RL training of the orchestrator. The same format generalises to recursive and randomised-pool extensions."
tags: [concepts, llm, agent, orchestration, prompt-engineering]
sources:
  - Papers/conductor-rl-orchestrator.md
  - Raw/conductor-rl-orchestrator-arxiv.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# Coordination Topology in Natural Language (Python-List Output Format)

**Source:** [[Papers/conductor-rl-orchestrator]] · [[Raw/conductor-rl-orchestrator-arxiv]]
**Category:** Technical Reference / Output Format
**Status:** Production-validated

---

## Overview

The Conductor emits each coordination strategy as three parallel Python lists after its chain-of-thought:

```python
model_id    = [0, 2, 1]      # worker LLM per step
subtasks    = [..., ..., ...] # natural-language instruction per step
access_list = [[], [0], [0,1]] # which prior step outputs each worker sees
```

This is the format that makes the entire [[Concepts/rl-conductor-trained-orchestrator]] pattern work. It is intentionally minimal:

- **Trivially parseable** — any Python interpreter can execute the lists.
- **Executable** — the workflow runner simply iterates steps in order, calling `model_id[i]` with `subtasks[i]` and the prior responses indicated by `access_list[i]`.
- **Verifiable** — the format reward is binary: 0 if the lists don't parse, 1 otherwise. This makes RL training possible.
- **Topologically expressive** — the same three-list format encodes best-of-N, sequential chains, parallel trees with aggregation, and recursive self-revision.

## Why Three Parallel Lists?

Alternatives considered by the authors and rejected:

- **Free-form JSON.** More flexible but harder to constrain — the model can emit malformed JSON, nested structures, or invalid agent IDs.
- **A single DSL.** More compact but harder for an LLM to generate correctly on first try.
- **Three sequential blocks (one list per block).** Harder to enforce parallel lengths — the model can mismatch `len(model_id) != len(subtasks)`.
- **Three parallel lists with explicit length declaration.** What Conductor does. The parallel structure forces length agreement by construction.

The format is shown in Figure 13 (full Conductor prompt) and Figure 14 (recursive Conductor prompt) of the Raw paper.

## What Each List Encodes

### `model_id[i]`

Integer index into the available worker pool. The pool is fixed per-query (either a closed-source model like GPT-5, an open-source model like Qwen-32B, or the Conductor itself for recursion).

### `subtasks[i]`

Natural-language instruction to the worker. This is where the Conductor's prompt-engineering strategy lives. Examples from the Raw paper (Figures 18–28):

- `"Analyze the problem, understand the constraints, and propose a strategy..."`
- `"Critique the previous solution and identify any logical errors."`
- `"Format the answer according to the schema below."`

The Conductor learns to write these instructions during RL training.

### `access_list[i]`

List of step indices whose outputs should be visible to worker `i` as prior context. This is the **communication topology**:

- `[]` — the worker sees only the original query (no prior context).
- `[0, 1]` — the worker sees outputs from steps 0 and 1.
- `[[0], [0, 1]]` — the workflow has parallel branches; step 2 sees step 0, step 3 sees steps 0 and 1.

`access_list` is what makes the output a *topology* and not just a sequence.

## Emergent Topologies

The same three-list format encodes all of these patterns the Conductor discovered during training:

| Topology | `model_id` shape | `access_list` shape |
|----------|------------------|---------------------|
| Single agent | `[0]` | `[[]]` |
| Best-of-N | `[0, 0, 0]` | `[[], [], []]` |
| Sequential chain | `[0, 1, 2]` | `[[], [0], [1]]` |
| Parallel + aggregate | `[0, 1, 2]` | `[[], [], [[0], [1]]]` |
| Tree | `[0, 1, 2, 3]` | `[[], [], [0], [1]]` |
| Verify and revise | `[0, 1, 2]` | `[[], [], [[0, 1]]]` |
| Recursive self-as-worker | see [[Concepts/recursive-test-time-scaling]] | |

## Why This Format Enables RL

The format reward is a hard constraint:

```python
if not all([isinstance(x, int) for x in model_id]) \
   or len(model_id) != len(subtasks) != len(access_list) \
   or any(x not in available_agents for x in model_id):
    return 0  # format reward
```

This makes the supervisor signal *clean* — the Conductor either produces a valid workflow or it doesn't. Without a parseable format, RL training would be bottlenecked on the orchestrator generating valid syntax.

## When to Use This Format

- You're training an LLM to design multi-agent workflows with RL.
- You want the workflow to be human-inspectable (the three lists are easy to read).
- The worker pool is small enough to fit in the prompt (≤10 agents).

## When NOT to Use

- The workflow needs to encode state, control flow, or conditional branching that exceeds what three parallel lists can express.
- The worker pool is too large to enumerate (you'd want an embedding-based retrieval step first).
- You need typed outputs per worker (e.g. structured JSON from the coder worker) — the format encodes the *coordination* but not the *output schema*.

## Related Concepts

- [[Concepts/rl-conductor-trained-orchestrator]] — the base pattern using this format
- [[Concepts/recursive-test-time-scaling]] — recursion reuses the same three-list format
- [[Concepts/coordinator-worker-task-dag-orchestration]] — broader DAG-style orchestration; this format is one specific encoding

## References

- Paper: [[Papers/conductor-rl-orchestrator]]
- Raw extraction: [[Raw/conductor-rl-orchestrator-arxiv]] — Section 3.1, Figures 13 & 14
- Original: https://arxiv.org/html/2512.04388v5
