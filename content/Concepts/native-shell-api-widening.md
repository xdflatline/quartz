---
title: "Native Shell API Widening"
details: "Apps ship as signed packages that may never be built again, so public APIs must only widen: inputs gain optional members, types only widen, defaults and behavior stay, modes are string unions rather than booleans, functions return objects rather than tuples, and a rename keeps the old name as a deprecated alias."
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
---
# Native Shell API Widening

**Source:** [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## Why Widening Only

Apps are delivered to host apps as **signed packages and may never be built again**: every later release of NSH runs them as they are. Apply the same discipline to what an app or a component library exposes to others — its components' props and events, its crate's exports, the functions a host app's native components and modules receive.

The rules:

- inputs gain **optional members** only; types only widen; defaults and behavior stay (new behavior is opt-in);
- a function whose parameters may grow takes its options as one object (`scrollTo({ x, y, animated })`), never a further positional parameter; parameters that never will, such as a range's start and end, stay positional;
- a **mode is a string union**, which can gain values, rather than a boolean that later needs a third state;
- a value has one type: `version: string`, never `string | number`;
- what a function returns is an **object**, which can gain a field, rather than a tuple or a bare value;
- a function returning a Promise reports every failure by rejecting it, and a failure the caller can handle carries a `code`, as NSH's own do: callers branch on codes, while messages are for people and may change;
- a **rename keeps the old name** as a `@deprecated` alias of the same implementation.

## Public API Design for Reusable Components

- props establish valid defaults: `#[prop(default)]` or `#[prop(default = …)]` in Rust, `??` where the prop is read in TSX;
- every prop, event and export has a doc comment; in Rust it becomes the TypeScript declaration TSX sees;
- callbacks describe requested changes and include pointer details only when they are meaningful;
- explicit parts, slots and render functions are preferable to inspecting arbitrary descendants;
- adding reusable behavior must not force a product-level visual choice.

## Rust Struct Field Visibility

In Rust, **private fields are the default** for behavioral state that must evolve without breaking callers. Public fields are appropriate for deliberately record-like configuration and serialized data.

Every public struct with public fields must carry `#[non_exhaustive]` and implement `Default`, so callers can create values without exhaustive struct literals and a field can be added without breaking them.

## Stable Import Paths

Keep public import paths stable while reorganizing internals: a crate's `#[native_module]` specifier and its exports, and a TSX module's exports, are what other code imports.

Prefer platform control terminology and NSH's established naming over web-framework vocabulary. See [[Concepts/native-shell-ui-language|Native Shell UI Language]] for the naming table and the precise domain words.

## Callback and Event Wording

Every event passes one object, even with one field and for a value's change too, its fields named as the props they report: `onChange({ value })`, `onOpenChange({ open, reason })`, `onLinkPress({ url })`. A later field is then an addition.

- Name the act, not past tense or a request: `onPress`, `onClose`, `onCancel`, `onBackPress`.
- Name the intent rather than the geometry when the act has a name: `onLoadMore`, not "the end was reached".
- Lifecycle pairs are `onOpen` / `onClose`; phases are `Start` / `End`, never `Begin`.
- Document whether a callback runs before or after the component's own state changes, and whether it may re-enter the component.

## Related Concepts

- [[Concepts/native-shell-ui-language|Native Shell UI Language]] — the vocabulary rules that make a public API legible
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — what a reusable component may and may not expose
