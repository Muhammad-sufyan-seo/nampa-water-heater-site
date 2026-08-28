#!/usr/bin/env python3
"""Generate all 6 symptom-based pages for Nampa Water Heater Pros. Run from anywhere: python3 scripts/build_symptoms.py

HISTORICAL SCAFFOLDING SCRIPT — see the warning in build_pages.py. Re-running
this will overwrite the 6 symptom pages with their original generated content.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import (
    header, breadcrumb_nav, footer, faq_schema, cta_banner,
    SIDEBAR_BRANDS, sidebar_related, sidebar_areas,
    BASE, PHONE_DISPLAY, PHONE_TEL, BRAND, DOMAIN, PHONE_SVG18
)

def service_schema_symptom(name, desc):
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
    "areaServed": {{"@type": "City", "name": "Nampa", "addressRegion": "ID"}}
  }}
  </script>"""


SYMPTOM_PAGES = []

# ---- LEAKING ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/leaking.html",
    "prefix": "../",
    "title": "Water Heater Leaking in Nampa, ID | Causes, Fixes & When to Call",
    "desc": "Water heater leaking in Nampa, ID? Learn the common causes, safe DIY checks, and when to call a professional. Same-day service. Call (208) 987-5152.",
    "canonical": "symptoms/leaking.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/leaking.html"), ("Water Heater Leaking", "symptoms/leaking.html")],
    "schema_extra": service_schema_symptom(
        "Water Heater Leak Diagnosis &amp; Repair in Nampa, ID",
        "Diagnosis and repair of leaking water heaters in Nampa, Idaho. Tank corrosion, T&P valve failure, and connection leaks."
    ) + "\n" + faq_schema([
        ("What's the average cost to repair a hot water heater?",
         "Water heater repair costs in Nampa, ID typically range from $150 to $600 depending on the issue. A leak from a loose fitting might cost $120–$180 to fix, while a leak from tank corrosion usually means replacement is needed since a corroded tank cannot be repaired."),
        ("Is a leaking water heater always a sign of tank failure?",
         "No. Many leaks come from loose water connections, a failing pressure relief valve, or condensation—all repairable without replacing the unit. However, if water is leaking directly from the tank body itself (not a fitting or valve), that indicates internal corrosion and the tank cannot be repaired; replacement is necessary."),
        ("Is it worth it to repair a hot water heater?",
         "If your unit is under 7 years old and the leak is from a fitting, valve, or connection (not the tank itself), repair is almost always worth it and inexpensive. If the leak is from the tank body on a unit over 8–10 years old, replacement is the better value."),
        ("Should I shut off my water heater if it's leaking?",
         "Yes. If you notice active leaking, shut off the water supply to the unit and, for electric units, switch off the breaker (or turn the gas control to pilot/off for gas units). This prevents further water damage and, in the case of electrical components getting wet, reduces safety risk. Then call a professional for diagnosis.")
    ]),
    "h1": "Water Heater Leaking in Nampa, Idaho — Causes & Fixes",
    "eyebrow": "Nampa, ID · Water Heater Leak Diagnosis",
    "hero_lead": "A leaking water heater can mean anything from a loose fitting to a failed tank. Here's how to identify the source safely, what it typically costs to fix, and when you need to call a professional immediately.",
    "causes": """
              <h2>Common Causes of a Leaking Water Heater in Nampa</h2>
              <ul>
                <li><strong>Tank Corrosion (Internal Rust-Through)</strong> — The most serious cause. Once the steel tank itself corrodes and leaks, the tank cannot be repaired—only replaced. Nampa's hard water accelerates anode rod depletion, which speeds up this process once the rod is used up.</li>
                <li><strong>Pressure Relief Valve (T&amp;P Valve) Discharge</strong> — This safety valve releases water when internal pressure or temperature exceeds safe limits. A failed or worn valve can leak even under normal conditions. This is a repairable, inexpensive fix.</li>
                <li><strong>Loose Water Connections</strong> — Fittings at the cold water inlet, hot water outlet, or drain valve can loosen over time or develop mineral deposits that prevent a tight seal. Usually a quick, low-cost repair.</li>
                <li><strong>Condensation</strong> — On gas water heaters, condensation can form on the tank exterior during initial fill or with a new cold water supply, and can be mistaken for a leak. This typically resolves on its own within a day.</li>
                <li><strong>Drain Valve Failure</strong> — The plastic drain valve at the tank's base can crack or fail to seal properly, especially on older units.</li>
                <li><strong>Excess Pressure from a Failed Expansion Tank</strong> — If your home has a closed plumbing system (check valve or pressure regulator), a failed expansion tank can cause excess pressure that forces the T&amp;P valve to discharge repeatedly.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Locate the source first.</strong> Dry off the tank and surrounding connections with a towel, then check every 15–20 minutes to see where water reappears first.</li>
                <li><strong>Check the T&amp;P valve discharge pipe.</strong> If water is coming from the pipe extending down the side of the tank, the pressure relief valve may be releasing water due to excess pressure or temperature—or the valve itself may be worn out.</li>
                <li><strong>Inspect all visible fittings.</strong> Look at the cold water inlet, hot water outlet, and drain valve at the bottom of the tank for visible moisture or mineral crust (a sign of a slow, ongoing leak).</li>
                <li><strong>Look for rust-colored water.</strong> Rust-tinted water pooling under the tank strongly suggests internal tank corrosion—not a fitting issue.</li>
                <li><strong>Check the floor drain pan (if present).</strong> Many Nampa homes have water heaters installed with a catch pan and drain line. Water in this pan confirms an active leak somewhere above.</li>
              </ol>""",
    "when_to_call": """
              <h2>When to Call a Professional Immediately</h2>
              <ul>
                <li>Water is leaking directly from the tank body itself (not a fitting or valve)</li>
                <li>You see active water pooling and don't know the source</li>
                <li>The leak is near electrical components on an electric water heater</li>
                <li>The T&amp;P valve is discharging continuously or repeatedly</li>
                <li>You notice rust-colored water, which indicates internal corrosion</li>
                <li>The leak is causing water damage to floors, walls, or belongings</li>
              </ul>
              <p>Shut off the water supply and power/gas to the unit before we arrive if you suspect an active leak from the tank itself.</p>""",
    "cost_table": """
              <h2>Cost Context for Water Heater Leak Repairs</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Repair Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Loose fitting / connection tightening</td><td>$100 – $180</td></tr>
                  <tr><td>T&amp;P valve replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Drain valve replacement</td><td>$120 – $200</td></tr>
                  <tr><td>Expansion tank replacement</td><td>$200 – $400</td></tr>
                  <tr><td>Full water heater replacement (tank corrosion)</td><td>$1,300 – $2,500</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/repair.html">Water Heater Repair</a></li>
                <li><a href="../services/replacement.html">Water Heater Replacement</a></li>
                <li><a href="no-hot-water.html">No Hot Water</a></li>"""
})

