#!/usr/bin/env python3
"""v3 dataset: expand the Nampa-only topical map to exactly 300 pages."""
import sys
sys.path.insert(0, ".")
from build_data import PAGES as BASE_PAGES

# Confirmed cannibalization from v2 Table 6 -> drop, slots reused by v3 expansion.
DROP = {
    "/resources/signs-water-heater-needs-replacing",          # dup of /common-issues/water-heater-needs-replacing-nampa-id
    "/resources/water-heater-sizing-nampa-homes",             # dup of /water-heater-types/water-heater-sizing-guide
    "/resources/water-heater-control-board-error-codes",      # dup of tankless error codes + brand error-code pages
}

PAGES = [dict(p) for p in BASE_PAGES if p["url"] not in DROP]

# Per-page quality-gate metadata for v2 rows (defaults; v3 rows carry their own).
MONEY_DEFAULT = {
    "0-Core": "/services",
    "1-Service": "/services",
    "2-Issue": "/services/water-heater-repair-nampa-id",
    "3-Type": "/services/water-heater-installation-nampa-id",
    "4-Brand": "/services/water-heater-repair-nampa-id",
    "5-Location": "/services",
    "7-Resource": "/services/water-heater-repair-nampa-id",
    "8-Seasonal": "/services/water-heater-maintenance-nampa-id",
}
for p in PAGES:
    p.setdefault("money", MONEY_DEFAULT.get(p["cluster"], "/services"))
    # v2 pages already carrying an explicit GATE note are source-required.
    p.setdefault("source_req", "Yes" if "GATE:" in p.get("notes", "") or "NEEDS:" in p.get("notes", "") else "No")
    p.setdefault("cannib", "Low")
    p.setdefault("index", "Index")
    p.setdefault("intent", p.get("intent", "Informational"))
    p.setdefault("why", "")

REPAIR = "/services/water-heater-repair-nampa-id"
INSTALL = "/services/water-heater-installation-nampa-id"
REPLACE = "/services/water-heater-replacement-nampa-id"
MAINT = "/services/water-heater-maintenance-nampa-id"
TANKLESS_R = "/services/tankless-water-heater-repair-nampa-id"
TANKLESS_I = "/services/tankless-water-heater-installation-nampa-id"
EMERG = "/services/emergency-water-heater-repair-nampa-id"
FLUSH = "/services/water-heater-flushing-nampa-id"
GAS_R = "/services/gas-water-heater-repair-nampa-id"
ELEC_R = "/services/electric-water-heater-repair-nampa-id"
DESCALE = "/services/tankless-water-heater-descaling-nampa-id"
ANODE = "/services/anode-rod-replacement-nampa-id"
EXPTANK = "/services/expansion-tank-installation-repair-nampa-id"
TPVALVE = "/services/pressure-relief-valve-replacement-nampa-id"
VENT = "/services/water-heater-venting-repair-nampa-id"
RECIRC = "/services/recirculation-pump-installation-nampa-id"
INSPECT = "/services/water-heater-inspection-nampa-id"

_seq = [0]
def mk(prefix, tier, cluster, ptype, url, title, intent, parent, money,
       why, source_req="No", cannib="Low", index="Index", notes=""):
    _seq[0] += 1
    PAGES.append(dict(
        id=f"{prefix}-{_seq[0]:03d}", tier=tier, cluster=cluster, ptype=ptype, url=url,
        title=title, intent=intent, parent=parent, status="New", notes=notes,
        money=money, source_req=source_req, cannib=cannib, index=index, why=why,
    ))

