# Completed passes

| Field | Value |
|---|---|
| Metric ID | `MET-PASS-COMPLETED` |
| Name | Completed passes |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts eligible recorded pass attempts that the StatsBomb outcome model does not
mark as unsuccessful. It describes successful distribution volume, not pass
difficulty or value.

## Intended use

Totals, per-90 rates, passing-volume context, Player Profile, Player Explorer,
Metric Leaders, Compare, and candidate similarity after redundancy review.

## Prohibited interpretation

More completed passes do not by themselves mean better passing, greater
progression, safer decisions, or independence from team possession and role.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID` — `events[].type.id`, selecting Pass.
- `SRC-EVENT-BASE-PLAYER-ID` and `SRC-EVENT-BASE-TEAM-ID` —
  `events[].player.id` and `events[].team.id`.
- `SRC-PASS-OUTCOME-ID` — `events[].pass.outcome.id`; absence commonly encodes
  completion in the StatsBomb event model.
- `SRC-PASS-TYPE-ID` — `events[].pass.type.id`, retained for special-type
  alternatives and splits.

## Prerequisites

`FEAT-PASS-ATTEMPT`, `FEAT-PASS-COMPLETED`, a valid Pass object and actor, an
audited pass-outcome vocabulary, and `FEAT-MINUTES` for per-90 output.

## Formal definition

For eligible pass attempts \(P_{p,t,s}^{(v)}\):

\[
C_{p,t,s}^{(v)}=\sum_{e\in P_{p,t,s}^{(v)}}
I(\text{outcome}(e)\text{ is absent})
\]

Version \(v\) owns the eligibility treatment of special pass types and any
provider outcome whose meaning is `Unknown` or non-football administration.
The initial candidate treats a structurally valid missing outcome as completed;
it does not treat a missing or malformed Pass object as completion.

## Calculation steps

1. Select player-attributed Pass events with a valid nested Pass object.
2. Apply the versioned eligibility taxonomy; retain pass-type splits.
3. Validate the outcome ID against the audited provider vocabulary.
4. Mark a structurally valid attempt complete only when `pass.outcome` is
   absent.
5. Aggregate count and retain attempts and minutes beside normalized output.

## Numerator

Eligible pass attempts marked completed.

## Denominator

None for the count. `MET-PASS-COMPLETION-RATE` uses eligible attempts as its
denominator.

## Unit

Completed passes.

## Normalization

Expose total and \(C \times 5{,}400 / \text{validated player seconds}\) per 90.
Per-90 is unavailable when minutes are unavailable or zero. Team-possession
adjustment is not part of this version.

## Comparison group

Position-compatible player–team–season profiles with the same competitions,
seasons, minute rule, pass eligibility version, and source coverage.

## Sample requirements

No validated universal minimum. Show attempts and minutes. Candidate eligibility
is tested in `EXP-THRESH-001`; low pass volume remains visible.

## Edge cases

- An absent outcome within a valid Pass object is different from an absent Pass
  object.
- Incomplete, Out, Pass Offside, Injury Clearance, and Unknown meanings must be
  audited; no unknown ID is silently treated as success.
- Throw-ins, kickoffs, corners, free kicks, and goal kicks may be included in
  the base total or exposed as splits; exclusion alternatives are compared in
  `EXP-PASS-001`.
- A pass followed by a teammate touch is not reconstructed as complete when the
  provider explicitly supplies a failure outcome.
- Duplicate events are not separate passes.

## Missing-data handling

Exclude malformed or unknown-outcome records from both completed and eligible
attempt counts until classified, warn, and expose the excluded count. Do not
convert missing event files or missing actors into zero production.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, and
`DQ-INCOMPLETE-VIDEO` for per-90 output.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiment: `EXP-PASS-001`.
- Open gates: observed outcome vocabulary, special-type denominator, malformed
  objects, independent event fixtures, and count reconciliation.

## Limitations

Outcome absence is a provider-schema convention, not a direct observation of the
next touch. Volume is heavily influenced by possession and tactical role.

## References

- [Research dossier §§7.1 and 24; R2 and R9](../../research/research-dossier.md)
- [Experiment registry: EXP-PASS-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-PASS-COMPLETED](../../data/feature-lineage.md)

## Examples

Illustrative only: from 12 eligible Pass events, 9 have no outcome, 2 are
Incomplete, and 1 has an unclassified outcome. Completed passes = 9; the
unclassified event is excluded and warned, not treated as either result.

## Changelog

- `0.1.0` — Initial proposed StatsBomb-outcome definition.
