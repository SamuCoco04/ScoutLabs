from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from .config import DatasetNotFoundError, build_dataset_paths, resolve_data_dir
from .inventory import inventory_from_paths, write_inventory_reports

VALID_FORMATS = {"json", "csv", "markdown", "all"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="scoutlabs", description="ScoutLabs tooling")
    subparsers = parser.add_subparsers(dest="command")

    inventory_parser = subparsers.add_parser(
        "inventory",
        help="Inspect StatsBomb Open Data and generate an inventory report",
    )
    inventory_parser.add_argument("--data-dir", type=Path, help="Path to StatsBomb data root")
    inventory_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("reports"),
        help="Directory where generated reports are written",
    )
    inventory_parser.add_argument(
        "--format",
        choices=sorted(VALID_FORMATS),
        default="all",
        help="Output format to generate",
    )
    inventory_parser.set_defaults(handler=run_inventory)
    return parser


def run_inventory(args: argparse.Namespace) -> int:
    try:
        data_dir = resolve_data_dir(args.data_dir)
    except DatasetNotFoundError as exc:
        print(str(exc))
        return 2

    paths = build_dataset_paths(data_dir)
    result = inventory_from_paths(paths)
    written_files = write_inventory_reports(result, args.output_dir, args.format)

    for path in written_files:
        print(path)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    if not hasattr(args, "handler"):
        parser.print_help()
        return 1
    return args.handler(args)
