export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // Block .html URL requests — return 404 so old .html paths never redirect
    if (pathname.endsWith('.html')) {
      return new Response(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>404 Not Found</title>' +
        '<meta name="robots" content="noindex"></head>' +
        '<body><h1>404 Not Found</h1>' +
        '<p>The page you requested does not exist. ' +
        '<a href="/">Return to Nampa Water Heater Pros</a>.</p></body></html>',
        {
          status: 404,
          headers: { 'content-type': 'text/html; charset=utf-8' },
        }
      );
    }

    // Redirect trailing-slash paths to no-trailing-slash (except homepage /)
    if (pathname.length > 1 && pathname.endsWith('/')) {
      const canonical = new URL(url);
      canonical.pathname = pathname.slice(0, -1);
      return Response.redirect(canonical.toString(), 301);
    }

    // With html_handling: "none", ASSETS serves files by exact path only (no auto-redirects).
    // Try the bare path first — handles non-HTML assets (CSS, images, fonts, etc.)
    // and the homepage / (ASSETS always serves index.html at the root).
    const assetResponse = await env.ASSETS.fetch(request);
    if (assetResponse.status !== 404) {
      return assetResponse;
    }

    // Clean URL → .html file on disk: /about → about.html
    const htmlResponse = await env.ASSETS.fetch(
      new Request(new URL(pathname + '.html', url).toString(), {
        method: request.method,
        headers: request.headers,
      })
    );
    if (htmlResponse.status === 200) {
      return htmlResponse;
    }

    // Hub/directory pages: /services → services/index.html
    const indexResponse = await env.ASSETS.fetch(
      new Request(new URL(pathname + '/index.html', url).toString(), {
        method: request.method,
        headers: request.headers,
      })
    );
    if (indexResponse.status === 200) {
      return indexResponse;
    }

    return assetResponse; // 404
  },
};
