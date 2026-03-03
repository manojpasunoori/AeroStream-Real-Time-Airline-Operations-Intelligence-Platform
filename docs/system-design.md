# System Design Details

## Data Model Design
- **PostgreSQL** stores immutable KPI snapshots per processed flight event.
- **MongoDB** stores dynamic route configuration and caching metadata.

## Analytics KPI Logic
- Delay KPI = direct mapped `delay_minutes` from ingestion event.
- Route reliability score = `max(0, 100 - delay_minutes * 1.5)` in current baseline model.
- Extended scoring can include historical route confidence and cancellation penalties.

## Observability Setup
- FastAPI service exposes `/metrics` via Prometheus Instrumentator.
- Spring Boot service exposes `/actuator/prometheus` via Micrometer.
- Grafana dashboard includes request rate and JVM memory panels.

## Deployment Strategy
- Docker images built in GitHub Actions and pushed to GHCR.
- Kubernetes manifests separated into reusable base + cloud overlays.
- Azure DevOps pipeline orchestrates test/build and EKS/AKS rollout stages.
