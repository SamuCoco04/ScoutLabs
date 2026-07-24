# Validation results

**Document status:** Structural snapshot audit integrated; event-order check remains planned
**Validation scope:** local StatsBomb Open Data snapshot
**Rule:** only executed checks with retained evidence may appear under Completed
validations.

This document separates the prior inventory baseline from validations completed by the
current audit. It does not validate football metrics, feature definitions, xT, VAEP,
spatial similarity, 360-derived features, or similarity models.

## Prior inventory baseline

The existing generated inventory at `reports/statsbomb_inventory.json` records:

- 80 competition-season records;
- 3,961 matches;
- 426 three-sixty files.

These three facts establish the baseline referenced by the
[research dossier](research-dossier.md). They are not substitutes for the full snapshot
audit below. File presence does not establish JSON validity, schema conformance,
relationship resolution, coordinate validity, 360 link resolution, or visible-area
usability.

## Authoritative validation IDs

This table reserves each identifier once.

| Validation ID | Object | Audit state |
|---|---|---|
| VAL-AUDIT-001 | Reproducibility metadata | Completed |
| VAL-FILE-001 | File-family coverage and orphans | Completed |
| VAL-JSON-001 | JSON, root, and encoding validity | Completed |
| VAL-SCHEMA-001 | Observed schema, event types, and field occurrences | Completed |
| VAL-ID-001 | Audited identifier presence and type | Completed |
| VAL-ID-002 | Match identifier uniqueness | Completed |
| VAL-ID-003 | Event UUID uniqueness | Completed |
| VAL-REL-001 | Related-event and structural link resolution | Completed |
| VAL-COORD-001 | Coordinate shapes and ranges | Completed |
| VAL-LINEUP-001 | Complete match-to-lineup team equality | Completed |
| VAL-360-001 | 360 event-link resolution | Completed |
| VAL-360-002 | Visible-area polygon validity | Completed |
| VAL-360-003 | 360 actor/goalkeeper label multiplicity and flags | Completed |

## Audit environment

| Field | Value |
|---|---|
| Audit timestamp (UTC) | 2026-07-24T19:52:53.244431Z to 2026-07-24T20:16:10.316470Z (1,397.005 seconds) |
| Dataset path | `C:\Users\cocod\ScoutLabs\data\statsbomb-open-data\data` |
| Dataset source commit | `b0bc9f22dd77c206ddedc1d742893b3bbe64baec` (`master`) |
| ScoutLabs commit | `f2e655d88639d17d7feca6440147b6176e0e8c14` (`docs/product-definition`; dirty documentation worktree captured in artifact) |
| Python version | CPython 3.13.7 |
| Audit command and script/version | `python -u reports/audit_snapshot.py --data-dir data/statsbomb-open-data/data --output reports/snapshot-audit.json --progress-every 100`; cwd `C:\Users\cocod\ScoutLabs`; executable `C:\Python313\python.exe`; audit schema `1.0.0` |
| Temporary audit-tool hashes | `audit_snapshot.py`: SHA-256 `433654F23605AAD67E59DEE7512377520BC8DECF99F19FF045F929606EA747D2`; `verify_utf8.py`: `3B7BA6C7D0B5D9D621D4BE03DA98B35FE7A4EDCA642604123895C19ECCC2A42F`; `verify_visible_area_closure.py`: `D702ECCCE6DAF23BCEF8B08FD2D59371987E143E6E66A620A25D6486A9BBCAFA`; `render_data_docs.py`: `1777A3BAE118AC202892C796AECF1179A0365F87C0F271F404AD675C97BF3F9C` |
| Retained audit artifact | `reports/snapshot-audit.json`; 577,584 bytes; SHA-256 `EE21EFF3F14FF4DA8CBE15ED35150427F255582D49466B3443DC2FEEEB4823F0` |
| Dataset content manifest | SHA-256 `676857cc079ceb4a0aa5369e01be762544dc76451720a9bb818e3d45eb5f09cb` |
| UTF-8 supplement | `python reports\verify_utf8.py data\statsbomb-open-data\data reports\utf8-audit.json` with `.venv-1\Scripts` prepended to `PATH`; `reports/utf8-audit.json`; 2026-07-24T20:18:37.877069Z to 2026-07-24T20:19:05.060931Z; SHA-256 `E8F45241CB80312C047A9F4079A7D2C341C2784586AC8CCBFF0E10D0142F057C` |
| Visible-area closure supplement | `python reports\verify_visible_area_closure.py data\statsbomb-open-data\data\three-sixty reports\visible-area-closure-audit.json` with `.venv-1\Scripts` prepended to `PATH`; 2026-07-24T20:30:54.585104Z to 2026-07-24T20:31:41.114421Z; artifact SHA-256 `5CD040727ECE260E2118A95B2DA6556D8CEB81D56845F0891302A7AD3E958607` |
| Match/lineup supplement | `python reports/render_data_docs.py`; cwd `C:\Users\cocod\ScoutLabs`; executable `C:\Python313\python.exe`; generated 2026-07-24T20:32:42.828293Z; `reports/snapshot-supplement.json`; artifact SHA-256 `977527C021ECE6230A75C69CDAAB9A0A88A545C8A0B38D4267534FA2086794AD` |
| Inventory command | `scoutlabs inventory --data-dir data/statsbomb-open-data/data` (final rerun pending) |
| Audit methodology | Every JSON file in competitions, matches, lineups, events, and three-sixty was read once, one file at a time. JSON path/type/occurrence statistics were collected recursively. Global event UUID uniqueness used exact 16-byte UUID partitions on disk. Relationships were resolved inside each event file; 360 UUIDs were resolved against the corresponding event file. |
| Known limitations | Event index/timestamp monotonicity was not executed. One malformed 360 file could not contribute frame/schema records. Provider-version values and complete home/away-to-lineup equality come from the retained supplement, not the base artifact. Temporary inspection scripts are deleted at handoff as required; their hashes, exact commands, methods, and generated artifacts remain, but their source is not versioned. |

