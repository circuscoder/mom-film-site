# V2 redesign review

## Audit before implementation

The source was a vanilla static site with no build or dependencies. Its actual tokens
were white/gray/charcoal with yellow accent and a system sans stack, newer than parts
of the PRD. The recognizable MOM wordmark, supplied production photos, film premise,
filmmaker identities and responsive padding were the assets to preserve.

The conversion path was inconsistent with the newsletter goal: both top CTAs sent
visitors to `/watch/`; newsletter signup was buried in the footer behind name fields.
The footer changed its button to “Thanks!” without a request. The watch form ignored
validation and revealed a dummy Vimeo URL. Other visible placeholders included fake
contact addresses, a `#` support link and a developer-facing trailer caption. The
hero's 100dvh height plus header pushed its bottom action beyond the initial viewport.
Images lacked intrinsic dimensions; there was no skip link. The repeated full-width
section pattern made the page longer without strengthening the signup invitation.

## Design decisions

Reading: intimate cinematic film landing page for visitors from social/word of mouth.
Dials: variance 6, motion 4, density 3. Native CSS, the supplied photography, inherited
system typography, softened light neutrals and the existing yellow accent. The
UI/UX database matched newsletter/content-first structure; its generic pink/Inter
recommendation was not adopted because the existing brand and brief take precedence.

The hero pairs a short premise with an actual email field. Mobile gets a single
composition with a visible photographic opening, stable title and stacked form.
One desktop-only 28px drift provides depth to the opening still; no moving body text,
buttons or fields, scroll hijacking, or fixed backgrounds. No additional reveals were
needed. The article-like synopsis, trailer photo, compact filmmaker biographies and
screenings note lead to the closing signup. The watch route remains separate.

The explicit v2 constraints take precedence over generic skill defaults: existing
vanilla stack/no dependencies, existing photos, fixed light identity, repeated signup
intent requested by the brief, and passive requestAnimationFrame scroll motion. The
v1 form field identities/order remain; unused footer names are hidden and are not sent.
The watch consent language is preserved, with unavailable state disclosed before use.

## Validation

Executed `python scripts/check_site.py` with installed Python Playwright/Chromium.
Both `/` and `/watch/` passed at every required viewport:

| Viewport | Side padding | Horizontal overflow | Hero signup button |
| --- | --- | --- | --- |
| 360x800 | 42px | None | Above fold |
| 390x844 | 42px | None | Above fold |
| 768x1024 | 39.96px | None | Above fold |
| 1440x900 | 58px | None | Above fold |
| 1900x1080 | 250px | None | Above fold |

- `layout.js` is byte-for-byte unchanged; `.wrap` retains original max-width and padding.
- All home screenshots visually inspected; crops, hierarchy, readable text, form fit.
- All images loaded; explicit dimensions/aspect ratios reserve space.
- Keyboard focus moves to first invalid field; visible labels and focus indicators.
- Unconfigured forms report unavailable without sending; watch order and hidden reveal checked.
- Both newsletter placements tested with mocked accepted/rejected HTTP/JSON responses.
- Loading/disabled button, duplicate-submit guard, network failure, retained input and successful retry tested.
- Photo layer covers hero edges during drift; mobile and reduced motion use no transform.
- No-JavaScript view has static photography, visible unavailable text and disabled submission.
- No browser JavaScript errors. JavaScript syntax and Git whitespace checks passed.
- Reviewed against freshly retrieved Vercel Web Interface Guidelines (2026-09-09).

Screenshots are in workspace scratch (`/_scratch/mom-v2-checks`), outside the site repo.
Lighthouse was not installed; no Lighthouse score or production Web Vitals claim is made.
Tests use local mocked endpoints; real provider capture cannot be verified until supplied.
No push or deployment was performed.

## Activation input

A real newsletter subscription endpoint with CORS, multipart POST field names/list
parameters, and documented JSON acceptance semantics. Enter these at
`assets/js/signup-config.js`, then verify actual list capture/confirmation/unsubscribe
with the provider. See README for the exact contract. Trailer delivery additionally
needs its own real URL and server-side delivery mechanism; it is not activated by
newsletter configuration.
