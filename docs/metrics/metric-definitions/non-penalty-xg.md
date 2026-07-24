# Non-penalty xG

| Field | Value |
|---|---|
| Metric ID | `MET-SHOOT-NON-PENALTY-XG` |
| Name | Non-penalty xG |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Sums provider-supplied StatsBomb pre-shot expected goals for a player’s
non-penalty, non-shootout shots. It describes the aggregate chance quality and
volume of the shots taken.

## Intended use

Goal-threat totals/per 90, shot-profile context, Player Profile, Player
Explorer, Metric Leaders, Compare, and similarity research.

## Prohibited interpretation

This is not a ScoutLabs-trained xG model, post-shot xG, finishing, goals
prevented, causal player quality, or a competition-strength adjustment.

## Source fields

All fields from [non-penalty shots](non-penalty-shots.md), plus
`SRC-SHOT-XG` — `events[].shot.statsbomb_xg`, provider-supplied pre-shot xG.

## Prerequisites

`FEAT-NON-PENALTY-SHOT`, `FEAT-SHOT-XG`, `FEAT-NON-PENALTY-XG`;
eligible Shot taxonomy and finite numeric xG within its documented domain.

## Formal definition

\[
npxG_{p,t,s}=\sum_{e\in NPS_{p,t,s}}
\text{statsbomb\_xg}(e)
\]

The eligible set is exactly `MET-SHOOT-NON-PENALTY-SHOTS`. The sum is a direct
aggregation
of a provider value; provider metadata/version must remain traceable.

## Calculation steps

1. Build the eligible non-penalty-shot set.
2. Validate `shot.statsbomb_xg` type, finiteness, and range.
3. Sum without per-shot rounding.
4. retain raw xG sum, eligible shot count, xG-covered shot count, provider
   metadata, and minutes.
5. Divide only after aggregation for per-90 or average-per-shot variants.

## Numerator

Sum of StatsBomb xG over eligible non-penalty shots.

## Denominator

None for total/per 90. Average npxG per shot uses
`MET-SHOOT-NON-PENALTY-SHOTS` and is a separate rate.

## Unit

Expected goals; optional expected goals per 90.

## Normalization

Expose total and per 90 from validated seconds. Preserve the provider version.
Percentiles require a named comparison population and common metric version.

## Comparison group

Position-compatible player–team–season profiles with the same source/provider
version treatment, competition/season scope, minutes rule, and xG coverage.

## Sample requirements

No validated minimum. Always show minutes and shot count. `EXP-THRESH-001` and
`EXP-SHRINK-001` test sample and stability policy.

## Edge cases

- Missing or invalid xG excludes the shot from the sum but not from
  non-penalty-shot coverage reporting.
- Regulation/extra-time penalties and all shootout kicks are excluded.
- A goal does not alter its pre-shot xG contribution.
- Sum team components before calculating a combined per-90 rate.
- Provider xG versions must not be silently pooled if their semantics differ.
- Never round individual xG values before summation.

## Missing-data handling

Report eligible shots, xG-covered shots, and coverage. A profile below a future
coverage gate is unavailable for comparison. Missing xG is not zero.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-SHOOTOUT`,
`DQ-PROVIDER-VERSION`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-THRESH-001`, `EXP-SHRINK-001`, and
  `EXP-REDUND-001`.
- Open gates: field coverage, value domain, provider version differences,
  exclusion fixtures, aggregation invariants, and stability.

## Limitations

The metric inherits the provider model, training data, and calibration. It is
strongly opportunity- and team-dependent and does not separate chance getting
from chance selection.

## References

- [Research dossier §§9.1–9.3 and R2](../../research/research-dossier.md)
- [Non-penalty-shots definition](non-penalty-shots.md)
- [Feature lineage: FEAT-NON-PENALTY-XG](../../data/feature-lineage.md)

## Examples

Illustrative only: eligible shots with xG 0.04, 0.12, and 0.30 yield 0.46 npxG.
A separate penalty with xG 0.76 contributes zero to this metric.

## Changelog

- `0.1.0` — Initial provider-xG aggregation proposal.
