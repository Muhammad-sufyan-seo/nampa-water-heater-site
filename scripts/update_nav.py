#!/usr/bin/env python3
"""Update navigation and footer in all existing HTML files.

HISTORICAL SCAFFOLDING SCRIPT — see the warning in build_pages.py. This was
used once to expand nav/footer links across all pre-existing pages to the
full 14-service/6-symptom/areas-hub structure. Safe to re-run if the nav
structure changes again, but review the diff before committing.
"""
import os
import re

BASE = "/home/user/nampa-water-heater-site"

def get_prefix(filepath):
    """Return the relative path prefix based on file depth."""
    rel = os.path.relpath(filepath, BASE)
    depth = len(rel.split(os.sep)) - 1
    if depth == 0:
        return "./"
    return "../" * depth

def nav_html(prefix, active_page=""):
    svc = prefix + "services/"
    sym = prefix + "symptoms/"
    areas = prefix + "areas/"
    root = prefix

    lines = []
    lines.append(f'      <nav class="main-nav" role="navigation" aria-label="Primary navigation">')
    lines.append(f'        <a href="{root}index.html">Home</a>')
    lines.append(f'        <div class="nav-dropdown">')
    lines.append(f'          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">')
    lines.append(f'            Services <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>')
    lines.append(f'          </button>')
    lines.append(f'          <div class="nav-dropdown-menu" role="menu">')

    service_items = [
        ("repair.html", "Water Heater Repair"),
        ("gas-repair.html", "Gas Water Heater Repair"),
        ("electric-repair.html", "Electric Water Heater Repair"),
        ("heat-pump-repair.html", "Heat Pump (Hybrid) Repair"),
        ("tankless-repair.html", "Tankless Water Heater Repair"),
        ("commercial-repair.html", "Commercial Water Heater Repair"),
        ("installation.html", "Water Heater Installation"),
        ("gas-installation.html", "Gas Water Heater Installation"),
        ("electric-installation.html", "Electric Water Heater Installation"),
        ("heat-pump-installation.html", "Heat Pump (Hybrid) Installation"),
        ("tankless-installation.html", "Tankless Water Heater Installation"),
        ("commercial-installation.html", "Commercial Water Heater Installation"),
        ("replacement.html", "Water Heater Replacement"),
        ("maintenance.html", "Water Heater Maintenance"),
    ]
    for slug, label in service_items:
        href = svc + slug
        active = ' class="active"' if active_page == slug else ''
        lines.append(f'            <a href="{href}"{active} role="menuitem">{label}</a>')

    lines.append(f'          </div>')
    lines.append(f'        </div>')

    # Common Issues dropdown
    lines.append(f'        <div class="nav-dropdown">')
    lines.append(f'          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">')
    lines.append(f'            Common Issues <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>')
    lines.append(f'          </button>')
    lines.append(f'          <div class="nav-dropdown-menu" role="menu">')
    symptom_items = [
        ("leaking.html", "Water Heater Leaking"),
        ("no-hot-water.html", "No Hot Water"),
        ("noise.html", "Water Heater Making Noise"),
        ("pilot-light.html", "Pilot Light Won\'t Stay Lit"),
        ("rusty-water.html", "Rusty or Discolored Water"),
        ("breaker-tripping.html", "Breaker Keeps Tripping"),
    ]
    for slug, label in symptom_items:
        href = sym + slug
        lines.append(f'            <a href="{href}" role="menuitem">{label}</a>')
    lines.append(f'          </div>')
    lines.append(f'        </div>')

    # Areas dropdown
    lines.append(f'        <div class="nav-dropdown">')
    lines.append(f'          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">')
    lines.append(f'            Areas We Serve <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>')
    lines.append(f'          </button>')
    lines.append(f'          <div class="nav-dropdown-menu" role="menu">')
    lines.append(f'            <a href="{areas}index.html" role="menuitem">All Service Areas</a>')
    lines.append(f'            <a href="{areas}downtown-nampa.html" role="menuitem">Downtown Nampa</a>')
    lines.append(f'            <a href="{areas}central-nampa.html" role="menuitem">Central Nampa</a>')
    lines.append(f'            <a href="{areas}south-nampa.html" role="menuitem">South Nampa</a>')
    lines.append(f'          </div>')
    lines.append(f'        </div>')
    lines.append(f'        <a href="{root}about.html">About</a>')
    lines.append(f'        <a href="{root}contact.html">Contact</a>')
    lines.append(f'        <a href="tel:+12089875152" class="header-cta" aria-label="Call (208) 987-5152">')
    lines.append(f'          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>')
    lines.append(f'          Call (208) 987-5152')
    lines.append(f'        </a>')
    lines.append(f'      </nav>')
    return "\n".join(lines)

