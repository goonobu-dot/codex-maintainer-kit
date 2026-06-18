# Start Here

This page helps a first-time visitor understand Codex Maintainer Kit in the First 3 minutes.

## What This Project Is

Codex Maintainer Kit is a local CLI that prepares an open source repository for human-reviewed Codex-assisted maintenance. It scans a repository and creates practical Markdown artifacts such as a maintenance audit, maintainer brief, task queue, and review report.

## First 3 minutes

1. Read the [beginner guide](BEGINNER_GUIDE.md) if the project is new to you.
2. Skim [Use Cases](USE_CASES.md) to choose the right command.
3. Install locally with `python3 -m pip install -e .`.
4. Run `codex-maintainer-kit audit . --output OSS_MAINTENANCE_AUDIT.md` on a test repository.

## Choose Your Path

| You need | Run | Read next |
| --- | --- | --- |
| A repository health check | `audit` | [Use Cases](USE_CASES.md) |
| A Codex-ready context brief | `brief` | [Example output](../examples/MAINTAINER_BRIEF.example.md) |
| Maintenance tasks | `tasks` | [Task schema](../schema/codex-tasks.schema.json) |
| Human review of local changes | `review` | [Review example](../examples/CODEX_REVIEW.example.md) |

## Safety Note

The kit generates artifacts for human review. It does not auto-merge code, open pull requests, or grant Codex repository write access.
