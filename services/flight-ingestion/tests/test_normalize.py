import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.api.routes import _normalize_flight


def test_normalize_flight_maps_required_fields():
    raw = {
        "departure": {"iata": "JFK", "scheduled": "2024-10-10T10:00:00+00:00", "actual": "2024-10-10T10:15:00+00:00", "delay": 15},
        "arrival": {"iata": "LAX"},
        "flight": {"iata": "AA100"},
        "airline": {"name": "American Airlines"},
        "flight_status": "active",
    }
    event = _normalize_flight(raw)
    assert event.route_key == "JFK-LAX"
    assert event.delay_minutes == 15
    assert event.flight_number == "AA100"
