# Local snapshot coverage report

This report contains measured facts from the complete local snapshot. Recommendations are isolated in the final section.

## Audit metadata

| Item | Value |
|---|---|
| Audit UTC | `2026-07-24T19:52:53.244431+00:00` to `2026-07-24T20:16:10.316470+00:00` |
| Duration | 1,397.005 seconds |
| Dataset | `C:\Users\cocod\ScoutLabs\data\statsbomb-open-data\data` |
| Dataset content manifest SHA-256 | `676857cc079ceb4a0aa5369e01be762544dc76451720a9bb818e3d45eb5f09cb` |
| StatsBomb Open Data commit | `b0bc9f22dd77c206ddedc1d742893b3bbe64baec` |
| ScoutLabs commit at audit | `f2e655d88639d17d7feca6440147b6176e0e8c14` |
| Python | CPython 3.13.7 |
| Full audit command | `python -u reports/audit_snapshot.py --data-dir data/statsbomb-open-data/data --output reports/snapshot-audit.json --progress-every 100` |
| UTF-8 supplement | `2026-07-24T20:18:37.877069+00:00` to `2026-07-24T20:19:05.060931+00:00`; 8,977 files / 16,880,346,686 bytes; 0 strict-decoding errors |

Method: every physical JSON file was read one file at a time. The schema walker counted every container, item and leaf. Exact UUID partitions were used for global event uniqueness. Relationships were resolved inside each event file, and 360 UUIDs against the same-match event map. The UTF-8 result is a separate incremental 1 MiB strict-decoding audit.

### Physical and analytical universes

The physical universe is used for schema, raw field, ID and relationship observation. The analytical universe is keyed only by the 3,961 valid integer `match_id` records. Orphan records are never folded into competition-season or match-coverage denominators.

| Family | Physical files | Referenced by valid match | Orphan / unreferenced | Valid matches without physical file | Valid JSON |
|---|---:|---:|---:|---:|---:|
| events | 4,235 | 3,961 | 274 | 0 | 4,235 |
| lineups | 4,235 | 3,961 | 274 | 0 | 4,235 |
| three-sixty | 426 | 426 | 0 | 3,535 | 425 |

The one malformed file is `three-sixty/3845506.json`: `JSONDecodeError` at line 92,794, column 3 (character 2,637,824). It decoded as UTF-8 but was not valid JSON. No file was unreadable and every successfully parsed root was an array.

## Global snapshot

| Measure | Physical complete snapshot | Valid-match analytical universe |
|---|---:|---:|
| Competition IDs | 24 | same source catalogue |
| Competition-season records | 80 | 80 |
| Match records / unique valid IDs | 3,961 | 3,961 |
| Team IDs | 354 physical union | 354 lineup/match union |
| Player IDs | 11,889 physical lineup/event union | 11,794 valid-match lineup union |
| Lineup team records | 8,470 | 7,922 |
| Lineup player records | 161,958 | 152,133 |
| Event records | 14,874,171 | 13,911,986 |
| 360 parsed frames | 1,381,467 | 1,381,467 |
| Shot freeze-frame player records | 1,397,782 | not separately grouped |
| Observed JSON paths | 357 | schema uses physical universe |

The physical player union includes event actors and the 274 orphan lineup/event files. The analytical player figure is a reproducible lineup-ID union, not an appearance or minutes count.

### Identifier and duplicate checks

- Valid event UUIDs: 14,874,171; missing/invalid: 0; duplicate UUIDs or extra occurrences globally: 0.
- Duplicate match records: 0; duplicate competition-season records: 0; duplicate player IDs within one team lineup: 0.
- Stable team IDs with multiple observed labels: 7; stable player IDs with multiple observed labels: 42. These are label variations to preserve and review, not identifier collisions.

### Match metadata value distributions

- `data_version`: `1.0.2`: 100, `1.0.3`: 88, `1.1.0`: 3,771, `<missing>`: 2.
- `shot_fidelity_version`: `2`: 3,764, `<missing>`: 197.
- `xy_fidelity_version`: `2`: 3,718, `<missing>`: 243.
- Metadata objects: `empty_object`: 2, `nonempty_object`: 3,959.

These distributions were measured in a supplemental pass over the 80 small match files; the base schema audit only stored occurrence, type and one representative value.

### Exact lineup-team consistency supplement

