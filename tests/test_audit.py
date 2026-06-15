from pathlib import Path

from codex_maintainer_kit.audit import build_audit_report, render_audit_markdown
from codex_maintainer_kit.scanner import GitState, RepositoryScan


def _scan(files: dict[str, bool]) -> RepositoryScan:
    return RepositoryScan(
        root=Path("/repo/demo"),
        files=files,
        project_hints=["python"],
        git_state=GitState(status="clean", changed_files=[]),
    )


def test_build_audit_report_scores_ready_repository() -> None:
    report = build_audit_report(
        _scan(
            {
                "readme": True,
                "license": True,
                "contributing": True,
                "code_of_conduct": True,
                "security": True,
                "changelog": True,
                "agents": True,
                "issue_templates": True,
                "ci": True,
                "tests": True,
            }
        )
    )

    assert report.score == 100
    assert report.status == "ready"
    assert all(item.status == "ready" for item in report.items)
    assert report.next_actions == ["Run a focused Codex maintenance review for stale docs, missing edge-case tests, and small safe improvements."]


def test_build_audit_report_prioritizes_missing_maintainer_essentials() -> None:
    report = build_audit_report(
        _scan(
            {
                "readme": True,
                "license": False,
                "contributing": False,
                "code_of_conduct": True,
                "security": False,
                "changelog": True,
                "agents": False,
                "issue_templates": False,
                "ci": True,
                "tests": False,
            }
        )
    )

    assert report.score < 70
    assert report.status == "needs-work"
    assert [action.split(":", 1)[0] for action in report.next_actions[:3]] == ["Add LICENSE", "Add AGENTS.md", "Add Test Suite"]


def test_render_audit_markdown_is_maintainer_friendly() -> None:
    report = build_audit_report(
        _scan(
            {
                "readme": True,
                "license": False,
                "contributing": True,
                "code_of_conduct": True,
                "security": True,
                "changelog": True,
                "agents": False,
                "issue_templates": True,
                "ci": True,
                "tests": True,
            }
        )
    )

    markdown = render_audit_markdown(report)

    assert markdown.startswith("# OSS Maintenance Audit")
    assert "Health score:" in markdown
    assert "## Maintainer Essentials" in markdown
    assert "## Prioritized Next Actions" in markdown
    assert "## Suggested Codex Prompt" in markdown
    assert "| LICENSE | missing | high |" in markdown
