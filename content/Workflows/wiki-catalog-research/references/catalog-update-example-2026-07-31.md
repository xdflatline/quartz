# Worked Example: OpenCode Go 13→17 Model Expansion (2026-07-31)

This is the full worked example of a catalog-update session using the wiki-catalog-research pattern. Captured for the next session to follow when the user says "X needs an update, there are new Y" against any catalog.

## What the user asked

> the opencode go models research need an update, there are new models

That's the entire ask. No list of new models, no specs, no date. The session had to figure out everything.

## Step 1 — Verify against the live source

Fetched in parallel:

- `https://opencode.ai/docs/go/` — the official OpenCode Go docs, current model list
- A community changelog (`julien.cloud/opencode-go-models/`) — caught items that were shipped but not yet in the main doc

The official doc listed 17 active models. The existing wiki had 13. Diff: 4 new + 1 previously-undocumented.

| Model | Developer | Released | Notes |
|---|---|---|---|
| Grok 4.5 | xAI | 2026-07-08 | First non-Asian model on Go; 80 TPS; trained alongside Cursor |
| GPT 5.6 Luna | OpenAI | 2026-07-09 | GPT-5.6 fast tier; **80% price cut on 2026-07-30**; uses `/responses` (NOT chat completions) |
| Hy3 | Tencent | 2026-07-06 | Apache 2.0; 295B/21B MoE; final Hunyuan 3 (no Hunyuan 4) |
| Kimi K3 | Moonshot AI | 2026-07-16 | First 3T-class open-weights; 1M context; weights due 2026-07-27 |
| MiniMax M2.5 | MiniMax | (pre-existing) | Was in endpoint table, never documented |

## Step 2 — Diff against the existing index

Existing `Research/OpenCode-Go/OpenCode-Go.md` had:
- 13 rows in the Model Catalog
- 13 rows in the Highlights table
- Tier Summary with 3 bands
- No Endpoint Routing Reference (would have helped catch the GPT 5.6 Luna endpoint difference)

Diffs:
- +5 rows in Model Catalog (4 new + 1 previously-undocumented)
- +5 rows in Highlights
- Tier Summary needs to expand (Hy3 and GPT 5.6 Luna reshape the budget tier; Kimi K3 reshapes the flagship tier)
- NEW: Endpoint Routing Reference table (3 endpoints now, was 2)

## Step 3 — Plan stated in chat

> Plan: 5 new per-item pages (grok-4.5, gpt-5.6-luna, hy3, kimi-k3, minimax-m2.5), the main OpenCode-Go.md index gets 5 new table rows in both Model Catalog and Highlights, Tier Summary updates, and a new Endpoint Routing Reference table.

User confirmed implicitly by not interrupting.

## Step 4 — Per-item pages created

Each followed the exact per-item convention from the existing catalog. Section order: Developer / Released / License / Model ID → Architecture → Key Features → Benchmarks → Pricing → Endpoint → Best For.

**Grok 4.5** — `2,989 bytes` — dense V9 foundation, 500K context, 80 TPS, Cursor training partnership, EU unavailable at launch. The 120/5h request budget makes it the lowest-throughput model in the catalog despite competitive per-token pricing.

**GPT 5.6 Luna** — `2,292 bytes` — emphasized the `/v1/responses` endpoint difference in both the `## Endpoint` section and the index's routing reference. Noted the 2x usage multiplier on Go (mentioned in the julien.cloud changelog) and the 80% price cut on 2026-07-30.

**Hy3** — `2,532 bytes` — emphasized Apache 2.0 (rare among Chinese frontier-tier models), hybrid fast/slow thinking, the "no Hunyuan 4" naming clarification, and second-cheapest pricing.

**Kimi K3** — `3,541 bytes` — emphasized "first 3T-class open-weights", Kimi Delta Attention, native vision, BrowseComp 90.4% at full context, weights-due-2026-07-27 (so not yet self-hostable as of 2026-07-31), and the 110/5h request budget being the lowest in the catalog.

