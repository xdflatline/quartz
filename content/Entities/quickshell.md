---
title: "Quickshell"
details: "QtQuick-based toolkit for building Linux desktop shells (status bars, widgets, lockscreens, display managers) configured in QML with hot reload. Integrates Wayland/X11 windowing, Hyprland/I3/Sway workspaces, Pipewire audio, BlueZ, UPower, MPRIS, StatusNotifierItem, Polkit, and greetd. Latest release v0.3.1 (2026-08-20); pre-1.0, breaking changes expected."
tags:
  - entities
  - linux
  - desktop
  - qt
  - widget
created: 2026-08-31
updated: 2026-08-31
type: entity
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# Quickshell

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Tool / Framework
**Repository:** https://git.outfoxxed.me/quickshell/quickshell (mirrored to https://github.com/quickshell-mirror/quickshell)
**Website:** https://quickshell.org/
**Latest Release:** v0.3.1 — 2026-08-20
**Tagline:** *building blocks for your desktop*

## Overview

Quickshell is a low-level toolkit for composing a Linux desktop shell from declarative QML scenes. Unlike simple status bars (Waybar, waybar-style config files), Quickshell configurations are full programs: the user writes QML that wires QtQuick primitives to system services, and Quickshell loads, runs, and hot-reloads that QML on top of the user's existing Wayland compositor or X11 window manager. It occupies a similar role to KDE Plasma's QML engine, but is composable rather than tied to a full desktop environment.

## Key Details

### Built-in integrations

The runtime ships with bindings for the system services a desktop shell needs:

- **Windowing:** Wayland and X11 window creation (`FloatingWindow`, `PanelWindow`)
- **Window management & screen capture:** Wayland protocols (ext-workspace, ext-background-effect for blur, screencopy with Vulkan support as of v0.3.0)
- **Tiling workspaces:** Hyprland, I3, Sway (Hyprland module supports Lua config since v0.3.0)
- **Audio:** Pipewire, including `PwNodePeakMonitor` for level meters and service auto-reconnect
- **Bluetooth:** BlueZ
- **Authentication:** PAM (lockscreens), Polkit agent (v0.3.0), greetd (display manager)
- **Power:** UPower, Power Profiles Daemon
- **Media:** MPRIS (player control, metadata), StatusNotifierItem (system tray)
- **Networking:** network management support added in v0.3.0

### Hot reload

Files saved on disk are reloaded by the running shell without restart — see [[Concepts/hot-reload-qml-config-iteration]]. Reloads are skipped if file content is unchanged (v0.3.0).

### Iteration language

The config is QML (QtQuick), with property bindings evaluated reactively — see [[Concepts/qtquick-reactive-binding-model]]. An official LSP (`qmlls`) is integrated and the docs include editor configs for Emacs (`qml-ts-mode`), Neovim (`nvim-lspconfig`), Helix, and VSCode.

### Platform support

Packages available for Nix (Nixpkgs + embedded flake mirrors), Arch (`quickshell` in core, `quickshell-git` in AUR), Fedora (core + errornointernet COPR), Debian, Ubuntu (avengemedia/danklinux PPA), OpenSUSE (OBS `home:AvengeMedia:danklinux`), Gentoo (GURU overlay), and Guix (`(gnu packages wm)`).

### Status

Pre-1.0 — the project warns that breaking changes are expected before 1.0, and the v0.3.0 changelog already introduced one: config paths are no longer canonicalized (shell id is derived from the symlink path), so users on symlinked configs may need to migrate their config/state/cache directories.

### Showcase configurations

Quickshell is the runtime target for several end-user desktop configurations ([[Concepts/qml-desktop-shell-composition]]):

- [[Entities/caelestia]] — Soramane's rice ([caelestia-dots/shell](https://github.com/caelestia-dots/shell))
- [[Entities/dots-hyprland-illogical-impulse]] — end_4's rice ([dots-hyprland](https://github.com/end-4/dots-hyprland))
- Zephyr — flickowoa ([zephyr](https://github.com/flickowoa/zephyr))
- outfoxxed's [nixnew/modules/quickshell](https://git.outfoxxed.me/outfoxxed/nixnew/src/branch/master/modules/user/modules/quickshell) — a NixOS modules approach to composing Quickshell configs

## Related Concepts

- [[Concepts/qml-desktop-shell-composition]] — the architectural pattern Quickshell implements
- [[Concepts/hot-reload-qml-config-iteration]] — the iteration loop Quickshell enables
- [[Concepts/qtquick-reactive-binding-model]] — the runtime model Quickshell's QML config relies on

## Related Entities

- [[Entities/qtquick-qml]] — the language/runtime underneath Quickshell
- [[Entities/hyprland]] — primary compositor integration target
- [[Entities/caelestia]] — flagship showcase config
- [[Entities/dots-hyprland-illogical-impulse]] — second flagship showcase config

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Original: https://quickshell.org/