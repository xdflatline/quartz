---
title: "Behavior Presentation Boundary"
details: "Base owns reusable behavior and the structure required to implement it; the presentation layer owns the product's visual language. 'Unstyled' does not mean 'one empty view' - overlay placement, keyboard navigation, editing, virtualization, back navigation, dismissal and safe areas require internal structure. Base must not choose brand colors, typography, density, icons, variants or strings."
tags:
  - concept
  - desktop
  - architecture-pattern
  - software-engineering
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-coding-guides.md
  - Raw/nsh-design-guides.md
---
# Behavior Presentation Boundary

**Source:** [[Raw/nsh-coding-guides]], [[Raw/nsh-design-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## The Durable Rule

> Base owns reusable behavior and the structure required to implement it. The presentation layer owns the product's visual language.

## "Unstyled" Does Not Mean "One Empty View"

Moving internal structure out to every caller would not create flexibility — it would duplicate fragile behavior. Overlay placement, keyboard navigation, editing, virtualization, back navigation, dismissal and safe areas all require internal structure and state.

This is the discipline NSH inherits from Shadcn's most useful contribution, which was never a particular border color but a way of building a system:

- own the top layer of the interface instead of fighting a sealed abstraction;
- compose small, predictable parts into product-specific components;
- provide defaults that already form one visual language;
- keep the code and composition legible to both people and AI;
- **separate behavior primitives from the styled layer.**

## What Base Must Not Decide

Base must not choose brand colors, typography, density, final icons, component variants, strings or application composition. Instead, expose presentation through:

- `class` / `style` on the main part;
- `<part>Class` / `<part>Style` for every other part;
- typed state styles (`active`, `hover`, `focus`, `selected`, `checked`, `disabled`);
- named slots (`trigger`, `header`, `footer`);
- render functions.

Do not inspect arbitrary descendants to discover titles, descriptions or close buttons: make semantic parts explicit, and take every label as a prop or a child.

## Where Reusable Behavior Goes

Move reusable behavior without product styling to `nsh/base`, or to a crate the app's products share; keep themed, opinionated presentation in the application's components.

Reusable behavior belongs in `nsh/base`; visual policy stays above it. Applications build their components on `nsh/base`, in TSX or in the app's Rust crate.

## Composing From the Standard Component

Compose from the standard semantic component before building a custom surface. Do not reproduce a menu, a popover, a sheet or a dialog from generic views merely to match one screenshot.

`Menu`, `ContextMenu`, `Popover`, `Sheet`, `Tooltip` and `Dialog` from `nsh/base` preserve placement, focus transfer, keyboard navigation, selection, disabled state, dismissal on Escape and back, and the accessibility contract. If the standard component cannot express a recurring valid pattern, **improve its explicit API** instead of styling arbitrary descendants at each call site.

This is also why the design guide forbids custom pressable views where a semantic component already supplies focus, keyboard, disabled and accessibility behavior.

## The Three Layers

NSH applies the Shadcn ideas through the split between:

1. the primitives of `nsh`;
2. the unstyled base components of `nsh/base`;
3. the styled layer, which belongs to the app.

## Element Families Are Not Interchangeable

Do not force every component into one template. The ecosystem contains:

- **semantic elements** such as `Button`, `Switch` and `MenuItem`;
- **compound behavior roots** such as `Dialog`, `Popover`, `Menu`, `ContextMenu`, `Sheet` and `NavStack`;
- **stateful systems** such as `Input`, `List`, `TextView` and a navigation stack's state;
- **infrastructure** such as overlays and their placement, virtualization, scrolling, safe areas, the keyboard and animation.

An element may be internally complex and still be value-like to its caller. A stateful system may expose render functions so apps own presentation without reimplementing behavior. **Choose the public seam from the behavior, not from how many views appear in its output.**

`Menu`, `ContextMenu`, `Popover`, `Sheet`, `Dialog` and `AlertDialog` are not interchangeable boxes: each owns different selection, focus, keyboard, dismissal and layout contracts, and takes its own form on each device.

## Related Concepts

- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layered dependency direction this boundary implements
- [[Concepts/native-shell-design-system|Native Shell Design System]] — the visual language the presentation layer owns
- [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] — the runs-once model the base layer is built on