# ===========================================================================
# POOL A — Deeper troubleshooting  (/common-issues)
# Symptom pages ONLY where the symptom is the query. Component-failure symptoms
# live on the component page instead (see Pool B) -- see Table 6.
# ===========================================================================
A = [
 ("tankless-water-heater-goes-cold-mid-shower","Tankless Water Heater Goes Cold Mid-Shower","T2",TANKLESS_R,
  "Owns the 'cold water sandwich' query -- tankless-specific, not covered by the tank 'runs out fast' page."),
 ("water-heater-works-intermittently","Water Heater Works Only Sometimes","T3",REPAIR,
  "Intermittent-fault diagnostic; different troubleshooting path than a hard failure."),
 ("water-heater-shuts-off-randomly","Water Heater Shuts Off Randomly","T3",REPAIR,
  "Covers safety-lockout / ECO trip / flame-sensor shutdown as a user-visible behaviour."),
 ("water-heater-slow-recovery","Water Heater Takes Too Long to Reheat","T3",REPAIR,
  "Recovery-rate complaint; bridges to the recovery-rate glossary entry and sizing guide."),
 ("burner-wont-ignite","Water Heater Burner Won't Ignite","T2",GAS_R,
  "Distinct from 'pilot light won't stay lit' -- ignition failure vs. pilot retention."),
 ("no-hot-water-one-fixture","No Hot Water at One Fixture Only","T3",REPAIR,
  "Isolates fixture/mixing-valve faults from whole-house heater faults; prevents wrong-service calls."),
 ("low-hot-water-pressure","Low Hot Water Pressure","T3",REPAIR,
  "Pressure (not temperature) complaint -- separate diagnostic chain."),
 ("water-heater-wont-fill","Water Heater Won't Fill","T4",REPAIR,
  "Post-drain refill failure; common after DIY flushing, links back to the flushing service."),
 ("crossed-hot-cold-connection","Hot and Cold Water Reversed at the Tap","T4",REPAIR,
  "Cross-connection diagnostic -- often misreported as a water heater failure."),
 ("water-hammer-banging-pipes","Banging Pipes After Hot Water Use","T4",EXPTANK,
  "Water hammer / thermal expansion symptom; bridges to expansion tank service."),
 ("water-heater-pilot-goes-out-windy","Pilot Light Blows Out in Windy Conditions","T4",GAS_R,
  "Draft/venting-specific cause; links to venting repair rather than thermocouple replacement."),
 ("water-heater-runs-constantly","Water Heater Runs Constantly / Never Shuts Off","T3",REPAIR,
  "Opposite failure mode from short cycling; distinct thermostat/dip-tube diagnostic."),
 ("lukewarm-water-only","Only Lukewarm Water, Never Hot","T3",ELEC_R,
  "Classic single-element / crossed-thermostat symptom, distinct from 'runs out fast'."),
]
for slug, title, tier, money, why in A:
    mk("A","%s"%tier,"2-Issue","Issue",f"/common-issues/{slug}",f"{title} in Nampa, ID",
       "Informational","/common-issues",money,why)

# ===========================================================================
# POOL B — Components / parts  (/water-heater-parts) -- NEW HUB
# Each page: what it does / signs of failure / repair vs replace / when to call.
# ===========================================================================
mk("B","T2","9-Parts","Hub","/water-heater-parts","Water Heater Parts & Components Explained",
   "Informational","/",REPAIR,
   "Hub for the component-entity layer. DEVIATION from rule 13 (entity->/water-heater-types): 28 part "
   "pages inside the types hub would drown the 10 system-type entities. Flagged for your override.",
   notes="Deliberate hub deviation -- see Summary sheet.")

