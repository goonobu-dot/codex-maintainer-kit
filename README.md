# Codex Maintainer Kit

Codex Maintainer Kit prepares open source repositories for Codex-assisted maintenance.

It scans a local repository, identifies basic maintenance gaps, and generates a `MAINTAINER_BRIEF.md` that a human maintainer can hand to Codex before asking it to improve docs, tests, issue templates, release notes, or repository instructions.

The goal is not to replace maintainers. The goal is to make recurring maintenance work easier to review, delegate, and verify.

## Why This Exists

Open source maintenance is rarely just writing new code. Maintainers spend time on:

- keeping README and contribution docs accurate
- adding tests before refactors
- preparing releases and changelogs
- reviewing pull requests
- making issue reports easier to act on
- deciding what AI-generated changes are safe to merge

Codex can help with that work, but it needs clear repository context and human review rules. This kit creates that starting context.

## What It Does

- Detects common maintainer files such as `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `AGENTS.md`, issue templates, CI workflows, and tests.
- Detects simple project hints such as Python, JavaScript, Go, Rust, Ruby, and PHP markers.
- Summarizes current Git working-tree changes.
- Generates a Markdown maintainer brief with:
  - repository readiness checklist
  - Codex task queue
  - suggested Codex prompt
  - human review rule
- Creates starter maintainer files with `init`.
- Turns readiness gaps into `CODEX_TASKS.md`, JSON, and GitHub issue Markdown files with `tasks`.
- Adds suggested labels, verification commands, and maintainer review checklists to generated issue drafts.

## Installation

From a local checkout:

```bash
python3 -m pip install -e .
```

## Usage

Generate a maintainer brief:

```bash
codex-maintainer-kit brief /path/to/repo --output MAINTAINER_BRIEF.md
```

Generate Codex-ready maintenance tasks:

```bash
codex-maintainer-kit tasks /path/to/repo --output CODEX_TASKS.md
```

Generate machine-readable tasks:

```bash
codex-maintainer-kit tasks /path/to/repo --format json --output codex-tasks.json
```

Generate GitHub issue drafts:

```bash
codex-maintainer-kit tasks /path/to/repo --github-issues-dir .github/generated-maintenance-issues
```

Preview starter files:

```bash
codex-maintainer-kit init /path/to/repo --dry-run
```

Create starter files:

```bash
codex-maintainer-kit init /path/to/repo
```

The `init` command creates:

- `AGENTS.md`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/maintenance.md`

Existing files are skipped unless `--force` is passed.

## Example Output

See:

- [examples/MAINTAINER_BRIEF.example.md](examples/MAINTAINER_BRIEF.example.md)
- [examples/MAINTAINER_BRIEF.generated.md](examples/MAINTAINER_BRIEF.generated.md), generated from this repository
- [examples/CODEX_TASKS.example.md](examples/CODEX_TASKS.example.md)
- [examples/CODEX_TASKS.generated.md](examples/CODEX_TASKS.generated.md), generated from this repository

## Codex for Open Source

This project was created for maintainers who want to use Codex in open source workflows without removing human review.

The application notes and publishing checklist live in:

- [docs/CODEX_FOR_OSS_APPLICATION.md](docs/CODEX_FOR_OSS_APPLICATION.md)
- [docs/PUBLISHING_CHECKLIST.md](docs/PUBLISHING_CHECKLIST.md)

## How This Differs From Existing Tools

This project is intentionally not a replacement for mature repository health or security tools.

- [OpenSSF Scorecard](https://github.com/ossf/scorecard) measures open source security posture.
- [Repolinter](https://github.com/todogroup/repolinter) linted repository metadata and policy files.

Codex Maintainer Kit focuses on a narrower workflow: creating a practical maintenance brief, turning gaps into Codex-ready tasks, generating issue drafts, and keeping human review as the final checkpoint.

## Maintainer Workflow

1. Run `codex-maintainer-kit brief`.
2. Review the generated checklist.
3. Run `codex-maintainer-kit tasks`.
4. Convert the generated task file or issue drafts into scoped maintenance work.
5. Ask Codex to make the smallest useful change.
6. Run tests and inspect the diff.
7. Merge only after human review.

## Development

Run tests:

```bash
python3 -m pytest tests -q
```

Run the CLI without installing:

```bash
PYTHONPATH=src python3 -m codex_maintainer_kit.cli brief . --output /tmp/maintainer-brief.md
PYTHONPATH=src python3 -m codex_maintainer_kit.cli tasks . --output /tmp/codex-tasks.md
```

## License

MIT
