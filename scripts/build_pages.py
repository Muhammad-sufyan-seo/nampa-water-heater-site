#!/usr/bin/env python3
"""Generate all missing service and symptom pages for Nampa Water Heater Pros.

HISTORICAL SCAFFOLDING SCRIPT — re-running this will OVERWRITE the 14 service
pages with their original generated content, wiping out post-generation fixes
made directly to the HTML (entity-consistency @id/foundingDate additions,
stat bar, sidebar/cost-table class fixes, wording corrections, etc.). Do not
re-run against a live page without re-applying those fixes afterward, or use
it only as a reference for the page structure/template pattern.
"""

BASE = "/home/user/nampa-water-heater-site/nampa-water-heater"

PHONE_DISPLAY = "(208) 987-5152"
PHONE_TEL = "+12089875152"
BRAND = "Nampa Water Heater Pros"
CITY = "Nampa, ID"
DOMAIN = "https://nampawaterheater.com"

PHONE_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'
PHONE_SVG18 = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'

def header(prefix, title, desc, canonical, breadcrumbs, schema_json, active_page=""):
    svc = prefix + "services/"
    sym = prefix + "symptoms/"
    areas = prefix + "areas/"
    root = prefix

    bc_items = "".join([
        f'{{"@type": "ListItem", "position": {i+1}, "name": "{name}", "item": "{DOMAIN}/{url}"}}'
        for i, (name, url) in enumerate(breadcrumbs)
    ])
    bc_items = ",\n      ".join([
        f'{{"@type": "ListItem", "position": {i+1}, "name": "{name}", "item": "{DOMAIN}/{url}"}}'
        for i, (name, url) in enumerate(breadcrumbs)
    ])

    bc_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {bc_items}
    ]
  }}
  </script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{DOMAIN}/{canonical}">
  <link rel="stylesheet" href="{prefix}assets/css/style.css">

  {bc_schema}

{schema_json}
</head>
<body>

  <!-- HEADER -->
  <header class="site-header" role="banner">
    <div class="header-inner">
      <a href="{root}index.html" class="site-logo" aria-label="{BRAND} — Home">
        <div class="logo-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M12 2C8.5 2 6 5 6 8c0 4 4 8 6 12 2-4 6-8 6-12 0-3-2.5-6-6-6zm0 8a2 2 0 110-4 2 2 0 010 4z"/>
          </svg>
        </div>
        <div class="logo-text">
          {BRAND}
          <span>Nampa, Idaho · 83651 · 83686 · 83687</span>
        </div>
      </a>

      <nav class="main-nav" role="navigation" aria-label="Primary navigation">
        <a href="{root}index.html">Home</a>
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">
            Services <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>
          </button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="{svc}repair.html"{' class="active"' if active_page=='repair.html' else ''} role="menuitem">Water Heater Repair</a>
            <a href="{svc}gas-repair.html"{' class="active"' if active_page=='gas-repair.html' else ''} role="menuitem">Gas Water Heater Repair</a>
            <a href="{svc}electric-repair.html"{' class="active"' if active_page=='electric-repair.html' else ''} role="menuitem">Electric Water Heater Repair</a>
            <a href="{svc}heat-pump-repair.html"{' class="active"' if active_page=='heat-pump-repair.html' else ''} role="menuitem">Heat Pump (Hybrid) Repair</a>
            <a href="{svc}tankless-repair.html"{' class="active"' if active_page=='tankless-repair.html' else ''} role="menuitem">Tankless Water Heater Repair</a>
            <a href="{svc}commercial-repair.html"{' class="active"' if active_page=='commercial-repair.html' else ''} role="menuitem">Commercial Water Heater Repair</a>
            <a href="{svc}installation.html"{' class="active"' if active_page=='installation.html' else ''} role="menuitem">Water Heater Installation</a>
            <a href="{svc}gas-installation.html"{' class="active"' if active_page=='gas-installation.html' else ''} role="menuitem">Gas Water Heater Installation</a>
            <a href="{svc}electric-installation.html"{' class="active"' if active_page=='electric-installation.html' else ''} role="menuitem">Electric Water Heater Installation</a>
            <a href="{svc}heat-pump-installation.html"{' class="active"' if active_page=='heat-pump-installation.html' else ''} role="menuitem">Heat Pump (Hybrid) Installation</a>
            <a href="{svc}tankless-installation.html"{' class="active"' if active_page=='tankless-installation.html' else ''} role="menuitem">Tankless Water Heater Installation</a>
            <a href="{svc}commercial-installation.html"{' class="active"' if active_page=='commercial-installation.html' else ''} role="menuitem">Commercial Water Heater Installation</a>
            <a href="{svc}replacement.html"{' class="active"' if active_page=='replacement.html' else ''} role="menuitem">Water Heater Replacement</a>
            <a href="{svc}maintenance.html"{' class="active"' if active_page=='maintenance.html' else ''} role="menuitem">Water Heater Maintenance</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">
            Common Issues <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>
          </button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="{sym}leaking.html" role="menuitem">Water Heater Leaking</a>
            <a href="{sym}no-hot-water.html" role="menuitem">No Hot Water</a>
            <a href="{sym}noise.html" role="menuitem">Water Heater Making Noise</a>
            <a href="{sym}pilot-light.html" role="menuitem">Pilot Light Won't Stay Lit</a>
            <a href="{sym}rusty-water.html" role="menuitem">Rusty or Discolored Water</a>
            <a href="{sym}breaker-tripping.html" role="menuitem">Breaker Keeps Tripping</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">
            Areas We Serve <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor" aria-hidden="true"><path d="M0 0l5 6 5-6z"/></svg>
          </button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="{areas}index.html" role="menuitem">All Service Areas</a>
            <a href="{areas}downtown-nampa.html" role="menuitem">Downtown Nampa</a>
            <a href="{areas}central-nampa.html" role="menuitem">Central Nampa</a>
            <a href="{areas}south-nampa.html" role="menuitem">South Nampa</a>
          </div>
        </div>
        <a href="{root}about.html">About</a>
        <a href="{root}contact.html">Contact</a>
        <a href="tel:{PHONE_TEL}" class="header-cta" aria-label="Call {PHONE_DISPLAY}">
          {PHONE_SVG}
          Call {PHONE_DISPLAY}
        </a>
      </nav>

      <button class="mobile-menu-btn" id="mobile-menu-btn" aria-label="Open navigation menu" aria-expanded="false" aria-controls="mobile-nav">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="menu-icon">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </div>
    <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation">
      <div class="mobile-cta-bar">
        <a href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">
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
      <a href="{root}contact.html">Contact</a>
    </nav>
  </header>"""


def breadcrumb_nav(crumbs, root):
    """crumbs: list of (label, href) tuples, last is current page (no href needed)"""
    parts = []
    for i, (label, href) in enumerate(crumbs[:-1]):
        parts.append(f'<a href="{root}{href}">{label}</a>')
        parts.append('<span aria-hidden="true">›</span>')
    parts.append(f'<span aria-current="page">{crumbs[-1][0]}</span>')
    return f"""
  <!-- BREADCRUMB -->
  <nav class="breadcrumb" aria-label="Breadcrumb navigation">
    <div class="breadcrumb-inner">
      {" ".join(parts)}
    </div>
  </nav>"""


def footer(prefix):
    svc = prefix + "services/"
    areas = prefix + "areas/"
    root = prefix
    return f"""
  <!-- FOOTER -->
  <footer class="site-footer" role="contentinfo">
    <div class="footer-inner">
      <div class="service-area-block">
        <h3>Our Nampa Service Area</h3>
        <p>We provide rapid water heater repair, replacement, and tankless installations throughout Nampa, ID, including Downtown, Central Nampa, South Nampa, and surrounding communities. <strong>Primary Zip Codes: 83651, 83686, 83687.</strong></p>
      </div>
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{root}index.html" class="site-logo" aria-label="{BRAND} — Home">
            <div class="logo-mark" aria-hidden="true">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C8.5 2 6 5 6 8c0 4 4 8 6 12 2-4 6-8 6-12 0-3-2.5-6-6-6zm0 8a2 2 0 110-4 2 2 0 010 4z"/></svg>
            </div>
            <div class="logo-text">{BRAND}<span>Nampa, Idaho · Service Area Business</span></div>
          </a>
          <p>Fast, reliable water heater repair, installation, and replacement throughout Nampa, ID.</p>
          <a href="tel:{PHONE_TEL}" class="footer-phone">{PHONE_DISPLAY}</a>
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
        <p>&copy; 2025 {BRAND}. All rights reserved. Serving Nampa, ID 83651 · 83686 · 83687.</p>
        <div><a href="{root}privacy-policy.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="{root}terms.html">Terms of Service</a></div>
      </div>
    </div>
  </footer>

  <div class="sticky-call-bar" role="complementary" aria-label="Call now">
    <a href="tel:{PHONE_TEL}" aria-label="Call {BRAND}">
      {PHONE_SVG18}
      Call {PHONE_DISPLAY} — Same-Day Service
      <small>Tap to call {BRAND}</small>
    </a>
  </div>

  <script src="{prefix}assets/js/main.js"></script>
</body>
</html>"""


def faq_schema(faqs):
    items = []
    for q, a in faqs:
        items.append(f'''      {{
        "@type": "Question",
        "name": "{q}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{a}"
        }}
      }}''')
    joined = ",\n".join(items)
    return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{joined}
    ]
  }}
  </script>"""


