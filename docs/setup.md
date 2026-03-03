# Setup Guide

## Prerequisites
- Docker & Docker Compose
- Java 17 + Maven (for local Java development)
- Python 3.11 (for local ingestion development)
- Node 20 (for frontend)

## Environment Variables
Create `.env` in project root:
```env
AVIATIONSTACK_API_KEY=your_key
JWT_SECRET=change-me
```

## Run Unit Tests
```bash
pytest services/flight-ingestion/tests
mvn -f services/flight-analytics/pom.xml test
```

## API Documentation
- Ingestion Swagger: `http://localhost:8000/docs`
- Analytics Swagger: `http://localhost:8080/swagger-ui/index.html`
- GraphQL endpoints:
  - `http://localhost:8000/graphql`
  - `http://localhost:8080/graphql`