- Valid matches checked: 3,961.
- Exact full home/away team-set matches: 3,961.
- Team-set mismatches: 0.
- Duplicate team entries: 0; missing expected: 0; unexpected: 0; invalid team IDs: 0.
- Valid matches without lineup file: 0.

## Competition-season coverage

All counts in this table use valid match IDs. Event and lineup file coverage require a parsed list root. 360 is optional and partial; its percentage is availability, not a completeness expectation. Approximate player counts are unions of lineup/event player IDs in that competition-season, not appearances.

| Competition ID | Season ID | Competition | Season | Gender | Match dates | Valid matches | Teams | Approx. players | Events | Event files | Lineup files | 360 files | 360 frames | Warnings |
|---:|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | 27 | Premier League | 2015/2016 | male | 2015-08-08–2016-05-17 | 380 | 20 | 644 | 1,313,773 | 380 (100.0%) | 380 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=380 |
| 2 | 44 | Premier League | 2003/2004 | male | 2003-08-16–2004-05-15 | 38 | 20 | 399 | 129,401 | 38 (100.0%) | 38 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=38 |
| 7 | 27 | Ligue 1 | 2015/2016 | male | 2015-08-07–2016-05-14 | 377 | 20 | 649 | 1,358,593 | 377 (100.0%) | 377 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=377 |
| 7 | 108 | Ligue 1 | 2021/2022 | male | 2021-08-29–2022-05-21 | 26 | 18 | 420 | 101,766 | 26 (100.0%) | 26 (100.0%) | 26 (100.0%) | 86,352 | — |
| 7 | 235 | Ligue 1 | 2022/2023 | male | 2022-08-06–2023-06-03 | 32 | 20 | 485 | 129,490 | 32 (100.0%) | 32 (100.0%) | 32 (100.0%) | 111,770 | — |
| 9 | 27 | 1. Bundesliga | 2015/2016 | male | 2015-08-15–2016-05-14 | 34 | 18 | 421 | 115,240 | 34 (100.0%) | 34 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=34 |
| 9 | 281 | 1. Bundesliga | 2023/2024 | male | 2023-08-19–2024-05-18 | 34 | 18 | 460 | 137,765 | 34 (100.0%) | 34 (100.0%) | 34 (100.0%) | 118,607 | — |
| 11 | 1 | La Liga | 2017/2018 | male | 2017-08-20–2018-05-20 | 36 | 20 | 441 | 136,538 | 36 (100.0%) | 36 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=36 |
| 11 | 2 | La Liga | 2016/2017 | male | 2016-08-20–2017-05-21 | 34 | 20 | 444 | 124,813 | 34 (100.0%) | 34 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=34 |
| 11 | 4 | La Liga | 2018/2019 | male | 2018-08-18–2019-05-19 | 34 | 20 | 441 | 131,702 | 34 (100.0%) | 34 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=34 |
| 11 | 21 | La Liga | 2009/2010 | male | 2009-09-12–2010-05-16 | 35 | 20 | 379 | 128,395 | 35 (100.0%) | 35 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=35 |
| 11 | 22 | La Liga | 2010/2011 | male | 2010-08-29–2011-05-11 | 33 | 20 | 398 | 130,899 | 33 (100.0%) | 33 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=33 |
| 11 | 23 | La Liga | 2011/2012 | male | 2011-08-29–2012-05-12 | 37 | 20 | 386 | 145,993 | 37 (100.0%) | 37 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=37 |
| 11 | 24 | La Liga | 2012/2013 | male | 2012-08-19–2013-05-12 | 32 | 20 | 364 | 130,457 | 32 (100.0%) | 32 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=32 |
| 11 | 25 | La Liga | 2013/2014 | male | 2013-08-18–2014-05-17 | 31 | 20 | 367 | 118,016 | 31 (100.0%) | 31 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=31 |
| 11 | 26 | La Liga | 2014/2015 | male | 2014-08-24–2015-05-23 | 38 | 20 | 433 | 142,957 | 38 (100.0%) | 38 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=38 |
| 11 | 27 | La Liga | 2015/2016 | male | 2015-08-21–2016-05-15 | 380 | 20 | 601 | 1,295,354 | 380 (100.0%) | 380 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=380 |
| 11 | 37 | La Liga | 2004/2005 | male | 2004-10-16–2005-05-01 | 7 | 7 | 113 | 22,204 | 7 (100.0%) | 7 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=7 |
| 11 | 38 | La Liga | 2005/2006 | male | 2005-10-01–2006-02-25 | 17 | 17 | 249 | 57,668 | 17 (100.0%) | 17 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=17 |
| 11 | 39 | La Liga | 2006/2007 | male | 2006-08-28–2007-06-17 | 26 | 20 | 328 | 92,656 | 26 (100.0%) | 26 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=26 |
| 11 | 40 | La Liga | 2007/2008 | male | 2007-08-26–2008-05-17 | 27 | 20 | 373 | 96,913 | 27 (100.0%) | 27 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=27 |
| 11 | 41 | La Liga | 2008/2009 | male | 2008-08-31–2009-05-10 | 31 | 19 | 353 | 107,089 | 31 (100.0%) | 31 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=31 |
| 11 | 42 | La Liga | 2019/2020 | male | 2019-09-21–2020-07-19 | 33 | 20 | 476 | 129,058 | 33 (100.0%) | 33 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=33 |
| 11 | 90 | La Liga | 2020/2021 | male | 2020-09-27–2021-05-16 | 35 | 19 | 516 | 139,030 | 35 (100.0%) | 35 (100.0%) | 35 (100.0%) | 128,840 | — |
| 11 | 278 | La Liga | 1973/1974 | male | 1974-02-17–1974-02-17 | 1 | 2 | 24 | 2,974 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 12 | 27 | Serie A | 2015/2016 | male | 2015-08-22–2016-05-15 | 380 | 20 | 699 | 1,353,739 | 380 (100.0%) | 380 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=380 |
| 12 | 86 | Serie A | 1986/1987 | male | 1986-11-09–1986-11-09 | 1 | 2 | 32 | 3,005 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 1 | Champions League | 2017/2018 | male | 2018-05-26–2018-05-26 | 1 | 2 | 36 | 3,497 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 2 | Champions League | 2016/2017 | male | 2017-06-03–2017-06-03 | 1 | 2 | 36 | 3,400 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 4 | Champions League | 2018/2019 | male | 2019-06-01–2019-06-01 | 1 | 2 | 46 | 3,165 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 21 | Champions League | 2009/2010 | male | 2010-05-22–2010-05-22 | 1 | 2 | 36 | 3,410 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 22 | Champions League | 2010/2011 | male | 2011-05-28–2011-05-28 | 1 | 2 | 36 | 4,326 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 23 | Champions League | 2011/2012 | male | 2012-05-19–2012-05-19 | 1 | 2 | 36 | 4,695 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 24 | Champions League | 2012/2013 | male | 2013-05-25–2013-05-25 | 1 | 2 | 36 | 3,338 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 25 | Champions League | 2013/2014 | male | 2014-05-24–2014-05-24 | 1 | 2 | 36 | 4,263 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 26 | Champions League | 2014/2015 | male | 2015-06-06–2015-06-06 | 1 | 2 | 36 | 3,433 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 27 | Champions League | 2015/2016 | male | 2016-05-28–2016-05-28 | 1 | 2 | 36 | 4,708 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 37 | Champions League | 2004/2005 | male | 2005-05-25–2005-05-25 | 1 | 2 | 28 | 4,648 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 39 | Champions League | 2006/2007 | male | 2007-05-23–2007-05-23 | 1 | 2 | 36 | 3,064 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 41 | Champions League | 2008/2009 | male | 2009-05-27–2009-05-27 | 1 | 2 | 36 | 3,329 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 44 | Champions League | 2003/2004 | male | 2004-05-26–2004-05-26 | 1 | 2 | 28 | 3,223 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 71 | Champions League | 1971/1972 | male | 1972-05-31–1972-05-31 | 1 | 2 | 24 | 3,027 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 76 | Champions League | 1999/2000 | male | 1999-11-23–1999-11-23 | 1 | 2 | 28 | 3,384 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 276 | Champions League | 1970/1971 | male | 1971-06-02–1971-06-02 | 1 | 2 | 24 | 3,529 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 16 | 277 | Champions League | 1972/1973 | male | 1973-05-30–1973-05-30 | 1 | 2 | 24 | 3,195 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 35 | 75 | UEFA Europa League | 1988/1989 | male | 1989-03-15–1989-05-03 | 3 | 4 | 60 | 10,086 | 3 (100.0%) | 3 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=3 |
| 37 | 4 | FA Women's Super League | 2018/2019 | female | 2018-09-09–2019-05-11 | 107 | 11 | 264 | 356,568 | 107 (100.0%) | 107 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=107 |
| 37 | 42 | FA Women's Super League | 2019/2020 | female | 2019-09-07–2020-02-23 | 87 | 12 | 280 | 292,253 | 87 (100.0%) | 87 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=87 |
| 37 | 90 | FA Women's Super League | 2020/2021 | female | 2020-09-05–2021-05-09 | 131 | 12 | 312 | 443,295 | 131 (100.0%) | 131 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=131 |
| 37 | 281 | FA Women's Super League | 2023/2024 | female | 2023-10-01–2024-05-18 | 132 | 12 | 336 | 495,189 | 132 (100.0%) | 132 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=132 |
| 43 | 3 | FIFA World Cup | 2018 | male | 2018-06-14–2018-07-15 | 64 | 32 | 736 | 227,825 | 64 (100.0%) | 64 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=64 |
| 43 | 51 | FIFA World Cup | 1974 | male | 1974-06-19–1974-07-07 | 6 | 6 | 132 | 19,259 | 6 (100.0%) | 6 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=6 |
| 43 | 54 | FIFA World Cup | 1986 | male | 1986-06-22–1986-06-29 | 3 | 4 | 88 | 8,471 | 3 (100.0%) | 3 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=3 |
| 43 | 55 | FIFA World Cup | 1990 | male | 1990-06-24–1990-06-24 | 1 | 2 | 44 | 3,140 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 43 | 106 | FIFA World Cup | 2022 | male | 2022-11-20–2022-12-18 | 64 | 32 | 829 | 234,637 | 64 (100.0%) | 64 (100.0%) | 64 (100.0%) | 203,882 | — |
| 43 | 269 | FIFA World Cup | 1958 | male | 1958-06-24–1958-06-29 | 2 | 3 | 66 | 7,341 | 2 (100.0%) | 2 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=2 |
| 43 | 270 | FIFA World Cup | 1962 | male | 1962-05-30–1962-05-30 | 1 | 2 | 44 | 3,754 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 43 | 272 | FIFA World Cup | 1970 | male | 1970-06-03–1970-06-21 | 6 | 7 | 154 | 20,030 | 6 (100.0%) | 6 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=6 |
| 44 | 107 | Major League Soccer | 2023 | male | 2023-08-27–2023-10-22 | 6 | 7 | 145 | 21,786 | 6 (100.0%) | 6 (100.0%) | 6 (100.0%) | 19,679 | — |
| 49 | 3 | NWSL | 2018 | female | 2018-04-15–2018-08-12 | 36 | 9 | 211 | 114,163 | 36 (100.0%) | 36 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=36 |
| 49 | 107 | NWSL | 2023 | female | 2023-03-25–2023-11-12 | 137 | 12 | 347 | 462,436 | 137 (100.0%) | 137 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=137 |
| 53 | 106 | UEFA Women's Euro | 2022 | female | 2022-07-06–2022-07-31 | 31 | 16 | 371 | 105,141 | 31 (100.0%) | 31 (100.0%) | 30 (96.774194%) | 90,850 | matches_without_360_files=1 |
| 53 | 315 | UEFA Women's Euro | 2025 | female | 2025-07-02–2025-07-27 | 31 | 16 | 369 | 105,658 | 31 (100.0%) | 31 (100.0%) | 31 (100.0%) | 90,559 | — |
| 55 | 43 | UEFA Euro | 2020 | male | 2021-06-11–2021-07-11 | 51 | 24 | 612 | 192,664 | 51 (100.0%) | 51 (100.0%) | 51 (100.0%) | 166,871 | — |
| 55 | 282 | UEFA Euro | 2024 | male | 2024-06-14–2024-07-14 | 51 | 24 | 621 | 187,924 | 51 (100.0%) | 51 (100.0%) | 51 (100.0%) | 164,530 | — |
| 72 | 30 | Women's World Cup | 2019 | female | 2019-06-07–2019-07-07 | 52 | 24 | 552 | 176,442 | 52 (100.0%) | 52 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=52 |
| 72 | 107 | Women's World Cup | 2023 | female | 2023-07-20–2023-08-20 | 64 | 32 | 736 | 226,118 | 64 (100.0%) | 64 (100.0%) | 64 (100.0%) | 199,526 | — |
| 81 | 48 | Liga Profesional | 1997/1998 | male | 1997-10-25–1997-10-25 | 1 | 2 | 28 | 3,572 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 81 | 275 | Liga Profesional | 1981 | male | 1981-04-10–1981-04-10 | 1 | 2 | 25 | 3,086 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 87 | 84 | Copa del Rey | 1983/1984 | male | 1984-05-05–1984-05-05 | 1 | 2 | 25 | 2,596 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 87 | 268 | Copa del Rey | 1982/1983 | male | 1983-06-04–1983-06-04 | 1 | 2 | 30 | 2,557 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 87 | 279 | Copa del Rey | 1977/1978 | male | 1978-04-19–1978-04-19 | 1 | 2 | 25 | 2,917 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 116 | 68 | North American League | 1977 | male | 1977-08-28–1977-08-28 | 1 | 2 | 25 | 3,205 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |
| 131 | 281 | Serie A Women | 2023/2024 | female | 2023-09-16–2024-05-19 | 130 | 10 | 298 | 432,487 | 130 (100.0%) | 130 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=130 |
| 135 | 281 | Frauen Bundesliga | 2023/2024 | female | 2023-09-15–2024-05-20 | 132 | 12 | 324 | 459,696 | 132 (100.0%) | 132 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=132 |
| 182 | 281 | Liga F | 2023/2024 | female | 2023-09-15–2024-06-16 | 240 | 16 | 456 | 835,429 | 240 (100.0%) | 240 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=240 |
| 223 | 282 | Copa America | 2024 | male | 2024-06-21–2024-07-15 | 32 | 16 | 412 | 100,324 | 32 (100.0%) | 32 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=32 |
| 1238 | 108 | Indian Super league | 2021/2022 | male | 2021-11-19–2022-03-20 | 115 | 11 | 313 | 344,667 | 115 (100.0%) | 115 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=115 |
| 1267 | 107 | African Cup of Nations | 2023 | male | 2024-01-13–2024-02-11 | 52 | 24 | 606 | 162,903 | 52 (100.0%) | 52 (100.0%) | 1 (1.923077%) | 1 | matches_without_360_files=51 |
| 1470 | 274 | FIFA U20 World Cup | 1979 | male | 1979-09-07–1979-09-07 | 1 | 2 | 36 | 3,245 | 1 (100.0%) | 1 (100.0%) | 0 (0.0%) | 0 | matches_without_360_files=1 |