def service_schema(name, desc, price_range, service_type):
    return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{name}",
    "description": "{desc}",
    "provider": {{
      "@type": "LocalBusiness",
      "name": "{BRAND}",
      "telephone": "{PHONE_DISPLAY}",
      "areaServed": {{"@type": "City", "name": "Nampa", "addressRegion": "ID"}}
    }},
    "areaServed": {{"@type": "City", "name": "Nampa", "addressRegion": "ID"}},
    "serviceType": "{service_type}",
    "offers": {{
      "@type": "Offer",
      "priceRange": "{price_range}",
      "priceCurrency": "USD"
    }}
  }}
  </script>"""


def cta_banner(headline, sub, cta_label, section_label=""):
    return f"""
    <!-- CTA BANNER -->
    <div class="cta-banner" role="complementary"{' aria-label="'+section_label+'"' if section_label else ''}>
      <div class="container">
        <h2>{headline}</h2>
        <p>{sub}</p>
        <a href="tel:{PHONE_TEL}" class="btn-white" aria-label="Call {BRAND}">
          {PHONE_SVG18}
          {cta_label}
        </a>
      </div>
    </div>"""


SIDEBAR_BRANDS = """
            <div class="sidebar-card">
              <h3>Brands We Service</h3>
              <ul>
                <li>Rheem</li>
                <li>A.O. Smith</li>
                <li>Bradford White</li>
                <li>American Standard</li>
                <li>Navien</li>
                <li>Rinnai</li>
                <li>Noritz</li>
                <li>State Water Heaters</li>
              </ul>
            </div>"""

def sidebar_related(links_html):
    return f"""
            <div class="sidebar-card">
              <h3>Related Services</h3>
              <ul>
{links_html}
              </ul>
            </div>"""

def sidebar_areas(prefix):
    areas = prefix + "areas/"
    return f"""
            <div class="sidebar-card">
              <h3>Service Areas</h3>
              <p style="font-size:0.85rem;color:var(--slate);">Serving <a href="{areas}downtown-nampa.html">Downtown Nampa</a>, <a href="{areas}central-nampa.html">Central Nampa</a>, and <a href="{areas}south-nampa.html">South Nampa</a>.</p>
            </div>"""

# ============================================================
# PAGE DATA
# ============================================================

PAGES = []

# ---- GAS REPAIR ----
PAGES.append({
    "path": f"{BASE}/services/gas-repair.html",
    "prefix": "../",
    "active": "gas-repair.html",
    "title": "Gas Water Heater Repair in Nampa, ID | Same-Day Service",
    "desc": "Licensed gas water heater repair in Nampa, Idaho. Pilot light failures, gas valve issues, thermocouple replacement. Same-day service. Call (208) 987-5152.",
    "canonical": "services/gas-repair.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Gas Water Heater Repair", "services/gas-repair.html")
    ],
    "schema_extra": service_schema(
        "Gas Water Heater Repair in Nampa, ID",
        "Professional gas water heater repair services in Nampa, Idaho. Thermocouple, pilot light, gas valve, and burner repairs. Same-day service available.",
        "$150 - $550", "Gas Water Heater Repair"
    ) + "\n" + faq_schema([
        ("What causes a gas water heater to stop working?",
         "The most common causes in Nampa homes are a failed thermocouple (the safety sensor that keeps the pilot lit), a dirty pilot orifice, a faulty gas valve, or a failed thermostat. Canyon County's hard water also causes sediment accumulation that stresses burner components."),
        ("How much does gas water heater repair cost in Nampa?",
         "Gas water heater repairs in Nampa typically run $150–$550. Thermocouple replacement is the most common fix at $150–$250. Gas valve or burner assembly replacement runs $300–$550. We provide upfront pricing before any work begins."),
        ("Is it safe to relight my gas water heater pilot myself?",
         "Relighting a pilot is generally safe if you follow the manufacturer's instructions printed on the unit. However, if the pilot won't stay lit, if you smell gas, or if you're unsure of the procedure, stop and call a licensed technician. A failed thermocouple—not user error—is the most common reason a pilot won't stay lit."),
        ("How long does a gas water heater last?",
         "Standard gas tank water heaters typically last 8–12 years. In Nampa, hard water (200–350 ppm) can reduce this by 1–3 years if annual sediment flushing isn't performed. Tankless gas units last 15–20 years with proper maintenance including periodic descaling.")
    ]),
    "h1": "Gas Water Heater Repair in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Gas Water Heater Specialists",
    "hero_lead": "Pilot light failure, no hot water, or a gas valve issue on your gas water heater? Our licensed technicians diagnose and repair all brands of gas storage and tankless water heaters throughout Nampa and the Treasure Valley—usually the same day you call.",
    "main_content": """
              <h2 id="gas-repair-content-heading">Gas Water Heater Repair: What We Fix</h2>
              <p>Gas water heaters are the most common type in Nampa homes, and they have unique failure modes that require gas-system expertise. Nampa Water Heater Pros technicians are licensed and trained specifically on gas appliances—from standing pilot units to modern electronic ignition systems.</p>

              <h3>Common Gas Water Heater Problems in Nampa</h3>
              <ul>
                <li><strong>Pilot Light Won't Stay Lit</strong> — Almost always a thermocouple failure. This safety device senses whether the pilot is burning; when it wears out, it cuts gas flow even when the pilot is lit. Replacement is a quick, affordable fix.</li>
                <li><strong>No Hot Water Despite Running</strong> — Often a faulty gas valve, failed thermostat, or burner that's clogged with sediment. Nampa's hard water (200–350 ppm) accelerates burner orifice fouling.</li>
                <li><strong>Lukewarm or Inconsistent Hot Water</strong> — Typically a thermostat set too low, a partially failing gas valve, or sediment buildup reducing the heat transfer between the burner and water.</li>
                <li><strong>Gas Smell Near the Unit</strong> — Shut off the gas supply immediately and call us or your gas utility. A gas odor near a water heater indicates a leak that must be addressed before any repair work begins.</li>
                <li><strong>Rumbling or Popping Sounds</strong> — Sediment accumulation on the burner surface. Canyon County's hard water deposits calcium carbonate on every surface the water contacts, including the tank bottom near the burner.</li>
                <li><strong>Pressure Relief Valve Discharge</strong> — The T&P valve releasing water indicates excess temperature or pressure inside the tank—a safety condition that needs immediate diagnosis.</li>
              </ul>

              <h3>Gas Water Heater Repair Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Repair Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Thermocouple replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Pilot assembly &amp; orifice cleaning</td><td>$150 – $220</td></tr>
                  <tr><td>Gas valve replacement</td><td>$300 – $450</td></tr>
                  <tr><td>Thermostat replacement</td><td>$200 – $320</td></tr>
                  <tr><td>Burner assembly replacement</td><td>$250 – $420</td></tr>
                  <tr><td>Sediment flush</td><td>$120 – $180</td></tr>
                  <tr><td>Pressure relief valve replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Flue/draft hood inspection &amp; repair</td><td>$100 – $250</td></tr>
                </tbody>
              </table>
              <p style="font-size:0.9rem;color:var(--slate);">Prices are estimates for the Nampa, ID market. Exact cost depends on unit age, brand, and part availability. We provide written quotes before starting any work.</p>

              <h3>Brands We Repair</h3>
              <p>We service all major gas water heater brands sold in the Treasure Valley: Rheem, A.O. Smith, Bradford White, American Standard, State Water Heaters, Noritz, Navien, and Rinnai. Our technicians carry common gas-system parts on every service vehicle to enable same-day repairs in most cases.</p>

              <h3>Gas Repair vs. Replacement</h3>
              <p>Not every gas water heater problem justifies a full replacement. Our technicians follow a straightforward decision framework: if your unit is under 8 years old and the repair costs less than 40% of a new unit, repair is almost always the better economic choice. For units 10+ years old or with severe corrosion, we'll give you an honest replacement recommendation—including what a new energy-efficient unit would save you on monthly gas bills.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Gas Repairs We Handle</h3>
              <ul>
                <li>Thermocouple replacement</li>
                <li>Pilot light failure</li>
                <li>Gas valve repair</li>
                <li>Burner assembly</li>
                <li>Thermostat replacement</li>
                <li>Sediment flush</li>
                <li>T&amp;P valve replacement</li>
                <li>Electronic ignition issues</li>
                <li>Flue &amp; venting inspection</li>
              </ul>
            </div>""",
    "cta_h2": "Gas Water Heater Problem in Nampa? Call Now.",
    "cta_sub": "Same-day gas water heater repair throughout Nampa, ID. Licensed &amp; insured. Upfront pricing on every job.",
    "cta_label": f"Call {PHONE_DISPLAY} — Same-Day Available",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="electric-repair.html">Electric Water Heater Repair</a></li>
                <li><a href="tankless-repair.html">Tankless Water Heater Repair</a></li>
                <li><a href="gas-installation.html">Gas Water Heater Installation</a></li>"""
})

