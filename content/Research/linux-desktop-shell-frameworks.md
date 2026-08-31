---
title: "Linux Desktop-Shell Frameworks"
details: "Survey of the architectural space Quickshell occupies — declarative, QML-configured, Wayland-integrated shell frameworks for status bars, widgets, lockscreens, and display managers. Synthesizes the QML desktop-shell composition pattern, hot-reload iteration, and the QtQuick reactive binding model across the Quickshell, KDE Plasma, and broader Linux desktop ecosystems."
tags:
  - research
  - linux
  - desktop
  - qt
  - survey
created: 2026-08-31
updated: 2026-08-31
type: research
sources:
  - "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# Research Index: Linux Desktop-Shell Frameworks

**Updated:** 2026-08-31
**Source:** [[Raw/quickshell-org-docs-bundle-2026-08-31]] (quickshell.org home, about, install, changelog v0.1.0 → v0.3.1)

---

## Overview

This index covers the architectural space of declarative, QML-configured desktop shells on Linux — the niche where the user's shell configuration is a program written in QML rather than a static style file. Quickshell is the focal point (v0.3.1, 2026-08-20); the broader space includes KDE Plasma (the large-scale precedent), Sailfish OS, and Ubuntu Touch / Lomiri. The survey is grounded in the Quickshell documentation bundle but extends to the wider QML-as-shell pattern.

## Concepts

### Architectural patterns
- [[Concepts/qml-desktop-shell-composition]] — the shell-as-QML-program pattern; user-authored scenes importing bindings to the compositor and system services
- [[Concepts/hot-reload-qml-config-iteration]] — save-to-reload iteration loop that makes authoring tractable
- [[Concepts/qtquick-reactive-binding-model]] — declarative property bindings that propagate state changes automatically

## Tools & Projects

### Shell runtimes
- [[Entities/quickshell]] — open-source QML shell toolkit (v0.3.1, 2026-08-20); primary integrator of Wayland protocols, Hyprland, Pipewire, BlueZ, UPower, MPRIS, Polkit, greetd
- [[Entities/qtquick-qml]] — the underlying declarative language and scene-graph runtime from Qt

### Compositors (primary integration targets)
- [[Entities/hyprland]] — dynamic tiling Wayland compositor with the protocol extensions (ext-workspace, blur, screencopy, session-lock) the polished shell ecosystem relies on
- (Not yet ingested) Sway, I3 — i3-compatible Wayland/tiling WMs that Quickshell integrates

### Showcase shell configurations
- [[Entities/caelestia]] — Soramane's Hyprland + Quickshell rice (caelestia-dots/shell)
- [[Entities/dots-hyprland-illogical-impulse]] — end_4's Hyprland + Quickshell rice
- (Not yet ingested) Zephyr, outfoxxed's nixnew modules — additional showcases listed on quickshell.org

## Raw Sources

- [[Raw/quickshell-org-docs-bundle-2026-08-31]] — homepage, about, install, and changelog bundle retrieved 2026-08-31

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [quickshell.org/](https://quickshell.org/) | Homepage | 2026-08-31 | Tagline, features, code example, showcase configs |
| [quickshell.org/about](https://quickshell.org/about) | About | 2026-08-31 | Built-in integrations list, "Is Quickshell for me?" |
| [quickshell.org/docs/v0.3.0/guide/install-setup](https://quickshell.org/docs/v0.3.0/guide/install-setup) | Install | 2026-08-31 | Per-distro install, optional deps, editor configs |
| [quickshell.org/changelog](https://quickshell.org/changelog) | Changelog | 2026-08-31 | v0.1.0 → v0.3.1 release notes (truncated extraction) |

## Cross-Cutting Themes

### 1. The shell is a program, not a stylesheet
The central reframing across the entire pattern. Once accepted, the rest of the design follows — reactive bindings ([[Concepts/qtquick-reactive-binding-model]]) eliminate imperative update code, hot reload ([[Concepts/hot-reload-qml-config-iteration]]) keeps the iteration loop tight, and the shell host's only job is to expose system services as QML objects.

### 2. Hyprland is the protocol-extension-rich compositor
Polished shells need ext-workspace, ext-background-effect (blur), screencopy, session-lock, idle-inhibitor, keyboard-shortcuts-inhibit — most of which Hyprland ships or Quickshell consumes. Sway/I3 users get a working shell but lose the blur/animation polish that the Hyprland showcase configs demonstrate.

### 3. Crash-fix density during reload cycles
Roughly a third of Quickshell v0.1 → v0.3 bug fixes are reload-cycle-related (use-after-free when an object is torn down but still referenced). The pattern is mature but not yet boring.

### 4. Per-distro packaging has converged
Quickshell v0.3.x is packaged for Nix (Nixpkgs + flake), Arch (core + AUR), Fedora (core + COPR), Debian, Ubuntu PPA, OpenSUSE OBS, Gentoo GURU, and Guix. No major Linux family is missing — a sign the ecosystem treats the project as stable enough to ship.

### 5. Editor integration is a first-class concern
Quickshell's install page includes editor configs for Emacs (`qml-ts-mode`), Neovim (`nvim-lspconfig`), Helix (built-in), and VSCode (`qt-qml.qmlls.useQmlImportPathEnvVar`). `qmlls` (the official QML language server) is the LSP backend for all of them. The config-as-program posture demands serious editing tooling.

## Next Research Directions

- **Evaluate** whether to ingest Sway/I3 docs as separate [[Entities/]] pages, given Quickshell's workspace integrations include them alongside Hyprland
- **Survey** the broader QML-as-shell space (KDE Plasma plasmoids, Sailfish OS Silica, Lomiri) to compare the same pattern at different scales
- **Compare** Quickshell's hot-reload model to other live-reload UI toolchains (React Fast Refresh, SwiftUI Previews, Flutter Hot Reload) — the conceptual overlap is strong but the implementation differs
- **Investigate** the Pipewire audio-peak-detection module (`PwNodePeakMonitor`) and the broader audio integration — likely a reusable pattern for cross-platform audio metering UIs
- **Test** the actual install-and-configure flow on a NixOS system using outfoxxed's flake, to verify the docs match reality

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Original: https://quickshell.org/