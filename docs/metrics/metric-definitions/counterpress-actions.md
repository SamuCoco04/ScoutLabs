# Counterpress actions

| Field | Value |
|---|---|
| Metric ID | `MET-PRESS-COUNTERPRESS-ACTIONS` |
| Name | Counterpress actions |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts player-attributed events for which StatsBomb supplies
`counterpress: true`. It describes provider-tagged defensive activity in a
short post-turnover context.

## Intended use

Totals/per 90, event-type and location splits, Player Profile, Player Explorer,
Metric Leaders, Compare, and experimental similarity dimensions.

## Prohibited interpretation

This is not a ScoutLabs-detected counterpress, complete team counterpress,
pressing intensity, recovery success, tracking-derived counterpress model, or
proof of a coordinated tactical instruction.

## Source fields

- `SRC-EVENT-BASE-COUNTERPRESS` — `events[].counterpress`, a locally observed
  top-level conditional provider flag across eligible defensive event types.
- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
  `SRC-EVENT-BASE-TEAM-ID`, and `SRC-EVENT-BASE-LOCATION`.
- `SRC-EVENT-POSSESSION` — `events[].possession`, context and audit.

## Prerequisites

`FEAT-COUNTERPRESS`; valid event type, player/team attribution, boolean flag,
and an audited list of event types on which the conditional flag can appear.

## Formal definition

\[
CP_{p,t,s}=\sum_e
I(\text{player}(e)=p\land\text{team}(e)=t
\land\text{counterpress}(e)=\text{true})
\]

The base count spans all valid player-attributed event types on which the
provider legitimately supplies the flag. A pressure-only subset is retained but
is not substituted for the base definition.

## Calculation steps

1. Select events with an explicit boolean `counterpress: true`.
2. Validate event type, UUID, actor, team, and conditional-field eligibility.
3. Count unique events once.
4. retain event-type, location, possession, and subsequent-outcome context as
   separate descriptive fields.
5. Aggregate total and per 90.

## Numerator

Unique player events explicitly tagged `counterpress: true`.

## Denominator

None for count/per 90. Share of pressures or defensive actions is a separate
rate with a named denominator.

## Unit

Provider-tagged counterpress actions; optional per 90.

## Normalization

Expose total and per 90. Possession/opportunity adjustment is not part of this
version and requires `EXP-DEF-001`.

## Comparison group

Position-compatible player–team–season profiles with common source/event
version, competitions/seasons, minute rule, and coverage.

## Sample requirements

No validated minimum; the event is potentially sparse. Show minutes, count, and
tagged-event-type distribution. Test through `EXP-DEF-001` and
`EXP-THRESH-001`.

## Edge cases

- Absence of the conditional flag means “not tagged,” not proof that no
  counterpress occurred in reality.
- A tagged Pressure event counts in both `MET-PRESS-PRESSURES` and this metric;
  that overlap must be considered in similarity redundancy.
- Boolean false and missing are retained as distinct source states for coverage.
- Tagged non-Pressure defensive actions remain eligible when verified by the
  provider taxonomy.
- Do not reconstruct or expand a time window around turnovers in this metric.

## Missing-data handling

Malformed flags or missing actors make the event unavailable for player counts.
Missing flags are not imputed from sequence timing. Source/event-file absence is
not zero counterpressing.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, and
`DQ-PROVIDER-VERSION`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-DEF-001`, `EXP-REDUND-001`, and
  `EXP-THRESH-001`.
- Open gates: eligible event-type audit, boolean coverage, overlap with
  pressures/recoveries, opportunity adjustment, stability, and expert wording.

## Limitations

The provider flag is an event-level proxy. Event data cannot observe complete
team structure, closing speed, unrecorded pressure, or coordinated behavior
between events.

## References

- [Research dossier §§11.1, 24, and recommendations R7 and R10](../../research/research-dossier.md)
- [Experiment registry: EXP-DEF-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-COUNTERPRESS](../../data/feature-lineage.md)

## Examples

Illustrative only: two Pressure events and one Ball Recovery event explicitly
tagged `counterpress: true` yield 3 counterpress actions and a 2/1 type split.

## Changelog

- `0.1.0` — Initial provider-flag aggregation proposal.
