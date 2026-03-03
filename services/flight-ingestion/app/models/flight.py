from datetime import datetime
from pydantic import BaseModel


class FlightEvent(BaseModel):
    event_id: str
    flight_number: str
    airline: str
    departure_airport: str
    arrival_airport: str
    scheduled_departure: datetime | None = None
    actual_departure: datetime | None = None
    delay_minutes: int = 0
    status: str
    route_key: str
    ingested_at: datetime