# ---- ELECTRIC REPAIR ----
PAGES.append({
    "path": f"{BASE}/services/electric-repair.html",
    "prefix": "../",
    "active": "electric-repair.html",
    "title": "Electric Water Heater Repair in Nampa, ID | Same-Day Service",
    "desc": "Licensed electric water heater repair in Nampa, Idaho. Heating element replacement, thermostat failures, tripped breakers. Same-day service. Call (208) 987-5152.",
    "canonical": "services/electric-repair.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Electric Water Heater Repair", "services/electric-repair.html")
    ],
    "schema_extra": service_schema(
        "Electric Water Heater Repair in Nampa, ID",
        "Professional electric water heater repair in Nampa, Idaho. Heating element and thermostat replacement, breaker issues, sediment flushing. Same-day service.",
        "$120 - $500", "Electric Water Heater Repair"
    ) + "\n" + faq_schema([
        ("Why does my electric water heater have no hot water?",
         "The most common causes are a failed heating element (upper or lower), a tripped high-limit safety switch, a faulty thermostat, or a tripped circuit breaker. In Nampa, hard water mineral scale coating the lower heating element is a leading cause of element failure—scale acts as insulation that causes elements to overheat and burn out."),
        ("How much does it cost to replace a water heater heating element in Nampa?",
         "Heating element replacement in Nampa typically runs $120–$250 for labor plus $20–$60 for the element itself. If both elements need replacement, expect $200–$350 total. We provide upfront pricing before starting."),
        ("Why does my electric water heater breaker keep tripping?",
         "A repeatedly tripping breaker on a water heater circuit usually means a failed heating element that's drawing too much current, a short in the wiring, or a breaker that's reached the end of its life. Do not keep resetting it—call a licensed technician to diagnose the root cause."),
        ("Is it worth repairing an electric water heater?",
         "Yes, for units under 8–10 years old. Most electric water heater repairs are heating element or thermostat replacements—relatively inexpensive fixes that extend unit life significantly. For units over 12 years old with multiple issues, replacement makes more economic sense.")
    ]),
    "h1": "Electric Water Heater Repair in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Electric Water Heater Specialists",
    "hero_lead": "No hot water, a tripped breaker, or lukewarm water from your electric water heater? Nampa Water Heater Pros technicians diagnose and repair all electric water heater models—heating elements, thermostats, and wiring issues—with same-day service throughout Nampa.",
    "main_content": """
              <h2 id="electric-repair-content-heading">Electric Water Heater Repair: What We Fix</h2>
              <p>Electric water heaters are reliable but have specific failure points that require the right diagnostic approach. The most common problems we see in Nampa electric water heaters are heating element failures accelerated by the city's hard water, thermostat issues, and high-limit safety switch trips.</p>

              <h3>Common Electric Water Heater Problems in Nampa</h3>
              <ul>
                <li><strong>No Hot Water at All</strong> — Often a tripped high-limit switch (reset button on the thermostat access panel) or a completely failed upper heating element. Upper element failure means no hot water; lower element failure means running out quickly.</li>
                <li><strong>Running Out of Hot Water Too Fast</strong> — The lower heating element is likely coated in mineral scale (Nampa water runs 200–350 ppm hardness) or has failed. Scale deposits insulate the element, forcing it to work harder until it burns out.</li>
                <li><strong>Lukewarm Water</strong> — Faulty thermostat, element coated in scale, or thermostat set too low. Both upper and lower thermostats can fail independently.</li>
                <li><strong>Breaker Trips Repeatedly</strong> — A failing element that's drawing excess current, a wiring short, or an aging breaker. Never repeatedly reset a tripping water heater breaker—have it diagnosed professionally.</li>
                <li><strong>Water Around the Unit</strong> — Could be a failing pressure relief valve, a corroded tank, or loose connections at the element gaskets.</li>
                <li><strong>Discolored or Rusty Water</strong> — Often the anode rod has depleted, allowing tank corrosion to begin. Nampa's hard water depletes anode rods faster than average.</li>
              </ul>

              <h3>Electric Water Heater Repair Costs in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Repair Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Upper heating element replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Lower heating element replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Both elements replacement</td><td>$250 – $380</td></tr>
                  <tr><td>Thermostat replacement (one)</td><td>$130 – $230</td></tr>
                  <tr><td>High-limit reset &amp; diagnosis</td><td>$100 – $160</td></tr>
                  <tr><td>Anode rod replacement</td><td>$120 – $200</td></tr>
                  <tr><td>T&amp;P valve replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Sediment flush</td><td>$120 – $180</td></tr>
                </tbody>
              </table>

              <h3>The Hard-Water Factor in Nampa</h3>
              <p>Nampa's municipal water supply typically measures 200–350 ppm of calcium carbonate—well into the "hard" and "very hard" classifications. This mineral load deposits on heating elements, forming a scale coating that acts as insulation. The element must heat to higher temperatures to push heat through the scale, eventually burning itself out. Annual sediment flushing and element inspection is particularly important for Nampa electric water heater owners.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Electric Repairs We Handle</h3>
              <ul>
                <li>Heating element replacement</li>
                <li>Thermostat replacement</li>
                <li>High-limit switch reset</li>
                <li>Anode rod replacement</li>
                <li>Sediment flush</li>
                <li>T&amp;P valve replacement</li>
                <li>Element gasket replacement</li>
                <li>Wiring diagnosis</li>
              </ul>
            </div>""",
    "cta_h2": "Electric Water Heater Not Working in Nampa?",
    "cta_sub": "Same-day electric water heater repair throughout Nampa, ID. Licensed &amp; insured. Upfront pricing.",
    "cta_label": f"Call {PHONE_DISPLAY} — Same-Day Service",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="gas-repair.html">Gas Water Heater Repair</a></li>
                <li><a href="electric-installation.html">Electric Water Heater Installation</a></li>
                <li><a href="../symptoms/breaker-tripping.html">Breaker Keeps Tripping</a></li>"""
})

# ---- HEAT PUMP REPAIR ----
PAGES.append({
    "path": f"{BASE}/services/heat-pump-repair.html",
    "prefix": "../",
    "active": "heat-pump-repair.html",
    "title": "Heat Pump Water Heater Repair in Nampa, ID | Hybrid Water Heater Service",
    "desc": "Expert heat pump (hybrid) water heater repair in Nampa, Idaho. Error codes, compressor issues, refrigerant, fan motor. Same-day service. Call (208) 987-5152.",
    "canonical": "services/heat-pump-repair.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Heat Pump Water Heater Repair", "services/heat-pump-repair.html")
    ],
    "schema_extra": service_schema(
        "Heat Pump Water Heater Repair in Nampa, ID",
        "Specialized heat pump and hybrid water heater repair in Nampa, Idaho. Error codes, compressor, fan motor, refrigerant, and control board diagnostics.",
        "$200 - $800", "Heat Pump Water Heater Repair"
    ) + "\n" + faq_schema([
        ("How long do heat pump water heaters last?",
         "Heat pump water heaters typically last 13–15 years with proper maintenance—significantly longer than conventional tank units. In Nampa, the refrigerant circuit should be inspected every few years and the air filter cleaned monthly to maintain efficiency."),
        ("What are common heat pump water heater error codes?",
         "Common error codes vary by brand but often indicate issues with the fan motor (E01/F01 codes), refrigerant pressure (E02), temperature sensor faults, or control board errors. Always check your owner's manual for brand-specific code meanings. If the unit switches to electric-only mode (bypassing the heat pump), the compressor or refrigerant circuit needs professional diagnosis."),
        ("Can a heat pump water heater be repaired, or does it need replacement?",
         "Many heat pump water heater issues—error codes, fan motor failure, control board, thermistors—are repairable at a cost much lower than replacement ($200–$500 vs. $1,400–$2,000+). Compressor failure is the main exception: compressor replacement often approaches the cost of a new unit, making replacement the better value for units over 8 years old."),
        ("Why is my heat pump water heater in emergency/electric-only mode?",
         "Emergency mode means the heat pump circuit has been bypassed and the unit is running on conventional electric resistance heating, which uses 2–3× more electricity. This typically happens when the unit detects a problem with the compressor, refrigerant pressure, or fan motor, or when ambient temperatures drop too low for heat pump operation. Call us for a diagnostic.")
    ]),
    "h1": "Heat Pump Water Heater Repair in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Hybrid Water Heater Specialists",
    "hero_lead": "Error codes, efficiency loss, or your heat pump water heater stuck in electric-only mode? Nampa Water Heater Pros has the specialized training to diagnose and repair heat pump and hybrid water heater systems—the same day you call.",
    "main_content": """
              <h2 id="heat-pump-repair-content-heading">Heat Pump Water Heater Repair in Nampa</h2>
              <p>Heat pump (hybrid) water heaters are significantly more energy-efficient than conventional electric units, but they have more complex components that require specialized repair expertise. Nampa Water Heater Pros technicians are trained on the heat pump circuit—compressor, refrigerant, fan motor, and control systems—in addition to the standard electric backup elements.</p>

              <h3>Common Heat Pump Water Heater Problems</h3>
              <ul>
                <li><strong>Error Codes / Display Faults</strong> — Modern heat pump water heaters have diagnostic systems that display error codes when something is wrong. Common codes relate to fan motor, compressor, temperature sensors, or refrigerant pressure. We diagnose and clear codes properly—not just reset them.</li>
                <li><strong>Unit Running in Electric-Only (Emergency) Mode</strong> — This means the heat pump circuit has failed or been bypassed. You're still getting hot water, but at 2–3× the energy cost. The most common causes are fan motor failure, low refrigerant, or a control board issue.</li>
                <li><strong>No Hot Water at All</strong> — Could be a control board failure, a failed compressor (rare but possible), or a failed electric backup element.</li>
                <li><strong>Inadequate Hot Water / Long Recovery</strong> — Refrigerant charge issues, a dirty air filter restricting airflow, or a degraded compressor reduce heat pump efficiency and extend recovery times.</li>
                <li><strong>Condensate Leaking</strong> — Heat pump water heaters produce condensation as a normal part of operation. If condensate is pooling excessively, the drain line may be clogged or the unit is positioned on an uneven surface.</li>
                <li><strong>Loud Operation</strong> — Fan motor bearing wear, loose housing panels, or refrigerant issues can cause unusual noise from heat pump units.</li>
              </ul>

              <h3>Heat Pump Repair Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Repair Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Fan motor replacement</td><td>$250 – $450</td></tr>
                  <tr><td>Thermistor / sensor replacement</td><td>$150 – $300</td></tr>
                  <tr><td>Control board replacement</td><td>$350 – $650</td></tr>
                  <tr><td>Refrigerant recharge (if applicable)</td><td>$300 – $500</td></tr>
                  <tr><td>Compressor replacement</td><td>$600 – $1,000+</td></tr>
                  <tr><td>Electric backup element replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Condensate drain clearing</td><td>$80 – $150</td></tr>
                </tbody>
              </table>
              <p style="font-size:0.9rem;color:var(--slate);">Note: When compressor replacement approaches the cost of a new unit, we'll give you an honest recommendation. A new heat pump water heater qualifies for the federal 30% energy tax credit under the Inflation Reduction Act.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Heat Pump Repairs</h3>
              <ul>
                <li>Error code diagnosis</li>
                <li>Fan motor replacement</li>
                <li>Thermistor replacement</li>
                <li>Control board diagnosis</li>
                <li>Refrigerant inspection</li>
                <li>Backup element service</li>
                <li>Condensate drain clearing</li>
                <li>Air filter service</li>
              </ul>
            </div>""",
    "cta_h2": "Heat Pump Water Heater Issues in Nampa?",
    "cta_sub": "Specialized heat pump water heater diagnostics and repair throughout Nampa, ID. Same-day service available.",
    "cta_label": f"Call {PHONE_DISPLAY} for Heat Pump Repair",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="electric-repair.html">Electric Water Heater Repair</a></li>
                <li><a href="heat-pump-installation.html">Heat Pump Installation</a></li>"""
})

