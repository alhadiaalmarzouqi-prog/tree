-- Local development bootstrap (P0). Creates a non-superuser application role and an EMPTY database.
-- It creates NO tables, schema, RLS policies or data. Schema and migrations belong to later phases
-- (P1 onward) and must not be added here.
--
-- Usage (run as the local superuser; choose the password interactively, never commit it):
--   psql -h localhost -U postgres -v app_password="<choose-a-password>" -f infra/postgres/dev-bootstrap.sql
--
-- Note: psql variables are not expanded inside dollar-quoted or single-quoted literals in plain SQL
-- without \gexec; this script uses \gexec so the password is passed as a quoted literal.

SELECT format('CREATE ROLE sovereign_app LOGIN PASSWORD %L NOSUPERUSER NOBYPASSRLS NOCREATEDB NOCREATEROLE', :'app_password')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'sovereign_app')
\gexec

SELECT format('ALTER ROLE sovereign_app WITH LOGIN PASSWORD %L NOSUPERUSER NOBYPASSRLS NOCREATEDB NOCREATEROLE', :'app_password')
WHERE EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'sovereign_app')
\gexec

SELECT 'CREATE DATABASE sovereign_lineage_dev OWNER sovereign_app ENCODING ''UTF8'' TEMPLATE template0'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'sovereign_lineage_dev')
\gexec
