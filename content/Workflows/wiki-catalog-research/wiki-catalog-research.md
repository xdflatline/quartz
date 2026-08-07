---
title: "Wiki Catalog Research"
details: "The catalog-style research pattern for closed enumerations of similar items (LLM model lists, vendor tools, product versions) where each item warrants a per-entity page rather than a row in a single table. Covers the Research/<area>/ subdirectory pattern, per-item page convention, index structure, and the catalog-expansion update workflow."
tags:
  - workflow
  - wiki
  - catalog
  - research
  - knowledge-management
created: 2026-08-07
updated: 2026-08-07
type: guide
source: ~/.hermes/skills/wiki-catalog-research/SKILL.md
---

# Wiki Catalog Research

This workflow covers **catalog-style research in the operator's Quartz garden** — research areas that track a closed enumeration of similar items (LLM model lists, vendor tool inventories, product version catalogs) where each item has its own data (architecture, pricing, endpoint, benchmarks) too rich for a single table row, and too volatile for a single flat index page.

For the full source-of-truth skill — including the 13→17 model expansion worked example and the trigger conditions — see `~/.hermes/skills/wiki-catalog-research/SKILL.md`.

## 1. When to use this workflow (and when not)

Use the catalog pattern when **all** of the following apply:

1. The research area tracks a **closed-ish enumeration** of items (provider models, vendor tools, product versions, plugin lists)
2. Each item has its own data — architecture, pricing, endpoint, benchmarks, license, use case — **too rich for a single table row**
3. The items change over time (new entries, pricing updates, deprecations) and need a **dated `Updated:` banner** to track those changes
4. The catalog is large enough that a single index page would lose readability

**Do not** use this pattern for:

- Open-ended research topics — use the standard `Research/<topic>.md` flat index instead
- Small enumerations (5 or fewer items fit comfortably in a single Research page with a table)
- Items that are primarily pointers to Entity pages (the Entity tier already handles "one page per thing")

When in doubt: use the [[wiki-content-ingestion|wiki-content-ingestion]] workflow's standard four-tier protocol first. Switch to the catalog pattern only when the four-tier protocol's "no subdirectories" rule is violated by the volume of items.

## 2. Directory structure

```
content/Research/
  <area>/                    # the catalog's working directory
    <area>.md                # the index — overview, model catalog table, tier summary, endpoint routing reference
    <item-1>.md              # per-item page
    <item-2>.md
    ...
```

**Naming:**

- The directory uses **Title-Case or kebab-case** to match the area (`OpenCode-Go`, not `opencode-go`)
- The **index file shares the directory name** (`OpenCode-Go/OpenCode-Go.md`)
- **Per-item files use lowercase kebab-case** matching the item's canonical ID (`grok-4.5.md`, `kimi-k3.md`, `minimax-m2.5.md`)

**Why the index shares the directory name.** Quartz treats a directory containing an `<dirname>.md` as a folder page; the file becomes the rendered index when visitors land on `/<area>/`. The directory + index pattern also means the catalog is discoverable from the broader Research index.

## 3. Per-item page convention

The convention established in the operator's existing `Research/OpenCode-Go/` catalog is fixed. Match it exactly — consistency across the catalog matters more than per-page perfection:

```markdown
---
title: <Item Name>
details: <one-sentence summary>.
tags:
  - research
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: note
---
# <Item Name>

**Developer:** <vendor>
**Released:** <YYYY-MM-DD>           # omit if not publicly known
**License:** <if known>              # omit if not yet published
**Model ID:** `<area>/<item-id>`

## Architecture
| Feature | Specification |
|---------|---------------|
| Total Parameters | ... |
| Active Parameters | ... per token |
| Architecture | Mixture-of-Experts (MoE) / Dense / ... |
| Context Window | ... tokens |
| Modalities | Text / +Image / +Video / +Audio |
| Attention | <type> |
| Modes | Thinking / Non-Thinking / Hybrid / ... |

## Key Features
- **<feature 1>** — <explanation>
- **<feature 2>** — <explanation>

## Benchmarks
- <benchmark name>: <score> (<context: vendor-reported / independent / community>)

## Pricing (<context>)
| Metric | Value |
|--------|-------|
| Input | $X.XX / 1M tokens |
| Output | $X.XX / 1M tokens |
| Cache Read | $X.XX / 1M tokens |
| Cache Write | $X.XX / 1M tokens |       # only if supported
| Est. requests per 5h | N |
| Est. requests per month | N |

## Endpoint
Chat completions / Messages / Responses: `<url>`

## Best For
- <use case 1>
- <use case 2>
- <use case 3>
```