def mobile_nav_html(prefix):
    svc = prefix + "services/"
    sym = prefix + "symptoms/"
    areas = prefix + "areas/"
    root = prefix
    phone_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'
    return f"""      <a href="tel:+12089875152" aria-label="Call (208) 987-5152">
          {phone_svg}
          Tap to Call: (208) 987-5152
        </a>
      </div>
      <div class="mobile-nav-section">Repair Services</div>
      <a href="{svc}repair.html">Water Heater Repair</a>
      <a href="{svc}gas-repair.html">Gas Water Heater Repair</a>
      <a href="{svc}electric-repair.html">Electric Water Heater Repair</a>
      <a href="{svc}heat-pump-repair.html">Heat Pump (Hybrid) Repair</a>
      <a href="{svc}tankless-repair.html">Tankless Water Heater Repair</a>
      <a href="{svc}commercial-repair.html">Commercial Water Heater Repair</a>
      <div class="mobile-nav-section">Installation Services</div>
      <a href="{svc}installation.html">Water Heater Installation</a>
      <a href="{svc}gas-installation.html">Gas Water Heater Installation</a>
      <a href="{svc}electric-installation.html">Electric Water Heater Installation</a>
      <a href="{svc}heat-pump-installation.html">Heat Pump (Hybrid) Installation</a>
      <a href="{svc}tankless-installation.html">Tankless Water Heater Installation</a>
      <a href="{svc}commercial-installation.html">Commercial Water Heater Installation</a>
      <div class="mobile-nav-section">Other Services</div>
      <a href="{svc}replacement.html">Water Heater Replacement</a>
      <a href="{svc}maintenance.html">Water Heater Maintenance</a>
      <div class="mobile-nav-section">Common Issues</div>
      <a href="{sym}leaking.html">Water Heater Leaking</a>
      <a href="{sym}no-hot-water.html">No Hot Water</a>
      <a href="{sym}noise.html">Water Heater Making Noise</a>
      <a href="{sym}pilot-light.html">Pilot Light Won't Stay Lit</a>
      <a href="{sym}rusty-water.html">Rusty or Discolored Water</a>
      <a href="{sym}breaker-tripping.html">Breaker Keeps Tripping</a>
      <div class="mobile-nav-section">Areas We Serve</div>
      <a href="{areas}index.html">All Service Areas</a>
      <a href="{areas}downtown-nampa.html">Downtown Nampa</a>
      <a href="{areas}central-nampa.html">Central Nampa</a>
      <a href="{areas}south-nampa.html">South Nampa</a>
      <div class="mobile-nav-section">Company</div>
      <a href="{root}about.html">About Us</a>
      <a href="{root}contact.html">Contact</a>"""

