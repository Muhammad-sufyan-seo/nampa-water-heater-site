# Nampa Water Heater Pros — Site Audit Report

**Audit date:** 2026-08-27
**Site root:** `nampa-water-heater/`
**Reference model:** harrisburgwaterheater.com (structure only — all business facts replaced with Nampa, ID data)

---

## STEP 1 — INITIAL AUDIT (Before Fixes)

### Pages Found at Audit Start (11 total)

| Page | Path |
|---|---|
| Homepage | `index.html` |
| About | `about.html` |
| Contact | `contact.html` |
| Privacy Policy | `privacy-policy.html` |
| Terms of Service | `terms.html` |
| Water Heater Repair | `services/repair.html` |
| Water Heater Installation | `services/installation.html` |
| Water Heater Replacement | `services/replacement.html` |
| Downtown Nampa area page | `areas/downtown-nampa.html` |
| Central Nampa area page | `areas/central-nampa.html` |
| South Nampa area page | `areas/south-nampa.html` |

### ⚠️ Issues Found in Existing Pages

1. **Wrong phone number site-wide** — every page used `(208) 555-0123` / `+12085550123` (a placeholder number) instead of the required call-tracking number `(208) 987-5152` / `+12089875152`. Affected all 11 files, in visible text, `tel:` links, and `telephone` schema fields.
2. **All pages set to `noindex, follow`** — every single page had `<meta name="robots" content="noindex, follow">`, which would have kept the entire site out of Google's index.
3. **`robots.txt` blocked the entire site** — `Disallow: /` for all user-agents, contradicting any indexing effort.
4. **No `sitemap.xml`** existed.
5. **Navigation only referenced 3 service pages and 3 area pages** — no symptom pages, no areas hub, no way to reach the additional service pages required by the build spec.
6. **Mobile nav out of sync with desktop nav** on `index.html`, `contact.html`, and `services/repair.html` — a `<!-- [LEADSMART_TRACKING_NUMBER] -->` comment before the phone link broke a straightforward mobile-menu structure, so these three pages' mobile menus still showed the old 3-service/3-area structure.

### ✅ What Already Passed

- Single H1 per page, logical heading hierarchy, no skipped levels.
- Semantic HTML (`<main>`, `<article>`, `<section>`, `<nav>`, `<figure>`) used correctly throughout.
- `LocalBusiness`, `Service`, `FAQPage`, `BreadcrumbList`, and `WebPage` JSON-LD schema present and valid on relevant pages.
- **No fake street address anywhere** — schema used city/region/country only (`addressLocality`, `addressRegion`, `addressCountry`), with a proper Service Area block in the footer. This was correct from the start and preserved.
- **No reviews/testimonials section** anywhere on the site — confirmed absent, matching the reference model.
- All existing `<img>` tags had descriptive, keyword-relevant alt text.
- Existing pages were responsive with real breakpoints (1024px / 768px / 480px) and fluid typography (`clamp()`), no fixed pixel widths breaking mobile.

### ❌ Pages Missing (compared to the required 30-page list)

18 of 30 required pages did not exist:
- 11 service pages (gas/electric/heat-pump/tankless/commercial repair & installation, maintenance)
- 6 symptom pages (leaking, no hot water, noise, pilot light, rusty water, breaker tripping)
- 1 areas hub page (`areas/index.html`)

---

## STEP 2 — STRUCTURAL MODEL REPLICATION

All new pages were built using the **exact structural pattern** of the existing Nampa pages (which already mirror the Harrisburg reference model): sticky header with dropdown nav, breadcrumb bar, hero section with eyebrow/H1/lead/CTA/trust-signal row, two-column article + sidebar content layout, cost tables, FAQ schema, mid-page CTA banner, full footer with service-area block, and sticky mobile call bar. No reviews/testimonials section was added anywhere, consistent with the reference site.

Business-specific facts (name, phone, city, ZIPs, neighborhoods, housing narrative, brands) were confirmed as Nampa-specific throughout — see Step 5 verification below.

**Note on "Serving Since [Year]":** No founding year is hardcoded anywhere on the site. The homepage trust-signal row uses only verifiable claims (Licensed & Insured, Same-Day Availability, Serving All of Nampa, Upfront Pricing) rather than an invented "since [year]" or "X,XXX+ serviced" stat, since neither was confirmed. **Action needed from client:** supply the actual founding year and any real service-count statistic if you want a Harrisburg-style stat bar added.

---

## STEP 3 — PAGES BUILT

### ✅ Service Pages (14/14 required + 0/1 optional built)

**Repair (6/6):**
1. ✅ Water Heater Repair — `services/repair.html` (existing)
2. ✅ Gas Water Heater Repair — `services/gas-repair.html` (**new**)
3. ✅ Electric Water Heater Repair — `services/electric-repair.html` (**new**)
4. ✅ Heat Pump (Hybrid) Water Heater Repair — `services/heat-pump-repair.html` (**new**)
5. ✅ Tankless Water Heater Repair — `services/tankless-repair.html` (**new**)
6. ✅ Commercial Water Heater Repair — `services/commercial-repair.html` (**new**)