# ---- TANKLESS REPAIR ----
PAGES.append({
    "path": f"{BASE}/services/tankless-repair.html",
    "prefix": "../",
    "active": "tankless-repair.html",
    "title": "Tankless Water Heater Repair in Nampa, ID | Error Code Service",
    "desc": "Tankless water heater repair in Nampa, Idaho. Error codes, descaling, flow sensors, ignition failures. All brands. Same-day service. Call (208) 987-5152.",
    "canonical": "services/tankless-repair.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Tankless Water Heater Repair", "services/tankless-repair.html")
    ],
    "schema_extra": service_schema(
        "Tankless Water Heater Repair in Nampa, ID",
        "Expert tankless water heater repair in Nampa, Idaho. Error code diagnosis, descaling for hard water, flow sensor, igniter, and heat exchanger service. All brands.",
        "$150 - $700", "Tankless Water Heater Repair"
    ) + "\n" + faq_schema([
        ("Why does my tankless water heater keep showing an error code?",
         "Error codes on tankless water heaters in Nampa most commonly indicate: scale buildup in the heat exchanger from hard water (this is critical in Nampa where water runs 200–350 ppm), flow sensor issues, ignition failures, venting problems, or low water pressure. The code displayed (like Navien E003, Rinnai Code 11, or Noritz Code 11) points to the specific system affected."),
        ("How often does a tankless water heater need to be descaled in Nampa?",
         "In Nampa, we recommend annual descaling due to the city's hard water (200–350 ppm calcium carbonate). Without regular descaling, mineral scale builds up in the heat exchanger, reducing efficiency, triggering error codes, and eventually causing heat exchanger failure. Annual service is the single most important maintenance item for Nampa tankless unit owners."),
        ("What is the average cost to repair a tankless water heater?",
         "Tankless water heater repairs in Nampa typically range from $150 for a flow sensor or igniter replacement to $500–$700 for a heat exchanger that requires chemical descaling or part replacement. Descaling service (annual maintenance) runs $150–$250."),
        ("Can a tankless water heater be repaired, or do I need a new one?",
         "Most tankless water heater problems are repairable. Common serviceable issues include flow sensors, igniters, flame sensors, venting blockages, and scale buildup. Heat exchanger replacement is expensive but sometimes worthwhile on units under 10 years old. For units 15+ years old with heat exchanger failure, replacement is usually the better value.")
    ]),
    "h1": "Tankless Water Heater Repair in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Tankless Water Heater Specialists",
    "hero_lead": "Error codes, no ignition, or cold water surprises from your tankless water heater? Nampa Water Heater Pros specializes in all major tankless brands—Navien, Rinnai, Noritz, Rheem, and more. Annual descaling is critical in Nampa's hard-water market. Call us for same-day service.",
    "main_content": """
              <h2 id="tankless-repair-content-heading">Tankless Water Heater Repair in Nampa</h2>
              <p>Tankless water heaters offer endless hot water and significant energy savings, but they require regular maintenance—especially in Nampa where hard water (200–350 ppm) accelerates scale buildup inside heat exchangers. Nampa Water Heater Pros technicians are factory-trained on all major tankless brands sold in Idaho.</p>

              <h3>Common Tankless Water Heater Problems in Nampa</h3>
              <ul>
                <li><strong>Error Codes</strong> — Modern tankless units display specific error codes for each fault. We carry reference guides for all major brands (Navien, Rinnai, Noritz, Rheem, A.O. Smith) and can diagnose error codes accurately—not just reset them and hope for the best.</li>
                <li><strong>No Ignition / Code 11 / Code 111</strong> — Ignition failure errors (one of the most common) indicate a faulty igniter, flame sensor, gas supply issue, or blocked venting. Nampa's elevation (~2,600 ft) also affects combustion airflow slightly.</li>
                <li><strong>Cold Water Sandwich Effect</strong> — Brief bursts of cold water mid-shower are often a flow sensor calibration issue or inlet temperature fluctuation, not a unit failure.</li>
                <li><strong>Low Hot Water Pressure from Tankless</strong> — Scale buildup in the cold water inlet filter screen or heat exchanger restricts flow. In Nampa, inlet screens need cleaning every 6 months.</li>
                <li><strong>Unit Won't Fire Above Minimum Flow</strong> — The flow sensor may be partially blocked by scale, reporting flow rates below the unit's activation threshold.</li>
                <li><strong>Scale-Related Heat Exchanger Failure</strong> — Without annual descaling in Nampa's hard-water environment, scale accumulates inside the heat exchanger, reducing heat transfer efficiency and eventually cracking coils under thermal stress.</li>
              </ul>

              <h3>Annual Descaling: Critical for Nampa Tankless Units</h3>
              <p>Nampa's hard water deposits calcium carbonate at roughly 3× the rate of soft-water markets. Without annual descaling (flushing with food-grade citric acid solution), your tankless unit's heat exchanger will scale up within 2–3 years, triggering error codes and reducing efficiency by 10–30%. We offer annual maintenance plans that include descaling, inlet filter cleaning, and a full system inspection.</p>

              <h3>Tankless Repair Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Service Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Annual descaling service</td><td>$150 – $250</td></tr>
                  <tr><td>Inlet filter cleaning</td><td>$80 – $120</td></tr>
                  <tr><td>Igniter replacement</td><td>$200 – $350</td></tr>
                  <tr><td>Flame sensor replacement</td><td>$150 – $280</td></tr>
                  <tr><td>Flow sensor replacement</td><td>$180 – $300</td></tr>
                  <tr><td>Gas valve repair/replacement</td><td>$300 – $550</td></tr>
                  <tr><td>Heat exchanger replacement</td><td>$500 – $900</td></tr>
                  <tr><td>Venting inspection &amp; repair</td><td>$100 – $300</td></tr>
                </tbody>
              </table>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Tankless Services</h3>
              <ul>
                <li>Error code diagnosis</li>
                <li>Annual descaling</li>
                <li>Inlet filter cleaning</li>
                <li>Igniter replacement</li>
                <li>Flow sensor repair</li>
                <li>Gas valve service</li>
                <li>Venting inspection</li>
                <li>Heat exchanger service</li>
              </ul>
            </div>""",
    "cta_h2": "Tankless Water Heater Issues in Nampa?",
    "cta_sub": "Same-day tankless repair and annual descaling service throughout Nampa, ID. Licensed &amp; insured.",
    "cta_label": f"Call {PHONE_DISPLAY} — Tankless Specialists",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="tankless-installation.html">Tankless Installation</a></li>
                <li><a href="maintenance.html">Water Heater Maintenance</a></li>"""
})

# ---- COMMERCIAL REPAIR ----
PAGES.append({
    "path": f"{BASE}/services/commercial-repair.html",
    "prefix": "../",
    "active": "commercial-repair.html",
    "title": "Commercial Water Heater Repair in Nampa, ID | Business Water Heater Service",
    "desc": "Commercial water heater repair in Nampa, Idaho for restaurants, apartments, offices, and light industrial. Large tank, tankless, and booster repair. Call (208) 987-5152.",
    "canonical": "services/commercial-repair.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Commercial Water Heater Repair", "services/commercial-repair.html")
    ],
    "schema_extra": service_schema(
        "Commercial Water Heater Repair in Nampa, ID",
        "Commercial water heater repair services in Nampa, Idaho. Restaurants, multi-family, offices, and light industrial. Large-capacity tank and commercial tankless systems.",
        "$200 - $1200", "Commercial Water Heater Repair"
    ) + "\n" + faq_schema([
        ("What types of commercial water heaters do you repair in Nampa?",
         "We repair commercial storage tank water heaters (40–100+ gallon), commercial tankless systems, point-of-use units, and booster heaters used in restaurant dishwasher applications. We service gas and electric commercial units from Rheem, A.O. Smith, Bradford White, American Standard, Noritz, Navien, and Rinnai."),
        ("How quickly can you respond to a commercial water heater emergency in Nampa?",
         "We prioritize commercial calls, particularly for food service operations where hot water is required for health code compliance. We target same-day response for commercial emergencies in the Nampa area."),
        ("What causes commercial water heaters to fail more often than residential units?",
         "Commercial water heaters experience higher demand cycles, which accelerates wear on heating elements, thermostats, and anode rods. Nampa's hard water (200–350 ppm) compounds this through sediment accumulation. Commercial units that lack a quarterly sediment flush schedule fail significantly earlier than properly maintained units."),
        ("Are commercial water heater repairs more expensive than residential?",
         "Commercial repairs typically cost more due to larger components, higher-capacity parts, and sometimes more complex multi-unit configurations. Expect $200–$600 for most common repairs on standard commercial units, with larger systems or complete control board replacements running higher.")
    ]),
    "h1": "Commercial Water Heater Repair in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Commercial Water Heater Specialists",
    "hero_lead": "A failed commercial water heater is a business emergency—especially for restaurants, hotels, or multi-family properties. Nampa Water Heater Pros handles commercial water heater repair for businesses throughout Nampa and the Treasure Valley, with priority response for food service and hospitality operations.",
    "main_content": """
              <h2 id="commercial-repair-content-heading">Commercial Water Heater Repair in Nampa</h2>
              <p>Commercial water heaters face heavier demand cycles than residential units and fail in ways that impact business operations. Our technicians are experienced with large-capacity storage systems, commercial tankless units, and booster heater configurations common in Nampa's restaurant and hospitality sectors.</p>

              <h3>Commercial Water Heater Types We Service</h3>
              <ul>
                <li><strong>Large-Capacity Storage Units (40–100+ gallon)</strong> — Gas and electric commercial storage heaters for restaurants, hotels, apartments, and office buildings.</li>
                <li><strong>Commercial Tankless Systems</strong> — High-output gas tankless units for applications requiring continuous hot water delivery.</li>
                <li><strong>Booster Heaters</strong> — Inline booster units that raise water temperature to 140–180°F for restaurant dishwasher compliance. These require specialized service.</li>
                <li><strong>Point-of-Use Commercial Units</strong> — Small electric units at individual sinks in medical offices, salons, and light commercial settings.</li>
                <li><strong>Multi-Unit Configurations</strong> — Manifolded tankless systems or stacked storage units for high-demand commercial properties.</li>
              </ul>

              <h3>Common Commercial Water Heater Failures</h3>
              <ul>
                <li>Heating element failure in electric commercial units</li>
                <li>Gas valve, burner, or pilot assembly failure</li>
                <li>Thermostat and high-limit control failures</li>
                <li>Sediment accumulation (especially critical with Nampa hard water)</li>
                <li>Anode rod depletion leading to tank corrosion</li>
                <li>Pressure relief valve failure or pressure issues</li>
                <li>Booster heater thermostat failure (affecting dishwasher NSF compliance)</li>
                <li>Commercial tankless scale buildup and error codes</li>
              </ul>

              <h3>Priority Response for Food Service</h3>
              <p>Restaurants operating under Canyon County Health Department regulations require water temperatures that meet NSF/ANSI standards for commercial dishwashing. A failed booster heater or commercial water heater can trigger a health code violation. We prioritize food service calls for same-day response throughout Nampa.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Commercial Services</h3>
              <ul>
                <li>Large-capacity tank repair</li>
                <li>Commercial tankless repair</li>
                <li>Booster heater service</li>
                <li>Point-of-use repair</li>
                <li>Multi-unit systems</li>
                <li>Priority food service response</li>
                <li>Quarterly maintenance plans</li>
              </ul>
            </div>""",
    "cta_h2": "Commercial Water Heater Down in Nampa?",
    "cta_sub": "Priority commercial water heater repair throughout Nampa, ID. Same-day response for food service and hospitality operations.",
    "cta_label": f"Call {PHONE_DISPLAY} — Commercial Priority Line",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="commercial-installation.html">Commercial Installation</a></li>
                <li><a href="maintenance.html">Water Heater Maintenance</a></li>"""
})

