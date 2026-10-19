#!/usr/bin/env python3
"""
Regenerate sitemap.xml from the repo's actual file tree, preserving every
existing URL's <lastmod>/<changefreq>/<priority> and original ordering.

This is a MERGE, not a from-scratch rebuild: lastmod values are historical
publish dates that cannot be mechanically re-derived, and priority/changefreq
follow a page-category convention (home=1.0, hub index pages and money
service pages=0.9, service-areas=0.8, about/contact=0.6, guide/symptom
pages=0.7, legal=0.4) that isn't a pure function of path depth either. So:

  - Every URL already in sitemap.xml keeps its exact existing metadata and
    position, as long as the file backing it still exists.
  - A URL whose file no longer exists is dropped (the page was removed).
  - A URL for a file that exists but isn't in sitemap.xml yet is new; it's
    appended at the end (matching this project's actual history: every
    batch so far appended after the prior ones) with the same defaults
    every batch on this site has used by hand: today's date, "monthly",
    "0.7".

Clean-URL derivation mirrors src/worker.js's candidatePaths() in reverse:
  index.html at the repo root        -> /
  <dir>/index.html                   -> /<dir>
  <name>.html                        -> /<name>
  <dir>/<name>.html                  -> /<dir>/<name>
No trailing slash (except the homepage), no .html suffix — matching the
clean-URL convention the Worker actually serves.

The Worker's filterSitemap() (src/worker.js) hides not-yet-released
RELEASE_GATES entries from the PUBLIC sitemap.xml at request time; this
script does not do date-based filtering itself — it always emits every real
page, gated or not, exactly as the static file has always contained them.
"""
import os
import re
import sys
from datetime import date, datetime, timezone
from xml.sax.saxutils import escape, unescape

BASE = "/home/user/nampa-water-heater-site"
DOMAIN = "https://nampawaterheater.com"

# Directories that never contain page files.
EXCLUDED_DIRS = {'.git', 'scripts', 'assets', 'rules', 'node_modules', '.wrangler', 'src'}


def discover_urls(base_dir=BASE):
    """Walk the file tree and return the set of clean canonical URLs for
    every real .html page, derived the same way src/worker.js resolves
    clean URLs to on-disk files (in reverse)."""
    urls = set()
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS and not d.startswith('.')]
        for fname in files:
            if not fname.endswith('.html'):
                continue
            rel = os.path.relpath(os.path.join(root, fname), base_dir)
            rel = rel.replace(os.sep, '/')
            if rel == 'index.html':
                url = '/'
            elif rel.endswith('/index.html'):
                url = '/' + rel[:-len('/index.html')]
            else:
                url = '/' + rel[:-len('.html')]
            urls.add(url)
    return urls


def parse_existing_sitemap(xml_text):
    """Parse sitemap.xml into an ordered list of dicts, preserving order.
    Returns [{'url': '/about', 'lastmod': '2026-08-29', 'changefreq': 'monthly',
    'priority': '0.6'}, ...] with url as the path only (domain stripped)."""
    entries = []
    for block in re.findall(r'<url>(.*?)</url>', xml_text, re.DOTALL):
        loc_m = re.search(r'<loc>(.*?)</loc>', block)
        if not loc_m:
            continue
        loc = unescape(loc_m.group(1).strip())
        if not loc.startswith(DOMAIN):
            continue
        path = loc[len(DOMAIN):]
        if path == '':
            path = '/'
        entry = {'url': path}
        for field in ('lastmod', 'changefreq', 'priority'):
            m = re.search(rf'<{field}>(.*?)</{field}>', block)
            if m:
                entry[field] = unescape(m.group(1).strip())
        entries.append(entry)
    return entries


# Defaults for a URL that exists on disk but has no prior sitemap entry —
# matches the values this project has used by hand for every new guide/
# symptom page across the Oct 5, Oct 6, and Oct 19 batches.
NEW_ENTRY_CHANGEFREQ = 'monthly'
NEW_ENTRY_PRIORITY = '0.7'


def build_sitemap(existing_entries, discovered_urls, today=None):
    """Merge existing sitemap entries with the discovered URL set.
    - Existing entries whose URL is still a real file are kept as-is, in
      their original order.
    - Existing entries whose URL no longer corresponds to a file are dropped.
    - URLs present on disk but not in existing_entries are appended, sorted,
      with default metadata.
    Returns an ordered list of entry dicts (same shape as parse_existing_sitemap).
    """
    if today is None:
        today = datetime.now(timezone.utc).date().isoformat()

    existing_urls = {e['url'] for e in existing_entries}
    kept = [e for e in existing_entries if e['url'] in discovered_urls]

    new_urls = sorted(discovered_urls - existing_urls)
    appended = [
        {
            'url': u,
            'lastmod': today,
            'changefreq': NEW_ENTRY_CHANGEFREQ,
            'priority': NEW_ENTRY_PRIORITY,
        }
        for u in new_urls
    ]
    return kept + appended


def render_xml(entries):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for e in entries:
        loc = f"{DOMAIN}/" if e['url'] == '/' else f"{DOMAIN}{e['url']}"
        lines.append('  <url>')
        lines.append(f'    <loc>{escape(loc)}</loc>')
        if 'lastmod' in e:
            lines.append(f"    <lastmod>{escape(e['lastmod'])}</lastmod>")
        if 'changefreq' in e:
            lines.append(f"    <changefreq>{escape(e['changefreq'])}</changefreq>")
        if 'priority' in e:
            lines.append(f"    <priority>{escape(e['priority'])}</priority>")
        lines.append('  </url>')
    lines.append('</urlset>')
    lines.append('')
    return '\n'.join(lines)


def main():
    sitemap_path = os.path.join(BASE, 'sitemap.xml')
    with open(sitemap_path, encoding='utf-8') as f:
        existing_xml = f.read()
    existing_entries = parse_existing_sitemap(existing_xml)
    discovered = discover_urls(BASE)

    new_entries = build_sitemap(existing_entries, discovered)
    output = render_xml(new_entries)

    dropped = {e['url'] for e in existing_entries} - discovered
    added = {e['url'] for e in new_entries} - {e['url'] for e in existing_entries}

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Sitemap written with {len(new_entries)} URLs ({len(existing_entries)} existing, "
          f"{len(added)} added, {len(dropped)} dropped).")
    if added:
        print("Added (new, default metadata — review priority/changefreq if this isn't a "
              "standard guide/symptom page):")
        for u in sorted(added):
            print(f"  {u}")
    if dropped:
        print("Dropped (no longer a real file):")
        for u in sorted(dropped):
            print(f"  {u}")


if __name__ == '__main__':
    sys.exit(main())
