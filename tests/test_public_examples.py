from pathlib import Path


def test_generated_examples_do_not_include_local_home_paths() -> None:
    for path in Path("examples").glob("*.generated.md"):
        text = path.read_text(encoding="utf-8")
        assert "/Users/" not in text
        assert "file:///Users/" not in text


def test_public_repo_ci_uses_minimal_permissions_and_node24_actions() -> None:
    workflow = Path(".github/workflows/tests.yml").read_text(encoding="utf-8")
    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert "actions/checkout@v5" in workflow
    assert "actions/setup-python@v6" in workflow


def test_dependabot_covers_actions_and_python_packaging() -> None:
    dependabot = Path(".github/dependabot.yml").read_text(encoding="utf-8")
    assert 'package-ecosystem: "github-actions"' in dependabot
    assert 'package-ecosystem: "pip"' in dependabot
    assert 'interval: "monthly"' in dependabot
    assert "version-update:semver-major" in dependabot


def test_readme_links_beginner_guides() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/BEGINNER_GUIDE.md" in readme
    assert "docs/BEGINNER_GUIDE.ja.md" in readme
    assert "docs/START_HERE.md" in readme
    assert "docs/START_HERE.ja.md" in readme
    assert "docs/USE_CASES.md" in readme
    assert "docs/USE_CASES.ja.md" in readme


def test_beginner_guides_explain_project_in_plain_language() -> None:
    english = Path("docs/BEGINNER_GUIDE.md").read_text(encoding="utf-8")
    japanese = Path("docs/BEGINNER_GUIDE.ja.md").read_text(encoding="utf-8")
    assert "Beginner-Friendly Guide" in english
    assert "maintenance health check" in english
    assert "Codex Maintainer Kit やさしい解説" in japanese
    assert "中学生でも分かる" in japanese


def test_start_here_and_use_cases_help_first_time_users() -> None:
    english_start = Path("docs/START_HERE.md").read_text(encoding="utf-8")
    japanese_start = Path("docs/START_HERE.ja.md").read_text(encoding="utf-8")
    english_cases = Path("docs/USE_CASES.md").read_text(encoding="utf-8")
    japanese_cases = Path("docs/USE_CASES.ja.md").read_text(encoding="utf-8")
    assert "Start Here" in english_start
    assert "First 3 minutes" in english_start
    assert "まずここから" in japanese_start
    assert "最初の3分" in japanese_start
    assert "Use Cases" in english_cases
    assert "maintenance audit" in english_cases
    assert "ユースケース" in japanese_cases
    assert "メンテナンス監査" in japanese_cases
