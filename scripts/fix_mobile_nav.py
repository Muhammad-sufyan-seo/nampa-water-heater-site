#!/usr/bin/env python3
import re, os

BASE = "/home/user/nampa-water-heater-site/nampa-water-heater"
PHONE_TEL = "+12089875152"
PHONE_DISPLAY = "(208) 987-5152"
PHONE_SVG18 = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'

def get_prefix(filepath):
    rel = os.path.relpath(filepath, BASE)
    depth = len(rel.split(os.sep)) - 1
    return "../" * depth if depth else ""

def mobile_nav_body(prefix):
    svc = prefix + "services/"
    sym = prefix + "symptoms/"
    areas = prefix + "areas/"
    root = prefix
    return f"""<a href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">
          {PHONE_SVG18}
          Tap to Call: {PHONE_DISPLAY}
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

files = [
    f"{BASE}/index.html",
    f"{BASE}/contact.html",
    f"{BASE}/services/repair.html",
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_prefix(filepath)
    new_mobile = mobile_nav_body(prefix)

    # Match from mobile-cta-bar div through the </nav> (allowing optional comment before <a> tag)
    pattern = re.compile(
        r'(<div class="mobile-cta-bar">\s*(?:<!--[^>]*-->\s*)?)<a href="tel:[^"]*"[^>]*>.*?(</nav>)',
        re.DOTALL
    )
    new_content, n = pattern.subn(
        lambda m: f'{m.group(1)}{new_mobile}\n    {m.group(2)}',
        content
    )
    if n == 0:
        print(f"WARNING: no match in {filepath}")
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed mobile nav in {filepath} ({n} replacement(s))")