## Event coverage

Counts distinguish all physical event files from valid-match events. Match and competition-season coverage are analytical and therefore cannot exceed 3,961 matches or 80 competition-seasons.

| Event type | Type ID | Physical events | Analytical events | % physical events | Valid-match coverage | Competition-season coverage |
|---|---:|---:|---:|---:|---:|---:|
| Pass | 30 | 4,103,274 | 3,836,550 | 27.586573% | 3,961 (100.000000%) | 80 (100.000000%) |
| Ball Receipt* | 42 | 3,844,731 | 3,589,099 | 25.848372% | 3,961 (100.000000%) | 80 (100.000000%) |
| Carry | 43 | 3,204,901 | 3,007,953 | 21.546754% | 3,961 (100.000000%) | 80 (100.000000%) |
| Pressure | 17 | 1,394,692 | 1,301,279 | 9.376603% | 3,961 (100.000000%) | 80 (100.000000%) |
| Ball Recovery | 2 | 461,777 | 433,698 | 3.104556% | 3,961 (100.000000%) | 80 (100.000000%) |
| Duel | 4 | 310,493 | 287,707 | 2.087464% | 3,961 (100.000000%) | 80 (100.000000%) |
| Clearance | 9 | 196,307 | 183,434 | 1.319784% | 3,961 (100.000000%) | 80 (100.000000%) |
| Block | 6 | 168,778 | 157,782 | 1.134705% | 3,961 (100.000000%) | 80 (100.000000%) |
| Dribble | 14 | 146,706 | 138,745 | 0.986314% | 3,961 (100.000000%) | 80 (100.000000%) |
| Goal Keeper | 23 | 132,406 | 123,920 | 0.890174% | 3,961 (100.000000%) | 80 (100.000000%) |
| Miscontrol | 38 | 126,292 | 118,271 | 0.849069% | 3,961 (100.000000%) | 80 (100.000000%) |
| Foul Committed | 22 | 117,584 | 108,845 | 0.790525% | 3,961 (100.000000%) | 80 (100.000000%) |
| Foul Won | 21 | 111,773 | 103,354 | 0.751457% | 3,961 (100.000000%) | 80 (100.000000%) |
| Dispossessed | 3 | 110,360 | 103,657 | 0.741957% | 3,961 (100.000000%) | 80 (100.000000%) |
| Shot | 16 | 108,281 | 101,227 | 0.727980% | 3,961 (100.000000%) | 80 (100.000000%) |
| Interception | 10 | 96,159 | 90,879 | 0.646483% | 3,961 (100.000000%) | 80 (100.000000%) |
| Dribbled Past | 39 | 90,743 | 85,864 | 0.610071% | 3,961 (100.000000%) | 80 (100.000000%) |
| Substitution | 19 | 28,044 | 26,481 | 0.188542% | 3,958 (99.924262%) | 78 (97.500000%) |
| Injury Stoppage | 40 | 18,172 | 17,200 | 0.122172% | 3,570 (90.128755%) | 74 (92.500000%) |
| Half End | 34 | 17,216 | 16,120 | 0.115744% | 3,961 (100.000000%) | 80 (100.000000%) |
| Half Start | 18 | 17,216 | 16,120 | 0.115744% | 3,961 (100.000000%) | 80 (100.000000%) |
| 50/50 | 33 | 15,889 | 14,549 | 0.106823% | 2,670 (67.407220%) | 68 (85.000000%) |
| Tactical Shift | 36 | 11,737 | 10,865 | 0.078909% | 3,579 (90.355971%) | 73 (91.250000%) |
| Starting XI | 35 | 8,470 | 7,922 | 0.056944% | 3,961 (100.000000%) | 80 (100.000000%) |
| Referee Ball-Drop | 41 | 6,265 | 5,977 | 0.042120% | 1,963 (49.558192%) | 61 (76.250000%) |
| Shield | 28 | 6,007 | 5,578 | 0.040385% | 2,894 (73.062358%) | 62 (77.500000%) |
| Player Off | 27 | 4,541 | 4,271 | 0.030529% | 2,326 (58.722545%) | 65 (81.250000%) |
| Player On | 26 | 4,500 | 4,230 | 0.030254% | 2,318 (58.520576%) | 65 (81.250000%) |
| Bad Behaviour | 24 | 2,987 | 2,816 | 0.020082% | 1,684 (42.514517%) | 64 (80.000000%) |
| Camera On | 5 | 2,588 | 2,571 | 0.017399% | 106 (2.676092%) | 3 (3.750000%) |
| Error | 37 | 2,256 | 2,158 | 0.015167% | 1,536 (38.778086%) | 60 (75.000000%) |
| Offside | 8 | 1,513 | 1,400 | 0.010172% | 1,166 (29.437011%) | 62 (77.500000%) |
| Camera off | 29 | 693 | 690 | 0.004659% | 106 (2.676092%) | 3 (3.750000%) |
| Own Goal Against | 20 | 410 | 387 | 0.002756% | 375 (9.467306%) | 43 (53.750000%) |
| Own Goal For | 25 | 410 | 387 | 0.002756% | 375 (9.467306%) | 43 (53.750000%) |

