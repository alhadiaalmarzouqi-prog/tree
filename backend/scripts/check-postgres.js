'use strict';

/**
 * Local PostgreSQL connectivity check (P0 foundation only).
 * Reads connection settings from environment variables; never hard-codes credentials.
 * Exit code 0 = server reachable and `SELECT 1` succeeds; 1 = failure.
 *
 * Required env: DATABASE_URL, e.g. postgres://sovereign_app:<password>@localhost:5432/sovereign_lineage_dev
 */
const { Client } = require('pg');

async function main() {
  const connectionString = process.env.DATABASE_URL;
  if (!connectionString) {
    console.error('DB_CHECK_FAILED DATABASE_URL is not set');
    process.exit(1);
  }

  const client = new Client({ connectionString, connectionTimeoutMillis: 5000 });
  try {
    await client.connect();
    const result = await client.query('SELECT version() AS version');
    console.log(`DB_CHECK_OK ${result.rows[0].version.split(' ').slice(0, 2).join(' ')}`);
  } catch (error) {
    console.error(`DB_CHECK_FAILED ${error.message}`);
    process.exitCode = 1;
  } finally {
    await client.end().catch(() => undefined);
  }
}

void main();
