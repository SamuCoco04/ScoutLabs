# Progressive carries

| Field | Value |
|---|---|
| Metric ID | `MET-PROG-CARRIES` |
| Name | Progressive carries |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts recorded carries that move the ball materially closer to the opponent’s
goal under a named rule. Carries represent general movement with the ball and
must not be conflated with attempts to beat an opponent (Dribbles).

## Intended use

Progression totals/per 90, carry maps, Player Profile, Player Explorer, Metric
Leaders, Compare, and similarity research.

## Prohibited interpretation

This is not a native provider flag, dribble success, running ability, line
breaking, xT, or complete off-ball movement.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, and
  `SRC-EVENT-BASE-TEAM-ID`.
- `SRC-EVENT-BASE-LOCATION` — `events[].location`.
- `SRC-CARRY-END-LOCATION` — `events[].carry.end_location`.

## Prerequisites

`FEAT-CARRY-X-PROGRESSION`, `FEAT-PROGRESSIVE-CARRY`; valid Carry object and
actor; valid start/end coordinates; attacking-direction normalization;
versioned pitch geometry.

## Formal definition

Using the goal-distance change \(\Delta_g\) and versioned threshold \(T_v\)
defined in [progressive passes](progressive-passes.md):

\[
PC_{p,t,s}^{(v)}=\sum_{e\in \text{Carry}_{p,t,s}}
I(\Delta_g(e)\ge T_v(s_e,z_e))
\]

`EXP-PROG-001` compares context-dependent 30/15/10-metre goal-distance
reduction, fixed x-gain, tactical-zone advance, and xT-gain alternatives. No
default is selected here; a pass and carry may share a principle only if their
opportunity and stability tests support it.

## Calculation steps

1. Select valid Carry events attributed to the player.
2. Validate and normalize start/end coordinates.
3. Calculate goal-distance, x-gain, zone transition, and experimental xT
   components without conflating them.
4. Apply one named rule version.
5. Aggregate total and per 90 while retaining carry volume and spatial coverage.

## Numerator

Carries satisfying the selected progression rule.

## Denominator

None for count/per 90. A progressive-carry share would use eligible carries and
requires its own catalogue entry/version.

## Unit

Progressive carries; optional per 90.

## Normalization

Expose total and per 90 using validated seconds. Comparison normalization
requires a common rule, source coverage, population, and minimum minutes.

## Comparison group

Position-compatible player–team–season profiles. Goalkeepers and outfield
players should not share default progression comparisons.

## Sample requirements

No validated universal threshold. Display minutes, all carries, and progressive
carries. Test sample stability through `EXP-PROG-001` and `EXP-THRESH-001`.

## Edge cases

- Zero-length and backwards carries do not qualify.
- Carry chains split by provider events are counted as recorded, not silently
  merged.
- Carries crossing a boundary exactly follow the zone version’s boundary rule.
- A carry followed by a loss remains progressive geometrically; retention or
  value is a separate metric.
- Dribble events are not carries unless the provider also supplies a distinct
  carry record.
- Physical-metre thresholds require an explicit coordinate conversion.

## Missing-data handling

Exclude invalid/missing start/end records and report spatial eligibility. Do not
infer a carry from consecutive touches or impute coordinates.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`,
`DQ-COORD-RANGE`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-PROG-001`, `EXP-REDUND-001`, and
  `EXP-THRESH-001`.
- Open gates: threshold selection, coordinate conversion, carry segmentation,
  stability, retention interaction, and football review.

## Limitations

Carries are provider-recorded actions, not continuous trajectories. The metric
does not observe speed, pressure throughout the carry, opponents bypassed, or
whether the subsequent possession retained value.

## References

- [Research dossier §§8.1 and 24](../../research/research-dossier.md)
- [Experiment registry: EXP-PROG-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-CARRY-X-PROGRESSION and FEAT-PROGRESSIVE-CARRY](../../data/feature-lineage.md)

## Examples

Illustrative only: a carry from one tactical zone into a more advanced zone may
qualify under the zone rule while failing a fixed-distance rule. Its rule
version must be visible.

## Changelog

- `0.1.0` — Competing carry-progression definitions registered; no default
  selected.
