---
title: "Hot-Reload QML Config Iteration"
details: "Workflow for iterating on a desktop-shell QML configuration by saving a file and seeing the change applied to the running shell without restart. Quickshell implements this via a file watcher (`QS_DISABLE_FILE_WATCHER` env var to disable); reloads are skipped if file content is unchanged. Reduces the write-evaluate loop to 'save file, look at screen' and is the main reason QML desktop-shell composition is practical despite its higher initial complexity."
tags:
  - concepts
  - architecture-pattern
  - desktop
  - qt
created: 2026-08-31
updated: 2026-08-31
type: concept
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# Hot-Reload QML Config Iteration

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Architecture Pattern
**Status:** Production-validated (Quickshell v0.1.0 → v0.3.x)

## Overview

Hot-reload QML config iteration is the workflow where a desktop shell ([[Concepts/qml-desktop-shell-composition]]) watches the user's QML files and re-applies them to the running shell as soon as they are saved, without restarting the process or losing state. Quickshell's documentation leads with this as the first key feature (*"loads changes as soon as they're saved, letting you iterate as fast as you can type"*) — without it, authoring a QML shell would be a write-compile-restart cycle analogous to writing a C++ GUI in the 1990s.

## Core Content

### Mechanism

1. **File watcher** — Quickshell subscribes to filesystem events on the user's config directory. The v0.3.0 release added `QS_DISABLE_FILE_WATCHER` to disable the watcher, and added a guard that skips reload if the file content did not change (preventing spurious reloads on touched-but-unchanged files).
2. **QML re-parse** — when a watched file changes, Quickshell re-parses it and updates the affected object tree.
3. **State preservation** — object identities and signal connections across reloads are preserved where possible; objects that are no longer referenced are torn down.

### Why it matters for shell authoring

A desktop shell has live state: open windows, current workspace, audio volume, network connections, monitor arrangement. A full restart loses all of that. Hot reload keeps the runtime state and only swaps the description of the UI on top of it. Combined with QML's reactive property bindings ([[Concepts/qtquick-reactive-binding-model]]), this makes authoring feel like editing a live document — save a file, the bar rearranges.

### Failure modes

Quickshell's changelog through v0.1 → v0.3 lists repeated fixes for hot-reload-related crashes:

- Asynchronous loaders not working after reload / before window creation
- `JsonAdapter` crashes/bad data on reload
- `FileView` crashes when watched files update
- IPC calls from children of crashed/relaunched process crashing
- Crashes from accessing freed objects via `ScriptModel`

The recurring pattern: reload tears down an object that something else still holds a reference to, and the second access is a use-after-free. As of v0.3.1 these are largely fixed but the project's own install guide warns the project is pre-1.0 and breaking changes are expected.

### Comparison to related iteration workflows

| Workflow | Iteration unit | Speed | State loss |
|----------|----------------|-------|------------|
| Restart a desktop environment (e.g. `plasmashell --replace`) | whole shell | seconds–minutes | full |
| Reload a status bar (`killall waybar && waybar &`) | single bar | sub-second | bar state only |
| **Hot reload QML config** | individual file | sub-second | none |
| Browser DevTools live CSS edit | CSS file | sub-second | none (DOM preserved) |

## Key Insights

1. **Hot reload is what makes the QML shell composition pattern viable for individuals.** Without it, the cost of authoring would gate the ecosystem to a small set of authors; with it, forking a config and tweaking colors/layouts is approachable for a much wider audience.
2. **Crash fixes during reload are an ongoing investment.** The v0.1 → v0.3 changelog shows roughly a third of bug fixes are reload-cycle-related.
3. **`QS_DISABLE_FILE_WATCHER` and `QS_DISABLE_CRASH_HANDLER`** are escape hatches for users on filesystems (NFS, etc.) where the file watcher misbehaves, or for power users who want fail-fast behavior.

## Related Concepts

- [[Concepts/qml-desktop-shell-composition]] — the pattern this enables
- [[Concepts/qtquick-reactive-binding-model]] — what makes the post-reload state coherent

## Related Entities

- [[Entities/quickshell]] — primary implementation
- [[Entities/qtquick-qml]] — the language being re-parsed

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Original: https://quickshell.org/