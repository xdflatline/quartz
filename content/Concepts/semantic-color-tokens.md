---
title: "Semantic Color Tokens"
details: "Colors are resolved from the theme by semantic role, never embedded as literals. Roles cover surfaces, text, emphasis, structure and interaction; a missing role is added to the app's theme file rather than hardcoded at the call site. Raw hex, rgb()/rgba() and hsl() belong only inside theme definitions or audited data/raster content whose color is itself the data."
tags:
  - concept
  - desktop
  - architecture-pattern
  - software-engineering
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-design-guides.md
  - Raw/nsh-coding-guides.md
---
# Semantic Color Tokens

**Source:** [[Raw/nsh-design-guides]], [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH design and coding guides)

## The Rule

Read colors from the theme — `theme()` in Rust, token classes in TSX — and use them **by semantic role**. Application UI should not contain raw hex, `rgb()`/`rgba()`, or `hsl()` colors, or palette classes such as `bg-zinc-100`.

```rust
use nsh_base::theme;

view()
    .rounded(move || theme().radius)
    .border_1()
    .border_color(move || theme().border)
    .bg(move || theme().background)
    .p_4()
    .gap_1()
    .child(text("Balance").text_color(move || theme().foreground))
    .child(text("Updated just now").text_sm().text_color(move || theme().muted_foreground))
```

```tsx
<View class="gap-1 rounded-(--radius) border border-border bg-background p-4">
  <Text class="text-foreground">Balance</Text>
  <Text class="text-sm text-muted-foreground">Updated just now</Text>
</View>
```

## The Role Vocabulary

| Role | Use for |
|---|---|
| `background`, `foreground` | The main surface and text |
| `card`, `popover`, `sidebar` (+ foreground variants) | Their named surfaces |
| `muted`, `muted-foreground` | Supporting information |
| `primary` | The principal action or selection emphasis |
| `secondary`, `accent` | Quieter emphasis, hovered or focused rows |
| `destructive` | Destructive actions and errors — nothing else |
| `success`, `warning` | Only for their meanings, when the app adds them |
| `chart-1` … `chart-5` | Data series |
| `border`, `input`, `ring` | Structure and interaction |

Do not use a semantic status color as decoration. Do not encode meaning by color alone.

## Missing Roles Are Added to the Theme

If the required role does not exist, **define it in the app's theme file** rather than embedding a palette value at the call site:

```json
"up": "#16a34a"
```

in both its `light` and `dark` values makes `text-up`, `bg-up/30`, `token("up")` in TSX and `theme().color("up")` in Rust available.

Every name in the app's theme file is a token, as a variable of Tailwind's `@theme` is, and the theme has light and dark values, so **a token follows the appearance with no `dark:` class**. Name tokens after roles, not components, so they do not become the extension point for every widget.

Raw colors belong only inside theme definitions or in audited data/raster content whose color is itself the data.

## Theme Changes Are Native

Change the theme through the app's theme file (`nsh.json` `"theme"`), or let the embedding app give its own: classes naming tokens and Rust bindings reading `theme()` are restyled **natively** whenever it changes, with no JavaScript running. Code that copies a token's value into a signal of its own stops following it.

An embedded app can be given its host's theme, and the host's theme is applied the same way. Verify every custom surface in light and dark themes and with custom theme values, including the theme of a host app that embeds yours; never assume that foreground is black or background is white.

## Badge and Variant Scarcity

Use a badge for a short state, count, or classification that benefits from rapid scanning — not for every label, metadata value, filter, or section title. Keep most badges neutral; reserve semantic colors for states that truly carry success, warning, destructive, or informational meaning. A row of multicolored badges is usually a missing hierarchy or grouping decision.

Keep badge and alert variants semantic and scarce. Ordinary metadata stays neutral; do not map every enum case or section to a different color merely because a variant exists.

## Related Concepts

- [[Concepts/native-shell-design-system|Native Shell Design System]] — the full visual language these tokens serve
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — Base exposes tokens, the app decides the palette