# ---- NO HOT WATER ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/no-hot-water.html",
    "prefix": "../",
    "title": "No Hot Water in Nampa, ID | Causes, Diagnostic Checks & Repair",
    "desc": "No hot water in Nampa, ID? Learn the common causes for gas and electric water heaters, safe DIY checks, and when to call a pro. Call (208) 987-5152.",
    "canonical": "symptoms/no-hot-water.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/no-hot-water.html"), ("No Hot Water", "symptoms/no-hot-water.html")],
    "schema_extra": service_schema_symptom(
        "No Hot Water Diagnosis &amp; Repair in Nampa, ID",
        "Emergency diagnosis and repair for no hot water in Nampa, Idaho homes. Gas and electric water heater troubleshooting and same-day repair."
    ) + "\n" + faq_schema([
        ("What's the average cost to repair a hot water heater?",
         "Water heater repair costs in Nampa typically range from $150–$600. A no-hot-water diagnosis often reveals a thermocouple failure ($150–$250), a failed heating element ($150–$250), or a tripped breaker/reset switch (often a quick, low-cost fix once the root cause is found)."),
        ("What is the most common reason for no hot water?",
         "For gas water heaters, a failed thermocouple or pilot light issue is most common. For electric water heaters, a tripped high-limit switch or a failed upper heating element is most common. In Nampa, hard-water sediment buildup contributes to both types of failures over time."),
        ("Who do I call if I need a new hot water heater?",
         "Call a dedicated water heater specialist rather than a general plumber for faster, more accurate diagnosis. Nampa Water Heater Pros specializes exclusively in water heater repair, installation, and replacement throughout Nampa, ID."),
        ("Can I fix a no-hot-water problem myself?",
         "Some basic checks are safe to do yourself: checking the breaker, checking the gas supply valve, and verifying the thermostat setting. However, diagnosing gas valve issues, thermocouple failures, or electrical element problems should be left to a licensed technician for safety and accuracy.")
    ]),
    "h1": "No Hot Water in Nampa, Idaho — Causes & Fixes",
    "eyebrow": "Nampa, ID · Emergency No-Hot-Water Diagnosis",
    "hero_lead": "No hot water is one of the most common—and most urgent—water heater complaints we get in Nampa. Here's what typically causes it for gas and electric units, what you can safely check yourself, and when to call for same-day service.",
    "causes": """
              <h2>Common Causes of No Hot Water in Nampa</h2>
              <h3>Gas Water Heaters</h3>
              <ul>
                <li><strong>Pilot Light Is Out</strong> — Often caused by a failed thermocouple, a draft blowing out the flame, or a gas supply interruption.</li>
                <li><strong>Failed Thermocouple</strong> — This safety sensor cuts gas flow to the pilot when it can't detect a flame. When it wears out, it can cut gas even with a lit pilot.</li>
                <li><strong>Gas Valve Failure</strong> — If the gas valve itself fails, no gas reaches the burner regardless of pilot status.</li>
                <li><strong>Closed Gas Supply Valve</strong> — Sometimes simply closed accidentally during other home maintenance.</li>
              </ul>
              <h3>Electric Water Heaters</h3>
              <ul>
                <li><strong>Tripped Circuit Breaker</strong> — The water heater circuit may have tripped due to a failing element or wiring issue.</li>
                <li><strong>Tripped High-Limit Safety Switch</strong> — A red reset button on the thermostat access panel trips when water gets too hot, cutting power to prevent scalding or tank damage.</li>
                <li><strong>Failed Upper Heating Element</strong> — If the top element fails completely, you'll get no hot water at all (versus a failed lower element, which causes hot water to run out quickly).</li>
                <li><strong>Failed Thermostat</strong> — A stuck or failed thermostat can prevent elements from engaging.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Check the breaker panel</strong> for electric units — look for a tripped breaker labeled "water heater." Reset once; if it trips again, stop and call a professional.</li>
                <li><strong>Check the gas supply valve</strong> for gas units — ensure the valve at the gas line is in the "on" (parallel to the pipe) position.</li>
                <li><strong>Look for the pilot light</strong> through the viewing window on gas units — if it's out, follow the relighting instructions on the unit's label. If it won't stay lit, that points to a thermocouple issue.</li>
                <li><strong>Check the high-limit reset button</strong> on electric units — located under the upper access panel, behind the insulation. If it's tripped, it will have popped out. Only reset once; repeated tripping means a professional diagnosis is needed.</li>
                <li><strong>Verify the thermostat setting</strong> hasn't been accidentally changed or turned down.</li>
              </ol>""",
    "when_to_call": """
              <h2>When to Call a Professional Immediately</h2>
              <ul>
                <li>The pilot light won't stay lit after attempting to relight it</li>
                <li>You smell gas near the unit — shut off the gas supply and call immediately</li>
                <li>The breaker trips again after one reset</li>
                <li>The high-limit switch trips repeatedly</li>
                <li>You've checked the basics above and still have no hot water</li>
                <li>The unit is more than 8–10 years old and showing other signs of wear</li>
              </ul>""",
    "cost_table": """
              <h2>Cost Context for No-Hot-Water Repairs</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Likely Repair</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Thermocouple replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Gas valve replacement</td><td>$300 – $450</td></tr>
                  <tr><td>Heating element replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Thermostat replacement</td><td>$130 – $230</td></tr>
                  <tr><td>High-limit switch diagnosis &amp; reset</td><td>$100 – $160</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/gas-repair.html">Gas Water Heater Repair</a></li>
                <li><a href="../services/electric-repair.html">Electric Water Heater Repair</a></li>
                <li><a href="pilot-light.html">Pilot Light Won't Stay Lit</a></li>"""
})

