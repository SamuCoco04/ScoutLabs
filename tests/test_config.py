from __future__ import annotations

from pathlib import Path

import pytest

from scoutlabs.config import DatasetNotFoundError, resolve_data_dir


def test_resolve_data_dir_uses_explicit_argument(tmp_path: Path) -> None:
    data_dir = tmp_path / "dataset"
    data_dir.mkdir()
    (data_dir / "competitions.json").write_text("[]", encoding="utf-8")

    resolved = resolve_data_dir(data_dir=data_dir, cwd=tmp_path, env={})

    assert resolved == data_dir.resolve()


def test_resolve_data_dir_falls_back_to_default_relative_path(tmp_path: Path) -> None:
    default_dir = (tmp_path / ".." / "open-data" / "data").resolve()
    default_dir.mkdir(parents=True)
    (default_dir / "competitions.json").write_text("[]", encoding="utf-8")

    resolved = resolve_data_dir(cwd=tmp_path, env={})

    assert resolved == default_dir


def test_resolve_data_dir_raises_clear_error_when_missing(tmp_path: Path) -> None:
    isolated_cwd = tmp_path / "isolated"
    isolated_cwd.mkdir()

    with pytest.raises(DatasetNotFoundError, match="competitions.json"):
        resolve_data_dir(cwd=isolated_cwd, env={})