**Installation (6/6):**
7. ✅ Water Heater Installation — `services/installation.html` (existing)
8. ✅ Gas Water Heater Installation — `services/gas-installation.html` (**new**)
9. ✅ Electric Water Heater Installation — `services/electric-installation.html` (**new**)
10. ✅ Heat Pump (Hybrid) Water Heater Installation — `services/heat-pump-installation.html` (**new**)
11. ✅ Tankless Water Heater Installation — `services/tankless-installation.html` (**new**)
12. ✅ Commercial Water Heater Installation — `services/commercial-installation.html` (**new**)

**Other (2/2 required):**
13. ✅ Water Heater Replacement — `services/replacement.html` (existing)
14. ✅ Water Heater Maintenance — `services/maintenance.html` (**new**)
15. ⬜ *Electric Tankless Water Heaters* (optional, not built — flagged below for client decision)

### ✅ Symptom-Based Pages (6/6 required)

16. ✅ Water Heater Leaking — `symptoms/leaking.html` (**new**)
17. ✅ No Hot Water — `symptoms/no-hot-water.html` (**new**)
18. ✅ Water Heater Making Noise — `symptoms/noise.html` (**new**)
19. ✅ Pilot Light Won't Stay Lit — `symptoms/pilot-light.html` (**new**)
20. ✅ Rusty, Discolored, or Smelly Hot Water — `symptoms/rusty-water.html` (**new**)
21. ✅ Water Heater Breaker Keeps Tripping — `symptoms/breaker-tripping.html` (**new**)

Each symptom page includes: causes breakdown, safe homeowner diagnostic checks, a "when to call a pro" section, and a cost-context table, plus `FAQPage` + `Service` JSON-LD schema.

### ✅ Area Pages (3/3 required)

22. ✅ Downtown Nampa — `areas/downtown-nampa.html` (existing)
23. ✅ Central Nampa — `areas/central-nampa.html` (existing)
24. ✅ South Nampa — `areas/south-nampa.html` (existing)

### ✅ Core Pages (6/6 required)

25. ✅ Homepage — `index.html` (existing)
26. ✅ About Us — `about.html` (existing)
27. ✅ Contact — `contact.html` (existing)
28. ✅ Areas We Serve hub — `areas/index.html` (**new** — links to all 3 area pages, plus a full-text list of North Nampa, West Nampa, East Nampa, Franklin Road corridor, Karcher area, Sky Ranch, Southside Nampa, and adjacent unincorporated Canyon County for topical coverage)
29. ✅ Privacy Policy — `privacy-policy.html` (existing)
30. ✅ Terms of Service — `terms.html` (existing)

**Total: 29/30 required pages built (14 service + 6 symptom + 3 area + 1 hub + 6 core). The 30th item is the explicitly optional Electric Tankless page.**

---

## FIXES APPLIED

1. **Phone number corrected everywhere** — `(208) 555-0123` → `(208) 987-5152` and `+12085550123` → `+12089875152`, across all visible text, `tel:` links, and JSON-LD `telephone` fields, on all 11 pre-existing files.
2. **`noindex` removed from every page** — all `<meta name="robots">` tags changed from `noindex, follow` to `index, follow` (11 existing + 18 new = 29 pages).
3. **`robots.txt` fixed** — changed from blocking the entire site (`Disallow: /`) to `Allow: /` with a `Sitemap:` reference.
4. **`sitemap.xml` created** — lists all 29 live pages.
5. **Full site navigation rebuilt** — header dropdown, mobile nav, and footer link structure on every page now include all 14 service pages, all 6 symptom pages, the areas hub, and the 3 area pages (up from 3 services / 3 areas).
6. **Mobile nav desync fixed** on `index.html`, `contact.html`, and `services/repair.html` (the `LEADSMART_TRACKING_NUMBER` comment had broken the original mobile-menu markup for these three files specifically).
7. **Broken breadcrumb "Home" links fixed** — several new pages linked `href="../"` instead of `href="../index.html"`; corrected to explicit file paths across 17 pages.
8. **Heading ID mismatches fixed** — `aria-labelledby` on 5 installation-page `<article>` elements pointed to IDs that didn't exist due to a naming inconsistency (`-install-` vs `-installation-`); corrected so every ARIA reference resolves.

---

## AUDIT CHECKS PERFORMED (Automated)

