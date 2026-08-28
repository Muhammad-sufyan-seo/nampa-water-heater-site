# Verified Claims Registry — nampawaterheater.com

This registry is the single source of truth for every factual, numeric,
comparative, technical, safety, or business claim published on this site.
**A claim's presence in website copy, JSON-LD, an HTML comment, or a prior
planning document is not evidence of that claim's accuracy.** Only an entry
in this file, backed by the fields below, establishes publication status.
See `rules/content-seo-rules.md` §9 (Factual Integrity and Source
Verification) for the full policy this registry implements.

**This registry is adapted from the Harrisburg reference site's
`docs/verified-claims.md` methodology, not its findings.** Harrisburg's
specific conclusions (about Harrisburg's water utility, Harrisburg
geography) do not transfer to Nampa. Every entry below was produced by
reading Nampa's actual published content and applying the same evidentiary
standard fresh — it is not a find-replace of the Harrisburg registry.

**Core rule: Repetition is not verification.** A claim repeated across 13
pages has the same evidentiary weight as the same claim on one page:
whatever is recorded here.

## Status definitions

| Status | Meaning | May publish? |
|---|---|---|
| `Verified` | Directly accessible primary source, exact URL, exact quotation on file | Yes, with required qualifiers |
| `Conditional` | Evidence exists but is incomplete, indirect, or the claim's stated condition must accompany it | **No** — prohibited until the condition is met or source is upgraded to Verified |
| `Unverified` | No qualifying source found, or no source sought at all | **No** |
| `Retired` | Actively investigated and found unsupported; do not re-propose without new evidence | **No** |
| `Owner-confirmed` | Business-controlled fact (not independently verifiable) with an identifiable written confirmation record | Yes, citing the record |

## Registry entries

---

### `WATER-HARD-N001` — Nampa/Canyon County water hardness "200–350 ppm"

- **Exact claim:** "Nampa's municipal water supply is considered moderately
  to very hard, typically measuring 200–350 parts per million (ppm) of
  calcium carbonate" / "hard water (200–350 ppm)"
- **Classification:** Local fact (water-quality)
- **Status:** `Unverified`
- **Publication permission:** **Prohibited as a specific figure** — no
  utility, municipal, or standards-body source was ever fetched for this
  number. It was written as a plausible-sounding range during initial site
  construction, not sourced from Nampa's actual water provider (City of
  Nampa Public Works / relevant Canyon County water utility annual
  report).
- **Source URL:** None obtained.
- **Exact supporting quotation:** None on file.
- **Source type:** N/A
- **Affected paths/sections:** 13 files sitewide — `index.html` (FAQ text +
  visible answer), `about.html`, `areas/central-nampa.html`,
  `areas/downtown-nampa.html`, `services/commercial-repair.html`,
  `services/electric-repair.html`, `services/gas-repair.html`,
  `services/installation.html`, `services/maintenance.html`,
  `services/repair.html`, `services/tankless-installation.html`,
  `services/tankless-repair.html`, `symptoms/noise.html`
- **Limitations/conditions:** Idaho's Snake River Plain aquifer region
  (which supplies Canyon County) is broadly known to run hard, so a
  qualitative "hard water" framing is plausible — but a specific ppm range
  requires a fetched, citable source, not plausibility. Do not swap in a
  different unsourced number, and do not remove the qualitative "hard
  water" framing entirely without owner input — see remediation approach
  below.
- **Owner-confirmation record:** None
- **Review trigger:** A directly fetchable City of Nampa or water-provider
  hardness report becomes available
