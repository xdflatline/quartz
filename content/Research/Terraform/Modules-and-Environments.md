---
title: Modules and Environments
details: "Structural patterns for organizing Terraform across multiple environments."
tags: [research]
created: 2026-06-26
updated: 2026-06-26
type: content
---

# Modules and Environments

The recommended pattern for production environments is **Environment-as-Directory**.

## Structural Pattern
```text
├── modules/             # Reusable modules (VPC, App, DB)
│   ├── vpc/
│   └── app/
└── environments/        # Root configurations calling modules
    ├── dev/
    │   ├── main.tf
    │   └── backend.tf
    ├── stage/
    └── prod/
```

## Why Environment-as-Directory?
- **Blast Radius:** Total state isolation between environments.
- **Safety:** Prevents cross-environment drift or accidental updates to production.
- **Versioning:** Allows pinning modules to specific versions per environment (e.g., canary testing in dev).

## Note on Workspaces
Avoid using Workspaces for environment separation (e.g., prod/staging). Workspaces are designed for managing multiple instances of the same infrastructure (e.g., feature-branch testing) rather than production-grade isolation.
