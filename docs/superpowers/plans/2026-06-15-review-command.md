# Review Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `review` command that turns the current working-tree changes into a human maintainer review brief.

**Architecture:** Reuse `scan_repository()` for changed files and repository hints. Add `review.py` for risk classification, checklist generation, and Markdown rendering. Wire the CLI in `cli.py` with optional configured verification commands.

**Tech Stack:** Python 3.9+, argparse, pytest.

---

### Task 1: Review Report Contract

**Files:**
- Create: `tests/test_review.py`
- Modify: `tests/test_cli.py`

- [ ] Write failing tests for clean repositories, source+test changes, workflow/security-sensitive changes, Markdown rendering, and CLI file output.
- [ ] Run targeted tests and confirm they fail because `codex_maintainer_kit.review` and the CLI command do not exist.

### Task 2: Review Implementation

**Files:**
- Create: `src/codex_maintainer_kit/review.py`
- Modify: `src/codex_maintainer_kit/cli.py`

- [ ] Add dataclasses for changed-file review items and review reports.
- [ ] Classify changed files into docs, tests, source, config, CI, and security-sensitive groups.
- [ ] Generate a risk level, focused checklist, verification command, and Codex review prompt.
- [ ] Add `codex-maintainer-kit review` with optional `--output`.

### Task 3: Public Documentation

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Create: `examples/CODEX_REVIEW.example.md`

- [ ] Document the `review` command and where it fits in the maintainer workflow.
- [ ] Add an example review report that demonstrates a realistic changed-file set.
- [ ] Update changelog with the unreleased review feature.

### Task 4: Verification

**Files:**
- All changed files.

- [ ] Run `python3 -m pytest -p no:cacheprovider tests -q`.
- [ ] Run `codex-maintainer-kit review` against this repository.
- [ ] Run `git diff --check` and inspect `git status --short`.
