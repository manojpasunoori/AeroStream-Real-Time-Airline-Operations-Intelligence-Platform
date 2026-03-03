"""Generate mock Kafka flight events for integration testing."""
import json
import random
from datetime import datetime, timezone
from uuid import uuid4

ROUTES = [("JFK", "LAX"), ("LHR", "CDG"), ("DXB", "SIN")]


def build_event() -> dict:
    dep, arr = random.choice(ROUTES)
    delay = random.randint(0, 90)
    return {
        "event_id": str(uuid4()),
        "flight_number": f"AS{random.randint(100, 999)}",
        "airline": "AeroStream Air",
        "departure_airport": dep,
        "arrival_airport": arr,
        "delay_minutes": delay,
        "status": "delayed" if delay > 15 else "active",
        "route_key": f"{dep}-{arr}",
        "ingested_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    print(json.dumps([build_event() for _ in range(10)], indent=2))
