# PostgreSQL — Local environment (P0)

This folder bootstraps a local development database. It creates only an
application role and an EMPTY database. It deliberately creates NO schema,
tables, RLS policies, or migrations — those belong to later phases (P1 onward)
and must not be added here.

## Requirements

- A PostgreSQL server reachable at `localhost:5432` (a service or container).
- A superuser capable of running `psql` (e.g. the local `postgres` role).

## Bootstrap

```
psql -h localhost -U postgres \
  -v app_password="<choose-a-password>" \
  -f dev-bootstrap.sql
```

This creates:
- role `sovereign_app` (LOGIN, NOSUPERUSER, NOBYPASSRLS) — safe defaults for
  the app's non-superuser role, and
- empty database `sovereign_lineage_dev` owned by `sovereign_app`.

## Connection

```
DATABASE_URL=postgres://sovereign_app:<password>@localhost:5432/sovereign_lineage_dev
```

Validate the connection from the backend:

```
cd backend
npm run db:check
```

## Notes

- The role has `NOBYPASSRLS` (RLS is applied in later phases); RLS is not
  configured here.
- Credentials are chosen interactively and must never be committed.
- This server instance is shared with other local services; the script is
  idempotent for the role and database objects.