Rare locally observed event types (<10,000 physical records): Starting XI, Referee Ball-Drop, Shield, Player Off, Player On, Bad Behaviour, Camera On, Error, Offside, Camera off, Own Goal Against, Own Goal For.
All 35 event types listed by the bundled v1.1 specification were observed. Camera On and Camera off are documented as deprecated but remain present; there are no documented-only or observed-only event type names relative to that bundled list.

## Important conditional-field coverage

The denominator is the physical record count of the relevant event type, not all events. True-only booleans therefore measure tag prevalence, not conventional null completeness.

| Family | JSON path | Relevant records | Occurrence | Non-null | Coverage |
|---|---|---:|---:|---:|---:|
| Pass event | `events[].pass.end_location` | 4,103,274 | 4,103,274 | 4,103,274 | 100.000% |
| Pass event | `events[].pass.recipient` | 4,103,274 | 3,847,151 | 3,847,151 | 93.758% |
| Pass event | `events[].pass.outcome` | 4,103,274 | 925,619 | 925,619 | 22.558% |
| Pass event | `events[].pass.assisted_shot_id` | 4,103,274 | 75,700 | 75,700 | 1.845% |
| Carry event | `events[].carry.end_location` | 3,204,901 | 3,204,901 | 3,204,901 | 100.000% |
| Dribble event | `events[].dribble.outcome` | 146,706 | 146,706 | 146,706 | 100.000% |
| Shot event | `events[].shot.end_location` | 108,281 | 108,281 | 108,281 | 100.000% |
| Shot event | `events[].shot.statsbomb_xg` | 108,281 | 108,281 | 108,281 | 100.000% |
| Shot event | `events[].shot.freeze_frame` | 108,281 | 106,907 | 106,907 | 98.731% |
| Duel event | `events[].duel.outcome` | 310,493 | 165,906 | 165,906 | 53.433% |
| Interception event | `events[].interception.outcome` | 96,159 | 96,159 | 96,159 | 100.000% |
| Ball Recovery event | `events[].ball_recovery.recovery_failure` | 461,777 | 36,196 | 36,196 | 7.838% |
| Goal Keeper event | `events[].goalkeeper.type` | 132,406 | 132,406 | 132,406 | 100.000% |
| Goal Keeper event | `events[].goalkeeper.outcome` | 132,406 | 62,773 | 62,773 | 47.409% |
| Substitution event | `events[].substitution.replacement` | 28,044 | 28,044 | 28,044 | 100.000% |
| Starting XI / Tactical Shift event | `events[].tactics.lineup` | 20,207 | 20,207 | 20,207 | 100.000% |
| event | `events[].counterpress` | 2,190,561 | 486,800 | 486,800 | 22.223% |

