# useseam-landing

Landing page and waitlist for [useseam.ai](https://useseam.ai) — a coming-soon data sync platform that keeps workspace tools (Notion, Airtable, Linear, Google Sheets) in sync without manual ops work.

---

## Product decisions

**Launching a landing page before the product is ready**

The site is live and collecting waitlist signups while the core product is still being built. The goal is to validate demand early, accumulate a list of interested users to reach out to at launch, and get real signal on whether the positioning resonates — before investing further in product.

**"Coming soon" framing, not a waitlist-only gate**

The page leads with product messaging (pain points, vision) rather than just asking for an email. This is deliberate: the landing page doubles as a positioning test. If the copy resonates, that's signal the framing is right; if signups are low, the copy or audience targeting may need adjustment.

**Single waitlist, no segmentation**

There's no role or use-case dropdown on signup. Keeping friction minimal maximizes conversion at this stage. Segmentation can come later when onboarding real users.

---

## Technical decisions

**FastAPI + single-file HTML, no frontend framework**

The page is intentionally static-first. There's no React, no build step, no JS bundler. A single `landing.html` file is served as a `FileResponse` from FastAPI. This makes the project trivial to deploy, read, and modify — appropriate for a landing page that needs to move fast and stay simple.

**Three CSS themes, one HTML file**

Three stylesheets (`landing.css`, `landing-minimal.css`, `landing-bold.css`) are swappable by changing a single `<link>` tag. This made it cheap to explore visual directions without branching the HTML. The bold dark theme is currently active.

**SQLite-via-file waitlist storage (waitlist.json)**

Signups are stored in a flat JSON file rather than a database. This is intentional for this stage: zero infrastructure to set up, easy to inspect and export, and sufficient for the expected volume. If the list grows to a scale where this matters, migrating to a real database is straightforward.

**Persistent volume on Fly.io for waitlist durability**

`waitlist.json` is written to `/data`, which is a mounted Fly.io volume (`fly.toml` → `[[mounts]]`). This survives deploys and machine restarts. Without this, the file would be lost on every deploy since the container filesystem is ephemeral.

**Resend for email notifications**

Each new signup fires a notification email to the owner via [Resend](https://resend.com). Resend was chosen over SendGrid/Mailgun for its simpler API and generous free tier. The notification is fire-and-forget (failures are caught and ignored) so a Resend outage never blocks a user from signing up.

**Fly.io with auto-stop/auto-start**

The app runs on a single shared-CPU 512 MB Fly machine in `ewr` (Newark). `auto_stop_machines = 'stop'` and `min_machines_running = 0` mean the machine sleeps when idle and wakes on the first request. This keeps hosting costs near zero for low-traffic periods while remaining always-reachable.

---

## Local setup

```bash
cp .env.example .env
# fill in RESEND_API_KEY and NOTIFY_EMAIL

pip install -r requirements.txt
python serve.py
```

The app runs at `http://localhost:8080`.

## Deploying

See [DEPLOYING.md](DEPLOYING.md) for Fly.io deploy instructions.