B = [
 ("anode-rod","Anode Rod","T2",ANODE,"Sacrificial corrosion protection; the single highest-leverage part for tank longevity.","Yes"),
 ("dip-tube","Dip Tube","T3",REPAIR,"Cold-water delivery to tank bottom; failure causes lukewarm output.","No"),
 ("thermostats","Water Heater Thermostats (Upper & Lower)","T3",ELEC_R,"Temperature control on electric units; upper/lower interaction explains partial-heat symptoms.","No"),
 ("heating-elements","Heating Elements","T2",ELEC_R,"Primary electric heat source; burnout is the most common electric failure.","No"),
 ("thermocouple","Thermocouple","T2",GAS_R,"Flame-proving safety device; the usual cause of pilot-retention failure.","No"),
 ("gas-control-valve","Gas Control Valve","T2",GAS_R,"Combined thermostat/gas regulator; expensive part driving repair-vs-replace decisions.","No"),
 ("burner-assembly","Burner Assembly","T3",GAS_R,"Combustion component; soot//flame-pattern faults indicate service need.","No"),
 ("pilot-assembly","Pilot Assembly","T3",GAS_R,"Standing-pilot ignition group; distinct part from the thermocouple it houses.","No"),
 ("igniter","Igniter (Piezo & Electronic)","T3",GAS_R,"Electronic ignition failure mode on modern units without standing pilots.","No"),
 ("flame-sensor","Flame Sensor","T3",GAS_R,"Flame-rectification sensing; dirty sensors cause intermittent lockouts.","No"),
 ("heat-exchanger","Heat Exchanger (Tankless)","T2",TANKLESS_R,"Core tankless component; scale damage here drives descaling economics.","No"),
 ("pressure-relief-valve","Temperature & Pressure Relief (T&P) Valve","T2",TPVALVE,"Primary overpressure safety device; never to be capped or plugged.","No"),
 ("expansion-tank","Thermal Expansion Tank","T2",EXPTANK,"Absorbs thermal expansion in closed systems; failure causes pressure spikes.","No"),
 ("drain-valve","Drain Valve","T3",FLUSH,"Flushing access point; plastic valve failure is a common post-maintenance leak source.","No"),
 ("water-shutoff-valve","Cold-Water Shutoff Valve","T3",REPAIR,"Isolation point every homeowner should locate before an emergency.","No"),
 ("gas-shutoff-valve","Gas Shutoff Valve","T3",GAS_R,"Gas isolation point; pairs with the emergency shut-off safety pages.","No"),
 ("venting-system","Venting System (Flue & Draft Hood)","T2",VENT,"Combustion-gas exhaust; improper venting is a CO risk, not just an efficiency issue.","No"),
 ("condensate-drain","Condensate Drain","T3",TANKLESS_R,"Condensing-unit byproduct handling; blockage causes shutdowns and nuisance leaks.","No"),
 ("recirculation-pump","Recirculation Pump","T3",RECIRC,"Hot-water delivery speed component; the main comfort upgrade sold at install.","No"),
 ("mixing-valve","Thermostatic Mixing Valve","T3",INSTALL,"Allows high tank storage temp with safe delivery temp; ties to scald-risk safety page.","No"),
 ("high-limit-switch","High-Limit Switch (ECO)","T3",ELEC_R,"Overtemperature cutout; repeated trips signal a thermostat fault, not a nuisance.","No"),
 ("heat-trap-nipples","Heat Trap Nipples","T4",INSTALL,"Standby-loss reduction fitting; commonly mistaken for a flow restriction.","No"),
 ("dielectric-nipples","Dielectric Nipples & Unions","T4",INSTALL,"Galvanic-corrosion prevention at dissimilar-metal joints.","No"),
 ("drain-pan","Drain Pan & Pan Drain Line","T3",INSTALL,"Leak containment; central to the garage/upper-floor installation safety argument.","No"),
 ("flow-sensor","Flow Sensor (Tankless)","T4",TANKLESS_R,"Activation component; low-flow cutoff explains 'won't fire at low draw' complaints.","No"),
 ("blower-power-vent-motor","Power Vent Blower Motor","T4",VENT,"Power-vent-specific component with its own noise and lockout failure modes.","No"),
 ("insulation-jacket","Tank Insulation & Jacket","T4",MAINT,"Standby-loss factor; also the 'should I add a blanket' question.","No"),
 ("sediment-trap","Gas Line Sediment Trap (Drip Leg)","T4",GAS_R,"Code-relevant gas-line fitting protecting the gas valve.","No"),
]
for slug, title, tier, money, why, src in B:
    mk("B",tier,"9-Parts","Component",f"/water-heater-parts/{slug}",f"{title}: Function, Failure Signs & Repair",
       "Informational","/water-heater-parts",money,why,source_req=src,
       notes="Component page owns this part's failure symptoms -- do NOT build a parallel symptom page in /common-issues (Table 6).")