- **Date checked:** 2026-08-28
- **Remediation approach (see `AUDIT-REPORT.md` Phase 3/4 for what was
  actually applied):** replace the specific "200–350 ppm" figure with
  non-numeric qualitative language ("Nampa's water supply is considered
  hard" / "local hard-water conditions") in visible text and FAQ answers,
  consistent with §9.3's rule that an unresolved local-fact claim gets
  `Unverified` treatment, not a swapped assertion.

---

### `LIFE-HARDWATER-N002` — Hard water shortens tank life by 1–3 years

- **Exact claim:** "hard water (200–350 ppm) can reduce this by 1–3 years if
  annual sediment flushing isn't performed" / "shortens tank lifespan"
- **Classification:** Technical / comparative
- **Status:** `Unverified`
- **Publication permission:** **Prohibited**
- **Source URL:** None. No DOE, EPA, or manufacturer publication was ever
  sought for this figure — unlike the Harrisburg site (which searched and
  found nothing), Nampa's copy was written without a search being
  attempted at all.
- **Exact supporting quotation:** None obtainable.
- **Source type:** N/A — no source type, since none was sought
- **Affected paths/sections:** `index.html` (FAQ), `services/gas-repair.html`
  (FAQ)
- **Limitations/conditions:** The general mechanism (mineral scale reduces
  heating efficiency and can accelerate component wear) is plausible and
  widely stated across the plumbing trade, but the specific "1–3 years"
  figure and any DOE-style attribution require a real source neither
  Harrisburg nor Nampa's content ever obtained.
- **Owner-confirmation record:** N/A
- **Review trigger:** A directly fetchable DOE, EPA, or WQA publication
  stating a comparable figure is found
- **Date checked:** 2026-08-28

---

### `MAINT-STUDY-N003` — "Studies show" 30–50% longer life claim

- **Exact claim:** "Studies show properly maintained water heaters in
  hard-water areas last 30–50% longer than neglected units."
- **Classification:** Technical / comparative, unattributed
- **Status:** `Unverified` — **worse than a missing citation, since the
  sentence claims "studies show" without naming any study.** This is a
  weasel-word pattern — remove or attribute for real; never leave "studies
  show" standing without a named source.
- **Publication permission:** **Prohibited**
- **Source URL:** None
- **Exact supporting quotation:** None
- **Source type:** N/A
- **Affected paths/sections:** `services/maintenance.html`
- **Limitations/conditions:** None found in any form
- **Owner-confirmation record:** N/A
- **Review trigger:** A specific, named, directly fetchable study is found
  making a comparable claim
- **Date checked:** 2026-08-28

---

### `INT-MAINT-N004` — Universal annual sediment flush / anode rod
inspection / tankless descaling intervals

- **Exact claims:** "we recommend annual maintenance for all water heater
  types" / "Standard tank units need annual sediment flushing and anode
  rod inspection" / "Tankless units need annual descaling plus inlet
  filter cleaning every 6 months" / "Annual flushing is the minimum
  maintenance recommendation"
- **Classification:** Technical / maintenance interval
- **Status:** `Unverified` as universal schedules
- **Publication permission:** **Prohibited as a universal, one-size
  schedule** — manufacturer maintenance intervals vary by brand and model
  (mirrors the exact issue Harrisburg found and fixed for the identical
  claim shape). No manufacturer documentation was fetched to support a
  single sitewide interval.
- **Source URL:** None
- **Exact supporting quotation:** None
- **Source type:** N/A
- **Affected paths/sections:** `services/maintenance.html` (primary — the
  whole page is built around these intervals), `areas/downtown-nampa.html`,
  and general "annual flushing" mentions across several other service
  pages
- **Limitations/conditions:** Approved wording pattern (matches Harrisburg's
  locked wording, adapted): "Follow the maintenance schedule specified by
  the manufacturer," "many manufacturers recommend an annual check," "the
  owner's manual governs the exact interval for your unit."
- **Owner-confirmation record:** N/A
- **Review trigger:** A directly fetchable manufacturer specification for a
  named model/brand sold by this business
- **Date checked:** 2026-08-28

---

### `INT-ANODE-N005` — Anode rod depletion "typically 3-5 years"

- **Exact claim:** "Once it's fully depleted (typically 3-5 years, faster in
  Nampa's hard water)"
- **Classification:** Technical / maintenance interval
- **Status:** `Unverified`
- **Publication permission:** **Prohibited as a universal figure**
- **Source URL:** None
- **Exact supporting quotation:** None
- **Source type:** N/A
- **Affected paths/sections:** `symptoms/rusty-water.html`
- **Limitations/conditions:** Anode rod life is manufacturer- and
  water-chemistry-dependent; no universal figure is supportable without a
  named source.
- **Owner-confirmation record:** N/A
- **Review trigger:** A directly fetchable manufacturer specification
- **Date checked:** 2026-08-28

---

### `LIFE-TANK-N006` — Tank/tankless service-life figures (8–12 yr tank,
15–20 / 20+ yr tankless, 12–15 yr "longest-lasting" brands)

- **Exact claims:** "Standard gas tank water heaters typically last 8–12
  years" / "Tankless gas units last 15–20 years" / "well-maintained units
  often reaching 12–15 years" / "lifespans of 20+ years"
