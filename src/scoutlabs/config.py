from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values, load_dotenv


class DatasetNotFoundError(FileNotFoundError):
    pass


@dataclass(slots=True, frozen=True)
class DatasetPaths:
    root: Path

    @property
    def competitions_file(self) -> Path:
        return self.root / "competitions.json"

    @property
    def matches_dir(self) -> Path:
        return self.root / "matches"

    @property
    def lineups_dir(self) -> Path:
        return self.root / "lineups"

    @property
    def events_dir(self) -> Path:
        return self.root / "events"

    @property
    def three_sixty_dir(self) -> Path:
        return self.root / "three-sixty"


def _resolve_candidate(candidate: str | Path, cwd: Path) -> Path:
    path = Path(candidate)
    if not path.is_absolute():
        path = (cwd / path).resolve()
    return path


def resolve_data_dir(
    data_dir: str | Path | None = None,
    *,
    env: Mapping[str, str] | None = None,
    cwd: Path | None = None,
) -> Path:
    current_dir = cwd or Path.cwd()
    environment = os.environ if env is None else env
    dotenv_path = current_dir / ".env"
    dotenv_config = dotenv_values(dotenv_path)
    if env is None:
        load_dotenv(dotenv_path=dotenv_path, override=False)

    candidates: list[Path] = []
    if data_dir is not None:
        candidates.append(_resolve_candidate(data_dir, current_dir))

    env_value = environment.get("STATSBOMB_DATA_DIR")
    if env_value:
        candidates.append(_resolve_candidate(env_value, current_dir))

    dotenv_value = dotenv_config.get("STATSBOMB_DATA_DIR")
    if dotenv_value:
        candidates.append(_resolve_candidate(dotenv_value, current_dir))

    candidates.extend(
        [
            _resolve_candidate("data/statsbomb-open-data/data", current_dir),
            _resolve_candidate("../open-data/data", current_dir),
            _resolve_candidate("../statsbomb-open-data/data", current_dir),
        ]
    )

    for candidate in candidates:
        if candidate.is_dir() and (candidate / "competitions.json").is_file():
            return candidate

    expected = "competitions.json"
    raise DatasetNotFoundError(
        "No se encontró el dataset de StatsBomb. Se esperaba encontrar "
        f"{expected} en una de las rutas candidatas. Configura STATSBOMB_DATA_DIR "
        "con la carpeta que contiene competitions.json o usa --data-dir."
    )


def build_dataset_paths(root: Path) -> DatasetPaths:
    return DatasetPaths(root=root)
