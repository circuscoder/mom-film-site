# MOM film site

Newsletter-first film landing page with a separate `/watch/` route. Plain HTML, CSS,
JavaScript; no build step or runtime dependencies. Serve this folder as a static site.

```sh
python -m http.server 8765 --bind 127.0.0.1
```

V2 is local on `redesign/v2-newsletter`. V1 remains at `archive/v1-responsive` and
`design-v1-responsive`. Do not push or deploy this pass.

## Connect the newsletter

Edit **`assets/js/signup-config.js`**. Both homepage forms use this one configuration.
Provide:

1. A public HTTPS POST endpoint that adds the email to the actual MOM newsletter list
   (or queues the provider's confirmation email), allows CORS from the deployed site,
   accepts multipart form data, and returns JSON. A generic inbox/contact form does
   not subscribe anyone unless its automation explicitly does so.
2. The provider's email field name and any public required list/form fields. Put them
   in `emailField` and `extraFields`.
3. The provider's documented acceptance response. Adapt `isAccepted(response, body)`
   to it; default requires both HTTP success and `{ "success": true }`. Match
   `successMessage` to whether confirmation is required. Do not call a pending
   double-opt-in request a completed subscription.

No API secrets belong in client-side code. Providers that require a secret need a
server-side adapter. Verify the list assignment, unsubscribe flow, and consent copy
with the selected provider before launch; then make one real test subscription and
confirm it appears in that provider's list. The local regression tests mock requests
and send no addresses externally.

Until configured, the page explains that signup is unavailable. Submitting never
reports success or sends an email. Invalid input gets an inline error and focus;
requests have a disabled/loading state, 15-second timeout, retained input on failure,
and retry. No-JavaScript visitors see the unavailable message and disabled buttons.
The footer retains existing name field IDs/names/order as hidden empty fields;
only email is requested and sent. If the provider actually requires names, surface
those fields and add their mapping in the configuration/adapter.

## Trailer access

`/watch/` retains first name, last name, then email, the existing field identifiers,
and the separate consent intent. It validates fields but honestly reports unavailable
access. It no longer reveals a fictitious Vimeo link. Activation is a separate task:
provide the real trailer URL and a server-side delivery/access mechanism. A static
client-side gate cannot protect a private trailer. Newsletter configuration does not
silently subscribe watch visitors or change watch consent.

## Design and maintenance

- `REDESIGN_PLAN.md`: accepted v2 direction and constraints.
- `REDESIGN_REVIEW.md`: audit, design decisions and validation evidence.
- `assets/css/tokens.css`: inherited light palette/system-font tokens, softened surfaces.
- `assets/js/layout.js`: locked measured padding interpolation; unchanged from v1.
- `assets/js/motion.js`: 28px maximum photo drift; desktop only, reduced-motion static.
- Existing routes and section IDs remain; no new tracking or external asset requests.

## Regression checks

With an existing Python Playwright installation and Chromium browser available:

```sh
python scripts/check_site.py
```

Start the local server first. Optional `--url` and `--output` override the server and
screenshot destination. The default output is workspace scratch, not the repository.
Checks cover both routes at all five planned sizes, preserved padding, overflow,
loaded images, early CTA visibility, field validation/focus, truthful unconfigured
states, provider acceptance/rejection, loading, duplicate submission, network error,
retry, photo-edge coverage, reduced motion, and a no-JavaScript fallback.
