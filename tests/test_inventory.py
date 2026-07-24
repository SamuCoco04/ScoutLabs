from __future__ import annotations

import json
import shutil
from pathlib import Path

from scoutlabs.config import DatasetPaths
from scoutlabs.inventory import (
    build_inventory,
    render_markdown,
    write_inventory_reports,
)

FIXTURES = Path(__file__).parent / "fixtures"


def _dataset_paths() -> DatasetPaths:
    return DatasetPaths(root=FIXTURES)


def test_build_inventory_aggregates_matches_players_and_teams() -> None:
    result = build_inventory(_dataset_paths())

    assert len(result.rows) == 2
    first_row = result.rows[0]
    assert first_row.competition_name == "Alpha League"
    assert first_row.match_count == 2
    assert first_row.team_count == 3
    assert first_row.player_count == 5
    assert first_row.event_file_count == 1
    assert first_row.lineup_file_count == 2
    assert first_row.three_sixty_file_count == 1


def test_build_inventory_deduplicates_players_and_handles_missing_files() -> None:
    result = build_inventory(_dataset_paths())

    warnings = "\n".join(result.warnings)
    assert "Falta el archivo esperado de eventos" in warnings
    assert "Falta el archivo esperado de alineaciones" in warnings
    assert result.summary["approx_unique_player_count"] == 5


def test_global_teams_include_match_without_lineup_file() -> None:
    result = build_inventory(_dataset_paths())

    beta_row = next(row for row in result.rows if row.competition_name == "Beta Cup")
    assert beta_row.match_count == 1
    assert beta_row.lineup_file_count == 0
    assert beta_row.team_count == 2
    assert result.summary["team_count"] == 5


def test_invalid_match_id_is_excluded_from_all_counts_and_coverage(tmp_path: Path) -> None:
    dataset_root = tmp_path / "dataset"
    shutil.copytree(FIXTURES, dataset_root)
    match_file = dataset_root / "matches" / "1" / "10.json"
    matches = json.loads(match_file.read_text(encoding="utf-8"))
    matches.append(
        {
            "match_id": "not-an-integer",
            "match_date": "2024-01-15",
            "home_team": {"home_team_id": 66},
            "away_team": {"away_team_id": 77},
        }
    )
    match_file.write_text(json.dumps(matches), encoding="utf-8")

    result = build_inventory(DatasetPaths(root=dataset_root))
    alpha_row = next(row for row in result.rows if row.competition_name == "Alpha League")

    assert alpha_row.match_count == 2
    assert alpha_row.event_file_count == 1
    assert alpha_row.lineup_file_count == 2
    assert alpha_row.three_sixty_file_count == 1
    assert alpha_row.event_coverage == 0.5
    assert alpha_row.lineup_coverage == 1.0
    assert alpha_row.three_sixty_coverage == 0.5
    assert result.summary["match_count"] == sum(row.match_count for row in result.rows) == 3
    assert result.summary["event_file_count"] == 1
    assert result.summary["lineup_file_count"] == 2
    assert result.summary["three_sixty_file_count"] == 1
    assert any("sin match_id entero" in warning for warning in result.warnings)


def test_generated_at_is_iso_8601_utc() -> None:
    result = build_inventory(_dataset_paths())

    assert result.generated_at.endswith("Z")


def test_render_markdown_contains_required_sections() -> None:
    result = build_inventory(_dataset_paths())
    markdown = render_markdown(result)

    assert "Resumen global" in markdown
    assert "Cobertura" in markdown
    assert "Advertencias" in markdown


def test_write_inventory_reports_generates_all_formats(tmp_path: Path) -> None:
    result = build_inventory(_dataset_paths())
    written_files = write_inventory_reports(result, tmp_path, "all")

    expected_names = {
        "statsbomb_inventory.json",
        "statsbomb_inventory.csv",
        "statsbomb_inventory.md",
    }
    assert {path.name for path in written_files} == expected_names

    json_payload = json.loads((tmp_path / "statsbomb_inventory.json").read_text(encoding="utf-8"))
    assert json_payload["summary"]["match_count"] == 3

    csv_text = (tmp_path / "statsbomb_inventory.csv").read_text(encoding="utf-8")
    assert "competition_id,season_id" in csv_text

    md_text = (tmp_path / "statsbomb_inventory.md").read_text(encoding="utf-8")
    assert "# StatsBomb Inventory" in md_text