**Section order is fixed:** Developer / Released / License / Model ID → Architecture → Key Features → Benchmarks → Pricing → Endpoint → Best For. Rearranging wastes review time.

**For previously-undocumented items** that show up in the endpoint table but have no public spec, use a stub form:

```markdown
## Architecture
| Feature | Specification |
|---------|---------------|
| Architecture | (same as <nearest-known-generation>) |
| Context Window | (same as <nearest-known-generation>) |

## Key Features
- **<Retention reason>** — why this old item is still in the catalog
- **No benchmark data** — <vendor> did not publish specs; doc only exposes pricing and endpoint
```

Document the gap explicitly. **Do not invent specifications.**

## 4. Index page structure

The index is the working surface. Every catalog-update session edits this file. The convention:

```markdown
---
title: <Area>
details: <catalog purpose>.
tags:
  - research
created: <date>
updated: <date>          # <-- bump on every catalog-update session
type: note
---
# <Area>

<one-paragraph overview>

**Updated <YYYY-MM-DD>:** <change summary — new items, pricing changes, removed items, endpoint changes>.

## Provider Overview
- **<endpoint-1>:** <URL> (<which model families>)
- **<endpoint-2>:** <URL> (<which model families>)
- **<endpoint-3>:** <URL> (<which model families>) -- <when this differs from default>

## Usage Limits
| Window | Limit |
|--------|-------|

## Model Catalog
| <Item> | <Developer> | <Params> | <Context> | <Input> | <Output> |

## Highlights and Recommended Use Cases
| <Item> | Highlights | Recommended Use Case |

## Tier Summary
- **<tier 1>:** <items>
- **<tier 2>:** <items>
- **<tier 3>:** <items>

## Endpoint Routing Reference
| Endpoint | Models |
|----------|--------|
```

**The "Updated" banner is mandatory.** It is the single signal a future session uses to decide whether the index is current. Every catalog update must:

- Bump the `updated:` frontmatter value
- Add a new "Updated <date>:" line at the top of the body, summarizing what changed

**The Endpoint Routing Reference table is mandatory for multi-endpoint catalogs.** When a provider exposes 2+ endpoints (`/chat/completions` vs `/messages` vs `/responses` style), clients configuring SDKs need to know which endpoint applies to which model. A wrong endpoint choice fails silently with auth/parse errors.

**The Tier Summary tells the user where to start.** Group by price/quality bands, name 3-5 items per tier, and update the tier notes when items move between tiers.

## 5. Build behavior

Quartz keeps a **legacy uppercase redirect-stub** at `public/Research/<area>/<item>.html` while the real page lives at lowercase `public/research/<area>/<item>.html`. The `<area>.md` index file builds to `public/research/<area>/index.html` (NOT to `public/research/<area>/<area>.html`).

**Verification recipe** (run after every catalog update):

```bash
# After npx quartz build, verify against the LOWERCASE path:
ls -la public/research/<area>/<item>.html
# Real pages: >= 25 KB. Stubs: 300-340 bytes. < 1 KB = something is wrong.

ls -la public/research/<area>/index.html
# The index should be the largest file in the directory.

# Legacy uppercase stubs are expected and harmless:
ls -la public/Research/<area>/
# Files there are 300-340 bytes redirect stubs, not the real pages.
```

The legacy uppercase stub at `public/Research/<area>/<item>.html` is the same pattern as the per-page case. Both files coexist. Do NOT "fix" the uppercase stub by deleting the source `<area>/<item>.md` file.

