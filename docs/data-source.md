# StatsBomb Open Data

StatsBomb Open Data es una fuente externa y no forma parte del código de ScoutLabs. Los archivos del dataset no pertenecen a este repositorio y no deben copiarse, moverlos ni reescribirlos dentro de ScoutLabs.

## Estructura básica

El inventario de ScoutLabs asume la estructura habitual del dataset:

```text
data/
├── competitions.json
├── matches/<competition_id>/<season_id>.json
├── lineups/<match_id>.json
├── events/<match_id>.json
└── three-sixty/<match_id>.json
```

El archivo usado para validar la raíz del dataset es `competitions.json`.

## Atribución y uso

ScoutLabs debe atribuir correctamente a StatsBomb cuando muestre o derive información procedente del dataset. Antes de redistribuir datos o resultados derivados, revisa siempre las condiciones de uso y licencia publicadas por StatsBomb.

## Limitaciones

La cobertura del dataset puede ser parcial. No todos los partidos incluyen eventos, alineaciones o datos 360, y algunos archivos pueden estar ausentes o contener campos incompletos. ScoutLabs está diseñado para tolerar esas ausencias sin detener el análisis completo.