# ---- GAS INSTALLATION ----
PAGES.append({
    "path": f"{BASE}/services/gas-installation.html",
    "prefix": "../",
    "active": "gas-installation.html",
    "title": "Gas Water Heater Installation in Nampa, ID | Licensed & Insured",
    "desc": "Gas water heater installation in Nampa, Idaho. New installs, upgrades, tank-to-tankless conversions. Licensed, permit-ready. Same-day quotes. Call (208) 987-5152.",
    "canonical": "services/gas-installation.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/installation.html"), ("Gas Water Heater Installation", "services/gas-installation.html")
    ],
    "schema_extra": service_schema(
        "Gas Water Heater Installation in Nampa, ID",
        "Professional gas water heater installation in Nampa, Idaho. Tank and tankless systems, code-compliant permits, seismic strapping, and proper gas line connection.",
        "$800 - $2,500", "Gas Water Heater Installation"
    ) + "\n" + faq_schema([
        ("How much does gas water heater installation cost in Nampa?",
         "Gas water heater installation in Nampa typically runs $800–$1,400 for a standard tank replacement (unit + labor). A new high-efficiency gas tank unit runs $500–$900 for the unit, plus $300–$500 in labor. Tankless gas installation runs $1,500–$2,500+ due to gas line sizing, venting, and condensate drain requirements."),
        ("Do I need a permit for gas water heater installation in Nampa?",
         "Yes. The City of Nampa and Canyon County require permits for water heater installations. Permit requirements include inspecting the gas connections, venting, and seismic strapping. All installations we perform include permit management and inspection scheduling."),
        ("How long does gas water heater installation take?",
         "Standard tank-for-tank gas water heater replacement takes 2–3 hours including draining the old unit, disconnecting gas and water lines, installing the new unit, and testing all connections. Tankless installations or gas line upgrades take longer—typically 4–8 hours."),
        ("What size gas water heater do I need for my Nampa home?",
         "For most Nampa single-family homes: 40-gallon for 1–3 people, 50-gallon for 3–4 people, 75-gallon for 4–6 people. For tankless, the right BTU rating depends on simultaneous demand and Nampa's cold groundwater temperature (approximately 55°F in winter). We'll size the unit correctly during your estimate.")
    ]),
    "h1": "Gas Water Heater Installation in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Licensed Gas Water Heater Installers",
    "hero_lead": "New gas water heater installation, tank-to-tankless upgrade, or replacement of a failed unit? Nampa Water Heater Pros handles all gas water heater installations throughout Nampa—including permits, gas line work, seismic strapping, and code-compliant venting.",
    "main_content": """
              <h2 id="gas-install-content-heading">Gas Water Heater Installation in Nampa</h2>
              <p>Gas water heaters remain the most popular choice in Nampa and the Treasure Valley, offering fast recovery times and lower operating costs than electric units in Idaho's natural gas market. Whether you're replacing a failed unit, upgrading to a higher-efficiency model, or making the switch to tankless, our licensed installers handle the complete job.</p>

              <h3>What's Included in Our Gas Water Heater Installations</h3>
              <ul>
                <li><strong>Old Unit Removal</strong> — We drain, disconnect, and haul away your old water heater. No disposal headaches.</li>
                <li><strong>Gas Line Inspection &amp; Connection</strong> — We inspect the existing gas flex connector for age and condition, replacing if needed. Tankless installations may require gas line upsizing.</li>
                <li><strong>Proper Venting</strong> — Standard tank units use B-vent or direct-vent configurations. High-efficiency and condensing gas units require PVC venting. We ensure proper draft and code-compliant termination.</li>
                <li><strong>Seismic Strapping</strong> — Required by Idaho code and the IRC. All units are strapped to wall studs per current standards.</li>
                <li><strong>Permit Management</strong> — We pull the permit and schedule the required inspection with the City of Nampa or Canyon County.</li>
                <li><strong>Testing &amp; Commissioning</strong> — We light the pilot, set the thermostat to 120°F (safe household default), check for leaks at all connections, and confirm proper hot water delivery before we leave.</li>
              </ul>

              <h3>Gas Water Heater Installation Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Installation Type</th><th>Typical Total Cost (Unit + Labor)</th></tr>
                </thead>
                <tbody>
                  <tr><td>Standard 40-gal gas tank (like-for-like)</td><td>$850 – $1,200</td></tr>
                  <tr><td>High-efficiency 50-gal gas tank</td><td>$1,000 – $1,600</td></tr>
                  <tr><td>Gas tankless (standard install)</td><td>$1,500 – $2,200</td></tr>
                  <tr><td>Gas tankless (with gas line upgrade)</td><td>$2,000 – $3,000+</td></tr>
                  <tr><td>Power vent gas tank (no chimney)</td><td>$1,100 – $1,800</td></tr>
                </tbody>
              </table>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Installation Includes</h3>
              <ul>
                <li>Old unit removal &amp; haul-away</li>
                <li>Gas line inspection</li>
                <li>Code-compliant venting</li>
                <li>Seismic strapping</li>
                <li>Permit management</li>
                <li>Testing &amp; commissioning</li>
                <li>Thermostat set to 120°F</li>
              </ul>
            </div>""",
    "cta_h2": "Gas Water Heater Installation in Nampa — Get a Quote",
    "cta_sub": "Same-day installation available. Licensed, permit-ready installers throughout Nampa, ID.",
    "cta_label": f"Call {PHONE_DISPLAY} — Free Quote",
    "related_links": """                <li><a href="installation.html">Water Heater Installation</a></li>
                <li><a href="gas-repair.html">Gas Water Heater Repair</a></li>
                <li><a href="tankless-installation.html">Tankless Installation</a></li>"""
})

