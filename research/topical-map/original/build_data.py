#!/usr/bin/env python3
"""
Canonical dataset for the Nampa Water Heater Pros topical map.
Single source of truth -> derives Tables 1-6 for the xlsx deliverable.
"""

PHONE = "(208) 987-5152"
BRAND = "Nampa Water Heater Pros"
DOMAIN = "https://nampawaterheater.com"

# ---------------------------------------------------------------------------
# TABLE 1 candidate data lives inline with the master list below (status=Existing)
# ---------------------------------------------------------------------------

# Each row: id, tier, cluster, page_type, url, title, intent, parent, status, notes
# intent: Commercial / Informational / Navigational / Local-Commercial
# status: Existing / Existing-Optimize / New

PAGES = []

def add(pid, tier, cluster, ptype, url, title, intent, parent, status, notes=""):
    PAGES.append(dict(id=pid, tier=tier, cluster=cluster, ptype=ptype, url=url,
                       title=title, intent=intent, parent=parent, status=status, notes=notes))

# ============================================================
# CLUSTER 0 — CORE / NAVIGATIONAL (existing, 5) — no new pages
# ============================================================
add("EX-001", "T1", "0-Core", "Homepage", "/", "Nampa Water Heater Pros | Water Heater Repair & Installation in Nampa, ID",
    "Navigational", "-", "Existing", "Root entity hub. Stat bar (Since 2019 / 9,000+ / 60 min) already implemented.")
add("EX-002", "T2", "0-Core", "Core", "/about", "About Nampa Water Heater Pros", "Informational",
    "/", "Existing", "AboutPage schema + stat bar present.")
add("EX-003", "T1", "0-Core", "Core", "/contact", "Contact Nampa Water Heater Pros", "Navigational",
    "/", "Existing", "Primary conversion page besides tel: click. Sidebar widget already added.")
add("EX-004", "T4", "0-Core", "Legal", "/privacy-policy", "Privacy Policy", "Navigational",
    "/", "Existing", "Rewritten to match direct-provider business model (BIZ-MODEL-N009).")
add("EX-005", "T4", "0-Core", "Legal", "/terms", "Terms of Service", "Navigational",
    "/", "Existing", "Same rewrite as Privacy Policy. Flag: not substitute for attorney review per verified-claims registry.")

# ============================================================
# CLUSTER 1 — CORE SERVICE (MONEY) PAGES
# Existing: hub + 14 service pages (15 total)
# ============================================================
add("EX-010", "T1", "1-Service", "Hub", "/services", "Water Heater Services in Nampa, ID", "Local-Commercial",
    "/", "Existing", "Cluster hub. CollectionPage/ItemList schema present.")
add("EX-011", "T1", "1-Service", "Service", "/services/water-heater-repair-nampa-id", "Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services", "Existing", "Fuel-agnostic repair pillar.")
add("EX-012", "T2", "1-Service", "Service", "/services/gas-water-heater-repair-nampa-id", "Gas Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services/water-heater-repair-nampa-id", "Existing", "")
add("EX-013", "T2", "1-Service", "Service", "/services/electric-water-heater-repair-nampa-id", "Electric Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services/water-heater-repair-nampa-id", "Existing", "")
add("EX-014", "T2", "1-Service", "Service", "/services/heat-pump-water-heater-repair-nampa-id", "Heat Pump Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services/water-heater-repair-nampa-id", "Existing", "")
add("EX-015", "T2", "1-Service", "Service", "/services/tankless-water-heater-repair-nampa-id", "Tankless Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services/water-heater-repair-nampa-id", "Existing", "")
add("EX-016", "T2", "1-Service", "Service", "/services/commercial-water-heater-repair-nampa-id", "Commercial Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/services/water-heater-repair-nampa-id", "Existing", "")
add("EX-017", "T1", "1-Service", "Service", "/services/water-heater-installation-nampa-id", "Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services", "Existing", "Fuel-agnostic install pillar.")
add("EX-018", "T2", "1-Service", "Service", "/services/gas-water-heater-installation-nampa-id", "Gas Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services/water-heater-installation-nampa-id", "Existing", "")
add("EX-019", "T2", "1-Service", "Service", "/services/electric-water-heater-installation-nampa-id", "Electric Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services/water-heater-installation-nampa-id", "Existing", "")
add("EX-020", "T2", "1-Service", "Service", "/services/heat-pump-water-heater-installation-nampa-id", "Heat Pump Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services/water-heater-installation-nampa-id", "Existing", "")
add("EX-021", "T2", "1-Service", "Service", "/services/tankless-water-heater-installation-nampa-id", "Tankless Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services/water-heater-installation-nampa-id", "Existing", "")
add("EX-022", "T2", "1-Service", "Service", "/services/commercial-water-heater-installation-nampa-id", "Commercial Water Heater Installation in Nampa, ID",
    "Local-Commercial", "/services/water-heater-installation-nampa-id", "Existing", "")
