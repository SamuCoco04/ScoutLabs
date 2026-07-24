from __future__ import annotations

import json
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