`events[].counterpress` is flattened in local JSON. Its measured denominator combines Pressure, Dribbled Past, 50/50, Duel, Block, Interception, and non-offensive Foul Committed, matching the documented eligible families used by ScoutLabs. It is not divided by all 14.9 million events.

## Relationship coverage

| Check | Count |
|---|---:|
| Related-event references | 21,887,644 |
| Resolved related-event references | 21,887,644 |
| Unresolved related-event references | 0 |
| Passes with recipient | 3,847,151 |
| Recipients resolved to a match player | 3,847,151 |
| Pass assisted-shot links | 75,700 |
| Resolved pass assisted-shot links | 75,700 |
| Shot key-pass links | 75,700 |
| Resolved shot key-pass links | 75,700 |
| Substitutions with replacement | 28,044 |
| Replacement resolved to a match player | 28,044 |
| Shot → Goal Keeper provider edges | 108,281 |
| Goal Keeper → Shot provider edges | 108,281 |
| Dribble → Dribbled Past provider edges | 90,743 |
| Dribbled Past → Dribble provider edges | 90,743 |

Structural related-event resolution was 100.000000%. These are provider-supplied edges. Sequence adjacency that ScoutLabs may infer later is not a provider relationship and was not validated.

## Coordinate coverage

| JSON path | Observations | Shape-valid | Invalid shape | Non-numeric / non-finite | Outside strict 120×80 x/y | Dimensions |
|---|---:|---:|---:|---:|---:|---|
| `events[].carry.end_location` | 3,204,901 | 3,204,901 | 0 | 0 | 128 | 2D=3,204,901 |
| `events[].goalkeeper.end_location` | 69,494 | 69,494 | 0 | 0 | 0 | 2D=69,494 |
| `events[].location` | 14,757,858 | 14,757,858 | 0 | 0 | 381 | 2D=14,757,858 |
| `events[].pass.end_location` | 4,103,274 | 4,103,274 | 0 | 0 | 1,177 | 2D=4,103,274 |
| `events[].shot.end_location` | 108,281 | 108,281 | 0 | 0 | 0 | 2D=32,771, 3D=75,510 |
| `events[].shot.freeze_frame[].location` | 1,397,782 | 1,397,782 | 0 | 0 | 0 | 2D=1,397,782 |
| `three-sixty[].freeze_frame[].location` | 21,561,945 | 21,561,945 | 0 | 0 | 189,128 | 2D=21,561,945 |

