---
title: Conventional Commits

details: Conventional Commits is a specification for adding human and machine readable change history to the commit message.
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
Conventional Commits is a specification for adding human and machine readable change history to the commit message.

**Format:**

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

**Types:**
*   `feat`: A new feature.
*   `fix`: A bug fix.
*   `chore`: Routine tasks, maintenance, build processes, or other changes that don't modify src or test files.
*   `refactor`: A code change that neither fixes a bug nor adds a feature.
*   `docs`: Documentation only changes.
*   `style`: Changes that do not affect the meaning of the code (white-space, formatting, semi-colons, etc).
*   `test`: Adding missing tests or correcting existing tests.
*   `perf`: A code change that improves performance.

**Scope:**
*   Optional. A noun describing the section of the codebase affected.

**Description:**
*   A concise, imperative summary of the change.
*   Starts with a lowercase letter and does not end with a period.

**Body:**
*   A more detailed explanation of the change, providing context, motivation, and any other relevant information.

**Footer:**
*   Used for referencing issues (e.g., `Closes #123`) or noting breaking changes (`BREAKING CHANGE: ...`).