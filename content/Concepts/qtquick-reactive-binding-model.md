---
title: "QtQuick Reactive Binding Model"
details: "Runtime model used by QtQuick/QML where declarative property expressions like `color: timer.invert ? \"purple\" : \"green\"` are tracked by the engine and re-evaluated automatically whenever any dependency (the `timer.invert` property) changes. Combined with signal handlers (`onTriggered: ...`) it provides a reactive UI substrate without explicit subscribe/unsubscribe code. The model is the foundation Quickshell's hot-reload iteration loop ([[Concepts/hot-reload-qml-config-iteration]]) and shell composition pattern ([[Concepts/qml-desktop-shell-composition]]) rely on."
tags:
  - concepts
  - architecture-pattern
  - qt
created: 2026-08-31
updated: 2026-08-31
type: concept
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# QtQuick Reactive Binding Model

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Architecture Pattern
**Status:** Production-validated (Qt 4.7+ / QtQuick 1.0+)

## Overview

In QtQuick/QML, a property's value can be declared as an expression rather than a literal — and the QML engine tracks which other properties that expression depends on, then re-evaluates the expression whenever any dependency changes. Combined with signals (`onTriggered`, `onClicked`) and imperative JavaScript, this gives a reactive UI runtime where the *description* of state (the binding graph) is separate from the *propagation* of state changes (the engine). The Quickshell homepage leads with this example — a `Timer` toggling a custom `invert` property and the window's `color` binding updating automatically — because it is the smallest possible demo of the model.

## Core Content

### Three primitives

1. **Property bindings** — `color: timer.invert ? "purple" : "green"`. The engine parses the expression, identifies that `timer.invert` is read, and subscribes the binding to `invert`'s change signal. When `invert` changes, the engine re-evaluates and assigns the new value.

2. **Custom properties** — declared inline: `property bool invert: false`. Adds a QML-level property to the object, with default, type, and (optional) change signal. Custom properties participate in the binding system identically to built-in properties.

3. **Signal handlers** — `onTriggered: timer.invert = !timer.invert`. Imperatively respond to a signal; the *handler* runs side effects, the *binding* drives declarative state. Bindings and handlers are deliberately separated — assigning to a property inside a binding destroys the binding (the property is now imperative, not declarative).

### What the engine does for you

- Tracks dependencies at parse/evaluate time, not at runtime introspection time — cheap
- Breaks cycles automatically — if A depends on B and B on A, the engine gives up and uses the literal default
- Preserves identity across hot reload — a property's binding may be torn down and rebuilt, but the object identity and connections to other objects persist where possible
- Animates property changes — when a bound value changes, the scene graph can smoothly transition (default behavior is instant; explicit `Behavior on x { NumberAnimation { ... } }` for animation)

### Why this matters for desktop shells

Without reactive bindings, a shell would have to imperatively update the bar's volume slider whenever audio changes, update the clock every second, redraw the workspace indicator on workspace switch, etc. With bindings, each of those updates is a single declarative expression (`volumeSlider.value: pipewire.volume`) that is automatically maintained by the engine. Combined with hot reload ([[Concepts/hot-reload-qml-config-iteration]]) and the shell composition pattern ([[Concepts/qml-desktop-shell-composition]]), the author only describes the desired state — propagation is free.

### Anti-patterns

- **Imperative assignment breaks bindings.** `onSomeSignal: foo.bar = 42` severs the binding on `foo.bar`. Use a separate intermediate property if you need to mix imperative and declarative.
- **Bindings over complex expressions get expensive.** The engine re-evaluates on every dependency change; if the expression is a heavy computation, wrap it in a function and call it from a binding to a cheap flag.
- **Bindings don't survive QML re-instantiation.** They survive hot reload (same object identity), but if the object is destroyed and recreated, the binding is rebuilt from scratch.

## Key Insights

1. **The QML binding model is to UI what React's hooks-with-deps are to component logic** — but operating at the property level rather than the component level, with declarative rather than declarative-or-imperative semantics.
2. **Signals + bindings + JS = reactive UI without a virtual DOM.** QtQuick predates and differs structurally from React/SwiftUI/Flutter's render-tree approaches; the comparison is conceptual, not implementation.
3. **The model's biggest win in a desktop shell is wiring UI to live system state.** Each compositor/audio/network integration is exposed as a QML object with properties, and the user's bar/widget code is pure bindings.

## Related Concepts

- [[Concepts/hot-reload-qml-config-iteration]] — relies on bindings being preserved across reload
- [[Concepts/qml-desktop-shell-composition]] — uses bindings as the primary state-propagation mechanism

## Related Entities

- [[Entities/qtquick-qml]] — the language/runtime
- [[Entities/quickshell]] — the open-source implementation that exposes system services as bindable QML objects

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Official QML intro: https://doc.qt.io/qt-6/qtqml-index.html