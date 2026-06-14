from __future__ import annotations

from codex_maintainer_kit.scanner import RepositoryScan


LABELS = {
    "readme": "README",
    "license": "LICENSE",
    "contributing": "CONTRIBUTING",
    "code_of_conduct": "CODE_OF_CONDUCT",
    "security": "SECURITY",
    "changelog": "CHANGELOG",
    "agents": "AGENTS.md",
    "issue_templates": "GitHub issue templates",
    "ci": "CI workflow",
    "tests": "test suite",
}


TASKS = {
    "readme": "Add or update `README.md` with purpose, install steps, usage examples, and maintenance status.",
    "license": "Add or update `LICENSE` so users know how they can reuse the project.",
    "contributing": "Add `CONTRIBUTING.md` with local setup, test commands, and PR expectations.",
    "code_of_conduct": "Add `CODE_OF_CONDUCT.md` if the project accepts outside participation.",
    "security": "Add `SECURITY.md` with vulnerability reporting expectations.",
    "changelog": "Add `CHANGELOG.md` or release notes before the first public tag.",
    "agents": "Add `AGENTS.md` so Codex and other agents know the repo rules and verification commands.",
    "issue_templates": "Add issue templates for bugs, docs improvements, and maintenance tasks.",
    "ci": "Add a CI workflow that runs tests on pull requests.",
    "tests": "Add a minimal test suite that covers the public behavior users rely on.",
}


def render_maintenance_brief(scan: RepositoryScan) -> str:
    missing = [key for key, present in scan.files.items() if not present]
    lines: list[str] = [
        "# Maintainer Brief",
        "",
        f"Repository: `{scan.root}`",
        f"Project hints: {', '.join(scan.project_hints)}",
        f"Git state: `{scan.git_state.status}`",
        "",
        "## Repository Readiness",
        "",
    ]

    for key, label in LABELS.items():
        mark = "x" if scan.files.get(key, False) else " "
        lines.append(f"- [{mark}] {label}")

    lines.extend(["", "## Codex Task Queue", ""])
    if missing:
        for key in missing:
            lines.append(f"- [ ] {TASKS[key]}")
    else:
        lines.append("- [ ] No foundational gaps detected. Run a focused Codex review for defects, stale docs, and missing edge-case tests.")

    if scan.git_state.changed_files:
        lines.extend(["", "## Current Working Tree", ""])
        for path in scan.git_state.changed_files:
            lines.append(f"- `{path}`")

    lines.extend(
        [
            "",
            "## Suggested Codex Prompt",
            "",
            "Use this repository as an open source maintenance target. Review the readiness checklist above, pick one task, make the smallest useful change, run the relevant tests, and explain the tradeoffs before proposing a merge.",
            "",
            "## Human Review Rule",
            "",
            "Do not auto-merge Codex output. A human maintainer must review the diff, check tests, and decide whether the change matches the project direction.",
            "",
        ]
    )
    return "\n".join(lines)