| Check | Result |
|---|---|
| H1 count per page | ✅ Exactly 1 on all 29 pages |
| Heading hierarchy (no skipped levels) | ✅ Verified on spot-checked pages; h1→h2→h3→h4 throughout |
| JSON-LD schema syntax validity | ✅ All 83 JSON-LD blocks across the site parse as valid JSON |
| Internal link integrity | ✅ 0 broken internal links after fixes (was 17 before fix) |
| Phone number consistency | ✅ `(208) 987-5152` present on all 29 pages, no stray old number remains |
| Fake street address check | ✅ None found — schema uses `addressLocality`/`addressRegion`/`addressCountry` only |
| Reviews/testimonials check | ✅ None found (2 false-positive text matches were "review their privacy policies" and "code compliance review" — not customer reviews) |
| "Harrisburg" leftover text check | ✅ None found anywhere in the codebase |
| Brand name consistency | ✅ "Nampa Water Heater Pros" present on all 29 pages |
| Image alt text | ✅ All existing `<img>` tags have descriptive, location/keyword-relevant alt text |
| Mobile nav / desktop nav parity | ✅ All 29 pages now have matching 6-section nav structure |

---

## ⚠️ OPEN ITEMS FOR CLIENT / FUTURE DECISION

1. **Tailwind CSS vs. custom CSS** — the reference build brief calls for "Tailwind CSS used, no framework leftovers." The site actually uses a hand-written custom CSS file (`assets/css/style.css`, ~1,480 lines) with its own design tokens (Industrial Craft / Pacific Northwest Trade palette), not the Tailwind utility-class framework. The custom CSS **is** fully responsive (breakpoints at 1024/768/480px, fluid `clamp()` typography) and already extended consistently to all 29 pages. Rewriting the entire site's styling system to Tailwind is a large, separate undertaking that risks breaking the working, cohesive design — **flagging this rather than doing it unprompted.** Let us know if you want a Tailwind migration as a follow-up project.
2. ~~"Serving Since [Year]" / stat bar~~ — **RESOLVED.** Client provided canonical values (2019 founding year, 9,000+ serviced, 60 min avg. response time); stat bar is now live on homepage + About page. See "Entity Consistency Audit" section below.
3. ~~Social profile placeholders~~ — **RESOLVED.** The `sameAs` array (which held `PLACEHOLDER_FACEBOOK_URL` / `PLACEHOLDER_GOOGLE_BUSINESS_URL`) has been removed entirely from the Organization schema, with a `TODO` HTML comment left above the schema block for whoever adds real profile URLs later.
4. **Hero/content images** — several pages carry `<!-- PLACEHOLDER - CLIENT TO REPLACE -->` comments around stock Unsplash imagery (used with descriptive alt text as a placeholder). Recommend replacing with real jobsite photos before launch.
5. **Optional page not built** — "Electric Tankless Water Heaters in Nampa, ID" (item 15, explicitly optional in the brief) was not built. Can be added on request.

---

## STEP 5 — FINAL QA PASS

**Verified 2026-08-27 16:36 UTC**

- ✅ All 29 built pages exist and are reachable from header nav, mobile nav, and footer nav (verified via link-crawl script — 0 broken internal links).
- ✅ No broken internal links anywhere on the site (automated crawl of all `href` attributes across all 29 HTML files).
- ✅ No fake address anywhere — visible HTML or schema (spot-checked and grepped for `streetAddress`, none found).
- ✅ No reviews/testimonials section anywhere (grepped whole site; only false-positive text unrelated to customer reviews).
- ✅ Phone number `(208) 987-5152` / `+12089875152` consistent across every page: header CTA, mobile tap-to-call, footer, sticky call bar, contact page, and every `telephone` schema field.
- ✅ Brand name "Nampa Water Heater Pros" consistent on every page; zero leftover "Harrisburg" references anywhere in the repository.
- ✅ All 83 JSON-LD schema blocks across the site are syntactically valid JSON (`LocalBusiness`, `Service`, `FAQPage`, `BreadcrumbList`, `WebPage` types all present where applicable).
- ✅ `robots.txt` allows crawling and references `sitemap.xml`; all pages set to `index, follow`.

### Summary

- **14/14 service pages built** (11 new + 3 pre-existing)
- **6/6 symptom pages built** (all new)
- **3/3 area pages + 1/1 hub page built** (hub new, area pages pre-existing)
- **6/6 core pages present** (all pre-existing)
- **29/30 total required pages live** (1 optional page intentionally not built — see open items)
- **7 categories of issues found and fixed** in the pre-existing 11 pages (phone number, noindex, robots.txt, nav gaps, mobile nav desync, broken breadcrumb links, heading ID mismatches)
- **0 unresolved ⚠️ items** from the Step 1 audit — all fixed prior to Step 2/3 build work, per instructions
- **3 open items** flagged for client decision (Tailwind migration, stat-bar data, social placeholder URLs) — none block launch, none are rule violations, all require information only the client can provide

---

## ENTITY CONSISTENCY AUDIT

**Audit date:** 2026-08-27 (second pass)

Google and AI-driven search increasingly evaluate local-business trustworthiness by checking whether core identity facts are byte-for-byte identical everywhere they appear. This pass locked seven canonical fields and searched the entire codebase for any deviation.

### Canonical Values Locked

