---
title: "QtQuick / QML"
details: "Declarative UI framework from the Qt project. QML is the JSON-like interface description language; QtQuick is the runtime scene-graph (rendering, animation, event delivery) it describes. Used by Quickshell, KDE Plasma, Sailfish OS, and many embedded HMI projects."
tags:
  - entities
  - qt
  - desktop
created: 2026-08-31
updated: 2026-08-31
type: entity
source: "[[Raw/quickshell-org-docs-bundle-2026-08-31]]"
---

# QtQuick / QML

**Source:** Documentation bundle ([[Raw/quickshell-org-docs-bundle-2026-08-31]])
**Category:** Framework / Language
**Website:** https://doc.qt.io/qt-6/qtqml-index.html
**Maintainer:** The Qt Company / KDE community

## Overview

QtQuick is the declarative UI framework shipped as part of Qt. QML (Qt Modeling Language) is the language used to describe a QtQuick scene: a tree of objects with declarative property bindings, signal handlers, and JavaScript-like expressions. The QtQuick runtime provides the scene graph, animation system, and event delivery that the QML describes. Quickshell uses QtQuick as its UI substrate — the user's config is QML, and the shell host supplies the C++/Qt side that hosts the scene graph and exposes system services as QML objects ([[Concepts/qtquick-reactive-binding-model]]).

## Key Details

### QML as a language

- **Object tree:** every QML document is a tree of nested objects (`Item`, `Window`, custom types)
- **Property bindings:** `property int x: parent.width / 2` — bindings re-evaluate when their dependencies change
- **Signal handlers:** `onTriggered: ...`, `onClicked: ...` etc.
- **Custom properties:** declared inline with `property <type> <name>: <default>`
- **JavaScript expressions:** inline for non-trivial logic; standalone JS files for reuse
- **Imports:** `import QtQuick`, `import QtQuick.Controls`, `import Quickshell` (for the Quickshell-specific types)

### QtQuick as a runtime

- Hardware-accelerated scene graph (OpenGL / Vulkan / Metal / Direct3D backends)
- Animation system — properties can be smoothly animated when changed
- Touch / pointer / keyboard event delivery
- Layouts (anchors, Row/Column/Grid)
- Item-level effects (multi-effect shaders, gaussian blur via `qt5compat`)

### Tools

- `qmlls` — the official QML language server (used by Quickshell for LSP support)
- `qmlscene` / `qml` — quick QML preview runners
- Qt Creator — IDE with first-class QML support
- Tree-sitter grammars: `yuja/tree-sitter-qmljs`, `tree-sitter-qmljs`

### Adoption beyond Quickshell

- KDE Plasma — Plasma 5 and 6 use QML extensively for plasmashell, panels, and system tray
- Sailfish OS — the mobile OS UI is QML
- Ubuntu Touch (Lomiri) — QML-based shell
- Many embedded automotive / industrial HMIs

## Related Concepts

- [[Concepts/qtquick-reactive-binding-model]] — how QML property bindings and signals drive reactive UIs
- [[Concepts/qml-desktop-shell-composition]] — the pattern of using QML scenes as desktop shell components

## Related Entities

- [[Entities/quickshell]] — uses QtQuick as its UI substrate

## References

- Raw Article: [[Raw/quickshell-org-docs-bundle-2026-08-31]]
- Official index: https://doc.qt.io/qt-6/qtqml-index.html