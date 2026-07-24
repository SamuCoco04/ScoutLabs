# Metrics and models

This directory is the canonical entry point for ScoutLabs candidate metrics and
analytical model documentation. It records definitions and research decisions;
it does not imply that a metric or model has been implemented, validated, or
admitted to the product.

## Navigate

- [Candidate metric catalogue](metric-catalog.md) — the cross-category registry,
  lineage, denominators, maturity, and planned evidence for every candidate.
- [Metric definitions](metric-definitions/README.md) — detailed, versioned
  specifications for foundational metrics.
- [Model cards](model-cards/README.md) — intended use, risks, inputs, and
  validation gates for proposed or implemented analytical models.
- [Similarity baseline v0 proposal](model-cards/similarity-baseline-v0-proposal.md)
  — an unselected, transparent nearest-neighbour baseline research plan.

Related foundations:

- [Product brief](../../BRIEF.md)
- [Data documentation](../data/README.md)
- [Research documentation](../research/README.md)
- [Reviewed research dossier](../research/research-dossier.md)
- [Experiment registry](../research/metric-experiments.md)
- [Research methodology](../research/research-methodology.md)

## Maturity is not availability

Metric maturity uses only:

`Proposed` → `Researching` → `Experimentally supported` → `Validated` →
`Approved for MVP`

`Rejected` and `Deprecated` are terminal or retirement states. A field being
present in StatsBomb Open Data does not make a metric validated. Conversely, a
metric can have a rigorous definition while remaining `Proposed` because
coverage, edge cases, stability, or football interpretation have not been
validated. Every candidate in this first foundation is `Proposed` or
`Researching`; none is `Approved for MVP`.

Model status is separate: `Proposal`, `Experimental`, `Candidate`, `Production`,
or `Deprecated`.

## Admission process

A metric advances only through the evidence gates defined in the
[research methodology](../research/research-methodology.md):

1. Register a stable `MET-` identifier, football question, source lineage,
   definition, unit, denominator, intended use, and prohibited interpretation.
2. Measure source and conditional-field coverage; satisfy applicable `DQ-`
   rules.
3. Implement reproducibly with tests for formula and edge cases.
4. Complete its linked `EXP-` experiments, including competing definitions,
   samples, stability, redundancy, and expert review where required.
5. Record completed evidence under a `VAL-` identifier.
6. Obtain explicit review before `Approved for MVP`.

Historical values must retain metric version, source snapshot, analytical unit,
comparison group, normalization, and model version where applicable. A
definition change that changes values requires a new version; it must not
silently rewrite prior results.

## Interpretation rules

- The default profile unit is player–team–season; combined multi-team views must
  preserve their components.
- Totals, denominators, and sample warnings accompany normalized values.
- Per-90 rates describe exposure; they are not reliability adjustments.
- Percentiles name their exact comparison population.
- Provider-supplied values, direct aggregations, ScoutLabs derivations, and model
  outputs remain distinguishable.
- Event maps describe recorded activity, not continuous tracking.
- Similarity means statistical proximity under a stated configuration. It is not
  quality, suitability, affordability, or transfer advice.

