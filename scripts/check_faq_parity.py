#!/usr/bin/env python3
"""Verify FAQPage schema text matches visible .faq-answer text word-for-word, sitewide.
Added after the 2026-08 content audit found 17 pages with orphaned FAQ schema
(no visible counterpart) and 4 pillar pages with schema/visible text drift."""
import re, json, os

BASE = "/home/user/nampa-water-heater-site"

all_ok = True
checked = 0
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts', 'assets', 'rules')]
    for fname in sorted(files):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, BASE)
        with open(path, encoding="utf-8") as f:
            content = f.read()

        scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        data = None
        for s in scripts:
            try:
                parsed = json.loads(s)
            except json.JSONDecodeError:
                continue
            if parsed.get("@type") == "FAQPage":
                data = parsed
                break
        if data is None:
            continue

        checked += 1
        schema_answers = [q["acceptedAnswer"]["text"] for q in data["mainEntity"]]
        schema_questions = [q["name"] for q in data["mainEntity"]]

        visible_blocks = re.findall(r'<div class="faq-answer"[^>]*>\s*<p>(.*?)</p>\s*</div>', content, re.DOTALL)
        visible_questions = re.findall(r'<button class="faq-question"[^>]*>\s*(.*?)\s*<span class="faq-icon"', content, re.DOTALL)

        if len(visible_blocks) != len(schema_answers):
            print(f"{rel}: COUNT MISMATCH - schema has {len(schema_answers)}, visible has {len(visible_blocks)}")
            all_ok = False
            continue

        for i, (sa, va) in enumerate(zip(schema_answers, visible_blocks), 1):
            va_stripped = re.sub(r'<a\s+href="tel:[^"]*"[^>]*>(.*?)</a>', r'\1', va)
            va_stripped = re.sub(r'</?strong>', '', va_stripped).strip()
            if sa.strip() != va_stripped:
                print(f"{rel} Q{i}: ANSWER MISMATCH")
                print(f"  schema : {sa!r}")
                print(f"  visible: {va_stripped!r}")
                all_ok = False

        for i, (sq, vq) in enumerate(zip(schema_questions, visible_questions), 1):
            if sq.strip() != vq.strip():
                print(f"{rel} Q{i}: QUESTION MISMATCH schema={sq!r} visible={vq!r}")
                all_ok = False

print(f"\nChecked {checked} pages with FAQPage schema.")
print("ALL PAGES MATCH WORD-FOR-WORD" if all_ok else "MISMATCHES FOUND ABOVE")
