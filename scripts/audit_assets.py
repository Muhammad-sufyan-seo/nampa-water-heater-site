#!/usr/bin/env python3
"""
Static asset audit for nampawaterheater.com.

For every HTML file, resolves every href/src attribute value as a browser
would (relative to the page's clean URL) and checks whether the resulting
disk file exists. Reports missing files and any non-root-relative paths.

Exit code 0 = clean; 1 = issues found.
"""

import re, os, sys
from urllib.parse import urljoin, urlparse

BASE_URL = "https://nampawaterheater.com"
REPO     = "/home/user/nampa-water-heater-site"

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

def main():
    all_html = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".wrangler")]
        for f in files:
            if f.endswith(".html"):
                all_html.append(os.path.join(root, f))

    attr_pat   = re.compile(r'(href|src)=["\']([^"\']+)["\']')
    asset_ext  = re.compile(r"\.(css|js|png|ico|webp|jpg|jpeg|svg|woff|woff2)$", re.I)
    skip_proto = re.compile(r"(https?://|tel:|mailto:|#|data:)")

    missing      = []
    not_rooted   = []
    ok           = 0

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

            # Only check asset-type references for existence
            if not asset_ext.search(url_path):
                continue

            disk_file = url_to_file(url_path)
            if disk_file is None:
                missing.append((rel_page, ref, url_path))
            else:
                ok += 1

    rc = 0
    print(f"Asset references checked: {ok + len(missing)}")
    print(f"  OK      : {ok}")
    print(f"  MISSING : {len(missing)}")
    if missing:
        rc = 1
        for page, ref, url_path in missing:
            print(f"    MISSING  {page:55s}  {ref}  ->  {url_path}")

    print(f"\nNon-root-relative internal refs: {len(not_rooted)}")
    if not_rooted:
        rc = 1
        for page, attr, ref in not_rooted[:20]:
            print(f"    NOT-ROOTED  {page:55s}  {attr}={ref!r}")
        if len(not_rooted) > 20:
            print(f"    ... and {len(not_rooted) - 20} more")

    return rc

if __name__ == "__main__":
    sys.exit(main())
