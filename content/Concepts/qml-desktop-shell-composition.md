---
title: "QML Desktop-Shell Composition"
details: "Architectural pattern where a Linux desktop shell (status bar, widgets, lockscreen, display manager, notification popups) is composed from declarative QML scenes that import bindings to the host compositor and system services. The user-facing config is a program written in QML, not a static style file. Quickshell is the primary open-source implementation; KDE Plasma's plasmashell is the larger-scale precedent."
tags:
  - concepts
  - architecture-pattern
  - desktop
  - linux
  - qt
created: 2026-08-31
updated: 2026-08-31
type: concept
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# QML Desktop-Shell Composition

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Architecture Pattern
**Status:** Production-validated (Quickshell v0.3.x, KDE Plasma 5/6)

## Overview

Most Linux desktop shells are configured by editing a small number of files (CSS-ish bar styles, JSON widget lists, keybinding lists). The QML desktop-shell composition pattern instead treats the shell as a *program* the user authors — a QML scene tree whose nodes are panels, widgets, lockscreens, popups, and IPC consumers, with property bindings ([[Concepts/qtquick-reactive-binding-model]]) wiring them to live data from the compositor, audio system, network, power, and media players. This trades a higher learning curve for a much larger design space: arbitrary layout, animation, and reactive logic are first-class, not workarounds.

## Core Content

### Pattern shape

| Layer | Role | Implementation in [[Entities/quickshell]] | Precedent |
|-------|------|------------------------------------------|-----------|
| Compositor | owns the screen, places windows | External: Hyprland / Sway / I3 / X11 WM | Same |
| Shell host (runtime) | parses user QML, hosts the scene graph, exposes system services as QML objects | The `quickshell` binary | KDE Plasma's `plasmashell` |
| User-authored QML | the shell program itself | Files under the user's config dir | Plasma QML packages, plasmoids |
| Built-in QML types | widgets, panels, lockscreens, IPC consumers provided by the host | `FloatingWindow`, `PanelWindow`, `WlSessionLockSurface`, `MprisPlayer`, etc. | KDE Plasma C++-exposed QML types |
| Integrations | live bindings to system services | Pipewire, BlueZ, UPower, MPRIS, StatusNotifierItem, Hyprland IPC, greetd, Polkit | KIO, PowerDevil, BluezQt |

### Why QML specifically

- **Reactive property bindings** ([[Concepts/qtquick-reactive-binding-model]]) eliminate manual update code — `color: timer.invert ? "purple" : "green"` re-evaluates automatically
- **Declarative scene graph** with hardware-accelerated rendering out of the box
- **One language for layout, animation, and logic** — no separation between "style file" and "script"
- **LSP tooling** (`qmlls`) is first-party and integrated by the shell host (Quickshell includes editor configs for Emacs, Neovim, Helix, and VSCode)
- **Hot reload** ([[Concepts/hot-reload-qml-config-iteration]]) makes authoring interactive

### Tradeoffs vs simple bars

| Dimension | Simple bar (Waybar, etc.) | QML shell composition |
|-----------|---------------------------|------------------------|
| Authoring effort | Edit a few config files | Write a program |
| Customization ceiling | Limited to the bar's widget set | Arbitrary layout, animation, IPC, custom types |
| Language | JSON / CSS-ish | QML (JS-flavored declarative) |
| Reactive updates | Manual `pulse` scripts or polling | Property bindings to live data |
| Iteration speed | Restart the bar to test | Hot reload on save |
| Failure mode | Typos in JSON; restart | QML errors surface with stack traces |

Quickshell's own docs are explicit about the tradeoff: *"Quickshell is a relatively low-level tool compared to simple status bars like Waybar. When writing a Quickshell configuration, you are not just changing styles and layouts, but practically programming, which is considerably more complex."*

### Reference showcase configurations

- [[Entities/caelestia]] — opinionated Hyprland + Quickshell rice by Soramane
- [[Entities/dots-hyprland-illogical-impulse]] — end_4's Hyprland + Quickshell rice
- outfoxxed's nixnew modules — NixOS modules for declarative Quickshell config
- KDE Plasma (precedent) — `plasmashell` runs user QML packages; same pattern, larger ecosystem

## Key Insights

1. **The shell is a program, not a stylesheet.** This is the central reframing: once you accept that, the rest of the design (reactive bindings, hot reload, LSP, type imports) follows.
2. **The host's job is to expose system services as QML objects.** Whether the host is `quickshell` or `plasmashell`, the *user-side* pattern is the same — what differs is which integrations are bundled.
4. **Hyprland is the dominant compositor target in the Quickshell ecosystem**, because it ships the protocol extensions (ext-workspace, ext-background-effect/blur, screencopy with Vulkan, session-lock) that a polished shell needs. Quickshell also integrates I3, Sway, and X11, but the showcase configs are Hyprland-based.
5. **Per-distro packaging is mature** — Nix (Nixpkgs + flake mirrors), Arch (core + AUR), Fedora (core + COPR), Debian, Ubuntu PPA, OpenSUSE OBS, Gentoo GURU, Guix.

## Related Concepts

- [[Concepts/hot-reload-qml-config-iteration]] — the iteration loop this pattern enables
- [[Concepts/qtquick-reactive-binding-model]] — the runtime model the pattern relies on

## Related Entities

- [[Entities/quickshell]] — open-source implementation
- [[Entities/qtquick-qml]] — the language/runtime
- [[Entities/hyprland]] — primary compositor target
- [[Entities/caelestia]] — flagship showcase
- [[Entities/dots-hyprland-illogical-impulse]] — flagship showcase

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Original: https://quickshell.org/about