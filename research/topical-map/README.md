# Nampa topical map — recovered archive

This directory exists so the topical map built earlier in this project
cannot be lost again the way it was once already (recovered 2026-10-19
from this session's own transcript after a context-compaction cycle
caused it to be reported, incorrectly, as never having existed).

- **`original/`** — the two Python scripts that generated the map, restored
  byte-for-byte from the session transcript. **Do not edit these.** See
  `original/README.md` for full provenance and known caveats.
- **`annotate_status.py`** — reads `original/`, classifies every one of the
  295 rows (published / existing / rejected / source-blocked / not yet
  evaluated), and writes `status.csv`. Re-run it after any future batch
  that touches one of these topics, updating the hand-curated dicts near
  the top of the file as you go.
- **`status.csv`** — the output of the above: one row per map entry, with
  a `status` and `reason`. This is the file to consult before proposing a
  new page from this map.
- **`site-inventory.md`** — a separate, complementary view: every one of
  the site's 48 actually-live URLs as of 2026-10-19, with its provenance
  (pre-existing, built outside the map, or published from this map). Not
  every live page traces to a map row — the October 5 batch and the
  October 6 dip-tube page were built before this map was reconciled
  against the live site.

## Status summary (295 map rows, 2026-10-19)

| Status | Count | Meaning |
|---|---:|---|
| `not_yet_evaluated` | 173 | Map says no source needed, but not individually checked against live-page text this round. Unscreened, not pre-approved. |
| `source_blocked` | 38 | Map says a primary source is required; none obtained. Needs a new owner-supplied document — this environment cannot fetch one itself. |
| `existing` | 31 | Already live when the map was built. |
| `rejected_category` | 30 | Falls under a whole category the owner has explicitly rejected (brands, emergency shutoff/CO, short-cycling, insulation blankets, warranty, or — by this annotation's own added consistency rule — T&P valve safety). |
| `published` | 9 | Live, from the October 19 batch. |
| `rejected_duplicate` | 9 | Individually checked against a live page's actual text and found to substantially duplicate it. |
| `considered_not_selected` | 6 | Looked at, flagged as weaker or needing careful scoping, but not confirmed duplicate — still a legitimate future candidate. |

The large `not_yet_evaluated` bucket is the honest state of things: most of
the map's 264 proposed-new rows have never been read against this site's
actual, current page text. Treat that bucket as where a future batch's
candidates should be drawn from — after the same per-row duplication check
this project has applied to every row it has actually published.
