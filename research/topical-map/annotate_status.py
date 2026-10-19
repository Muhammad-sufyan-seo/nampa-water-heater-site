#!/usr/bin/env python3
"""
Build research/topical-map/status.csv: every row of the recovered 295-row
topical map (original/build_data.py + build_data_v3.py), annotated with a
publication status and reason.

This is an honest reconciliation, not a claim that all 295 rows were
individually re-vetted against live page content. Status categories:

  published           -- built and live; published_url is the actual URL
                         used (often adapted from the map's proposed url
                         to match this site's actual flat/common-issues
                         convention rather than the map's proposed
                         /resources//water-heater-parts//glossary hubs,
                         which were never built).
  existing            -- one of the 31 pages already live when the map
                         was built (map status "Existing").
  rejected_category    -- excluded as a whole previously-rejected topic
                         category (brand pages, emergency shutoff/CO,
                         short-cycling, insulation blankets, warranty),
                         regardless of this specific row's own metadata.
  rejected_duplicate   -- individually checked against a live page's
                         actual text (not just title/metadata) during the
                         Oct 19 selection pass, and found to substantially
                         duplicate it. Reason names the live page.
  considered_not_selected -- looked at during the Oct 19 pass, flagged as
                         weaker/thinner/needing careful scoping, but NOT
                         confirmed as a duplicate or otherwise blocked.
                         Still a legitimate future candidate.
  source_blocked       -- the map's own source_req is "Yes" (a primary
                         source is needed before publishing) and this row
                         wasn't otherwise categorized above. No manufacturer
                         document was available for ANY of these in this
                         project as of this annotation; this environment's
                         total egress block (every external fetch attempt
                         returns EGRESS_BLOCKED, confirmed repeatedly and
                         exhaustively across this project) means none can
                         be resolved without a new owner-supplied document.
  not_yet_evaluated    -- the remaining majority of rows. source_req is
                         "No" in the map (the original author judged no
                         primary source necessary), but this annotation
                         pass did not individually read live-page content
                         to confirm non-duplication for every one of these.
                         Treat as an unscreened candidate pool for a future
                         batch, not as pre-approved.

Run: python3 research/topical-map/annotate_status.py
Writes: research/topical-map/status.csv
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'original'))
from build_data_v3 import PAGES  # noqa: E402

OUT_CSV = os.path.join(HERE, 'status.csv')

# ---------------------------------------------------------------------------
# Published this project (Oct 5 / Oct 6 / Oct 19 batches), mapped from the
# map's proposed url to the actual published URL. Not every published page
# originated as a specific map row with matching intent — where one does,
# it's listed by its map url; where a published page has no map-row
# counterpart (most of the Oct 5 batch, which predates the map being
# reconciled against), it's listed in site-inventory.md instead, not here.
# ---------------------------------------------------------------------------
PUBLISHED = {
    # map url                                                    : published url (actual)
    '/resources/flushing-vs-descaling': '/flushing-vs-descaling-nampa-id',
    '/common-issues/tankless-water-heater-goes-cold-mid-shower':
        '/common-issues/tankless-water-heater-goes-cold-mid-shower-nampa-id',
    '/common-issues/water-heater-shuts-off-randomly':
        '/common-issues/water-heater-shuts-off-randomly-nampa-id',
    '/common-issues/no-hot-water-one-fixture': '/common-issues/no-hot-water-one-fixture-nampa-id',
    '/common-issues/low-hot-water-pressure': '/common-issues/low-hot-water-pressure-nampa-id',
    '/common-issues/burner-wont-ignite': '/common-issues/water-heater-burner-wont-ignite-nampa-id',
}

# A few published topics came from the v2 base list (build_data.py, ids
# NEW-0xx) rather than a v3 Pool, and from a row this annotation adds by
# hand (hot-and-cold-water-reversed has no map row at all — see below).
PUBLISHED_BY_ID = {
    'NEW-028': '/common-issues/water-heater-condensation-nampa-id',
    'NEW-030': '/common-issues/water-heater-burning-smell-nampa-id',
}

# No map row (v2 or v3) actually proposes "hot and cold water reversed at
# the tap" — it was identified independently during the Oct 19 gap
# analysis as a genuinely uncovered intent, not sourced from the map.
NO_MAP_ROW_PUBLISHED = [
    {
        'id': '(none — not a map row)',
        'url': '/common-issues/hot-and-cold-water-reversed-nampa-id',
        'title': 'Hot and Cold Water Reversed at the Tap',
        'status': 'published',
        'reason': 'Identified during Oct 19 gap analysis, not present in the recovered map '
                   'under any id; a plumbing cross-connection, genuinely novel intent.',
        'published_url': '/common-issues/hot-and-cold-water-reversed-nampa-id',
    }
]

# Rows individually checked against live-page TEXT during the Oct 19
# selection pass and found to substantially duplicate it. Keyed by map id.
REJECTED_DUPLICATE = {
    'A-004': 'Substantially covered by water-heater-dip-tube-failure-nampa-id\'s '
             '"high demand periods" / "undersized unit" causes and by '
             'no-hot-water-nampa-id\'s failed-lower-element distinction.',
    'A-010': 'water-heater-making-noise-nampa-id already has a "Banging or Knocking '
              '(Water Hammer)" cause bullet covering this exact symptom.',
    'A-013': 'Substantially covered by no-hot-water-nampa-id\'s "failed lower element... '
              'hot water run out quickly" distinction and dip-tube-failure\'s causes list.',
    'NEW-021': 'Substantially covered by the same no-hot-water-nampa-id lower-element '
               'distinction and dip-tube-failure\'s causes list as A-004/A-013.',
    'NEW-022': 'Direct duplicate of the already-live common-issues/water-heater-rotten-egg-'
               'smell-nampa-id page (published Oct 5, after this map row was written).',
    'NEW-023': 'Would need manufacturer-specific, model-specific error-code tables - same '
               'blocked category as the dropped /brands pages; thin/unsupportable without them.',
    'NEW-024': 'Substantially covered by repair-vs-replace-nampa-id (its whole purpose) and '
               'water-heater-lifespan-nampa-id\'s "Signs a Water Heater Is Nearing the End of '
               'Its Service Life" section.',
    'NEW-025': 'Partially covered: repair-vs-replace-nampa-id\'s FAQ already states tank-body '
               'corrosion means replacement, not repair. A dedicated page would need new value '
               'beyond that single already-published conclusion; not attempted this round.',
    'NEW-032': 'Sediment is already pervasively covered qualitatively across making-noise, '
               'maintenance-checklist, sizing-guide, and lifespan pages; no single-page gap.',
}

# Rows looked at, flagged as weaker/needing careful scoping, but NOT
# confirmed as duplicates — legitimate future candidates, not rejected.
CONSIDERED_NOT_SELECTED = {
    'A-002': 'Vaguer catch-all ("works only sometimes"); risks overlapping conceptually with '
              'A-003 (shuts off randomly) without its own crisp mechanism. Not individually '
              'confirmed as a duplicate.',
    'A-008': 'Niche/thin (post-flush refill failure); not individually confirmed as a '
              'duplicate, just judged lower-value than the 9 selected.',
    'A-011': 'Not reviewed in depth this round.',
    'A-012': 'Map\'s own note says distinct from short-cycling, which is correct, but this '
              'pass did not individually verify it against no-hot-water/making-noise live text.',
    'NEW-020': 'Borderline safety-adjacent (water too hot touches scalding-safety territory); '
                'not individually vetted for whether it can stay at a general-knowledge level.',
    'NEW-027': 'Needs careful scoping against water-heater-tripping-breaker-nampa-id\'s existing '
                'electrical causes to avoid restating them; not attempted this round.',
}

REJECT_BRAND_PREFIX = '/brands/'
REJECT_SHUTOFF_CO_SLUGS = {
    'when-to-shut-off-gas', 'when-to-shut-off-water', 'when-to-shut-off-power',
    'when-to-call-emergency-service', 'gas-leak-detection-basics', 'co-detector-placement',
    'gas-smell-water-heater',
}
REJECT_SHORT_CYCLING_SLUGS = {'water-heater-short-cycling-nampa-id'}
REJECT_INSULATION_SLUGS = {'insulation-blanket-guidance'}
REJECT_WARRANTY_SLUGS = {'warranty-cost-considerations', 'water-heater-warranty-lookup'}
REJECT_TP_SAFETY_SLUGS = {'water-heater-overflow-tp-valve'}  # NEW-031: treated as safety-
# blocked despite the v2 list's own "No" tag, for consistency with Pool F's
# "pressure-relief-valve-safety" row (source_req "Yes") on the same component.


def slug_of(url):
    return url.rstrip('/').rsplit('/', 1)[-1]


def classify(row):
    url = row['url']
    slug = slug_of(url)
    rid = row['id']

    if row['status'] == 'Existing':
        return 'existing', 'One of the 31 pages already live when the map was built.'

    if rid in PUBLISHED_BY_ID:
        return 'published', f"Published at {PUBLISHED_BY_ID[rid]}."
    if url in PUBLISHED:
        pub = PUBLISHED[url]
        if pub:
            return 'published', f"Published at {pub}."

    if url.startswith(REJECT_BRAND_PREFIX):
        return ('rejected_category',
                'Brand-specific troubleshooting/error-code page - same category dropped from '
                'the Oct 5 release (6 brand pages + /brands hub): needs manufacturer-verified '
                'error-code tables this project has never obtained.')
    if slug in REJECT_SHUTOFF_CO_SLUGS:
        return ('rejected_category',
                'Emergency gas/water/power shutoff or carbon-monoxide topic - explicitly '
                'rejected earlier this session ("Topic A"): needs CPSC/NFPA/utility primary '
                'sources; this environment\'s total egress block has never allowed fetching one.')
    if slug in REJECT_SHORT_CYCLING_SLUGS:
        return ('rejected_category',
                'Short-cycling - explicitly rejected by the owner (insufficient/contradictory '
                'sourcing across the manufacturer documents actually reviewed) and named again '
                'as off-limits in the Oct 19 task itself.')
    if slug in REJECT_INSULATION_SLUGS:
        return ('rejected_category',
                'Insulation-blanket guidance - explicitly rejected: may require model-specific '
                'manufacturer safety instructions not available.')
    if slug in REJECT_WARRANTY_SLUGS:
        return ('rejected_category',
                'Warranty coverage/cost topic - explicitly rejected: requires actual warranty '
                'documents, none available.')
    if slug in REJECT_TP_SAFETY_SLUGS:
        return ('rejected_category',
                'T&P valve discharge is a safety event; treated at the same source_req bar as '
                'Pool F\'s "pressure-relief-valve-safety" row despite this row\'s own "No" tag, '
                'for internal consistency. No primary source available.')

    if rid in REJECTED_DUPLICATE:
        return 'rejected_duplicate', REJECTED_DUPLICATE[rid]
    if rid in CONSIDERED_NOT_SELECTED:
        return 'considered_not_selected', CONSIDERED_NOT_SELECTED[rid]

    if row.get('source_req') == 'Yes':
        return ('source_blocked',
                'Map marks this topic as needing a primary source before publishing. No '
                'manufacturer/code/safety document for this specific topic has been obtained; '
                'this environment\'s total egress block (every external fetch attempt returns '
                'EGRESS_BLOCKED) means it can only be unblocked by a new owner-supplied document.')

    return ('not_yet_evaluated',
            'Map marks source_req "No", but this annotation pass did not individually read '
            'live-page content to confirm non-duplication for this row. Unscreened candidate '
            'for a future batch, not pre-approved.')


def main():
    fieldnames = ['id', 'url', 'title', 'status', 'reason', 'published_url',
                  'map_status', 'source_req', 'cannib', 'cluster', 'tier']
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for extra in NO_MAP_ROW_PUBLISHED:
            w.writerow({
                'id': extra['id'], 'url': extra['url'], 'title': extra['title'],
                'status': extra['status'], 'reason': extra['reason'],
                'published_url': extra['published_url'],
                'map_status': '', 'source_req': '', 'cannib': '', 'cluster': '', 'tier': '',
            })
        for row in PAGES:
            status, reason = classify(row)
            published_url = ''
            if status == 'published':
                published_url = PUBLISHED_BY_ID.get(row['id']) or PUBLISHED.get(row['url'], '')
            w.writerow({
                'id': row['id'], 'url': row['url'], 'title': row['title'],
                'status': status, 'reason': reason, 'published_url': published_url,
                'map_status': row['status'], 'source_req': row.get('source_req', ''),
                'cannib': row.get('cannib', ''), 'cluster': row['cluster'], 'tier': row['tier'],
            })
    print(f"Wrote {OUT_CSV}")

    from collections import Counter
    rows = [classify(r)[0] for r in PAGES] + ['published'] * len(NO_MAP_ROW_PUBLISHED)
    print("Status counts:", Counter(rows))


if __name__ == '__main__':
    main()
