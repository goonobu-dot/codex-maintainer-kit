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
