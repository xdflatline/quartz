---
title: "Wiki Content Ingestion"
details: "The four-tier Raw → Concept → Entity → Index protocol for ingesting external research into the Quartz wiki. The wiki-specific distillation of the wiki-content-ingestion skill in jin — more concise, no gallery instructions, single `details:` field, this operator's `shortest` link resolution."
tags:
  - workflow
  - wiki
  - ingestion
  - protocol
  - knowledge-management
created: 2026-08-07
updated: 2026-08-07
type: guide
source: ~/jin/skills/software-development/wiki-content-ingestion/SKILL.md
---

# Wiki Content Ingestion

This workflow is the wiki-specific distillation of the `wiki-content-ingestion` skill in `~/jin/skills/`. It is **more concise** (no gallery instructions, no source-extraction recipes for content the operator doesn't have), uses the **single `details:`** frontmatter field (the operator's current schema; `detail:` has been dropped per the 2026-08-07 housekeeping plan), and is calibrated to this operator's `shortest` link-resolution setting (not `absolute`).

For the full source-of-truth skill — including GitBook extraction recipes, the historical filename-collision recovery, and the bulk-fix script — see `~/jin/skills/software-development/wiki-content-ingestion/SKILL.md`.

## 1. Protocol Overview (Quartz Structure)

The Wiki Ingest Protocol has four tiers, with folder names strictly capitalized:

| Tier | Directory | Purpose | Example |
|------|-----------|---------|---------|
| **Raw** | `Raw/` | Verbatim source content with metadata, flattened (no subdirectories) | `Raw/hn-multiagent-orchestration-production.md` |
| **Papers** | `Papers/` | Peer-reviewed research, arXiv preprints, academic papers | `Papers/hindsight-agent-memory.md` |
| **Concept** | `Concepts/` | Extracted patterns, architectures, principles | `Concepts/multi-agent-orchestration-patterns.md` |
| **Entity** | `Entities/` | Tools, projects, people, products mentioned | `Entities/memori-memory-layer.md` |
| **Index** | `Research/` | Cross-linking synthesis document | `Research/ai-agent-memory-orchestration.md` |

**Flow:** Raw → Concept + Entity → Index (bidirectional wikilinks with capitalization).

## 2. Frontmatter Schema

Wiki pages use this frontmatter shape:

```yaml
---
title: "Page Title"
details: "Detailed summary; the only description field (no detail:)."
tags:
  - <tier-tag>
  - <topical-tag-1>
  - <topical-tag-2>
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: <concept|entity|research|raw|paper|note|...>
---
```

**Notes:**

- **Only `details:` is used.** The `detail:` field is deprecated as of 2026-08-07.
- **`details:` values with a colon must be quoted.** YAML treats a colon as a mapping separator. Wrap in double quotes: `details: "Tool design pattern: a single selector tool."`
- **`tags:` is a YAML list, not a string.** Each tag is a separate `-` line. Use the [[tags|Tag Index]] vocabulary; don't invent product-name tags.
- **`type:` enum:** `raw | concept | entity | research | paper | project | idea | note | index | resource | content`. The `entitie` typo is forbidden; `entity` is correct.
- **`type: entitie`** must be fixed to `type: entity` (53 files in `Entities/` need this fix; the housekeeping plan handles it).

## 3. Ingestion Steps

### Step 1: Fetch & Save Raw Article

Use the most appropriate extraction method for the source type:

- **GitBook docs** (`.gitbook.io`, `mintlify.app`, `docs.<vendor>.io`) — try the `.md` URL mirror first; raw markdown is 10-100x smaller than the HTML.
- **PDF** — use `/home/master/tools/markitdown.sh` to convert to markdown.
- **Blog posts / articles** (lilianweng.github.io, dev.to, arXiv html) — `web_extract` from the page URL.
- **GitHub READMEs** — `web_extract` from the raw GitHub URL (`raw.githubusercontent.com`).

Save with the required frontmatter to `Raw/<source>-<topic-slug>-<YYYY-MM-DD>.md`.

### Step 2: Create Concept Pages

For each distinct architectural pattern, principle, or technique in the source, create a file in `Concepts/`.

**Before writing each concept file, verify the filename is novel.** `write_file` has no create-only mode — a pre-existing file with the same name will be **silently overwritten**, destroying unrelated research. The collision is invisible until `git status` shows an unexpected `M` (modified) on a file you thought was new.

```bash
# Run before writing any new concept file
ls ~/quartz/content/Concepts/ | grep -F "<proposed-filename>.md"
# Also search by likely aliases / synonyms
search_files(pattern="<key-words-from-title>", target="content", path="/home/quartz")
```

If a file already exists with that name (or a near-synonym), either:

- **Reuse the existing file** and edit it with `patch`, not `write_file`
- **Pick a more specific name** that disambiguates (e.g. `agent-composition-tree-mastra` instead of colliding with `agent-first-pipeline-architecture`)
- **Add a bidirectional cross-reference** between the two distinct concepts

**Naming discipline:** prefer the most specific accurate name. General architectural terms get reused across different frameworks; framework-specific names are collision-resistant.

### Step 3: Create Entity Pages

For each tool, project, product, company, or person mentioned, create a file in `Entities/`. Apply the same filename-collision check as for Concepts. Use the [[tags|Tag Index]] vocabulary — **no product-name tags** (Qwen3.5 articles get `llm`, not `qwen`).

