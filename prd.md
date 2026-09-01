# MOM Site — PRD

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
column marketing page). Dark mode is the **default** (a user decision, reversing the source's
light-default) — the same token set the source calls its dark-mode block becomes MOM's `:root`.

### Color (dark default)

| Role | Value | Used for |
| --- | --- | --- |
| Background | `#14110d` | page background |
| Ink (text) | `#f4f1ea` | body text |
| Dim | `#4a453c` | inactive states |
| Accent | `#e8674f` | links, CTA, hover/focus states, leader/rule accents |
| Rule / secondary text | `#948a79` | captions, secondary text, hint text |
| Panel | `#1e1a15` | card/panel surface (e.g. the form container) |

A light variant exists in the source tokens (`#f4f1ea` bg / `#14110d` ink / `#c0392b` accent) —
not used for v1 (dark is the fixed default per user decision), but kept available at
`design-system-export/tokens/colors.css` if a toggle is ever wanted later.

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
