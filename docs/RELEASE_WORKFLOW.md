# Release Workflow

This workflow keeps releases human-reviewed while using Codex to prepare maintenance context.

## Release Principles

- Codex can draft release notes, review readiness, and identify missing maintenance work.
- Codex should not publish releases automatically.
- A human maintainer owns the final tag, GitHub Release, and merge decision.

## Pre-Release Checklist

1. Generate the maintainer brief:

   ```bash
   PYTHONPATH=src python3 -m codex_maintainer_kit.cli brief . --output MAINTAINER_BRIEF.md
   ```

2. Generate Codex maintenance tasks:

   ```bash
   PYTHONPATH=src python3 -m codex_maintainer_kit.cli tasks . --output CODEX_TASKS.md
   ```

3. Ask Codex to review release readiness:

   ```text
   Review MAINTAINER_BRIEF.md, CODEX_TASKS.md, README.md, CHANGELOG.md, and the current diff.
   Identify only release-blocking issues and small documentation fixes.
   Do not propose auto-release or auto-merge behavior.
   ```

4. Run tests:

   ```bash
   python3 -m pytest -p no:cacheprovider tests -q
   ```

5. Update `CHANGELOG.md` with the release version and date.

6. Commit the release notes:

   ```bash
   git add CHANGELOG.md
   git commit -m "docs: prepare vX.Y.Z release"
   ```

7. Tag the release:

   ```bash
   git tag -a vX.Y.Z -m "vX.Y.Z"
   ```

8. Push the branch and tag:

   ```bash
   git push origin main
   git push origin vX.Y.Z
   ```

9. Create the GitHub Release:

   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md
   ```

## Human Review Gate

Before publishing, confirm:

- [ ] Tests pass locally or in GitHub Actions.
- [ ] The changelog only claims shipped behavior.
- [ ] Generated Codex tasks do not include release blockers.
- [ ] No secrets, tokens, or private paths are included in release notes.
- [ ] A human maintainer reviewed the final diff.

## Why This Matters

The project is designed for AI-assisted OSS maintenance, not unattended automation. Release preparation should demonstrate the same operating model: Codex can surface work and draft changes, but maintainers keep control over publishing.
