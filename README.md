# España WhatsApp Lead Agent

[![CI](https://img.shields.io/github/actions/workflow/status/Personaz1/espana-whatsapp-lead-agent/ci.yml?branch=master)](https://github.com/Personaz1/espana-whatsapp-lead-agent/actions)
[![Release](https://img.shields.io/github/v/release/Personaz1/espana-whatsapp-lead-agent)](https://github.com/Personaz1/espana-whatsapp-lead-agent/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Production-oriented scaffold for a Spain-focused WhatsApp lead qualification backend.

## What it includes

- FastAPI backend
- WhatsApp webhook endpoint scaffold
- Event ingestion endpoint
- PostgreSQL schema starter
- Docker Compose for local environment
- CI smoke check

## Architecture (MVP)

1. Inbound message from WhatsApp provider (Twilio/Meta)
2. `POST /webhooks/whatsapp` receives payload
3. Payload normalization + validation (TODO in scaffold)
4. Persist lead/event in PostgreSQL (TODO in scaffold)
5. Trigger downstream workflow (qualification / follow-up)

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Health check:

```bash
curl http://localhost:8080/health
```

## API

### `GET /health`
Returns service health.

### `POST /webhooks/whatsapp`
Receives raw provider webhook payload.

Example:

```bash
curl -X POST http://localhost:8080/webhooks/whatsapp \
  -H 'content-type: application/json' \
  -d '{"from":"+34600000000","text":"Hola, me interesa"}'
```

### `POST /api/v1/events`
Stores a normalized event payload (scaffold response for now).

Example:

```bash
curl -X POST http://localhost:8080/api/v1/events \
  -H 'content-type: application/json' \
  -d '{"source":"whatsapp","payload":{"intent":"lead","locale":"es-ES"}}'
```

## Data model starter

See `db/schema.sql`.

- `inbound_events`
- `contacts`

## Security / compliance notes

- Verify webhook signatures before processing production traffic.
- Encrypt sensitive data at rest.
- Implement GDPR-compliant retention/erasure policies for EU users.

## Roadmap

- Provider adapters (Meta + Twilio)
- Idempotency keys and retry safety
- Lead scoring and routing
- Admin visibility for event pipeline

## License

MIT
