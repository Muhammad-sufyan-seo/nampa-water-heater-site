#!/usr/bin/env python3
"""Build areas/index.html (the "Areas We Serve" hub page). Run from anywhere: python3 scripts/build_areas_hub.py

HISTORICAL SCAFFOLDING SCRIPT — see the warning in build_pages.py. Re-running
this will overwrite areas/index.html with its original generated content.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import (
    header, footer, PHONE_DISPLAY, PHONE_TEL, BRAND, DOMAIN, PHONE_SVG18, BASE
)

prefix = "../"
root = prefix

title = "Areas We Serve | Water Heater Service Throughout Nampa, ID | Nampa Water Heater Pros"
desc = "Nampa Water Heater Pros serves Downtown Nampa, Central Nampa, South Nampa, and surrounding Treasure Valley neighborhoods. ZIP 83651, 83686, 83687. Call (208) 987-5152."
canonical = "areas/index.html"

breadcrumb_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": "{DOMAIN}/areas/index.html"}}
    ]
  }}
  </script>"""

webpage_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Areas We Serve | Nampa Water Heater Pros",
    "url": "{DOMAIN}/areas/index.html",
    "description": "{desc}",
    "isPartOf": {{"@id": "{DOMAIN}/#website"}}
  }}
  </script>"""

h = header(prefix, title, desc, canonical, [("Home", ""), ("Areas We Serve", "areas/index.html")], breadcrumb_schema + "\n" + webpage_schema)

foot = footer(prefix)

content = f"""{h}

  <!-- BREADCRUMB -->
  <nav class="breadcrumb" aria-label="Breadcrumb navigation">
    <div class="breadcrumb-inner">
      <a href="{root}index.html">Home</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">Areas We Serve</span>
    </div>
  </nav>

  <main id="main-content">

    <!-- PAGE HERO -->
    <section class="page-hero" aria-labelledby="areas-heading">
      <div class="page-hero-inner">
        <p class="hero-eyebrow">Nampa, Idaho · Service Area</p>
        <h1 id="areas-heading">Water Heater Service Areas in Nampa, Idaho</h1>
        <p class="hero-lead">
          Nampa Water Heater Pros provides water heater repair, installation, and replacement throughout Nampa, ID and the surrounding Treasure Valley. We serve every neighborhood in the Nampa city limits, with dedicated service pages for our highest-demand areas below.
        </p>
        <div class="hero-ctas">
          <a href="tel:{PHONE_TEL}" class="btn-primary" aria-label="Call {BRAND} for service in your Nampa neighborhood">
            {PHONE_SVG18}
            Call {PHONE_DISPLAY} — Same-Day Available
          </a>
          <a href="{root}contact.html" class="btn-secondary">Request a Callback</a>
        </div>
      </div>
    </section>

    <!-- AREA CARDS -->
    <section class="section" aria-labelledby="area-cards-heading">
      <div class="container">
        <h2 id="area-cards-heading">Our Primary Nampa Service Areas</h2>
        <p>Each area of Nampa has its own housing stock and water heater needs. Below are our three primary service area pages with neighborhood-specific guidance.</p>

        <div class="area-cards-grid">
          <article class="area-card">
            <h3><a href="downtown-nampa.html">Downtown Nampa</a></h3>
            <p><strong>ZIP 83651</strong> — Historic and older homes near Nampa's city center. Aging water heaters and outdated plumbing connections are common. We focus on fast diagnostic repair and code-compliant replacement for older housing stock.</p>
            <a href="downtown-nampa.html" class="btn-secondary">View Downtown Nampa Services</a>
          </article>

          <article class="area-card">
            <h3><a href="central-nampa.html">Central Nampa</a></h3>
            <p><strong>ZIP 83651</strong> — Established residential neighborhoods with a mix of home ages. We provide both repair and replacement services, with particular attention to hard-water sediment issues common in this area's water heaters.</p>
            <a href="central-nampa.html" class="btn-secondary">View Central Nampa Services</a>
          </article>

          <article class="area-card">
            <h3><a href="south-nampa.html">South Nampa</a></h3>
            <p><strong>ZIP 83686</strong> — Newer construction and established luxury homes near Lake Lowell. Higher-capacity systems, tankless upgrades, and new installation services are our focus in this growing part of Nampa.</p>
            <a href="south-nampa.html" class="btn-secondary">View South Nampa Services</a>
          </article>
        </div>

        <h2>Full Nampa Neighborhood Coverage</h2>
        <p>In addition to our three primary service area pages, we provide water heater repair, installation, and replacement throughout all of Nampa's neighborhoods and surrounding communities, including North Nampa, West Nampa, East Nampa, the Franklin Road corridor, the Karcher area, Sky Ranch, Southside Nampa, and unincorporated Canyon County areas immediately adjacent to Nampa city limits. If your neighborhood isn't listed above, we still serve you — call to confirm coverage for your address.</p>

        <div class="service-area-block" style="margin-top:2rem;">
          <h3>Primary Zip Codes We Serve</h3>
          <p><strong>83651 · 83686 · 83687</strong> — covering Downtown Nampa, Central Nampa, South Nampa, and the broader Nampa, Idaho service area.</p>
        </div>
      </div>
    </section>

    <!-- CTA BANNER -->
    <div class="cta-banner" role="complementary">
      <div class="container">
        <h2>Water Heater Service Anywhere in Nampa</h2>
        <p>Same-day service throughout Nampa, ID. Licensed and insured professionals. Upfront pricing.</p>
        <a href="tel:{PHONE_TEL}" class="btn-white" aria-label="Call {BRAND}">
          {PHONE_SVG18}
          Call {PHONE_DISPLAY} — Same-Day Service Available
        </a>
      </div>
    </div>

  </main>
{foot}"""

with open(f"{BASE}/areas/index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Built areas/index.html")
