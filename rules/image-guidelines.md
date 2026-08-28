# Image Guidelines — Nampa Water Heater Pros

Adapted from the Harrisburg reference site's `IMAGE-MANIFEST.md` and CLAUDE.md
§12 (Image Design System). **The starting position is materially different and
that difference is the most important thing in this file:** Harrisburg has a
39-file local photo library (`assets/images/`) with a documented manifest of
which real file every page uses. Nampa has **no local image library at all** —
`assets/` contains only `css/` and `js/`. The 7 `<img>` tags that exist across
Nampa's 29 pages all point to remote Unsplash URLs, and 22 of the 29 pages
carry zero images of any kind.

Do not let this file's structure (borrowed from a site with real photography)
imply Nampa has image coverage it doesn't. Every claim below about what
currently exists is stated plainly; recommendations for what to add are
labeled as such, not presented as already-done.

---

## 1. Current state (as of this rules migration)

| Page | Image(s) |
|---|---|
| `about.html` | 1 (Unsplash) |
| `services/repair.html` | 1 (Unsplash) |
| `services/installation.html` | 1 (Unsplash) |
| `services/replacement.html` | 1 (Unsplash) |
| `areas/downtown-nampa.html` | 1 (Unsplash) |
| `areas/central-nampa.html` | 1 (Unsplash) |
| `areas/south-nampa.html` | 1 (Unsplash) |
| All other 22 pages (index, contact, privacy, terms, areas/index, 9 fuel-matrix service pages, maintenance, 6 symptom pages) | **0** |

Each of the 7 existing images already carries: descriptive alt text
(entity + Nampa reference), `loading="lazy"`, and inline sizing. None uses
`srcset`/`sizes` — the site has no responsive-image pattern established
anywhere, so there is no existing convention to "stay consistent with" per
se; CSS `max-width: 100%; height: auto;` on the image element (already the
site's implicit behavior via its content-width containers) is the applicable
pattern until/unless a `srcset` convention is deliberately introduced.

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
