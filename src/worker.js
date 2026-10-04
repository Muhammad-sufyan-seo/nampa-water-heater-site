/**
 * Cloudflare Worker + Static Assets router for nampawaterheater.com
 *
 * Contract:
 *   /                -> index.html                       (200)
 *   /about           -> about.html                       (200)
 *   /services        -> services/index.html              (200)
 *   /assets/x.css    -> assets/x.css                     (200)
 *   /about.html      -> styled 404 (never redirect)
 *   /services/       -> 301 -> /services
 *   www.<host>/x     -> 301 -> <host>/x
 *
 * Asset resolution is fully explicit. `html_handling` is set to "none" in
 * wrangler.jsonc, so ASSETS serves a file only at its literal path and performs
 * no index/extension rewriting of its own. Every candidate path is therefore
 * constructed here. Do not reintroduce a dependency on ASSETS rewriting.
 */

const CANONICAL_HOST = 'nampawaterheater.com';

/**
 * Extensions that identify static asset files.
 * Requests for these must go directly to ASSETS — no .html or /index.html
 * fallback — so a missing asset returns a genuine 404, never HTML.
 */
const STATIC_EXTS = new Set([
  '.css', '.js', '.mjs',
  '.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.gif',
  '.woff', '.woff2', '.ttf', '.eot',
  '.json', '.webmanifest', '.xml', '.txt', '.pdf',
  '.mp4', '.webm', '.mp3', '.ogg',
]);

function hasStaticExtension(pathname) {
  const dot = pathname.lastIndexOf('.');
  return dot !== -1 && STATIC_EXTS.has(pathname.slice(dot).toLowerCase());
}

// Cache-Control tiers keyed by file extension.
const CC_SCRIPT = new Set(['.css', '.js', '.mjs']);
const CC_MEDIA  = new Set([
  '.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.gif',
  '.woff', '.woff2', '.ttf', '.eot',
  '.mp4', '.webm', '.mp3', '.ogg',
]);

function cacheControl(pathname) {
  const dot = pathname.lastIndexOf('.');
  const ext = dot !== -1 ? pathname.slice(dot).toLowerCase() : '';
  if (CC_SCRIPT.has(ext)) return 'public, max-age=3600, must-revalidate';
  if (CC_MEDIA.has(ext))  return 'public, max-age=604800';
  return 'public, max-age=0, must-revalidate';
}

function withCacheControl(response, cc) {
  const r = new Response(response.body, response);
  r.headers.set('cache-control', cc);
  return r;
}