| Field | Canonical Value |
|---|---|
| Business/Brand Name | `Nampa Water Heater Pros` |
| Phone Number | `(208) 987-5152` (visible) / `tel:+12089875152` (href) |
| Domain | `nampawaterheater.com` (non-www, already the sole form in use) |
| Founding Year | `2019` |
| Service Stat | `9,000+ Water Heaters Serviced` |
| Primary Service Area Wording | `Serving Nampa, ID and surrounding areas — 83651, 83686, 83687` |
| Address Format (service area, not physical) | `[Neighborhood], Nampa, Idaho, [Zip], United States` |

### Search Method

Grepped every `.html` file for: all spacing/spelling variants of the business name; every phone-number format (parenthesized, hyphenated, digits-only, `tel:` href); every `nampawaterheater.com` reference (checked for stray `www.` or `http://` variants — none existed); every "since"/"founded"/"foundingDate" mention; every water-heaters-serviced stat; every "serving Nampa" / zip-code sentence; and the `@id` value on every `LocalBusiness` schema block.

### Findings — 8 Inconsistencies Found and Fixed

| # | Inconsistency | Where | Fix |
|---|---|---|---|
| 1 | `"Primary Target Zip Codes"` vs. `"Primary Zip Codes"` (two different labels for the same fact) | `about.html`, `contact.html`, `index.html` (3 files) — vs. 24 other files using the shorter label | Normalized all 3 stragglers to `"Primary Zip Codes"` |
| 2 | Service-area sentence used `·` (middle-dot) separators and no "and surrounding areas" phrase: `"Serving Nampa, ID 83651 · 83686 · 83687"` | Footer copyright line (all 29 pages), homepage trust bar, `privacy-policy.html`, `terms.html` | Replaced everywhere with the canonical `"Serving Nampa, ID and surrounding areas — 83651, 83686, 83687"` (32 total occurrences fixed) |
| 3 | `LocalBusiness` schema `@id` was `#business` on the homepage and **absent entirely** on the other 23 pages carrying `LocalBusiness` schema (as `Service.provider` or standalone) | `index.html` + 23 other files | Renamed to `#organization` and added the identical `"@id": "https://nampawaterheater.com/#organization"` to all 24 `LocalBusiness` blocks, so every page's business schema resolves to the same entity |
| 4 | Two lingering `@id` references still pointed at the old `#business` fragment after the rename | `about.html` (`AboutPage.about`), `contact.html` (`ContactPage.about`, presumed similarly) | Updated both to `#organization` |
| 5 | No `foundingDate` in schema anywhere | `index.html` Organization block | Added `"foundingDate": "2019"` |
| 6 | Placeholder `sameAs` URLs (`PLACEHOLDER_FACEBOOK_URL`, `PLACEHOLDER_GOOGLE_BUSINESS_URL`) — a fake/broken link is itself a trust-signal risk | `index.html` | Removed the `sameAs` array entirely; added `<!-- TODO: add sameAs social profile URLs once provided (Facebook, Google Business Profile) -->` directly above the schema `<script>` block |
| 7 | No service-area citation string in the canonical `[Neighborhood], Nampa, Idaho, [Zip], United States` format anywhere | All 3 area pages | Added `Service Area: Downtown Nampa, Nampa, Idaho, 83651, United States` (and the Central/South equivalents) to each area page's "Area Details" sidebar card |
| 8 | Stale numeric fact: About page's stat row claimed **"7 Major Brands Serviced"** while the brand list used in every service-page sidebar has **8** brands (Rheem, A.O. Smith, Bradford White, American Standard, Navien, Rinnai, Noritz, State Water Heaters) | `about.html` | Corrected the stat to `8` |

### Confirmed Already Consistent (no fix needed)

- Business name spelling/spacing: 323 occurrences, zero variants.
- Phone number format: 306 visible occurrences of `(208) 987-5152` + 187 `tel:+12089875152` hrefs, zero variants (no missing space, no hyphenated form, no stray digit).
- Domain: 143 occurrences of `https://nampawaterheater.com`, zero `www.` or alternate-protocol variants.

---

## STAT BAR IMPLEMENTATION

Added a `.stat-bar` component (new CSS in `assets/css/style.css`, "STAT BAR" section) to the dark-navy hero background used by both `index.html` and `about.html`:

**`Since 2019 | 9,000+ Water Heaters Serviced | 60 min Avg. Response Time | Licensed & Insured`**

The exact wording is identical, word-for-word, on both pages (verified via grep — see Post-Cleanup Verification below). The "60 min Avg. Response Time" figure was confirmed directly with the client rather than invented, since a precise, unverifiable response-time claim would itself have been a trust-signal risk.

---

## CODEBASE CLEANUP SUMMARY

