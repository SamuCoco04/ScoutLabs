# Pass completion rate

| Field | Value |
|---|---|
| Metric ID | `MET-PASS-COMPLETION-RATE` |
| Name | Pass completion rate |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Shows the share of eligible recorded pass attempts classified as completed
under one explicit outcome and pass-type policy.

## Intended use

Passing/circulation context in Player Profile, Player Explorer, Metric Leaders,
Compare, and similarity research. It must be shown with completed and attempted
pass counts.

## Prohibited interpretation

Completion rate is not pass quality, ambition, difficulty, progression, or
decision quality. Rates from different eligibility versions or tiny
denominators are not directly comparable.

## Source fields

Uses the same fields as [completed passes](completed-passes.md):
`SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
`SRC-EVENT-BASE-TEAM-ID`, `SRC-PASS-OUTCOME-ID`, and `SRC-PASS-TYPE-ID`.

## Prerequisites

`FEAT-PASS-ATTEMPT`, `FEAT-PASS-COMPLETED`,
`FEAT-PASS-COMPLETION-RATE`, and identical eligibility version for numerator
and denominator.

## Formal definition

\[
\text{PassCompletionPct}_{p,t,s}^{(v)}
=100\frac{\text{CompletedPasses}_{p,t,s}^{(v)}}
{\text{EligiblePassAttempts}_{p,t,s}^{(v)}}
\]

The result is unavailable when eligible attempts are zero. Numerator and
denominator must be recomputed from the same record set; independently filtered
aggregates cannot be divided.

## Calculation steps

1. Build the versioned eligible-pass set.
2. Apply the audited completion rule from `MET-PASS-COMPLETED`.
3. Count all eligible attempts and completed attempts.
4. Return unavailable for a zero denominator.
5. Store numerator, denominator, percentage, eligibility version, and excluded
   record count together.

## Numerator

`MET-PASS-COMPLETED` completed passes under the same version.

## Denominator

`MET-PASS-ATTEMPTS` eligible pass attempts under the same version.

## Unit

Percentage from 0 to 100.

## Normalization

The rate already uses an opportunity denominator and is never converted per 90.
Percentiles or standardized values require a named comparison group. Shrinkage,
if adopted, is a separate value and must not overwrite the raw rate.

## Comparison group

Position-compatible player–team–season profiles using identical pass
eligibility, competitions/seasons, minute threshold, and a validated
minimum-attempt rule.

## Sample requirements

No threshold is yet validated. Always display attempts. `EXP-PASS-001`,
`EXP-THRESH-001`, and `EXP-SHRINK-001` test minimum denominators and stability.

## Edge cases

- Zero eligible attempts returns unavailable, not 0%.
- Unknown/malformed outcomes are excluded symmetrically and reported.
- Rounding occurs only for display after aggregation.
- Special pass types cannot be removed from only one side of the fraction.
- Combining teams requires summing numerators and denominators, not averaging
  team percentages.

## Missing-data handling

Unavailable numerator or denominator makes the rate unavailable. Do not impute
missing passes or interpret missing files as zero attempts.

## Quality dependencies

All dependencies of `MET-PASS-COMPLETED`, especially
`DQ-EVENT-TYPE-OBJECT`,
`DQ-CONDITIONAL-FIELD`, `DQ-EVENT-UUID-UNIQUE`, plus a denominator-consistency
test candidate under `DQ-ID-MISSING` and `DQ-ID-TYPE`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-PASS-001`, `EXP-THRESH-001`, and
  `EXP-SHRINK-001`.
- Open gates: eligibility taxonomy, minimum attempts, aggregation invariants,
  stability, and user-facing denominator display.

## Limitations

The rate reflects chosen pass risk, receiver context, team style, game state,
and provider outcomes. A high rate can result from conservative pass selection.

## References

- [Completed-passes definition](completed-passes.md)
- [Research dossier §§6.2, 7.1, and 24](../../research/research-dossier.md)
- [Experiment registry](../../research/metric-experiments.md)
- [Feature lineage: FEAT-PASS-COMPLETION-RATE](../../data/feature-lineage.md)

## Examples

Illustrative only: 72 completed passes from 80 eligible attempts yields 90%.
Nine completions from 10 attempts also yields 90%, but the displayed denominator
and sample warning distinguish the evidence.

## Changelog

- `0.1.0` — Initial proposed rate with explicit numerator and denominator.
