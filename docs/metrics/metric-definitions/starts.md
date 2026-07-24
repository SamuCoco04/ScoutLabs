# Starts

| Field | Value |
|---|---|
| Metric ID | `MET-AVAIL-STARTS` |
| Name | Starts |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts matches in which a player is named in the provider-supplied Starting XI
tactical lineup. It answers “how often did the player begin the match on the
field?”

## Intended use

Availability and sample context on Player Profile, Player Explorer, Compare,
and similarity explanations. It is a prerequisite for minutes-state
reconstruction.

## Prohibited interpretation

Starts do not establish role, importance, full-match participation, or tactical
position beyond the recorded starting snapshot. A lineup roster entry is not a
start.

## Source fields

- `SRC-EVENT-TACTICS-LINEUP` —
  `events[].tactics.lineup[].player.id` on Starting XI events.
- `SRC-EVENT-BASE-TEAM-ID` — `events[].team.id`.
- `SRC-EVENT-BASE-TYPE-ID` — `events[].type.id`.
- `SRC-LINEUP-PLAYER-ID` — `lineups[].lineup[].player_id`, roster
  reconciliation only.

## Prerequisites

`FEAT-START`; valid match, player, and team identities; exactly one usable
Starting XI snapshot per team at match start or a documented resolution rule.

## Formal definition

\[
S_{p,t,s}=\sum_{m\in M_{t,s}}
 I(p\in \text{StartingXI}(m,t))
\]

The membership test uses the `tactics.lineup` attached to a Starting XI event,
not the full lineup-file roster and not the first event acted by the player.

## Calculation steps

1. Select Starting XI events by canonical event type.
2. resolve the event team and nested player IDs.
3. Validate uniqueness, team membership, and expected lineup cardinality.
4. Emit one start per player–team–match.
5. Sum across the profile.

## Numerator

Distinct valid matches whose team Starting XI contains the player.

## Denominator

None (count).

## Unit

Matches started.

## Normalization

Show the total and optionally starts/appearances as a separately versioned rate.
Do not calculate starts per 90.

## Comparison group

No performance percentile is recommended. Preserve player–team–season context
and covered matches.

## Sample requirements

None to calculate. Downstream sample admission depends on minutes and metric
opportunities, not starts alone.

## Edge cases

- Duplicate identical Starting XI events count once but trigger validation.
- Conflicting Starting XI snapshots make affected team-match starts unavailable.
- A player added by a Player On event at time zero is not silently treated as a
  starter; the discrepancy requires investigation.
- Extra-time-only replacement entries are not starts.
- Tactical Shift lineups never redefine the match start.
- A player listed in the lineup file but absent from Starting XI evidence is not
  a starter.

## Missing-data handling

If the Starting XI event or its tactics object is absent, do not infer starts
from early touches. Return unavailable for the affected team-match and expose
the missing evidence.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-LINEUP-CONSISTENCY`,
`DQ-STARTING-XI-CONSISTENCY`, `DQ-EVENT-TYPE-OBJECT`, and
`DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiment: `EXP-MIN-001`.
- Open gates: duplicate/conflicting Starting XI handling, team cardinality,
  missing tactics, and known-match fixtures.

## Limitations

The provider’s starting position is a snapshot, not a full-match tactical role.
Starts alone are a poor exposure measure.

## References

- [Research dossier §§5 and 6.1](../../research/research-dossier.md)
- [Experiment registry: EXP-MIN-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-START](../../data/feature-lineage.md)

## Examples

Illustrative only: a player appears in the Starting XI of four matches and
enters from the bench in two. Starts = 4; appearances = 6.

## Changelog

- `0.1.0` — Initial proposed Starting XI definition.
