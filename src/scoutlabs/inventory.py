from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from .config import DatasetPaths


@dataclass(slots=True, frozen=True)
class InventoryRow:
    competition_id: int
    season_id: int
    country_name: str
    competition_name: str
    competition_gender: str
    season_name: str
    match_count: int
    first_match_date: str | None
    last_match_date: str | None
    team_count: int
    player_count: int
    event_file_count: int
    lineup_file_count: int
    three_sixty_file_count: int
    event_coverage: float
    lineup_coverage: float
    three_sixty_coverage: float


@dataclass(slots=True, frozen=True)
class InventoryResult:
    dataset_root: str
    generated_at: str
    summary: dict[str, Any]
    rows: list[InventoryRow]
    warnings: list[str]


def _read_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def _coerce_int(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    return None


def _coerce_str(value: Any) -> str:
    return value if isinstance(value, str) else ""


def _match_file(path: Path, match_id: int) -> Path:
    return path / f"{match_id}.json"


def _parse_match_date(value: Any, warnings: list[str], context: str) -> date | None:
    if not isinstance(value, str):
        warnings.append(f"{context}: fecha de partido ausente o inválida.")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        warnings.append(f"{context}: no se pudo interpretar la fecha {value!r}.")
        return None


def _extract_unique_team_ids(match: dict[str, Any]) -> set[int]:
    team_ids: set[int] = set()
    home_team = match.get("home_team")
    if isinstance(home_team, dict):
        team_id = _coerce_int(home_team.get("home_team_id"))
        if team_id is not None:
            team_ids.add(team_id)
    away_team = match.get("away_team")
    if isinstance(away_team, dict):
        team_id = _coerce_int(away_team.get("away_team_id"))
        if team_id is not None:
            team_ids.add(team_id)
    return team_ids


def _extract_players_and_teams_from_lineups(path: Path) -> tuple[set[int], set[int], bool]:
    if not path.is_file():
        return set(), set(), False

    try:
        payload = _read_json_file(path)
    except json.JSONDecodeError:
        return set(), set(), False

    player_ids: set[int] = set()
    team_ids: set[int] = set()

    if isinstance(payload, list):
        for team_entry in payload:
            if not isinstance(team_entry, dict):
                continue
            team_id = _coerce_int(team_entry.get("team_id"))
            if team_id is not None:
                team_ids.add(team_id)
            lineup = team_entry.get("lineup")
            if not isinstance(lineup, list):
                continue
            for player_entry in lineup:
                if not isinstance(player_entry, dict):
                    continue
                player_id = _coerce_int(player_entry.get("player_id"))
                if player_id is not None:
                    player_ids.add(player_id)
    return player_ids, team_ids, True


def load_competitions(dataset_paths: DatasetPaths) -> list[dict[str, Any]]:
    payload = _read_json_file(dataset_paths.competitions_file)
    if not isinstance(payload, list):
        raise ValueError("competitions.json debe contener una lista JSON")
    competitions: list[dict[str, Any]] = []
    for item in payload:
        if isinstance(item, dict):
            competitions.append(item)
    return competitions


def build_inventory(dataset_paths: DatasetPaths) -> InventoryResult:
    competitions = load_competitions(dataset_paths)
    rows: list[InventoryRow] = []
    warnings: list[str] = []
    global_players: set[int] = set()
    global_team_ids: set[int] = set()
    global_competition_ids: set[int] = set()
    global_match_count = 0
    global_events = 0
    global_lineups = 0
    global_three_sixty = 0

    sorted_competitions = sorted(
        competitions,
        key=lambda item: (
            _coerce_str(item.get("competition_name")),
            _coerce_str(item.get("season_name")),
            _coerce_int(item.get("competition_id")) or -1,
            _coerce_int(item.get("season_id")) or -1,
        ),
    )

    for competition in sorted_competitions:
        competition_id = _coerce_int(competition.get("competition_id"))
        season_id = _coerce_int(competition.get("season_id"))
        if competition_id is None or season_id is None:
            warnings.append("Se omitió una competición/temporada con identificadores inválidos.")
            continue

        global_competition_ids.add(competition_id)

        competition_name = _coerce_str(competition.get("competition_name"))
        season_name = _coerce_str(competition.get("season_name"))
        country_name = _coerce_str(competition.get("country_name"))
        competition_gender = _coerce_str(competition.get("competition_gender"))

        match_file = dataset_paths.matches_dir / str(competition_id) / f"{season_id}.json"
        matches: list[dict[str, Any]] = []
        if match_file.is_file():
            try:
                match_payload = _read_json_file(match_file)
                if isinstance(match_payload, list):
                    matches = [item for item in match_payload if isinstance(item, dict)]
                else:
                    warnings.append(f"{match_file}: se esperaba una lista de partidos.")
            except json.JSONDecodeError:
                warnings.append(f"{match_file}: no se pudo leer el JSON de partidos.")
        else:
            warnings.append(f"Falta el archivo de partidos esperado: {match_file}.")

        match_dates: list[date] = []
        team_ids: set[int] = set()
        competition_player_ids: set[int] = set()
        event_file_count = 0
        lineup_file_count = 0
        three_sixty_file_count = 0

        for match in matches:
            match_id = _coerce_int(match.get("match_id"))
            if match_id is None:
                warnings.append(
                    f"{match_file}: se omitió un partido sin match_id en "
                    f"{competition_name} / {season_name}."
                )
                continue

            global_match_count += 1

            match_date = _parse_match_date(
                match.get("match_date"), warnings, f"match_id={match_id}"
            )
            if match_date is not None:
                match_dates.append(match_date)

            team_ids.update(_extract_unique_team_ids(match))

            event_path = _match_file(dataset_paths.events_dir, match_id)
            lineup_path = _match_file(dataset_paths.lineups_dir, match_id)
            three_sixty_path = _match_file(dataset_paths.three_sixty_dir, match_id)

            if event_path.is_file():
                event_file_count += 1
                global_events += 1
            else:
                warnings.append(f"Falta el archivo esperado de eventos: {event_path}.")

            if lineup_path.is_file():
                lineup_file_count += 1
                global_lineups += 1
                players, lineup_team_ids, valid = _extract_players_and_teams_from_lineups(
                    lineup_path
                )
                if not valid:
                    warnings.append(f"{lineup_path}: no se pudo procesar la alineación.")
                competition_player_ids.update(players)
                global_players.update(players)
                team_ids.update(lineup_team_ids)
                global_team_ids.update(lineup_team_ids)
            else:
                warnings.append(f"Falta el archivo esperado de alineaciones: {lineup_path}.")

            if three_sixty_path.is_file():
                three_sixty_file_count += 1
                global_three_sixty += 1
            elif three_sixty_path.exists():
                warnings.append(
                    f"{three_sixty_path}: el archivo 360 existe pero no se pudo contabilizar."
                )

        first_match_date = min(match_dates).isoformat() if match_dates else None
        last_match_date = max(match_dates).isoformat() if match_dates else None
        match_count = len(matches)

        rows.append(
            InventoryRow(
                competition_id=competition_id,
                season_id=season_id,
                country_name=country_name,
                competition_name=competition_name,
                competition_gender=competition_gender,
                season_name=season_name,
                match_count=match_count,
                first_match_date=first_match_date,
                last_match_date=last_match_date,
                team_count=len(team_ids),
                player_count=len(competition_player_ids),
                event_file_count=event_file_count,
                lineup_file_count=lineup_file_count,
                three_sixty_file_count=three_sixty_file_count,
                event_coverage=(event_file_count / match_count) if match_count else 0.0,
                lineup_coverage=(lineup_file_count / match_count) if match_count else 0.0,
                three_sixty_coverage=(three_sixty_file_count / match_count) if match_count else 0.0,
            )
        )

    rows.sort(
        key=lambda row: (
            row.competition_name,
            row.season_name,
            row.competition_id,
            row.season_id,
        )
    )

    summary = {
        "competition_count": len(global_competition_ids),
        "season_count": len(rows),
        "match_count": global_match_count,
        "approx_unique_player_count": len(global_players),
        "event_file_count": global_events,
        "lineup_file_count": global_lineups,
        "three_sixty_file_count": global_three_sixty,
        "team_count": len(global_team_ids),
    }

    return InventoryResult(
        dataset_root=str(dataset_paths.root),
        generated_at=datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        summary=summary,
        rows=rows,
        warnings=warnings,
    )


def _result_to_dict(result: InventoryResult) -> dict[str, Any]:
    return {
        "dataset_root": result.dataset_root,
        "generated_at": result.generated_at,
        "summary": result.summary,
        "rows": [asdict(row) for row in result.rows],
        "warnings": result.warnings,
    }


def write_inventory_reports(
    result: InventoryResult, output_dir: Path, output_format: str
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written_files: list[Path] = []

    if output_format in {"json", "all"}:
        json_path = output_dir / "statsbomb_inventory.json"
        with json_path.open("w", encoding="utf-8") as file_handle:
            json.dump(_result_to_dict(result), file_handle, ensure_ascii=False, indent=2)
            file_handle.write("\n")
        written_files.append(json_path)

    if output_format in {"csv", "all"}:
        csv_path = output_dir / "statsbomb_inventory.csv"
        fieldnames = (
            list(asdict(result.rows[0]).keys())
            if result.rows
            else [
                "competition_id",
                "season_id",
                "country_name",
                "competition_name",
                "competition_gender",
                "season_name",
                "match_count",
                "first_match_date",
                "last_match_date",
                "team_count",
                "player_count",
                "event_file_count",
                "lineup_file_count",
                "three_sixty_file_count",
                "event_coverage",
                "lineup_coverage",
                "three_sixty_coverage",
            ]
        )
        with csv_path.open("w", encoding="utf-8", newline="") as file_handle:
            writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in result.rows:
                writer.writerow(asdict(row))
        written_files.append(csv_path)

    if output_format in {"markdown", "all"}:
        md_path = output_dir / "statsbomb_inventory.md"
        md_path.write_text(render_markdown(result), encoding="utf-8")
        written_files.append(md_path)

    return written_files


def render_markdown(result: InventoryResult) -> str:
    lines: list[str] = []
    lines.append("# StatsBomb Inventory")
    lines.append("")
    lines.append("## Resumen global")
    lines.append("")
    lines.append(f"- Competiciones y temporadas: {result.summary['competition_count']}")
    lines.append(f"- Temporadas: {result.summary['season_count']}")
    lines.append(f"- Partidos: {result.summary['match_count']}")
    lines.append(f"- Jugadores únicos aproximados: {result.summary['approx_unique_player_count']}")
    lines.append(f"- Archivos de eventos: {result.summary['event_file_count']}")
    lines.append(f"- Archivos de alineaciones: {result.summary['lineup_file_count']}")
    lines.append(f"- Archivos 360: {result.summary['three_sixty_file_count']}")
    lines.append("")
    lines.append("## Tabla de competiciones y temporadas")
    lines.append("")
    lines.append(
        "| competition_id | season_id | country_name | competition_name | "
        "competition_gender | season_name | match_count | first_match_date | "
        "last_match_date | team_count | player_count | events | lineups | three_sixty |"
    )
    lines.append(
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | ---: | ---: | ---: |"
        " ---: | ---: |"
    )
    for row in result.rows:
        lines.append(
            f"| {row.competition_id} | {row.season_id} | {row.country_name or ''} | "
            f"{row.competition_name or ''} | {row.competition_gender or ''} | "
            f"{row.season_name or ''} | {row.match_count} | {row.first_match_date or ''} | "
            f"{row.last_match_date or ''} | {row.team_count} | {row.player_count} | "
            f"{row.event_file_count} | {row.lineup_file_count} | {row.three_sixty_file_count} |"
        )
    lines.append("")
    lines.append("## Cobertura")
    lines.append("")
    lines.append(
        f"- Eventos: {result.summary['event_file_count']} archivos para "
        f"{result.summary['match_count']} partidos."
    )
    lines.append(
        f"- Alineaciones: {result.summary['lineup_file_count']} archivos para "
        f"{result.summary['match_count']} partidos."
    )
    lines.append(
        f"- Datos 360: {result.summary['three_sixty_file_count']} archivos para "
        f"{result.summary['match_count']} partidos."
    )
    lines.append("")
    lines.append("## Advertencias")
    lines.append("")
    if result.warnings:
        for warning in result.warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- No se detectaron advertencias.")
    lines.append("")
    return "\n".join(lines)


def inventory_from_paths(paths: DatasetPaths) -> InventoryResult:
    return build_inventory(paths)