## 6. Catalog-update workflow

When the user says "X needs an update, there are new Y":

1. **Verify against the live source first.** The user often doesn't have the exact list of changes; you do. Fetch the authoritative provider doc AND a community changelog in parallel via web tools. Live docs are the source of truth; community changelogs catch the gap between release and doc update.

2. **Diff against the existing index.** Compare the new authoritative list to the catalog table in `Research/<area>/<area>.md`. Identify:
   - **New items:** need a per-item page
   - **Items with changed pricing/specs:** need the per-item page updated
   - **Items with changed endpoints:** need both the per-item page and the Endpoint Routing Reference updated
   - **Removed items:** the per-item page stays (for historical record) but the index should mark it deprecated
   - **Provider-wide changes** (new endpoint, new tier, new usage limit): update the Provider Overview / Usage Limits sections

3. **Plan the diff before writing.** State in chat: "Plan: +N new per-item pages, M existing pages need pricing update, K index sections need rows added." This is the user's signal to interrupt if the plan is wrong. Don't skip this step.

4. **Create new per-item pages in parallel** via `write_file`. Each new page should match the existing per-item convention exactly (Developer → Architecture → Key Features → Benchmarks → Pricing → Endpoint → Best For). Use a `todo` list to track each one; mark `completed` as you write them.

5. **Update the index in one consolidated edit.** The index gets:
   - A new "Updated <date>:" banner at the top
   - New rows in the Model Catalog table (sorted by release date, then developer)
   - New rows in the Highlights and Recommended Use Cases table
   - Updated Tier Summary (and a tier-summary note if items moved between tiers)
   - New rows in the Endpoint Routing Reference (if any new endpoints)

6. **Build, verify, commit, push.**
   - `npx quartz build` must complete with 0 errors
   - `Found N input files` should go up by exactly the number of new files you created
   - `Emitted N files` should increase by approximately 3 per new file (the page + OG image + alias redirect)
   - `git status --short` should show only your intended changes — every line should be `A ` (added) for new files or ` M` (modified, leading space) for the index you edited
   - Mismatched deltas = silent failure; investigate before committing
   - Commit with Conventional Commits; push to the publish branch

7. **Don't create Raw stubs unless asked.** Unlike a normal ingestion, a catalog update aggregates across many primary sources; one Raw page per source is excessive. List external sources in the index footer as a flat URL list, not as Raw stubs.

## 7. Common pitfalls

### The "endpoint change is silent" trap

When a provider moves a model from one endpoint to another, or adds a new endpoint variant, code that worked yesterday will start failing with auth errors or parse errors. Always update the Endpoint Routing Reference table, AND update each per-item page's `## Endpoint` section. Both must agree.

### The "previously-undocumented model" gap

Providers sometimes ship a model in their endpoint table without documenting it in their main docs. The right move is to create a stub per-item page with explicit "no benchmark data / no public spec" notes rather than skipping it. Skipping creates a gap between what the catalog claims to track and what it actually covers.

### The "pricing change" trap

Pricing changes more often than the per-item page gets updated. When the index says "Updated <date>:" the user trusts that the prices listed in the catalog table are current as of that date. If a per-item page has a different price than the index, that's a bug. Verify alignment before committing.

### The "tier drift" trap

Items move between tiers (budget / mid / flagship) as pricing and quality change. The Tier Summary is the most-read section of the index; if it lists an item as flagship but the item is now budget-tier, the visitor picks the wrong model. Re-derive the tier summary from the current data on every update, don't just add to it.

### The "alias collision" trap

If a per-item page's `aliases:` frontmatter resolves to the same URL as the canonical slug, the alias redirect stub overwrites the real page at the lowercase path. Symptom: the lowercase HTML is 300-340 bytes instead of 25+ KB. Fix: use a distinct alias path.

## 8. Worked example

For the full 13→17 OpenCode-Go model expansion worked example (diff plan, per-item page content for the four new models, the index delta, the build verification), see [[references/catalog-update-example-2026-07-31|OpenCode-Go catalog update example]].
