#!/usr/bin/env python3
import re, os, json

BASE = "/home/user/nampa-water-heater-site/nampa-water-heater"
errors = []
count = 0

for root, dirs, files in os.walk(BASE):
    if 'assets' in root:
        continue
    for fname in files:
        if not fname.endswith('.html'):
            continue
        filepath = os.path.join(root, fname)
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
        scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        for i, script in enumerate(scripts):
            count += 1
            try:
                json.loads(script)
            except json.JSONDecodeError as e:
                errors.append((filepath, i, str(e)))

print(f"Checked {count} JSON-LD blocks across the site.")
if errors:
    print(f"\n{len(errors)} INVALID:")
    for filepath, i, err in errors:
        print(f"  {filepath} [script #{i}]: {err}")
else:
    print("All JSON-LD blocks are valid JSON.")
