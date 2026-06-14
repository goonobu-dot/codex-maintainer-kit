# Maintainer Brief

Repository: `/path/to/example-repo`
Project hints: python
Git state: `clean`

## Repository Readiness

- [x] README
- [x] LICENSE
- [ ] CONTRIBUTING
- [ ] CODE_OF_CONDUCT
- [ ] SECURITY
- [ ] CHANGELOG
- [ ] AGENTS.md
- [ ] GitHub issue templates
- [x] CI workflow
- [x] test suite

## Codex Task Queue

- [ ] Add `CONTRIBUTING.md` with local setup, test commands, and PR expectations.
- [ ] Add `SECURITY.md` with vulnerability reporting expectations.
- [ ] Add `AGENTS.md` so Codex and other agents know the repo rules and verification commands.
- [ ] Add issue templates for bugs, docs improvements, and maintenance tasks.

## Suggested Codex Prompt

Use this repository as an open source maintenance target. Review the readiness checklist above, pick one task, make the smallest useful change, run the relevant tests, and explain the tradeoffs before proposing a merge.

## Human Review Rule

Do not auto-merge Codex output. A human maintainer must review the diff, check tests, and decide whether the change matches the project direction.
