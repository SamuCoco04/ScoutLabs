# Goalkeeper xG faced

| Field | Value |
|---|---|
| Metric ID | `MET-GK-XG-FACED` |
| Name | Goalkeeper xG faced |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Sums provider-supplied pre-shot StatsBomb xG for opponent shots that can be
reliably linked to goalkeeper shot-facing actions. It describes the pre-shot
chance quality faced by a goalkeeper.

## Intended use

Goalkeeper-specific Player Profile, Player Explorer, Compare, shot-facing maps,
sample context, and goalkeeper similarity research. Penalty and non-penalty
splits must remain available.

## Prohibited interpretation

This is not post-shot xG, goals prevented, save quality, goalkeeper positioning,
shot placement, finishing-adjusted performance, or a ScoutLabs-trained model.
It must not be used in outfield comparison groups.

## Source fields

- `SRC-EVENT-BASE-ID`, `SRC-EVENT-BASE-TYPE-ID`,
  `SRC-EVENT-BASE-PLAYER-ID`, `SRC-EVENT-BASE-TEAM-ID`, and
  `SRC-EVENT-BASE-PERIOD`, and `SRC-EVENT-RELATED-EVENTS`.
- `SRC-SHOT-XG`, `SRC-SHOT-TYPE-ID`, and `SRC-SHOT-OUTCOME-ID`.
- `SRC-SHOT-KEY-PASS-ID` is creation lineage only and does not identify the
  goalkeeper.
- `SRC-GK-TYPE-ID` — `events[].goalkeeper.type.id`.
- `SRC-GK-OUTCOME-ID` — `events[].goalkeeper.outcome.id`.
- On-pitch attribution and per-90 context inherit the audited source lineage of
  `FEAT-MINUTES` (Starting XI, substitutions, Player On/Off, period boundaries,
  dismissals, and lineup position intervals).

## Prerequisites

`FEAT-SHOT-XG`, `FEAT-GK-SHOT-FACED`, `FEAT-GK-XG-FACED`, `FEAT-MINUTES`;
audited goalkeeper type/outcome taxonomy; unique resolved Shot-to-Goalkeeper
relationship; opponent team consistency; finite numeric xG; validated
participation intervals for attribution and per-90 output.

## Formal definition

Let \(L_{g,m}^{(v)}\) be unique opponent Shot events linked under goalkeeper
taxonomy version \(v\) to eligible shot-facing actions attributed to goalkeeper
\(g\):

\[
xGFaced_{g,t,s}^{(v)}=\sum_{q\in L_{g,t,s}^{(v)}}
\text{statsbomb\_xg}(q)
\]

Each Shot contributes at most once. `EXP-GK-001` must define eligible goalkeeper
types/outcomes and compare link-first with shot-outcome-plus-on-pitch
reconciliation. The proposal selects no final taxonomy.

## Calculation steps

1. Identify goalkeeper on-pitch intervals and candidate Goal Keeper events.
2. Audit type/outcome values that represent a shot faced (save, goal conceded,
   and other valid shot-facing cases).
3. Resolve related Shot UUIDs within the same match; confirm opposing teams.
4. Validate and deduplicate provider xG by Shot UUID.
5. Sum xG; retain shots faced, penalties, outcomes, unresolved links, xG
   coverage, and minutes.

## Numerator

Sum of StatsBomb xG over unique, eligible, linked opponent shots.

## Denominator

None for total/per 90. Mean xG per shot faced uses the eligible
`FEAT-GK-SHOT-FACED` count as a separate rate denominator.

## Unit

Expected goals faced; optional per 90.

## Normalization

Expose total, per 90, and per-shot context separately. Penalty and non-penalty
splits are mandatory. Provider xG version and link policy remain traceable.

## Comparison group

Goalkeeper-only player–team–season profiles with the same taxonomy, provider
version treatment, competition/season scope, minimum minutes, minimum shots
faced, and link coverage.

## Sample requirements

No validated threshold. Always show minutes and linked shots faced.
`EXP-GK-001`, `EXP-THRESH-001`, and `EXP-GK-002` establish taxonomy,
stability, and goalkeeper comparison rules.

## Edge cases

- Penalties are included in the total but must be separately available; a
  non-penalty variant would explicitly exclude them and shootouts.
- Shootout treatment must be separate from match shot-stopping.
- One shot linked to duplicate Goal Keeper references contributes once.
- A Goal without a resolvable Goal Keeper event, or a Goal Keeper action without
  a shot link, is a coverage case, not automatically included or zero xG.
- Own goals, deflections, rebounds, goalkeeper substitutions, and outfield
  players acting as goalkeeper require audited rules.
- Missing xG and unresolved links are distinct failures.

## Missing-data handling

Do not impute xG, invent a goalkeeper from team identity alone, or assign zero
to unresolved shots. Report eligible candidate shots, resolved links, xG-covered
shots, and profile coverage. Inadequate coverage makes comparison unavailable.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`,
`DQ-REL-UNRESOLVED`, `DQ-SHOOTOUT`, `DQ-INCOMPLETE-VIDEO`,
`DQ-PROVIDER-VERSION`, `DQ-SHOT-GK-LINK`, `DQ-STARTING-XI-CONSISTENCY`,
`DQ-SUBSTITUTION-CONSISTENCY`, `DQ-PLAYER-ON-OFF`,
`DQ-PERIOD-BOUNDARY`, `DQ-STOPPAGE-TIME`, `DQ-EXTRA-TIME`, and
`DQ-DISMISSAL`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-GK-001`, `EXP-THRESH-001`, and
  `EXP-GK-002`.
- Open gates: GK taxonomy, shot-link resolution, on-pitch attribution, penalties,
  shootouts, rebounds, own goals, xG coverage, and goalkeeper-specific stability.

## Limitations

Pre-shot xG reflects chance quality before placement and is heavily shaped by
team defence and opponents. It cannot evaluate whether the goalkeeper could or
should have saved a shot.

## References

- [Research dossier §12 and recommendation R8](../../research/research-dossier.md)
- [Experiment registry: EXP-GK-001 and EXP-GK-002](../../research/metric-experiments.md)
- [Feature lineage: FEAT-GK-XG-FACED](../../data/feature-lineage.md)

## Examples

Illustrative only: four unique linked opponent shots with xG 0.05, 0.20, 0.35,
and 0.75 yield 1.35 xG faced. The 0.75 penalty remains separately identified.

## Changelog

- `0.1.0` — Initial pre-shot linked-xG proposal; goalkeeper taxonomy unresolved.
