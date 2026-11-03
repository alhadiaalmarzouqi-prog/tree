# Sovereign Lineage — Backend (NestJS)

REST API skeleton for the Sovereign Lineage Platform.

## Requirements
- Node.js >= 22

## Install
```
npm install
```

## Scripts
```
npm run lint       # ESLint (src, test, scripts)
npm run typecheck  # TypeScript typecheck
npm test           # Jest unit tests
npm run test:e2e   # Jest end-to-end test (health route)
npm run build      # nest build -> dist/
npm run db:check   # connect to PostgreSQL via DATABASE_URL
```

## Configuration
Copy `backend/.env.example` to `backend/.env` and set `PORT` and `DATABASE_URL`.
Never commit `.env`.

## Health endpoint
```
GET /api/v1/health
```

Example response: `{ "status": "ok", "service": "sovereign-lineage-backend" }`