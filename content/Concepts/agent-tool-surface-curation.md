---
title: "Agent tool surface curation"
details: "Design rules for exposing a large backend to an agent through a small, explicit allow-list of tools: completeness degrades tool selection, read-only and write surfaces are separated as capability boundaries, descriptions encode when to reach for a tool, and the handshake tool list is the single source of truth. Includes the deliberate omission of a raw schema browser so agents are forced through the semantic layer, and startup validation that fails loudly when a curated tool disappears from the API spec."
tags:
  - concept
  - agent
  - mcp
  - tooling
  - architecture-pattern
created: 2026-11-03
updated: 2026-11-03
type: concept
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Agent tool surface curation

**Source:** NVIDIA Auto Ontology MCP documentation and skills ([[Raw/nvidia-auto-ontology-2026-11-03]])
**Category:** Agent tooling design
**Status:** Implemented as an explicit allow-list in an open-source MCP server

---

## Overview

An MCP server in front of a real product usually has a large API behind it. Auto Ontology's spec publishes 87 operations. Exposing all of them would be the obvious, cheap choice — and the source states plainly that it would **degrade tool selection badly**. The server therefore exposes nine hand-picked read tools, and the omissions are as deliberate as the inclusions.

Curation is not only about count. It is about what the shape of the surface teaches the model: which entry point to prefer, which questions are legitimate, and which reasoning paths are off-limits. A tool surface is a curriculum, and the agent learns it from names, descriptions, and the handshake instructions.

## Core Content

### The allow-list is explicit and self-checking

Tools are declared as `ToolSpec` entries naming the HTTP method, path, agent-facing name, and a description that says **when to reach for it**. Two properties make this more than a config file:

- **Startup fails loudly** if a curated entry no longer exists in the API spec. An upstream rename cannot silently drop a tool; the server refuses to start instead. This converts a silent capability regression into a deployment error.
- **The handshake list is the source of truth.** The skills that document the tools explicitly say not to copy a tool table into the session and to trust the handshake if the two disagree. Documentation drift cannot produce a model calling tools that do not exist.

### Omission as a design decision

There is deliberately **no tool for browsing databases, schemas, or raw columns.** The stated reason is behavioural, not security-related: a catalog browser invites an agent to reason about raw tables instead of business meaning, which is exactly the failure the semantic layer exists to prevent. The legitimate table-level case is covered by `describe_table`, which returns the *terms and SQL attributes a table participates in* — a view through the semantic layer rather than around it.

This is the generalisable move: if a system's guarantees depend on a path being taken, do not expose the shortcut. "The prompt tells it to use the glossary" is a weaker guarantee than "there is no tool that bypasses the glossary."

### Read and write are separate surfaces

Everything on MCP reads. Writes — creating terms, patching attributes, importing models, resetting compilation — go through the authenticated `/api/...` gateway and are covered by a separate skill with its own permission model and publication gates. The split is a capability boundary, not an implementation detail:

- an agent wired for read-only querying cannot mutate the glossary by accident;
- write operations get their own review discipline (validate SQL → apply smallest change → verify persisted state → staged readback);
- the query skill's stated limitation is that it "does not turn a read-only question into a mutation" — the surface enforces what the instruction merely repeats.

### Descriptions and handshake instructions do sequencing work

The server advertises **instructions at handshake** describing how the tools sequence, because a model left to itself "tends to reach straight for `ask_question`". That is a real observation about tool-using models: the most powerful tool is the most attractive one, and skipping the cheap pre-flight is the default behaviour.

The documented sequence is `check_readiness` → `search_terms` → `check_answerable` → `ask_question` → validate. Each step is cheap relative to the next, and each one can prevent the expensive call from being wasted. Encoding the sequence in the handshake rather than only in prose documentation is what makes it part of the protocol instead of part of the prompt.

### Return structured fields, not rendered prose

`ask_question` returns the answer, the SQL, and the rows as **separate fields**, not the markdown the web UI receives, "so an agent can use the SQL without parsing prose". Results are capped at 100 rows with `row_count` and `truncated` reported explicitly, and progress notifications mirror the reasoning trace.

The design principle: a tool built for agents should return the evidence in a form the agent can check, not the presentation form a human wants. Structured truncation metadata is what makes a completeness claim auditable; a rendered table with "showing first 100" in prose is not.

### The tool surface inherits the product's permissions

The MCP server holds no credentials of its own, no client secret, and no database configuration — it is an HTTP client of the public API, and sign-in is OAuth handled by the product. Consequences: a session can do exactly what the person behind it can do, permission changes take effect on the next call, and there is no way to configure a token for the server itself (which would make every caller act as its owner). Delegated identity, not a service account, is the safer default for an agent gateway.

## Key Insights

1. **Tool count is a quality parameter.** Exposing every operation is not generous, it is a selection problem handed to the model.
2. **Omission enforces architecture.** Removing the raw-schema tool is how the semantic layer stops being optional.
3. **Descriptions should answer "when", not only "what".** A tool the model never chooses is equivalent to a tool that does not exist.
4. **Put sequencing in the handshake.** Instructions that live only in docs lose to the model's preference for the powerful tool.
5. **Validate the allow-list at startup.** A curated surface needs a mechanism that notices when the API underneath it moves.
6. **Separate read and write surfaces physically.** Instruction-level caution is weaker than a capability boundary.

## Related Concepts

- [[Concepts/semantic-layer-agent-grounding]] — the layer the tool surface routes through
- [[Concepts/answer-readiness-vs-answerability]] — why cheap checks precede the expensive tool
- [[Concepts/grounded-answer-validation]] — what the structured SQL/rows fields are for
- [[Concepts/semantic-contract-for-measures]] — the write-side discipline the read surface deliberately omits

## Related Entities

- [[Entities/auto-ontology]]

## References

- Raw Source: [[Raw/nvidia-auto-ontology-2026-11-03]] (`docs/mcp.md` — "Tools", "Extending the tool surface"; `AGENTS.md`)
