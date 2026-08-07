---
title: "On-Demand Skills Catalog Pattern"

details: "An on-demand instruction-loading pattern: skills (per the Agent Skills format: SKILL.md with YAML frontmatter plus optional references/, scripts/, assets/) are discovered at agent build time. Instead of inlining every skill into the system prompt, the harness appends only a catalog of names and descriptions. The LLM calls load_skill to fetch a skill's full instructions on demand, and read_skill_file to fetch individual resource files. read_skill_file resolves symlinks and rejects any path that escapes the skill directory. Implemented in AURA (mezmo/aura) as [agent.skills]."
tags:
  - concepts
  - context-engineering
  - agent
created: 2026-07-25
updated: 2026-07-25
type: concept
source: https://github.com/mezmo/aura
---

# On-Demand Skills Catalog Pattern

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Architecture Pattern
**Status:** Production-validated (AURA, also formalized in the agentskills.io spec)

---

## Overview

An **on-demand skills catalog** is a pattern for giving an agent access to a library of task-specific instructions without bloating the system prompt. Skills are discovered at agent build time, exposed to the LLM as a catalog of names and one-line descriptions, and fetched in full only when the agent decides a task calls for one.

The pattern is the standard answer to "my agent has 50 procedures and 200 references — I cannot fit them all in the system prompt." Instead of inlining, the catalog tells the LLM what is available, and the agent pulls in what it needs.

## Core Content

### The Agent Skills Format

Each skill is a directory in the [Agent Skills format](https://agentskills.io/specification):

```text
skills/
└── code-review/
    ├── SKILL.md       # required: frontmatter (name, description) + instructions
    ├── references/    # optional resources, fetched via read_skill_file
    ├── scripts/
    └── assets/
```

`SKILL.md` has YAML frontmatter (`name`, `description`) followed by the instructions. The `name` field must match the directory name (validated at discovery time). Directories without a `SKILL.md` are skipped.

### Configuration

```toml
[agent.skills]
local = [
  { source = "./skills" },               # relative paths resolve from the process CWD
  { source = "/opt/aura/shared-skills" }
]
```

Each `source` is a directory containing skill subdirectories. Multiple sources are merged; on collision, the first source loaded wins and a warning is logged.

### Discovery and Catalog

Discovery runs at agent build time and validates each skill against the spec. The harness then appends only a **catalog** of names and descriptions to the system prompt, not the full instructions:

```text
Available skills (call load_skill to fetch full instructions):
- code-review: Review code changes for correctness, style, and security.
- incident-postmortem: Generate a blameless postmortem from an incident timeline.
- runbook-search: Search the operations runbook for the relevant procedure.
- ...
```

The full instructions stay on disk until the agent calls `load_skill`.

### The Two Skill Tools

| Tool | Purpose |
|------|---------|
| `load_skill(name)` | Fetch the full `SKILL.md` instructions for a named skill and inject them into context. |
| `read_skill_file(skill_name, path)` | Fetch an individual resource file (a reference doc, a script, an asset). |

`read_skill_file` resolves symlinks and **rejects any path that escapes the skill directory** — the security boundary. A malicious or buggy skill cannot trick the LLM into reading `/etc/passwd` by symlinking a file there.

### Per-Worker Overrides

In orchestration, the coordinator inherits `[agent.skills]`. Workers inherit it too, unless overridden:

```toml
[orchestration.worker.knowledge.skills]
local = [{ source = "./knowledge-skills" }]   # worker-specific skills

[orchestration.worker.operations.skills]
local = []                                    # no skills for this worker
```

An explicit empty `local = []` disables skills for that worker. Useful when a worker is on a constrained LLM and even a catalog of names is too much overhead.

### Path Resolution Semantics

Relative `source` paths resolve from the **process current working directory** in every mode (web server, standalone CLI, and A2A). `CONFIG_PATH` / `--config` locate the TOML file only; they do not change how paths inside TOML are resolved. This is a footgun: if the operator starts the server from a different working directory, relative `source` paths break silently.

## Key Insights

1. **Catalog-not-inline is the right unit of disclosure.** The system prompt is the most expensive real estate in the agent's context. A 50-skill catalog takes a few hundred tokens; inlining all 50 skills would consume tens of thousands. The catalog lets the LLM know what is available without paying the cost.
2. **`load_skill` is a tool call, not a system-prompt fragment.** The LLM decides when to load a skill. This is the right place for the decision: the model has the full task context, so it knows whether `code-review` is relevant before paying the token cost.
3. **The `read_skill_file` escape check is the security boundary.** A skill can ship a 10-MB reference doc; `read_skill_file` must not let the LLM use that to read arbitrary host files. The symlink-resolve-and-escape-reject is a tight, mechanical safety check.
4. **Discovery validation is a build-time gate.** Validating each skill at agent build time means a missing `name` field or a name/directory mismatch is caught before the agent ever runs. Runtime skill loading is then purely a fetch operation.
5. **Per-worker override is the cost knob.** A coordinator sees the full skill catalog; a tight-token-budget worker can have a smaller subset or no skills at all. The override is the lever for tuning the LLM load against the task profile.

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — broader pattern this is a composition mechanism in
- [[Concepts/coordinator-worker-task-dag-orchestration]] — per-worker skill overrides
- [[Concepts/scratchpad-context-window-management]] — the parallel context-management pattern for tool outputs
- [[Entities/mezmo-aura]] — concrete implementation
- [[Concepts/agent-stack-layers]] — broader stack layering that includes this tier

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- Spec: https://agentskills.io/specification