### HTML
- Removed 5 leftover `<!-- [LEADSMART_TRACKING_NUMBER] -->` build-artifact comments (a call-tracking placeholder from the original scaffolding tool that never got wired up and served no function) from `index.html`, `contact.html`, `services/repair.html`.
- Removed one genuinely unused `id="repair-breadcrumb"` attribute (orphaned, no CSS/JS/ARIA reference) from `services/repair.html`.
- Removed a duplicate `BreadcrumbList` JSON-LD block on `areas/index.html` (a bug introduced by the hub-page build script layering its own breadcrumb schema on top of one already produced by the shared header helper).
- Spot-checked "redundant wrapper `<div>`" candidates flagged by an automated scan — all were legitimate two-column icon+text-block layout containers required by the surrounding flex/grid CSS, not actually redundant; none removed.
- Re-verified: single H1 and correct heading hierarchy on all 29 pages, semantic tags (`<main>`, `<article>`, `<section>`, `<nav>`) intact.

### CSS
- Removed one fully dead selector, `.btn-dark` (defined but referenced by zero HTML files).
- Fixed three real bugs found by cross-referencing every HTML `class=` attribute against CSS: `content-sidebar` (used on all 17 new service/symptom pages) had no CSS rule at all — renamed to the already-styled `.sidebar` class used by the original pages, restoring the intended sticky-sidebar behavior. `cost-table` (used on 15 pages) had no CSS rule — added a full `.cost-table` block (header styling, zebra-striped rows, mobile horizontal-scroll fallback) matching the site's existing design tokens. `area-cards-grid` (used on the new areas hub page) had no CSS rule — renamed to the existing `.areas-grid` class already used (and already responsive) on the homepage.
- Added a new "STAT BAR" section, formatted consistently with the file's existing section-comment style (`/* ===... TITLE ...=== */`).
- Confirmed zero duplicate top-level selector definitions.
- Confirmed mobile → tablet → desktop scaling still works after all edits (1024px / 768px / 480px breakpoints all still present and correctly targeting the classes used).

### JavaScript
- Audited `assets/js/main.js` (71 lines): no `console.log`/`debugger` statements, no duplicate event listeners, no unused functions. Vanilla JS, already minimal. No changes needed.

### Build Scripts
Moved into a new `/scripts/` folder at the **repo root** (a sibling of `nampa-water-heater/`, so it stays outside the Cloudflare Pages build/deploy root and is never served):
`update_nav.py`, `build_pages.py`, `build_symptoms.py`, `build_areas_hub.py`, `build_sitemap.py`, `check_links.py`, `validate_schema.py`, `fix_mobile_nav.py`.

Two of these (`build_areas_hub.py`, `build_symptoms.py`) imported shared code via a hardcoded path into this session's temporary scratchpad directory — that would have broken the moment the session ended. Fixed both to resolve the import relative to the script's own file location (`os.path.dirname(os.path.abspath(__file__))`) so they work standalone from the repo. All 8 scripts were re-verified to compile and run correctly from their new location.

**Important caveat documented directly in the scripts:** `build_pages.py`, `build_symptoms.py`, `build_areas_hub.py`, and `update_nav.py` are snapshot/scaffolding generators. Re-running them would regenerate their target pages from the original templates, **overwriting** the entity-consistency fixes, stat bar, and CSS-class corrections made directly to the HTML in this pass. Each now carries an explicit warning comment to this effect. `check_links.py`, `validate_schema.py`, `build_sitemap.py`, and `fix_mobile_nav.py` remain safe to re-run at any time (read-only or idempotent).

---

## POST-CLEANUP + ENTITY CONSISTENCY VERIFICATION

**Verified 2026-08-27 (second pass, after cleanup)**

| Check | Result |
|---|---|
| `check_links.py` (run from `/scripts/`) | ✅ Zero broken internal links |
| `validate_schema.py` (run from `/scripts/`) | ✅ All 82 JSON-LD blocks valid JSON (83 → 82 after removing the duplicate BreadcrumbList on the areas hub page) |
| H1 count per page | ✅ Exactly 1 on all 29 pages |
| Mobile nav consistency | ✅ All 29 pages carry exactly 6 `mobile-nav-section` groups |
| Phone number | ✅ `(208) 987-5152` — 306 visible + 187 `tel:+12089875152` hrefs, zero format variants anywhere |
| Business name | ✅ `Nampa Water Heater Pros` — 323 occurrences, zero spelling/spacing variants |
| Domain | ✅ `https://nampawaterheater.com` — 143 occurrences, zero `www.`/protocol variants |
| Schema `@id` | ✅ `https://nampawaterheater.com/#organization` present on all 24 `LocalBusiness` blocks plus all 2 cross-references (`about.html`, `contact.html`) — one stable entity across the whole site |
| Stat bar | ✅ `Since 2019`, `9,000+ Water Heaters Serviced`, `60 min Avg. Response Time` — identical wording on both `index.html` and `about.html` |
| `noindex` tags | ✅ None remaining anywhere |
| `robots.txt` | ✅ `Allow: /` + `Sitemap:` reference |
| `sitemap.xml` | ✅ 29 `<loc>` entries, matching the 29 live `.html` files exactly |
| Unused CSS | ✅ Zero dead selectors after removing `.btn-dark` |
| Undefined HTML classes | ✅ Zero (after fixing `content-sidebar`, `cost-table`, `area-cards-grid`); remaining 2 flagged candidates (`menu-icon`, `service-area`) confirmed as a JS hook and an inline-styled element respectively — not bugs |
| JS console/debug statements | ✅ None found |
| Build scripts | ✅ Relocated to `/scripts/`, all 8 compile and run correctly from the new location, portability bug (hardcoded scratchpad import path) fixed in 2 scripts |

