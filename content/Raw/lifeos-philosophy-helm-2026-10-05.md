---
title: "LifeOS: Helm (Philosophy)"
details: "The LifeOS terminal: kitty for the window, herdr for the session layer. Configuration, not a fork — kitty installs through Homebrew, herdr runs as its own unmodified binary, Helm is the config that makes them one terminal. `helm doctor` checks the setup."
tags:
  - raw
  - tooling
source: https://ourlifeos.ai/philosophy/helm/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Helm

**Source:** [https://ourlifeos.ai/philosophy/helm/](https://ourlifeos.ai/philosophy/helm/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Helm

The LifeOS terminal: kitty for the window, herdr for your sessions, installed with one command.


Fig. 25·The stock base untouched; one layer bolted on

Helm is the terminal LifeOS was built in, and it ships inside LifeOS itself. It has two parts. [Kitty](https://sw.kovidgoyal.net/kitty/) supplies the window, the theme, the fonts and the keyboard protocol. [Herdr](https://herdr.dev/), a workspace manager built for coding agents, runs inside it and owns your sessions, tabs and panes.

Neither one is forked. Kitty installs through [Homebrew](https://brew.sh/) and herdr runs as its own unmodified binary; Helm is the configuration that makes them work as one terminal. If you run LifeOS, you already have it. One command rigs your terminal:

```
bash ~/.claude/LIFEOS/DOCUMENTATION/Terminal/install.sh
```

Then install herdr from [herdr.dev](https://herdr.dev/) and run `herdr` inside kitty. `helm doctor` checks the whole setup.

## What’s in it

- **Herdr as the session layer.** Every agent session gets a workspace in herdr’s sidebar, with herdr tracking whether each agent is working, waiting on you, or done. The herdr server keeps sessions alive when you close the window.

- **One set of keys.**`cmd+t` opens a workspace, `cmd+n` a tab, `cmd+shift+l` splits right, `cmd+k` jumps to any workspace, tab or agent. Kitty passes each of these chords through to herdr while herdr is focused, and runs its own version of the same action in a plain kitty window.

- **Links that open on a plain click**, even though herdr holds the mouse in every pane.

- **The look.** Tokyo Night Storm, a [Nerd Font](https://www.nerdfonts.com/), and a branded boot card.


## The LifeOS connection

With LifeOS running, herdr’s sidebar becomes a live view of your work. [Hooks](https://ourlifeos.ai/philosophy/hook-system) write each session’s name, its state and its progress against its ISA onto its row in the sidebar. A second list shows each worker: which model is running and which helper agents it has dispatched. Without LifeOS, herdr’s own agent tracking still works and Helm is simply a very good terminal.

## Why configuration and not a fork

A fork of a terminal emulator is a compiled application you maintain forever: upstream security fixes, monthly releases, signed builds. Configuration gets the same experience for none of that. Kitty and herdr keep improving underneath, and because the installer links rather than copies, updating LifeOS updates Helm.

Helm lives in the [LifeOS repo](https://github.com/danielmiessler/LifeOS) under `LIFEOS/DOCUMENTATION/Terminal/`.

[Full documentationHelm — the LifeOS Terminal (Optional) →](https://docs.ourlifeos.ai/Terminal__Helm)
