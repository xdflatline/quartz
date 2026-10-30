---
title: "Native Shell (NSH)"
details: "Native Shell is a cross-platform application framework for phones, tablets, desktops and the web, with Rust and TSX authoring. It renders with each platform's own UI, provides behavior-only components in nsh/base, and leaves visual policy to the app. Developed by Longbridge; the guides inherit GPUI Kit's desktop product judgment."
tags:
  - entity
  - desktop
  - tooling
  - documentation
created: 2026-10-30
updated: 2026-10-30
type: entity
sources:
  - Raw/nsh-design-guides.md
  - Raw/nsh-coding-guides.md
---
# Native Shell (NSH)

**Source:** [[Raw/nsh-design-guides]], [[Raw/nsh-coding-guides]]
**Official Site:** https://nsh.dev/
**Repository:** https://github.com/longbridge/nsh
**Org:** Longbridge

## Overview

Native Shell (NSH) is a **cross-platform application framework** for phones, tablets, desktops and the web, and often inside a host app. Authors write either **TSX modules** (an interpreted dialect) or **Rust components**; apps can be entirely in Rust, entirely in TSX, or mix them.

Its central architectural bet is a **three-layer split**:

1. `nsh` — the primitives: styles, layout, reactivity, and the environment;
2. `nsh/base` — reusable *behavior* without product presentation: navigation, dialogs, popovers, menus, sheets, a press target;
3. the app's own styled layer — the product's visual language.

NSH renders with each platform's own UI and leaves the look to the app. `nsh/base`'s components bring **behavior, state, focus and accessibility**; every color, size, radius and spacing comes from the app's own components.

## Design Lineage

The design guides record the **product judgment GPUI Kit accumulated through years of desktop work, carried over to NSH**. The coding guides likewise place GPUI Kit's `gpui-base`, GPUI and `gpui-component` first in the vocabulary lookup order, after NSH's own API and before the platforms' controls. See [[Entities/gpui-kit|GPUI Kit]].

NSH also borrows from **shadcn/ui** — specifically the *method* (own the top layer, compose predictable parts, ship dependable defaults, keep code legible to people and AI, separate behavior primitives from the styled layer), not the look. See [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]].

## Authoring Surface

| Language | Use for |
|---|---|
| **Rust** | Component libraries and demanding logic — native code from start to end |
| **TSX** | What changes often or is delivered at run time (its code runs in an interpreter, so costs multiply) |

A `#[component]` has typed props (`#[derive(Props)]`) and events (`#[derive(Event)]`); TSX imports it with declarations generated from them. Retained state that TSX uses with `new` is a `#[class]`, and functions are a `#[module]`.

## Runtime Model

NSH is **retained state with declarative construction**, on Solid's model — see [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]]. The reactive graph, renderer, layout and lists are native; one turn of the app's code becomes one batch of native operations.

Each `NshAppView`, `NshView` or `AppView` a native app embeds runs **its own VM, its own module state and its own reactive graph**, so several surfaces in one host app never share state by accident.

## Platform Reach

Apps run on phones, tablets, desktops and the web, and often inside a host app. The guides require designing for each:

- **System UI keeps the platform's look** — on iOS and Android a page's header is the system's; the desktops and the web show the page's `header` slot, which the app draws.
- **The host's theme** — an embedded app can be given its host's theme, and token-reading classes follow it natively.
- **Safe areas and the keyboard** — `env(safe-area-inset-*)`, `env(keyboard-inset-height)`.
- **Appearance, text size, and motion** — every surface works in light and dark, at the user's text size, with reduced motion.
- **Right to left** — start and end properties mirror.
- **Touch and pointer** — touch targets at least 44 × 44 points; hover and tooltips exist only with a pointer.

## Capability Model

An app declares what it reaches outside its VM in `nsh.json` `"capabilities"`: the hosts it fetches from, the pages a web view shows, the clipboard, the status bar. An app that will be delivered into other apps lists exactly what it uses, and handles a **refused** request as it handles a failed one: a host app may grant less than the app declares.

## Published Guides

- **Design Guides** — [[Raw/nsh-design-guides]]
- **Coding Guides** — [[Raw/nsh-coding-guides]]

## Related Concepts

- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layered dependency direction
- [[Concepts/native-shell-design-system|Native Shell Design System]] — the visual rules for the app's styled layer
- [[Concepts/native-shell-state-ownership|Native Shell State Ownership]] — the narrowest-owner rule
- [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] — the runs-once model
- [[Concepts/native-shell-api-widening|Native Shell API Widening]] — the signed-package contract
- [[Concepts/native-shell-ui-language|Native Shell UI Language]] — the wording rules
- [[Concepts/semantic-color-tokens|Semantic Color Tokens]] — resolving colors by role
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — the Base/app split
- [[Concepts/stable-domain-identity|Stable Domain Identity]] — keys as behavior