# ---- ELECTRIC INSTALLATION ----
PAGES.append({
    "path": f"{BASE}/services/electric-installation.html",
    "prefix": "../",
    "active": "electric-installation.html",
    "title": "Electric Water Heater Installation in Nampa, ID | Licensed Installers",
    "desc": "Electric water heater installation in Nampa, Idaho. Standard tank, heat pump upgrades. Licensed, permit-ready, seismic strapping included. Call (208) 987-5152.",
    "canonical": "services/electric-installation.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/installation.html"), ("Electric Water Heater Installation", "services/electric-installation.html")
    ],
    "schema_extra": service_schema(
        "Electric Water Heater Installation in Nampa, ID",
        "Professional electric water heater installation in Nampa, Idaho. Standard tank and heat pump hybrid systems. Code-compliant, permit-managed, seismic strapping included.",
        "$700 - $2,000", "Electric Water Heater Installation"
    ) + "\n" + faq_schema([
        ("How much does electric water heater installation cost in Nampa?",
         "Electric water heater installation in Nampa typically runs $700–$1,200 for a standard tank replacement (unit + labor). Heat pump (hybrid) electric installations cost $1,400–$2,000+ for the unit plus $300–$500 in labor. Pricing depends on unit size, brand, and whether electrical upgrades are needed."),
        ("Should I get a heat pump (hybrid) water heater instead of a standard electric tank?",
         "For most Nampa homeowners with sufficient space (at least 700 cubic feet of air around the unit), a heat pump water heater makes strong economic sense. Heat pump units use 2–3× less electricity than standard electric tanks and qualify for the federal 30% energy tax credit under the Inflation Reduction Act. The upfront premium pays back in 4–6 years for most Idaho households."),
        ("Do I need an electrical upgrade for a new electric water heater?",
         "Most standard electric water heater replacements (like-for-like) don't require electrical upgrades if the existing 240V/30A circuit is in good condition. Heat pump water heaters typically need a 240V/30A circuit. If you're adding a water heater to a location without an existing circuit, we'll coordinate with a licensed electrician."),
        ("How long does electric water heater installation take?",
         "Standard tank-for-tank electric water heater replacement takes 2–3 hours. Heat pump water heater installation may take 3–4 hours due to additional setup, condensate drain routing, and system commissioning.")
    ]),
    "h1": "Electric Water Heater Installation in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Electric Water Heater Installation",
    "hero_lead": "Standard electric tank replacement or upgrade to a heat pump water heater? Nampa Water Heater Pros installs all types of electric water heaters throughout Nampa—including permit management, seismic strapping, and proper electrical connections.",
    "main_content": """
              <h2 id="electric-install-content-heading">Electric Water Heater Installation in Nampa</h2>
              <p>Electric water heaters are a reliable choice for Nampa homes without gas service, or for those seeking the impressive efficiency of heat pump technology. Our licensed installers handle complete electric water heater installations, from standard tank replacements to full heat pump system upgrades.</p>

              <h3>Electric Water Heater Options for Nampa Homes</h3>
              <ul>
                <li><strong>Standard Electric Tank (40–80 gallon)</strong> — The most affordable installation option. Uses two electric resistance elements (upper and lower) to heat water. Recovery time is slower than gas, but upfront costs are lower and operation is simple and reliable.</li>
                <li><strong>Heat Pump (Hybrid) Water Heater</strong> — Moves heat from surrounding air into the water rather than generating heat directly—2–3× more efficient than standard electric. Qualifies for the federal 30% Residential Clean Energy Tax Credit. Requires adequate space (700+ cubic feet of unconditioned or semi-conditioned space).</li>
                <li><strong>Electric Tankless</strong> — On-demand electric heating for point-of-use applications. Whole-home electric tankless typically requires significant electrical service upgrades (100A+) and is rarely cost-effective in full-home applications.</li>
              </ul>

              <h3>Electric Installation Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Installation Type</th><th>Typical Total Cost (Unit + Labor)</th></tr>
                </thead>
                <tbody>
                  <tr><td>Standard 40-gal electric tank (like-for-like)</td><td>$750 – $1,100</td></tr>
                  <tr><td>Standard 50-gal electric tank</td><td>$850 – $1,200</td></tr>
                  <tr><td>80-gal electric tank</td><td>$1,000 – $1,600</td></tr>
                  <tr><td>Heat pump (hybrid) water heater</td><td>$1,400 – $2,200</td></tr>
                  <tr><td>Point-of-use electric unit</td><td>$400 – $700</td></tr>
                </tbody>
              </table>
              <p style="font-size:0.9rem;color:var(--slate);">Heat pump installations qualify for the federal 30% Residential Clean Energy Tax Credit (up to $2,000) under the Inflation Reduction Act—ask us about current eligibility.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Installation Includes</h3>
              <ul>
                <li>Old unit removal &amp; haul-away</li>
                <li>Electrical connection check</li>
                <li>Seismic strapping</li>
                <li>Permit management</li>
                <li>Condensate drain (heat pump)</li>
                <li>Full testing &amp; commissioning</li>
              </ul>
            </div>""",
    "cta_h2": "Electric Water Heater Installation in Nampa",
    "cta_sub": "Same-day installation available. Licensed, permit-ready. Heat pump upgrades available. Nampa, ID.",
    "cta_label": f"Call {PHONE_DISPLAY} — Get a Quote",
    "related_links": """                <li><a href="installation.html">Water Heater Installation</a></li>
                <li><a href="heat-pump-installation.html">Heat Pump Installation</a></li>
                <li><a href="electric-repair.html">Electric Water Heater Repair</a></li>"""
})

# ---- HEAT PUMP INSTALLATION ----
PAGES.append({
    "path": f"{BASE}/services/heat-pump-installation.html",
    "prefix": "../",
    "active": "heat-pump-installation.html",
    "title": "Heat Pump Water Heater Installation in Nampa, ID | Hybrid Water Heaters",
    "desc": "Heat pump water heater installation in Nampa, Idaho. Energy-efficient hybrid systems, tax credit eligible. Licensed installers. Same-day quotes. Call (208) 987-5152.",
    "canonical": "services/heat-pump-installation.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/installation.html"), ("Heat Pump Water Heater Installation", "services/heat-pump-installation.html")
    ],
    "schema_extra": service_schema(
        "Heat Pump Water Heater Installation in Nampa, ID",
        "Heat pump (hybrid) water heater installation in Nampa, Idaho. Energy Star certified, federal tax credit eligible. Licensed and permit-managed installation.",
        "$1,400 - $2,500", "Heat Pump Water Heater Installation"
    ) + "\n" + faq_schema([
        ("How much does heat pump water heater installation cost in Nampa?",
         "Heat pump water heater installation in Nampa typically runs $1,400–$2,500 total (unit + labor). The unit itself costs $1,000–$1,800; installation adds $300–$500. However, the federal 30% Residential Clean Energy Tax Credit can reduce your net cost by $400–$600, making the effective payback period 4–6 years for most Idaho households."),
        ("What are the requirements for a heat pump water heater in a Nampa home?",
         "Heat pump water heaters need at least 700 cubic feet of surrounding unconditioned or semi-conditioned space (a garage, basement, or utility room). They work best between 40°F and 90°F ambient temperature. A 240V/30A electrical circuit is required. They also produce condensate that must drain away from the unit."),
        ("Is a heat pump water heater worth it in Idaho?",
         "Yes, particularly for Idaho Power customers in Nampa. Heat pump water heaters use roughly 60–70% less electricity than standard electric resistance units. Idaho Power has historically offered rebates for qualifying installations, and the federal 30% tax credit makes the economics compelling. Most Nampa households see payback in 4–6 years."),
        ("What brands of heat pump water heaters do you install in Nampa?",
         "We install Rheem ProTerra, A.O. Smith Voltex, Bradford White AeroTherm, and American Standard heat pump water heaters—all Energy Star certified models that qualify for the federal tax credit.")
    ]),
    "h1": "Heat Pump Water Heater Installation in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Energy-Efficient Water Heating",
    "hero_lead": "Upgrade to a heat pump water heater and cut your water heating bill by up to 70%—while qualifying for the federal 30% Residential Clean Energy Tax Credit. Nampa Water Heater Pros installs Energy Star certified heat pump water heaters throughout Nampa with same-day quotes.",
    "main_content": """
              <h2 id="heat-pump-install-content-heading">Heat Pump Water Heater Installation in Nampa</h2>
              <p>Heat pump water heaters are the most energy-efficient water heating option available for electric customers in Nampa. By moving heat from surrounding air into the water rather than generating it directly, heat pump units achieve energy factors of 3.5–4.0 compared to 0.9 for standard electric resistance units. That translates to roughly 60–70% lower water heating electricity costs.</p>

              <h3>How Heat Pump Water Heaters Work</h3>
              <p>Heat pump water heaters operate like a refrigerator in reverse. A compressor extracts heat energy from the surrounding air and concentrates it into the water tank. They work most efficiently in spaces between 40°F and 90°F—making a Nampa garage, basement, or utility room an ideal installation location. Electric resistance backup elements kick in during peak demand or when ambient temperatures drop too low for efficient heat pump operation.</p>

              <h3>Federal Tax Credit: 30% Back</h3>
              <p>Under the Inflation Reduction Act (IRA), qualified heat pump water heaters are eligible for the Residential Clean Energy Tax Credit—30% of installation cost, up to $2,000, with no income limit. This credit directly reduces your federal tax liability. Ask us for current qualifying models when you call for a quote.</p>

              <h3>Installation Requirements</h3>
              <ul>
                <li>Minimum 700 cubic feet of surrounding air space</li>
                <li>240V/30A electrical circuit</li>
                <li>Ambient temperature 40°F–90°F (garage, basement, utility room)</li>
                <li>Condensate drain location within reach</li>
                <li>Ceiling height of at least 7 feet</li>
              </ul>

              <h3>Heat Pump Installation Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Item</th><th>Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Heat pump water heater unit (50–80 gal)</td><td>$1,000 – $1,800</td></tr>
                  <tr><td>Installation labor (standard)</td><td>$300 – $500</td></tr>
                  <tr><td>Condensate drain installation (if needed)</td><td>$100 – $200</td></tr>
                  <tr><td>Old unit removal &amp; disposal</td><td>Included</td></tr>
                  <tr><td>Federal tax credit (30%)</td><td>-$420 to -$600+</td></tr>
                  <tr><td><strong>Estimated net cost after credit</strong></td><td><strong>$800 – $1,900</strong></td></tr>
                </tbody>
              </table>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Heat Pump Installation</h3>
              <ul>
                <li>All Energy Star brands</li>
                <li>Federal tax credit guidance</li>
                <li>Old unit removal</li>
                <li>Condensate drain setup</li>
                <li>Permit management</li>
                <li>Full commissioning</li>
              </ul>
            </div>""",
    "cta_h2": "Ready to Upgrade to Heat Pump in Nampa?",
    "cta_sub": "Get a quote for heat pump water heater installation. Tax credit eligible. Licensed &amp; insured. Nampa, ID.",
    "cta_label": f"Call {PHONE_DISPLAY} — Free Installation Quote",
    "related_links": """                <li><a href="installation.html">Water Heater Installation</a></li>
                <li><a href="electric-installation.html">Electric Installation</a></li>
                <li><a href="heat-pump-repair.html">Heat Pump Repair</a></li>"""
})

