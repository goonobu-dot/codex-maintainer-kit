from pathlib import Path

from codex_maintainer_kit.scanner import scan_repository


def test_scan_repository_detects_maintainer_files(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Demo\n", encoding="utf-8")
    (tmp_path / "LICENSE").write_text("MIT\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname = \"demo\"\n", encoding="utf-8")
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "test.yml").write_text("name: test\n", encoding="utf-8")

    scan = scan_repository(tmp_path)

    assert scan.root == tmp_path
    assert scan.files["readme"] is True
    assert scan.files["license"] is True
    assert scan.files["ci"] is True
    assert scan.files["contributing"] is False
    assert "python" in scan.project_hints


def test_scan_repository_reports_missing_git_as_unknown_not_failure(tmp_path: Path) -> None:
    scan = scan_repository(tmp_path)

    assert scan.git_state.status == "not_a_git_repository"
    assert scan.git_state.changed_files == []


def test_scan_repository_detects_dirty_git_status(tmp_path: Path) -> None:
    (tmp_path / ".git").mkdir()
    (tmp_path / "README.md").write_text("# Demo\n", encoding="utf-8")

    scan = scan_repository(tmp_path, git_status_output=" M README.md\n?? notes.md\n")

    assert scan.git_state.status == "dirty"
    assert scan.git_state.changed_files == ["README.md", "notes.md"]


def test_scan_repository_detects_additional_project_hints(tmp_path: Path) -> None:
    (tmp_path / "pom.xml").write_text("<project />\n", encoding="utf-8")
    (tmp_path / "Package.swift").write_text("// swift-tools-version: 6.0\n", encoding="utf-8")
    (tmp_path / "Demo.csproj").write_text("<Project />\n", encoding="utf-8")

    scan = scan_repository(tmp_path)

    assert "java" in scan.project_hints
    assert "swift" in scan.project_hints
    assert "dotnet" in scan.project_hints
