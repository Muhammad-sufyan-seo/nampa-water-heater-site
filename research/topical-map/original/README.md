# Original topical-map scripts — recovered, unmodified

These two files are preserved exactly as they were written earlier in this
project's session, with **zero edits**. Do not modify them — they are the
historical record, not a working tool. The annotated, maintained view of
this data lives one directory up in `research/topical-map/status.csv` and
`research/topical-map/annotate_status.py`.

## Provenance

A 300-page "topical authority map" for this site was built earlier in this
same Claude Code session (branch `claude/nampa-water-heater-audit-wuanxi`,
around 2026-09-22), at the owner's request, following the same methodology
previously used for two reference sites ("the basketball site," "Lancaster
Water Heater Pros," and "Harrisburg Water Heater Pros"). The deliverable
was an `.xlsx` workbook (`nampa-topical-authority-map.xlsx`) sent directly
to the owner — **it was never committed to this git repository**, and the
two Python scripts that generated it lived only in that session's
temporary scratchpad directory, which does not persist.

Later in the same session, after a context-window compaction, this
project's working memory of the map was lost, and the map was reported
(incorrectly) as never having existed. The owner corrected this and asked
for the map to be located rather than recreated. It was recovered by
searching this session's own raw JSONL transcript
(`~/.claude/projects/.../4d552465-9d76-53d7-ad8d-93187f6b86e5.jsonl`) for
the tool-call that originally wrote each file, and extracting that
tool-call's exact `content` field. Both recovered files were diffed
byte-for-byte against the original scratchpad copies before being
committed here, and confirmed identical.

## What's here

- `build_data.py` — the v2 base dataset (137 pages: the 31 pages live at
  the time, plus 106 proposed new pages across pools A–D, I).
- `build_data_v3.py` — imports `PAGES` from `build_data.py`, drops 3 rows
  found to duplicate each other in a prior pass, and adds pools A–J (the
  v3 expansion to 295 total rows — the session called this "the 300-page
  plan," rounding).

Run `python3 build_data_v3.py` from this directory for a quick summary
count (imports `build_data.py` via a relative `sys.path` insert, so it
must be run from here, or with this directory on `PYTHONPATH`). Each
row is a plain dict with fields including `url`, `title`, `intent`,
`cluster`, `tier`, `status` (`Existing` or `New`), `source_req` (does
this topic's claims need a primary source before publishing), `cannib`
(the original author's own cannibalization-risk estimate), and `why`.

## Known structural caveats (do not silently fix — they're part of the record)

- `build_data_v3.py` line ~243 has `"TPVALWE if False else TPVALVE"` —
  a leftover placeholder from a find-and-replace that was never cleaned
  up. It evaluates to `TPVALVE` either way, so the data is correct, but
  the dead branch is preserved as-is since this file is a historical
  artifact, not live code.
- Many `url` values use a `/resources/`, `/water-heater-parts/`, or
  `/glossary/` prefix proposing new hub sections that were never built —
  this site's actual convention (confirmed in `rules/content-seo-rules.md`
  §7, "flat file structure at root") keeps new pages flat at the root or
  under the existing `/common-issues/` hub. Every page actually published
  from this map so far has used a flat/existing-hub URL instead of the
  map's originally proposed nested path — see `status.csv`'s `published_url`
  column for the actual URL used versus the map's `url` column.