# ---- NOISE ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/noise.html",
    "prefix": "../",
    "title": "Water Heater Making Noise in Nampa, ID | Popping, Rumbling & Banging",
    "desc": "Water heater making noise in Nampa, ID? Learn what popping, rumbling, and banging sounds mean and when to call a pro. Call (208) 987-5152.",
    "canonical": "symptoms/noise.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/noise.html"), ("Water Heater Making Noise", "symptoms/noise.html")],
    "schema_extra": service_schema_symptom(
        "Water Heater Noise Diagnosis in Nampa, ID",
        "Diagnosis and repair of noisy water heaters in Nampa, Idaho. Sediment flushing and component repair to eliminate popping, rumbling, and banging sounds."
    ) + "\n" + faq_schema([
        ("Why does my water heater make popping or rumbling noises?",
         "Popping, rumbling, or crackling noises almost always indicate sediment buildup at the bottom of the tank. As water boils underneath the layer of sediment, steam bubbles escape through it, causing the popping sound. This is extremely common in Nampa due to hard water (200–350 ppm)."),
        ("Is it dangerous if my water heater is making loud noises?",
         "Sediment noise itself isn't immediately dangerous, but it indicates a condition that reduces efficiency and accelerates tank wear. A high-pitched whistling or screeching sound, however, can indicate high pressure or a failing T&P valve, which should be checked promptly."),
        ("Will a sediment flush stop the noise?",
         "In most cases, yes—though heavy, long-term sediment accumulation can become compacted and difficult to fully remove with a standard flush. If flushing doesn't resolve the noise, the sediment layer may be too thick, and unit replacement may be the more practical option."),
        ("What is the most common problem with a hot water heater?",
         "In Nampa, sediment buildup from hard water is the single most common water heater problem, contributing to noise, reduced efficiency, heating element failure, and shortened tank life.")
    ]),
    "h1": "Water Heater Making Noise in Nampa, Idaho — What It Means",
    "eyebrow": "Nampa, ID · Water Heater Noise Diagnosis",
    "hero_lead": "Popping, rumbling, banging, or whistling from your water heater? Most noise complaints trace back to sediment buildup from Nampa's hard water. Here's how to tell what's happening and what to do about it.",
    "causes": """
              <h2>Common Causes of Water Heater Noise in Nampa</h2>
              <ul>
                <li><strong>Popping or Cracking Sounds</strong> — The most common cause: sediment (calcium carbonate) has accumulated at the bottom of the tank. Water trapped beneath this layer boils and escapes as steam bubbles, creating a popping sound. Nampa's hard water (200–350 ppm) makes this extremely common.</li>
                <li><strong>Rumbling or Low Humming</strong> — Heavy sediment accumulation causing inefficient heat transfer, forcing the burner or elements to work harder and longer.</li>
                <li><strong>Banging or Knocking (Water Hammer)</strong> — Usually a plumbing issue rather than the water heater itself—often caused by a valve closing quickly elsewhere in the home, creating a pressure shockwave through the pipes.</li>
                <li><strong>Whistling or Screeching</strong> — Can indicate high water pressure, a partially closed shut-off valve, or a T&amp;P valve beginning to fail.</li>
                <li><strong>Ticking Sounds</strong> — Often normal expansion and contraction of metal components as the water heats and cools. Usually harmless.</li>
                <li><strong>Buzzing or Humming (Electric Units)</strong> — Can indicate a loose heating element or an electrical component issue.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Note when the noise occurs</strong> — during heating cycles, when water is running, or constantly. This helps narrow down the cause.</li>
                <li><strong>Check the age of your unit</strong> — units over 5 years old without regular flushing are highly likely to have sediment accumulation.</li>
                <li><strong>Listen for a whistling sound near the T&amp;P valve</strong> — this may indicate the valve needs replacement.</li>
                <li><strong>Check if banging happens elsewhere in the house too</strong> — if so, it may be a general water hammer issue rather than a water heater problem.</li>
              </ol>
              <p><strong>Do not attempt to flush a hot water tank yourself</strong> without proper knowledge of the shutoff and drain procedure—scalding water and pressure release require care.</p>""",
    "when_to_call": """
              <h2>When to Call a Professional</h2>
              <ul>
                <li>Popping or rumbling has been present for more than a few weeks (sediment is likely built up significantly)</li>
                <li>You hear whistling or screeching, which can indicate a pressure or valve issue</li>
                <li>The noise is accompanied by reduced hot water output or higher energy bills</li>
                <li>Your unit hasn't had a sediment flush in over a year</li>
                <li>The noise gets progressively louder over time</li>
              </ul>""",
    "cost_table": """
              <h2>Cost Context for Noise-Related Repairs</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Service</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Sediment flush</td><td>$120 – $180</td></tr>
                  <tr><td>T&amp;P valve replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Heating element replacement (if loose/failing)</td><td>$150 – $250</td></tr>
                  <tr><td>Full replacement (heavy, compacted sediment)</td><td>$1,300 – $2,500</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/maintenance.html">Water Heater Maintenance</a></li>
                <li><a href="../services/repair.html">Water Heater Repair</a></li>
                <li><a href="rusty-water.html">Rusty or Discolored Water</a></li>"""
})