## Completed validations

The records below are limited to checks explicitly executed by the retained artifacts.
`Fail` identifies a source-quality finding, not an audit-process failure.

| ID | Object | Method | Dataset scope | Expected result | Observed result | Pass/fail | Limitations | Linked DQ rules | Follow-up |
|---|---|---|---|---|---|---|---|---|---|
| `VAL-AUDIT-001` | Audit reproducibility metadata | Verify UTC bounds, duration, command/cwd/executable, dataset path, source and ScoutLabs commits, Python/audit versions, tool/artifact hashes, and dataset manifest | Retained audit artifacts and audited snapshot | Required provenance is present and every retained artifact is integrity-checkable | Audit ran with the command recorded above from `C:\Users\cocod\ScoutLabs`, 2026-07-24T19:52:53.244431Z–20:16:10.316470Z for 1,397.005 seconds on CPython 3.13.7; both commits, dirty-state evidence, audit schema 1.0.0, temporary-tool hashes, artifact hashes, and dataset manifest SHA-256 are present | Pass | The working tree was dirty by design. Exact argv is recorded here because it is not embedded in the base JSON. Temporary script source is deleted rather than versioned, so the retained method and hashes support traceability but not a bit-for-bit rerun from tracked files alone | `DQ-REPRODUCIBILITY` | Preserve retained JSON artifacts and this run record; implement permanent audited tooling before recurring validation |
| `VAL-FILE-001` | File-family coverage and orphans | Compare strict integer valid match IDs with physical integer-stem event, lineup, and three-sixty filenames | 3,961 valid match IDs; 4,235 event, 4,235 lineup, and 426 three-sixty files | Every valid match has event/lineup files, and no physical family file is orphaned; 360 absence is measured coverage | Event and lineup coverage is 3,961/3,961 with zero missing files, but each family has 274 orphan files among 4,235 physical files; all 426 three-sixty files reference valid matches and 3,535 valid matches have no 360 file; zero invalid filename stems | Fail | A missing 360 file is coverage, not a source error unless availability was claimed; file presence does not establish readable content | `DQ-FILE-MISSING`, `DQ-FILE-ORPHAN` | Keep orphan event/lineup files outside the 3,961-match analytical universe and investigate their missing match metadata |
| `VAL-JSON-001` | UTF-8, JSON syntax, and root type | Read and parse all source JSON; separately strict-decode all bytes incrementally in 1 MiB chunks | 8,977 files totaling 16,880,346,686 bytes across all five families | Every file is strict UTF-8, valid JSON, and has the expected array root | UTF-8 supplement: 8,977/8,977 files and all bytes decoded with zero errors. JSON parse: 8,976 valid, one invalid, zero unreadable, and zero unexpected roots. `three-sixty/3845506.json` fails with a missing comma at line 92,794, column 3 | Fail | The malformed file contributes to the content manifest but not frame, schema, coordinate, relationship, or label counts | `DQ-JSON-MALFORMED`, `DQ-JSON-ROOT`, `DQ-ENCODING` | Quarantine the malformed file analytically; do not repair or modify provider data |
| `VAL-SCHEMA-001` | Observed paths, types, occurrences, event types, and match metadata versions | Recursively scan readable JSON for path/type/occurrence and event-family conditional counts; group provider metadata child values over valid matches in the retained supplement | 8,976 readable files, 14,874,171 physical-file events, and all 3,961 valid match records | Every observed path/type and event type is enumerated and provider-version values are grouped reproducibly | 357 observed JSON paths and 35 observed event types were extracted; 13,911,986 events belong to the valid universe. Match `data_version`: 1.1.0=3,771, 1.0.2=100, 1.0.3=88, missing=2; `shot_fidelity_version`: 2=3,764, missing=197; `xy_fidelity_version`: 2=3,718, missing=243 | Pass | This validates observed schema and version distributions, not documented-but-unobserved fields/event types or compatibility effects; the malformed 360 file is absent from nested counts | `DQ-CONDITIONAL-FIELD`, `DQ-EVENT-TYPE-OBJECT`, `DQ-PROVIDER-VERSION` | Reconcile observed paths with official specifications and assess whether missing/mixed provider versions affect candidate features |
| `VAL-ID-001` | Audited identifier presence and type | Apply strict non-boolean integer checks to competition/season and match IDs, validate event/360 UUID strings without coercion, and count non-null invalid team/player ID types | 80 competition-season records, 3,961 match records, 14,874,171 events, and 1,381,467 parsed 360 frames | No audited identity key is missing or invalid | Zero invalid competition-season IDs and zero invalid match IDs; all 14,874,171 event IDs are present, canonical valid UUIDs; all 1,381,467 parsed 360 event UUID values are valid; zero non-null invalid team/player ID types were counted | Pass | Missing team/player keys were not exhaustively tested as required identifiers; the malformed 360 file was not parsed; validation is limited to identifiers explicitly audited | `DQ-ID-MISSING`, `DQ-ID-TYPE` | Extend family-specific required-ID presence checks before normalized ingestion |
| `VAL-ID-002` | Global valid `match_id` uniqueness | Build a global frequency set over strict integer, non-boolean match IDs | All 3,961 match records | Every valid match ID occurs once | 3,961 valid records produced 3,961 unique valid match IDs; zero duplicate records | Pass | Invalid IDs would be excluded before uniqueness, but none were observed | `DQ-MATCH-ID-UNIQUE` | Retain the same strict criterion in every match counter and join |
| `VAL-ID-003` | Event UUID uniqueness | Partition canonical UUIDs by first byte and compare exact 16-byte UUID values per file and globally | All 14,874,171 readable event records | Every event UUID is unique within and across files | Zero within-file duplicates, zero global duplicate UUIDs, and zero duplicate occurrences | Pass | Uniqueness does not validate event semantics or links; all 274 orphan event files are included in the global check | `DQ-EVENT-UUID-UNIQUE` | Preserve exact UUID uniqueness validation in future snapshots |
| `VAL-REL-001` | Related-event and structural pass/shot link resolution | Resolve `related_events[]` inside each event file and type-check pass-assisted-shot and shot-key-pass UUID targets | All 4,235 readable event files | Every audited reference resolves to the required same-file event/type | All 21,887,644 related-event references resolved (100%); all 75,700 pass-assisted-shot links resolved to Shot and all 75,700 shot-key-pass links resolved to Pass; recipient and substitution replacement resolution counts were also retained | Pass | Structural resolution does not prove causal attribution, expected reciprocity, or complete shot-to-goalkeeper semantics | `DQ-REL-UNRESOLVED`, `DQ-PASS-SHOT-LINK` | Review semantic edge cases in `EXP-XA-001`, `EXP-LOSS-001`, and `EXP-GK-001` |
| `VAL-COORD-001` | Coordinate shapes and ranges | Validate context-specific location shapes, numeric finiteness, and x/y against `[0,120]`/`[0,80]` | 45,203,535 observed event, shot-freeze-frame, and parsed 360 coordinates | Every coordinate has a valid shape/type and lies in the provider x/y domain | All 45,203,535 shapes are numeric and finite, with zero invalid shapes; 190,814 x/y values are out of range: 189,128 360 freeze-frame locations, 1,177 pass end locations, 381 event start locations, and 128 carry end locations | Fail | Shot z was shape/type checked but was not range constrained; polygons are separate; the malformed 360 file was not parsed | `DQ-COORD-SHAPE`, `DQ-COORD-RANGE` | Exclude out-of-range geometry from spatial derivations while retaining non-spatial event facts |
| `VAL-LINEUP-001` | Complete match-to-lineup team equality | Read all 80 match and 4,235 lineup files; for each valid match compare the complete lineup-root `team_id` list with its home/away set and count duplicate, missing, unexpected, invalid, and absent entries | All 3,961 valid matches and their 3,961 referenced lineup files | Every valid match has exactly the two expected distinct lineup teams | 3,961/3,961 matches have the exact team set; zero mismatches, missing expected teams, unexpected teams, duplicate entries, invalid team IDs, or absent lineup files | Pass | The 274 orphan lineup files are outside the valid-match universe; this check does not validate player membership, Starting XI, substitutions, dismissals, positions, or minutes | `DQ-LINEUP-CONSISTENCY` | Use the validated team attribution as a prerequisite, then resolve timeline edge cases in `EXP-MIN-001` |
| `VAL-360-001` | 360-to-event UUID resolution | Resolve each parsed 360 `event_uuid` against the corresponding match event file without cross-match fallback | 1,381,467 frames from 425 readable three-sixty files | Every valid 360 UUID resolves to exactly one same-match event | 1,357,627 links resolved and 23,840 did not; resolution is 98.274298%; all 1,381,467 frame UUID values are valid and unique | Fail | `three-sixty/3845506.json` is malformed and contributes no frames; a resolved link does not establish frame or polygon usability | `DQ-360-LINK-UNRESOLVED` | Exclude unresolved frames from 360 derivations and investigate the affected match/event coverage |
| `VAL-360-002` | Visible-area polygon validity | Base audit: validate even coordinate lists with at least three vertices, numeric finite in-range values, no repeated consecutive vertices, and non-zero shoelace area. Retained supplement: compare each first coordinate pair with the final pair as required by the documented explicit-closure format | 1,381,467 observed `visible_area` values from all 425 readable 360 files | Every observed polygon passes the executed geometric checks and repeats its first vertex at the end | All 1,381,467 are non-empty, explicitly closed, valid non-zero-area polygons; zero missing, empty, invalid-shape, non-numeric, non-finite, out-of-range, repeated-consecutive-vertex, unclosed, or zero-area cases | Pass | The malformed 360 file was not parsed; the audit did not test self-intersection, repair geometry, or establish feature-specific visible coverage | `DQ-VISIBLE-AREA-POLYGON` | Define feature-specific usable visibility in `EXP-360-001`; do not equate geometric validity with analytical usability |
| `VAL-360-003` | 360 actor/goalkeeper label multiplicity and flags | Count actor/keeper multiplicity, missing/invalid flags, `actor_not_teammate`, and more than one keeper per teammate/opponent side | 1,381,467 parsed frames and 21,561,945 visible-player records | Every frame has one actor, no executed flag anomaly, and at most one keeper per side | Two frames have zero actors, 28 have two actors, and 28 have more than one keeper on a side; 56 frames are flagged potentially inconsistent. All visible-player flags are boolean and `actor_not_teammate` is zero | Fail | The 56 summary excludes the two zero-actor frames; the audit did not compare actor identity/team with the linked event; non-actor identity is unavailable | `DQ-360-ACTOR`, `DQ-360-KEEPER-LABEL`, `DQ-360-COVERAGE` | Exclude unusable actor-relative frames and quantify feature-specific bias in `EXP-360-001` and `EXP-360-002` |

