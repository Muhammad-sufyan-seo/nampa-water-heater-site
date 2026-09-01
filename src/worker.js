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

    // Try to serve the request from static assets
    const response = await env.ASSETS.fetch(request);

    // If ASSETS returns 404 for a path without trailing slash,
    // try serving it as a directory index (e.g., /services → services/index.html)
    if (response.status === 404 && !pathname.endsWith('/')) {
      const indexRequest = new Request(
        new URL(pathname + '/', url).toString(),
        { method: request.method, headers: request.headers }
      );
      const indexResponse = await env.ASSETS.fetch(indexRequest);
      if (indexResponse.status === 200) {
        return indexResponse;
      }
    }

    return response;
  },
};
