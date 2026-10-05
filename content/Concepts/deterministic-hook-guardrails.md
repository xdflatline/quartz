---
title: "Deterministic Hook Guardrails — Fixed-Point Rule Scripts"
details: "An architectural pattern for safety, verification, and ambient automation in agent runtimes: small scripts wired to fixed lifecycle moments (session start, prompt submit, before-tool, after-output, session stop) that run on their own regardless of model behavior. Security hooks run inline and can hard-stop unsafe actions; ambient hooks run in the background and fail quietly so a broken hook never freezes work. The model can forget a rule; the hook runs it every time. Used in Claude Code, LifeOS, Hermes, and similar agent frameworks; the same shape that lets guardrails be enforced at fixed points is what lets the loop keep moving when no one is asking."
tags:
  - concept
  - architecture-pattern
  - agent
  - harness
  - cybersecurity
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-hook-system-2026-10-05]]"
---

# Deterministic Hook Guardrails — Fixed-Point Rule Scripts

**Source:** [[Raw/lifeos-philosophy-hook-system-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Some rules are too important to trust to memory. A *hook* is code that fires on its own at a fixed point in a session, before a tool runs or after a response is written, and does the thing that has to happen every time. The model can forget a rule; the hook runs regardless.

A model is smart but not reliable the way a bank vault is reliable. Ask it to remember a safety rule on every turn and most of the time it will — which is exactly the problem. *Most of the time* is not good enough for the check that keeps a credential out of a public file or stops a destructive command before it runs.

## The lifecycle

The system exposes fixed moments in every session, and a hook is a small script wired to one of them. When that moment arrives, the script runs. Nothing has to remember to call it.

The arc of a turn:

- **Session start** — load context so the system knows who you are and what you're on.
- **Prompt submit** — classify how much effort the request deserves, before any work begins.
- **Before a tool** — inspect the command; hard-stop it if it would leak a secret or do damage.
- **After output** — capture what was learned and refresh the dashboard.
- **Session stop** — check the response met its format and rules before it ships.

## Two design rules

**Most hooks run in the background and fail quietly**, so a broken one never freezes your work. The security hooks are the exception: they run in line and can hard-stop an unsafe action before it happens.

**Every hook is built to finish fast and exit cleanly**, because a hook that hangs would hang the whole session.

A second job, beyond safety: hooks keep the loop moving when no one is asking. A system that only acts when prompted is a chatbot. The hook lifecycle is what makes this one behave like something that runs on its own — capturing state into memory, refreshing the dashboard, classifying prompts by effort, enforcing security boundaries.

## Before-a-tool hook — fires every time

```
git push --force origin main
✗ blocked — force-push over main is irrecoverable
```

The model never had to remember this rule; the hook did.

## Connection to other patterns

- [[Concepts/four-tier-verification-stack]] — hooks are the mechanism that enforces the code and glance tiers at lifecycle boundaries
- [[Entities/hermes-agent]] — same lifecycle hook shape, applied to a personal assistant runtime
- [[Concepts/sandboxed-execution-for-ai-agents]] — the *where* of execution; hooks are the *when*

## Key Insights

1. **Hooks outlive model attention.** A model that forgot the rule is irrelevant. The check still fires.
2. **Inline vs background is the split.** Security hooks run inline (they must block); ambient hooks run in the background (they must not freeze).
3. **Speed matters more than correctness of the hook itself.** A hook that hangs is worse than no hook. Fail fast, fail quiet.
4. **Hooks are also automation.** They keep the system running between prompts, not just enforcing rules.

## Related Concepts

- [[Concepts/four-tier-verification-stack]] — hooks enforce the lower tiers
- [[Entities/lifeos]] — primary productization

## References

- Raw: [[Raw/lifeos-philosophy-hook-system-2026-10-05]] and [[Raw/lifeos-philosophy-security-2026-10-05]]
- Origin essay: [Personal AI Infrastructure](https://danielmiessler.com/blog/personal-ai-infrastructure)