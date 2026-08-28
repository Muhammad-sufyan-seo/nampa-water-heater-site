#!/usr/bin/env python3
"""Verify every page has exactly one H1, and that no H1 text is duplicated
verbatim as an H2 on the same page or reused verbatim across different pages."""
import re, os

BASE = "/home/user/nampa-water-heater-site"

def get_h1s(html):
    return re.findall(r'<h1\b[^>]*>(.*?)</h1>', html, re.DOTALL)

def get_h2s(html):
    return re.findall(r'<h2\b[^>]*>(.*?)</h2>', html, re.DOTALL)

def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', s).strip()

files = []
for root, dirs, fnames in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts', 'assets', 'rules')]
    for fname in sorted(fnames):
        if fname.endswith('.html'):
            files.append(os.path.join(root, fname))

errors = []
all_h1_texts = {}

for path in files:
    rel = os.path.relpath(path, BASE)
    with open(path, encoding='utf-8') as f:
        html = f.read()

    h1s = [clean(h) for h in get_h1s(html)]
    if len(h1s) != 1:
        errors.append(f"{rel}: has {len(h1s)} H1 tags (expected exactly 1)")
        continue

    h1_text = h1s[0]
    h2s = [clean(h) for h in get_h2s(html)]
    if h1_text in h2s:
        errors.append(f"{rel}: H1 text duplicated verbatim as an H2 on the same page: {h1_text!r}")

    if h1_text in all_h1_texts:
        errors.append(f"{rel}: H1 text {h1_text!r} duplicates the H1 on {all_h1_texts[h1_text]}")
    else:
        all_h1_texts[h1_text] = rel

print(f"Checked {len(files)} pages.")
if errors:
    print(f"\n{len(errors)} issue(s) found:")
    for e in errors:
        print(f"  {e}")
else:
    print("PASS: every page has exactly one H1, unique sitewide, never duplicated as an H2.")
