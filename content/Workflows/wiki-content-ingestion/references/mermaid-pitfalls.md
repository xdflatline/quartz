# Mermaid Pitfalls in Quartz

Two recurring issues with Mermaid diagrams in `quartz-community/obsidian-flavored-markdown`. Both are environmental facts about how the plugin works, not bugs in your content.

## 1. Hardcoded `style X fill:#...` breaks dark mode

**Symptom:** Boxes/text in a diagram render with a light pastel fill in dark mode, making the text (which falls back to a light color) nearly unreadable.

**Root cause:** The OFM plugin initializes Mermaid at `scripts/mermaid.inline.ts:223-238` with theme variables:

```ts
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose",
  theme: darkMode ? "dark" : "base",
  themeVariables: {
    primaryColor:    computedStyleMap["--light"],
    primaryTextColor: computedStyleMap["--darkgray"],
    clusterBkg:      computedStyleMap["--light"],
    // ...
  },
});
```

These CSS variables are read from `:root` on every `themechange` event, so unstyled nodes do swap correctly between light and dark.

The catch: an inline `style A fill:#e3f2fd` in the diagram source overrides `primaryColor` for that node at parse time, and the override is **not** a CSS variable — it's a literal hex string baked into the rendered SVG. Mermaid has no theme-variable entry that reaches into an inline-styled node. The fill is whatever the diagram says, regardless of `themechange`.

**Fix:** strip the hardcoded fills. The plugin's `themeVariables` already provide consistent primary/secondary/tertiary/clusterBkg colors that swap correctly. If a diagram needs accent color, prefer `classDef` with theme-aware classes, or accept the theme defaults.

**Re-runnable cleanup (idempotent, safe to re-run):**

```bash
# dry-run first — list affected files
cd ~/quartz/content
grep -rlE "^\s*style\s+[A-Za-z0-9_,.\s-]+\s+(fill|stroke):" \
  Concepts/ Research/ Entities/ Raw/ 2>/dev/null

# strip the lines (BRE-friendly)
for f in $(grep -rlE "^\s*style\s+[A-Za-z0-9_,.\s-]+\s+(fill|stroke):" \
            Concepts/ Research/ Entities/ Raw/ 2>/dev/null); do
  sed -i -E '/^[[:space:]]*style[[:space:]]+[A-Za-z0-9_]+[[:space:]]+(fill|stroke):/d' "$f"
done
```

**Verify with a build, not just a grep:**

```bash
cd ~/quartz && npx quartz build 2>&1 | tail -5
# Should show: 0 errors, expected file count
```

Then hard-refresh the deployed page (cache-bust with `?v=2` on the URL) and toggle dark mode in the browser. The boxes should now follow the theme.

## 2. Shell safety: destructive `sed -i` needs a guard, not just a pre/post count

**Lesson from a real run:** when I ran `sed -i -E '/pattern/d' file` with an over-greedy character class, the edit was actually destructive (it deleted the targeted lines) but my `before=$(grep -c ...)` and `after=$(grep -c ...)` both printed `0` — because the original `grep` pattern didn't match the same thing the `sed` pattern matched. The "0 -> 0" output looked like a no-op. The actual deletion was correct, but my verification was broken and could not detect a future bug.

**Rules:**

1. **Quote the file paths** — `sed -i ''` (BSD/macOS) and `sed -i` (GNU) differ. On Linux the empty argument is unneeded, but missing it on macOS silently writes a backup. Always specify the suffix explicitly: `sed -i.bak` then `rm file.bak`, or run a dry-run first with `sed -E 's/x/y/' file | diff - file`.
2. **Match `sed` and `grep` patterns** — if you verify with `grep`, the grep pattern must be identical to the sed regex. A small difference (e.g., `[[:space:]-]` vs `[[:space:]]`) makes the verification lie.
3. **Always `git diff` after `sed -i`** — for tracked files, `git diff --stat` is the cheapest, most accurate check. `-- 7 files changed, 49 deletions(-)` is the truth; `0 -> 0` from a mismatched grep is not.
4. **Prefer `patch` tool over `sed -i`** — `patch(path, old_string, new_string)` is exact-string, hard to over-match, and returns a unified diff for free. Use it for any edit where the match is specific enough to be a unique string.
5. **Build, then commit, then push** — `npx quartz build` catches all content-side breakage (YAML errors, wikilink breaks, Mermaid parse errors). Run it as the final verification step.
