from pathlib import Path

from codex_maintainer_kit.cli import main


def test_brief_command_writes_markdown_file(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "README.md").write_text("# Demo\n", encoding="utf-8")
    output = tmp_path / "brief.md"

    exit_code = main(["brief", str(repo), "--output", str(output)])

    assert exit_code == 0
    text = output.read_text(encoding="utf-8")
    assert text.startswith("# Maintainer Brief")
    assert "Codex Task Queue" in text


def test_init_dry_run_lists_files_without_writing(tmp_path: Path, capsys) -> None:
    exit_code = main(["init", str(tmp_path), "--dry-run"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "AGENTS.md" in captured.out
    assert "CONTRIBUTING.md" in captured.out
    assert not (tmp_path / "AGENTS.md").exists()


def test_tasks_command_writes_markdown_file(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "README.md").write_text("# Demo\n", encoding="utf-8")
    output = tmp_path / "CODEX_TASKS.md"

    exit_code = main(["tasks", str(repo), "--output", str(output)])

    assert exit_code == 0
    text = output.read_text(encoding="utf-8")
    assert text.startswith("# Codex Maintenance Tasks")
    assert "## Task 1: Add LICENSE" in text


def test_tasks_command_writes_json_file(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    output = tmp_path / "tasks.json"

    exit_code = main(["tasks", str(repo), "--format", "json", "--output", str(output)])

    assert exit_code == 0
    text = output.read_text(encoding="utf-8")
    assert '"tasks"' in text
    assert '"id": "update-readme"' in text


def test_tasks_command_writes_github_issue_files(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    issues_dir = tmp_path / "issues"

    exit_code = main(["tasks", str(repo), "--github-issues-dir", str(issues_dir)])

    assert exit_code == 0
    files = sorted(path.name for path in issues_dir.iterdir())
    assert "01-add-license.md" in files
    assert "02-add-agents.md" in files
    assert (issues_dir / "01-add-license.md").read_text(encoding="utf-8").startswith("# Add LICENSE")
