# Model cards

Model cards document analytical methods that combine features or metrics. They
do not establish implementation or production approval.

## Contents

- [_template.md](_template.md) — required model-card fields.
- [Similarity baseline v0 proposal](similarity-baseline-v0-proposal.md) —
  `MOD-SIM-BASELINE-V0`, status `Proposal`.

No xT or VAEP model card exists because ScoutLabs has not implemented,
evaluated, or selected a specific xT or VAEP model version. Those methods remain
research experiments.

## Status and review

Allowed model statuses are `Proposal`, `Experimental`, `Candidate`,
`Production`, and `Deprecated`. Movement toward `Production` requires completed
mechanical validation, sensitivity analysis, football review, reproducibility
evidence, and product approval. A model card must retain the exact feature and
metric versions, source snapshot, comparison population, preprocessing,
missing-data policy, weights, and code artifact needed to reproduce a result.

See the [research methodology](../../research/research-methodology.md),
[similarity research plan](../../research/similarity-research.md), and
[experiment registry](../../research/metric-experiments.md).