- **Classification:** Technical / lifecycle
- **Status:** `Unverified`
- **Publication permission:** **Prohibited** on new or materially-rewritten
  content; existing occurrences are a known, flagged gap pending a
  dedicated remediation pass (see limitations below — same scoping
  Harrisburg applied to its own equivalent finding)
- **Source URL:** None directly fetched.
- **Exact supporting quotation:** None
- **Source type:** N/A
- **Affected paths/sections:** `index.html`, `services/gas-repair.html`, and
  likely other service pages carrying similar lifespan ranges (a full
  sitewide sweep for every occurrence was not completed as part of this
  registry's initial pass — treat any additional instance found later as
  covered by this same entry, not a new one)
- **Limitations/conditions:** These specific ranges are commonly repeated
  across the plumbing trade as rough industry consensus, but "commonly
  repeated" is explicitly not evidence per this registry's governing rule.
  A full sitewide remediation (replacing every instance with sourced or
  non-numeric language) is a larger task than this pass's scope — flagging
  it here rather than silently leaving it unaddressed.
- **Owner-confirmation record:** N/A
- **Review trigger:** A directly fetchable manufacturer or DOE service-life
  publication
- **Date checked:** 2026-08-28

---

### `BIZ-CLAIMS-N007` — Business-controlled operational claims

| Claim | Occurrences | Owner-confirmation record | Status |
|---|---|---|---|
| "Since 2019" | Homepage + About page stat bar | User confirmed in-session (entity-consistency task, this project) | **Owner-confirmed** |
| "9,000+ Water Heaters Serviced" | Homepage + About page stat bar | User confirmed in-session (entity-consistency task, this project) | **Owner-confirmed** |
| "60 min Avg. Response Time" | Homepage + About page stat bar | User confirmed in-session via `AskUserQuestion` (entity-consistency task, this project) | **Owner-confirmed** |
| "Licensed & Insured" | Stat bar + scattered trust-signal mentions sitewide | None found | `Unverified / Awaiting owner confirmation` |
| Same-day service / same-day availability | Widespread (hero, CTAs, trust signals) | None found | `Unverified / Awaiting owner confirmation` |
| "8 brands serviced" | Sidebar brand lists sitewide | Derived directly from the brand list itself (self-evidently correct by counting the list) — **not** a claim requiring external verification | Not applicable — internally consistent, not an external claim |

- **Classification:** Business-controlled
- **Publication permission:** `Owner-confirmed` claims may publish citing
  the record above. "Licensed & Insured" and same-day-service claims:
  existing sitewide occurrences left in place (removing them sitewide is a
  larger, separately-scoped decision the business owner should make, not
  something to silently strip during a content audit) — but no new page or
  materially-rewritten section should introduce a new instance beyond what
  already exists identically sitewide.
- **Owner-confirmation record:** "Since 2019," "9,000+," and "60 min" — see
  above. All three were supplied directly by the site owner in the prompt
  that requested the stat bar be added, and the response-time figure was
  confirmed via an explicit multiple-choice question rather than assumed.
- **Review trigger:** Written confirmation obtained for "Licensed &
  Insured" or same-day-service claims
- **Date checked:** 2026-08-28

---

### `PRICE-REPO-N008` — Service page and symptom page price ranges

- **Exact claim:** All dollar figures across the 14 service pages and 6
  symptom pages (e.g., "$150–$600" repair range, per-fuel installation cost
  tables)
- **Classification:** Price
- **Status:** `Repository-authoritative` (internal provenance tag, not an
  external verification status)
- **Publication permission:** Permitted as the business's own stated
  pricing, not as externally verified market data
- **Source URL:** N/A — the business's own service prices
- **Exact supporting quotation:** N/A
- **Source type:** Business-controlled (internal)
- **Affected paths/sections:** All 14 service pages, all 6 symptom pages
- **Limitations/conditions:** A given price range should read identically
  everywhere it's cited — if a future price change is made on the page
  that "owns" a figure, the same figure elsewhere must be updated in the
  same edit, not left to drift.
- **Owner-confirmation record:** None on file specifically for individual
  price ranges — same open item as `BIZ-CLAIMS-N007`'s unconfirmed rows
- **Review trigger:** Any price change on an owning page
- **Date checked:** 2026-08-28
