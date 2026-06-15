from __future__ import annotations

from dataclasses import dataclass

from codex_maintainer_kit.scanner import RepositoryScan


@dataclass(frozen=True)
class AuditCheck:
    key: str
    label: str
    weight: int
    priority: str
    why_it_matters: str
    next_action: str


@dataclass(frozen=True)
class AuditItem:
    label: str
    status: str
    priority: str
    why_it_matters: str
    next_action: str


@dataclass(frozen=True)
class AuditReport:
    repository: str
    project_hints: list[str]
    git_state: str
    score: int
    status: str
    items: list[AuditItem]
    next_actions: list[str]


AUDIT_CHECKS = [
    AuditCheck(
        key="license",
        label="LICENSE",
        weight=14,
        priority="high",
        why_it_matters="Users need clear reuse rights before they can adopt or contribute to the project.",
        next_action="Add LICENSE: choose the intended license and update README references if needed.",
    ),
    AuditCheck(
        key="agents",
        label="AGENTS.md",
        weight=12,
        priority="high",
        why_it_matters="Codex and other agents need repository rules, commands, and human review boundaries.",
        next_action="Add AGENTS.md: document setup, test commands, coding rules, and the human review rule.",
    ),
    AuditCheck(
        key="tests",
        label="Test suite",
        weight=12,
        priority="high",
        why_it_matters="Automated tests let maintainers verify AI-assisted changes before merge.",
        next_action="Add Test Suite: cover the smallest public behavior users rely on.",
    ),
    AuditCheck(
        key="readme",
        label="README",
        weight=11,
        priority="medium",
        why_it_matters="A useful README explains purpose, setup, usage, and the maintainer workflow.",
        next_action="Update README: add purpose, install steps, usage examples, and verification commands.",
    ),
    AuditCheck(
        key="ci",
        label="CI workflow",
        weight=11,
        priority="medium",
        why_it_matters="CI catches regressions and gives contributors fast feedback.",
        next_action="Add CI Workflow: run the documented test command on pull requests.",
    ),
    AuditCheck(
        key="contributing",
        label="CONTRIBUTING",
        weight=10,
        priority="medium",
        why_it_matters="Contribution docs reduce maintainer back-and-forth and clarify expectations.",
        next_action="Add CONTRIBUTING: document setup, tests, PR expectations, and AI-assisted contribution rules.",
    ),
    AuditCheck(
        key="security",
        label="SECURITY",
        weight=10,
        priority="medium",
        why_it_matters="Security reporting instructions keep sensitive reports out of public issues.",
        next_action="Add SECURITY: explain how to report vulnerabilities and what is in scope.",
    ),
    AuditCheck(
        key="issue_templates",
        label="Issue templates",
        weight=8,
        priority="low",
        why_it_matters="Templates turn vague reports into actionable maintenance work.",
        next_action="Add Issue Templates: include expected behavior, context, and verification fields.",
    ),
    AuditCheck(
        key="changelog",
        label="CHANGELOG",
        weight=7,
        priority="low",
        why_it_matters="Release notes help users understand what changed and whether to upgrade.",
        next_action="Add CHANGELOG: record the current release state without claiming future work.",
    ),
    AuditCheck(
        key="code_of_conduct",
        label="CODE_OF_CONDUCT",
        weight=5,
        priority="low",
        why_it_matters="Community expectations help public projects handle collaboration consistently.",
        next_action="Add CODE_OF_CONDUCT: set basic contribution behavior and maintainer response expectations.",
    ),
]


def build_audit_report(scan: RepositoryScan) -> AuditReport:
    total_weight = sum(check.weight for check in AUDIT_CHECKS)
    earned_weight = sum(check.weight for check in AUDIT_CHECKS if scan.files.get(check.key, False))
    score = round((earned_weight / total_weight) * 100)
    items = [_build_item(scan, check) for check in AUDIT_CHECKS]
    next_actions = [item.next_action for item in items if item.status == "missing"][:5]
    if not next_actions:
        next_actions = ["Run a focused Codex maintenance review for stale docs, missing edge-case tests, and small safe improvements."]

    return AuditReport(
        repository=str(scan.root),
        project_hints=scan.project_hints,
        git_state=scan.git_state.status,
        score=score,
        status=_status_for_score(score),
        items=items,
        next_actions=next_actions,
    )


def render_audit_markdown(report: AuditReport) -> str:
    lines = [
        "# OSS Maintenance Audit",
        "",
        f"Repository: `{report.repository}`",
        f"Project hints: {', '.join(report.project_hints)}",
        f"Git state: `{report.git_state}`",
        f"Health score: **{report.score}/100** (`{report.status}`)",
        "",
        "## Maintainer Essentials",
        "",
        "| Check | Status | Priority | Why it matters |",
        "| --- | --- | --- | --- |",
    ]

    for item in report.items:
        lines.append(f"| {item.label} | {item.status} | {item.priority} | {item.why_it_matters} |")

    lines.extend(["", "## Prioritized Next Actions", ""])
    for action in report.next_actions:
        lines.append(f"- [ ] {action}")

    lines.extend(
        [
            "",
            "## Suggested Codex Prompt",
            "",
            "Review this OSS maintenance audit. Pick the highest-priority missing item, make the smallest useful change, run the documented verification command, and leave a concise maintainer note explaining the tradeoff and risk.",
            "",
            "## Human Review Rule",
            "",
            "Do not auto-merge AI-generated maintenance changes. A human maintainer must review the diff, confirm the project policy choices, and verify the result before merge.",
            "",
        ]
    )
    return "\n".join(lines)


def _build_item(scan: RepositoryScan, check: AuditCheck) -> AuditItem:
    present = scan.files.get(check.key, False)
    return AuditItem(
        label=check.label,
        status="ready" if present else "missing",
        priority=check.priority,
        why_it_matters=check.why_it_matters,
        next_action=check.next_action,
    )


def _status_for_score(score: int) -> str:
    if score >= 90:
        return "ready"
    if score >= 70:
        return "mostly-ready"
    return "needs-work"
