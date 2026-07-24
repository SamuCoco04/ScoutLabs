# [Metric name]

| Field | Value |
|---|---|
| Metric ID | `MET-...` |
| Name | [Metric name] |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

State the football question and what a higher or lower value can responsibly
mean.

## Intended use

Name the eligible analytical unit, comparison group, and product surfaces.

## Prohibited interpretation

State claims that this metric cannot support.

## Source fields

List canonical `SRC-` IDs and exact JSON paths. Mark provider-supplied inputs
and ScoutLabs-derived values separately.

## Prerequisites

List normalized entities, `FEAT-` dependencies, direction normalization, joins,
and eligibility rules.

## Formal definition

Define the metric using mathematical notation or unambiguous pseudocode. Specify
the analytical unit and time/sample window.

## Calculation steps

1. Define eligible source records.
2. Apply exclusions and quality gates.
3. Calculate the numerator.
4. Calculate the denominator.
5. Apply normalization without hiding raw components.

## Numerator

Define the numerator and its unit.

## Denominator

Define the denominator. Use `None (count)` for totals. Never use zero when the
denominator is unavailable.

## Unit

Count, seconds, minutes, percentage, expected goals, per 90, or another explicit
unit.

## Normalization

Describe totals, per-90, rates, and comparison-population transforms separately.

## Comparison group

Specify position, competitions, seasons, sample threshold, and other filters
that must accompany percentiles or standardized values.

## Sample requirements

Name minimum minutes or action opportunities as a pending experiment when no
threshold has been validated.

## Edge cases

- List extra time, shootouts, special outcomes, missing links, or taxonomy
  ambiguity as applicable.
- Document competing treatments rather than silently selecting one.

## Missing-data handling

State when to return unavailable, exclude a record, or issue a warning. Missing
must never become zero without evidence.

## Quality dependencies

List applicable `DQ-` identifiers and their effect.

## Validation

- Completed `VAL-` evidence: None unless a validation is actually recorded.
- Planned experiment: `EXP-...`.
- Admission gates still open: coverage, formula, stability, expert review, or
  other named gates.

## Limitations

Distinguish activity from quality, context from ability, and event data from
tracking.

## References

Link to the reviewed research dossier, official specifications, recommendations,
and experiment registry. Do not duplicate the full literature review.

## Examples

Use synthetic arithmetic only, explicitly labeled illustrative. Do not invent
local coverage or player results.

## Changelog

- `0.1.0` — Initial proposed definition.
