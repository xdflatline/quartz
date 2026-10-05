---
title: "LifeOS: Learning (Philosophy)"
details: "Every Algorithm run ends with reflection: what worked, what didn't, what a smarter version would have done. Reflections roll up from events → patterns → Frames (living models of domains). It's the bridge between one session and the compounding archive."
tags:
  - raw
  - agent
  - memory
source: https://ourlifeos.ai/philosophy/learning/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Learning

**Source:** [https://ourlifeos.ai/philosophy/learning/](https://ourlifeos.ai/philosophy/learning/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Learning

Every run reflects on itself and feeds the next.


Fig. 21·Runs compact into lessons that feed the next run

Every run ends with the system asking three questions: what worked, what didn’t, and what a smarter version of it would have done. The answers don’t just sit in a log. They change the next run.

## Why it exists

Finishing a task tells you nothing about whether the approach was any good. A system that never looks back repeats the same mistake forever, politely, at speed. Reflection is what turns one hard session into a permanent upgrade instead of a story you tell twice.

It also keeps the bar honest. A low rating isn’t noise to smooth over. It’s the most useful signal the system gets, and it earns a real post-mortem rather than a shrug. It’s cheaper to learn a lesson once than to pay for it every week.

## How it works

Learning is how every [Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) run ends. None of it is a chore you run. The reflection fires on its own when a run ends, and your ratings are just how you already react. When a run ends, [LEARN](https://danielmiessler.com/blog/the-last-algorithm) writes a short reflection into the record: what the approach got right, and where a better version would have gone instead. A one-to-ten score rides along, and anything in the bottom band triggers a full capture of the transcript, the tool calls, and a root-cause read. That full capture exists so the failure can be traced to its root later, and so a change can be found that stops the whole class of it.

Every run ends herethree questions, asked automatically

- What workedThe parts of the approach that earned their place.
- What didn'tWhere it went sideways — and a low score triggers a full root-cause capture.
- What's smarterWhat a better version would have done instead, written back into the record.

Learnings sort themselves too. A tooling or config failure files under one heading; a wrong-approach or missed-the-point call files under another, so patterns don’t blur across kinds. Then individual learnings roll up. A synthesis pass reads across many ratings and finds the recurring approach error, the class of task that keeps going sideways. Above patterns sit Frames: living models of a domain like writing or deployment that the system reads before work and revises after. That’s the dual loop. The Algorithm consults the Frame on its way in and rewrites it on its way out, so taste accumulates.

```
# Generate pattern synthesis
bun run ~/.claude/LIFEOS/TOOLS/LearningPatternSynthesis.ts --week
```

## Where it fits

LEARN closes the Algorithm’s loop and hands off to [memory](https://ourlifeos.ai/philosophy/memory). A reflection worth keeping becomes a durable note; a Frame that’s proven out becomes something the next run reads first. So learning is the bridge between one session and the compounding archive. Memory stores what’s true now; learning changes how the system works next. The layers stack, from single events at the bottom up to the Frames on top, each level more general and slower to change than the one beneath.

The stackbottom to top — more general, slower to change

- EventsOne reflection from one run.
- PatternsA recurring error found across many runs.
- FramesA living model of a domain the system reads before work and revises after.

This is also where the system’s honesty lives. [Verification](https://ourlifeos.ai/philosophy/assay) proves a task met its criteria. Learning asks the harder question of whether the criteria were the right ones, and whether next time should be run differently at all.

## What it feels like

You correct the system once and it stays corrected. A rough patch on Monday shows up as a smoother path on Thursday, without you saying anything. Over weeks you notice it stops making a whole class of mistake, and starts anticipating things you used to have to spell out. The corrections you gave a month ago are still holding. It behaves less like a tool you retrain and more like someone who is genuinely getting better at the work.

[Full documentationCortex — the LifeOS Memory System →](https://docs.ourlifeos.ai/Memory__MemorySystem)
