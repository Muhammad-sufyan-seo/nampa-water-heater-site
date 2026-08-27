#!/usr/bin/env python3
import re, os

BASE = "/home/user/nampa-water-heater-site/nampa-water-heater"
broken = []

all_files = []
for root, dirs, files in os.walk(BASE):
    if 'assets' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

for filepath in all_files:
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    dirpath = os.path.dirname(filepath)
    hrefs = re.findall(r'href="([^"]+)"', content)
    for href in hrefs:
        if href.startswith(('http://', 'https://', 'tel:', 'mailto:', '#')):
            continue
        # strip fragment
        path_part = href.split('#')[0]
        if not path_part:
            continue
        resolved = os.path.normpath(os.path.join(dirpath, path_part))
        if not os.path.isfile(resolved):
            broken.append((filepath, href, resolved))

if broken:
    print(f"Found {len(broken)} broken links:")
    for filepath, href, resolved in broken:
        print(f"  {filepath} -> {href} (resolved: {resolved})")
else:
    print("No broken internal links found.")