**Result: the site is fully entity-consistent, cleaned up, and ready to merge to `main` for Cloudflare Pages deployment.**

---

## PHONE NUMBER FULL-SITE AUDIT

**Audit date:** 2026-08-27 (third pass)

Following the entity-consistency work, this pass specifically re-swept the entire codebase for any wrong or leftover phone number in any format, and enforced click-to-call correctness on every phone link.

### Search Method

Scanned all 33 files under `nampa-water-heater/` with an `.html`, `.js`, `.json`, `.xml`, `.txt`, or `.css` extension for: the original placeholder `(208) 555-0123` in every format (spaced, hyphenated, digits-only, `tel:` href); the Harrisburg reference number `(717) 470-0340` in every format; any `(208)` number that isn't `987-5152`; every `tel:` href value; every schema JSON-LD `telephone` field; `alt` text on images; meta tags (description, Open Graph); and every `<a>` tag carrying a "Call"-style `aria-label` or the phone SVG icon, to confirm none were missing their `href`.

### Findings

| # | Item | Where | Status |
|---|---|---|---|
| 1 | Original placeholder `(208) 555-0123` / `+12085550123` in any format | Whole codebase | ✅ Zero instances — already fully fixed in the prior audit pass, confirmed still holding |
| 2 | Harrisburg reference number `(717) 470-0340` in any format | Whole codebase | ✅ Zero instances — never leaked into this build |
| 3 | Any other `(208)` number besides `987-5152` | Whole codebase | ✅ Zero instances, with one reviewed non-issue: `contact.html:194` has `placeholder="(208) 555-0000"` on the contact form's `<input type="tel">` field. This is the visitor's own phone-number input, not a business-number reference — `555-0100`/`555-0000` is the standard NANP-reserved "fictional number" convention for form-field examples (the same role `jane@example.com` plays for the email field next to it). Confirmed correct, not changed. |
| 4 | `tel:` href format consistency | All 29 pages, 187 links | ✅ All 187 were already exactly `tel:+12089875152` — zero variants, zero missing `+1`, zero stray spaces/dashes inside the href |
| 5 | Schema JSON-LD `telephone` field format | 24 files with `LocalBusiness` schema | ⚠️ **Found and fixed**: all 24 used the visible format `"(208) 987-5152"` instead of the required international-dash format. Updated to `"+1-208-987-5152"` in all 24. |
| 6 | `<a>` tags with a Call-style `aria-label` missing `href="tel:..."` | All 29 pages | ✅ Zero found |
| 7 | `<a>` tags wrapping the phone SVG icon missing `href="tel:..."` | All 29 pages (141 phone-icon instances) | ✅ Zero found |
| 8 | `alt` text mentioning a phone number | All images site-wide | ✅ None found (no image alt text references a phone number at all) |
| 9 | Open Graph tags | Whole codebase | ℹ️ No `og:*` meta tags exist anywhere on the site (not introduced by this or prior passes) — nothing to check here; flagging as a separate potential future enhancement, out of scope for this phone-number task |
| 10 | JS click interception on `tel:` links | `assets/js/main.js` | ✅ Reviewed the full 71-line file: the only `click` listeners are on the mobile-menu toggle button, the FAQ accordion buttons, and `a[href^="#"]` anchors for smooth-scroll (which explicitly cannot match `tel:` hrefs since they require a leading `#`). No `preventDefault()`, no interception of any kind touches phone links. |

### Verification Script

Added `scripts/check_phone.py` (new; complements `check_links.py` and `validate_schema.py`). It:
1. Scans every file for the old-number patterns and confirms zero matches (excluding the confirmed-correct form placeholder).
2. Confirms every `tel:` href equals exactly `tel:+12089875152`.
3. Confirms every schema `telephone` field equals exactly `+1-208-987-5152`.
4. Confirms every `<a>` tag with a Call-style `aria-label` or the phone icon has a `tel:` href.
5. Reports total counts and a final PASS/FAIL verdict.

---

## PHONE NUMBER VERIFICATION — PASSED

**Verified 2026-08-27 (`scripts/check_phone.py` output)**

