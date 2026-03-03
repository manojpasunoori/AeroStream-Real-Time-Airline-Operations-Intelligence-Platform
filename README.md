# ✈️ AeroStream — Real-Time Airline Operations Intelligence Platform

<div align="center">

![Platform](https://img.shields.io/badge/Platform-Cloud%20Native-0ea5e9)
![Architecture](https://img.shields.io/badge/Architecture-Event%20Driven-22c55e)
![Backend](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Spring%20Boot-f97316)
![Data](https://img.shields.io/badge/Data-Kafka%20%7C%20PostgreSQL%20%7C%20MongoDB-a855f7)
![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20TypeScript-2563eb)
![Observability](https://img.shields.io/badge/Observability-Prometheus%20%2B%20Grafana-14b8a6)

**A production-style, distributed aviation intelligence platform that ingests real-time flight feeds, streams events, computes KPIs, and surfaces analytics through REST, GraphQL, and an interactive dashboard.**

</div>

---

## 🌟 Why AeroStream (Recruiter Snapshot)

AeroStream demonstrates **real-world software engineering depth** across system design, backend services, data engineering, frontend visualization, cloud operations, and DevOps automation.

### What this project proves
- ✅ **Distributed systems understanding** (event-driven architecture with Kafka topics and consumer groups).
- ✅ **Polyglot backend design** (Python ingestion + Java analytics microservices).
- ✅ **Data platform literacy** (PostgreSQL for structured analytics, MongoDB for flexible config/cache patterns).
- ✅ **API craftsmanship** (versioned REST + GraphQL + OpenAPI + JWT security).
- ✅ **Cloud-native deployment mindset** (Docker, Kubernetes manifests, EKS/AKS overlays, ingress/TLS).
- ✅ **Operational excellence** (Prometheus metrics, Grafana dashboards, CI/CD workflows).

---

## 🧭 Table of Contents

1. [Business Problem](#-business-problem)
2. [Solution Overview](#-solution-overview)
3. [High-Level Architecture](#-high-level-architecture)
4. [Core Features](#-core-features)
5. [Technology Stack](#-technology-stack)
6. [Data & Event Contracts](#-data--event-contracts)
7. [Repository Structure](#-repository-structure)
8. [Local Development Setup](#-local-development-setup)
9. [API Guide (REST + GraphQL)](#-api-guide-rest--graphql)
10. [Security Design](#-security-design)
11. [Observability](#-observability)
12. [Kubernetes Deployment (EKS/AKS)](#-kubernetes-deployment-eksaks)
13. [CI/CD Pipelines](#-cicd-pipelines)
14. [Testing Strategy](#-testing-strategy)
15. [Roadmap](#-roadmap)
16. [How to Talk About This Project in Interviews](#-how-to-talk-about-this-project-in-interviews)

---

## 🧩 Business Problem

Airline operations teams require up-to-the-minute visibility into flight movements, delays, and route reliability to optimize turnaround times, gate allocation, disruption management, and customer communication.

Traditional reporting stacks are often **batch-oriented** and fail to provide actionable intelligence in real time.

---

## 🚀 Solution Overview

AeroStream is a **real-time airline intelligence platform** powered by:
- **Aviationstack API** as upstream flight feed (requires API key).
- **Flight Ingestion Service (FastAPI)** for polling + normalization.
- **Apache Kafka** for event streaming.
- **Flight Analytics Service (Spring Boot)** for KPI computation.
- **PostgreSQL + MongoDB** for analytics persistence and dynamic configuration.
- **React + TypeScript frontend** for live dashboards and exploratory search.

---

## 🏗️ High-Level Architecture

```mermaid
flowchart LR
  A[Aviationstack API] --> B[Flight Ingestion Service / FastAPI]
  B -->|flight_updates| K[(Apache Kafka)]
  K --> C[Flight Analytics Service / Spring Boot]
  C --> P[(PostgreSQL)]
  C --> M[(MongoDB)]
  C -->|REST + GraphQL| G[API Gateway / Ingress TLS]
  G --> F[React Dashboard]
  B --> O[Prometheus]
  C --> O
  O --> R[Grafana]
```

### Architectural style
- **Microservices + Event-Driven + Cloud-Native**
- **Asynchronous pipeline** for decoupling ingestion and analytics
- **Multi-cloud deployability** through Kubernetes manifests and overlays

---

## 🎯 Core Features

### 1) Real-time flight ingestion
- Polls Aviationstack flight endpoint.
- Normalizes heterogeneous upstream payload fields.
- Publishes canonical flight events to Kafka.

### 2) Stream analytics and KPI computation
- Consumes `flight_updates` events.
- Computes delay and route reliability KPI.
- Persists computed metrics in PostgreSQL.
- Supports dynamic route threshold configuration model in MongoDB.

### 3) API surface for clients
- **REST** endpoints (versioned under `/api/v1`).
- **GraphQL** endpoints for flexible querying.
- **Swagger/OpenAPI** docs support.

### 4) Frontend intelligence dashboard
- Live KPI chart visualization.
- Search by flight number or route/airport code.
- Tabular operational visibility for quick triage.

### 5) Ops & cloud readiness
- Dockerized services.
- Kubernetes manifests for EKS and AKS.
- ConfigMaps and Secrets.
- Prometheus + Grafana monitoring.

---

## 🧰 Technology Stack

| Layer | Tools |
|---|---|
| Ingestion | Python, FastAPI, HTTPX, Pydantic |
| Streaming | Apache Kafka |
| Analytics | Java 17, Spring Boot, Spring Kafka, Spring Data JPA, Spring GraphQL |
| Datastores | PostgreSQL, MongoDB |
| Frontend | React, TypeScript, Recharts, Axios |
| Infra | Docker, Docker Compose, Kubernetes, NGINX Ingress |
| Security | JWT, OAuth2 Resource Server, TLS ingress |
| Observability | Prometheus, Grafana, Micrometer |
| CI/CD | GitHub Actions, Azure DevOps Pipelines |

---

## 📦 Data & Event Contracts

### Kafka topics
- `flight_updates` → canonical per-flight updates from ingestion service.
- `delay_events` → delayed-flight focused event stream.
- `route_performance` → aggregated route-level KPI stream.

### Canonical event example (`flight_updates`)
```json
{
  "event_id": "4f2f1f11-f8d6-4b07-b5c5-8f5d2d83c1d0",
  "flight_number": "AA100",
  "airline": "American Airlines",
  "departure_airport": "JFK",
  "arrival_airport": "LAX",
  "delay_minutes": 18,
  "status": "active",
  "route_key": "JFK-LAX",
  "ingested_at": "2026-01-01T10:30:00Z"
}
```

### KPI baseline formula
```text
reliability_score = max(0, 100 - delay_minutes * 1.5)
```

---

## 🗂️ Repository Structure

```text
.
├── services/
│   ├── flight-ingestion/     # FastAPI ingestion microservice
│   └── flight-analytics/     # Spring Boot analytics microservice
├── frontend/                 # React + TypeScript web app
├── infra/
│   ├── gateway/              # NGINX API gateway config
│   ├── k8s/                  # Base + EKS/AKS overlays
│   ├── observability/        # Prometheus + Grafana assets
│   └── scripts/              # bootstrap + topic creation scripts
├── docs/                     # architecture + setup + system design
├── scripts/                  # mock data generation
├── tests/                    # integration test plan
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Local Development Setup

> Prerequisites: Docker, Docker Compose, Python 3.11+, Java 17+, Node 20+

### 1) Configure environment
Create `.env` in project root:

```bash
cp .env.example .env
# then set AVIATIONSTACK_API_KEY and JWT_SECRET
```

### 2) Launch full stack
```bash
docker compose up --build
```

### 3) (Optional) Create Kafka topics manually
```bash
./infra/scripts/create-topics.sh
```

### 4) Open local services
- Frontend: `http://localhost:3000`
- Ingestion API docs: `http://localhost:8000/docs`
- Analytics API docs: `http://localhost:8080/swagger-ui/index.html`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

---

## 🔌 API Guide (REST + GraphQL)

### Ingestion service (FastAPI)
**Base:** `http://localhost:8000/api/v1`

- `POST /ingest` → polls Aviationstack, normalizes, emits Kafka events.
- `GET /health` → service health.
- `GET /graphql` / `POST /graphql` → GraphQL endpoint.

Example:
```bash
curl -X POST "http://localhost:8000/api/v1/ingest?limit=25" \
  -H "Authorization: Bearer <jwt-token>"
```

### Analytics service (Spring Boot)
**Base:** `http://localhost:8080/api/v1/analytics`

- `GET /` → list all KPI records.
- `GET /flight/{flightNumber}` → KPI by flight.
- `GET /route/{routeKey}` → KPI by route.
- GraphQL endpoint: `POST /graphql`

GraphQL sample:
```graphql
query {
  analyticsByFlight(flightNumber: "AA100") {
    flightNumber
    routeKey
    delayMinutes
    reliabilityScore
    status
  }
}
```

---

## 🔐 Security Design

- JWT validation on ingestion and analytics APIs.
- OAuth2 resource-server style config for Spring service.
- HTTPS/TLS termination at ingress/API gateway.
- Secrets kept in Kubernetes `Secret` resources.
- Configuration externalized via `ConfigMap`.

---

## 📈 Observability

### Metrics
- Ingestion service: `/metrics`
- Analytics service: `/actuator/prometheus`

### Monitoring
- Prometheus scrapes both services.
- Grafana provisions dashboard for request and JVM visibility.

### Why this matters
- Faster incident detection.
- Better SLO tracking.
- Easier capacity planning and performance tuning.

---

## ☁️ Kubernetes Deployment (EKS/AKS)

### Apply AWS EKS overlay
```bash
kubectl apply -k infra/k8s/eks
```

### Apply Azure AKS overlay
```bash
kubectl apply -k infra/k8s/aks
```

### Included assets
- Namespace
- ConfigMap + Secret
- Deployments + Services
- Ingress with TLS host routing

---

## 🔁 CI/CD Pipelines

### GitHub Actions
- **CI workflow**: install dependencies, run tests, build frontend.
- **Docker publish workflow**: build/push images to GHCR on tags.

### Azure DevOps
- Multi-stage pipeline:
  1. Build and test
  2. Deploy to EKS
  3. Deploy to AKS

---

## 🧪 Testing Strategy

- **Unit tests**
  - Python (`pytest`) for normalization logic.
  - Java (`JUnit`) for KPI reliability scoring.
- **Integration plan**
  - End-to-end validation across ingestion → Kafka → analytics → databases → API responses.
- **Mock data tooling**
  - `scripts/generate_mock_data.py` for realistic synthetic event generation.

Run tests:
```bash
pytest services/flight-ingestion/tests
mvn -f services/flight-analytics/pom.xml test
```

---

## 🗺️ Roadmap

- [ ] Add schema registry (Avro/Protobuf) for strongly governed event contracts.
- [ ] Implement dead-letter queue + retry strategy for malformed events.
- [ ] Add route-level windowed aggregations in analytics service.
- [ ] Add RBAC policies for fine-grained role-based API access.
- [ ] Add OpenTelemetry tracing across services.
- [ ] Add map-based UI for geospatial flight visualization.

---

## 💼 How to Talk About This Project in Interviews

Use this concise pitch:

> “I built AeroStream, a cloud-native event-driven analytics platform for airline operations. I used FastAPI to ingest live flight data from Aviationstack, Kafka for streaming, Spring Boot for KPI analytics, and Postgres/Mongo for persistence. I exposed both REST and GraphQL APIs, built a React dashboard for operational visibility, and productionized the stack with Docker, Kubernetes, CI/CD pipelines, and Prometheus/Grafana observability.”

### Recruiter-friendly highlights
- End-to-end ownership from architecture to deployment.
- Practical tradeoffs in consistency, throughput, and observability.
- Hands-on multi-cloud deployment readiness (AWS + Azure).

---

## 📚 Additional Documentation

- `docs/architecture.md`
- `docs/system-design.md`
- `docs/setup.md`

---

## 🤝 Contributing

1. Create a feature branch.
2. Commit changes with clear messages.
3. Add/adjust tests.
4. Open a PR with architecture and rollout notes.

---

## 📄 License

This repository is intended for educational, portfolio, and demonstration use.
