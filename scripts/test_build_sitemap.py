#!/usr/bin/env python3
"""Regression tests for scripts/build_sitemap.py.

Run: python3 scripts/test_build_sitemap.py

Covers:
  1. Clean canonical URL format (no .html, no trailing slash except '/').
  2. Idempotency: regenerating against the CURRENT repo file tree + the
     CURRENT checked-in sitemap.xml reproduces it exactly (same URL set,
     same order, same metadata per URL) — the core "no unintended changes"
     regression check.
  3. Dropped paths (the 7 removed /brands URLs) never appear, regardless of
     input, because they aren't real files.
  4. Gated paths are included statically (every RELEASE_GATES key that
     corresponds to a real file is present in the generated sitemap) —
     gating is the Worker's dynamic filterSitemap() responsibility, not
     this script's; this script must never try to replicate it.
  5. Merge logic itself (new file gets appended with sensible defaults,
     deleted file's old entry is dropped, untouched entries are preserved
     byte-for-byte) using a synthetic fixture, not just the current no-op case.
"""
import os
import re
import sys
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_sitemap import (
    discover_urls, parse_existing_sitemap, build_sitemap, render_xml, BASE, DOMAIN,
)

failures = 0
checks = 0


def assert_(condition, label):
    global checks, failures
    checks += 1
    if not condition:
        failures += 1
        print(f"  FAIL: {label}")


# ---------------------------------------------------------------------------
# 1. Clean canonical URL format
# ---------------------------------------------------------------------------
print("Testing clean canonical URL format...\n")
discovered = discover_urls(BASE)
assert_(len(discovered) > 0, "discover_urls found at least one page")
for u in discovered:
    assert_(not u.endswith('.html'), f"{u}: no .html suffix")
    assert_(u == '/' or not u.endswith('/'), f"{u}: no trailing slash")
    assert_(u.startswith('/'), f"{u}: starts with /")

# ---------------------------------------------------------------------------
# 2. Idempotency against the real repo: regenerating must reproduce the
#    current sitemap.xml exactly — same URLs, same order, same metadata.
# ---------------------------------------------------------------------------
print("\nTesting idempotency against the current repo state...\n")
with open(os.path.join(BASE, 'sitemap.xml'), encoding='utf-8') as f:
    current_xml = f.read()
current_entries = parse_existing_sitemap(current_xml)

regenerated = build_sitemap(current_entries, discovered, today='2026-10-19')

assert_(len(regenerated) == len(current_entries),
        f"regenerated entry count ({len(regenerated)}) matches current ({len(current_entries)})")

current_urls_ordered = [e['url'] for e in current_entries]
regenerated_urls_ordered = [e['url'] for e in regenerated]
assert_(regenerated_urls_ordered == current_urls_ordered,
        "regenerated URL order matches current sitemap.xml order exactly")

for cur, regen in zip(current_entries, regenerated):
    assert_(cur == regen, f"{cur['url']}: metadata (lastmod/changefreq/priority) unchanged")

# No dropped, no added, on a clean re-run against unchanged reality.
dropped = {e['url'] for e in current_entries} - discovered
added = discovered - {e['url'] for e in current_entries}
assert_(dropped == set(), f"no URLs dropped on idempotent run (found: {dropped})")
assert_(added == set(), f"no URLs added on idempotent run (found: {added})")

rendered = render_xml(regenerated)
# Normalize only whitespace-at-EOF differences; byte-for-byte otherwise.
assert_(rendered.strip() == current_xml.strip(),
        "re-rendered XML is byte-identical to the checked-in sitemap.xml")

# ---------------------------------------------------------------------------
# 3. Dropped /brands paths never appear, from real discovery or from a
#    stale sitemap entry (simulating one that lingered after removal).
# ---------------------------------------------------------------------------
print("\nTesting dropped /brands paths are always excluded...\n")
DROPPED_PATHS = [
    '/brands',
    '/brands/rheem-water-heater-repair-nampa-id',
    '/brands/ao-smith-water-heater-repair-nampa-id',
    '/brands/bradford-white-water-heater-repair-nampa-id',
    '/brands/navien-water-heater-repair-nampa-id',
    '/brands/rinnai-water-heater-repair-nampa-id',
    '/brands/noritz-water-heater-repair-nampa-id',
]
for p in DROPPED_PATHS:
    assert_(p not in discovered, f"{p}: absent from real file-tree discovery")

# Simulate a stale sitemap that still lists a dropped page — the merge must
# drop it since no file backs it, proving removal is enforced by file
# presence, not merely by omission from a fresh run.
stale_entries = current_entries + [{
    'url': '/brands/rheem-water-heater-repair-nampa-id',
    'lastmod': '2026-09-01', 'changefreq': 'monthly', 'priority': '0.7',
}]
merged = build_sitemap(stale_entries, discovered, today='2026-10-19')
merged_urls = {e['url'] for e in merged}
assert_('/brands/rheem-water-heater-repair-nampa-id' not in merged_urls,
        "a stale sitemap entry for a removed page is dropped on merge")