def footer_html(prefix):
    svc = prefix + "services/"
    areas = prefix + "areas/"
    root = prefix
    return f"""  <!-- FOOTER -->
  <footer class="site-footer" role="contentinfo">
    <div class="footer-inner">
      <div class="service-area-block">
        <h3>Our Nampa Service Area</h3>
        <p>We provide rapid water heater repair, replacement, and tankless installations throughout Nampa, ID, including Downtown, Central Nampa, South Nampa, and surrounding communities. <strong>Primary Zip Codes: 83651, 83686, 83687.</strong></p>
      </div>
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{root}index.html" class="site-logo" aria-label="Nampa Water Heater Pros — Home">
            <div class="logo-mark" aria-hidden="true">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C8.5 2 6 5 6 8c0 4 4 8 6 12 2-4 6-8 6-12 0-3-2.5-6-6-6zm0 8a2 2 0 110-4 2 2 0 010 4z"/></svg>
            </div>
            <div class="logo-text">Nampa Water Heater Pros<span>Nampa, Idaho · Service Area Business</span></div>
          </a>
          <p>Fast, reliable water heater repair, installation, and replacement throughout Nampa, ID.</p>
          <a href="tel:+12089875152" class="footer-phone">(208) 987-5152</a>
        </div>
        <div class="footer-col">
          <h4>Repair Services</h4>
          <ul>
            <li><a href="{svc}repair.html">Water Heater Repair</a></li>
            <li><a href="{svc}gas-repair.html">Gas Repair</a></li>
            <li><a href="{svc}electric-repair.html">Electric Repair</a></li>
            <li><a href="{svc}heat-pump-repair.html">Heat Pump Repair</a></li>
            <li><a href="{svc}tankless-repair.html">Tankless Repair</a></li>
            <li><a href="{svc}commercial-repair.html">Commercial Repair</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Installation &amp; More</h4>
          <ul>
            <li><a href="{svc}installation.html">Water Heater Installation</a></li>
            <li><a href="{svc}gas-installation.html">Gas Installation</a></li>
            <li><a href="{svc}electric-installation.html">Electric Installation</a></li>
            <li><a href="{svc}heat-pump-installation.html">Heat Pump Installation</a></li>
            <li><a href="{svc}tankless-installation.html">Tankless Installation</a></li>
            <li><a href="{svc}commercial-installation.html">Commercial Installation</a></li>
            <li><a href="{svc}replacement.html">Replacement</a></li>
            <li><a href="{svc}maintenance.html">Maintenance</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Areas We Serve</h4>
          <ul>
            <li><a href="{areas}index.html">All Service Areas</a></li>
            <li><a href="{areas}downtown-nampa.html">Downtown Nampa</a></li>
            <li><a href="{areas}central-nampa.html">Central Nampa</a></li>
            <li><a href="{areas}south-nampa.html">South Nampa</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="{root}about.html">About Us</a></li>
            <li><a href="{root}contact.html">Contact</a></li>
            <li><a href="{root}privacy-policy.html">Privacy Policy</a></li>
            <li><a href="{root}terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 Nampa Water Heater Pros. All rights reserved. Serving Nampa, ID 83651 · 83686 · 83687.</p>
        <div><a href="{root}privacy-policy.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="{root}terms.html">Terms of Service</a></div>
      </div>
    </div>
  </footer>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_prefix(filepath)

    # Build new nav HTML
    new_nav = nav_html(prefix)
    # Build new mobile nav content (everything between mobile-cta-bar <a> and the closing </nav>)
    new_mobile = mobile_nav_html(prefix)
    # Build new footer
    new_footer = footer_html(prefix)

    # Replace old nav block: from <nav class="main-nav" to </nav> that precedes the mobile-menu-btn
    content = re.sub(
        r'<nav class="main-nav"[^>]*>.*?</nav>(?=\s*\n\s*<button class="mobile-menu-btn")',
        new_nav,
        content,
        flags=re.DOTALL
    )

    # Replace mobile nav content: everything between mobile-cta-bar opening <a> and closing </nav>
    content = re.sub(
        r'(<div class="mobile-cta-bar">\s*)<a href="tel:[^"]*"[^>]*>.*?(</nav>)',
        lambda m: f'<div class="mobile-cta-bar">\n        {new_mobile}\n      {m.group(2)}',
        content,
        flags=re.DOTALL
    )

    # Replace footer block
    content = re.sub(
        r'<!-- FOOTER -->\s*<footer class="site-footer"[^>]*>.*?</footer>',
        new_footer,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {filepath}")

# Process all existing HTML files
for root_dir, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git', 'scripts', 'assets')]
    for fname in files:
        if fname.endswith('.html'):
            process_file(os.path.join(root_dir, fname))

print("Done updating existing files.")
