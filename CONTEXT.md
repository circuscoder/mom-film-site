# MOM site context

Updated 2026-09-09. Public film site; primary goal: MOM newsletter signup.

The site is implemented in plain HTML/CSS/JavaScript. Read `REDESIGN_PLAN.md` for the
current v2 brief and `README.md` for preview, integration, and verification. `prd.md`
retains the original scope/history; its v2 amendment takes precedence for this pass.

V1 is archived at `archive/v1-responsive` and `design-v1-responsive` (commit
`ad0f6a6`). V2 work is on `redesign/v2-newsletter`; local review only, no push/deploy.

Existing photography is supplied locally under `assets/img`; do not replace it with
invented film imagery. `assets/js/layout.js` and the measured container padding are
locked unless new measurements justify a change across every required viewport.

Newsletter activation needs a real provider endpoint, its field contract and accepted
response. Configure `assets/js/signup-config.js`; no provider is connected yet. Watch
access remains unavailable until a separate real trailer delivery mechanism is supplied.

Parent routing: `/factories/website/CONTEXT.md`. Brand/content source routing remains
in the company workspace; this folder is the public site's implementation layer.
