# MOM Site — PRD

## V2 amendment (2026-09-09)

`REDESIGN_PLAN.md` supersedes the historical v1 requirements below for this pass.
The homepage now prioritizes newsletter signup in the hero and footer. It preserves
the existing photography, system font, light neutral palette with yellow accent,
routes/anchors, and measured `layout.js` spacing. Photo parallax is a progressive
desktop enhancement with a static mobile/reduced-motion fallback.

No fake signup or trailer success is allowed. Newsletter integration is prepared in
`assets/js/signup-config.js` but needs an actual provider endpoint/contract. `/watch/`
preserves first-name, last-name, email order and reports unavailable access until
real delivery is connected. Placeholder contact/support links are removed.

The required deliverable is a locally committed v2 on `redesign/v2-newsletter`, not
a deployment. See `README.md` and `REDESIGN_REVIEW.md` for the current implementation
and validation. The original v1 description below is retained as planning history.

Last updated: 2026-09-01

## Problem / why this exists

MOM's content pipeline (`/factories/mom-content`) produces social clips, newsletters, and Substack
articles, but there is nowhere for a new visitor to land and actually subscribe outside of
whatever platform (Substack, social) they first encountered the content on. A public MOM site
gives the project a home and a direct newsletter signup path it doesn't currently own.

## Who it's for

Prospective MOM audience members arriving from social/word-of-mouth, who want to learn about the
film and sign up for updates.

## Reference analysis

