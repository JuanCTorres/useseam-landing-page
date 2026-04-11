# useseam-landing

Landing page and waitlist for [useseam.ai](https://useseam.ai), a coming-soon data sync platform that keeps workspace tools (Notion, Airtable, Linear, Google Sheets) in sync without manual ops work.

## Product decisions

**Launching before the product is ready**
The site collects waitlist signups while the core product is still being built, to validate demand and test positioning early.

**"Coming soon" framing, not a waitlist gate**
The page leads with product messaging rather than just asking for an email. Low signups = signal to revisit the copy or targeting.

**Single waitlist, no segmentation**
No role or use-case dropdown. Keeping friction low maximizes conversion at this stage.

## Technical decisions

**FastAPI + single-file HTML**
No React, no build step, no JS bundler. A single `landing.html` is served as a `FileResponse`. Easy to deploy and modify.

**Flat JSON file for waitlist storage**
Signups go to `waitlist.json` rather than a database. Zero infrastructure, easy to inspect and export, sufficient for expected volume.

**Persistent volume on Fly.io**
`waitlist.json` is written to `/data`, a mounted Fly.io volume, so it survives deploys and machine restarts.

**Resend for email notifications**
Each signup fires a notification email via [Resend](https://resend.com). Failures are caught and ignored so a Resend outage never blocks a signup.

**Fly.io with auto-stop/auto-start**
Runs on a single shared-CPU 512 MB machine in `ewr`. The machine sleeps when idle and wakes on request, keeping hosting costs near zero.
