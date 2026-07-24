# ScoutLabs

ScoutLabs es una base profesional para análisis y scouting futbolístico. Esta primera fase se centra en una sola capacidad: inspeccionar un dataset de StatsBomb Open Data sin copiarlo dentro del repositorio, sin añadir backend, frontend, base de datos ni modelos de machine learning.

## Alcance de esta fase

El proyecto incluye una aplicación Python tipada que localiza el dataset de StatsBomb, valida su estructura mínima, lee `competitions.json`, recorre competiciones y temporadas, relaciona cada temporada con sus partidos y genera un inventario legible en JSON, CSV y Markdown.

## Requisitos

- Python 3.11 o superior.
- `pytest` para pruebas.
- `ruff` para linting y formato.
- StatsBomb Open Data disponible dentro de `data/statsbomb-open-data/data`, como
  repositorio hermano o mediante `STATSBOMB_DATA_DIR`.

## Estructura

```text
ScoutLabs/
├── .github/workflows/ci.yml
├── docs/data-source.md
├── reports/
├── src/scoutlabs/
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Obtener StatsBomb Open Data

Clona el repositorio oficial como carpeta hermana de ScoutLabs. Un ejemplo en PowerShell:

```powershell
Set-Location ..
git clone https://github.com/statsbomb/open-data.git open-data
Set-Location ScoutLabs
```

En Bash:

```bash
cd ..
git clone https://github.com/statsbomb/open-data.git open-data
cd ScoutLabs
```

ScoutLabs busca por defecto primero `data/statsbomb-open-data/data`; después prueba
`../open-data/data` y `../statsbomb-open-data/data`.

## Entorno virtual

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Bash:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

## Configuración

Copiar `.env.example` a `.env` y ajustar la ruta si hace falta:

```powershell
Copy-Item .env.example .env
```

```bash
cp .env.example .env
```

Contenido esperado:

```ini
STATSBOMB_DATA_DIR=data/statsbomb-open-data/data
```

`.env` está ignorado por Git.

## Ejecutar el inventario

El comando principal es `scoutlabs inventory` y también funciona como `python -m scoutlabs inventory`.

PowerShell:

```powershell
scoutlabs inventory
scoutlabs inventory --data-dir ..\open-data\data --output-dir reports --format all
```

Bash:

```bash
scoutlabs inventory
scoutlabs inventory --data-dir ../open-data/data --output-dir reports --format all
```

La ruta del dataset se resuelve en este orden:

1. El argumento `--data-dir`.
2. La variable de entorno ya definida `STATSBOMB_DATA_DIR`.
3. El valor `STATSBOMB_DATA_DIR` leído de `.env`, sin sobrescribir el entorno.
4. `data/statsbomb-open-data/data`.
5. `../open-data/data`.
6. `../statsbomb-open-data/data`.

Otras opciones admitidas:

- `--output-dir` define dónde escribir los reportes.
- `--format` admite `json`, `csv`, `markdown` y `all`.

## Archivos generados

Por defecto se generan estos archivos dentro de `reports/`:

- `statsbomb_inventory.json`
- `statsbomb_inventory.csv`
- `statsbomb_inventory.md`

## Pruebas y linting

PowerShell:

```powershell
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

Bash:

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Documentation

- [Product brief](BRIEF.md)
- [Data documentation](docs/data/README.md)
- [Research documentation](docs/research/README.md)
- [Reviewed research dossier](docs/research/research-dossier.md)
- [Metrics and model documentation](docs/metrics/README.md)

## Qué no incluye todavía

- Frontend.
- Backend Java.
- PostgreSQL.
- FastAPI.
- Spring Boot.
- Next.js.
- Machine learning.
- Docker.
