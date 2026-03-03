# AeroStream Architecture

## Event-Driven Topology
```mermaid
flowchart LR
  A[Aviationstack API] --> B[Flight Ingestion Service\nFastAPI]
  B -->|flight_updates| K[(Kafka)]
  K --> C[Flight Analytics Service\nSpring Boot]
  C --> D[(PostgreSQL)]
  C --> E[(MongoDB)]
  C -->|REST/GraphQL| F[API Gateway/Ingress]
  F --> G[React Dashboard]
  B --> H[Prometheus]
  C --> H
  H --> I[Grafana]
```

## Kafka Schemas
- `flight_updates`
  - `event_id`, `flight_number`, `departure_airport`, `arrival_airport`, `delay_minutes`, `status`, `route_key`, `ingested_at`
- `delay_events`
  - subset of delayed flights with severity flags.
- `route_performance`
  - route-level aggregates (`avg_delay`, `reliability_score`, `window_start`, `window_end`).
