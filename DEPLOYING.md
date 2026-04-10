# Deploying

The app runs on [Fly.io](https://fly.io) as `useseam-landing`.

## Deploy

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

- [flyctl](https://fly.io/docs/hands-on/install-flyctl/) installed
- Authenticated: `fly auth login`