- **Files scanned:** 33 (`.html`, `.js`, `.json`, `.xml`, `.txt`, `.css` under `nampa-water-heater/`)
- **Old/wrong phone number instances found:** 0
- **Old/wrong phone number instances fixed:** 0 (none remained — the prior audit's fix held completely)
- **Schema `telephone` field format issues found and fixed:** 24 (all converted from `(208) 987-5152` to `+1-208-987-5152`)
- **Total clickable `tel:` links verified across the site:** 187, all exactly `href="tel:+12089875152"`
- **Total phone-icon `<a>` elements checked for missing `href`:** 141, zero missing
- **Total Call-labeled `<a>` elements checked for missing `href`:** all, zero missing
- **JS click-interception check:** passed — no script touches or blocks `tel:` link behavior

**Zero instances of any incorrect phone number remain anywhere on the site.** Every visible phone number reads exactly `(208) 987-5152`. Every clickable phone link uses `href="tel:+12089875152"` and will trigger native click-to-call on mobile with no JavaScript in the way. Every schema `telephone` field now uses the `+1-208-987-5152` international-dash format.

---

## DIRECTORY FLATTENING — MOVED TO ROOT

**Change date:** 2026-08-28

The site previously lived inside a `nampa-water-heater/` subfolder at the repo root, which was causing Cloudflare Pages deployment issues (Pages expects the site's `index.html` and assets at the configured build-output root, not nested one level deeper than necessary). This pass flattened the structure.

### What Moved

Every file and folder from inside `nampa-water-heater/` was moved to the repository root via `git mv` (preserving file history):

- `index.html`, `about.html`, `contact.html`, `privacy-policy.html`, `terms.html`, `sitemap.xml`, `robots.txt` — moved to root
- `services/`, `areas/`, `symptoms/`, `assets/` (including `assets/css/` and `assets/js/`) — moved to root as whole subtrees, contents unchanged

The now-empty `nampa-water-heater/` directory was then removed with `rmdir`. `scripts/` and `AUDIT-REPORT.md` were already at the root and were not touched.

### Path Verification — No Broken Paths

Because the entire site subtree moved as a single unit (every page and its assets shifted up by exactly one directory level together), **all relative paths between pages and assets remained correct with zero edits needed**:
- Root-level pages (`index.html`, `about.html`, etc.) already referenced `assets/css/style.css` and `assets/js/main.js` with no `../` prefix — still correct, since `assets/` is now also at root.
- One-level-deep pages (`services/*.html`, `areas/*.html`, `symptoms/*.html`) already referenced `../assets/...` and `../index.html` — still correct, since those pages are still exactly one level below the new root.
- **Canonical tags, schema `url`/`@id` fields, `sitemap.xml`, and `robots.txt`** were already using absolute URLs (`https://nampawaterheater.com/...`) that matched the site's intended final root-relative structure — these were never dependent on the physical `nampa-water-heater/` folder name and needed no changes. Spot-checked one page per directory depth (root, `services/`, `areas/`, `symptoms/`) to confirm.

### Real Bug Found and Fixed: Verification Scripts

The 7 build/audit scripts in `scripts/` (`build_pages.py`, `build_sitemap.py`, `check_links.py`, `check_phone.py`, `fix_mobile_nav.py`, `update_nav.py`, `validate_schema.py`) all hardcoded `BASE = "/home/user/nampa-water-heater-site/nampa-water-heater"` — pointing at the now-deleted subfolder. Updated all 7 to `BASE = "/home/user/nampa-water-heater-site"` (the new repo root).

This surfaced a second, related bug: with `BASE` now set to the actual repo root, `os.walk(BASE)` in `check_links.py`, `validate_schema.py`, `build_sitemap.py`, `update_nav.py`, and `check_phone.py` would additionally descend into `.git/` (thousands of internal git objects) and `scripts/` (irrelevant `.py` files) on every run — harmless to correctness (both only match `.html`/`.js`/etc. by extension) but wasteful, and a latent risk if the repo ever grows a build tool that drops matching-extension files inside `.git/hooks` or similar. Fixed all 5 affected scripts to prune `.git` and `scripts` from the walk via `dirs[:] = [d for d in dirs if d not in (...)]`, in addition to the existing `assets` exclusion where applicable.

### Verification After Flatten

| Check | Result |
|---|---|
| `scripts/check_links.py` | ✅ 0 broken internal links (runs in ~0.02s, confirming `.git` is now properly pruned) |
| `scripts/validate_schema.py` | ✅ All 82 JSON-LD blocks still valid |
| `scripts/check_phone.py` | ✅ Full PASS — 187/187 `tel:` links correct, 24/24 schema `telephone` fields correct, 0 old numbers |
| H1 count per page | ✅ Exactly 1 on all 29 pages, confirmed intact after the move |
| File count vs. sitemap | ✅ 29 `.html` files on disk, 29 `<loc>` entries in `sitemap.xml` — exact match |
| `robots.txt` | ✅ Unchanged, still `Allow: /` with correct `Sitemap:` reference |
| All scripts compile | ✅ All 9 files in `scripts/` (8 original + `check_phone.py`) pass `python3 -m py_compile` after the `BASE` path update |

**Confirmed: `nampa-water-heater/` subfolder no longer exists. All website files (HTML, CSS, JS, images referenced by path, `sitemap.xml`, `robots.txt`) live directly at the repository root. `scripts/` and `AUDIT-REPORT.md` remain at root, unaffected by the move. Every verification script passes.**

---

## CLOUDFLARE WORKERS CONFIG (`wrangler.jsonc`) — INSPECTED AND FIXED

**Change date:** 2026-08-28

### Where the Config Actually Lived

`main` had no `wrangler.toml` or `wrangler.jsonc` at all. Cloudflare's GitHub App had auto-generated one on a separate, never-merged branch — `cloudflare/workers-autoconfig` (commit `236f9a1`, authored by the `cloudflare-workers-and-pages[bot]`) — created *before* the directory-flatten work, so it still pointed at the old subfolder. Brought `wrangler.jsonc` and the companion `.gitignore` from that branch onto `main` via `git checkout origin/cloudflare/workers-autoconfig -- wrangler.jsonc .gitignore`, then fixed it in place.

### BEFORE

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "nampa-water-heater-site",
  "compatibility_date": "2026-07-21",
  "observability": {
    "enabled": true
  },
  "assets": {
    "directory": "nampa-water-heater"
  },
  "compatibility_flags": [
    "nodejs_compat"
  ]
}
```

### AFTER

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "nampa-water-heater-site",
  "compatibility_date": "2026-07-21",
  "observability": {
    "enabled": true
  },
  "assets": {
    "directory": "./"
  },
  "compatibility_flags": [
    "nodejs_compat"
  ]
}
```

Only the `assets.directory` value changed. Other fields checked and confirmed already correct:
- `name`: `"nampa-water-heater-site"` ✅ matches the repo name
- `compatibility_date`: `"2026-07-21"` ✅ present and recent (about 5 weeks old at time of this audit)
- No other field referenced the old `nampa-water-heater/` subfolder path

### Real Bug Found During Dry-Run Validation: Missing `.assetsignore`

Ran `npx wrangler deploy --dry-run` (wrangler auto-installed via `npx`, v4.127.0) — it resolved with no config errors both before and after the fix. But the dry-run's own output ("✨ Read 418 files from the assets directory") was suspiciously high for a 45-file site, which led to checking exactly what `directory: "./"` would sweep up. Confirmed by reading wrangler's own source (`createAssetsIgnoreFunction`) that its **default** ignore list only excludes `.assetsignore` itself, `_redirects`, and `_headers` — nothing else. Without an explicit `.assetsignore` file, deploying with `directory: "./"` would have published `.git/` (full commit history and objects), `.wrangler/` (local build cache), `scripts/` (internal Python dev tooling), `AUDIT-REPORT.md`, and `wrangler.jsonc` itself as publicly-served static assets alongside the real site.

Added `.assetsignore` (same pattern syntax as `.gitignore`, confirmed via wrangler's source — it uses the same `ignore` matching library) excluding: `.git`, `.wrangler`, `.gitignore`, `wrangler.jsonc`, `scripts`, `AUDIT-REPORT.md`, `node_modules`.

**Verified the fix actually works**, not just that the file exists: re-ran the dry-run with `WRANGLER_LOG=debug` (the correct verbosity env var — `--log-level` is not a valid flag on this wrangler version) and confirmed every excluded path is logged as `Ignoring asset: ...` during manifest construction — `.git/` (all ~250 internal objects/refs/logs), `.wrangler/`, `scripts/` (all 9 `.py` files), `AUDIT-REPORT.md`, and `wrangler.jsonc` were all correctly excluded from the upload manifest. Note: the "Read N files" summary line always reports the *raw pre-filter* directory scan count by design (confirmed in wrangler's source — the ignore function runs after that log line), so that number staying high is expected and not a sign the ignore file isn't working.

### Dry-Run Result

```
✨ Read 418 files from the assets directory /home/user/nampa-water-heater-site
Total Upload: 0.35 KiB / gzip: 0.25 KiB
No bindings found.
--dry-run: exiting now.
```

✅ Config resolves without errors. No deploy was performed (dry-run only, per instructions).

### Verification Summary

| Check | Result |
|---|---|
| `wrangler.jsonc` exists on `main` | ✅ (brought over from the `cloudflare/workers-autoconfig` bot branch, was previously unmerged) |
| `assets.directory` | ✅ Fixed: `"nampa-water-heater"` → `"./"` |
| `name` field | ✅ Already correct: `"nampa-water-heater-site"` |
| `compatibility_date` | ✅ Already present and recent: `"2026-07-21"` |
| Other stale path references | ✅ None found |
| `npx wrangler deploy --dry-run` | ✅ Resolves with no errors |
| `.assetsignore` excludes dev/VCS files from the public deploy | ✅ Added and verified via debug-log manifest inspection — `.git`, `.wrangler`, `scripts/`, `AUDIT-REPORT.md`, `wrangler.jsonc` all correctly excluded |

**`wrangler.jsonc` now correctly serves the flattened site from the repository root, without exposing git internals or dev tooling as public static assets.**