[forward.movie](https://www.forward.movie/) (Squarespace) — analyzed 2026-09-01 via a live
walkthrough (playwright) plus a raw-HTML pull (scrapling). Structural pattern borrowed: a single
scrolling homepage (hero → synopsis → embedded trailer → filmmakers → contact/signup) plus a
**separate, dedicated page** for the gated watch flow (`/watch-the-film-email` there) rather than
a modal or inline gate — name/email form, one-line disclosure of why the email is required, submit
reveals/sends the film link. MOM's site borrows this shape; screenings/touring info is dropped
(not applicable yet).

## Scope

**In scope (v1):**

- [ ] Single-page home: hero (title, logline, "Watch the Trailer" CTA), synopsis (from
      `mom_bible.md`), filmmakers (Shannon Lucio — writer/director; Charlie Hofheimer — producer),
      footer contact. The trailer itself is **not** embedded/public on the homepage — per the
      user, the Vimeo trailer is the gated item (unlike forward.movie, where the trailer is public
      and only the full film is gated).
- [ ] Separate `/watch` page: name/email form gates the trailer. Real-world purpose (per the user):
      the Vimeo link may genuinely be private/unlisted, so this is real access control, not just
      UX — submit → (eventually) an email with the link + the address captured for the newsletter.
      **Placeholder mechanism for v1** — client-side only, reveals the link on submit, does not
      actually send email or capture addresses yet. Swap for a real backend (Substack embed, or a
      form service) before public launch.
- [ ] Dark-mode-default visual system built from the vendored `letterform-cartographer` design
      tokens (see Design tokens below)

**Out of scope (for now):**

- [ ] Real email capture/newsletter backend — placeholder only until decided
- [ ] Full film marketing site (press kit, gallery, screenings/touring)
- [ ] E-commerce or ticketing

## What done looks like

A live, deployed site (GitHub Pages) matching the scope above, built through the skill's full
sequence — reference analysis (done), this PRD, build, review, deploy.

## Design tokens

Source: `/library/web-scraping/scrapling`'s sibling vendored asset —
`arm/factories/website/letterform-cartographer/design-system-export/tokens/` (a real Claude Design
export, confirmed with the user 2026-09-01) — **tokens only**, not that project's own layout/
components (that project is a 3-column documentation-reader tool; MOM's site is a simple single-
column marketing page). Light is the **default** (the source's own light-default block) — flipped
from an initial dark-default choice back to light on 2026-09-01, to read closer to forward.movie's
own light/dark-banded rhythm.

### Color (light default)

| Role | Value | Used for |
| --- | --- | --- |
| Background | `#f4f1ea` | page background |
| Ink (text) | `#14110d` | body text |
| Dim | `#b9b2a4` | inactive states |
| Accent | `#c0392b` | links, CTA, hover/focus states, leader/rule accents |
| Rule / secondary text | `#655d50` | captions, secondary text, hint text |
| Panel | `#e8e3d8` | alternating section band, card/panel surface |

A dark variant exists in the source tokens (`#14110d` bg / `#f4f1ea` ink / `#e8674f` accent) —
not used for v1 (light is the fixed default per user decision), but kept available at
`design-system-export/tokens/colors.css` if a toggle is ever wanted later.

### Hero photo

A real behind-the-scenes production still (`assets/img/hero-bts.jpg`, from the MOM Dropbox —
`01_SOURCE_LIBRARY/03_PHOTOGRAPHS/Sissy Short Photos/IMG_5272.jpeg`, the proof-of-concept short's
production photos) is used full-bleed in the hero, with a dark gradient scrim for text legibility —
mirrors forward.movie's own hero pattern. Most files in that Dropbox folder are location-scouting
reference shots (some with technical overlays burned in) rather than usable photography; this one
was hand-picked as a clean, evocative exception. Filmmaker photos for both Shannon Lucio and
Charlie Hofheimer were provided directly by the user (2026-09-01) — the earlier Wikimedia Commons
CC BY-SA photo of Shannon was swapped out once a better one was available.

### Typography

System stack only — no commercial/licensed webfonts (matches both the source tokens' own
constraint and the Circus brand guide's flag that Futura/Gill Sans need a free alternative before
any web build):

- Body/UI: `"Helvetica Neue", Helvetica, Arial, sans-serif`
- Monospace (if needed — form labels, fine print): `ui-monospace, SFMono-Regular, Consolas, monospace`

Scale is dense/small per the source (11–19px range, generous letter-spacing on labels) — MOM's
hero/title treatment gets more room than the source's utilitarian UI (this is a film site, not a
documentation tool), but stays within the same restrained, non-decorative register. Confirm actual
pixel sizes per section during build against `typography-fundamentals` guidance (hierarchy,
line-length, contrast) rather than copying the source's UI-density scale verbatim.

### Motion, spacing, shape

- Motion: short (.15–.25s) `ease` opacity/color fades only — no scale/bounce/position transitions.
- Corners: nearly square (3–18px depending on element) — nothing pill-shaped.
- Shadows: none, except the one drawer-shadow token in the source (not expected to be needed here).
- Spacing: reuse the source's rhythm (tight, 16–24px padding) as a starting point, adapted to a
  single-column layout rather than the source's fixed 3-column grid.

## Delivery checklist

- [ ] Hero section (film title, logline, primary CTA linking to `/watch`)
- [ ] Synopsis section (short synopsis from `mom_bible.md` §3)
- [ ] Filmmakers section (Shannon Lucio, Charlie Hofheimer)
- [ ] Footer contact — **placeholder** email until a real contact address is provided
- [ ] `/watch` page — name/email form, placeholder gate logic, disclosure line, **placeholder**
      Vimeo link until a real URL is provided
- [ ] Dark-default token system applied (color/type/spacing/motion per above)
- [ ] Responsive (single column collapses cleanly on mobile — no 3-column grid to worry about)
- [ ] Checked against `web-design-guidelines`/`design-taste-frontend` (no AI-tell defaults) and
      `typography-fundamentals` (type hierarchy/scale) before calling the build done
- [ ] `.gitignore` in place, pushed to a new GitHub repo, GitHub Pages enabled
- [ ] Live URL confirmed working, asset paths correct post-deploy

## Open questions

- **Vimeo trailer URL** — not found in the MOM knowledge base or Dropbox DAM (both are empty
  templates as of 2026-09-01); placeholder embed until provided.
- **Contact email** — not yet decided; placeholder (`hello@mom-film.example` or similar clearly-
  marked placeholder) until provided.
- Real newsletter backend (Substack vs. form service) — deferred past v1, see Scope.
- Domain — not yet decided; GitHub Pages' default `*.github.io` URL until a custom domain is chosen.
