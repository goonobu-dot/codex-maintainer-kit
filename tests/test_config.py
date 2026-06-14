from pathlib import Path

from codex_maintainer_kit.config import load_config


def test_load_config_returns_defaults_when_file_is_missing(tmp_path: Path) -> None:
    config = load_config(tmp_path)

    assert config.project_name is None
    assert config.verification_command is None
    assert config.default_labels == []


def test_load_config_reads_supported_flat_toml_values(tmp_path: Path) -> None:
    (tmp_path / "codex-maintainer-kit.toml").write_text(
        '\n'.join(
            [
                'project_name = "Demo Project"',
                'verification_command = "npm test"',
                'release_command = "npm run release"',
                'default_labels = ["maintenance", "codex"]',
            ]
        ),
        encoding="utf-8",
    )

    config = load_config(tmp_path)

    assert config.project_name == "Demo Project"
    assert config.verification_command == "npm test"
    assert config.release_command == "npm run release"
    assert config.default_labels == ["maintenance", "codex"]