const NOT_FOUND_BODY = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>Page Not Found | Nampa Water Heater Pros</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600&family=Source+Serif+4:wght@300;400&display=swap">
  <style>
    :root {
      --navy: #1B2A3B;
      --ember: #E8500A;
      --ember-dark: #C44208;
      --cream: #F7F4EF;
      --slate: #4A5568;
      --light: #EDE9E3;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--cream);
      color: var(--navy);
      font-family: 'Source Serif 4', Georgia, serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
      text-align: center;
    }
    .brand {
      font-family: 'Oswald', 'Arial Narrow', sans-serif;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--slate);
      margin-bottom: 2rem;
    }
    .code {
      font-family: 'Oswald', sans-serif;
      font-size: clamp(6rem, 20vw, 9rem);
      font-weight: 600;
      line-height: 1;
      color: var(--ember);
      margin-bottom: 0.25rem;
    }
    h1 {
      font-family: 'Oswald', sans-serif;
      font-size: clamp(1.4rem, 4vw, 2rem);
      font-weight: 400;
      color: var(--navy);
      margin-bottom: 1rem;
    }
    p {
      font-size: 1.05rem;
      color: var(--slate);
      max-width: 36rem;
      line-height: 1.6;
      margin-bottom: 2.5rem;
    }
    nav {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      justify-content: center;
    }
    nav a {
      display: inline-block;
      padding: 0.65rem 1.4rem;
      border-radius: 4px;
      font-family: 'Oswald', sans-serif;
      font-size: 0.95rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      transition: background 0.15s, color 0.15s;
    }
    nav a.primary {
      background: var(--ember);
      color: #fff;
    }
    nav a.primary:hover { background: var(--ember-dark); }
    nav a.secondary {
      background: var(--light);
      color: var(--navy);
      border: 1px solid #d0ccc6;
    }
    nav a.secondary:hover { background: #dedad3; }
    .divider {
      width: 3rem;
      height: 3px;
      background: var(--ember);
      margin: 0 auto 2rem;
      border-radius: 2px;
    }
  </style>
</head>
<body>
  <p class="brand">Nampa Water Heater Pros</p>
  <div class="code" aria-hidden="true">404</div>
  <div class="divider"></div>
  <h1>Page Not Found</h1>
  <p>The page you requested doesn&rsquo;t exist. It may have moved or the URL may be incorrect.</p>
  <nav aria-label="Return navigation">
    <a href="/" class="primary">Go Home</a>
    <a href="/services" class="secondary">Our Services</a>
    <a href="/contact" class="secondary">Contact Us</a>
  </nav>
</body>
</html>`;

function notFound() {
  return new Response(NOT_FOUND_BODY, {
    status: 404,
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'no-store',
    },
  });
}

/**
 * Fetch one asset path from the ASSETS binding.
 * Builds the target by assigning `pathname` on a same-origin URL rather than
 * resolving a relative string: `new URL('/' + '/index.html', base)` parses as a
 * protocol-relative URL and silently retargets a different host.
 */
function assetRequest(url, path, request) {
  const target = new URL(url.toString());
  target.pathname = path;
  return new Request(target.toString(), {
    method: request.method,
    headers: request.headers,
  });
}

/** Candidate on-disk paths for a clean URL, in resolution order. */
function candidatePaths(pathname) {
  if (pathname === '/') {
    return ['/index.html'];
  }
  return [
    pathname,                    // exact file: css, js, images, robots.txt, sitemap.xml
    pathname + '.html',          // clean page URL: /about -> about.html
    pathname + '/index.html',    // hub/directory: /services -> services/index.html
  ];
}

/**
 * Scheduled-release gate. Deployed pages stay deployed but return the
 * ordinary 404 until their release instant — the gate is enforced here,
 * not by timing the deploy itself, so the exact minute a page goes live
 * never depends on when `git push` or CI happened to run.
 */
const RELEASE_GATES = {
  '/repair-vs-replace-nampa-id': '2026-10-05T01:00:00Z',
  '/common-issues/water-heater-rotten-egg-smell-nampa-id': '2026-10-05T01:00:00Z',
  '/water-heater-lifespan-nampa-id': '2026-10-05T01:00:00Z',
  '/gas-vs-electric-water-heater-nampa-id': '2026-10-05T01:00:00Z',
  '/tankless-vs-tank-water-heater-nampa-id': '2026-10-05T01:00:00Z',
  '/water-heater-sizing-guide-nampa-id': '2026-10-05T01:00:00Z',
  '/water-heater-maintenance-checklist-nampa-id': '2026-10-05T01:00:00Z',
};

/** Pure function — takes `now` as a parameter so release boundaries are testable. */
function isGated(pathname, now) {
  const releaseAt = RELEASE_GATES[pathname];
  if (!releaseAt) return false;
  return now.getTime() < new Date(releaseAt).getTime();
}

/**
 * Strip any <url>...</url> block from a sitemap XML string whose <loc>
 * path is currently gated. Pure function — `now` passed in for testability.
 */
function filterSitemap(xmlText, now) {
  return xmlText.replace(/<url>[\s\S]*?<\/url>\s*/g, (block) => {
    const locMatch = block.match(/<loc>(.*?)<\/loc>/);
    if (!locMatch) return block;
    let pathname;
    try {
      pathname = new URL(locMatch[1]).pathname;
    } catch {
      return block;
    }
    return isGated(pathname, now) ? '' : block;
  });
}

async function route(request, env) {
  const url = new URL(request.url);

  // Canonical host: www -> apex, preserving path and query.
  if (url.hostname === 'www.' + CANONICAL_HOST) {
    const canonical = new URL(url.toString());
    canonical.hostname = CANONICAL_HOST;
    return Response.redirect(canonical.toString(), 301);
  }

  const pathname = url.pathname;

  // .html URLs must 404, never redirect.
  if (pathname.endsWith('.html')) {
    return notFound();
  }

  // Scheduled-release gate: not yet public, behaves exactly like a 404.
  if (isGated(pathname, new Date())) {
    return notFound();
  }

  // Trailing slash -> no trailing slash, except the homepage.
  if (pathname.length > 1 && pathname.endsWith('/')) {
    const canonical = new URL(url.toString());
    canonical.pathname = pathname.slice(0, -1);
    return Response.redirect(canonical.toString(), 301);
  }

  // sitemap.xml is a static file normally served as-is, but it must never
  // list a page before that page's own release gate opens — otherwise the
  // sitemap itself becomes the early-discovery leak, even though the page
  // behind the link still 404s. Filtered dynamically so this holds exactly
  // in step with RELEASE_GATES, with no separate timed deploy required.
  if (pathname === '/sitemap.xml') {
    const response = await env.ASSETS.fetch(assetRequest(url, pathname, request));
    if (response.status !== 200) {
      return new Response('', { status: 404, headers: { 'cache-control': 'no-store' } });
    }
    const text = await response.text();
    const filtered = filterSitemap(text, new Date());
    return new Response(filtered, {
      status: 200,
      headers: {
        'content-type': 'application/xml; charset=utf-8',
        'cache-control': cacheControl(pathname),
      },
    });
  }

  // Static assets (CSS, JS, images, fonts, etc.) are served directly.
  // Never try .html / /index.html variants: a missing asset must return a
  // genuine 404, not an HTML page.
  if (hasStaticExtension(pathname)) {
    const response = await env.ASSETS.fetch(assetRequest(url, pathname, request));
    if (response.status === 200) return withCacheControl(response, cacheControl(pathname));
    return new Response('', { status: 404, headers: { 'cache-control': 'no-store' } });
  }

  for (const path of candidatePaths(pathname)) {
    const response = await env.ASSETS.fetch(assetRequest(url, path, request));
    if (response.status === 200) {
      return withCacheControl(response, 'public, max-age=0, must-revalidate');
    }
  }

  return notFound();
}

export default {
  async fetch(request, env) {
    try {
      return await route(request, env);
    } catch (err) {
      // A routing bug must not surface as a platform 500. Serve the homepage
      // asset directly if we can; otherwise a clean 404.
      try {
        const url = new URL(request.url);
        const response = await env.ASSETS.fetch(assetRequest(url, '/index.html', request));
        if (response.status === 200) {
          return response;
        }
      } catch (_) {
        // fall through
      }
      return notFound();
    }
  },
};

// Named exports for the release-boundary test suite only — the Worker
// runtime uses the default export exclusively.
export { isGated, RELEASE_GATES, filterSitemap };
