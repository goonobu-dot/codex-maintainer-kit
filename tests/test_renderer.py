from pathlib import Path

from codex_maintainer_kit.renderer import render_maintenance_brief
from codex_maintainer_kit.scanner import GitState, RepositoryScan


def test_render_maintenance_brief_includes_codex_ready_sections() -> None:
    scan = RepositoryScan(
        root=Path("/repo/demo"),
        files={
            "readme": True,
            "license": False,
            "contributing": False,
            "code_of_conduct": False,
            "security": False,
            "changelog": False,
            "agents": False,
            "issue_templates": False,
            "ci": True,
            "tests": True,
        },
        project_hints=["python"],
        git_state=GitState(status="dirty", changed_files=["README.md"]),
    )

    markdown = render_maintenance_brief(scan)

    assert markdown.startswith("# Maintainer Brief")
    assert "## Repository Readiness" in markdown
    assert "## Codex Task Queue" in markdown
    assert "## Human Review Rule" in markdown
    assert "Do not auto-merge Codex output" in markdown
    assert "- [ ] Add or update `LICENSE`" in markdown


def test_render_maintenance_brief_prioritizes_existing_gaps() -> None:
    scan = RepositoryScan(
        root=Path("/repo/ready"),
        files={
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
        },
        project_hints=["javascript"],
        git_state=GitState(status="clean", changed_files=[]),
    )

    markdown = render_maintenance_brief(scan)

    assert "No foundational gaps detected" in markdown
    assert "Run a focused Codex review" in markdown