## Planned validation checks

Planned checks do not receive a `VAL-` identifier until they are completed. `Not run`
is not a failed observation.

| Check | Object | Method | Dataset scope | Expected result | Observed result | Pass/fail | Limitations | Linked DQ rules | Follow-up |
|---|---|---|---|---|---|---|---|---|---|
| Unassigned | Event index and timestamp order | Check index presence/type/uniqueness/strict file-order increase, then parse and compare timestamps within period with a documented simultaneous-event policy | Every readable event file | Index anomalies and timestamp regressions are enumerated | Not run | Not assessed | The snapshot audit extracted values but did not execute monotonicity or ordering checks | `DQ-EVENT-INDEX-ORDER`, `DQ-EVENT-TIMESTAMP-ORDER` | Implement and retain an order audit before time-window, minutes, or sequence validation |

## Planned football and model validation

The following work intentionally remains outside Completed validations:

- playing-time reconstruction and edge cases: `EXP-MIN-001`;
- pass, progression, entry, xA, loss, sequence, defending, and goalkeeper definitions:
  Priority 1 in [metric experiments](metric-experiments.md);
- scaling, missingness, distance, stability, same-player seasons, controls, and expert
  review: `EXP-SCALE-001` through `EXP-SIM-003`;
- xT and VAEP: `EXP-XT-001`, `EXP-VAEP-001`;
- spatial and 360 features: `EXP-SPATIAL-001`, `EXP-SPATIAL-002`,
  `EXP-360-001`, `EXP-360-002`;
- goalkeeper similarity: `EXP-GK-002`.

No football metric, feature transformation, or model is validated by a schema/coverage
audit alone.

## Integration checklist

Before moving a planned record to Completed:

1. paste exact observed counts from the retained audit artifact;
2. record the audit command, version, UTC timestamp, Python version, and both commits;
3. state `Pass` or `Fail` against the predeclared expected result;
4. retain warnings and representative failure paths without modifying source data;
5. link the applicable `DQ-` rules and data documentation;
6. ensure no experimental or football-validity conclusion is inferred from structural
   success;
7. obtain reviewer sign-off.
