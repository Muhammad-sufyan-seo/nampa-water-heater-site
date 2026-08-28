#!/usr/bin/env python3
import os

BASE = "/home/user/nampa-water-heater-site"
DOMAIN = "https://nampawaterheater.com"

pages = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts', 'assets')]
    for fname in sorted(files):
        if fname.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, fname), BASE)
            if rel == "index.html":
                url = f"{DOMAIN}/"
            else:
                url = f"{DOMAIN}/{rel}"
            pages.append(url)

pages.sort()

xml_entries = "\n".join([
    f"""  <url>
    <loc>{url}</loc>
  </url>""" for url in pages
])

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_entries}
</urlset>
"""

with open(f"{BASE}/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"Sitemap written with {len(pages)} URLs.")
for p in pages:
    print(f"  {p}")