# ---- PILOT LIGHT ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/pilot-light.html",
    "prefix": "../",
    "title": "Water Heater Pilot Light Won't Stay Lit in Nampa, ID | Causes & Fixes",
    "desc": "Water heater pilot light won't stay lit in Nampa, ID? Learn the causes—usually a thermocouple—and when to call a pro. Call (208) 987-5152.",
    "canonical": "symptoms/pilot-light.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/pilot-light.html"), ("Pilot Light Won't Stay Lit", "symptoms/pilot-light.html")],
    "schema_extra": service_schema_symptom(
        "Pilot Light Repair in Nampa, ID",
        "Diagnosis and repair of gas water heater pilot light failures in Nampa, Idaho. Thermocouple replacement and gas valve service."
    ) + "\n" + faq_schema([
        ("Why won't my water heater pilot light stay lit?",
         "The most common cause by far is a failed or worn thermocouple—the safety sensor that detects whether the pilot flame is burning. When it wears out, it signals the gas valve to shut off gas flow even when the pilot is actually lit. Other causes include a dirty pilot orifice, a draft blowing out the flame, or a failing gas valve."),
        ("Can I relight my pilot light myself?",
         "Yes, most manufacturers print step-by-step relighting instructions directly on the water heater. If you can successfully relight it and it stays lit, no further action needed. If it goes out again within minutes to hours, that points to a thermocouple failure requiring replacement."),
        ("How much does thermocouple replacement cost in Nampa?",
         "Thermocouple replacement in Nampa typically costs $150–$250, including parts and labor. It's one of the most common and most affordable gas water heater repairs."),
        ("Who do you call to come look at a hot water heater?",
         "Call a licensed plumber or dedicated water heater service company. Nampa Water Heater Pros specializes exclusively in water heater repair, installation, and replacement—giving faster, more accurate diagnosis than a general plumber.")
    ]),
    "h1": "Pilot Light Won't Stay Lit in Nampa, Idaho — What's Wrong",
    "eyebrow": "Nampa, ID · Gas Water Heater Pilot Light Repair",
    "hero_lead": "A pilot light that won't stay lit is one of the most common gas water heater complaints—and almost always points to one specific part: the thermocouple. Here's what's happening and how we fix it.",
    "causes": """
              <h2>Common Causes of Pilot Light Failure</h2>
              <ul>
                <li><strong>Worn Thermocouple (Most Common)</strong> — This small safety device sits in the pilot flame and generates a tiny electrical signal that tells the gas valve "the pilot is lit, keep gas flowing." When the thermocouple wears out or gets coated in soot, it can't generate a strong enough signal, so the gas valve shuts off gas flow—even though the pilot is technically burning fine. This causes the pilot to "go out" repeatedly.</li>
                <li><strong>Dirty or Clogged Pilot Orifice</strong> — Dust, soot, or debris can clog the small opening that the pilot gas flows through, causing a weak or unstable flame that's easily extinguished.</li>
                <li><strong>Draft Blowing Out the Flame</strong> — Air currents from nearby vents, doors, or ventilation can blow out an otherwise healthy pilot flame.</li>
                <li><strong>Failing Gas Valve</strong> — Less common, but if the thermocouple and pilot assembly test fine, the gas valve itself may be failing to maintain consistent gas flow.</li>
                <li><strong>Air in the Gas Line</strong> — After work on the gas system or a new tank installation, air trapped in the line can cause initial pilot lighting issues that resolve once fully purged.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Follow the manufacturer's relighting instructions</strong> printed on the water heater's control panel or door.</li>
                <li><strong>Hold the pilot button down for the full recommended time</strong> (usually 30-60 seconds) after lighting to allow the thermocouple to heat up sufficiently.</li>
                <li><strong>Observe the pilot flame color</strong> — it should be a steady blue flame. A yellow, flickering flame indicates a combustion issue.</li>
                <li><strong>Check for drafts</strong> near the unit that could be blowing out the pilot.</li>
                <li><strong>Note how long the pilot stays lit</strong> before going out — seconds vs. hours helps us diagnose the specific cause before we arrive.</li>
              </ol>""",
    "when_to_call": """
              <h2>When to Call a Professional</h2>
              <ul>
                <li>The pilot won't stay lit after 2-3 relighting attempts following manufacturer instructions</li>
                <li>You smell gas at any point — stop immediately, shut off the gas supply, and call</li>
                <li>The pilot flame looks yellow or unstable rather than steady blue</li>
                <li>The pilot lights but the burner doesn't ignite</li>
                <li>Your unit is older than 10 years and having other issues along with the pilot problem</li>
              </ul>""",
    "cost_table": """
              <h2>Cost Context for Pilot Light Repairs</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Repair Type</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Thermocouple replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Pilot assembly &amp; orifice cleaning</td><td>$150 – $220</td></tr>
                  <tr><td>Gas valve replacement</td><td>$300 – $450</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/gas-repair.html">Gas Water Heater Repair</a></li>
                <li><a href="no-hot-water.html">No Hot Water</a></li>
                <li><a href="../services/tankless-repair.html">Tankless Water Heater Repair</a></li>"""
})

