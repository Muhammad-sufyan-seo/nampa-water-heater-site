#!/usr/bin/env python3
"""
Internal link checker for nampawaterheater.com.

Handles both root-relative paths (/about, /services/xxx) and relative paths
(../about, ./contact). All asset paths (CSS, JS, images) are also checked.
The Worker serves /foo from foo.html and /foo/ from foo/index.html on disk.
"""
import re, os

BASE = "/home/user/nampa-water-heater-site"
broken = []

all_files = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts', 'node_modules', '.wrangler')]
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

def resolve_url_path(url_path):
    """Return the on-disk file for a given URL path, or None if not found."""
    if url_path == '/':
        disk = os.path.join(BASE, 'index.html')
        return disk if os.path.isfile(disk) else None
    # Strip leading slash for disk join
    rel = url_path.lstrip('/')
    if url_path.endswith('/'):
        # trailing slash -> index.html
        disk = os.path.join(BASE, rel, 'index.html')
        return disk if os.path.isfile(disk) else None
    else:
        # Try exact, then .html, then /index.html
        for candidate in [
            os.path.join(BASE, rel),
            os.path.join(BASE, rel + '.html'),
            os.path.join(BASE, rel, 'index.html'),
        ]:
            if os.path.isfile(candidate):
                return candidate
        return None

for filepath in all_files:
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    dirpath = os.path.dirname(filepath)
    hrefs = re.findall(r'href="([^"]+)"', content)
    for href in hrefs:
        if href.startswith(('http://', 'https://', 'tel:', 'mailto:', '#')):
            continue
        # strip fragment and query string — a request's pathname never
        # includes them, so e.g. style.css?v=20261004 resolves as style.css
        path_part = href.split('#')[0].split('?')[0]
        if not path_part:
            continue

        if path_part.startswith('/'):
            # Root-relative path — resolve from REPO root
            resolved = resolve_url_path(path_part)
            if resolved is None:
                broken.append((filepath, href, BASE + path_part))
        else:
            # Relative path — resolve from file's directory
            from urllib.parse import urljoin
            file_url = '/' + os.path.relpath(filepath, BASE).replace(os.sep, '/')
            resolved_url = urljoin(file_url, path_part)
            resolved = resolve_url_path(resolved_url)
            if resolved is None:
                broken.append((filepath, href, BASE + resolved_url))

if broken:
    print(f"Found {len(broken)} broken links:")
    for filepath, href, resolved in broken:
        print(f"  {os.path.relpath(filepath, BASE)} -> {href} (resolved: {resolved})")
else:
    print("No broken internal links found.")
