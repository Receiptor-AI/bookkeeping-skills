# bookkeeping-skills agent guide

## Repository context

This is the independent `bookkeeping-skills` Git repository. Paths and commands below are relative to this repository's root, whether cloned alone or checked out at `skills/bookkeeping` in the Receiptor monorepo. This file is the canonical repository guide; `CLAUDE.md` is only a local entrypoint. Do not require a parent checkout or sibling repository. Read runtime versions, package-manager requirements and commands from this checkout's package metadata and lockfile. For cross-repository work, request the other repository separately and state what could not be verified locally.

## PR authority

Only Kai may create or publish PRs, including drafts. Kai means a task explicitly launched through Gleap Kai Code (Cloud or Bridge); a standalone Codex, Claude or CLI session is not Kai, even when configuring Kai. Other agents hand off changes and validation results without creating a PR through any tool, API or browser. Follow the repository's configured default/base branch; do not invent a staging branch. Preserve unrelated work, never force-push protected branches, and leave merges, releases and production changes to Romeo's explicit instruction.

## Scope and validation

This repository owns portable bookkeeping skills. `SKILL.md` is the user-facing entrypoint, `skills/` contains task skills, and `jurisdictions/` contains country-specific references. Repository development instructions are separate from those runtime skill instructions.

- Read the affected skill and its referenced resources before editing. Preserve evidence standards, jurisdiction boundaries, approval requirements and accountant-reviewable output.
- Keep references relative to this repository or the individual packaged skill as appropriate. Validate that copied/installed skill folders retain the resources they reference.
- Use examples and supporting material already in the repository for focused validation. There is no package-manager test command to assume from a parent repository.
- Bookkeeping source changes do not authorize filing taxes, moving money or changing a customer's accounting records.
