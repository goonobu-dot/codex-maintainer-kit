from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import ast


CONFIG_FILENAME = "codex-maintainer-kit.toml"


@dataclass(frozen=True)
class MaintainerConfig:
    project_name: str | None = None
    verification_command: str | None = None
    release_command: str | None = None
    default_labels: list[str] | None = None

    def __post_init__(self) -> None:
        if self.default_labels is None:
            object.__setattr__(self, "default_labels", [])


def load_config(root: str | Path) -> MaintainerConfig:
    path = Path(root) / CONFIG_FILENAME
    if not path.exists():
        return MaintainerConfig()

    values: dict[str, object] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue
        key, raw_value = stripped.split("=", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if key in {"project_name", "verification_command", "release_command"}:
            values[key] = _parse_string(raw_value)
        elif key == "default_labels":
            values[key] = _parse_string_list(raw_value)

    return MaintainerConfig(
        project_name=_optional_string(values.get("project_name")),
        verification_command=_optional_string(values.get("verification_command")),
        release_command=_optional_string(values.get("release_command")),
        default_labels=_string_list(values.get("default_labels")),
    )


def _parse_string(raw_value: str) -> str:
    value = ast.literal_eval(raw_value)
    if not isinstance(value, str):
        raise ValueError(f"Expected string value, got: {raw_value}")
    return value


def _parse_string_list(raw_value: str) -> list[str]:
    value = ast.literal_eval(raw_value)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"Expected list of strings, got: {raw_value}")
    return value


def _optional_string(value: object | None) -> str | None:
    return value if isinstance(value, str) else None


def _string_list(value: object | None) -> list[str]:
    return value if isinstance(value, list) and all(isinstance(item, str) for item in value) else []