# ---------------------------------------------------------------------------
# 4. Gated paths are included statically (not excluded by this script) —
#    cross-check against src/worker.js's RELEASE_GATES.
# ---------------------------------------------------------------------------
print("\nTesting gated paths are included statically (gating is the Worker's job)...\n")
worker_src = open(os.path.join(BASE, 'src/worker.js'), encoding='utf-8').read()
gate_block_m = re.search(r'const RELEASE_GATES = \{(.*?)\};', worker_src, re.DOTALL)
assert_(gate_block_m is not None, "RELEASE_GATES block found in src/worker.js")
gate_paths = re.findall(r"'([^']+)':\s*'[^']+'", gate_block_m.group(1)) if gate_block_m else []
assert_(len(gate_paths) > 0, "at least one RELEASE_GATES entry found")
for p in gate_paths:
    assert_(p in discovered, f"{p}: gated path's file still exists on disk")
    assert_(p in merged_urls, f"{p}: gated path is present in the generated static sitemap "
                               f"(gating hides it dynamically via filterSitemap, not here)")

# ---------------------------------------------------------------------------
# 5. Merge logic on a synthetic fixture: new file added, deleted file's
#    entry dropped, untouched entry preserved exactly.
# ---------------------------------------------------------------------------
print("\nTesting merge logic on a synthetic fixture...\n")
tmp = tempfile.mkdtemp(prefix='sitemap_fixture_')
try:
    os.makedirs(os.path.join(tmp, 'common-issues'))
    with open(os.path.join(tmp, 'index.html'), 'w') as f:
        f.write('<html></html>')
    with open(os.path.join(tmp, 'about.html'), 'w') as f:
        f.write('<html></html>')
    with open(os.path.join(tmp, 'common-issues', 'new-symptom-nampa-id.html'), 'w') as f:
        f.write('<html></html>')
    # Deliberately do NOT create a file for '/contact', to test dropping.

    fixture_existing = [
        {'url': '/', 'lastmod': '2026-01-01', 'changefreq': 'weekly', 'priority': '1.0'},
        {'url': '/about', 'lastmod': '2026-01-02', 'changefreq': 'monthly', 'priority': '0.6'},
        {'url': '/contact', 'lastmod': '2026-01-03', 'changefreq': 'monthly', 'priority': '0.6'},
    ]
    fixture_discovered = discover_urls(tmp)
    assert_(fixture_discovered == {'/', '/about', '/common-issues/new-symptom-nampa-id'},
            f"fixture discovery matches expected set (got {fixture_discovered})")

    fixture_result = build_sitemap(fixture_existing, fixture_discovered, today='2026-10-19')
    result_urls = [e['url'] for e in fixture_result]

    assert_('/contact' not in result_urls, "fixture: deleted file's entry ('/contact') is dropped")
    assert_('/common-issues/new-symptom-nampa-id' in result_urls,
            "fixture: new file's URL is added")
    new_entry = next(e for e in fixture_result if e['url'] == '/common-issues/new-symptom-nampa-id')
    assert_(new_entry['lastmod'] == '2026-10-19', "fixture: new entry gets today's lastmod")
    assert_(new_entry['changefreq'] == 'monthly', "fixture: new entry gets 'monthly' changefreq")
    assert_(new_entry['priority'] == '0.7', "fixture: new entry gets '0.7' priority")

    preserved_root = next(e for e in fixture_result if e['url'] == '/')
    assert_(preserved_root == {'url': '/', 'lastmod': '2026-01-01', 'changefreq': 'weekly', 'priority': '1.0'},
            "fixture: untouched '/' entry preserved exactly (not reset to defaults)")
    preserved_about = next(e for e in fixture_result if e['url'] == '/about')
    assert_(preserved_about == {'url': '/about', 'lastmod': '2026-01-02', 'changefreq': 'monthly', 'priority': '0.6'},
            "fixture: untouched '/about' entry preserved exactly")

    # Existing entries (minus the dropped one) must keep their original
    # relative order, with the new one appended at the end.
    assert_(result_urls == ['/', '/about', '/common-issues/new-symptom-nampa-id'],
            f"fixture: final order is [kept-in-original-order, then appended new] (got {result_urls})")
finally:
    shutil.rmtree(tmp)

print(f"\n{checks - failures}/{checks} checks passed.")
if failures > 0:
    print(f"{failures} FAILURE(S)")
    sys.exit(1)
else:
    print("All build_sitemap regression tests passed.")
