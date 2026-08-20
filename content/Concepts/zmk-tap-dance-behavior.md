---
title: "ZMK Tap-Dance Behavior"
details: "ZMK's 'tap-dance' behavior collapses multiple distinct actions (short press, long press, double-tap, etc.) onto a single physical key. The Corne manual's TD0 example maps short press → Left Shift and double-click → Caps Lock. This is the canonical ZMK pattern for putting two related-but-distinct modifiers on one key without forcing the user onto an awkward layout."
tags:
  - concept
  - hardware
  - firmware
created: 2026-08-20
updated: 2026-08-20
type: concept
sources:
  - .Raw/manuals-plus-corne-mechanical-split-keyboard-2026-08-20.md
---

# ZMK Tap-Dance Behavior

ZMK's `behavior-tap-dance` lets a single physical key produce **different actions based on how the user pressed it**. The Corne manual documents the canonical example:

```dts
td0: td0 {
    compatible = "zmk,behavior-tap-dance";
    label = "TD0";
    #binding-cells = <0>;
    bindings = <&kp LEFT_SHIFT>, <&kp CAPS>;
};
```

This binds **short press → Left Shift** and **double click → Caps Lock** onto one key. The user gets two modifiers in one slot — useful on a 42-key Corne where every key has to earn its place.

## The general pattern

- `bindings` is a list of action cells; the i-th cell is the action emitted on an i-tap sequence (with the *last* cell being the default for "too many taps" or hold).
- `#binding-cells = <0>` declares that this behavior consumes no positional arguments in the keymap; the actions are baked into the behavior definition itself.
- Users add more tap-dance behaviors (`TD1`, `TD2`, ...) by copying the block and changing the `label` and `bindings`.

## Why tap-dance instead of a layer?

A **layer** would also give the user a second action per key, but at the cost of holding a modifier. A tap-dance behavior is **stateless from the user's perspective** — the distinction is whether they tap once or twice, not whether they're holding something down. This keeps the home row free of held modifiers and is critical on a keyboard small enough that held-modifier layers would dominate typing.

## Related: hold-tap (the `&lt` and `&gt` thumb pattern)

The Corne manual uses a different but related pattern for the thumb keys:

```text
&lt 3 SPACE  →  short press: SPACE; long press: layer 3
&gt 3 ENTER  →  short press: ENTER; long press: layer 3
```

`&lt` (layer-tap) and `&gt` (the inverted variant) are **hold-tap behaviors** — the action depends on whether the key was held or tapped. The "3" is the layer number; "SPACE" / "ENTER" is the tap action. This is the pattern that lets a 42-key keyboard have a full layer structure without sacrificing thumb access to space and enter.

The two patterns are complementary: tap-dance distinguishes *count of taps*, hold-tap distinguishes *tap vs hold*. A keyboard designer typically combines both — tap-dance on the home row for shifted/Caps, hold-tap on the thumbs for layer + space/enter.

## Related concepts

- [[Concepts/split-keyboard-firmware-architecture]] — the broader firmware context
- [[Entities/zmk]] — the open-source firmware project
- [[Entities/corne-keyboard]] — the keyboard this behavior was designed for