# ---- TANKLESS INSTALLATION ----
PAGES.append({
    "path": f"{BASE}/services/tankless-installation.html",
    "prefix": "../",
    "active": "tankless-installation.html",
    "title": "Tankless Water Heater Installation in Nampa, ID | Endless Hot Water",
    "desc": "Tankless water heater installation in Nampa, Idaho. Gas and electric on-demand systems. Licensed installers, permit-managed, gas line sizing included. Call (208) 987-5152.",
    "canonical": "services/tankless-installation.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/installation.html"), ("Tankless Water Heater Installation", "services/tankless-installation.html")
    ],
    "schema_extra": service_schema(
        "Tankless Water Heater Installation in Nampa, ID",
        "Tankless water heater installation in Nampa, Idaho. Gas and electric on-demand systems. Gas line sizing, code-compliant venting, and permit management included.",
        "$1,500 - $3,500", "Tankless Water Heater Installation"
    ) + "\n" + faq_schema([
        ("How much does tankless water heater installation cost in Nampa?",
         "Tankless water heater installation in Nampa ranges from $1,500–$2,500 for gas units with an existing adequate gas line, up to $2,500–$3,500+ if gas line upsizing is needed. The unit itself runs $700–$1,400 for residential gas tankless; installation labor, gas line work, and venting add $500–$1,500. Electric tankless for point-of-use applications is $400–$800 total."),
        ("What size tankless water heater do I need for my Nampa home?",
         "Sizing depends on the number of simultaneous hot water demands and Nampa's groundwater temperature (~55°F in winter). A typical Nampa household of 2–4 people needs a unit rated at 180,000–199,000 BTU (for gas) to handle 2 simultaneous fixtures in winter. We size units based on your specific home's demand profile."),
        ("Do tankless water heaters need special maintenance in Nampa?",
         "Yes—annual descaling is critical. Nampa's hard water (200–350 ppm) deposits mineral scale inside the heat exchanger. Without annual descaling, scale accumulates within 2–3 years, triggering error codes, reducing efficiency, and potentially causing heat exchanger failure. This is the #1 maintenance requirement for Nampa tankless owners."),
        ("What brands of tankless water heaters do you install in Nampa?",
         "We install Navien, Rinnai, Noritz, Rheem, and A.O. Smith tankless water heaters. Navien and Rinnai are the most popular choices in Nampa—both have excellent efficiency ratings and strong local parts availability. We recommend brands with condensing technology for the best long-term efficiency in Idaho's natural gas market.")
    ]),
    "h1": "Tankless Water Heater Installation in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Endless Hot Water Specialists",
    "hero_lead": "Upgrade to on-demand hot water with a tankless water heater installation in Nampa. Our licensed technicians handle everything—gas line sizing, code-compliant venting, permits, and same-day annual descaling service to protect your investment in Nampa's hard-water environment.",
    "main_content": """
              <h2 id="tankless-install-content-heading">Tankless Water Heater Installation in Nampa</h2>
              <p>Tankless (on-demand) water heaters provide endless hot water, take up less space than tank units, and last 15–20 years with proper maintenance—significantly longer than the 8–12 year lifespan of traditional tanks. In Nampa's hard-water environment, choosing a tankless unit requires careful sizing and a commitment to annual descaling service.</p>

              <h3>Gas Tankless vs. Electric Tankless</h3>
              <p><strong>Gas tankless</strong> is the right choice for most Nampa whole-home applications. Gas units heat water rapidly (high BTU output), are not affected by Idaho's cold groundwater temperatures as severely, and cost less to operate than electric in Idaho's natural gas market.</p>
              <p><strong>Electric tankless</strong> is best suited for point-of-use applications (a single sink or bathroom addition) rather than whole-home use. Whole-home electric tankless requires very high amperage (100A+) and is rarely cost-effective in full-home applications.</p>

              <h3>What's Included in Our Tankless Installations</h3>
              <ul>
                <li>Gas line inspection and sizing for required BTU output</li>
                <li>Code-compliant PVC (condensing) or stainless steel (non-condensing) venting</li>
                <li>Condensate drain installation (condensing units)</li>
                <li>Water inlet filter installation (essential for Nampa hard water)</li>
                <li>Seismic strapping</li>
                <li>Permit management and inspection scheduling</li>
                <li>Unit programming and commissioning</li>
                <li>Descaling loop valve setup (strongly recommended for Nampa)</li>
              </ul>

              <h3>Tankless Installation Cost in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Installation Type</th><th>Typical Total Cost</th></tr>
                </thead>
                <tbody>
                  <tr><td>Gas tankless (standard install)</td><td>$1,500 – $2,200</td></tr>
                  <tr><td>Gas tankless + gas line upgrade</td><td>$2,000 – $3,200</td></tr>
                  <tr><td>Gas tankless + descaling loop setup</td><td>Add $200 – $350</td></tr>
                  <tr><td>Electric point-of-use tankless</td><td>$400 – $750</td></tr>
                </tbody>
              </table>
              <p style="font-size:0.9rem;color:var(--slate);">Annual descaling service in Nampa: $150–$250/year. We strongly recommend a maintenance plan for all Nampa tankless installations due to hard water conditions.</p>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Tankless Installation</h3>
              <ul>
                <li>Gas line sizing</li>
                <li>Code-compliant venting</li>
                <li>Inlet filter setup</li>
                <li>Descaling loop valve</li>
                <li>Permit management</li>
                <li>Unit commissioning</li>
                <li>Annual maintenance plans</li>
              </ul>
            </div>""",
    "cta_h2": "Tankless Water Heater Installation in Nampa",
    "cta_sub": "Endless hot water. 15–20 year lifespan. Licensed, permit-managed installation throughout Nampa, ID.",
    "cta_label": f"Call {PHONE_DISPLAY} — Get a Tankless Quote",
    "related_links": """                <li><a href="installation.html">Water Heater Installation</a></li>
                <li><a href="tankless-repair.html">Tankless Repair &amp; Descaling</a></li>
                <li><a href="maintenance.html">Annual Maintenance Plans</a></li>"""
})

# ---- COMMERCIAL INSTALLATION ----
PAGES.append({
    "path": f"{BASE}/services/commercial-installation.html",
    "prefix": "../",
    "active": "commercial-installation.html",
    "title": "Commercial Water Heater Installation in Nampa, ID | Business Water Heaters",
    "desc": "Commercial water heater installation in Nampa, Idaho. Large tank, commercial tankless, booster heaters for restaurants and multi-family. Licensed. Call (208) 987-5152.",
    "canonical": "services/commercial-installation.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/installation.html"), ("Commercial Water Heater Installation", "services/commercial-installation.html")
    ],
    "schema_extra": service_schema(
        "Commercial Water Heater Installation in Nampa, ID",
        "Commercial water heater installation in Nampa, Idaho. Large-capacity tank, commercial tankless, and booster heater systems for restaurants, apartments, and businesses.",
        "$1,500 - $8,000", "Commercial Water Heater Installation"
    ) + "\n" + faq_schema([
        ("What commercial water heater systems do you install in Nampa?",
         "We install commercial storage tank water heaters (40–100+ gallon), high-output commercial tankless systems, booster heaters for restaurant NSF compliance, and manifolded multi-unit configurations for apartment complexes and hotels."),
        ("How much does commercial water heater installation cost in Nampa?",
         "Commercial water heater installation in Nampa ranges from $1,500–$3,000 for standard commercial tank replacement to $4,000–$8,000+ for multi-unit commercial tankless systems or new construction installations requiring gas line sizing and commercial venting. We provide written quotes after a site assessment."),
        ("Do you handle commercial water heater installation permits in Nampa?",
         "Yes. Commercial water heater installations require commercial mechanical permits from the City of Nampa or Canyon County Building Department. We manage the permit process, schedule inspections, and ensure all work meets Idaho commercial plumbing code."),
        ("What maintenance schedule do commercial water heaters need in Nampa?",
         "Commercial water heaters in Nampa should be flushed and inspected quarterly due to high demand cycles and the city's hard water. Anode rod inspection is recommended annually. Commercial tankless systems require descaling twice yearly in Nampa's hard-water environment.")
    ]),
    "h1": "Commercial Water Heater Installation in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Commercial Water Heater Specialists",
    "hero_lead": "New construction, expansion, or replacement of aging commercial water heating equipment? Nampa Water Heater Pros installs commercial water heaters for restaurants, apartment complexes, hotels, and offices throughout Nampa—with proper commercial permitting and inspection compliance.",
    "main_content": """
              <h2 id="commercial-install-content-heading">Commercial Water Heater Installation in Nampa</h2>
              <p>Commercial water heater installations require sizing for peak demand loads, compliance with commercial mechanical codes, and often coordination with gas utility capacity upgrades. Our team has installed commercial water heating systems for restaurants, multi-family buildings, medical offices, and light industrial facilities throughout Nampa.</p>

              <h3>Commercial Applications We Serve</h3>
              <ul>
                <li><strong>Restaurants &amp; Food Service</strong> — NSF-compliant booster heaters for dish machines (140°F+ water temp), high-output commercial tanks for high-volume kitchens.</li>
                <li><strong>Apartment Complexes</strong> — Individual unit water heaters or central water heating systems for multi-family buildings.</li>
                <li><strong>Hotels &amp; Hospitality</strong> — High-capacity storage systems or commercial tankless manifolds for continuous hot water demand.</li>
                <li><strong>Medical &amp; Dental Offices</strong> — Code-compliant water heater systems meeting Idaho healthcare facility requirements.</li>
                <li><strong>Light Industrial</strong> — Process hot water systems for manufacturing or cleaning applications.</li>
                <li><strong>New Construction</strong> — Coordination with general contractors for rough-in and final connection of commercial water heating equipment.</li>
              </ul>

              <h3>Commercial Installation Process</h3>
              <ol>
                <li><strong>Site Assessment</strong> — We evaluate existing gas/electric capacity, venting routes, and hot water demand to properly size the system.</li>
                <li><strong>Equipment Selection</strong> — We recommend appropriately sized commercial equipment from brands with strong local parts availability.</li>
                <li><strong>Commercial Permit</strong> — We pull the commercial mechanical permit from the City of Nampa or Canyon County.</li>
                <li><strong>Installation &amp; Inspection</strong> — We install to code, coordinate the required inspection, and provide you with inspection sign-off documentation.</li>
                <li><strong>Commissioning</strong> — We test all connections, verify output temperatures, and set thermostats to code-required levels for your application.</li>
              </ol>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Commercial Systems</h3>
              <ul>
                <li>Large-capacity storage tanks</li>
                <li>Commercial tankless systems</li>
                <li>Booster heaters (NSF)</li>
                <li>Multi-unit manifolds</li>
                <li>New construction rough-in</li>
                <li>Commercial permit management</li>
              </ul>
            </div>""",
    "cta_h2": "Commercial Water Heater Installation in Nampa",
    "cta_sub": "Site assessments available. Commercial permit management. Restaurants, apartments, offices. Nampa, ID.",
    "cta_label": f"Call {PHONE_DISPLAY} — Commercial Inquiries",
    "related_links": """                <li><a href="installation.html">Water Heater Installation</a></li>
                <li><a href="commercial-repair.html">Commercial Water Heater Repair</a></li>
                <li><a href="tankless-installation.html">Tankless Installation</a></li>"""
})

