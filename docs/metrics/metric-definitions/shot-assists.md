# Shot assists

| Field | Value |
|---|---|
| Metric ID | `MET-CREATE-SHOT-ASSISTS` |
| Name | Shot assists |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts qualifying passes recorded as directly setting up a teammate’s shot. It
describes final-pass creation volume under StatsBomb’s event/link semantics.

## Intended use

Chance-creation totals/per 90, pass and shot-link explanations, Player Profile,
Player Explorer, Metric Leaders, Compare, and similarity research.

## Prohibited interpretation

A shot assist is not synonymous with a key pass, goal assist, expected assist,
chance quality, all creative contribution, or an independently observed
commercial provider metric.

## Source fields

- `SRC-PASS-SHOT-ASSIST` — `events[].pass.shot_assist`.
- `SRC-PASS-GOAL-ASSIST` — `events[].pass.goal_assist`, retained as a subtype
  and reconciliation signal.
- `SRC-PASS-ASSISTED-SHOT-ID` —
  `events[].pass.assisted_shot_id`.
- `SRC-EVENT-RELATED-EVENTS` — `events[].related_events[]`, relationship
  corroboration.
- `SRC-EVENT-BASE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
  `SRC-EVENT-BASE-TEAM-ID`, and `SRC-EVENT-BASE-TYPE-ID`.
- `SRC-SHOT-KEY-PASS-ID` — `events[].shot.key_pass_id`, reverse link from the
  shot.

## Prerequisites

`FEAT-SHOT-ASSIST`; unique event UUIDs; valid Pass-to-Shot link; teammate and
match consistency; audited behavior of flags, forward links, reverse links,
goal assists, and relationship arrays.

## Formal definition

For eligible Pass event \(e\), let \(q(e)\) be the unique linked Shot event:

\[
SA(e)=I((\text{pass.shot\_assist}=\text{true}
\lor\text{pass.goal\_assist}=\text{true})
\land q(e)\text{ resolves}
\land \text{sameMatchTeam}(e,q(e)))
\]

\[
SA_{p,t,s}=\sum_e SA(e)
\]

This is the strict candidate. Including either flag prevents a scoring shot
from being omitted when only goal-assist evidence is present. `EXP-XA-001`
compares flag-first, link-first, and reconciled-union definitions. Conflicts are
reported rather than silently resolved. A goal-assist flag does not add a second
count for the same pass.

## Calculation steps

1. Select player-attributed Pass events with shot-assist/goal-assist/link
   evidence.
2. Resolve `assisted_shot_id`, shot `key_pass_id`, and relevant related-event
   references within the same match.
3. Confirm linked event is a Shot by the same team and not the passer.
4. Apply the selected reconciliation rule and record conflicts/missing links.
5. Count unique qualifying Pass event IDs once.

## Numerator

Unique qualifying passes linked to a teammate shot.

## Denominator

None for count/per 90. A shot-assist rate per eligible pass would be separate.

## Unit

Shot assists; optional per 90.

## Normalization

Expose total and per 90 using validated seconds. Keep goal-assist subtype,
linked-shot count, and coverage alongside the metric.

## Comparison group

Position-compatible player–team–season profiles with the same linkage rule,
competitions/seasons, minutes threshold, and link coverage.

## Sample requirements

No validated threshold. Creation is sparse; display minutes and counts. Test
minimum minutes and link stability in `EXP-XA-001` and `EXP-THRESH-001`.

## Edge cases

- One pass with duplicate relationship references counts once.
- Goal assists are a subtype, not an additional shot assist.
- A flag without a resolvable shot, a reverse-only link, or conflicting links is
  retained as a quality case and handled by the chosen version.
- Own goals, shots removed by an event correction, deflections, and unusual
  set-piece chains require audited treatment.
- The linked shooter must be a teammate in the same match.
- Non-pass final actions before shots are outside this metric.

## Missing-data handling

Under the strict candidate, unresolved/conflicting links are unavailable and
excluded, not treated as zero or as valid assists. Report flag coverage, link
coverage, resolution rate, and excluded count.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, and
`DQ-REL-UNRESOLVED`, and `DQ-PASS-SHOT-LINK`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiment: `EXP-XA-001`.
- Open gates: bidirectional-link resolution, flag disagreements, own goals,
  deflections, set pieces, duplicate relationships, and manual fixtures.

## Limitations

This final-action metric omits earlier creation and depends on provider tagging
and event relationships. Team shot volume and finishing choices shape counts.

## References

- [Research dossier §§7.7, 10, 24, and R5](../../research/research-dossier.md)
- [Experiment registry: EXP-XA-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-SHOT-ASSIST](../../data/feature-lineage.md)

## Examples

Illustrative only: a pass has `shot_assist: true`, links to one teammate Shot,
and that shot points back through `key_pass_id`. It contributes one shot assist,
even if the relationship UUID appears twice.

## Changelog

- `0.1.0` — Strict link-resolved proposal with competing reconciliation rules
  registered.
