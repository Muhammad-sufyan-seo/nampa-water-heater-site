# Image Guidelines — Nampa Water Heater Pros

Adapted from the Harrisburg reference site's `IMAGE-MANIFEST.md` and CLAUDE.md
§12 (Image Design System). Nampa now has its own local photo library —
`assets/images/` — with 46 real files (45 photos + `favicon.ico`), all used
site-wide as of the 2026-08 image-maximization pass. This supersedes the
"no local image library" state described in earlier versions of this file.

---

## 1. Current state (as of the 2026-08 image-maximization pass)

All 29 pages use only local `assets/images/` files. There are zero remote
Unsplash (or other external) image references anywhere on the site.

| Page group | Images per page |
|---|---|
| `index.html` | Hero (local JPG background) + an 8-image brand grid |
| `about.html`, `contact.html`, `areas/index.html` | 1–2 contextual images |
| 3 area pages (`areas/downtown-nampa.html`, `central-nampa.html`, `south-nampa.html`) | 2 each |
| 14 service pages | 2–4 each, concentrated on higher-intent pages (gas/electric repair, tankless repair/installation, replacement) |
| 6 symptom pages (`symptoms/*.html`) | 2–3 each — previously had **zero** images; now every symptom page opens with an exact-topic hero image |
| `privacy-policy.html`, `terms.html` | 0 (legal boilerplate; no content image is contextually relevant) |

Every `<img>` tag carries: descriptive alt text (entity + Nampa reference),
`loading="lazy"` (all non-decorative images; the homepage hero is a CSS
`background-image`, not an `<img>`, so lazy-loading doesn't apply to it),
and inline `width`/`height` + `style="width:100%;height:auto;display:block;"`
for responsive sizing. None uses `srcset`/`sizes` — the site has no
responsive-image pattern established anywhere, so there is no existing
convention to "stay consistent with" per se; the current CSS approach is the
applicable pattern until/unless a `srcset` convention is deliberately
introduced.

A `<link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">`
(root pages) / `href="../assets/images/favicon.ico"` (subfolder pages) is
present in every page's `<head>`, and the `nampa-water-heater-pros-logo.png`
file is used as a small image in every page's footer brand block.

## 2. What Harrisburg's system looks like, for reference only

Harrisburg mandates 8 image slots per page minimum (hero, brand logo strip,
trust-bar accent, 2 service-highlight split sections, a process visual, a
divider strip, and a pre-footer CTA banner), all sourced from a real,
purpose-shot 39-file photo library, with a documented reuse cap (max 5-6 uses
per image site-wide, tracked in `IMAGE-MANIFEST.md`). This is the target
end-state for a mature build with commissioned photography — it is **not**
achievable for Nampa today without either (a) real Nampa jobsite photography
being supplied, or (b) a deliberate decision to build out a larger stock-photo
set. Treat the 8-slot system as aspirational, not a compliance bar this
audit can pass or fail Nampa against today.

## 3. What this audit actually does

Given no local asset library exists, "select the most relevant available
image from the uploaded set" (as a generic image-audit instruction might
assume) has no literal set to select from. The practical equivalent applied
here, consistent with the Harrisburg site's own admitted interim practice
(§12.1 of its CLAUDE.md explicitly describes using stock photography "for
layout/visual review only" pending real photography): extend the same
Unsplash-sourced interim pattern already used on the 7 pages that have
images, to at least the highest-priority pages that currently have none —
prioritizing the 14 service (money) pages first — using topically accurate,
specific search terms (not generic "plumber" photos) and implementing them to
the same technical standard as the rest of this file specifies.

See `AUDIT-REPORT.md`'s Phase 2 section for exactly which pages were given a
new image in this pass, which were left for a future pass, and why.

## 4. Technical requirements for every image added or touched

- **Alt text:** entity + service + Nampa reference, matching the site's
  existing convention exactly, e.g. `alt="Licensed plumber diagnosing a gas
  water heater in a Nampa, Idaho home"`. Never generic (`alt="water heater"`)
  and never keyword-stuffed.
- **Loading:** `loading="eager"` (or omitted, with a `<link rel="preload"
  as="image">` if the page later adopts one) for the single
  above-the-fold/hero image on a page; `loading="lazy"` for every other
  image.
- **Layout stability:** explicit `width`/`height` attributes on every
  `<img>`, or a wrapping element with a CSS `aspect-ratio` set — either is
  acceptable, but one of the two must be present. No image may cause layout
  shift on load.
- **Responsiveness:** `max-width: 100%; height: auto;` behavior (already the
  effective default inside the site's content containers) — verify a newly
  added image is not given a fixed pixel width that would break this.
- **Format/URL hygiene:** Unsplash URLs must include explicit sizing/format
  query params (`?w=800&q=80` pattern, matching the 7 existing images)
  rather than an unbounded original-resolution fetch.
- **Relevance:** the image's actual subject must match its section's topic.
  A symptom page about "no hot water" needs a plumbing/water-heater
  diagnostic image, not an unrelated house-exterior or generic-toolbox stock
  photo. Verify this by eye, not just by filename/alt-text plausibility —
  Unsplash search results can return topically mismatched photos for a
  query that sounds right.

## 5. Real photography backlog (flagged, not actioned by this pass)

Every image on this site — the 7 existing and any added in this pass — is
stock photography, not real Nampa jobsite photography. This mirrors exactly
the gap Harrisburg's own manifest flags for its heat-pump/commercial pages
(no dedicated photography exists yet, closest-relevant photo reused with
accurate alt text as an acknowledged interim measure) — except for Nampa it
is the default state for the entire site, not four pages. Replacing stock
photography with real photography across all 29 pages is a distinct future
project requiring the business owner to supply photos; it is out of scope for
a content/rules audit and is not something to silently attempt with more
stock images beyond what this pass adds.
