# MOM — Film Site

Public site for the film **MOM**: a hero/synopsis/filmmakers page, plus a `/watch` page that
gates the Vimeo trailer behind a name/email form. Draft — expect frequent changes.

- Plain HTML/CSS, no build step. Static, deployable as-is via GitHub Pages (source: `/ (root)`).
- Visual system: see [`prd.md`](prd.md) — dark-default palette and type tokens vendored from a
  Claude Design export (`arm/factories/website/letterform-cartographer`), system fonts only.
- The `/watch` email gate is a **client-side placeholder** for v1 — it reveals the trailer link on
  submit but doesn't send email or capture addresses yet. See `prd.md`'s Open questions.

Planning docs: [`CONTEXT.md`](CONTEXT.md) (what/why), [`prd.md`](prd.md) (scope, design tokens,
delivery checklist).
