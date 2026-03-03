from datetime import datetime
from uuid import uuid4
import httpx
from fastapi import APIRouter, Depends
from app.api.auth import require_token
from app.core.config import settings
from app.kafka.producer import KafkaProducer
from app.models.flight import FlightEvent

router = APIRouter()
producer = KafkaProducer()


def _normalize_flight(raw: dict) -> FlightEvent:
    dep = raw.get("departure", {})
    arr = raw.get("arrival", {})
    flight = raw.get("flight", {})
    airline = raw.get("airline", {})

    scheduled = dep.get("scheduled")
    actual = dep.get("actual")
    scheduled_dt = datetime.fromisoformat(scheduled.replace("Z", "+00:00")) if scheduled else None
    actual_dt = datetime.fromisoformat(actual.replace("Z", "+00:00")) if actual else None
    delay = dep.get("delay") or 0

    return FlightEvent(
        event_id=str(uuid4()),
        flight_number=flight.get("iata", "UNKNOWN"),
        airline=airline.get("name", "UNKNOWN"),
        departure_airport=dep.get("iata", "UNK"),
        arrival_airport=arr.get("iata", "UNK"),
        scheduled_departure=scheduled_dt,
        actual_departure=actual_dt,
        delay_minutes=delay,
        status=raw.get("flight_status", "unknown"),
        route_key=f"{dep.get('iata', 'UNK')}-{arr.get('iata', 'UNK')}",
        ingested_at=datetime.utcnow(),
    )


@router.post("/ingest", dependencies=[Depends(require_token)])
async def ingest_flights(limit: int = 25) -> dict:
    params = {"access_key": settings.aviationstack_api_key, "limit": limit}
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(f"{settings.aviationstack_base_url}/flights", params=params)
        response.raise_for_status()
    payload = response.json()
    count = 0
    for raw in payload.get("data", []):
        event = _normalize_flight(raw)
        producer.publish(settings.kafka_topic_flight_updates, event.model_dump(mode="json"))
        count += 1
    return {"published": count, "topic": settings.kafka_topic_flight_updates}


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.app_name}