# ===========================================================================
# POOL C — Maintenance & prevention  (/resources)
# ===========================================================================
C = [
 ("water-heater-flushing-schedule","How Often to Flush a Water Heater","T3",FLUSH,"Interval guidance page distinct from the how-to; anchors the maintenance upsell.","Yes"),
 ("sediment-prevention","How to Prevent Sediment Buildup","T3",FLUSH,"Prevention framing distinct from the sediment symptom page.","No"),
 ("tankless-descaling-schedule","How Often to Descale a Tankless Water Heater","T3",DESCALE,"Tankless-specific interval; manufacturer-manual framing required.","Yes"),
 ("scale-prevention","Preventing Mineral Scale on Heat Exchangers","T4",DESCALE,"Scale (heat-exchanger deposit) is a different mechanism from tank sediment.","No"),
 ("water-heater-vacation-mode","Using Vacation Mode on Your Water Heater","T4",MAINT,"Covers both the vacation setting and extended-absence shutdown guidance.","No"),
 ("power-outage-water-heater-restart","Restarting a Water Heater After a Power Outage","T3",REPAIR,"High-intent seasonal/event query with a real safety sequence.","No"),
 ("leak-prevention","Water Heater Leak Prevention","T3",INSPECT,"Preventive framing feeding inspection service; distinct from 'it is leaking now'.","No"),
 ("corrosion-prevention","Preventing Water Heater Corrosion","T3",ANODE,"Ties anode, dielectric fittings and water chemistry into one preventive narrative.","No"),
 ("water-pressure-expansion-checks","Checking Home Water Pressure & Expansion Tank Charge","T3",EXPTANK,"DIY diagnostic supporting expansion tank and T&P service.","No"),
 ("drain-pan-maintenance","Drain Pan Inspection & Maintenance","T4",INSPECT,"Small but real maintenance task, especially for garage/upper-floor units.","No"),
 ("utility-room-ventilation","Utility Room Ventilation for Water Heaters","T4",VENT,"Combustion-air adequacy in confined spaces.","Yes"),
 ("annual-inspection-what-techs-check","What a Technician Checks During an Annual Inspection","T3",INSPECT,"Sells the inspection service by making the scope concrete.","No"),
 ("extend-water-heater-lifespan","How to Extend Water Heater Lifespan","T3",MAINT,"Aggregator page linking the whole prevention cluster to the maintenance money page.","Yes"),
 ("insulation-blanket-guidance","Should You Add an Insulation Blanket?","T4",MAINT,"Common DIY question with real do/do-not-cover safety caveats.","No"),
 ("pipe-insulation-hot-water","Insulating Hot Water Pipes","T4",RECIRC,"Delivery-efficiency topic supporting recirculation upsell.","No"),
 ("temperature-setting-efficiency","Best Water Heater Temperature Setting","T2",MAINT,"High-volume question sitting between efficiency and scald safety.","Yes"),
 ("supply-line-replacement","When to Replace Water Heater Supply Lines","T4",INSTALL,"Flex-connector failure is a top flood cause at replacement time.","No"),
 ("rental-property-water-heater-maintenance","Water Heater Maintenance for Rentals & Vacation Homes","T4",MAINT,"Landlord/absentee-owner segment with distinct needs.","No"),
 ("water-heater-maintenance-log","Keeping a Water Heater Maintenance Log","T4",MAINT,"Practical tool page; supports warranty-claim documentation.","No"),
 ("noise-prevention-maintenance","Preventing Water Heater Noise","T4",FLUSH,"Preventive counterpart to the noise diagnostic page.","No"),
]
for slug, title, tier, money, why, src in C:
    mk("C",tier,"7-Resource","Maintenance",f"/resources/{slug}",title,"Informational","/resources",money,why,source_req=src)

# ===========================================================================
# POOL D — Cost & buyer guides  (/resources). No unsourced figures: cost-factor framing.
# ===========================================================================
D = [
 ("tankless-water-heater-cost","Tankless Water Heater Cost Factors","T2",TANKLESS_I,"Tankless-specific cost drivers (gas sizing, venting, electrical) absent from the tank cost guides.","Yes"),
 ("gas-vs-electric-operating-cost","Gas vs. Electric Water Heater Operating Cost","T2",INSTALL,"Running-cost comparison distinct from purchase/install cost.","Yes"),
 ("labor-cost-factors","What Drives Water Heater Labor Cost","T3",REPAIR,"Explains variability (access, code upgrades, permits) without quoting numbers.","No"),
 ("emergency-service-cost-factors","Emergency Water Heater Service Cost Factors","T3",EMERG,"After-hours cost expectations; supports the emergency money page.","No"),
 ("permit-cost-guidance","Water Heater Permit Cost in Nampa","T4",INSTALL,"Permit fee guidance.","Yes"),
 ("warranty-cost-considerations","Water Heater Warranty Cost Considerations","T4",REPLACE,"Parts-only vs. labor coverage economics at replacement time.","No"),
 ("brand-price-comparison","Water Heater Brand Price Positioning","T3",REPLACE,"Relative positioning across the 8 serviced brands.","Yes"),
 ("size-capacity-cost-comparison","Water Heater Cost by Size & Capacity","T3",REPLACE,"Capacity-to-cost relationship supporting the sizing guide.","No"),
 ("energy-efficiency-payback","Energy-Efficiency Payback on a New Water Heater","T3",INSTALL,"Payback-period reasoning for heat pump / condensing upgrades.","Yes"),
 ("total-cost-of-ownership","Water Heater Total Cost of Ownership","T3",REPLACE,"Lifetime framing combining purchase, operating, and maintenance cost.","Yes"),
 ("cost-of-delaying-repair","The Cost of Delaying a Water Heater Repair","T4",REPAIR,"Urgency framing tied to real escalation paths (leak -> flood -> replacement).","No"),
 ("annual-operating-cost-by-fuel","Annual Operating Cost by Fuel Type","T4",INSTALL,"Fuel-type running-cost breakdown feeding the gas-vs-electric decision.","Yes"),
 ("budgeting-for-water-heater-replacement","Budgeting for a Water Heater Replacement","T4",REPLACE,"Planning-horizon page for homeowners with an aging unit. No financing claims.","No"),
]
for slug, title, tier, money, why, src in D:
    mk("D",tier,"7-Resource","Cost Guide",f"/resources/{slug}",title,"Informational","/resources",money,why,source_req=src,
       notes="Cost-FACTOR framing only. Reuse the existing $150-$600 repair range verbatim where cited (PRICE-REPO-N008); introduce no new dollar figures without a source.")

