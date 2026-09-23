/**
 * Cloudflare Worker + Static Assets router for nampawaterheater.com
 *
 * Contract:
 *   /                -> index.html                       (200)
 *   /about           -> about.html                       (200)
 *   /services        -> services/index.html              (200)
 *   /assets/x.css    -> assets/x.css                     (200)
 *   /about.html      -> 404 (never redirect)
 *   /services/       -> 301 -> /services
 *   www.<host>/x     -> 301 -> <host>/x
 *
 * Asset resolution is fully explicit. `html_handling` is set to "none" in
 * wrangler.jsonc, so ASSETS serves a file only at its literal path and performs
 * no index/extension rewriting of its own. Every candidate path is therefore
 * constructed here. Do not reintroduce a dependency on ASSETS rewriting.
 */

const CANONICAL_HOST = 'nampawaterheater.com';

const NOT_FOUND_BODY =
  '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>404 Not Found</title>' +
  '<meta name="robots" content="noindex"></head>' +
  '<body><h1>404 Not Found</h1>' +
  '<p>The page you requested does not exist. ' +
  '<a href="/">Return to Nampa Water Heater Pros</a>.</p></body></html>';

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

async function route(request, env) {
  const url = new URL(request.url);

  // Canonical host: www -> apex, preserving path and query.
  if (url.hostname === 'www.' + CANONICAL_HOST) {
    const canonical = new URL(url.toString());
    canonical.hostname = CANONICAL_HOST;
    return Response.redirect(canonical.toString(), 301);
  }

  const pathname = url.pathname;

  // Old .html paths must 404, never redirect.
  if (pathname.endsWith('.html')) {
    return notFound();
  }

  // Trailing slash -> no trailing slash, except the homepage.
  if (pathname.length > 1 && pathname.endsWith('/')) {
    const canonical = new URL(url.toString());
    canonical.pathname = pathname.slice(0, -1);
    return Response.redirect(canonical.toString(), 301);
  }

  for (const path of candidatePaths(pathname)) {
    const response = await env.ASSETS.fetch(assetRequest(url, path, request));
    if (response.status === 200) {
      return response;
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
