---
title: "LifeOS: Custom Spinner Verbs (Philosophy)"
details: "While the system works, you see your own animated working-verb ('Forging', 'Climbing') in your color and animation, plus rotating tips that surface short, current details about your installation. Edit the source JSON, run the sync, never hand-edit the live config."
tags:
  - raw
  - tooling
source: https://ourlifeos.ai/philosophy/spinner-verbs/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Custom Spinner Verbs

**Source:** [https://ourlifeos.ai/philosophy/spinner-verbs/](https://ourlifeos.ai/philosophy/spinner-verbs/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Custom Spinner Verbs

Your own animated working-verb and tips in the statusline.


Fig. 26·Your own words, one at a time, in the status window

While the system works, most tools show you a generic spinner. LifeOS shows [a working-verb that’s yours](https://danielmiessler.com/blog/customized-spinner-verbs-in-claude-code) — an animated word like “Forging” or “Climbing,” drawn from your own vocabulary, in your own icon, color, and animation. Next to it, a rotating set of tips surfaces short, true facts about the system while you wait.

## Why it exists

A spinner is dead time. You’re waiting, and the tool shows you a stock swirl that could belong to any app. That’s a small thing, but small things are what separate a system someone made from a generic shell you’re borrowing for the afternoon.

The working-verb makes the wait yours. It’s the same move as naming your assistant or [picking its voice](https://ourlifeos.ai/philosophy/voice): a personal detail most tools never bother with, doing the quiet work of making the system feel present and specific to you. The tips earn their place a different way. They turn idle seconds into a channel that tells you something true about the system you’re actually running.

## How it works

Two features share the statusline. Verbs are the animated working word and the way it’s styled. Tips are the short informational strings that rotate during longer work.

The verb vocabulary lives as customization assets, defined once and pushed to the live config. The words, icons, colors, and animations each sit in their own file under a Spinner customization folder. A sync tool reads those files and writes them out to the live settings and to downstream projects. You edit the source JSON and re-run the sync — you never hand-edit the live config, so the canonical version stays the one you can read and version. The statusline renderer reads that live config and draws the verb, so the next time the system starts working, you see the word you set.

Source to statuslineyou edit the JSON, never the live config

Edit the sourceAdd "Forging" to your verbs file, with its icon, color, and animation.

↓

Run the syncA tool reads your files and writes them out to the live settings.

↓

See it workNext time the system starts working, the word you set pulses in the statusline.

Tips work the same way, but they track a moving target. They carry real facts, like how many [skills](https://ourlifeos.ai/philosophy/skill-system) you have, how many hooks, and which version you’re on, so they can drift as the system changes. A maintenance workflow called `/ut` audits them against the current counts and versions and refreshes any that have gone stale. Run it after a change and the tips never lie about what’s installed.

## Where it fits

This is one of the surface features, the parts of LifeOS you see and feel rather than the machinery underneath. It rides in the statusline, the same strip the rest of the system status appears in, and it sits alongside Pulse and [the dashboard tooltips](https://ourlifeos.ai/philosophy/tooltips) as the touches that make the OS feel present while you use it.

It’s deliberately minor. Nothing about your goals depends on whether the spinner reads “Forging.” But the sum of these small, personal details is what makes a system feel like yours rather than a tool you happen to run.

## What it feels like

You send a hard request and the statusline starts to move. Instead of a nameless spinner, a word you chose pulses in a color you picked, and under it a tip reminds you the system has, say, a hundred-plus skills loaded. The wait stops being dead air.

It’s a small hit of personality at exactly the moment other tools give you nothing. You’re not staring at a loading state. You’re watching your system think, in its own voice.

In the statuslineyour word, not a stock spinner

while it works⚡ **Forging** — in your color, your animation, with a rotating tip beneath: "100+ skills loaded, each firing on plain-language intent."

[Full documentationCustom Spinner Verbs →](https://docs.ourlifeos.ai/Spinner__SpinnerSystem)