# ===========================================================================
# POOL E — Comparisons (system comparisons -> /water-heater-types; process -> /resources)
# ===========================================================================
E_TYPES = [
 ("50-gallon-vs-tankless","50-Gallon Tank vs. Tankless","T2",TANKLESS_I,"Most common real upgrade decision for an existing 50-gal household."),
 ("hybrid-vs-electric","Hybrid Heat Pump vs. Standard Electric","T2",INSTALL,"Efficiency-upgrade decision inside the electric fuel path."),
 ("condensing-vs-non-condensing-tankless","Condensing vs. Non-Condensing Tankless","T3",TANKLESS_I,"Venting and efficiency trade-off specific to tankless buyers."),
 ("electric-tankless-vs-gas-tankless","Electric vs. Gas Tankless","T3",TANKLESS_I,"Electrical-service feasibility is the deciding factor; distinct from tank gas-vs-electric."),
 ("power-vent-vs-atmospheric-vent","Power Vent vs. Atmospheric Vent","T3",VENT,"Venting-configuration decision affecting install feasibility."),
 ("direct-vent-vs-power-vent","Direct Vent vs. Power Vent","T4",VENT,"Combustion-air source distinction; matters in confined utility rooms."),
 ("natural-gas-vs-propane","Natural Gas vs. Propane Water Heaters","T4",INSTALL,"Fuel-supply decision for homes outside natural-gas service."),
 ("single-vs-dual-element-electric","Single vs. Dual Element Electric Water Heaters","T4",ELEC_R,"Recovery-rate implications; explains partial-heat symptoms."),
 ("standard-vs-high-efficiency","Standard vs. High-Efficiency Water Heaters","T3",INSTALL,"Efficiency-tier decision feeding payback and rebate pages."),
]
for slug, title, tier, money, why in E_TYPES:
    mk("E","%s"%tier,"3-Type","Comparison",f"/water-heater-types/{slug}",title,"Informational","/water-heater-types",money,why)

E_RES = [
 ("professional-repair-vs-diy","Professional Repair vs. DIY","T2",REPAIR,"Scope-of-safe-DIY decision; the natural conversion bridge from every DIY guide."),
 ("flushing-vs-descaling","Flushing vs. Descaling: What's the Difference","T3",MAINT,"Two maintenance actions routinely confused; disambiguates tank vs. tankless service."),
 ("anode-replacement-vs-tank-replacement","Anode Rod Replacement vs. Replacing the Tank","T2",ANODE,"Spend-now-vs-later decision unique to aging tanks."),
 ("expansion-tank-vs-pressure-regulator","Expansion Tank vs. Pressure-Reducing Valve","T3",EXPTANK,"Two different fixes for two different pressure problems, commonly conflated."),
 ("pilot-issue-vs-gas-valve-issue","Pilot Light Problem vs. Gas Valve Problem","T3",GAS_R,"Triage page separating a cheap fix from an expensive one."),
 ("noisy-heater-vs-sediment","Noisy Water Heater vs. Sediment Problem","T4",FLUSH,"Clarifies when noise indicates sediment and when it does not."),
 ("repair-vs-replace-by-age","Repair or Replace Based on Unit Age","T3",REPLACE,"Age-threshold decision framework complementing the cost-based one."),
]
for slug, title, tier, money, why in E_RES:
    mk("E",tier,"7-Resource","Comparison",f"/resources/{slug}",title,"Informational","/resources",money,why)