All 45,203,535 coordinate arrays had numeric, finite 2D/3D shapes. The strict pitch-domain check found 190,814 out-of-range x/y arrays: 189,128 are 360 visible-player locations, whose official specification explicitly allows manually placed players outside the visible area and whose coordinates can extend beyond the pitch; 1,686 are event start/pass/carry coordinates. The audit reports rather than clips them. The third shot-height coordinate was not range-constrained.

## Shot freeze frames

- Shots with `freeze_frame`: 106,907; all were non-empty.
- Player records: 1,397,782.
- Teammate labels: true=484,463, false=913,319.

## 360 coverage and validation

- Physical files: 426; parsed list-root files: 425; malformed JSON files: 1.
- Parsed frames / unique frame event UUIDs: 1,381,467 / 1,381,467.
- Resolved event links: 1,357,627; unresolved: 23,840; resolution 98.274298%.
- Visible-player records: 21,561,945.
- Teammate flags: `false`: 10,843,872, `true`: 10,718,073.
- Actor flags: `false`: 20,180,452, `true`: 1,381,493.
- Keeper flags: `false`: 21,062,301, `true`: 499,644.
- Actor-count distribution per frame: `0`: 2, `1`: 1,381,437, `2`: 28.
- Keeper-count distribution per frame: `0`: 881,872, `1`: 499,565, `2`: 19, `3`: 3, `4`: 8.
- Frames with multiple actors: 28; frames with >1 keeper label on the same teammate/opponent side: 28; actor-not-teammate records: 0.
- Frames flagged as potentially inconsistent by those implemented label checks: 56.

