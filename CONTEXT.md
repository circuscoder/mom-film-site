# MOM Site

Last updated: 2026-08-31

## What this workspace is for

The public website for the MOM film — separate from `/factories/mom-content`'s social/newsletter
*content* pipeline, which produces posts and articles but has no site of its own to publish them
on. Primary goal, per explicit user request: let visitors sign up for the MOM newsletter. Other
site sections (film info, updates, etc.) are open — not scoped yet.

Read `prd.md` for why this exists and current scope. No `spec.md` yet — no build has started, so
there's no real process to write a contract for.

## Status

**Genuinely empty as of 2026-08-31.** Folder just created; no analysis, briefing doc, PRD, or code
exists yet. Per `icm-website-builder` (the methodology this build should follow — see
`/library/icm-methodology/icm-website-builder/SKILL.md`), the next real steps are:

1. Analyze a reference site (if one exists) in Claude **chat**, not here — produces a markdown
   briefing doc written for Claude Code to read.
2. Drop that briefing doc in this folder.
3. From here, write the first Claude Code prompt: structure, scope, deploy target (GitHub Pages
   is the methodology's default), tech preference, ending on alignment questions before any file
   gets created.
4. Answer those questions, then request a PRD (design tokens, color, type, layout, delivery
   checklist) before any implementation code is written.

Don't skip straight to scaffolding code without that sequence — see the skill's "Common mistakes"
section for why.

## Folders

Not built out yet — single-file workspace until the process above produces a briefing doc and PRD.

## Open questions

- No reference site chosen yet — is there an existing site (a competitor, a prior MOM page, a
  visual reference) to analyze in Step 1, or is this a from-scratch design?
- Newsletter signup needs a backend (Substack? Mailchimp? something else?) — `/factories/mom-content`
  already has a Substack presence (`substack-ghostwriting` skill); worth checking whether signup
  should route there before picking a separate email tool.
- Domain and hosting — GitHub Pages is the methodology's default deploy target; not yet confirmed
  as the actual choice.
- Whether this site reuses `/factories/circus-brand`'s brand material or needs its own MOM-specific
  visual identity (MOM's identity work so far lives in `/library/mom-knowledge-engine/core_knowledge`,
  not `circus-brand`, which is explicitly non-MOM).
