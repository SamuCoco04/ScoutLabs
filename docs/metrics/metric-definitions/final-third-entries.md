# Final-third entries

| Field | Value |
|---|---|
| Metric ID | `MET-PROG-FINAL-THIRD-ENTRIES` |
| Name | Final-third entries |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts eligible passes and carries that move the ball from outside into the
attacking third. It describes a transparent route into advanced territory.

## Intended use

Progression totals/per 90, pass/carry splits, entry maps, Player Profile, Player
Explorer, Metric Leaders, Compare, and candidate similarity after redundancy
testing.

## Prohibited interpretation

An entry is not a chance, line break, successful reception, retained possession,
or action value. It is event-derived geometry, not a provider flag.

## Source fields

- `SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`, and
  `SRC-EVENT-BASE-TEAM-ID`.
- `SRC-EVENT-BASE-LOCATION`.
- `SRC-PASS-END-LOCATION` and `SRC-PASS-OUTCOME-ID`.
- `SRC-CARRY-END-LOCATION`.

## Prerequisites

`FEAT-FINAL-THIRD-ENTRY`, `FEAT-PASS-COMPLETED`; valid direction-normalized
coordinates; canonical 120×80 pitch; event/action subtype retained.

## Formal definition

For normalized point \(q=(x,y)\), define
\(\text{FinalThird}(q)=I(x\ge80)\). For eligible completed passes and carries:

\[
FTE(e)=I(x_{\text{start}}<80 \land x_{\text{end}}\ge80)
\]

\[
FTE_{p,t,s}=\sum_e FTE(e)
\]

Version 0.1 proposes action-end geometry. `EXP-ENTRY-001` compares this with a
stricter next-teammate-touch/retention rule. Pass and carry components are
stored separately even when a combined total is shown.

## Calculation steps

1. Select valid Carry events and completed, eligible Pass events.
2. Validate and normalize start/end coordinates.
3. Require the start outside and end inside the final third.
4. Count one entry per recorded action and preserve action type.
5. Aggregate pass, carry, and combined totals; retain minutes and spatial
   eligibility.

## Numerator

Eligible outside-to-inside final-third actions.

## Denominator

None for count/per 90. Entry share per eligible ball movement is a separate
rate.

## Unit

Entries; optional per 90.

## Normalization

Expose total, pass/carry split, and per 90. Percentiles require the same zone and
eligibility versions and a named comparison group.

## Comparison group

Position-compatible player–team–season profiles with the same competition and
season scope, zone definition, minutes rule, and source coverage.

## Sample requirements

No validated universal threshold. Show minutes, eligible passes/carries, and
entries; test threshold and stability through `EXP-ENTRY-001` and
`EXP-THRESH-001`.

## Edge cases

- An action starting on x=80 is already inside and is not an entry.
- An action ending on x=80 is inside under this boundary convention.
- An incomplete pass is excluded even if its intended endpoint is inside.
- A carry and a later pass are distinct entries only if each independently
  crosses from outside; actions beginning inside do not add repeated entries.
- Restart types can be retained as splits; any exclusion must be versioned.
- An action can count as both a final-third and penalty-area entry; the metrics
  answer different zone questions and must not be summed.

## Missing-data handling

Exclude an action with invalid/missing start or end from both count and spatial
eligibility; report coverage. Missing files or coordinates do not become zero.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-TYPE-OBJECT`,
`DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, and
`DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-ENTRY-001`, `EXP-REDUND-001`, and
  `EXP-THRESH-001`.
- Open gates: next-touch alternative, set-piece policy, boundary fixtures,
  direction normalization, retention interpretation, and sample stability.

## Limitations

The metric measures recorded transport into a fixed zone. It does not encode
opponents, pressure, team opportunity, pass value, or what happened next.

## References

- [Research dossier §§7.5, 8.2, and 24](../../research/research-dossier.md)
- [Experiment registry: EXP-ENTRY-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-FINAL-THIRD-ENTRY](../../data/feature-lineage.md)

## Examples

Illustrative only: a completed pass from x=75 to x=84 is one entry. A pass from
x=82 to x=100 is not, because it began inside. An incomplete pass from x=75
toward x=84 is not counted.

## Changelog

- `0.1.0` — Initial outside-to-inside geometric proposal.