No actor identity/team comparison against the linked event was performed. The scanner retained only the linked event type, and Open Data does not identify non-actor 360 players.

### Visible-area polygons

- Observed/non-empty: 1,381,467 / 1,381,467.
- Valid nonzero-area under implemented checks: 1,381,467.
- Empty: 0; invalid shape: 0; non-numeric: 0; non-finite: 0; out-of-range: 0; zero area: 0; consecutive duplicate vertex: 0.
- Separate explicit-closure supplement: 1,381,467 explicitly closed and 0 not explicitly closed across 1,381,467 parsed frames (2026-07-24T20:30:54.585104+00:00 to 2026-07-24T20:31:41.114421+00:00).

Validation required a flat even-length sequence with at least three vertices, numeric finite coordinates, strict pitch bounds, no consecutive duplicate vertices, and nonzero shoelace area. The raw sequence was treated as implicitly closed; first=last was not required. Self-intersection was not tested. These counters are separate checks and must not be treated as mutually exclusive. Explicit closure was measured separately after the base validator and was not a base admission requirement.

## Measured warnings

| Finding | Count | Interpretation |
|---|---:|---|
| Invalid JSON | 1 | One 360 file cannot enter frame-level analysis. |
| Orphan event / lineup files | 274 each | Excluded from the valid-match analytical universe. |
| Unresolved 360 links | 23,840 | Exclude from derived 360 features pending source review. |
| Strict coordinate-domain exceedances | 190,814 | Reported, not clipped; predominantly 360 player placements. |
| Potential 360 label anomalies | 56 | Limited to implemented multiplicity/flag consistency checks. |
| Duplicate match/event IDs | 0 | Exact checks completed. |
| Unresolved related-event references | 0 | Same-file UUID resolution completed. |

