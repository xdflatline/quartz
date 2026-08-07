---
title: "Coding Agent Tool Taxonomy"

details: "Weng's case study shows that the core tool interface has converged across all major coding-agent products. The taxonomy is not a spec — it's a description of what shipped in 2026. Eight tool groups cover every mainstream capability: file system (read/write/edit/patch), shell (bash), IO (lsp, git), external context (MCP, skills), web search, artifacts, backend processes (cron), and agent delegation. New tools slot into one of these groups; novel capabilities almost always extend rather than replace."
tags:
  - concepts
  - coding-agent
  - tooling
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Coding Agent Tool Taxonomy

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Technical Reference
**Status:** Production-validated (industry consensus as of mid-2026)

---

## Overview

The core interface of mainstream coding agents has **stabilized** across Claude Code, Codex, OpenCode, and Cursor-style agents. Weng's case study enumerates eight tool groups that together cover the entire surface area a coding agent operates on. The taxonomy is descriptive, not prescriptive — but it functions as a de facto industry standard that new tools and harnesses slot into.

## Core Content

### The Eight Tool Groups

| Group | Tools | Purpose |
|-------|-------|---------|
| **File system** | Discovery: `glob`, `grep`, `ls`; Read: `read`, `read_many`; Modification: `write` (whole file), `edit` (string exact-match), `multi_edit`, `apply_patch` (structured diff) | Persistent state, code editing |
| **Shell execution** | `bash`, `PowerShell` | Run commands, scripts, file operations |
| **IO** | `lsp`, `git_status`, `git_diff`, `git_commit` | IDE-style and VCS integration |
| **External context** | MCP tools, Skills | Pluggable capability from external servers |
| **Web search** | `web_search`, `web_fetch`, browser tools | External knowledge acquisition |
| **Artifacts** | Read docs/images; generate HTML, images | Mixed-modal I/O for the user |
| **Backend processes** | `CronCreate`, `CronDelete`, `CronList` | Long-running async jobs |
| **Agent delegation** | `spawn_agent`, `resume_agent`, `wait_agent`, `list_agents`, `close_agent`, `interrupt_agent` | Parallel sub-agents |

### Design Notes Per Group

#### File system

The richest group. `write` is whole-file replacement; `edit` does exact-string replacement (fragile but auditable); `multi_edit` batches; `apply_patch` is a structured diff format (the Anthropic / OpenAI convention). Read tools split between per-file (`read`) and bulk (`read_many`).

#### Shell execution

The foundation skill. `bash` is the universal escape hatch for any operation not covered by a dedicated tool. The harness is expected to interpret exit codes, capture stdout/stderr, and surface timeouts.

#### IO

`lsp` (language server protocol) gives the agent code intelligence — go-to-definition, find-references, type checking, refactor. Git tools are usually read-only except `git_commit` (commit is a write that the harness typically gates behind user approval).

#### External context

MCP (Model Context Protocol) is the standard for adding external tools at runtime. Skills are the file-based extension mechanism (see [[Concepts/on-demand-skills-catalog-pattern]]).

#### Web search

A read-only path to the world beyond the model's training cutoff. `web_search` returns ranked results; `web_fetch` retrieves full text; browser tools are the heavyweight option for sites that don't render server-side.

#### Artifacts

Bidirectional: read user-provided docs and images; produce HTML reports, generated images, exported PDFs. In a coding-agent context, this is usually the "show your work" surface for the final deliverable.

#### Backend processes

Cron primitives let the agent schedule its own follow-up tasks. The harness owns the schedule, not the agent — the agent proposes, the harness persists and fires.

#### Agent delegation

The parallelism interface. See [[Concepts/parallel-subagent-process-manager]].

## Key Insights

1. **The taxonomy is converged, not designed.** No one published a "coding agent tool spec" — the convergence happened because each tool group is the natural primitive for its problem.
2. **New tools slot into existing groups.** Almost every novel capability fits in file system, shell, IO, external context, or delegation. Whole new groups are rare.
3. **MCP is the integration boundary.** Any tool that needs to ship from a third party uses MCP. First-party tools can be either direct function calls or MCP servers.
4. **The `edit` tool is a known weak point.** Exact-string replacement is fragile; `apply_patch` is more robust; future harnesses will likely add AST-aware editing.

## Related Concepts

- [[Concepts/harness-as-runtime-os-analog]] — the OS analogy these tools embody
- [[Concepts/parallel-subagent-process-manager]] — the agent delegation group
- [[Concepts/file-system-as-agent-memory]] — the file system group in practice
- [[Concepts/on-demand-skills-catalog-pattern]] — the skills extension mechanism
- [[Concepts/standard-json-schema-tool-contracts]] — the underlying tool contract
- [[Concepts/capability-first-tool-design]] — how to scope a tool's surface

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
