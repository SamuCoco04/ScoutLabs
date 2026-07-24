# Appearances

| Field | Value |
|---|---|
| Metric ID | `MET-AVAIL-APPEARANCES` |
| Name | Appearances |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts matches in which a player is evidenced as having entered the field. It
answers “in how many matches did this player participate?” rather than “in how
many match squads was the player listed?”

## Intended use

Availability context for player–team–season profiles, Player Profile, Player
Explorer, Compare, and sample warnings. It should be displayed beside starts and
minutes.

## Prohibited interpretation

An appearance is not a start, a full match, selection quality, availability for
matches outside the dataset, or evidence that a lineup-listed substitute played.

## Source fields

- `SRC-LINEUP-PLAYER-ID` — `lineups[].lineup[].player_id`, provider-supplied
  roster identity and join evidence only.
- `SRC-EVENT-TACTICS-LINEUP` —
  `events[].tactics.lineup[].player.id` on Starting XI events.
- `SRC-EVENT-BASE-PLAYER-ID` — `events[].player.id`, event actor evidence.
- `SRC-SUBSTITUTION-REPLACEMENT-ID` —
  `events[].substitution.replacement.id`.
- `SRC-EVENT-BASE-PLAYER-ID` also identifies the actor on Player On and Player
  Off events.

## Prerequisites

`FEAT-APPEARANCE`; valid match and player identity; team-consistent lineup and
event joins; event-type normalization. A roster row alone is insufficient.

## Formal definition

For player \(p\), team \(t\), season \(s\), and valid matches \(M_{t,s}\):

\[
A_{p,t,s}=\sum_{m\in M_{t,s}} I(\text{onPitchEvidence}(p,m,t))
\]

`onPitchEvidence` is true when the player appears in the Starting XI, enters as
the recorded substitution replacement, has a Player On event, or has reliable
on-pitch actor evidence. Conflicting team or identity evidence makes the match
unavailable pending review rather than automatically true.

## Calculation steps

1. Resolve the player, team, season, and valid match.
2. Build the match participation state from Starting XI and change events.
3. Use actor events only as corroboration or recovery evidence, and flag any
   actor not reconcilable with the participation state.
4. Emit at most one appearance per player–team–match.
5. Sum distinct appearance flags for the profile.

## Numerator

Distinct valid matches with on-pitch evidence.

## Denominator

None (count). An optional team-match availability rate would be a separate
metric and requires a defined eligible-team-match denominator.

## Unit

Matches.

## Normalization

No per-90 form. Totals may be grouped by team and season. Percentiles are
generally inappropriate; appearances are sample context, not playing style.

## Comparison group

No performance comparison group. When used as an eligibility or warning
attribute, preserve competition, season, team, dataset coverage, and any
combined multi-team components.

## Sample requirements

None to calculate. Minimum appearances for downstream analysis must be defined
by the consuming experiment and cannot replace a minutes or opportunity rule.

## Edge cases

- A named substitute who never enters does not receive an appearance.
- A substitution replacement and a duplicate Player On event count once.
- A starter with no individual on-ball event still receives an appearance.
- Extra-time entry counts as an appearance; shootout-only participation does not
  count until the event taxonomy can distinguish legitimate on-pitch entry from
  shootout administration.
- A player represented by two teams in a season receives appearances in the
  corresponding team profiles; a combined view must deduplicate only by match.
- Missing Starting XI plus actor evidence is a recoverable but warned case, not
  silently equivalent to complete evidence.

## Missing-data handling

Return unavailable for a match if identity or team conflicts cannot be resolved.
Do not infer non-appearance from an absent event file or appearance from a
lineup roster alone. Retain the excluded-match count.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-LINEUP-CONSISTENCY`,
`DQ-STARTING-XI-CONSISTENCY`, `DQ-SUBSTITUTION-CONSISTENCY`,
`DQ-PLAYER-ON-OFF`, `DQ-EVENT-TYPE-OBJECT`, `DQ-EXTRA-TIME`,
`DQ-SHOOTOUT`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiment: `EXP-MIN-001`.
- Open gates: Starting XI/change-event reconciliation, duplicate change events,
  missing-event behavior, extra time, shootouts, and known-match fixtures.

## Limitations

Source coverage defines the observable match universe. Appearances do not
measure duration, availability between covered fixtures, or contribution.

## References

- [Research dossier §6.1 and recommendations R1, R2, R9](../../research/research-dossier.md)
- [Experiment registry: EXP-MIN-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-APPEARANCE](../../data/feature-lineage.md)

## Examples

Illustrative only: a player starts two matches, enters once as a replacement,
and is an unused substitute once. The metric is 3 appearances, not 4.

## Changelog

- `0.1.0` — Initial proposed evidence-based appearance definition.
