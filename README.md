# ScoutLabs

ScoutLabs es una base profesional para análisis y scouting futbolístico. Esta primera fase se centra en una sola capacidad: inspeccionar un dataset de StatsBomb Open Data sin copiarlo dentro del repositorio, sin añadir backend, frontend, base de datos ni modelos de machine learning.

## Alcance de esta fase

El proyecto incluye una aplicación Python tipada que localiza el dataset de StatsBomb, valida su estructura mínima, lee `competitions.json`, recorre competiciones y temporadas, relaciona cada temporada con sus partidos y genera un inventario legible en JSON, CSV y Markdown.

## Requisitos

- Python 3.11 o superior.
- `pytest` para pruebas.
- `ruff` para linting y formato.
- StatsBomb Open Data disponible como repositorio hermano o mediante `STATSBOMB_DATA_DIR`.

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

ScoutLabs espera por defecto `../open-data/data` y, como respaldo, `../statsbomb-open-data/data`.

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
STATSBOMB_DATA_DIR=../open-data/data
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

Opciones admitidas:

- `--data-dir` tiene prioridad sobre `STATSBOMB_DATA_DIR`.
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

## Qué no incluye todavía

- Frontend.
- Backend Java.
- PostgreSQL.
- FastAPI.
- Spring Boot.
- Next.js.
- Machine learning.
- Docker.
