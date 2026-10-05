---
title: "LifeOS: The Hook System (Philosophy)"
details: "Guardrails that are code, not good intentions: small scripts wired to fixed moments in every session (start, submit, before tool, after output, stop). Security hooks run in line and can hard-stop unsafe actions. Most hooks run in the background and fail quietly."
tags:
  - raw
  - agent
  - harness
source: https://ourlifeos.ai/philosophy/hook-system/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# The Hook System

**Source:** [https://ourlifeos.ai/philosophy/hook-system/](https://ourlifeos.ai/philosophy/hook-system/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# The Hook System

Guardrails that are code, not good intentions — enforced at fixed points.


Fig. 17·Fixed stations on every run; one can stop it cold

Some rules are too important to trust to memory. A hook is code that fires on its own at a fixed point in a session, before a tool runs or after a response is written, and does the thing that has to happen every time. The model can forget a rule; the hook runs regardless.

## Why it exists

A model is smart but not reliable the way a bank vault is reliable. Ask it to remember a safety rule on every turn and most of the time it will, which is exactly the problem. “Most of the time” is not good enough for the check that keeps a credential out of a public file or stops a destructive command before it runs.

Hooks fix that by moving the rule out of the model’s judgment and into code that always runs. The guardrail stops depending on whether the model remembered this turn. The thesis gives hooks a second, larger job too: keep the loop moving when no one is asking. A system that only acts when prompted is a chatbot. [The hook lifecycle](https://danielmiessler.com/blog/personal-ai-infrastructure) is what makes this one behave like something that runs on its own.

## How it works

The system exposes fixed moments in every session, and a hook is a small script wired to one of them. When that moment arrives, the script runs. Nothing has to remember to call it.

The moments cover the whole arc of a turn. At session start, one hook loads your context so the system knows who you are and what you’re working on. When you submit a prompt, another classifies how much effort it deserves before any work begins. Before a tool runs, a [security](https://ourlifeos.ai/philosophy/security) hook inspects the command and blocks it if it would expose a credential or do something dangerous. After a response, other hooks capture what was learned and update your [dashboard](https://ourlifeos.ai/philosophy/pulse).

```
# Test context loading directly
bun ~/.claude/hooks/LoadContext.hook.ts
```

The session lifecyclefixed points where hooks fire on their own

- Session startLoad your context, so the system knows who you are and what you're on.
- Prompt submitClassify how much effort the request deserves, before any work begins.
- Before a toolInspect the command; hard-stop it if it would leak a secret or do damage.
- After outputCapture what was learned and refresh the dashboard.
- Session stopCheck the response met its format and rules before it ships.

Two design rules keep this out of your way. Most hooks run in the background and fail quietly, so a broken one never freezes your work. The security hooks are the exception: they run in line and can hard-stop an unsafe action before it happens. And every hook is built to finish fast and exit cleanly, because a hook that hangs would hang the whole session.

## Where it fits

Hooks are the layer that makes the rest of the system trustworthy. Skills give it reach and [the Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) gives it a method, but hooks are what keep both inside the lines with nobody watching. They are where privacy and safety stop being promises and turn into enforced behavior.

They also do the quiet plumbing that keeps everything else current, like capturing each session’s work into [memory](https://ourlifeos.ai/philosophy/memory) and refreshing your dashboard the moment state changes. You rarely notice a hook. You notice its results: private data that stayed private, and a system that picked up exactly where it left off.

## What it feels like

Mostly it feels like nothing, which is the point. You work, and the rails hold. The moment you’d notice is the one that doesn’t happen: the secret that never reached a public file, the destructive command that got stopped before it ran. Good guardrails are invisible right up until they save you, and then you’re very glad they were code and not a good intention someone hoped the model would recall.

before-a-tool hook · fires every time

git push --force origin main✗ blocked — force-push over main is irrecoverablethe model never had to remember this rule; the hook did

[Full documentationHook System →](https://docs.ourlifeos.ai/Hooks__HookSystem)