add("EX-023", "T1", "1-Service", "Service", "/services/water-heater-replacement-nampa-id", "Water Heater Replacement in Nampa, ID",
    "Local-Commercial", "/services", "Existing", "")
add("EX-024", "T2", "1-Service", "Service", "/services/water-heater-maintenance-nampa-id", "Water Heater Maintenance in Nampa, ID",
    "Local-Commercial", "/services", "Existing", "Package/overview page. Do not duplicate with new flushing/descaling pages below.")

# New Cluster 1 pages (15)
add("NEW-001", "T1", "1-Service", "Service", "/services/emergency-water-heater-repair-nampa-id",
    "Emergency Water Heater Repair in Nampa, ID", "Local-Commercial", "/services/water-heater-repair-nampa-id", "New",
    "Distinct high-intent query (burst tank, active flooding, no hot water for a business). Absorb 'same-day' framing here instead of a separate page.")
add("NEW-002", "T2", "1-Service", "Service", "/services/water-heater-inspection-nampa-id",
    "Water Heater Inspection in Nampa, ID", "Local-Commercial", "/services", "New",
    "Pre-purchase / home-inspection-triggered inspection service; distinct from repair diagnostic.")
add("NEW-003", "T2", "1-Service", "Service", "/services/anode-rod-replacement-nampa-id",
    "Anode Rod Replacement in Nampa, ID", "Local-Commercial", "/services/water-heater-maintenance-nampa-id", "New",
    "Component-level service named as its own entity in content-seo-rules.md §8.")
add("NEW-004", "T2", "1-Service", "Service", "/services/expansion-tank-installation-repair-nampa-id",
    "Expansion Tank Installation & Repair in Nampa, ID", "Local-Commercial", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-005", "T2", "1-Service", "Service", "/services/pressure-relief-valve-replacement-nampa-id",
    "T&P Valve (Pressure Relief Valve) Replacement in Nampa, ID", "Local-Commercial", "/services/water-heater-repair-nampa-id", "New",
    "Safety-relevant component service.")
add("NEW-006", "T2", "1-Service", "Service", "/services/water-heater-flushing-nampa-id",
    "Water Heater Flushing & Sediment Removal in Nampa, ID", "Local-Commercial", "/services/water-heater-maintenance-nampa-id", "New",
    "Single most-searched maintenance task, split out from the general Maintenance package page.")
add("NEW-007", "T2", "1-Service", "Service", "/services/tankless-water-heater-descaling-nampa-id",
    "Tankless Water Heater Descaling in Nampa, ID", "Local-Commercial", "/services/tankless-water-heater-repair-nampa-id", "New",
    "Tankless-specific maintenance action distinct from tank flushing.")
add("NEW-008", "T3", "1-Service", "Service", "/services/water-heater-venting-repair-nampa-id",
    "Water Heater Venting & Flue Repair in Nampa, ID", "Local-Commercial", "/services/gas-water-heater-repair-nampa-id", "New", "")
add("NEW-009", "T2", "1-Service", "Service", "/services/water-heater-seismic-strapping-nampa-id",
    "Water Heater Seismic Strapping Installation in Nampa, ID", "Local-Commercial", "/services/water-heater-installation-nampa-id", "New",
    "Idaho code factor already named in content-seo-rules.md. NEEDS: cite actual Idaho code section before publishing specifics (§9.1).")
add("NEW-010", "T3", "1-Service", "Service", "/services/water-heater-removal-haul-away-nampa-id",
    "Water Heater Removal & Haul-Away in Nampa, ID", "Local-Commercial", "/services/water-heater-replacement-nampa-id", "New", "")
add("NEW-011", "T3", "1-Service", "Service", "/services/recirculation-pump-installation-nampa-id",
    "Recirculation Pump Installation in Nampa, ID", "Local-Commercial", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-012", "T3", "1-Service", "Service", "/services/point-of-use-water-heater-installation-nampa-id",
    "Point-of-Use Water Heater Installation in Nampa, ID", "Local-Commercial", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-013", "T2", "1-Service", "Service", "/services/commercial-water-heater-maintenance-nampa-id",
    "Commercial Water Heater Maintenance in Nampa, ID", "Local-Commercial", "/services/water-heater-maintenance-nampa-id", "New",
    "Fills a real gap: commercial currently has repair+install only, no maintenance page.")
add("NEW-014", "T3", "1-Service", "Service", "/services/water-heater-relocation-nampa-id",
    "Water Heater Relocation in Nampa, ID", "Local-Commercial", "/services/water-heater-installation-nampa-id", "New",
    "Remodel-driven query (moving unit to new location in same home).")