Event `index` and timestamp monotonicity, period-boundary semantics, minutes, Starting XI reconciliation and polygon self-intersection were not tested by this audit.

## Suitability assessment

| Use | Measured facts | Conservative recommendation |
|---|---|---|
| Direct metrics | Complete event files exist for all 3,961 valid matches; IDs and related edges resolve structurally. | Suitable for versioned direct-count experiments after event eligibility and quality rules are applied. |
| Per-90 metrics | Lineups cover every valid match and exact team sets match; final playing-time logic was not validated. | Do not publish per-90 values until EXP-MIN-001 validates period, dismissal, substitution and incomplete-video handling. |
| Sequence analysis | `index`, timestamp, possession and related-event fields are present. Ordering/monotonicity was not executed. | Suitable for planned sequence experiments, not validated sequence metrics. |
| Spatial maps | 45.2 million coordinate arrays were shape-valid; strict range exceptions are measured. | Suitable for event action maps with range policy. Event maps are not tracking heatmaps. |
| Player similarity | Broad event/lineup coverage exists across 80 competition-seasons. | Suitable for baseline research only after minutes, populations, scaling, redundancy and stability experiments. Similarity is not quality or transfer advice. |
| Goalkeeper analysis | Goal Keeper and Shot events, provider xG and provider relationships are present. | Suitable for taxonomy/link experiments; do not assume every shot has a goalkeeper pair. |
| xT research | Pass/carry start/end coordinates and outcomes are available. | Research-compatible; no ScoutLabs xT model is implemented or validated. |
| VAEP research | Actions, sequences and outcomes are available, but order/possession validation is incomplete. | Research-compatible after normalization and ordering gates; no production model claim. |
| 360 experiments | 1.38 million frames across 425 parsed files; 98.274298% links resolve; visibility is partial. | Restrict to explicitly usable linked frames and coverage-aware experiments. Frames are event-linked snapshots, not continuous tracking, and no proprietary commercial 360 metrics are present. |
