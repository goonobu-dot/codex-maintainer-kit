from pathlib import Path


def test_generated_examples_do_not_include_local_home_paths() -> None:
    for path in Path("examples").glob("*.generated.md"):
        text = path.read_text(encoding="utf-8")
        assert "/Users/" not in text
        assert "file:///Users/" not in text
