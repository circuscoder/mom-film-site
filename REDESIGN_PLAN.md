# MOM site v2: newsletter-first cinematic refresh

## Design read

A focused film landing page for people arriving from social or word of mouth. It should feel intimate, cinematic, and alive while staying simple enough that the next action is obvious: join the MOM newsletter.

Creative dials: variance 6/10, motion 4/10, density 3/10.

## Preserve the current version

The existing responsive site is frozen at commit `ad0f6a6` under both:

- branch `archive/v1-responsive`
- tag `design-v1-responsive`

The redesign lives on `redesign/v2-newsletter`. Do not push or deploy it over the current site during this pass.

## V2 plan

1. Recompose the homepage around one clear path: encounter the film, understand its emotional premise, join the newsletter.
2. Use the existing production photography and restrained palette. Avoid a component-heavy or card-based marketing layout.
3. Add one cinematic motion system: a subtle parallax drift in the hero/background photography, plus quiet opacity/translate reveals where they help reading order.
4. Make signup prominent near the top and again at the natural end of the page. Keep the separate `/watch` route and its current form field order.
5. Prepare the newsletter form for a real static-site form endpoint through one obvious configuration point. Until an endpoint is supplied, never report a fake successful subscription; show an honest setup/error state.
6. Keep the implementation as plain HTML, CSS, and small vanilla JavaScript files. No framework and no new dependency.

## Responsiveness is a locked constraint

- Preserve `assets/js/layout.js` and its measured `--page-x-live` interpolation table unless a change is backed by measurements and improves every tested viewport.
- Preserve the current wide-container behavior, route paths, anchor IDs, focus states, alt text, and keyboard access.
- Mobile must feel intentionally composed, not like a collapsed desktop page. Keep the signup action visible early, inputs at a comfortable tap size, readable type, and stable image crops.
- Do not use CSS `background-attachment: fixed`; it is unreliable on mobile browsers. Implement parallax with transforms on a dedicated visual layer.
- Use `transform` and `opacity` only for scroll motion. Use `requestAnimationFrame` or `IntersectionObserver`, keep work passive, and avoid layout reads on every frame.
- Reduce the parallax distance on small screens or disable it when that produces the better composition. Respect `prefers-reduced-motion: reduce` with a fully static fallback.
- Prevent horizontal overflow and cumulative layout shift. Motion must not move buttons, inputs, or body copy while the visitor is interacting with them.

## Motion concept to explore

Treat the page like a moving production still. The hero image can drift slowly behind a stable title and signup invitation, creating a small sense of depth. A second photo may echo that motion once later in the page, but there should be no animation on every section, no scroll hijacking, no carousel, and no decorative motion that competes with the form.

## Newsletter behavior

- Primary field: email. Ask for a name only when the chosen provider or messaging plan needs it.
- Provide inline validation, a submitting state, a real success state only after a successful response, and a clear retryable error state.
- Keep labels visible and preserve browser autofill.
- Put provider-specific details in one small configuration file or documented constant so the endpoint can be connected without redesigning the page.
- The watch gate and the general newsletter form may share visual styling, but keep their consent language and intent distinct.

## Required checks

Review the page at 360x800, 390x844, 768x1024, 1440x900, and 1900x1080. At each size confirm:

- no horizontal overflow or clipped text;
- the hero image crop still supports the title;
- navigation and CTA remain usable;
- the newsletter form is visible, readable, keyboard accessible, and honest about submission state;
- the existing responsive side-padding behavior remains intact;
- parallax stays subtle and does not reveal empty image edges;
- reduced-motion mode is fully static.

Finish with a local commit on `redesign/v2-newsletter`, a short before/after note, and the exact remaining input needed to activate real newsletter capture. Do not push or deploy.
