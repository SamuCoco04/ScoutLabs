from __future__ import annotations

import os
from pathlib import Path

import pytest

from scoutlabs.config import DatasetNotFoundError, resolve_data_dir


def test_resolve_data_dir_uses_explicit_argument(tmp_path: Path) -> None:
    data_dir = tmp_path / "dataset"
    data_dir.mkdir()
    (data_dir / "competitions.json").write_text("[]", encoding="utf-8")

    resolved = resolve_data_dir(data_dir=data_dir, cwd=tmp_path, env={})

    assert resolved == data_dir.resolve()


def test_resolve_data_dir_prefers_environment_over_dotenv(tmp_path: Path) -> None:
    environment_dir = tmp_path / "from-environment"
    dotenv_dir = tmp_path / "from-dotenv"
    for data_dir in (environment_dir, dotenv_dir):
        data_dir.mkdir()
        (data_dir / "competitions.json").write_text("[]", encoding="utf-8")
    (tmp_path / ".env").write_text(
        f"STATSBOMB_DATA_DIR={dotenv_dir}\n",
        encoding="utf-8",
    )

    resolved = resolve_data_dir(
        cwd=tmp_path,
        env={"STATSBOMB_DATA_DIR": str(environment_dir)},
    )

    assert resolved == environment_dir.resolve()


def test_resolve_data_dir_uses_dotenv_without_overwriting_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    environment_dir = tmp_path / "from-environment"
    dotenv_dir = tmp_path / "from-dotenv"
    for data_dir in (environment_dir, dotenv_dir):
        data_dir.mkdir()
        (data_dir / "competitions.json").write_text("[]", encoding="utf-8")
    (tmp_path / ".env").write_text(
        f"STATSBOMB_DATA_DIR={dotenv_dir}\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("STATSBOMB_DATA_DIR", str(environment_dir))

    resolved = resolve_data_dir(cwd=tmp_path)

    assert resolved == environment_dir.resolve()
    assert os.environ["STATSBOMB_DATA_DIR"] == str(environment_dir)


def test_resolve_data_dir_uses_dotenv_when_environment_is_absent(tmp_path: Path) -> None:
    dotenv_dir = tmp_path / "from-dotenv"
    dotenv_dir.mkdir()
    (dotenv_dir / "competitions.json").write_text("[]", encoding="utf-8")
    (tmp_path / ".env").write_text(
        f"STATSBOMB_DATA_DIR={dotenv_dir}\n",
        encoding="utf-8",
    )

    resolved = resolve_data_dir(cwd=tmp_path, env={})

    assert resolved == dotenv_dir.resolve()


def test_resolve_data_dir_falls_back_to_local_dataset(tmp_path: Path) -> None:
    local_dir = tmp_path / "data" / "statsbomb-open-data" / "data"
    local_dir.mkdir(parents=True)
    (local_dir / "competitions.json").write_text("[]", encoding="utf-8")

    resolved = resolve_data_dir(cwd=tmp_path, env={})

    assert resolved == local_dir.resolve()


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