# ===========================================================================
# POOL F — Safety  (/resources). Conservative language; no medical/legal claims.
# ===========================================================================
F = [
 ("water-heater-fire-risk","Water Heater Fire Risk & Prevention","T2",INSPECT,"Flammable-vapour and clearance hazards, especially garage installs.","Yes"),
 ("scalding-risk","Scalding Risk & Safe Water Temperature","T2",MAINT,"Temperature-safety page; pairs with mixing valve and temperature-setting pages.","Yes"),
 ("electrical-shock-risk","Electrical Safety Around Electric Water Heaters","T2",ELEC_R,"240V hazard awareness before any DIY element/thermostat work.","No"),
 ("pressure-relief-valve-safety","T&P Valve Safety: Why It Must Never Be Capped","T2",TPVALVE,"Single highest-consequence water heater safety rule.","Yes"),
 ("improper-venting-risks","Risks of Improper Water Heater Venting","T2",VENT,"Backdrafting and CO exposure; conservative framing, no medical claims.","Yes"),
 ("garage-water-heater-safety","Garage Water Heater Safety & Clearance","T2",INSTALL,"Elevation/ignition-source requirements relevant to many Nampa garage installs.","Yes"),
 ("when-to-shut-off-gas","When to Shut Off the Gas to Your Water Heater","T2",EMERG,"Decision page in the emergency triage set.","No"),
 ("when-to-shut-off-water","When to Shut Off the Water to Your Water Heater","T2",EMERG,"Companion decision page for leak scenarios.","No"),
 ("when-to-shut-off-power","When to Shut Off Power to an Electric Water Heater","T3",EMERG,"Completes the three-utility emergency triage set.","No"),
 ("when-to-call-emergency-service","When to Call Emergency Water Heater Service","T2",EMERG,"Threshold page converting safety traffic into the emergency money page.","No"),
 ("gas-leak-detection-basics","Recognising a Gas Leak at Home","T3",EMERG,"Detection-awareness page; defers to the gas utility for emergencies.","Yes"),
 ("co-detector-placement","Carbon Monoxide Detector Placement Near Appliances","T3",VENT,"Practical safety measure supporting the venting cluster.","Yes"),
 ("safe-temperature-for-households","Choosing a Safe Temperature for Kids & Older Adults","T3",MAINT,"Household-specific temperature guidance; conservative, non-medical framing.","Yes"),
 ("diy-repair-risks","Risks of DIY Water Heater Repair","T3",REPAIR,"Complements the pro-vs-DIY comparison with the specific hazard list.","No"),
 ("water-heater-explosion-risk","Water Heater Overpressure Risk Explained","T3",TPVALWE if False else TPVALVE,"Explains the pressure-failure mechanism the T&P valve exists to prevent. Factual, non-sensational framing.","Yes"),
]
for slug, title, tier, money, why, src in F:
    mk("F",tier,"7-Resource","Safety",f"/resources/{slug}",title,"Informational","/resources",money,why,source_req=src,
       notes="SAFETY PAGE: conservative language only. No medical, legal, or insurance advice. Defer to gas utility / fire service / manufacturer for emergency instruction.")

# ===========================================================================
# POOL G — Local Nampa context  (/resources). Nampa-only; no new service areas.
# ===========================================================================
G = [
 ("nampa-home-water-heater-problems","Common Water Heater Problems in Nampa Homes","T2",REPAIR,"Local aggregator tying the issue cluster to Nampa housing context.","Yes"),
 ("nampa-homeowner-checklist","Nampa Homeowner Water Heater Checklist","T3",MAINT,"Local practical checklist; entry point for new residents.","No"),
 ("older-nampa-homes-replacement","Water Heater Replacement in Older Nampa Homes","T2",REPLACE,"Ties Downtown/Central Nampa's older housing stock to replacement decisions.","Yes"),
 ("new-construction-nampa-sizing","Water Heater Sizing for New Construction in Nampa","T3",INSTALL,"Complements the South Nampa newer-construction angle.","Yes"),
 ("garage-water-heaters-nampa","Garage Water Heaters in Nampa Homes","T3",INSTALL,"Local installation pattern with freeze and clearance implications.","Yes"),
 ("nampa-winter-freeze-risk","Freeze Risk for Garage & Unheated-Space Water Heaters","T3",MAINT,"Seasonal local risk page; links winterizing to garage installs.","Yes"),
 ("canyon-county-code-overview","Canyon County Water Heater Code Overview","T4",INSTALL,"Local code orientation page.","Yes"),
 ("nampa-seasonal-water-usage","Seasonal Water Usage Patterns in Nampa","T4",MAINT,"Irrigation-season demand context.","Yes"),
 ("nampa-water-heater-replacement-timeline","What to Expect: Water Heater Replacement Timeline","T3",REPLACE,"Sets local expectations for scheduling, permits and install duration.","No"),
 ("hard-water-appliance-impact-nampa","Hard Water's Impact on Nampa Household Appliances","T3",MAINT,"Broadens the hard-water entity beyond the heater while staying locally framed.","Yes"),
]
for slug, title, tier, money, why, src in G:
    mk("G",tier,"7-Resource","Local Context",f"/resources/{slug}",title,"Informational","/resources",money,why,source_req=src,
       notes="LOCAL CLAIM GATE: any hardness figure, code citation, rebate amount, housing-stock statistic or utility fact requires a directly fetched primary source (verified-claims.md 9.1/9.3). Qualitative framing until then.")

