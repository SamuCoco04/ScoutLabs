# Pressures

| Field | Value |
|---|---|
| Metric ID | `MET-PRESS-PRESSURES` |
| Name | Pressures |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts player-attributed StatsBomb Pressure events. It describes recorded
pressure activity, not the complete intensity or effectiveness of a pressing
system.

## Intended use

Totals/per 90, pressure action maps, Player Profile, Player Explorer, Metric
Leaders, Compare, and similarity research with explicit event-proxy language.

## Prohibited interpretation

The metric is not continuous pressing intensity, closing speed, team shape,
pressure success, all defensive work, or equivalent to tracking-derived
pressure. The `under_pressure` flag on an opponent action is not another
Pressure event.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, and
  `SRC-EVENT-BASE-TEAM-ID`.
- `SRC-EVENT-BASE-LOCATION` — pressure start location.
- `SRC-EVENT-BASE-DURATION` — provider event duration, retained as context.
- `SRC-EVENT-BASE-UNDER-PRESSURE` — related on-ball context, not counted as the
  pressure itself.
- `SRC-EVENT-BASE-COUNTERPRESS` — `events[].counterpress`, a locally observed
  top-level conditional field and contextual subtype.

## Prerequisites

`FEAT-PRESSURE`; unique valid Pressure event, player/team attribution, event
taxonomy, and `FEAT-MINUTES` for per 90.

## Formal definition

\[
P_{p,t,s}=\sum_{e}
I(\text{type}(e)=\text{Pressure}\land\text{player}(e)=p
\land\text{team}(e)=t)
\]

Each unique provider Pressure event counts once regardless of duration or
whether a related on-ball outcome is available.

## Calculation steps

1. Select canonical Pressure events.
2. Validate event UUID, actor, team, and event object.
3. Count unique events.
4. retain location, duration, counterpress subtype, possession context, and link
   coverage for descriptive splits.
5. Aggregate total and per 90.

## Numerator

Unique valid recorded Pressure events attributed to the player.

## Denominator

None for count/per 90. Opportunity- or possession-adjusted pressure is a
separate research metric.

## Unit

Recorded pressures; optional per 90.

## Normalization

Expose total and per 90. Team-possession/opponent-action adjustments are not
part of this definition and require `EXP-DEF-001`.

## Comparison group

Position-compatible player–team–season profiles with the same competition,
season, minute rule, event coverage, and explicit team-context caveat.

## Sample requirements

No validated threshold. Show minutes and count. Test threshold and contextual
stability under `EXP-THRESH-001` and `EXP-DEF-001`.

## Edge cases

- One Pressure event and one opponent `under_pressure` flag are related concepts
  but not two pressure counts.
- Missing location or duration does not necessarily invalidate the count, but
  invalidates the corresponding spatial/duration split.
- Overlapping pressures by multiple players count for each recorded actor.
- Duplicate UUIDs do not count twice.
- Counterpress-tagged pressures are a subset; they remain in the base count.

## Missing-data handling

Missing actor/team/type prevents player attribution and excludes the event with
a warning. Missing event files or uncovered off-ball behavior cannot be treated
as zero pressure.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`,
`DQ-COORD-RANGE`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-DEF-001`, `EXP-THRESH-001`, and
  `EXP-REDUND-001`.
- Open gates: taxonomy/count reconciliation, missing actor/location behavior,
  relation to under-pressure flags, context adjustment, stability, and expert
  interpretation.

## Limitations

Event collection records selected pressure actions, not every press or
coordinated team behavior. Counts are shaped by team possession, role, opponent
behavior, and provider conventions.

## References

- [Research dossier §11.1 and recommendations R7 and R10](../../research/research-dossier.md)
- [Experiment registry: EXP-DEF-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-PRESSURE](../../data/feature-lineage.md)

## Examples

Illustrative only: eight unique Pressure events produce 8 pressures. Three
opponent events carrying `under_pressure: true` do not add three more.

## Changelog

- `0.1.0` — Initial recorded-event proxy definition.
