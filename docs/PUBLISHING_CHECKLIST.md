# Publishing Checklist

Use this checklist before applying to Codex for Open Source.

## Local Repository

- [ ] All tests pass with `python3 -m pytest -p no:cacheprovider tests -q`.
- [ ] README explains purpose, install, usage, and maintainer workflow.
- [ ] Examples are present:
  - `examples/MAINTAINER_BRIEF.generated.md`
  - `examples/CODEX_TASKS.generated.md`
- [ ] Maintainer docs are present:
  - `AGENTS.md`
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `CODE_OF_CONDUCT.md`
  - `CHANGELOG.md`
- [ ] GitHub Actions workflow is present.
- [ ] `v0.1.0` tag exists.

## GitHub

- [ ] Create a public GitHub repository named `codex-maintainer-kit`.
- [ ] Push the local `main` branch.
- [ ] Push the `v0.1.0` tag.
- [ ] Confirm GitHub profile visibility is public.
- [ ] Create 2-3 public issues:
  - Improve generated issue templates.
  - Add more language and package detectors.
  - Add release workflow examples.
- [ ] Confirm the README renders correctly on GitHub.

## Codex for Open Source Form

- [ ] Use ChatGPT account email.
- [ ] Use public GitHub username.
- [ ] Use public GitHub repository URL.
- [ ] Select `Main maintainer`.
- [ ] Select both Codex Security and API credits if desired.
- [ ] Paste the prepared answers from `docs/CODEX_FOR_OSS_APPLICATION.md`.
