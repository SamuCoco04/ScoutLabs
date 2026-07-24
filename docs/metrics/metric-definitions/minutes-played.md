# Minutes played

| Field | Value |
|---|---|
| Metric ID | `MET-AVAIL-MINUTES` |
| Name | Minutes played |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Measures evidenced on-pitch exposure using actual played period endpoints and
player entry/exit evidence. It answers “for how long was this player on the
field in covered matches?”

## Intended use

The exposure denominator for per-90 metrics, candidate eligibility, sample
warnings, Player Profile, Player Explorer, Compare, Metric Leaders, and
similarity research. Raw seconds are canonical; display minutes are derived.

## Prohibited interpretation

Minutes are not performance, availability outside covered matches, or a
reliability guarantee. Ninety nominal minutes must not be assumed for every
match. Shootout time is not playing time.

## Source fields

- `SRC-EVENT-TACTICS-LINEUP` —
  `events[].tactics.lineup[].player.id`.
- `SRC-EVENT-BASE-PERIOD` — `events[].period`.
- `SRC-EVENT-BASE-TIMESTAMP` — `events[].timestamp`.
- `SRC-EVENT-BASE-MINUTE` — `events[].minute`.
- `SRC-EVENT-BASE-SECOND` — `events[].second`.
- `SRC-EVENT-BASE-DURATION` — `events[].duration`, corroborating interval
  evidence where applicable, not a match-duration field.
- `SRC-EVENT-BASE-PLAYER-ID` — `events[].player.id`.
- `SRC-SUBSTITUTION-REPLACEMENT-ID` —
  `events[].substitution.replacement.id`.
- `SRC-SUBSTITUTION-OUTCOME-ID` — `events[].substitution.outcome.id`.
- `SRC-EVENT-BASE-PLAYER-ID` — `events[].player.id`, including Player On and
  Player Off actors conditional on event type.
- `SRC-PLAYER-OFF-PERMANENT` — `events[].player_off.permanent`.
- `SRC-HALF-END-EARLY-VIDEO-END` —
  `events[].half_end.early_video_end`.
- `SRC-HALF-END-MATCH-SUSPENDED` —
  `events[].half_end.match_suspended`.

There is no provider match-duration field in the reviewed source. Period
endpoints must be derived from event evidence.

## Prerequisites

`FEAT-START`, `FEAT-APPEARANCE`, and `FEAT-MINUTES`; normalized event order and
period-local time; team-consistent participation state; actual usable endpoint
for each played period.

## Formal definition

For every non-shootout period \(r\), build the union of on-pitch intervals
\([a_{p,r,k}, b_{p,r,k})\) supported by Starting XI and change evidence. Let
\(E_r\) be the actual period endpoint:

\[
\text{seconds}_{p,m}=\sum_{r\in\{1,2,3,4\}}
\sum_k \max(0,\min(b_{p,r,k},E_r)-a_{p,r,k})
\]

\[
\text{minutes}_{p,t,s}=
\frac{\sum_m \text{seconds}_{p,m}}{60}
\]

Periods 3 and 4 contribute only when played. Period 5 (shootout) is excluded.
Raw seconds are retained; presentation rounding is not part of the metric.

## Calculation steps

1. Validate event order, period boundaries, timestamp shape, and end evidence.
2. Seed on-pitch state from each team’s Starting XI.
3. Apply substitution replacement, Player On, Player Off, and permanent-exit
   evidence at period-local timestamps without double counting duplicates.
4. Carry legitimate on-pitch state across halftime and into extra time; close
   intervals at actual period endpoints.
5. Exclude shootout events and flag suspended, early-video-end, inconsistent, or
   unresolved dismissal cases.
6. Sum raw seconds by player–team–match and profile; divide by 60 only for the
   metric value shown.

## Numerator

Sum of validated on-pitch seconds.

## Denominator

60 seconds per minute. Per-90 consumers use validated player seconds divided by
5,400 seconds, not rounded display minutes.

## Unit

Minutes, backed by integer or precise raw seconds.

## Normalization

No normalization for the base metric. A count metric \(x\) per 90 is
\(x \times 5{,}400 / \text{validated seconds}\). Per-90 values are unavailable
when seconds are zero or evidence is invalid.

## Comparison group

Minutes are sample context. Eligibility thresholds may vary by position,
competition/season universe, and metric opportunity; those conventions must be
shown and versioned.

## Sample requirements

None to calculate. `EXP-THRESH-001` defines candidate-population thresholds, and
`EXP-SHRINK-001` evaluates reliability treatment. No universal minimum is
currently validated.

## Edge cases

- Stoppage time is included through actual period endpoints, not capped at 45 or
  90.
- Extra time is included; shootouts are excluded.
- A substitution at an endpoint must not create negative or duplicated time.
- A dismissal may be represented by Player Off, permanent flags, cards, or
  interacting evidence; the complete precedence rule remains unresolved.
- Temporary Player Off/On intervals must not be treated as permanent exits.
- Early video end and suspended matches retain partial evidence and a quality
  state; whether partial minutes are admitted downstream is a consumer decision.
- Abandoned periods, missing Half End, duplicate changes, and players acting
  while marked off-pitch require warnings and may make the match unavailable.
- Provider `minute` may be cumulative while `timestamp` is period-local; the
  normalized clock must not mix conventions.

## Missing-data handling

Do not substitute scheduled 90 minutes. If an endpoint or participation state
cannot be resolved, return unavailable for the affected player-match, retain
any separately labeled partial seconds for audit, and exclude it from per-90
denominators until a reviewed policy admits it.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-LINEUP-CONSISTENCY`,
`DQ-STARTING-XI-CONSISTENCY`, `DQ-SUBSTITUTION-CONSISTENCY`,
`DQ-PLAYER-ON-OFF`, `DQ-EVENT-TIMESTAMP-ORDER`,
`DQ-PERIOD-BOUNDARY`, `DQ-STOPPAGE-TIME`, `DQ-EXTRA-TIME`,
`DQ-SHOOTOUT`, `DQ-DISMISSAL`, `DQ-EVENT-TYPE-OBJECT`,
`DQ-CONDITIONAL-FIELD`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-MIN-001`, `EXP-THRESH-001`, and
  `EXP-SHRINK-001`.
- Open gates: clock convention, actual endpoints, substitutions, temporary and
  permanent exits, dismissals, stoppage time, extra time, shootouts, interrupted
  matches, and hand-checked fixtures.

## Limitations

Event evidence may be incomplete or internally inconsistent. Minute exposure
does not measure role consistency, intensity, or opportunity for every action.
Rounding at the player-match level can bias totals and is prohibited.

## References

- [Research dossier §6 and contested definitions](../../research/research-dossier.md)
- [Experiment registry](../../research/metric-experiments.md)
- [Feature lineage: FEAT-MINUTES](../../data/feature-lineage.md)
- [Data-quality rules](../../data/data-quality-rules.md)

## Examples

Illustrative only: a starter exits at 70:30 of regulation and a substitute enters
then. Their raw intervals are 4,230 seconds and the remaining validated match
seconds respectively; neither value is rounded before season aggregation.

## Changelog

- `0.1.0` — Initial research definition; complete playing-time edge-case policy
  deliberately remains unresolved pending `EXP-MIN-001`.
