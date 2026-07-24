# [Model name]

| Field | Value |
|---|---|
| Model ID | `MOD-...` |
| Name | [Name] |
| Version | `0.1.0` |
| Status | Proposal |
| Owner | ScoutLabs research |

## Intended use

Define the supported decision and product surface.

## Prohibited use

Define conclusions the output cannot support.

## Analytical unit

Define the input and output unit, including team and season treatment.

## Candidate population

Specify eligibility, position compatibility, competitions, seasons, and sample
rules.

## Input features

List exact `FEAT-` and `MET-` IDs with versions and feature-family grouping.

## Preprocessing

Document transformations, scaling fit population, outlier treatment,
normalization, and leakage controls.

## Missing-data policy

Define exclusions, pairwise behavior, imputation, coverage thresholds, and
coverage penalties. Missing values must not silently become zero.

## Weighting

Define defaults, user controls, constraints, normalization, and provenance.

## Algorithm

Give reproducible pseudocode or formula and all hyperparameters.

## Output

Define score/rank semantics, distance-to-similarity conversion, tie handling,
and retained provenance.

## Explanation

Define global, family, and feature-level explanations and visible warnings.

## Validation

List completed `VAL-` records and required mechanical, stability, expert,
negative-control, and product gates.

## Sensitivity

Test samples, scaling, thresholds, features, weights, missingness, comparison
groups, and random components where applicable.

## Limitations

State data, context, causality, fairness, and generalization boundaries.

## Decision risks

Describe harmful or misleading decisions and mitigations.

## Reproducibility

Record source snapshot, code revision, configuration, random seed, dependencies,
and artifact retention.

## Dependencies

List source fields, `DQ-` rules, metric versions, and software/runtime needs.

## Related experiments

List `EXP-` identifiers and statuses.

## Changelog

- `0.1.0` — Initial proposal.

