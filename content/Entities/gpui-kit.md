---
title: "GPUI Kit"
details: "GPUI Kit is the desktop UI kit whose product judgment Native Shell carried over: an interface should feel native, restrained, precise and understandable without guesswork. Its gpui-base, GPUI and gpui-component crates are the second tier of NSH's vocabulary lookup order, after NSH's own API."
tags:
  - entity
  - desktop
  - tooling
created: 2026-10-30
updated: 2026-10-30
type: entity
sources:
  - Raw/nsh-design-guides.md
  - Raw/nsh-coding-guides.md
---
# GPUI Kit

**Source:** [[Raw/nsh-design-guides]], [[Raw/nsh-coding-guides]]
**Type:** Desktop UI Kit

## Overview

GPUI Kit is the desktop UI kit that [[Entities/native-shell-nsh|Native Shell (NSH)]] inherits from. The NSH design guides describe themselves as recording "the product judgment GPUI Kit accumulated through years of desktop work, carried over to NSH":

> an interface should feel native, restrained, precise, and understandable without guesswork.

## Role in NSH's Vocabulary

The coding guides set the **vocabulary lookup order** for naming a prop or an event:

1. NSH's own API;
2. GPUI Kit's `gpui-base`, GPUI and `gpui-component`;
3. the platforms' controls.

This is a deliberate discipline against web-framework vocabulary drifting into a native framework. See [[Concepts/native-shell-ui-language|Native Shell UI Language]].

## The Rust-to-TSX Property Convention

NSH's component prop and event naming follows a table that is itself derived from this lineage:

| Concept | Naming pattern | Example |
|---|---|---|
| A component | A noun, `PascalCase` | `Button`, `Dialog`, `QuantityStepper` |
| Its props and events (Rust) | `<Component>Props`, `<Component>Event` | `ButtonProps`, `ButtonEvent::Press` → `onPress` |
| A behavior's state object | `<Control>State`, made by `create<Control>` | `NavStackState`, `createNavStack` |
| Why a value changed | `<Control>ChangeReason`, a string union | `DialogChangeReason`: `"cancel"`, `"backdropPress"` |
| A state | An adjective, positive, no `is` prefix | `open`, `hidden`, `disabled`, `selected`, `checked`, `readonly` |
| A value's change | `on<Value>Change({ <value>, ... })`, one object | `onChange({ value })` |

## Related Concepts

- [[Entities/native-shell-nsh|Native Shell (NSH)]] — the framework that carried the judgment over
- [[Concepts/native-shell-ui-language|Native Shell UI Language]] — the vocabulary rules that trace back here