# ---- RUSTY WATER ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/rusty-water.html",
    "prefix": "../",
    "title": "Rusty, Discolored, or Smelly Hot Water in Nampa, ID | Causes & Fixes",
    "desc": "Rusty, discolored, or smelly hot water in Nampa, ID? Learn what's causing it and when replacement is needed. Call (208) 987-5152.",
    "canonical": "symptoms/rusty-water.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/rusty-water.html"), ("Rusty, Discolored, or Smelly Water", "symptoms/rusty-water.html")],
    "schema_extra": service_schema_symptom(
        "Water Quality Diagnosis in Nampa, ID",
        "Diagnosis of rusty, discolored, and smelly hot water in Nampa, Idaho. Anode rod replacement and tank corrosion assessment."
    ) + "\n" + faq_schema([
        ("Why is my hot water rusty or discolored?",
         "Rusty or discolored hot water almost always originates from the water heater tank itself—either from a depleted anode rod allowing internal corrosion to begin, or from mineral sediment stirred up inside the tank. Nampa's hard water accelerates anode rod depletion, making this a common issue in the area."),
        ("Why does my hot water smell like rotten eggs?",
         "A sulfur or rotten-egg smell in hot water (but not cold) is typically caused by a chemical reaction between the magnesium anode rod and sulfate-reducing bacteria in the water, producing hydrogen sulfide gas. Replacing the anode rod with an aluminum or zinc-alloy rod usually resolves this."),
        ("Is it safe to use rusty hot water?",
         "Rust-discolored water from your own water heater (as opposed to municipal supply issues) is generally not a health hazard for bathing or washing, but it's not recommended for drinking or cooking. It also signals your tank is corroding internally and needs professional evaluation soon."),
        ("Can an anode rod replacement fix discolored water?",
         "Yes, if caught early. If the anode rod is depleted but the tank hasn't yet begun significant corrosion, replacing the anode rod can resolve rotten-egg odor and stop further internal corrosion. If the tank has already begun rusting through, replacement of the whole unit is usually necessary.")
    ]),
    "h1": "Rusty, Discolored, or Smelly Hot Water in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Water Quality & Tank Corrosion Diagnosis",
    "hero_lead": "Rust-colored water, a sulfur smell, or cloudy hot water are signs something's happening inside your tank. Here's what typically causes it in Nampa's hard-water environment, and how to tell if it's a simple fix or a sign of tank failure.",
    "causes": """
              <h2>Common Causes in Nampa Homes</h2>
              <ul>
                <li><strong>Depleted Anode Rod</strong> — The sacrificial anode rod attracts corrosive elements in the water, protecting the steel tank liner. Once it's fully depleted (typically 3-5 years, faster in Nampa's hard water), the tank itself begins to corrode, releasing rust particles into your hot water.</li>
                <li><strong>Internal Tank Corrosion</strong> — Once corrosion has started, rust-colored water is a direct symptom. This cannot be reversed—only replacement resolves ongoing tank corrosion.</li>
                <li><strong>Sulfur / Rotten Egg Smell</strong> — Caused by a reaction between the magnesium anode rod and naturally occurring sulfate-reducing bacteria, producing hydrogen sulfide gas. More common in well water but can occur with municipal supply too.</li>
                <li><strong>Sediment Stirred Up in the Tank</strong> — Mineral sediment at the tank bottom can cause temporarily cloudy or slightly discolored water, especially after the tank hasn't been used for a while or after a flush.</li>
                <li><strong>Galvanized Pipe Corrosion</strong> — In older Nampa homes, corroding galvanized steel pipes (not the water heater itself) can be the actual source of rust-colored water. Testing both hot and cold water helps isolate the source.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Test both hot and cold water separately.</strong> If only hot water is discolored, the water heater is the likely source. If both are affected, the issue may be in your home's plumbing or the municipal supply.</li>
                <li><strong>Run the hot water for several minutes</strong> and observe if the discoloration clears (suggesting stirred sediment) or persists (suggesting active corrosion).</li>
                <li><strong>Note the smell</strong> — a sulfur/rotten-egg odor specifically in hot water points to the anode rod reaction described above.</li>
                <li><strong>Check the age of your water heater.</strong> Units over 6-8 years old are at higher risk of anode rod depletion and beginning corrosion.</li>
              </ol>""",
    "when_to_call": """
              <h2>When to Call a Professional</h2>
              <ul>
                <li>Rust-colored water persists even after running the tap for several minutes</li>
                <li>A sulfur smell is present specifically in hot water</li>
                <li>Your water heater is over 6 years old and has never had the anode rod inspected</li>
                <li>You notice both discolored water and reduced hot water output (a sign of significant sediment or corrosion)</li>
                <li>You're unsure whether the source is the water heater or home plumbing</li>
              </ul>""",
    "cost_table": """
              <h2>Cost Context</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Service</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Anode rod replacement</td><td>$120 – $200</td></tr>
                  <tr><td>Sediment flush</td><td>$120 – $180</td></tr>
                  <tr><td>Full water heater replacement (active corrosion)</td><td>$1,300 – $2,500</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/maintenance.html">Water Heater Maintenance</a></li>
                <li><a href="../services/replacement.html">Water Heater Replacement</a></li>
                <li><a href="leaking.html">Water Heater Leaking</a></li>"""
})