add("NEW-015", "T4", "1-Service", "Service", "/services/gas-line-installation-water-heater-nampa-id",
    "Gas Line Installation for Water Heaters in Nampa, ID", "Local-Commercial", "/services/gas-water-heater-installation-nampa-id", "New",
    "SCOPE FLAG: verify this is actually offered before building — adjacent to general-plumbing/gas-fitting scope, may exceed the business's confirmed service list.")

# ============================================================
# CLUSTER 2 — PROBLEM / ISSUE PAGES
# Existing: hub + 6 (7 total)
# ============================================================
add("EX-030", "T1", "2-Issue", "Hub", "/common-issues", "Common Water Heater Issues in Nampa, ID", "Informational",
    "/", "Existing", "")
add("EX-031", "T2", "2-Issue", "Issue", "/common-issues/no-hot-water-nampa-id", "No Hot Water: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "")
add("EX-032", "T2", "2-Issue", "Issue", "/common-issues/water-heater-leaking-nampa-id", "Water Heater Leaking: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "")
add("EX-033", "T2", "2-Issue", "Issue", "/common-issues/water-heater-making-noise-nampa-id", "Water Heater Making Noise: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "")
add("EX-034", "T2", "2-Issue", "Issue", "/common-issues/pilot-light-wont-stay-lit-nampa-id", "Pilot Light Won't Stay Lit: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "")
add("EX-035", "T2", "2-Issue", "Issue", "/common-issues/rusty-discolored-water-nampa-id", "Rusty or Discolored Water: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "")
add("EX-036", "T2", "2-Issue", "Issue", "/common-issues/water-heater-tripping-breaker-nampa-id", "Water Heater Tripping the Breaker: Causes & Fixes in Nampa, ID",
    "Informational", "/common-issues", "Existing", "Absorb GFCI-tripping variant here rather than a new page.")

# New Cluster 2 pages (13)
add("NEW-020", "T2", "2-Issue", "Issue", "/common-issues/water-too-hot-nampa-id",
    "Water Heater Water Too Hot: Causes & Fixes", "Informational", "/common-issues", "New", "")
add("NEW-021", "T2", "2-Issue", "Issue", "/common-issues/water-heater-not-heating-enough-nampa-id",
    "Water Heater Not Heating Enough / Runs Out Fast: Causes & Fixes", "Informational", "/common-issues", "New",
    "Distinct from 'No Hot Water' (zero output) — this is partial/insufficient output.")
add("NEW-022", "T2", "2-Issue", "Issue", "/common-issues/water-heater-smells-nampa-id",
    "Water Heater Smells (Sulfur / Rotten Egg): Causes & Fixes", "Informational", "/common-issues", "New",
    "Distinct diagnostic path from rusty/discolored water (visual vs. odor).")
add("NEW-023", "T3", "2-Issue", "Issue", "/common-issues/tankless-water-heater-error-codes-nampa-id",
    "Tankless Water Heater Error Codes: What They Mean", "Informational", "/common-issues", "New",
    "Tankless-specific; no traditional pilot light, needs its own diagnostic page.")
add("NEW-024", "T2", "2-Issue", "Issue", "/common-issues/water-heater-needs-replacing-nampa-id",
    "How to Tell If Your Water Heater Needs Replacing", "Informational", "/services/water-heater-replacement-nampa-id", "New",
    "Strong informational-to-commercial bridge into Replacement pillar.")
add("NEW-025", "T3", "2-Issue", "Issue", "/common-issues/water-heater-tank-corrosion-nampa-id",
    "Water Heater Tank Corrosion / Rusted Tank Shell", "Informational", "/common-issues", "New",
    "Failure mode of the tank itself — distinct entity from 'rusty water' symptom.")
add("NEW-026", "T1", "2-Issue", "Issue", "/common-issues/gas-smell-water-heater-nampa-id",
    "Gas Smell Near Your Water Heater: What to Do", "Informational", "/services/emergency-water-heater-repair-nampa-id", "New",
    "SAFETY-CRITICAL page. Ties directly to Emergency Repair + Gas Repair pillars.")
add("NEW-027", "T3", "2-Issue", "Issue", "/common-issues/electric-water-heater-wont-turn-on-nampa-id",
    "Electric Water Heater Won't Turn On: Causes & Fixes", "Informational", "/common-issues", "New", "")
add("NEW-028", "T3", "2-Issue", "Issue", "/common-issues/water-heater-condensation-nampa-id",
    "Tankless / Heat Pump Water Heater Condensation Issues", "Informational", "/common-issues", "New",
    "Distinct from a 'leak' — normal-vs-excessive condensate framing for condensing units.")
add("NEW-029", "T4", "2-Issue", "Issue", "/common-issues/water-heater-short-cycling-nampa-id",
    "Water Heater Short Cycling: Causes & Fixes", "Informational", "/common-issues", "New", "")
add("NEW-030", "T3", "2-Issue", "Issue", "/common-issues/water-heater-burning-smell-nampa-id",
    "Water Heater Burning Smell: What It Means", "Informational", "/services/emergency-water-heater-repair-nampa-id", "New",
    "Safety-relevant — links to Emergency Repair.")
add("NEW-031", "T3", "2-Issue", "Issue", "/common-issues/water-heater-overflow-tp-valve-nampa-id",
    "Water Heater Overflowing / T&P Valve Discharging", "Informational", "/services/pressure-relief-valve-replacement-nampa-id", "New", "")
add("NEW-032", "T3", "2-Issue", "Issue", "/common-issues/water-heater-sediment-buildup-nampa-id",
    "Water Heater Sediment Buildup: Symptoms & Fix", "Informational", "/services/water-heater-flushing-nampa-id", "New", "")

# ============================================================
# CLUSTER 3 — SYSTEM / FUEL / PRODUCT TYPE PAGES (new hub + 10)
# ============================================================
add("NEW-040", "T2", "3-Type", "Hub", "/water-heater-types", "Types of Water Heaters", "Informational",
    "/", "New", "New hub separating TYPE/entity-definition intent from the transactional /services hub.")
add("NEW-041", "T2", "3-Type", "Type", "/water-heater-types/tank-water-heaters", "Tank Water Heaters: How They Work",
    "Informational", "/water-heater-types", "New", "")
add("NEW-042", "T2", "3-Type", "Type", "/water-heater-types/tankless-water-heaters", "Tankless Water Heaters: How They Work",
    "Informational", "/water-heater-types", "New", "")
add("NEW-043", "T2", "3-Type", "Comparison", "/water-heater-types/gas-vs-electric-water-heaters", "Gas vs. Electric Water Heaters: Which Is Right for Your Nampa Home",
    "Informational", "/water-heater-types", "New", "")
add("NEW-044", "T2", "3-Type", "Comparison", "/water-heater-types/tank-vs-tankless-water-heaters", "Tank vs. Tankless Water Heaters: Which Is Right for Nampa Homes",
    "Informational", "/water-heater-types", "New", "High-value comparison bridge page.")
add("NEW-045", "T2", "3-Type", "Type", "/water-heater-types/hybrid-heat-pump-water-heaters", "Hybrid (Heat Pump) Water Heaters Explained",
    "Informational", "/water-heater-types", "New", "")
add("NEW-046", "T3", "3-Type", "Type", "/water-heater-types/condensing-water-heaters", "Condensing Water Heaters Explained",
    "Informational", "/water-heater-types", "New", "Keep brief; heavily cross-link to tankless + heat pump to avoid thin overlap.")
add("NEW-047", "T3", "3-Type", "Type", "/water-heater-types/point-of-use-water-heaters", "Point-of-Use Water Heaters Explained",
    "Informational", "/water-heater-types", "New", "")
add("NEW-048", "T3", "3-Type", "Type", "/water-heater-types/commercial-water-heater-systems", "Commercial Water Heater Systems: Tank, Tankless & Booster",
    "Informational", "/water-heater-types", "New", "")
add("NEW-049", "T2", "3-Type", "Guide", "/water-heater-types/water-heater-sizing-guide", "Water Heater Sizing Guide: What Size Does Your Nampa Home Need",
    "Informational", "/water-heater-types", "New", "")
add("NEW-050", "T3", "3-Type", "Guide", "/water-heater-types/energy-efficiency-ratings-uef", "Water Heater Energy Efficiency Ratings (UEF) Explained",
    "Informational", "/water-heater-types", "New", "")

# ============================================================
# CLUSTER 4 — BRAND PAGES (new hub + 8, one per confirmed brand)
# ============================================================
add("NEW-060", "T3", "4-Brand", "Hub", "/brands", "Water Heater Brands We Service in Nampa, ID", "Informational",
    "/", "New", "Lists exactly the 8 confirmed brands per content-seo-rules.md §8 — do not add unconfirmed brands.")
add("NEW-061", "T2", "4-Brand", "Brand", "/brands/rheem-water-heater-repair-nampa-id", "Rheem Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "")
add("NEW-062", "T2", "4-Brand", "Brand", "/brands/ao-smith-water-heater-repair-nampa-id", "A.O. Smith Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "")
add("NEW-063", "T3", "4-Brand", "Brand", "/brands/bradford-white-water-heater-repair-nampa-id", "Bradford White Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "")
add("NEW-064", "T2", "4-Brand", "Brand", "/brands/navien-tankless-water-heater-repair-nampa-id", "Navien Tankless Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "Tankless brand — error-code differentiation possible, less risk of thin duplication vs. tank brands.")
add("NEW-065", "T2", "4-Brand", "Brand", "/brands/rinnai-tankless-water-heater-repair-nampa-id", "Rinnai Tankless Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "")
add("NEW-066", "T3", "4-Brand", "Brand", "/brands/noritz-tankless-water-heater-repair-nampa-id", "Noritz Tankless Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "")
add("NEW-067", "T4", "4-Brand", "Brand", "/brands/american-standard-water-heater-repair-nampa-id", "American Standard Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "Lower relative search volume brand — still legitimate, deprioritized.")
add("NEW-068", "T4", "4-Brand", "Brand", "/brands/state-water-heater-repair-nampa-id", "State Water Heater Repair in Nampa, ID",
    "Local-Commercial", "/brands", "New", "Lower relative search volume brand — still legitimate, deprioritized.")

# ============================================================
# CLUSTER 5 — LOCATION PAGES (existing hub + 3; NO new city/neighborhood pages)
# ============================================================
add("EX-070", "T1", "5-Location", "Hub", "/service-areas", "Nampa, ID Service Areas", "Navigational",
    "/", "Existing", "Per user decision: Nampa-only scope preserved. No new cities added.")
add("EX-071", "T2", "5-Location", "Area", "/service-areas/downtown-nampa", "Water Heater Service in Downtown Nampa, ID",
    "Local-Commercial", "/service-areas", "Existing", "ZIP 83651, repair-focused (older housing stock).")
add("EX-072", "T2", "5-Location", "Area", "/service-areas/central-nampa", "Water Heater Service in Central Nampa, ID",
    "Local-Commercial", "/service-areas", "Existing", "ZIP 83651, repair/replacement focus.")
add("EX-073", "T2", "5-Location", "Area", "/service-areas/south-nampa", "Water Heater Service in South Nampa, ID",
    "Local-Commercial", "/service-areas", "Existing", "ZIP 83686, installation/tankless focus (newer construction near Lake Lowell).")

# ============================================================
# CLUSTER 6 — SERVICE+LOCATION COMBOS
# Intentionally NOT built as a separate cluster (see notes to user).
# Cluster 1's *-nampa-id pages already ARE the service+location combination.
# ============================================================

# ============================================================
# CLUSTER 7 — INFORMATIONAL / RESOURCES (new hub + ~53)
# ============================================================
add("NEW-100", "T2", "7-Resource", "Hub", "/resources", "Water Heater Resources & Guides for Nampa Homeowners", "Informational",
    "/", "New", "")

# 7A Cost & Decision
add("NEW-101", "T2", "7-Resource", "Cost Guide", "/resources/water-heater-repair-cost-nampa-id", "Water Heater Repair Cost in Nampa, ID",
    "Informational", "/services/water-heater-repair-nampa-id", "New", "Must reuse the existing $150-$600 figure verbatim (PRICE-REPO-N008) — never re-derive.")
add("NEW-102", "T3", "7-Resource", "Cost Guide", "/resources/water-heater-installation-cost-nampa-id", "Water Heater Installation Cost in Nampa, ID",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-103", "T3", "7-Resource", "Cost Guide", "/resources/water-heater-replacement-cost-nampa-id", "Water Heater Replacement Cost in Nampa, ID",
    "Informational", "/services/water-heater-replacement-nampa-id", "New", "Scope tightly vs. Installation Cost guide — removal+swap framing, not new-construction framing.")
add("NEW-104", "T2", "7-Resource", "Comparison", "/resources/tankless-vs-tank-cost-comparison", "Tankless vs. Tank Water Heater Cost Comparison",
    "Informational", "/water-heater-types/tank-vs-tankless-water-heaters", "New", "")
add("NEW-105", "T2", "7-Resource", "Guide", "/resources/repair-vs-replace-water-heater", "Repair or Replace Your Water Heater: How to Decide",
    "Informational", "/services/water-heater-replacement-nampa-id", "New", "")
add("NEW-106", "T3", "7-Resource", "Cost Guide", "/resources/water-heater-installation-cost-by-fuel-type", "Water Heater Installation Cost by Fuel Type",
    "Informational", "/water-heater-types/gas-vs-electric-water-heaters", "New", "")
add("NEW-107", "T4", "7-Resource", "Guide", "/resources/hidden-costs-water-heater-installation", "Hidden Costs of Water Heater Installation",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "Permits, code upgrades, disposal fees.")
add("NEW-108", "T4", "7-Resource", "Guide", "/resources/water-heater-extended-warranty-worth-it", "Is an Extended Warranty Worth It on a New Water Heater?",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "")

# 7B Lifespan
add("NEW-109", "T2", "7-Resource", "Guide", "/resources/how-long-do-water-heaters-last", "How Long Do Water Heaters Last?",
    "Informational", "/services/water-heater-replacement-nampa-id", "New",
    "GATE: LIFE-TANK-N006 is Unverified — do not publish the 8-12/15-20yr figures without a manufacturer/DOE source; use qualitative framing until sourced.")
add("NEW-110", "T3", "7-Resource", "Guide", "/resources/signs-water-heater-needs-replacing", "Signs Your Water Heater Is Near the End of Its Life",
    "Informational", "/common-issues/water-heater-needs-replacing-nampa-id", "New", "Near-duplicate risk with NEW-024 — see Table 6.")
add("NEW-111", "T4", "7-Resource", "Guide", "/resources/lifespan-gas-vs-electric-vs-tankless", "Average Lifespan: Gas vs. Electric vs. Tankless",
    "Informational", "/resources/how-long-do-water-heaters-last", "New", "Same LIFE-TANK-N006 sourcing gate.")
add("NEW-112", "T4", "7-Resource", "Guide", "/resources/best-time-of-year-to-replace-water-heater", "Best Time of Year to Replace a Water Heater",
    "Informational", "/services/water-heater-replacement-nampa-id", "New", "")

# 7C Maintenance & DIY
add("NEW-113", "T3", "7-Resource", "DIY Guide", "/resources/how-to-flush-a-water-heater", "How to Flush a Water Heater (Step-by-Step)",
    "Informational", "/services/water-heater-flushing-nampa-id", "New", "")
add("NEW-114", "T3", "7-Resource", "DIY Guide", "/resources/how-to-test-a-tp-valve", "How to Test a T&P Valve",
    "Informational", "/services/pressure-relief-valve-replacement-nampa-id", "New", "")
add("NEW-115", "T3", "7-Resource", "Guide", "/resources/what-does-an-anode-rod-do", "What an Anode Rod Does and When to Replace It",
    "Informational", "/services/anode-rod-replacement-nampa-id", "New", "GATE: no universal '3-5 year' figure per INT-ANODE-N005 — manufacturer-manual framing only.")
add("NEW-116", "T4", "7-Resource", "DIY Guide", "/resources/how-to-relight-a-gas-pilot-light", "How to Relight a Gas Water Heater Pilot Light Safely",
    "Informational", "/common-issues/pilot-light-wont-stay-lit-nampa-id", "New", "Safety-framed.")
add("NEW-117", "T4", "7-Resource", "DIY Guide", "/resources/how-to-reset-a-water-heater", "How to Reset a Water Heater",
    "Informational", "/common-issues/no-hot-water-nampa-id", "New", "")
add("NEW-118", "T4", "7-Resource", "DIY Guide", "/resources/how-to-adjust-water-heater-temperature", "How to Adjust Water Heater Temperature Safely",
    "Informational", "/common-issues/water-too-hot-nampa-id", "New", "")
add("NEW-119", "T3", "7-Resource", "Guide", "/resources/what-is-an-expansion-tank", "What Is a Water Heater Expansion Tank and Do You Need One?",
    "Informational", "/services/expansion-tank-installation-repair-nampa-id", "New", "")
add("NEW-120", "T4", "7-Resource", "Guide", "/resources/what-is-a-pressure-reducing-valve", "What Is a Pressure-Reducing Valve (PRV)?",
    "Informational", "/services/expansion-tank-installation-repair-nampa-id", "New", "")
add("NEW-121", "T4", "7-Resource", "Guide", "/resources/water-heater-venting-requirements", "Water Heater Venting Requirements Explained",
    "Informational", "/services/water-heater-venting-repair-nampa-id", "New", "")
add("NEW-122", "T3", "7-Resource", "Guide", "/resources/diy-water-heater-troubleshooting-safety", "DIY Water Heater Troubleshooting: What's Safe and What Isn't",
    "Informational", "/common-issues", "New", "")
add("NEW-123", "T4", "7-Resource", "Guide", "/resources/how-often-should-a-water-heater-be-serviced", "How Often Should a Water Heater Be Serviced?",
    "Informational", "/services/water-heater-maintenance-nampa-id", "New", "GATE: INT-MAINT-N004 Unverified as universal schedule — 'follow manufacturer instructions' framing only.")
add("NEW-124", "T3", "7-Resource", "Checklist", "/resources/water-heater-maintenance-checklist", "Water Heater Maintenance Checklist for Nampa Homeowners",
    "Informational", "/services/water-heater-maintenance-nampa-id", "New", "")

# 7D Safety
add("NEW-125", "T2", "7-Resource", "Safety", "/resources/water-heater-carbon-monoxide-gas-safety", "Water Heater Safety: Carbon Monoxide & Gas Basics",
    "Informational", "/common-issues/gas-smell-water-heater-nampa-id", "New", "")
add("NEW-126", "T2", "7-Resource", "Safety", "/resources/what-to-do-if-you-smell-gas", "What to Do If You Smell Gas Near Your Water Heater",
    "Informational", "/common-issues/gas-smell-water-heater-nampa-id", "New", "Near-duplicate risk with NEW-026 — see Table 6; keep this as the how-to, NEW-026 as the symptom page.")
add("NEW-127", "T3", "7-Resource", "Safety", "/resources/how-to-shut-off-water-heater-emergency", "How to Shut Off Your Water Heater in an Emergency",
    "Informational", "/services/emergency-water-heater-repair-nampa-id", "New", "")
add("NEW-128", "T3", "7-Resource", "Safety", "/resources/water-heater-actively-leaking-what-to-do", "What to Do If Your Water Heater Is Actively Leaking",
    "Informational", "/common-issues/water-heater-leaking-nampa-id", "New", "")
add("NEW-129", "T4", "7-Resource", "Safety", "/resources/water-heater-flooding-basement-emergency-steps", "Water Heater Flooding a Basement: Emergency Steps",
    "Informational", "/services/emergency-water-heater-repair-nampa-id", "New", "")

# 7E Local / Climate / Code (all sourcing-gated)
add("NEW-130", "T2", "7-Resource", "Local", "/resources/does-nampa-have-hard-water", "Does Nampa Have Hard Water?",
    "Informational", "/", "New", "GATE: WATER-HARD-N001 Unverified — qualitative language only, NO ppm figure, per verified-claims remediation approach.")
add("NEW-131", "T3", "7-Resource", "Local", "/resources/hard-water-effect-on-water-heaters", "How Hard Water Affects Your Water Heater",
    "Informational", "/resources/does-nampa-have-hard-water", "New", "GATE: general mechanism only — no '1-3 year' lifespan-reduction figure (LIFE-HARDWATER-N002 Unverified).")
add("NEW-132", "T3", "7-Resource", "Local/Code", "/resources/idaho-seismic-strapping-code", "Idaho Water Heater Seismic Strapping Code Requirements",
    "Informational", "/services/water-heater-seismic-strapping-nampa-id", "New", "GATE: cite the actual Idaho building code section before publishing (§9.1) — do not state a code requirement without a fetched source.")
add("NEW-133", "T4", "7-Resource", "Local/Code", "/resources/water-heater-permit-requirements-nampa", "Water Heater Permit Requirements in Nampa / Canyon County",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "GATE: verify against City of Nampa / Canyon County building department before publishing specifics.")
add("NEW-134", "T3", "7-Resource", "Local", "/resources/winterizing-your-water-heater-idaho", "Winterizing Your Water Heater for Idaho Winters",
    "Informational", "/services/water-heater-maintenance-nampa-id", "New", "Absorbs the 'Winter Readiness' seasonal page — see Table 6.")
add("NEW-135", "T4", "7-Resource", "Local", "/resources/water-heater-rebates-idaho", "Energy Efficiency Rebates for Water Heaters in Idaho",
    "Informational", "/water-heater-types/hybrid-heat-pump-water-heaters", "New", "GATE: verify against actual Idaho Power / utility rebate program before publishing any dollar figure — do not fabricate rebate amounts.")

# 7F Sizing & Buying Guides
add("NEW-136", "T2", "7-Resource", "Guide", "/resources/water-heater-sizing-nampa-homes", "Water Heater Sizing: What Size Does Your Nampa Home Need?",
    "Informational", "/water-heater-types/water-heater-sizing-guide", "New", "Near-duplicate of NEW-049 — fold together, see Table 6.")
add("NEW-137", "T4", "7-Resource", "Guide", "/resources/40-vs-50-gallon-water-heater", "40-Gallon vs. 50-Gallon Water Heater: Which Fits Your Household?",
    "Informational", "/water-heater-types/water-heater-sizing-guide", "New", "")
add("NEW-138", "T3", "7-Resource", "Guide", "/resources/how-to-choose-a-new-water-heater", "How to Choose a New Water Heater: Buying Guide",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-139", "T3", "7-Resource", "Guide", "/resources/water-heater-installation-day-what-to-expect", "What to Expect on Water Heater Installation Day",
    "Informational", "/services/water-heater-installation-nampa-id", "New", "")
add("NEW-140", "T4", "7-Resource", "Guide", "/resources/questions-to-ask-before-hiring-a-water-heater-company", "Questions to Ask Before Hiring a Water Heater Company",
    "Informational", "/contact", "New", "Write generically — do not imply unconfirmed licensing claims about this business specifically.")

# 7G Comparisons
add("NEW-141", "T4", "7-Resource", "Guide", "/resources/water-softener-with-water-heater", "Should You Install a Water Softener With Your Water Heater?",
    "Informational", "/resources/hard-water-effect-on-water-heaters", "New", "Adjacent-scope — informational only, no CTA overreach into a service not offered.")
add("NEW-142", "T4", "7-Resource", "Guide", "/resources/single-family-vs-multi-family-water-heater-needs", "Single-Family vs. Multi-Family Water Heater Needs",
    "Informational", "/services/commercial-water-heater-installation-nampa-id", "New", "")
add("NEW-143", "T4", "7-Resource", "Comparison", "/resources/point-of-use-vs-whole-home-water-heater", "Point-of-Use vs. Whole-Home Water Heaters: Which Do You Need?",
    "Informational", "/water-heater-types/point-of-use-water-heaters", "New", "")
add("NEW-144", "T4", "7-Resource", "Guide", "/resources/is-a-recirculation-pump-worth-it", "Is a Recirculation Pump Worth Adding to Your System?",
    "Informational", "/services/recirculation-pump-installation-nampa-id", "New", "")

# 7H Component deep-dives
add("NEW-145", "T3", "7-Resource", "Deep-Dive", "/resources/how-a-gas-water-heater-works", "How a Gas Water Heater Works",
    "Informational", "/water-heater-types/tank-water-heaters", "New", "Thermocouple, gas valve, pilot assembly.")
add("NEW-146", "T3", "7-Resource", "Deep-Dive", "/resources/how-an-electric-water-heater-works", "How an Electric Water Heater Works",
    "Informational", "/water-heater-types/tank-water-heaters", "New", "Heating elements & thermostats.")
add("NEW-147", "T3", "7-Resource", "Deep-Dive", "/resources/how-a-tankless-water-heater-works", "How a Tankless Water Heater Works",
    "Informational", "/water-heater-types/tankless-water-heaters", "New", "Heat exchanger & flow sensor.")
add("NEW-148", "T4", "7-Resource", "Deep-Dive", "/resources/how-a-heat-pump-water-heater-works", "How a Heat Pump Water Heater Works",
    "Informational", "/water-heater-types/hybrid-heat-pump-water-heaters", "New", "Compressor & refrigerant circuit.")
add("NEW-149", "T4", "7-Resource", "Deep-Dive", "/resources/dip-tube-failure-explained", "Dip Tube Failure: What It Is and Why It Matters",
    "Informational", "/common-issues/water-heater-not-heating-enough-nampa-id", "New", "")
add("NEW-150", "T4", "7-Resource", "Deep-Dive", "/resources/water-heater-control-board-error-codes", "Water Heater Control Board & Error Codes Explained",
    "Informational", "/common-issues/tankless-water-heater-error-codes-nampa-id", "New", "Near-duplicate risk with NEW-023 — see Table 6.")
add("NEW-151", "T4", "7-Resource", "Deep-Dive", "/resources/water-heater-thermostat-settings-explained", "Water Heater Thermostat Settings Explained (Upper & Lower)",
    "Informational", "/common-issues/water-too-hot-nampa-id", "New", "")
add("NEW-152", "T4", "7-Resource", "Deep-Dive", "/resources/combustion-air-supply-requirements", "Water Heater Combustion Air Supply Requirements Explained",
    "Informational", "/services/water-heater-venting-repair-nampa-id", "New", "")

# FAQ consolidation
add("NEW-153", "T2", "7-Resource", "FAQ Hub", "/resources/water-heater-faqs-nampa", "Water Heater FAQs: Nampa Homeowners' Most Common Questions",
    "Informational", "/resources", "New", "Consolidates the PAA list already named in content-seo-rules.md §8. FAQPage schema must match visible text word-for-word per site standard.")

# ============================================================
# CLUSTER 8 — SEASONAL (evergreen, refreshed annually; NOT a dated news feed)
# ============================================================
add("NEW-160", "T4", "8-Seasonal", "Seasonal", "/resources/spring-water-heater-maintenance-checklist", "Spring Water Heater Maintenance Checklist",
    "Informational", "/resources/water-heater-maintenance-checklist", "New", "")
add("NEW-161", "T4", "8-Seasonal", "Seasonal", "/resources/summer-water-heater-efficiency-tips", "Summer Water Heater Efficiency Tips",
    "Informational", "/resources/water-heater-maintenance-checklist", "New", "")
add("NEW-162", "T4", "8-Seasonal", "Seasonal", "/resources/new-homeowner-water-heater-checklist", "Water Heater Checklist for New Homeowners",
    "Informational", "/resources/how-to-choose-a-new-water-heater", "New", "")

if __name__ == "__main__":
    print(f"Total pages: {len(PAGES)}")
    existing = [p for p in PAGES if p["status"] == "Existing"]
    new = [p for p in PAGES if p["status"] == "New"]
    print(f"Existing: {len(existing)}  New: {len(new)}")
    from collections import Counter
    print(Counter(p["cluster"] for p in PAGES))
    print(Counter(p["tier"] for p in PAGES))
