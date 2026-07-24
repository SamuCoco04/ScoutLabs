# Penalty-area entries

| Field | Value |
|---|---|
| Metric ID | `MET-PROG-PENALTY-AREA-ENTRIES` |
| Name | Penalty-area entries |
| Status | Proposed |
| Version | `0.1.0` |
| Owner | ScoutLabs research |

## Football interpretation

Counts eligible completed passes and carries that move the ball from outside
into the opponent penalty area.

## Intended use

Advanced progression and creation context, pass/carry splits, entry maps,
Player Profile, Player Explorer, Metric Leaders, Compare, and similarity
research.

## Prohibited interpretation

An entry is not necessarily a box touch, reception, chance, successful attack,
cross, line break, or pass value. It cannot be interpreted as continuous box
occupation.

## Source fields

`SRC-EVENT-BASE-TYPE-ID`, `SRC-EVENT-BASE-PLAYER-ID`,
`SRC-EVENT-BASE-TEAM-ID`, `SRC-EVENT-BASE-LOCATION`,
`SRC-PASS-END-LOCATION`, `SRC-PASS-OUTCOME-ID`, and
`SRC-CARRY-END-LOCATION`.

## Prerequisites

`FEAT-PENALTY-AREA-ENTRY`, `FEAT-PASS-COMPLETED`; valid
direction-normalized coordinates and versioned 120×80 pitch geometry.

## Formal definition

For normalized point \(q=(x,y)\), the proposed StatsBomb-coordinate box is:

\[
\text{Box}(q)=I(x\ge102 \land 18\le y\le62)
\]

For an eligible completed pass or carry:

\[
PAE(e)=I(\neg\text{Box}(s_e)\land\text{Box}(z_e))
\]

\[
PAE_{p,t,s}=\sum_e PAE(e)
\]

`EXP-ENTRY-001` compares action-end geometry with a next-teammate-touch or
short-retention requirement. The pitch-zone version must be retained.

## Calculation steps

1. Select valid carries and completed, eligible passes.
2. Validate and normalize start/end coordinates.
3. Apply the versioned box predicate to both points.
4. Require outside-to-inside transition; count once by action.
5. retain pass/carry splits, restart context, minutes, and eligible spatial
   action count.

## Numerator

Eligible actions crossing from outside to inside the opponent penalty area.

## Denominator

None for count/per 90. A share of eligible ball movements is a separate metric.

## Unit

Penalty-area entries; optional per 90.

## Normalization

Expose total, pass/carry split, and per 90 from validated seconds. Comparison
transforms require identical zone and eligibility versions.

## Comparison group

Position-compatible player–team–season profiles with named competitions,
seasons, minute rule, and pitch/eligibility versions.

## Sample requirements

No validated threshold. Show minutes, eligible movements, and entry count; test
stability and thresholds through `EXP-ENTRY-001` and `EXP-THRESH-001`.

## Edge cases

- Boundary points x=102, y=18, and y=62 are inside in this proposal.
- An action starting anywhere inside the box is not an entry.
- Incomplete intended deliveries are excluded.
- Restarts and crosses are retained as attributes; any open-play-only variant
  requires a separate version/name.
- An entry can also be a final-third entry when it starts before x=80; this is
  legitimate overlap, not two actions.
- End coordinates record the provider action endpoint, not guaranteed possession
  retention or a receiver’s exact touch.

## Missing-data handling

Invalid/missing coordinates or completion evidence make the action ineligible
and generate coverage reporting. Do not infer the box from textual event labels.

## Quality dependencies

`DQ-ID-MISSING`, `DQ-ID-TYPE`, `DQ-EVENT-TYPE-OBJECT`,
`DQ-CONDITIONAL-FIELD`, `DQ-COORD-SHAPE`, `DQ-COORD-RANGE`, and
`DQ-INCOMPLETE-VIDEO`.

## Validation

- Completed `VAL-` evidence: None.
- Planned experiments: `EXP-ENTRY-001`, `EXP-REDUND-001`, and
  `EXP-THRESH-001`.
- Open gates: exact zone/boundary fixtures, next-touch alternative, restarts,
  direction, overlap/redundancy, and sample stability.

## Limitations

Fixed geometry does not measure defensive structure, target availability,
pressure, action difficulty, or downstream chance quality.

## References

- [Research dossier §§7.5, 8.2, and 24](../../research/research-dossier.md)
- [Experiment registry: EXP-ENTRY-001](../../research/metric-experiments.md)
- [Feature lineage: FEAT-PENALTY-AREA-ENTRY](../../data/feature-lineage.md)

## Examples

Illustrative only: a completed pass from (96, 40) to (104, 42) is one proposed
entry; a pass from (104, 42) to (110, 40) is not an entry because it starts
inside.

## Changelog

- `0.1.0` — Initial outside-to-inside 120×80 box proposal.
