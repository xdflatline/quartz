---
title: "Native Shell Layered Architecture"
details: "Native Shell's dependency direction: app shell over pages over app components over a component library over nsh/base over nsh. Higher layers own domain meaning and orchestration; lower layers own reusable presentation or behavior. A reusable component must never depend on an app page, and a component library must never depend on one app's theme."
tags:
  - concept
  - desktop
  - architecture-pattern
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-coding-guides.md
---
# Native Shell Layered Architecture

**Source:** [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## Overview

Native Shell (NSH) organizes an application as a stack of layers with a **strict downward dependency direction**. Higher layers own domain meaning and orchestration; lower layers own reusable presentation or behavior. The guide's first rule about layering is negative and therefore easy to get wrong: *do not make a reusable component depend on an app page, and do not make a component library depend on one app's theme.*

The layering exists so that different engineers — or different coding agents — can work on separate pages in parallel with fewer file conflicts and less shared-state coupling.

## The Layers

| Layer | Owns | Contains |
|---|---|---|
| **App shell** | Composing root and navigation stacks | `App.tsx` entry (or `nsh.json` `"root"`), the root surface, navigation stacks |
| **Page** | One `NavPage`'s content, dialogs, and started work | `pages/Inbox.tsx` |
| **App component** | A repeated domain-aware pattern | `components/Card.tsx` |
| **Component library** | Styled, general-purpose UI | The app's own library or a community one, built on `nsh/base` |
| **`nsh/base`** | Reusable behavior without product presentation | Navigation, dialogs, popovers, menus, sheets, a press target |
| **`nsh`** | Primitives | Styles, layout, reactivity, the environment |

## File Layout by Convention

Nothing is configured; NSH finds these by convention:

```
App.tsx            # the entry, by convention: mount(App)
nsh.json
Cargo.toml         # the app's crate, with Rust components ("rust": ".")
src/
  lib.rs
pages/
  Inbox.tsx
  Compose.tsx
  Settings.tsx
components/
  Card.tsx
store.ts
```

- `pages/` holds one file per `NavPage`. A page grows into more files only when it needs them.
- `components/` holds the app's reusable components, the ones several pages use.
- `store.ts` holds the app's state: its signals and the functions that change them. Pages read the signals and call the functions.
- Tests are `*.test.tsx` files beside what they test.
- `Cargo.toml` and `src/lib.rs` are the app's own crate, with its Rust components (`nsh.json` `"rust": "."`); its `#[native_module]` in `src/lib.rs` names what TSX imports.

## The App Shell Composes, It Does Not Orchestrate

The shell composes pages but contains little page logic. Pages read the store's signals and call its functions; **they never write another page's state**. The store's signals stay private, and only what reads and changes them is exported, so mutable state sits behind its public functions:

```rust
/// The app's workspace: its state stays behind these functions.
#[derive(Clone, Copy)]
pub struct Workspace {
    name: Signal<SharedString>,
}

impl Workspace {
    /// A workspace named "Untitled".
    pub fn new() -> Self {
        Self { name: signal(SharedString::from("Untitled")) }
    }

    /// Its name (tracked where it is read).
    pub fn name(&self) -> SharedString {
        self.name.get()
    }

    /// Renames it.
    pub fn rename(&self, name: impl Into<SharedString>) {
        self.name.set(name.into());
    }
}
```

## The Acyclic Shape

```
App.tsx ──▶ pages/ ──▶ store.ts
              └──────▶ components/ ──▶ nsh/base, nsh
```

Pages may depend on the store and on components, but **not** on the shell or on another page's private parts. If one page must change what another shows, it does so through the store.

A page may hold the workspace and pass its *id* to search; search does not need the workspace's whole collection or its private signals. Passing the narrowest handle keeps the dependency acyclic.

## Root Ownership

Mount the app once. The root fills the surface with `flex: 1` and a background from the theme, and coordinates what belongs to the whole surface: the navigation stack, the dialogs, popovers, menus, sheets and tooltips shown over everything in it, and the safe area.

```rust
#[component]
pub fn App() -> impl IntoElement {
    provide_context(Workspace::new());
    view()
        .flex_1()
        .bg(move || theme().background)
        .child(inbox())
}
```

**One surface is one engine.** Each `NshAppView`, `NshView` or `AppView` a native app embeds runs its own VM, its own module state and its own reactive graph, so several surfaces in one host app never share state by accident. Do not mount a second root for each page inside one surface.

## Related Concepts

- [[Concepts/native-shell-state-ownership|Native Shell State Ownership]] — where each kind of state lives inside these layers
- [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] — why a component body runs once and bindings re-run
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — the durable rule separating `nsh/base` from the app's styled layer
- [[Concepts/native-shell-design-system|Native Shell Design System]] — the visual rules that govern the app's own component layer
