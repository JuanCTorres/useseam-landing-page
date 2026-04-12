# Deploying

The app runs on [Fly.io](https://fly.io) as `useseam-landing`.

## Deploy

### Via GitHub Actions (recommended)

Trigger the workflow manually from the `main` branch:

```bash
gh workflow run deploy --ref main
```

Or via the GitHub UI: **Actions → Deploy → Run workflow**.

Requires a `FLY_API_TOKEN` secret set in the repo (see Prerequisites below).

### Locally

```bash
fly deploy
```

This builds the Docker image and deploys to the `ewr` region. Takes ~1 minute.

## Logs

```bash
fly logs
```

## SSH into the machine

```bash
fly ssh console
```

## Environment variables / secrets

```bash
# Set a secret
fly secrets set KEY=value

# List secrets
fly secrets list
```

## Prerequisites

**Local deploys:**
- [flyctl](https://fly.io/docs/hands-on/install-flyctl/) installed
- Authenticated: `fly auth login`

**GitHub Actions:**
- `FLY_API_TOKEN` secret added to the repo (Settings → Secrets and variables → Actions)
- Generate the token with: `fly tokens create deploy -x 999999h`
