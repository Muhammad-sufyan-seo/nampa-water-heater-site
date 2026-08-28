# NAMPAWATERHEATER.COM — CONTENT & SEO RULES

Adapted from the Harrisburg Water Heater Pros master build file
(`harrisburg-water-heater` repo, `CLAUDE.md`), which itself cites Koray Tuğberk
Gübür's semantic SEO methodology and Bill Slawski's patent-informed heading
rules. This is not a straight copy — Harrisburg's site is a larger, phased
46-page build; Nampa's is a fixed, already-built 29-page site. Sections below
are rewritten to match what actually exists here, and every Harrisburg-specific
fact (city, phone, stat, brand list, zip codes, competitor names) has been
replaced with the corresponding Nampa fact or explicitly flagged as unresearched
rather than invented.

**Read "Factual Integrity and Source Verification" (§9) before writing or
editing any factual, numeric, comparative, technical, safety, or business
claim.** It governs every other section of this file.

---

## 1. WHAT THIS SITE IS AND HOW TO WRITE IT

**nampawaterheater.com / "Nampa Water Heater Pros"** is a professional water
heater service website for Nampa, Idaho. Write every word exactly as a real,
established, locally-trusted Nampa water heater company would write its own
website.

**This site is exclusively about Nampa, ID and its immediate service area.**
Every page, every sentence, every local reference is Nampa — not Boise
broadly, not the wider Treasure Valley as the primary subject, not any other
city. Downtown Nampa, Central Nampa, South Nampa — these are the communities
this business serves, with ZIP codes 83651, 83686, and 83687.

**Voice and positioning:**
- First person plural: "we service," "our technicians," "we've seen this in
  Nampa's older Downtown homes."
- Confident, locally specific, demonstrated expertise — never
  corporate-generic, never AI-template vague.
- Trust earned through local knowledge: Nampa's hard water and its effect on
  sediment/scale, the age split between Downtown/Central's older housing stock
  and South Nampa's newer construction near Lake Lowell, Idaho's seismic
  strapping code requirement.
- Expertise shown through precise technical detail and exact numbers — a real
  plumber talks in specifics, not vague reassurance.

**Hard build rules — hard failure if violated:**
- Zero meta-disclosure language. Zero "referral platform" or "advertising
  network" wording. A real plumber's site never explains its business model.
- Zero forms as the only conversion action — phone call is primary; the
  contact form (already built) is a secondary channel, not a replacement.
- Zero fabricated license numbers, staff names, or specific credentials not
  confirmed by the business owner.
- Zero fake street address in content or schema — service area + zip codes
  only. (Confirmed clean sitewide as of the 2026-08-27 entity-consistency
  audit — see `AUDIT-REPORT.md`.)
- **PERMANENT, LOCKED DECISION: this site does not and will not display
  testimonials, review counts, or star ratings anywhere, in any phase, ever.**
  No placeholder, no "X+ Reviews" claim, no invented review count. If a future
  task asks for a reviews/testimonials section, flag the conflict with this
  rule rather than adding one. (Mirrors the identical locked decision on the
  Harrisburg reference site — this is a house-wide policy, not
  Nampa-specific.)
- Phone: `(208) 987-5152` printed on every call button, `tel:+12089875152` in
  every href, `+1-208-987-5152` in every schema `telephone` field. One format
  per context, chosen once, never varied — see the Entity Consistency Audit in
  `AUDIT-REPORT.md` for the full verification trail.

**Service area footer block (every page — already implemented, keep this
exact pattern):**
```html
<div class="service-area-block">
  <h3>Our Nampa Service Area</h3>
  <p>We provide rapid water heater repair, replacement, and tankless
  installations throughout Nampa, ID, including Downtown, Central Nampa,
  South Nampa, and surrounding communities. <strong>Primary Zip Codes: 83651,
  83686, 83687.</strong></p>
</div>
```

---

## 2. TECH STACK

- **Custom CSS only — no Tailwind CSS, no framework CSS.** This matches the
  Harrisburg reference site's identical rule. The site's custom
  `assets/css/style.css` (~1,480 lines) already implements this correctly —
  do not introduce Tailwind or any other CSS framework. (This was flagged as
  an open question in the very first audit pass and resolved by direct
  confirmation against the Harrisburg reference: custom CSS is the house
  standard, not a deviation.)
