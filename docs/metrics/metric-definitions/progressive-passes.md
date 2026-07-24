# Progressive passes

| Field | Value |
|---|---|
| Metric ID | `MET-PROG-PASSES` |
| Name | Progressive passes |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts completed passes that move the ball materially closer to the opponent’s
goal under a named geometric rule. It asks how often a player advances
possession through passing, not whether a pass breaks a defensive line.

## Intended use

Progression totals/per 90, action maps, Player Profile, Player Explorer, Metric
Leaders, Compare, and similarity research after definition and redundancy
experiments.

## Prohibited interpretation

This is not a provider-supplied StatsBomb flag, xT, pass value, line breaking,
pass difficulty, or proof that possession was retained after the receiver’s
next action.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, and
  `SRC-EVENT-BASE-TEAM-ID`.
- `SRC-EVENT-BASE-LOCATION` — `events[].location`.
- `SRC-PASS-END-LOCATION` — `events[].pass.end_location`.
- `SRC-PASS-OUTCOME-ID` — completion eligibility.
- `SRC-PASS-TYPE-ID`, `SRC-PASS-LENGTH`, and `SRC-PASS-ANGLE` — audit,
  alternative rules, and explanatory context.

## Prerequisites

`FEAT-PASS-ATTEMPT`, `FEAT-PASS-COMPLETED`,
`FEAT-PASS-X-PROGRESSION`, `FEAT-PROGRESSIVE-PASS`; valid two-dimensional
start/end coordinates; attacking-direction normalization; versioned pitch
geometry and pass eligibility.

## Formal definition

For completed pass \(e\), start \(s_e\), end \(z_e\), opponent-goal centre \(g\),
and rule version \(v\):

\[
\Delta_g(e)=d(s_e,g)-d(z_e,g)
\]

\[
\text{ProgressivePass}^{(v)}(e)=
I(\Delta_g(e)\ge T_v(s_e,z_e)
\land \text{eligible}^{(v)}(e))
\]

\[
PP_{p,t,s}^{(v)}=\sum_e \text{ProgressivePass}^{(v)}(e)
\]

No threshold function \(T_v\) is selected in this proposal. `EXP-PROG-001`
must compare: context-dependent 30/15/10-metre goal-distance reduction;
fixed normalized x-gain; advance into a more advanced tactical zone; and xT
gain (the last is action value, not a like-for-like geometric definition).
Any physical-metre rule must document conversion from StatsBomb’s 120×80
coordinates.

## Calculation steps

1. Select completed, eligible Pass events.
2. validate and normalize start/end direction.
3. Calculate goal-distance reduction and rule-specific components.
4. Apply exactly one versioned threshold rule.
5. Aggregate count while retaining start/end points, rule version, attempts, and
   minutes.

## Numerator

Completed passes satisfying the selected progression rule.

## Denominator

None for count/per 90. A share variant uses eligible completed passes and must
be a separately named metric.

## Unit

Progressive passes; optional per 90.

## Normalization

Expose total and per 90 from validated seconds. Comparison percentiles must use
the same rule version and population. xT-weighted output is not this metric.

## Comparison group

Position-compatible player–team–season profiles with common rule, pitch
transform, pass eligibility, competitions/seasons, and minute threshold.

## Sample requirements

No validated threshold. Show minutes, completed passes, and progressive count;
test convergence and positional thresholds in `EXP-PROG-001` and
`EXP-THRESH-001`.

## Edge cases

- Incomplete passes are excluded even if the intended end point is advanced.
- Start equals end and backwards/lateral passes do not qualify unless a future
  rule explicitly and defensibly says otherwise.
- Passes starting very near goal need a threshold rule that does not create
  impossible expectations.
- Set pieces, goalkeeper passes, clearances, and crosses require explicit
  inclusion/split policy.
- Coordinates on zone boundaries follow a documented inclusive/exclusive
  convention.
- Line-breaking language is prohibited without opponent-structure evidence.

## Missing-data handling

Invalid/missing start, end, actor, or completion evidence excludes the event
from both count and eligible spatial denominator; report coverage. Never use
zero coordinates as imputation.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-UUID-UNIQUE`,
`DQ-EVENT-TYPE-OBJECT`, `DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`,
`DQ-COORD-RANGE`, and `DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-PROG-001`, `EXP-REDUND-001`, and
  `EXP-THRESH-001`.
- Open gates: threshold selection, coordinate conversion, set-piece policy,
  stability, overlap with entries/xT, and football review.

## Limitations

The rule is contested and sensitive to starting zone. Event geometry does not
observe defensive lines, pressure intensity, or receiving outcome beyond the
pass classification.

## References

- [Research dossier §§7.3, 24, and R9](../../research/research-dossier.md)
- [Experiment registry: EXP-PROG-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-PASS-X-PROGRESSION and FEAT-PROGRESSIVE-PASS](../../data/feature-lineage.md)

## Examples

Illustrative only: a completed pass reducing goal distance by 18 normalized
units may qualify under one fixed rule and fail a zone-specific rule. The
reported metric must name the rule version; this proposal does not decide the
case.

## Changelog

- `0.1.0` — Competing progression definitions registered; no default selected.
