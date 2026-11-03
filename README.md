# Sovereign Lineage Platform

Family tree and kinship discovery platform. The authoritative source documents
(analysis, decisions, and the M0 kinship reference) are under `project-docs/`
(Arabic) and `project-docs-en/` (English, incl. the M0 regression harness).

## Stack (owner decision DD-03)

- **Backend:** NestJS REST API, modular monolith (`backend/`)
- **Client:** Flutter (`mobile/`)
- **Database:** PostgreSQL (see `infra/postgres/`)

## Layout

| Path | Contents |
|---|---|
| `backend/` | NestJS API: source, unit + e2e tests, lint/typecheck, build, Postgres connectivity script |
| `mobile/` | Flutter client skeleton (pubspec, lib, smoke test) |
| `infra/postgres/` | Local PostgreSQL bootstrap (role + empty DB; no schema) |
| `.github/workflows/ci.yml` | CI (backend + Postgres, mobile, M0 regression) |
| `project-docs/`, `project-docs-en/` | Source docs, decisions, M0 reference/harness |
| `project-docs-en/P0-FOUNDATION-EXECUTION-REPORT.md` | P0 execution record (this phase) |

## Backend quick start

```
cd backend
npm install
npm run lint        # ESLint
npm run typecheck   # tsc --noEmit
npm test            # Jest unit tests
npm run test:e2e    # Jest e2e (health route)
npm run build       # nest build -> dist/
npm run db:check    # validate DATABASE_URL (see backend/.env.example)
```

## Mobile quick start

```
cd mobile
flutter pub get
flutter analyze
flutter test
```

## M0 regression

```
python project-docs-en/verification/m0-recalc/m0_verify.py
python project-docs-en/verification/m0-recalc/m0_mutation_check.py
```

## Phase

Current phase: **P0 (Repository and Foundation Tooling)**. The owner-directive
that moves the independent reviews into the implementation lifecycle is in
`project-docs-en/m3-review/OWNER-DIRECTIVE-2026-11-03-REVIEW-LIFECYCLE.md`.
No P1+ work is in progress. Verification status and remaining owner actions are in
`project-docs-en/P0-FOUNDATION-EXECUTION-REPORT.md` (backend lint/typecheck/build/test/e2e
and M0 are verified; Flutter `pub get`/`analyze`/`test`, PostgreSQL live bootstrap,
GitHub Actions execution, and `npm audit` detail are NOT yet executed here).
