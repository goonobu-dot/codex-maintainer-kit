# Audit Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an `audit` command that generates a practical OSS maintenance health report.

**Architecture:** Keep scanning in `scanner.py`, add audit scoring and report rendering in a new `audit.py`, and wire the CLI in `cli.py`. The audit report reuses existing repository facts and gives maintainers a prioritized next-step summary.

**Tech Stack:** Python 3.9+, argparse, pytest.

---

### Task 1: Audit Report Contract

**Files:**
- Create: `tests/test_audit.py`
- Modify: `tests/test_cli.py`

- [ ] Write failing tests for audit item classification, summary score, Markdown rendering, and CLI file output.
- [ ] Run targeted tests and confirm they fail because `codex_maintainer_kit.audit` and the CLI command do not exist.

### Task 2: Audit Implementation

**Files:**
- Create: `src/codex_maintainer_kit/audit.py`
- Modify: `src/codex_maintainer_kit/cli.py`

- [ ] Add `AuditItem` and `AuditReport` dataclasses.
- [ ] Add `build_audit_report(scan)` with weighted checks for maintainer essentials.
- [ ] Add `render_audit_markdown(report)` with score, status summary, prioritized next actions, and Codex prompt.
- [ ] Add `codex-maintainer-kit audit` with optional `--output`.
- [ ] Run targeted tests until they pass.

### Task 3: Public Documentation

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Create: `examples/OSS_MAINTENANCE_AUDIT.generated.md`

- [ ] Document the `audit` command and how it fits before `brief` and `tasks`.
- [ ] Generate an example audit report from this repository.
- [ ] Update changelog with the unreleased audit feature.

### Task 4: Verification

**Files:**
- All changed files.

- [ ] Run `python3 -m pytest -p no:cacheprovider tests -q`.
- [ ] Run the new CLI command against this repository.
- [ ] Review `git diff --check` and `git status --short`.