# ---- BREAKER TRIPPING ----
SYMPTOM_PAGES.append({
    "path": f"{BASE}/symptoms/breaker-tripping.html",
    "prefix": "../",
    "title": "Water Heater Breaker Keeps Tripping in Nampa, ID | Causes & Fixes",
    "desc": "Water heater breaker keeps tripping in Nampa, ID? Learn what causes it and why you shouldn't keep resetting it. Call (208) 987-5152.",
    "canonical": "symptoms/breaker-tripping.html",
    "breadcrumbs": [("Home", ""), ("Common Issues", "symptoms/breaker-tripping.html"), ("Breaker Keeps Tripping", "symptoms/breaker-tripping.html")],
    "schema_extra": service_schema_symptom(
        "Water Heater Electrical Diagnosis in Nampa, ID",
        "Diagnosis and repair of electric water heater circuit breaker tripping issues in Nampa, Idaho. Heating element and wiring diagnostics."
    ) + "\n" + faq_schema([
        ("Why does my water heater keep tripping the breaker?",
         "A repeatedly tripping breaker on an electric water heater circuit usually indicates a failed heating element drawing excess current, a short circuit in the wiring, a failing thermostat, or a breaker that's reached the end of its service life. This should not be repeatedly reset without diagnosis."),
        ("Is it dangerous to keep resetting a tripping breaker?",
         "Yes. A breaker trips as a safety mechanism to prevent electrical fires from overcurrent conditions. Repeatedly resetting a tripping breaker without addressing the underlying cause risks electrical fire, further damage to the water heater, or damage to your home's electrical panel."),
        ("How much does it cost to fix a tripping water heater breaker?",
         "Costs vary by root cause: heating element replacement runs $150–$250, thermostat replacement $130–$230, and wiring repairs vary based on complexity. A proper diagnostic visit will identify the specific cause before recommending a repair."),
        ("Can a bad breaker itself be the problem, not the water heater?",
         "Yes, though less common. Breakers can wear out over time and become oversensitive, tripping even under normal load. If a licensed electrician confirms the water heater and its wiring are functioning properly, the breaker itself may need replacement.")
    ]),
    "h1": "Water Heater Breaker Keeps Tripping in Nampa, Idaho",
    "eyebrow": "Nampa, ID · Electric Water Heater Electrical Diagnosis",
    "hero_lead": "A water heater breaker that trips repeatedly is a safety signal, not a nuisance to work around. Here's what typically causes it and why continually resetting it is the wrong approach.",
    "causes": """
              <h2>Common Causes of Breaker Tripping</h2>
              <ul>
                <li><strong>Failed Heating Element</strong> — When a heating element begins to fail internally (often from mineral scale buildup accelerated by Nampa's hard water), it can develop a short circuit that draws excess current, tripping the breaker as a protective measure.</li>
                <li><strong>Wiring Short or Damage</strong> — Damaged insulation on wiring connections, often from age or heat exposure, can cause a short circuit.</li>
                <li><strong>Failing Thermostat</strong> — A stuck or shorting thermostat can cause the elements to draw continuous excess power.</li>
                <li><strong>Water Intrusion into Electrical Components</strong> — If the unit has a slow leak affecting the wiring compartment, this creates a serious short-circuit and shock hazard.</li>
                <li><strong>Breaker Reaching End of Life</strong> — Less commonly, an aging breaker itself may become oversensitive and trip under normal load.</li>
                <li><strong>Undersized Breaker for the Unit</strong> — If a water heater was installed with an incorrectly sized breaker (should be 30A for most 240V residential units), it may trip under normal operating conditions.</li>
              </ul>""",
    "diagnostic": """
              <h2>Safe Homeowner Diagnostic Checks</h2>
              <ol>
                <li><strong>Reset the breaker once only.</strong> If it trips again within a short time, stop resetting it and call a professional — repeated resets risk electrical damage or fire.</li>
                <li><strong>Check for visible water near the unit or its electrical panel</strong> — water intrusion into electrical components is a serious safety hazard requiring immediate professional attention.</li>
                <li><strong>Note how quickly it trips</strong> after reset — immediate tripping suggests a hard short; delayed tripping suggests a gradual overload condition.</li>
                <li><strong>Check if other appliances on the same circuit</strong> are affected, which could indicate a broader electrical panel issue rather than a water heater-specific problem.</li>
              </ol>
              <p><strong>Never attempt to open the water heater's electrical access panel yourself</strong> — this involves exposed 240V wiring and should only be handled by a licensed technician.</p>""",
    "when_to_call": """
              <h2>When to Call a Professional Immediately</h2>
              <ul>
                <li>The breaker trips again after a single reset attempt</li>
                <li>You notice any water near the unit's electrical components</li>
                <li>You smell burning or notice scorch marks near the breaker or unit</li>
                <li>The breaker feels hot to the touch</li>
                <li>Multiple appliances on the same circuit are also affected</li>
              </ul>
              <p>Turn off the breaker and leave it off until a technician can diagnose the issue.</p>""",
    "cost_table": """
              <h2>Cost Context for Electrical Diagnosis &amp; Repair</h2>
              <table class="cost-table">
                <thead>
                  <tr><th>Likely Repair</th><th>Typical Cost Range</th></tr>
                </thead>
                <tbody>
                  <tr><td>Heating element replacement</td><td>$150 – $250</td></tr>
                  <tr><td>Thermostat replacement</td><td>$130 – $230</td></tr>
                  <tr><td>Wiring diagnosis &amp; repair</td><td>$150 – $350</td></tr>
                  <tr><td>Full electrical diagnostic visit</td><td>$100 – $160</td></tr>
                </tbody>
              </table>""",
    "related_links": """                <li><a href="../services/electric-repair.html">Electric Water Heater Repair</a></li>
                <li><a href="no-hot-water.html">No Hot Water</a></li>
                <li><a href="../services/repair.html">Water Heater Repair</a></li>"""
})