# ===========================================================================
# POOL H — Glossary  (/glossary) -- NEW HUB
# Every glossary page must link to >=1 service page and >=1 issue page.
# ===========================================================================
mk("H","T3","10-Glossary","Hub","/glossary","Water Heater Glossary","Informational","/",REPAIR,
   "Entity-definition layer. Captures definitional queries that would otherwise force definitions into "
   "money pages, and gives the internal-link graph a clean set of attribute nodes.")

H = [
 ("btu","BTU","T4",INSTALL,"Heat-output unit underpinning every sizing and fuel comparison."),
 ("recovery-rate","Recovery Rate","T3",INSTALL,"Core spec behind 'runs out fast' and sizing decisions."),
 ("first-hour-rating","First Hour Rating (FHR)","T3",INSTALL,"The sizing spec most buyers have never heard of but need."),
 ("ef-rating","Energy Factor (EF)","T4",INSTALL,"Legacy efficiency metric still printed on older units."),
 ("thermal-expansion","Thermal Expansion","T3",EXPTANK,"The physical mechanism behind expansion tanks and pressure spikes."),
 ("dielectric-nipple","Dielectric Nipple","T4",INSTALL,"Galvanic-corrosion prevention term encountered during installs."),
 ("heat-trap-nipple","Heat Trap Nipple","T4",INSTALL,"Standby-loss fitting frequently mistaken for a defect."),
 ("drip-leg","Drip Leg / Sediment Trap","T4",GAS_R,"Gas-line code term homeowners meet at inspection."),
 ("gas-shutoff-valve-term","Gas Shutoff Valve","T4",EMERG,"Safety-critical term in every emergency instruction."),
 ("dedicated-circuit","Dedicated Circuit","T4",ELEC_R,"Electrical requirement governing electric and hybrid feasibility."),
 ("direct-vent","Direct Vent","T4",VENT,"Venting classification determining install options."),
 ("power-vent","Power Vent","T4",VENT,"Venting classification with its own components and failure modes."),
 ("atmospheric-vent","Atmospheric Vent","T4",VENT,"Natural-draft classification; the backdrafting risk category."),
 ("scale","Mineral Scale","T3",DESCALE,"Heat-exchanger deposit distinct from tank sediment."),
 ("gpm-flow-rate","GPM (Flow Rate)","T3",TANKLESS_I,"Tankless sizing unit; the spec that decides simultaneous-fixture capability."),
 ("temperature-rise","Temperature Rise","T3",TANKLESS_I,"Paired with GPM for tankless sizing; groundwater-temperature dependent."),
 ("standby-loss","Standby Loss","T4",MAINT,"Efficiency concept justifying insulation and heat traps."),
 ("closed-plumbing-system","Closed Plumbing System","T3",EXPTANK,"The condition that makes an expansion tank necessary."),
 ("backdrafting","Backdrafting","T3",VENT,"Combustion-safety term central to the venting risk pages."),
 ("flue-gas","Flue Gas","T4",VENT,"Combustion byproduct term underlying venting requirements."),
 ("condensate-neutralizer","Condensate Neutralizer","T4",TANKLESS_I,"Condensing-unit accessory with drainage-code implications."),
 ("sacrificial-protection","Sacrificial (Cathodic) Protection","T4",ANODE,"The corrosion-science principle behind anode rods."),
 ("nsf-certification","NSF Certification","T4","/services/commercial-water-heater-installation-nampa-id","Commercial-compliance term relevant to food-service installs."),
 ("vent-category","Vent Categories (I-IV)","T4",VENT,"Classification determining allowable vent materials."),
 ("uef-term","Uniform Energy Factor (UEF)","T4",INSTALL,"Glossary stub only -- the full explainer lives at /water-heater-types/energy-efficiency-ratings-uef."),
 ("water-hardness-grains","Water Hardness (Grains per Gallon)","T4",MAINT,"Measurement unit page; no Nampa-specific figure without a source."),
]
for slug, title, tier, money, why in H:
    src = "Yes" if slug == "water-hardness-grains" else "No"
    cannib = "Medium" if slug in ("uef-term","sacrificial-protection","drip-leg","gas-shutoff-valve-term") else "Low"
    idx = "Needs Review" if cannib == "Medium" else "Index"
    mk("H",tier,"10-Glossary","Glossary",f"/glossary/{slug}",f"{title}: Definition & Why It Matters",
       "Informational","/glossary",money,why,source_req=src,cannib=cannib,index=idx,
       notes="Glossary requirement: must link to >=1 service page and >=1 issue page, and must carry real explanatory "
             "depth. If it cannot exceed a dictionary definition, fold it into its parent entity page instead of publishing.")

