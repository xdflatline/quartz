---
title: "Hyprland"
details: "Dynamic tiling Wayland compositor with eye-candy animations, written in C++. Built on wlroots. Provides the ext-workspace, ext-background-effect (blur), screencopy, idle-inhibitor, session-lock, and other protocols that Quickshell uses for window management, blur, screen capture, lockscreens, and idle detection."
tags:
  - entities
  - linux
  - desktop
created: 2026-08-31
updated: 2026-08-31
type: entity
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# Hyprland

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Tool / Window Manager
**Repository:** https://github.com/hyprwm/Hyprland
**Website:** https://hyprland.org/

## Overview

Hyprland is a dynamic tiling Wayland compositor — the layer that owns the screen, places windows, and handles input on Linux desktops using Wayland. It is built on the wlroots library and written in C++, with a Lua-based configuration language (added in newer versions) and an extensive set of Wayland protocol extensions for animations, blur effects, and IPC. It is the most popular target for the [[Entities/quickshell]] desktop-shell ecosystem: the showcase configs [[Entities/caelestia]] and [[Entities/dots-hyprland-illogical-impulse]] are both Hyprland-based, and Quickshell's Hyprland module is the most deeply integrated of its workspace modules (including Lua config support since v0.3.0).

## Key Details

### Compositor role

- Tiling layout engine with per-workspace rules and animations
- Window rules, workspace rules, monitor rules
- Input handling (keyboard, pointer, touch, gestures)
- IPC over Hyprland IPC socket (events and commands)

### Wayland protocol surface (relevant to Quickshell)

- `ext-workspace` — workspace info (Hyprland module is one of the workspace integrations; a generic `WindowManager` interface implementing ext-workspace was added in Quickshell v0.3.0)
- `ext-background-effect` — window blur support (Quickshell v0.3.0)
- `wlr-screencopy` / `ext-image-copy` — screen capture (Quickshell `ScreencopyView`, with Vulkan support since v0.3.0)
- `idle-inhibitor` — Quickshell v0.3.0 exposes Wayland idle inhibitors
- `idle` — Quickshell v0.3.0 adds Wayland idle timeouts
- `session-lock` — Quickshell `WlSessionLockSurface` for lockscreens
- `keyboard-shortcuts-inhibit` — Quickshell v0.3.0 can inhibit compositor shortcuts for focused windows

### Configuration

Hyprland config is a key-value file; v0.3.0 of Quickshell added Lua config support for the Hyprland module, enabling config expressions that read Hyprland state.

## Related Concepts

- [[Concepts/qml-desktop-shell-composition]] — Quickshell + Hyprland is the canonical example

## Related Entities

- [[Entities/quickshell]] — primary Quickshell integration target
- [[Entities/caelestia]] — Hyprland + Quickshell rice
- [[Entities/dots-hyprland-illogical-impulse]] — Hyprland + Quickshell rice

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Website: https://hyprland.org/