- Static HTML5 only — no React, no Next.js, no build framework.
- Mobile-first, fully responsive — verified breakpoints at 1024px / 768px /
  480px.
- Root-relative flat URL structure (`.html` files, not folder+index) — this
  differs from Harrisburg's clean-URL folder pattern, which is a Cloudflare
  Pages convention Nampa's Cloudflare Workers + static-assets deployment does
  not require. Do not convert to folder URLs without a corresponding redirect
  plan; it would break every existing external link and the sitemap.
- `<meta name="robots" content="index, follow">` on every page — the site
  was flipped from `noindex` in the first audit pass (2026-08-27). Any new
  page must ship with `index, follow` to match current site state.
- Git repo already initialized. Commit after each meaningful unit of work with
  a message describing what changed and why.

---

## 3. VISUAL DESIGN (already implemented — reference only, do not redesign)

The site's existing design system ("Industrial Craft / Pacific Northwest
Trade" palette) is complete and consistent across all 29 pages. Do not
introduce a new palette, font pairing, or component system without an
explicit design task. For reference, the live tokens (`assets/css/style.css`
`:root`):

- Navy `#1B2A3B`, Ember (accent/CTA) `#E8500A`, Ember-dark `#C44208`, Slate
  `#4A5568`, Cream `#F7F4EF`, Light-warm `#EDE9E3`, Steel `#8B9BAA`.
- Headings: Oswald. Body: Source Serif 4. Utility/mono: Roboto Mono.
- Sticky header, dark-navy hero with ember bottom border, `.stat-bar`
  component (Since 2019 | 9,000+ Water Heaters Serviced | 60 min Avg.
  Response Time | Licensed & Insured — homepage + About page only).
- CTA rule: ember accent color appears ONLY on call buttons and
  emergency-urgency elements — do not introduce it elsewhere.

---

## 4. SITE ARCHITECTURE (as-built — 29 pages, no phased expansion plan)

Unlike the Harrisburg reference site's 4-phase, ~46-page geographic expansion
plan, Nampa's site was built to a fixed, complete 29-page structure in a
single pass. There is no "Phase 2/3/4" backlog of unbuilt pages for this
site — treat any future page additions as a new, separately-scoped task, not
an assumed continuation of a Harrisburg-style rollout.

**Core (6):** Homepage, About, Contact, Areas We Serve (hub), Privacy Policy,
Terms of Service.

**Service pages — money pages (14):** Repair × {general, gas, electric, heat
pump, tankless, commercial} (6) + Installation × {same 6 fuel types} (6) +
Replacement + Maintenance (2).

**Symptom pages (6):** Leaking, No Hot Water, Making Noise, Pilot Light Won't
Stay Lit, Rusty/Discolored/Smelly Water, Breaker Tripping.

**Area pages (3):** Downtown Nampa (83651, older housing, repair angle),
Central Nampa (83651, established residential, repair/replacement angle),
South Nampa (83686, newer/luxury near Lake Lowell, installation/tankless
angle).

An optional 30th page — "Electric Tankless Water Heaters in Nampa, ID" — was
scoped but deliberately not built (see `AUDIT-REPORT.md`). Build it only if
requested; it is not an assumed backlog item.

---

## 5. ANTI-CANNIBALIZATION

- One macro context per page. Two pages with the same intent = fold one into
  the other as a section.
- Area pages: neighborhood-specific content only (housing stock, local
  issues) — link to the core service pages for full technical detail. Never
  repeat a full repair process on an area page.
- No two pages share more than ~20% overlapping sentence-level content. (See
  the Phase 3 duplication audit in `AUDIT-REPORT.md` for the actual
  cross-page check performed on this site.)
- Fuel-type matrix pages (gas/electric/heat-pump/commercial × repair/install)
  each own their fuel type's distinguishing components: **Gas** —
  thermocouple, pilot assembly, gas valve, venting; **Electric** — heating
  elements, thermostats, high-limit switch, 240V circuit; **Heat pump** —
  compressor, refrigerant circuit, fan motor, condensate drain; **Commercial**
  — booster heaters, manifolded units, recovery rate vs. tank size, NSF
  compliance. The fuel-agnostic Repair/Installation hub pages keep the
  cross-fuel overview and link down to the fuel-specific pages rather than
  duplicating their depth.