# ---- MAINTENANCE ----
PAGES.append({
    "path": f"{BASE}/services/maintenance.html",
    "prefix": "../",
    "active": "maintenance.html",
    "title": "Water Heater Maintenance in Nampa, ID | Annual Service Plans",
    "desc": "Water heater maintenance in Nampa, Idaho. Annual sediment flush, anode rod inspection, T&P valve testing. Extend your unit's life. Call (208) 987-5152.",
    "canonical": "services/maintenance.html",
    "breadcrumbs": [
        ("Home", ""), ("Services", "services/repair.html"), ("Water Heater Maintenance", "services/maintenance.html")
    ],
    "schema_extra": service_schema(
        "Water Heater Maintenance in Nampa, ID",
        "Annual water heater maintenance in Nampa, Idaho. Sediment flushing, anode rod inspection, T&P valve testing, and descaling. Extend your unit's life in Nampa's hard-water market.",
        "$120 - $250", "Water Heater Maintenance"
    ) + "\n" + faq_schema([
        ("How often should a water heater be serviced in Nampa?",
         "In Nampa, we recommend annual maintenance for all water heater types due to the city's hard water (200–350 ppm). Standard tank units need annual sediment flushing and anode rod inspection. Tankless units need annual descaling plus inlet filter cleaning every 6 months. Hard water accelerates all forms of water heater wear."),
        ("What does water heater maintenance include?",
         "A standard Nampa Water Heater Pros maintenance visit includes: sediment flush (tank units) or descaling (tankless units), anode rod inspection and replacement if depleted, T&P pressure relief valve test, thermostat temperature verification, visual inspection of all connections and venting, and a written condition report."),
        ("How much does water heater maintenance cost in Nampa?",
         "Annual maintenance runs $120–$180 for standard tank units and $150–$250 for tankless descaling service. Anode rod replacement (if needed) adds $80–$150. Annual maintenance typically costs 3–5× less than emergency repair calls caused by neglected maintenance."),
        ("Can regular maintenance extend my water heater's life?",
         "Significantly, especially in Nampa's hard-water environment. Annual sediment flushing removes scale deposits that cause heating element failure and tank corrosion. Annual anode rod inspection prevents the tank liner from corroding. Studies show properly maintained water heaters in hard-water areas last 30–50% longer than neglected units.")
    ]),
    "h1": "Water Heater Maintenance in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Annual Water Heater Service",
    "hero_lead": "Nampa's hard water (200–350 ppm) is the #1 killer of water heaters in the Treasure Valley. Annual maintenance—sediment flushing, anode rod inspection, and tankless descaling—is the most cost-effective way to protect your investment. Call us to schedule your Nampa water heater tune-up.",
    "main_content": """
              <h2 id="maintenance-content-heading">Water Heater Maintenance in Nampa's Hard-Water Market</h2>
              <p>Canyon County water ranks among the harder municipal supplies in the Treasure Valley, typically measuring 200–350 ppm of calcium carbonate. This mineral load deposits inside water heater tanks, on heating elements, and inside tankless heat exchangers at a rate that demands annual service to prevent premature failure.</p>

              <h3>Why Annual Maintenance Matters in Nampa</h3>
              <ul>
                <li><strong>Sediment Buildup</strong> — Calcium and magnesium settle at the bottom of tank water heaters, forming a hard insulating layer between the burner (gas) or heating element (electric) and the water. This forces the unit to work harder, increasing energy bills and causing premature element burnout.</li>
                <li><strong>Anode Rod Depletion</strong> — The sacrificial anode rod attracts corrosive minerals, protecting the tank liner. In Nampa's hard water, anode rods deplete faster than in soft-water markets. Once depleted, tank corrosion begins—leading to rusty water and eventual tank failure.</li>
                <li><strong>Tankless Scale Accumulation</strong> — Mineral scale inside a tankless heat exchanger acts as insulation, reducing heat transfer efficiency, triggering error codes, and eventually cracking the heat exchanger under thermal stress. Annual descaling is non-negotiable in Nampa.</li>
              </ul>

              <h3>Annual Maintenance Checklist</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Maintenance Item</th><th>Tank Units</th><th>Tankless Units</th></tr>
                </thead>
                <tbody>
                  <tr><td>Sediment flush</td><td>✓ Annual</td><td>—</td></tr>
                  <tr><td>Descaling (citric acid flush)</td><td>—</td><td>✓ Annual</td></tr>
                  <tr><td>Inlet filter cleaning</td><td>—</td><td>✓ Every 6 mo</td></tr>
                  <tr><td>Anode rod inspection</td><td>✓ Annual</td><td>—</td></tr>
                  <tr><td>T&amp;P valve test</td><td>✓ Annual</td><td>✓ Annual</td></tr>
                  <tr><td>Thermostat verification (120°F)</td><td>✓ Annual</td><td>✓ Annual</td></tr>
                  <tr><td>Connection &amp; venting inspection</td><td>✓ Annual</td><td>✓ Annual</td></tr>
                  <tr><td>Written condition report</td><td>✓ Annual</td><td>✓ Annual</td></tr>
                </tbody>
              </table>

              <h3>Maintenance Costs in Nampa</h3>
              <table class="cost-table">
                <thead>
                  <tr><th>Service</th><th>Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Tank unit annual maintenance</td><td>$120 – $180</td></tr>
                  <tr><td>Tankless annual descaling</td><td>$150 – $250</td></tr>
                  <tr><td>Anode rod replacement (if needed)</td><td>$80 – $150</td></tr>
                  <tr><td>T&amp;P valve replacement (if failed)</td><td>$100 – $200</td></tr>
                </tbody>
              </table>
""",
    "sidebar_items": """
            <div class="sidebar-card">
              <h3>Maintenance Services</h3>
              <ul>
                <li>Annual sediment flush</li>
                <li>Tankless descaling</li>
                <li>Anode rod inspection</li>
                <li>T&amp;P valve testing</li>
                <li>Thermostat check</li>
                <li>Connection inspection</li>
                <li>Written condition report</li>
              </ul>
            </div>""",
    "cta_h2": "Schedule Your Nampa Water Heater Tune-Up",
    "cta_sub": "Annual maintenance starting at $120. Protect your water heater from Nampa's hard water. Same-week appointments available.",
    "cta_label": f"Call {PHONE_DISPLAY} — Schedule Maintenance",
    "related_links": """                <li><a href="repair.html">Water Heater Repair</a></li>
                <li><a href="tankless-repair.html">Tankless Repair &amp; Descaling</a></li>
                <li><a href="replacement.html">Water Heater Replacement</a></li>"""
})

def build_service_page(page):
    prefix = page["prefix"]
    root = prefix
    svc = prefix + "services/"
    areas = prefix + "areas/"

    h = header(
        prefix, page["title"], page["desc"], page["canonical"],
        page["breadcrumbs"], page["schema_extra"], page["active"]
    )

    bc_crumbs = page["breadcrumbs"]
    bc_html = breadcrumb_nav(bc_crumbs, root)

    cta = cta_banner(page["cta_h2"], page["cta_sub"], page["cta_label"])

    related = sidebar_related(page["related_links"])
    brands = SIDEBAR_BRANDS
    areas_sidebar = sidebar_areas(prefix)

    foot = footer(prefix)

    # Build the final page
    h2_id = page["h1"].lower().replace(" ", "-").replace(",", "").replace("(", "").replace(")", "")[:30]
    page_id = page["active"].replace(".html", "")

    content = f"""{h}

{bc_html}

  <main id="main-content">

    <!-- PAGE HERO -->
    <section class="page-hero" aria-labelledby="{page_id}-heading">
      <div class="page-hero-inner">
        <p class="hero-eyebrow">{page["eyebrow"]}</p>
        <h1 id="{page_id}-heading">{page["h1"]}</h1>
        <p class="hero-lead">
          {page["hero_lead"]}
        </p>
        <div class="hero-ctas">
          <a href="tel:{PHONE_TEL}" class="btn-primary" aria-label="Call {BRAND} for service in Nampa">
            {PHONE_SVG18}
            Call {PHONE_DISPLAY} — Same-Day Available
          </a>
          <a href="{root}contact.html" class="btn-secondary">Request a Callback</a>
        </div>
        <div class="trust-signals">
          <div class="trust-item"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> Same-Day Service</div>
          <div class="trust-item"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg> Licensed &amp; Insured</div>
          <div class="trust-item"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> Upfront Pricing</div>
        </div>
      </div>
    </section>

    <!-- MAIN CONTENT + SIDEBAR -->
    <section class="section" aria-label="{page['h1']} content">
      <div class="container">
        <div class="content-with-sidebar">

          <!-- ARTICLE CONTENT -->
          <article class="article-content" aria-labelledby="{page_id}-content-heading">
{page["main_content"]}
          </article>

          <!-- SIDEBAR -->
          <aside class="content-sidebar" aria-label="Quick reference">
{page["sidebar_items"]}
{brands}
{related}
{areas_sidebar}
          </aside>

        </div>
      </div>
    </section>
{cta}

  </main>
{foot}"""

    return content


# Build all service pages
for page in PAGES:
    html = build_service_page(page)
    with open(page["path"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built: {page['path']}")

print("All service pages built.")