### Step 4: Create/Update Research Index

Synthesize the concepts and entities into a file in `Research/<topic>.md`. The Research page:

- Cross-links the new concept and entity pages
- Has a "Key Threads / Sources" table
- Has a "Cross-Cutting Themes" section
- Has actionable "Next Research Directions" with success criteria

## 4. Build, Verify, Commit, Push

The publish workflow is **strict and verification-first**. The full sequence after every ingestion:

```bash
cd ~/quartz && npx quartz build
# Must complete with 0 errors

cd ~/quartz && git status --short
# Every line should be A  (added) or  M (modified by you intentionally).
# Any unexpected M or D means write_file overwrote or removed something
# you did not intend — see the "Filename collision" pitfall.

cd ~/quartz && git diff --stat HEAD
# Should show only the files you intended to add or modify.

cd ~/quartz && grep -c "^detail:" content/**/*.md
# Should be 0 after the 2026-08-07 housekeeping pass.

cd ~/quartz && git add <the-new-files>
cd ~/quartz && git commit -m "feat(wiki): <conventional commit message>"
cd ~/quartz && git push origin publish
```

**Rule: build BEFORE commit, never after.** A broken build in `publish` will break the deployed site.

## 5. Pitfalls

The pitfalls that actually fire in this operator's setup. Full list with worked examples is in the jin skill.

### Filename collision silently overwrites pre-existing files

`write_file` has no "create-only" mode. Detection: after writing all new files but before staging or committing, run `git status --short` — any `M` on a file you did not intend to edit means `write_file` overwrote it. Fix: `git checkout HEAD -- <file>` to restore, rename your new file, add a cross-reference. **Prevention:** the filename-uniqueness check in Step 2.

### `details:` frontmatter values containing a colon break the build

Quartz v5 parses frontmatter with a strict YAML parser. A value containing a colon is read as a mapping entry. Wrap the value in double quotes: `details: "Pattern: a single selector delegates."` Bulk fix:

```bash
python3 ~/jin/skills/software-development/wiki-content-ingestion/scripts/quote-frontmatter.py \
    content/Concepts/*.md \
    content/Entities/*.md \
    content/Raw/*.md
```

The script is idempotent. Verification: `npx quartz build 2>&1 | grep -E "bad indentation|ERROR"` should return nothing.

### Cross-folder wikilinks use `shortest` resolution

This operator's `quartz.config.yaml` uses `markdownLinkResolution: shortest`, not `absolute`. Wikilinks between folders resolve relative to the source file's folder. Verification after a build with cross-folder links:

```bash
grep -o 'href="[^"]*"' public/entities/<page>.html | grep raw
# Should show: href="../raw/<filename>" (resolves to /raw/<filename>)
# NOT:        href="raw/<filename>" (would resolve to /entities/raw/<filename>)
```

### Wikilink format: capitalized folders, no subdirectories

All wikilinks must use **capitalized folder prefixes** matching the actual directory names: `[[Raw/filename]]`, `[[Concepts/name]]`, `[[Entities/name]]`, `[[Research/name]]`. Do NOT use lowercase paths like `[[raw/articles/filename]]` — these will not resolve.

### `patch` can silently eat the closing `---` of YAML frontmatter

A "replace the line ending in `---` with two lines" pattern (e.g. adding a new bullet to the `sources:` list and re-adding the closer on a new line) is easy to mishit. The closer is the line that terminates the YAML frontmatter block, so losing it means the entire body of the markdown file (including headings, etc.) is then parsed as YAML by the next build. The build will fail with a confusing error pointing at body text.

**Working pattern:** before any `patch` call that touches the frontmatter, do a defensive read of the first 20 lines to confirm the structure. Expect the YAML frontmatter to be terminated by a single `---` line on its own. If your planned `patch` would touch the closer, prefer one of:

- Make the `patch` strictly replace within the frontmatter, leaving the closer untouched.
- Add a new line BEFORE the closer by matching a longer context string that includes the closer.
- If you did eat the closer, restore it with a follow-up `patch`: `old_string` = the last frontmatter line + the body's first heading; `new_string` = the last frontmatter line + `---` + blank line + the body's first heading.

Verification: after any frontmatter-touching `patch`, re-read lines 1-15 before running `npx quartz build`. The closing `---` must exist.

### GitBook-rendered HTML injects widget text

When scraping GitBook-hosted docs (`<vendor>.gitbook.io`, `*.mintlify.app`) without using the `.md` mirror shortcut, every section gets a trailing "GitBook Assistant" label. A regex extractor will pick it up and embed it in your Raw file. **Fix (best):** fetch the raw `.md` mirror instead of the HTML. **Fix (fallback):** strip the literal string `GitBook Assistant` from the output before saving.

### Mermaid diagrams with hardcoded `style X fill:#...` break dark mode

Inline `style A fill:#XXXXXX` directives render with that literal hex color in both light and dark mode. **Fix:** drop the inline fills; the plugin's `themeVariables` already provide consistent, theme-aware defaults.

## 6. When to use the catalog workflow instead

If the source is a **closed enumeration of similar items** (LLM model lists, vendor tool inventories, product version catalogs) where each item has its own data too rich for a single table row, use the [[Workflows/wiki-catalog-research/wiki-catalog-research|Wiki Catalog Research]] workflow instead. The catalog pattern is an exception to the "no subdirectories" rule and uses `Research/<area>/<item>.md` for per-item pages.
