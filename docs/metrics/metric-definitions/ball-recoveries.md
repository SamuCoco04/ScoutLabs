# Ball recoveries

| Field | Value |
|---|---|
| Metric ID | `MET-DEF-BALL-RECOVERIES` |
| Name | Ball recoveries |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts recorded Ball Recovery events not explicitly marked as failed. It
describes successful provider-recorded recovery activity.

## Intended use

Totals/per 90, recovery maps, transition/sequence research, Player Profile,
Player Explorer, Metric Leaders, Compare, and similarity research.

## Prohibited interpretation

Recoveries are not every regain, complete defensive quality, tackle wins,
counterpress success, causal possession value, or continuous defensive
positioning.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
  `SRC-EVENT-BASE-TEAM-ID`, and `SRC-EVENT-BASE-LOCATION`.
- `SRC-BALL-RECOVERY-FAILURE` —
  `events[].ball_recovery.recovery_failure`.
- `SRC-EVENT-BASE-COUNTERPRESS` — tagged context, not success evidence.
- `SRC-EVENT-POSSESSION` — sequence context.

## Prerequisites

`FEAT-BALL-RECOVERY`; valid Ball Recovery event and actor/team; audited boolean
semantics for `recovery_failure`.

## Formal definition

\[
BR_{p,t,s}=\sum_{e\in \text{BallRecovery}_{p,t,s}}
I(\text{recovery\_failure}(e)\ne\text{true})
\]

This proposal interprets absent or false failure flag on a structurally valid
Ball Recovery as a successful recorded recovery. `EXP-DEF-001` must audit that
convention and compare all recovery events versus successful-only counts.

## Calculation steps

1. Select unique Ball Recovery events with player/team attribution.
2. Validate the nested object and failure flag when present.
3. Exclude explicit `recovery_failure: true` from the successful count while
   retaining it in attempt/coverage reporting.
4. Preserve location, counterpress, possession, and subsequent-retention context
   without changing the base count.
5. Aggregate total and per 90.

## Numerator

Recorded Ball Recovery events without an explicit failure flag.

## Denominator

None for count/per 90. Success rate requires all recovery attempts as a
denominator and is a separate candidate.

## Unit

Successful recorded recoveries; optional per 90.

## Normalization

Expose total and per 90. Possession- or opponent-opportunity adjustment is a
separate `EXP-DEF-001` alternative.

## Comparison group

Position-compatible player–team–season profiles with common competitions,
seasons, minutes rule, taxonomy, and event coverage.

## Sample requirements

No validated threshold. Show minutes and recovery attempts/successes. Test
stability and opportunity denominators under `EXP-DEF-001` and
`EXP-THRESH-001`.

## Edge cases

- Explicit failure is not a successful recovery but remains visible as an
  attempt.
- Missing and false failure values are distinct source states even if this
  candidate groups them after schema validation.
- A recovery followed quickly by a loss still counts as a recovery; retention
  is a separate sequence metric.
- A counterpress flag is context, not recovery-success evidence.
- Interceptions, tackles, goalkeeper claims, and opponent errors are not
  silently converted into Ball Recovery events.

## Missing-data handling

A malformed failure flag is unavailable, excluded from success, and warned.
Missing actor/team excludes player attribution. Missing event coverage is not
zero recovery activity.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, and
`DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-DEF-001`, `EXP-THRESH-001`, and
  `EXP-REDUND-001`.
- Open gates: failure semantics, attempt/success taxonomy, sequence retention,
  overlap with other regains, spatial coverage, and opportunity adjustment.

## Limitations

Provider-recorded recoveries capture selected event activity and are affected by
team possession, role, opposition, and event taxonomy. They do not capture
unrecorded defensive positioning that prevented an action.

## References

- [Research dossier §§11.2–11.4](../../research/research-dossier.md)
- [Experiment registry: EXP-DEF-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-BALL-RECOVERY](../../data/feature-lineage.md)

## Examples

Illustrative only: six valid Ball Recovery events include one explicit
`recovery_failure: true`; the proposed successful count is 5 and attempts are
shown as 6.

## Changelog

- `0.1.0` — Initial successful recorded-recovery proposal.
