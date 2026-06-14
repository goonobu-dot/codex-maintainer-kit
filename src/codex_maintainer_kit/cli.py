from __future__ import annotations

import argparse
from pathlib import Path
import sys

from codex_maintainer_kit.config import load_config
from codex_maintainer_kit.renderer import render_maintenance_brief
from codex_maintainer_kit.scanner import scan_repository
from codex_maintainer_kit.tasks import build_tasks, render_issue_markdown, render_tasks_json, render_tasks_markdown


TEMPLATES = {
    "AGENTS.md": """# Agent Instructions

## Scope

These instructions apply to this repository.

## Development

- Keep changes small and reviewable.
- Prefer tests for user-visible behavior.
- Run the documented test command before claiming work is complete.
- Do not auto-merge AI-generated changes.
""",
    "CONTRIBUTING.md": """# Contributing

Thanks for helping maintain this project.

## Local Workflow

1. Create a focused branch.
2. Make the smallest useful change.
3. Add or update tests when behavior changes.
4. Run the project test command.
5. Open a pull request with the reason, risk, and verification result.
""",
    ".github/ISSUE_TEMPLATE/maintenance.md": """---
name: Maintenance task
about: Track documentation, testing, release, or repository health work
title: "Maintenance: "
labels: maintenance
---

## Goal

## Current problem

## Suggested verification
""",
}


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "brief":
        return _brief(args)
    if args.command == "init":
        return _init(args)
    if args.command == "tasks":
        return _tasks(args)

    parser.print_help()
    return 1


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-maintainer-kit",
        description="Prepare open source repositories for Codex-assisted maintenance.",
    )
    subparsers = parser.add_subparsers(dest="command")

    brief = subparsers.add_parser("brief", help="Generate a Codex-ready maintainer brief.")
    brief.add_argument("repo", nargs="?", default=".", help="Repository path to inspect.")
    brief.add_argument("--output", "-o", help="Write Markdown to this file instead of stdout.")

    init = subparsers.add_parser("init", help="Create starter maintainer files.")
    init.add_argument("repo", nargs="?", default=".", help="Repository path to update.")
    init.add_argument("--dry-run", action="store_true", help="List files that would be written.")
    init.add_argument("--force", action="store_true", help="Overwrite existing files.")

    tasks = subparsers.add_parser("tasks", help="Generate Codex-ready maintenance tasks.")
    tasks.add_argument("repo", nargs="?", default=".", help="Repository path to inspect.")
    tasks.add_argument("--output", "-o", help="Write task output to this file instead of stdout.")
    tasks.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Task output format.")
    tasks.add_argument("--github-issues-dir", help="Write one GitHub issue Markdown file per task.")
    return parser


def _brief(args: argparse.Namespace) -> int:
    scan = scan_repository(args.repo)
    markdown = render_maintenance_brief(scan)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


def _init(args: argparse.Namespace) -> int:
    root = Path(args.repo).resolve()
    if not root.exists() or not root.is_dir():
        raise FileNotFoundError(f"Repository path does not exist or is not a directory: {root}")

    for relative_path, content in TEMPLATES.items():
        target = root / relative_path
        if args.dry_run:
            print(relative_path)
            continue
        if target.exists() and not args.force:
            print(f"skip existing {relative_path}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        print(f"wrote {relative_path}")
    return 0


def _tasks(args: argparse.Namespace) -> int:
    scan = scan_repository(args.repo)
    config = load_config(scan.root)
    tasks = build_tasks(scan, config=config)
    if args.format == "json":
        output_text = render_tasks_json(scan, tasks)
    else:
        output_text = render_tasks_markdown(scan, tasks)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(output_text, encoding="utf-8")
    else:
        print(output_text)

    if args.github_issues_dir:
        issues_dir = Path(args.github_issues_dir)
        issues_dir.mkdir(parents=True, exist_ok=True)
        for index, task in enumerate(tasks, start=1):
            filename = f"{index:02d}-{task.id}.md"
            (issues_dir / filename).write_text(render_issue_markdown(task), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
