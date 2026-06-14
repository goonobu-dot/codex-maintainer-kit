# Agent Instructions

## Scope

These instructions apply to the entire repository.

## Development Rules

- Keep changes small and reviewable.
- Use tests for behavior changes.
- Prefer standard library code unless a dependency removes clear complexity.
- Do not auto-merge AI-generated changes.
- Before claiming completion, run `python3 -m pytest tests -q`.

## Project Intent

This project helps maintainers prepare open source repositories for Codex-assisted maintenance. Changes should preserve that focus: practical maintainer context, clear human review rules, and simple local execution.
