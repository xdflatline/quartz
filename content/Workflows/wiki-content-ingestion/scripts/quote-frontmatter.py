#!/usr/bin/env python3
"""Quote `detail:` and `details:` values in Quartz markdown frontmatter.

YAML scalars that contain a colon (e.g. "Concept: pattern X and Y") are
interpreted as mapping entries and break the Quartz parser with
"bad indentation of a mapping entry". The fix is to wrap the value in
double quotes.

Usage:
    python3 quote-frontmatter.py <file.md> [<file2.md> ...]
    python3 quote-frontmatter.py content/Concepts/*.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Match `detail:` or `details:` at the start of a line, followed by a
# space and a value that does NOT already start with a quote character.
PATTERN = re.compile(r'^(detail|details):\s+(.*)$', flags=re.MULTILINE)


def quote_value(match: re.Match) -> str:
    key, value = match.group(1), match.group(2)
    if value.startswith(('"', "'")):
        return match.group(0)
    return f'{key}: "{value}"'


def process_file(path: Path) -> bool:
    content = path.read_text()
    new_content = PATTERN.sub(quote_value, content)
    if new_content != content:
        path.write_text(new_content)
        return True
    return False


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__, file=sys.stderr)
        return 1
    changed = []
    unchanged = []
    for arg in argv:
        for path in sorted(Path().glob(arg)) if '*' in arg else [Path(arg)]:
            if not path.is_file():
                print(f"skip (not a file): {path}", file=sys.stderr)
                continue
            if process_file(path):
                changed.append(str(path))
            else:
                unchanged.append(str(path))
    for p in changed:
        print(f"fixed:    {p}")
    for p in unchanged:
        print(f"no change: {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
