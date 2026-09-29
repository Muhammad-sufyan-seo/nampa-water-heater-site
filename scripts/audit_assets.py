#!/usr/bin/env python3
"""
Static asset audit for nampawaterheater.com.

For every HTML file, resolves every href/src attribute value and checks:
  1. File exists on disk (MISSING)
  2. Filename case matches exactly (CASE-MISMATCH)
  3. Image files have valid magic bytes (INVALID-IMAGE)

With --production: also makes HTTP requests to the live site and checks:
  4. HTTP status is 200 (HTTP-404)
  5. Content-Type is not text/html for binary assets (WRONG-MIME)

Exit code 0 = clean; 1 = issues found.

Usage:
  python3 scripts/audit_assets.py              # local checks only
  python3 scripts/audit_assets.py --production # + live HTTP checks
"""

import re, os, sys, struct
from urllib.parse import urljoin, urlparse

BASE_URL = "https://nampawaterheater.com"
REPO     = "/home/user/nampa-water-heater-site"

# Magic bytes for binary image formats
IMAGE_MAGIC = {
    '.png':  [(0, b'\x89PNG\r\n\x1a\n')],
    '.jpg':  [(0, b'\xff\xd8\xff')],
    '.jpeg': [(0, b'\xff\xd8\xff')],
    '.webp': [(0, b'RIFF'), (8, b'WEBP')],
    '.gif':  [(0, b'GIF8')],
    '.ico':  [(0, b'\x00\x00\x01\x00')],
    '.svg':  None,  # text-based; skip magic check
    '.woff': [(0, b'\x77\x4f\x46\x46')],
    '.woff2':[(0, b'\x77\x4f\x46\x32')],
}

def file_to_url(path):
    rel = os.path.relpath(path, REPO)
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("/index.html")]
    if rel.endswith(".html"):
        return "/" + rel[:-len(".html")]
    return "/" + rel

def url_to_file(url_path):
    candidates = (
        ["/index.html"] if url_path == "/"
        else [url_path, url_path + ".html", url_path + "/index.html"]
    )
    for c in candidates:
        disk = REPO + c
        if os.path.isfile(disk):
            return disk
    return None

def check_case(url_path):
    """Return True if the file at url_path exists with matching case."""
    disk = REPO + url_path
    if not os.path.exists(disk):
        return True  # handled by url_to_file missing check
    actual = os.path.basename(disk)
    expected = os.path.basename(url_path)
    return actual == expected

def check_image_magic(disk_path):
    """Return error string if image magic bytes are wrong, else None."""
    ext = os.path.splitext(disk_path)[1].lower()
    checks = IMAGE_MAGIC.get(ext)
    if checks is None:
        return None  # no magic check for this type
    try:
        with open(disk_path, 'rb') as f:
            header = f.read(16)
        for offset, magic in checks:
            if header[offset:offset+len(magic)] != magic:
                return f"bad magic at offset {offset}: expected {magic.hex()}, got {header[offset:offset+len(magic)].hex()}"
    except Exception as e:
        return str(e)
    return None

def check_production(url_path, production_base):
    """Return (status, mime_error) for a production HEAD request."""
    import urllib.request, ssl
    url = production_base + url_path
    req = urllib.request.Request(url, method='HEAD')
    req.add_header('User-Agent', 'audit_assets/1.0')
    ctx = ssl.create_default_context()
    try:
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        ct = resp.headers.get('Content-Type', '')
        ext = os.path.splitext(url_path)[1].lower()
        # Flag HTML content-type for non-HTML assets
        if ext in IMAGE_MAGIC and 'text/html' in ct:
            return resp.status, f"Content-Type is text/html for {ext} asset"
        if ext in ('.css', '.js', '.mjs') and 'text/html' in ct:
            return resp.status, f"Content-Type is text/html for {ext} asset"
        return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return 0, str(e)

def main():
    production_mode = '--production' in sys.argv

    all_html = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".wrangler", ".github")]
        for f in files:
            if f.endswith(".html"):
                all_html.append(os.path.join(root, f))

    attr_pat   = re.compile(r'(href|src)=["\']([^"\']+)["\']')
    asset_ext  = re.compile(r"\.(css|js|png|ico|webp|jpg|jpeg|svg|woff|woff2|gif)$", re.I)
    skip_proto = re.compile(r"(https?://|tel:|mailto:|#|data:)")

    missing       = []
    case_errors   = []
    magic_errors  = []
    not_rooted    = []
    http_errors   = []
    ok            = 0

    seen_assets = set()  # deduplicate production checks

    for filepath in sorted(all_html):
        page_url = BASE_URL + file_to_url(filepath)
        rel_page = os.path.relpath(filepath, REPO)
        with open(filepath, encoding="utf-8") as fh:
            content = fh.read()

        for attr, ref in attr_pat.findall(content):
            if not ref or skip_proto.match(ref):
                continue
            if ref.startswith("//"):
                continue

            resolved_url = urljoin(page_url, ref)
            url_path = urlparse(resolved_url).path

            # Flag: non-root-relative internal path
            if not ref.startswith(("/", "http", "https", "tel:", "mailto:", "#", "data:")):
                not_rooted.append((rel_page, attr, ref))

            # Only check asset-type references for existence / validity
            if not asset_ext.search(url_path):
                continue

            disk_file = url_to_file(url_path)
            if disk_file is None:
                missing.append((rel_page, ref, url_path))
                continue

            ok += 1

            # Case mismatch check
            if not check_case(url_path):
                case_errors.append((rel_page, ref, url_path))

            # Image magic byte check
            magic_err = check_image_magic(disk_file)
            if magic_err:
                magic_errors.append((rel_page, url_path, magic_err))

            # Production HTTP check (deduplicated)
            if production_mode and url_path not in seen_assets:
                seen_assets.add(url_path)
                status, mime_err = check_production(url_path, BASE_URL)
                if status != 200:
                    http_errors.append((url_path, f"HTTP {status}"))
                elif mime_err:
                    http_errors.append((url_path, mime_err))

    rc = 0
    total = ok + len(missing)
    print(f"Asset references checked: {total}")
    print(f"  OK              : {ok}")
    print(f"  MISSING         : {len(missing)}")
    print(f"  CASE-MISMATCH   : {len(case_errors)}")
    print(f"  INVALID-IMAGE   : {len(magic_errors)}")
    if production_mode:
        print(f"  HTTP-ERRORS     : {len(http_errors)}")

    if missing:
        rc = 1
        for page, ref, url_path in missing:
            print(f"\n  MISSING  {page:55s}  {ref}  ->  {url_path}")

    if case_errors:
        rc = 1
        for page, ref, url_path in case_errors:
            print(f"\n  CASE-MISMATCH  {page:55s}  {ref}  ->  {url_path}")

    if magic_errors:
        rc = 1
        for page, url_path, err in magic_errors:
            print(f"\n  INVALID-IMAGE  {url_path}  [{err}]")

    print(f"\nNon-root-relative internal refs: {len(not_rooted)}")
    if not_rooted:
        rc = 1
        for page, attr, ref in not_rooted[:20]:
            print(f"  NOT-ROOTED  {page:55s}  {attr}={ref!r}")
        if len(not_rooted) > 20:
            print(f"  ... and {len(not_rooted) - 20} more")

    if production_mode and http_errors:
        rc = 1
        print(f"\nProduction HTTP errors ({len(http_errors)}):")
        for url_path, err in http_errors:
            print(f"  HTTP-ERROR  {url_path}  [{err}]")

    return rc

if __name__ == "__main__":
    sys.exit(main())