**MiniMax M2.5** — `1,731 bytes` — used the stub form. Explicitly documented the gap: "No benchmark data — MiniMax did not publish M2.5 specs; the doc only exposes pricing and endpoint."

## Step 5 — Index update in one consolidated edit

Single `patch` operation with three parts:

1. **Provider Overview** — added the `/v1/responses` endpoint variant for GPT 5.6 Luna; updated the chat-completions and messages endpoint listings to mention the new families
2. **Model Catalog** — added 5 new rows; sorted by release date (newest first), then developer
3. **Highlights** — added 5 new rows; updated Tier Summary; added Endpoint Routing Reference table

The "Updated 2026-07-31:" banner at the top of the body summarized all changes in one line. The `updated:` frontmatter value was bumped to match.

## Step 6 — Build verification

```
Found 219 input files from `content` in 21ms     # was 214, +5 = exact match
Parsed 219 Markdown files in 9s
Filtered out 0 files in 166μs
Emitting files
Emitted 822 files to `public` in 27s             # was 807, +15 = 3 per new file (page + og image + alias redirect)
Done processing 219 files in 36s
```

Both deltas matched expectations exactly. Zero errors.

`git status --short` before commit:

```
M  content/Research/OpenCode-Go/OpenCode-Go.md
A  content/Research/OpenCode-Go/gpt-5.6-luna.md
A  content/Research/OpenCode-Go/grok-4.5.md
A  content/Research/OpenCode-Go/hy3.md
A  content/Research/OpenCode-Go/kimi-k3.md
A  content/Research/OpenCode-Go/minimax-m2.5.md
```

1 modified (the index, intentional), 5 added (the new pages, intentional). No unexpected `M` or `D` lines.

## Build artifact verification (lowercase path, real page)

```bash
ls -la ~/quartz/public/research/opencode-go/
# -rw-r--r-- 1 master master 28386 .../deepseek-v4-flash-og-image.webp
# -rw-r--r-- 1 master master 27513 .../deepseek-v4-flash.html
# ...
# -rw-r--r-- 1 master master 40808 .../index.html       <-- the OpenCode-Go.md index
# -rw-r--r-- 1 master master 25622 .../kimi-k3-og-image.webp
# -rw-r--r-- 1 master master 28947 .../kimi-k3.html
```

All per-item pages: 26-29 KB. Index: 40 KB. The legacy uppercase `public/Research/OpenCode-Go/*.html` files are 289-340 byte redirect stubs (expected behavior, documented in `quartz-content-patterns`).

## Commit

Conventional Commits format. Single commit covering all 6 file changes (1 modified + 5 added). The commit message documented:

- Which 4 new models were added and their release dates
- The 1 previously-undocumented model
- The endpoint routing change (`/v1/responses` addition)
- The build delta (input +5, emitted +15, 0 errors)

Pushed to `publish` branch (the user's working branch — NOT `main`, which would be wrong per the operator's documented branch-detection trap).

## What the next session should learn

1. **Verify against live source first.** The user said "new models" without specifying which; the live doc + community changelog pair revealed the full picture.
2. **Plan in chat before writing.** "Plan: 5 new pages, 5 index rows, 1 new routing table" took 30 seconds and prevented the user from having to redirect mid-execution.
3. **Match the existing per-item convention exactly.** Section order (Developer → Architecture → Key Features → Benchmarks → Pricing → Endpoint → Best For) is the operator's preference, not a recommendation. Following the existing pattern took 5 minutes of reading; deviating would have taken an hour of debate.
4. **Build deltas are a sanity check.** Input +5 (exactly the new files), emitted +15 (3 per new file) = no silent drops, no alias collisions, no extra pages.
5. **Multi-endpoint providers need a routing reference table.** The `/v1/responses` endpoint is NOT a drop-in for `/v1/chat/completions` — this is the kind of trap that causes silent auth/parse errors. Track the routing as a first-class table in the index.
6. **Previously-undocumented models need stubs, not silence.** If the endpoint table has a model the per-item pages don't cover, write a stub with explicit "no public spec" notes. The alternative is a silent gap in the catalog's coverage claim.
