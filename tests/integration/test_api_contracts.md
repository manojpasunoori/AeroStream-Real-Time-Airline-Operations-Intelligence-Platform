# Integration Test Plan

1. Start stack with `docker compose up --build`.
2. Call ingestion endpoint with JWT and assert `flight_updates` topic receives events.
3. Verify analytics service stores derived KPIs in PostgreSQL and route threshold config in MongoDB.
4. Verify REST and GraphQL queries return expected KPI payload.
