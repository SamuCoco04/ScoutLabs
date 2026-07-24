# Non-penalty shots

| Field | Value |
|---|---|
| Metric ID | `MET-SHOOT-NON-PENALTY-SHOTS` |
| Name | Non-penalty shots |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts recorded Shot events taken by a player outside penalties and shootouts.
It describes non-penalty shooting volume in covered matches.

## Intended use

Goal-threat totals/per 90, denominator for shot-quality summaries, Player
Profile, Player Explorer, Metric Leaders, Compare, and similarity research.

## Prohibited interpretation

Shot volume is not shot quality, finishing, goals, threat added, team-independent
ability, or continuous attacking involvement.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, and
  `SRC-EVENT-BASE-TEAM-ID`.
- `SRC-EVENT-BASE-PERIOD` — shootout exclusion.
- `SRC-SHOT-TYPE-ID` — `events[].shot.type.id`, penalty classification.
- `SRC-SHOT-OUTCOME-ID` — `events[].shot.outcome.id`, retained as context, not a
  count filter.

## Prerequisites

`FEAT-SHOT`, `FEAT-NON-PENALTY-SHOT`; valid Shot object, actor, team, period,
and audited Shot type vocabulary.

## Formal definition

\[
NPS_{p,t,s}=\sum_{e\in \text{Shot}_{p,t,s}}
I(\text{shotType}(e)\ne\text{Penalty}\land\text{period}(e)\ne5)
\]

The canonical provider type ID is used, not a localized name. Both penalty-type
shots and all period-5 shootout shots are excluded.

## Calculation steps

1. Select unique player-attributed Shot events with valid nested Shot objects.
2. Validate period and shot-type IDs.
3. Exclude penalty type and shootout period.
4. Count remaining shots regardless of outcome.
5. Aggregate total and per 90; retain outcome/type splits and minutes.

## Numerator

Eligible non-penalty, non-shootout Shot events.

## Denominator

None for count/per 90.

## Unit

Shots; optional per 90.

## Normalization

Expose total and per 90 from validated seconds. Shooting shares and conversion
rates require their own denominators and definitions.

## Comparison group

Position-compatible player–team–season profiles with common competition/season,
minute threshold, and source version. Goalkeepers are not compared with
outfield shooting populations.

## Sample requirements

No validated universal threshold. Show minutes and raw shot count; test
eligibility through `EXP-THRESH-001` and stability through
`EXP-SHRINK-001`.

## Edge cases

- Period-5 events are excluded even if a type is malformed.
- Penalties during regulation or extra time are excluded.
- Free-kick shots remain non-penalty and can be shown as a subtype.
- Own Goal Against is not silently converted into a player Shot.
- Blocked, saved, off-target, and goal outcomes all count if otherwise eligible.
- Duplicate event UUIDs count once and trigger a quality failure.

## Missing-data handling

An absent/unrecognized shot type prevents reliable non-penalty classification
and is excluded with a warning. Missing event files do not mean zero shots.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, and
`DQ-SHOOTOUT`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-THRESH-001` and `EXP-SHRINK-001`.
- Open gates: observed shot types/outcomes, period-5 fixtures, own-goal
  treatment, duplicates, and aggregation tests.

## Limitations

Shots depend on role, team chance creation, game state, and competition.
Recorded shots omit attacking contributions that do not end in a shot.

## References

- [Research dossier §9 and recommendation R2](../../research/research-dossier.md)
- [Experiment registry](../../research/metric-experiments.md)
- [Feature lineage: FEAT-NON-PENALTY-SHOT](../../data/feature-lineage.md)

## Examples

Illustrative only: five open-play shots, one direct-free-kick shot, one
regulation penalty, and one shootout kick produce 6 non-penalty shots.

## Changelog

- `0.1.0` — Initial provider-type and period-based exclusion proposal.
