---
name: release-notes
description: Generate concise release notes from the repository's Git history and current changes without modifying files. Use when a user asks for release notes, a changelog summary, or an overview of recent commits and working-tree changes.
---

# Release Notes

Generate release notes from the current repository state. This skill is read-only: do not edit, create, delete, rename, stage, commit, or revert files.

## Process

1. Inspect the current Git status.
2. Review the diff for tracked changes.
3. Review recent commits when useful for context.
4. Group changes by user-visible area or technical area.
5. Mention tests or validation evidence only when it is available.
6. Call out breaking changes, migration steps, unresolved issues, or unrelated pre-existing changes when relevant.

## Output format

# Release Notes

## Highlights

- Concise user-facing summary of the most important changes.

## Changes

- Grouped bullet points describing the changes.

## Fixes

- Bug fixes, if any.

## Validation

- Tests or checks that were actually run.

## Notes

- Breaking changes, limitations, or follow-up work.

If there are no meaningful changes, say so explicitly. Never invent changes or claim that files were modified by this skill.