# ===========================================================================
# POOL I — Brand troubleshooting & error codes  (/brands)
# No authorized-dealer / authorized-service claims anywhere.
# ===========================================================================
I_PAGES = [
 ("rheem-water-heater-troubleshooting","Rheem Water Heater Troubleshooting","T2",REPAIR),
 ("rheem-error-codes","Rheem Water Heater Error Codes","T2",REPAIR),
 ("ao-smith-water-heater-troubleshooting","A.O. Smith Water Heater Troubleshooting","T2",REPAIR),
 ("ao-smith-error-codes","A.O. Smith Water Heater Error Codes","T3",REPAIR),
 ("bradford-white-troubleshooting","Bradford White Water Heater Troubleshooting","T3",REPAIR),
 ("bradford-white-error-codes","Bradford White Water Heater Error Codes","T4",REPAIR),
 ("navien-error-codes","Navien Tankless Error Codes","T2",TANKLESS_R),
 ("rinnai-error-codes","Rinnai Tankless Error Codes","T2",TANKLESS_R),
 ("noritz-error-codes","Noritz Tankless Error Codes","T3",TANKLESS_R),
 ("state-water-heater-troubleshooting","State Water Heater Troubleshooting","T4",REPAIR),
 ("american-standard-troubleshooting","American Standard Water Heater Troubleshooting","T4",REPAIR),
 ("water-heater-warranty-lookup","How to Check Your Water Heater Warranty","T3",REPLACE),
 ("water-heater-model-serial-lookup","How to Find Your Water Heater's Model, Serial & Age","T2",REPLACE),
]
for slug, title, tier, money in I_PAGES:
    why = ("Brand-specific diagnostic intent, distinct from the brand's commercial repair page "
           "(which owns the 'hire someone in Nampa' query).")
    if "error-codes" in slug:
        why = "Error-code lookup is a high-volume, unambiguous informational query per brand; distinct from general troubleshooting."
    if "warranty" in slug or "model-serial" in slug:
        why = "Cross-brand utility page homeowners need before any repair-or-replace decision."
    mk("I",tier,"4-Brand","Brand Support",f"/brands/{slug}",f"{title}",
       "Informational","/brands",money,why,source_req="Yes",cannib="Medium",
       notes="BRAND CLAIM GATE: no 'authorized dealer', 'authorized service center', 'certified by <brand>' or "
             "warranty-authority claims unless verified in writing. Error-code tables must be transcribed from the "
             "manufacturer's own published documentation, cited -- never reconstructed from memory.")

# ===========================================================================
# POOL J — Seasonal / calendar  (/resources)
# ===========================================================================
J = [
 ("fall-water-heater-inspection","Fall Water Heater Inspection Checklist","T3",INSPECT,"Pre-heating-season inspection prompt."),
 ("holiday-guest-hot-water-prep","Preparing Hot Water Capacity for Holiday Guests","T4",MAINT,"Demand-spike scenario; bridges to sizing and recovery-rate content."),
 ("before-freeze-checklist","Before-Freeze Water Heater Checklist","T3",MAINT,"Event-triggered seasonal page distinct from general winterizing."),
 ("annual-water-heater-calendar","Annual Water Heater Care Calendar","T3",MAINT,"Month-by-month hub tying the whole seasonal set together."),
 ("back-to-school-hot-water-demand","Managing Hot Water Demand for Busy Households","T4",INSTALL,"Household-demand framing supporting sizing decisions."),
 ("spring-thaw-leak-check","Spring Leak Check After Winter","T4",INSPECT,"Post-winter inspection prompt complementing the spring checklist."),
]
for slug, title, tier, money, why in J:
    mk("J",tier,"8-Seasonal","Seasonal",f"/resources/{slug}",title,"Informational","/resources",money,why)

if __name__ == "__main__":
    from collections import Counter
    print(f"TOTAL: {len(PAGES)}")
    print("status:", Counter(p["status"] for p in PAGES))
    print("cluster:", Counter(p["cluster"] for p in PAGES))
    print("tier:", Counter(p["tier"] for p in PAGES))
    urls = [p["url"] for p in PAGES]
    dupes = [u for u, c in Counter(urls).items() if c > 1]
    print("DUPLICATE URLS:", dupes if dupes else "none")
