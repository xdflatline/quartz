---
title: "Standards Layer with Path Citation"
details: "Architectural pattern where a `docs/standards/` directory holds one profile per concern (per-language quality, cross-cutting concerns, document shape rules, templates), authored once, cited by every other artifact (AGENTS.md, Makefile, CodeRabbit config, agent prompts). Profiles own their concern, cite other profiles by path, and never restate. Adding a rule means editing one file, not five. Vendor-independent rules survive tool churn because they live in version-controlled markdown, not in vendor knowledge bases."
tags:
  - concept
  - agent
  - tooling
created: 2026-08-17
updated: 2026-08-17
type: concept
---

# Standards Layer with Path Citation

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

The standards layer is a `docs/standards/` directory of profiles — one per concern — that every other artifact references by path. Profiles do not embed each other and do not name their consumers. The result is "authored once, consumed many times": agents, CI, review tools, dev environments, and humans all anchor to the same operational context without each maintaining their own copy. Vendor independence is a side benefit — the accumulated learning lives in the repository, not in any vendor's knowledge base.

## Core Content

### What the Standards Layer Contains

Four categories, each authored once:

| Category | Example Profile | Concern |
|----------|-----------------|---------|
| Per-language quality | `python-profile.md`, `go-profile.md`, `ts-profile.md` | Language-specific style, test, and structure rules |
| Cross-cutting concerns | `code-review-rubric.md`, `testing-profile.md` | Rules that apply regardless of language |
| Document shape rules | `spec-shape.md`, `plan-shape.md`, `adr-shape.md` | What each artifact type looks like |
| Templates | `spec-template.md`, `plan-template.md`, `adr-template.md` | Starting points for new artifacts |

### Two Authoring Rules That Hold the Layer Together

1. **Each profile owns its concern.** Cross-language rules live in `code-review-rubric.md`; language profiles cite it rather than duplicating it. Test-substance rules live in `testing-profile.md`; the rubric refers to it.
2. **Profiles cite by path and never restate.** Adding a new rule means editing one file, not five.

### The Consumption Model

Every consumer in the repo points to the same profiles by path:

- **AGENTS.md hierarchy** (~19 files across root, app, submodule) names the deny-list paths relevant to its scope and links to the profiles that govern it. Cursor, Claude Code, Codex, CodeRabbit all read it.
- **Makefile** is the verification interface. Every artifact answers to `make ci`, `test`, `lint`, `fmt`, `build`, `run`. `make lint` is deliberately non-mutating — auto-fix lives under `make fmt`. Same interface across Go Lambda, Python ECS, TypeScript/Vue.
- **CodeRabbit config** is thin because the rules do not live in YAML. The file is mostly path routing — "review against `docs/standards/python-profile.md` and `docs/standards/code-review-rubric.md`."
- **Agent skills** reference profiles by path in their prompts, so agents and human reviewers are anchored to the same source of truth: the same document, in the same version.

### The Vendor-Independence Property

> "AI-coding agents and review tools are a competitive market, and every vendor has an incentive to pull you into its own knowledge base. If the rules live in version-controlled markdown, the accumulated learning stays with the repository instead of the vendor."

Switching vendors does not require re-encoding the rules. The profiles are markdown in the repo; whatever tool reads the repo picks them up.

### Anti-Pattern: Duplicated Rules

If the rule "lint is non-mutating" lives in `code-review-rubric.md`, the Makefile, the agent prompt, and the on-call runbook, four edits are required to change it and three will be missed. Path citation makes the rule live once; the consumers anchor to it.

## Key Insights

1. **"Authored once, consumed many times" is the architectural shape.** Profiles own a concern; every consumer points at them by path. The Makefile, AGENTS.md, CodeRabbit config, and agent prompts all anchor to the same documents.
2. **Profiles must not embed each other or name their consumers.** Embedding creates versioning drift; naming couples the profile to a tool that might be swapped.
3. **The Makefile is the verification interface.** One set of commands (`make ci`, `test`, `lint`, `fmt`, `build`, `run`) across languages, run by agent self-verify, CI, and human onboarding — same surface, same outcome.
4. **Vendor independence is a downstream property.** The rules are in the repo, not in any vendor's knowledge base, so tool churn does not destroy accumulated learning.

## Related Concepts

- [[Concepts/sdlc-as-context-engineering]] — the standards layer is one concrete instantiation
- [[Concepts/four-execution-lanes]] — lane-aware escalation is encoded in the standards layer
- [[Concepts/devcontainer-as-execution-boundary]] — `.devcontainer/` is one of the governed paths

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering