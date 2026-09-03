"""Core domain models for the booking system."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Traveler:
    id: str
    name: str
    email: str
    client_id: str
    title: str


@dataclass
class Segment:
    origin: str
    destination: str
    depart_at: datetime
    arrive_at: datetime
    carrier: str
    flight_number: str
    cabin: str  # one of: "economy", "premium_economy", "business", "first"

    @property
    def duration_hours(self) -> float:
        return (self.arrive_at - self.depart_at).total_seconds() / 3600


@dataclass
class Itinerary:
    id: str
    traveler: Traveler
    segment: Segment
    price_usd: float
