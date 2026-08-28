#!/usr/bin/env python3
"""
Phone-number verification script for Nampa Water Heater Pros.

1. Confirms ZERO instances of any old/wrong phone number anywhere in the site
   (555-0123, 470-0340, or any (208) number other than 987-5152 in a business
   context — the form-field placeholder (208) 555-0000 is intentionally
   excluded since it's a standard fake-example convention, not a business
   phone reference).
2. Confirms EVERY tel: href across the site is exactly tel:+12089875152.
3. Confirms every <a> tag that contains the phone SVG icon or a "Call"-style
   aria-label actually carries a tel: href (no missing href bug).
4. Confirms every schema JSON-LD "telephone" field uses the +1-208-987-5152
   format.
5. Reports total counts.
"""
import re, os

BASE = "/home/user/nampa-water-heater-site"
CORRECT_TEL_HREF = "tel:+12089875152"
CORRECT_VISIBLE = "(208) 987-5152"
CORRECT_SCHEMA_TEL = "+1-208-987-5152"
PHONE_ICON_MARKER = "M6.6 10.8c1.4 2.8"

old_number_patterns = [
    re.compile(r"555-0123|5550123|555 0123"),
    re.compile(r"470-0340|4700340"),
    re.compile(r"\(717\)|717-470"),
    re.compile(r"\(208\)\s?[0-9]{3}-[0-9]{4}"),  # any (208) number, filtered below
    re.compile(r"208-[0-9]{3}-[0-9]{4}"),
    re.compile(r"\+1208[0-9]{7}"),
]

all_files = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts')]
    for fname in files:
        if fname.endswith(('.html', '.js', '.json', '.xml', '.txt', '.css')):
            all_files.append(os.path.join(root, fname))

files_scanned = len(all_files)
old_number_hits = []
tel_href_hits = []
tel_href_bad = []
schema_tel_hits = []
schema_tel_bad = []
call_anchor_missing_href = []
phone_icon_missing_href = []
total_tel_links = 0

for filepath in sorted(all_files):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    for lineno, line in enumerate(lines, 1):
        # --- old/wrong number scan ---
        for pat in old_number_patterns:
            for m in pat.finditer(line):
                matched = m.group(0)
                if "987-5152" in matched or "9875152" in matched:
                    continue
                # Exclude the known-correct form placeholder
                if "555-0000" in line and "placeholder" in line:
                    continue
                old_number_hits.append((filepath, lineno, matched, line.strip()))

        # --- tel: href scan ---
        for m in re.finditer(r'tel:[^"\'\s>]*', line):
            total_tel_links += 1
            href = m.group(0)
            if href != CORRECT_TEL_HREF:
                tel_href_bad.append((filepath, lineno, href))
            else:
                tel_href_hits.append((filepath, lineno, href))

        # --- schema telephone field scan ---
        m = re.search(r'"telephone":\s*"([^"]+)"', line)
        if m:
            val = m.group(1)
            if val == CORRECT_SCHEMA_TEL:
                schema_tel_hits.append((filepath, lineno, val))
            else:
                schema_tel_bad.append((filepath, lineno, val))

    # --- <a> tags with Call-ish aria-label missing tel: href ---
    for m in re.finditer(r'<a\b([^>]*)>', content):
        attrs = m.group(1)
        aria_match = re.search(r'aria-label="([^"]*)"', attrs)
        has_call_label = aria_match and re.search(r'\bcall\b', aria_match.group(1), re.IGNORECASE)
        has_tel_href = 'href="tel:' in attrs
        if has_call_label and not has_tel_href:
            call_anchor_missing_href.append((filepath, attrs[:80]))

    # --- <a> tags wrapping the phone SVG icon but missing tel: href ---
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', content, re.DOTALL):
        attrs, inner = m.group(1), m.group(2)
        if PHONE_ICON_MARKER in inner and 'href="tel:' not in attrs:
            phone_icon_missing_href.append((filepath, attrs[:80]))

print(f"Files scanned: {files_scanned}")
print(f"Total tel: links found: {total_tel_links}")
print(f"Correctly-formatted tel: links ({CORRECT_TEL_HREF}): {len(tel_href_hits)}")
print(f"Incorrectly-formatted tel: links: {len(tel_href_bad)}")
for f, l, h in tel_href_bad:
    print(f"  {f}:{l} -> {h}")

print(f"\nSchema telephone fields matching '{CORRECT_SCHEMA_TEL}': {len(schema_tel_hits)}")
print(f"Schema telephone fields NOT matching: {len(schema_tel_bad)}")
for f, l, v in schema_tel_bad:
    print(f"  {f}:{l} -> \"{v}\"")

print(f"\nOld/wrong phone number instances found: {len(old_number_hits)}")
for f, l, matched, line in old_number_hits:
    print(f"  {f}:{l} -> matched '{matched}' in: {line}")

print(f"\n<a> tags with a Call-style aria-label but NO tel: href: {len(call_anchor_missing_href)}")
for f, attrs in call_anchor_missing_href:
    print(f"  {f}: {attrs}")

print(f"\n<a> tags wrapping the phone icon but NO tel: href: {len(phone_icon_missing_href)}")
for f, attrs in phone_icon_missing_href:
    print(f"  {f}: {attrs}")

ok = (
    len(old_number_hits) == 0
    and len(tel_href_bad) == 0
    and len(schema_tel_bad) == 0
    and len(call_anchor_missing_href) == 0
    and len(phone_icon_missing_href) == 0
)
print(f"\n{'PASS' if ok else 'FAIL'}: phone number verification {'passed' if ok else 'failed'}.")