- Symptom pages own the **diagnostic sequence** (how a homeowner identifies
  what's wrong, safe checks, when to call a pro). Service pages own the
  **repair scope and process**. E.g., "Pilot Light Won't Stay Lit" owns the
  thermocouple-failure diagnostic; "Gas Water Heater Repair" owns the repair
  service offering itself. Do not let these converge.
- Homepage service summaries: 2-3 sentences only — never copy a service
  page's intro paragraph verbatim.

---

## 6. CONTENT DEPTH STANDARD

Every service (money) page should be measurably comprehensive: what the
service covers, when it's needed, cost breakdown by component, process/what
to expect, Nampa-specific local factors (hard water, housing-stock age
split), brands serviced, and a repair-vs-replace framework where relevant.
Symptom pages should cover causes, safe homeowner diagnostic checks, when to
call a professional, and cost context.

**Koray semantic SEO writing rules (every sentence):**
1. Single macro context per page — never blend two service topics.
2. Every H2/H3 that poses an implicit question should answer it directly in
   the first sentence beneath it. Never delay the answer.
3. Bold the answer, never the search term. ("Water heater repair in Nampa
   typically costs **$150 to $600**" — bold the answer span, not "water
   heater repair.")
4. Factual structure: "X does Y" not "X is known for Y." Numeric values
   everywhere — no vague quantifiers like "several" or "many" where a real
   number is knowable.
5. Modal words weaken factual status: will/should/need to/have to — prefer
   present-tense facts.
6. Cite one real named authority per major technical claim where a claim
   actually has a verifiable source (see §9 — do not invent an attribution).
7. All numeric facts identical across every page referencing them — zero
   rounding drift. (E.g., the $150–$600 repair range must read identically on
   every page that states it.)
8. Same core n-gram opens AND closes each page where practical (contextual
   bookending) — e.g., a page's opening paragraph and its final CTA both
   reference the page's primary service + "Nampa."
9. Lists: consistent part-of-speech for the first word of every item. Tables:
   a defining sentence before the table, never a bare table.
10. Prefer the entity name over a pronoun where clarity matters. "The anode
    rod corrodes" rather than "it corrodes," especially across paragraph
    breaks.
11. After any plural noun introducing a set, give the members immediately.
    "Three components fail most often — the anode rod, the T&P valve, and the
    thermocouple" rather than leaving the set unspecified.
12. Cover genuinely useful zero-volume subtopics (permit requirements, anode
    rod lifespan, descaling interval) as H3/H4 — topic completeness is a
    ranking signal, but only state intervals within the bounds §9 allows.
13. Answer length: as short as possible, as long as necessary. Never pad to
    hit a word count.
14. No fluff, no filler, no self-promotional copy in informational sections —
    "in today's world," "it's important to note," and similar phrases have no
    place in body content.

**Heading structure rules (Bill Slawski / Google patent-informed):**
- Heading Vector principle: headings must accurately label the content
  beneath them. H1 states the single page entity. No heading is vague or
  generic.
- Exactly one H1 per page (verified sitewide — see `scripts/check_h1.py`). No
  H1 text duplicated anywhere else on the page as an H2.
- Every H1 unique across the entire site — never reused verbatim between
  pages.
- Sequential nesting only: H1→H2→H3→H4, no level skipping.
- Footer column headings match the document's heading flow.

---

## 7. INTERNAL LINKING

- Flat file structure at root (`services/`, `areas/`, `symptoms/` folders one
  level deep) — topical relationships live in internal linking, not folder
  depth.
- Header nav: Services mega-style dropdown (14 items) + Common Issues
  dropdown (6 symptom pages) + Areas We Serve dropdown (hub + 3 areas) + About
  + Contact + sticky call button. Already implemented identically across all
  29 pages — verify this stays true after any edit (`scripts/check_links.py`
  catches broken hrefs, not nav-structure drift; a visual/manual check is
  still worthwhile after nav-affecting edits).
- Footer: 6 columns (Repair Services / Installation & More / Areas We Serve /
  Company / brand block / bottom bar) — matches the site's existing footer
  template exactly on all 29 pages.
- Every service page links to: 1-2 related services (repair ↔ installation of
  the same fuel type, tank ↔ tankless) and the areas hub.
- Every symptom page links to: 2-3 relevant service pages using anchor text
  that matches the target page's H1.
- Anchor text matches the target page's H1 as closely as natural prose
  allows — never "click here."
- No dead links to unbuilt pages — `scripts/check_links.py` enforces this on
  every run; it must report 0 broken links before any commit.

---

## 8. NAMPA-SPECIFIC KEYWORD, ENTITY, AND ATTRIBUTE DATA

**Local entities (use throughout all pages):**
Nampa, Idaho; Canyon County; Treasure Valley; Lake Lowell; ZIP codes 83651 /
83686 / 83687.

**Nampa neighborhoods — use these details in content:**
- Downtown Nampa (ZIP 83651): the city's older, historic core — aging water
  heaters and outdated plumbing connections are common; repair-focused
  framing.
- Central Nampa (ZIP 83651): established residential neighborhoods, mixed
  home ages; repair and replacement framing, particular attention to
  hard-water sediment.
- South Nampa (ZIP 83686): newer construction and established luxury homes
  near Lake Lowell (built primarily mid-1990s through the 2000s, with newer
  developments alongside); installation, replacement, and tankless-upgrade
  framing.

**Component entities (use across the site for topical authority):**
anode rod, sacrificial magnesium/aluminum anode, T&P (temperature and
pressure relief) valve, thermocouple, heating element (upper and lower), gas
valve, thermostat (upper and lower), dip tube, pilot light assembly,
ignition system, expansion tank, pressure reducing valve, sediment, mineral
scale, heat exchanger (tankless), condensate drain (heat pump / condensing
tankless), flue/venting system, combustion air supply, control board
(tankless error codes), compressor and refrigerant circuit (heat pump).

**Brand entities — 8 confirmed, already used consistently sitewide (verify
against this exact list, do not drift):**
Rheem, A.O. Smith, Bradford White, American Standard, Navien, Rinnai, Noritz,
State Water Heaters.

Note: this list is **larger** than Harrisburg's 5-brand list (Rheem, A.O.
Smith, Bradford White, Rinnai, Navien) — Nampa's site deliberately adds
American Standard and Noritz per the original build brief, and also lists
State Water Heaters. Do not trim back to Harrisburg's 5-brand list; the
8-brand list is Nampa's correct, confirmed set.

**Numeric attributes — use IDENTICALLY across every page (see §9 for which of
these are sourced vs. which are the business's own stated pricing):**
- Repair cost: $150–$600 (business-stated pricing, used consistently across
  service and symptom pages)
- Installation cost: varies by fuel type and unit — see each installation
  page's own cost table; figures are copied verbatim between pages that
  reference the same service, never re-derived or averaged
- Founding year: 2019 (owner-confirmed 2026 — see stat bar on homepage +
  About page)
- Service stat: 9,000+ Water Heaters Serviced (owner-confirmed)
- Response time: 60 min Avg. Response Time (owner-confirmed)
- Brand count: 8 (see brand list above)

**PAA-style questions already answered on relevant pages (verify these stay
current — see `docs/verified-claims.md` for source status on each):**
- What's the average cost to repair a hot water heater?
- What is the most common problem with a hot water heater?
- Who do you call to come look at a hot water heater?
- Is it worth it to repair a hot water heater?
- Who do I call if I need a new hot water heater?
- Are water heater straps required in Idaho?
- Is Nampa Idaho tap water hard?
- What's the average cost of a water heater installation?
- Who is the best person to install a water heater?
- What is the longest lasting water heater brand?

---

## 9. FACTUAL INTEGRITY AND SOURCE VERIFICATION

**This section exists because the Harrisburg reference site's own audit
(2026-08-27) found it had published numeric, comparative, and attributed
claims — a hard-water hardness/geology characterization, a DOE lifespan
attribution, several maintenance intervals, a brand-specific figure — that no
accessible primary source actually supported.** A direct read of Nampa's
existing content shows the same shape of claims (hard-water ppm figures,
"hard water shortens tank life by 1-3 years," universal annual
flush/descale/anode-rod intervals). **These have not yet been re-verified
against a real source for Nampa** — see `rules/verified-claims.md` for the
live registry and Phase 3 of `AUDIT-REPORT.md` for the remediation status of
each specific instance found on this site.

**The single governing rule: repetition is not verification.** A claim that
appears on 20 Nampa pages carries no more evidentiary weight than the same
claim appearing once. Its presence in prior planning notes, in this file, or
in an HTML comment is not evidence either.

### 9.1 — Source hierarchy

In descending order of what can establish `Verified` status:
1. An official government or standards-body publication, at a URL directly
   and successfully fetched (not merely search-indexed).
2. Manufacturer documentation for the specifically named model.
3. A utility's or municipality's own official document (e.g., Nampa/Canyon
   County water quality report), directly fetched.
4. A written owner-confirmation record, for business-controlled claims only
   (§9.5) — never for technical, safety, or local-fact claims.

### 9.2 — Claim classification

| Status | May publish? |
|---|---|
| `Verified` | Yes, with any required qualifiers |
| `Conditional` | No — not until the condition and evidence are both met |
| `Unverified` | No |
| `Retired` | No — do not re-propose without materially new evidence |
| `Owner-confirmed` | Yes, citing the confirmation record (business-controlled claims only) |

### 9.3 — Local-fact rules

No water-hardness, geological, or demographic claim may be published without
an official document meeting §9.1. A specific ppm/gpg hardness figure for
Nampa's municipal water, a geological characterization, or a "highest demand"
claim about a neighborhood all require this. Do not substitute an unsupported
claim with its opposite — the correct status for an unresolved claim is
`Unverified`, not a swapped assertion.

### 9.4 — Technical, safety, and comparative-claim rules

No maintenance interval, repair procedure, or safety instruction may be
stated as a universal requirement — defer to "the manufacturer's
instructions" / "the unit's owner's manual." Comparative language ("shortens
tank life," "more efficient," "commonly," "typically") is a factual claim and
requires the same sourcing as any number. A qualifier does not exempt a claim
from this requirement — "often" attached to an unsupported figure is a hedged
unsupported claim, not a supportable one.

### 9.5 — Business-controlled claim rules

Claims only the business itself can confirm — phone number, hours, response
time, years in operation, service count, licensing/insurance status — reach
`Owner-confirmed` status only with an identifiable written confirmation
record. Founding year (2019), the 9,000+ stat, and the 60-minute response
time are `Owner-confirmed` per the entity-consistency task that established
them (see `AUDIT-REPORT.md`). "Licensed & Insured" has no confirmation record
on file and should be treated as `Unverified / Awaiting owner confirmation`
like every other unconfirmed business claim — its continued sitewide
presence is not itself evidence.

### 9.6 — Attribution rules

Attributing a claim to a named authority (the U.S. Department of Energy, a
manufacturer) is itself a claim and requires that authority's own accessible
publication stating it. An attribution that cannot be traced to a directly
fetched source is `Retired`, not merely unattributed — remove both the number
and the name together.

### 9.7 — Pre-publication factual gate

A new or materially-rewritten page does not ship with a numeric, comparative,
technical, or attributed claim that has no corresponding entry in
`rules/verified-claims.md`, or whose entry's status is anything other than
`Verified` or `Owner-confirmed`.

---

## 10. TECHNICAL SEO (as-implemented — reference, not a to-do list)

- Self-referencing canonical on every page, apex domain
  (`https://nampawaterheater.com/...`), no `www.` variant in use anywhere.
- `robots.txt`: minimal universal allow (`User-agent: *` / `Allow: /` /
  `Sitemap:` line) — 4 lines, no per-crawler blocks. Matches the Harrisburg
  reference site's own post-simplification standard.
- `sitemap.xml`: every live page, kept in exact sync with the file tree —
  `scripts/build_sitemap.py` regenerates it; 29 `<loc>` entries as of this
  writing.
- Schema: `LocalBusiness` with a single, sitewide `@id`
  (`https://nampawaterheater.com/#organization`) referenced by `@id` from
  every other node that needs it (provider references, `about`, `publisher`)
  — never re-declared with full properties in more than the one canonical
  block. See `AUDIT-REPORT.md`'s Entity Consistency Audit for the full
  standardization trail.
- `FAQPage` schema text must be word-for-word identical to the visible
  on-page text — any mismatch risks rich-result failure.
- Open Graph / Twitter Card tags: **not currently implemented sitewide** —
  flagged as a gap during this rules migration (Harrisburg's site has full
  OG/Twitter coverage; Nampa's does not). See Phase 2/3 findings in
  `AUDIT-REPORT.md`.
- Accessibility: 4.5:1 minimum contrast, underlined links (not color-only),
  48px minimum touch targets on buttons and `tel:` links.

---

## 11. SITE-WIDE CONSISTENCY (zero drift)

- Brand name: **Nampa Water Heater Pros** — exact casing, every mention, zero
  variants. (Verified: 323 occurrences, zero variants, as of the
  entity-consistency audit.)
- Phone: `(208) 987-5152` visible / `tel:+12089875152` href /
  `+1-208-987-5152` schema — one format per context, chosen once, never
  varied.
- Founding year: 2019. Stat: 9,000+ Water Heaters Serviced. Response time: 60
  min Avg. Response Time. All three appear together in the stat bar on the
  homepage and About page, word-for-word identical between the two.
- Numeric facts: copied exactly wherever repeated — never paraphrased or
  rounded differently between pages.
- Header and footer: structurally identical across every page (only active
  nav state changes).
- Service-area sentence: `Serving Nampa, ID and surrounding areas — 83651,
  83686, 83687` — this exact wording, wherever the sentence-form (not the
  "Primary Zip Codes:" label form) appears.

---

## 12. ZERO-DEFECT CHECKLIST (run before marking any content task done)

Adapted from the Harrisburg reference site's 44-point "Day-One Zero-Defect
Rules," trimmed to what applies to an already-built site doing content
maintenance rather than a fresh multi-phase build:

- [ ] Exactly one H1 per page, unique across the site
- [ ] No heading level skipped (H1→H2→H3→H4 only)
- [ ] No FAQ topic answered in both body prose AND the FAQ section with the
      same question
- [ ] No key phrase repeated verbatim more than once per page in close
      proximity (keyword-stuffing check)
- [ ] Every phone number is a working `tel:+12089875152` link, exact format
- [ ] Valid JSON-LD, no HTML tags inside any JSON-LD value
- [ ] `FAQPage` schema matches visible text word-for-word
- [ ] Self-referencing canonical present
- [ ] Every `<img>` has `width`/`height` (or CSS aspect-ratio), descriptive
      alt text, and correct `loading` attribute (`eager` for the
      above-the-fold hero, `lazy` for everything else)
- [ ] No horizontal scroll at 320px viewport width
- [ ] Tables wrapped for overflow scroll on narrow viewports
      (`.cost-table` mobile rule already implements this)
- [ ] CTA button text varies across the site — not identical everywhere
- [ ] `robots.txt`: zero non-standard directives
- [ ] Every H2/H3 that implies a question answers it directly in the first
      sentence beneath it
- [ ] Zero promotional language in informational answer text
- [ ] Zero instances of "near me" in title tags, H1s, or body copy (it is
      acceptable, at most once, inside an FAQ question — this pattern is not
      currently used on the Nampa site and should not be introduced without a
      specific reason)
- [ ] City/area name (Nampa, or a specific neighborhood) appears within the
      first 50 words of body content on service, symptom, and area pages
- [ ] At least one Nampa ZIP code mentioned naturally in body content
- [ ] No claim published without a corresponding `Verified` or
      `Owner-confirmed` entry in `rules/verified-claims.md` (see §9)

---

## 13. WHERE THIS DIFFERS FROM THE HARRISBURG REFERENCE (explicit, so this
doesn't silently drift back toward Harrisburg's specifics over time)

- Harrisburg: 4-phase, ~46-page geographic expansion plan. Nampa: fixed
  29-page site, no phased backlog.
- Harrisburg: folder + `index.html` clean URLs. Nampa: flat `.html` files at
  each level.
- Harrisburg: 5 confirmed brands. Nampa: 8 confirmed brands (adds American
  Standard, Noritz, State Water Heaters).
- Harrisburg: `Since 2017 / 7,000+ / 90 min` stat bar. Nampa: `Since 2019 /
  9,000+ / 60 min`.
- Harrisburg: full Open Graph/Twitter Card implementation. Nampa: not yet
  implemented — a real gap, not a stylistic difference.
- Harrisburg: `docs/verified-claims.md` already has a mature registry with
  Harrisburg-specific findings (limestone geology unverified, DOE attribution
  retired, etc.). Nampa's registry (`rules/verified-claims.md`) starts fresh
  — it does not inherit Harrisburg's specific findings, since those don't
  transfer to a different city and different, unverified water utility, but
  it applies the identical rigor to Nampa's own claims.
