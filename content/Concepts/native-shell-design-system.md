---
title: "Native Shell Design System"
details: "NSH's design thesis: build interfaces that feel native, quiet and precise. Clarity before personality, composition before invention, tokens before values, platform before web convention, state must be visible, geometry explains containment, feedback reflects reality. Covers hierarchy, semantic color, radius and spacing scales, alignment spines, density tiers and text scaling."
tags:
  - concept
  - desktop
  - architecture-pattern
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-design-guides.md
---
# Native Shell Design System

**Source:** [[Raw/nsh-design-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH design guide)

## The Design Thesis

Build interfaces that feel **native, quiet, and precise**. Let content, hierarchy, and interaction carry the experience; decoration should support them rather than compete with them.

1. **Clarity before personality.** Make the primary task and next action clear before adding brand expression.
2. **Composition before invention.** Start with established components and compose them into product-specific workflows. Create a new primitive only when its behavior is genuinely new.
3. **Tokens before values.** Colors, radii, typography, and spacing should form a system. Avoid isolated literals that cannot respond to themes.
4. **Platform before web convention.** Preserve keyboard access, window chrome, menus, dense data views, resizable regions, and persistent navigation on the desktops, and the system's headers, back gesture, alerts and touch targets on phones and tablets, where the task benefits from them.
5. **State must be visible.** Hover, pressed, focus, selection, disabled, loading, validation, and destructive states need distinct and consistent treatment.
6. **Geometry explains containment.** Radii, insets, and boundaries should describe one coherent hierarchy, even where surfaces overlap.
7. **Feedback reflects reality.** Loading, tooltips, and motion should clarify a real state or transition, not add ceremony to an immediate action.

## Start from the Task

Before drawing a screen, write down:

- the user's primary task;
- the object being viewed or changed;
- the actions that must remain immediately available;
- the information required to make a decision;
- empty, loading, error, offline, read-only, and permission-denied states;
- the keyboard, touch and screen-reader path through the workflow;
- where the app is shown: on its own, or inside a host app.

Organize the screen around those answers. Do not begin with a dashboard grid or a component catalogue. A good interface exposes the user's mental model — documents, accounts, projects, messages, settings — not the internal service architecture.

For every proposed action, name its visible object, current state, scope, and result. If the interface does not show or clearly imply those things, the action is premature. **Do not expose a capability merely because the backend has it.**

## Hierarchy and the Emphasis Budget

Prefer a small number of clear levels: window or page title, section title, body text, muted text, labels. Use size, weight, spacing, and separators before adding color or containers. Avoid nesting cards inside cards.

Evaluate hierarchy across the whole feature, not component by component. **Hide accent color and decoration during review**: the primary task, current selection, result summary, and next action should still be obvious from structure.

Treat emphasis as a limited budget. A local surface needs one clear focal point, not a field of competing highlights. If everything is colored, badged, bold, boxed, or promoted to an alert, nothing reads as important.

## Semantic Color

Read colors from the theme (`theme()` in Rust, token classes in TSX) and use them **by semantic role**:

- `background` and `foreground` for the main surface and text;
- `card`, `popover`, `sidebar`, and their foreground tokens for their named surfaces;
- `muted` and `muted-foreground` for supporting information;
- `primary` for the principal action or selection emphasis, `secondary` and `accent` for quieter emphasis and hovered or focused rows;
- `destructive` only for destructive actions and errors, and status colors the app adds (`success`, `warning`) only for their meanings;
- `chart-1` to `chart-5` for data series;
- `border`, `input`, and `ring` for structure and interaction.

Do not use a semantic status color as decoration. Do not encode meaning by color alone. Verify every custom surface in light and dark themes and with custom theme values, including the theme of a host app that embeds yours; never assume that foreground is black or background is white.

Use a badge for a short state, count, or classification that benefits from rapid scanning — not for every label, metadata value, filter, or section title. A row of multicolored badges is usually a missing hierarchy or grouping decision.

**Application UI should not contain raw hex, `rgb()`/`rgba()`, or `hsl()` colors, or palette classes such as `bg-zinc-100`.** If the required role does not exist, define it in the app's theme file (`"up": "#16a34a"` in its `light` and `dark` makes `text-up`, `bg-up/30`, `token("up")` in TSX and `theme().color("up")` in Rust) rather than embedding a palette value at the call site.

## Radius, Spacing, and Density

Use a **finite radius scale**, as with type and control sizes. For an ordinary rectangle, the radius should remain visibly smaller than half its shorter side. Use `rounded-full` only for intentional circles and pills; a tooltip must not become a capsule by accident.

Nested surfaces should read as concentric shapes: **inner radius ≈ max(0, outer radius − gap)**. A segmented control is one silhouette: its end segments follow the container's inner corners, its middle segments remain square, and each boundary has one divider of consistent thickness.

A radius must govern the entire visible surface, not just its border. Exposed corners remain transparent to the surface behind them; child backgrounds, selection fills, and scrolling content must also follow the boundary.

The shared semantic scale is intentionally small: spacing progresses through roughly **2, 4, 8, 12, 16, 24, and 32 points**, while typography stays near **12, 14, 16, 18, and 20 points**. Treat these as relationships rather than permission to scatter their current values through feature code.

### Spatial Grammar

| Relationship | Typical class | Current scale |
|---|---|---|
| Optical correction | `gap-0.5` | 2 pt |
| Parts of one control | `gap-1` | 4 pt |
| Closely related controls | `gap-2` | 8 pt |
| One content group | `gap-3` | 12 pt |
| Separate groups in one section | `gap-4` | 16 pt |
| Separate sections | `gap-6` | 24 pt |
| Major region boundary | `gap-8` | 32 pt |

Six rules for resolving horizontal and vertical space:

1. **Inside before outside.** A component's padding belongs to the component; the gap between components belongs to their parent.
2. **Vertical rhythm shows grouping.** The gap between a title and its description is smaller than the gap from that description to the next section.
3. **Horizontal space supports scanning.** Repeated rows keep icons, labels, values, badges, and trailing actions on stable columns.
4. **Leading and trailing are semantic.** Write them as start and end (`ps-*`, `me-*`), so the layout mirrors right to left.
5. **Do not double padding.** A card placed in an already padded panel should not automatically add another full panel inset.
6. **Use optical alignment sparingly.** A one- or two-point correction is valid for icon or glyph geometry, but document why it differs from the scale.

### Density Tiers

Medium is the default. Change density for the whole local context, not one isolated control:

- **comfortable / large:** onboarding, sparse forms, prominent decisions;
- **standard / medium:** most application chrome and workflows, and every touch screen;
- **compact / small:** desktop toolbars, menus, tables, and repeated professional data;
- **extra compact / xsmall:** exceptional high-density utilities, never the automatic choice for an entire application.

On touch screens every pressable target is at least 44 × 44 points. With a pointer, buttons commonly move through approximately 24, 28, and 32 pt frames, inputs extend to about 40 pt at large size, and table rows use about 28, 32, and 40 pt.

## Alignment Spines

Alignment is a structural system, not a final polish pass. Establish a small set of **alignment spines** for each surface: shared leading and trailing edges, text baselines, center lines, and fixed functional lanes.

- Give sibling regions a shared content inset.
- Repeat column geometry through the whole region — identity, metadata, status, numbers, actions.
- Preserve the spine through optional content: missing icons, badges, descriptions, or trailing actions must not move the remaining labels.
- When a nested level ends, return exactly to the parent spine.
- Align text by baselines, not by bounding-box centers, when mixed sizes share a row.
- Align comparable numbers to the end and use tabular figures (`tabular-nums`).
- Hairlines belong on the boundary owner. Two adjacent regions must not each draw the same separator.
- A scrollbar belongs to the region that scrolls and sits against that panel's trailing edge. Pad the scroll view's content, not the scroll view.

**Treat exact alignment and repeated gaps as quality invariants.** When two edges or spaces are intended to be equal, a one-rendered-pixel difference is a defect, not an acceptable optical approximation. But the rendered-pixel tolerance is a verification rule, not permission to patch the code with raw point offsets — equal relationships should resolve from the same spacing class or token. Fix the common owner when they differ.

## Text Scaling: The User's Text Size Is the App's Zoom

NSH's lengths are points, and the user's text size (Dynamic Type on iOS, font size on Android, the desktops' text scaling, a host app's own setting) scales text: every text and input that allows font scaling grows, while spacing, radii, borders and images keep their size.

Design in ratios:

- type steps keep the same hierarchy around the base body size;
- spacing steps keep the same grouping relationships around the type;
- control frames and hit targets grow with their labels: size them by their content and a minimum (`min-h-11`), not a fixed height;
- pane minima and comfortable widths account for larger text;
- corner radii and focus treatment remain optically consistent with the control frame.

Because text grows on its own, a fixed frame around it breaks. Let rows wrap or switch to a column when text gets large, and cap the scale of text that is already large (`maxFontSizeMultiplier`).

**As a rule, application layout should not write literal point values** (`p-[13px]`, `px(13.0)`). Use literal points only when the value represents a physical or raster boundary: a hairline, platform window inset, bitmap dimension, minimum hit-test tolerance, or geometry that must match an external surface.

## Surfaces and Elevation

Use elevation to explain **stacking, not importance**. The base surface is flat; separators and background contrast define its regions. Popovers, menus, sheets, dialogs, and notifications may use progressively stronger shadows because they sit above other content. **Do not put a shadow on every card.**

All surfaces of the same kind should share one treatment. Give the popup families one themed surface (the `popover` tokens, the border, `radius` and one shadow) so `Popover`, `Menu`, `ContextMenu` and `Tooltip` do not drift apart.

## Layout Shells

Most applications should use one of these shells:

- **single workspace:** a header or toolbar above one primary view;
- **navigation stack:** pages pushed and popped (`NavStack`), with the system's back gesture on phones;
- **sidebar workspace:** persistent navigation beside a changing detail view;
- **master–detail:** resizable collection and detail panes, two pages on a phone;
- **document workspace:** tabs for multiple long-lived objects;
- **utility window:** one focused task with a short, fixed action path.

Keep global navigation stable while content changes. Give the primary work area the remaining space with `flex-1` and `min-w-0` / `min-h-0` where overflowing children must shrink.

## Responsive Windows

A window can be any size: the user, a split view or the host app decides it. Decide what happens as a window narrows:

1. preserve the primary task;
2. allow resizable regions to reach a documented minimum;
3. collapse secondary labels or inspectors;
4. move low-frequency actions into a menu;
5. scroll only the region whose content actually overflows.

**Do not hide an action without providing another path to it.** A clipped region also clips an outward focus ring; never trade away keyboard visibility merely to simplify overflow.

## Related Concepts

- [[Concepts/native-shell-ui-language|Native Shell UI Language]] — the wording rules that carry the design system's meaning
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — which layer owns the visual language
- [[Concepts/semantic-color-tokens|Semantic Color Tokens]] — the token discipline this system depends on
- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layers the styled component layer sits in