def build_symptom_page(page):
    prefix = page["prefix"]
    root = prefix

    h = header(prefix, page["title"], page["desc"], page["canonical"], page["breadcrumbs"], page["schema_extra"])
    bc_html = breadcrumb_nav(page["breadcrumbs"], root)
    cta = cta_banner(
        "Still Having Water Heater Problems in Nampa?",
        "Our licensed technicians provide same-day diagnosis and repair throughout Nampa, ID. Upfront pricing, no guesswork.",
        f"Call {PHONE_DISPLAY} — Same-Day Service"
    )
    related = sidebar_related(page["related_links"])
    areas_sidebar = sidebar_areas(prefix)
    foot = footer(prefix)

    page_id = page["path"].split("/")[-1].replace(".html", "")

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
          <a href="tel:{PHONE_TEL}" class="btn-primary" aria-label="Call {BRAND} for diagnosis in Nampa">
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
{page["causes"]}
{page["diagnostic"]}
{page["when_to_call"]}
{page["cost_table"]}
          </article>

          <!-- SIDEBAR -->
          <aside class="content-sidebar" aria-label="Quick reference">
{sidebar_related(page["related_links"])}
{areas_sidebar}
          </aside>

        </div>
      </div>
    </section>
{cta}

  </main>
{foot}"""
    return content


for page in SYMPTOM_PAGES:
    html = build_symptom_page(page)
    with open(page["path"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built: {page['path']}")

print("All symptom pages built.")
