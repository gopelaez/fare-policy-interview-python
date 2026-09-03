"""Helpers for building test data."""

from datetime import datetime, timedelta

from policy.models import Itinerary, Segment, Traveler


def make_traveler(
    client_id: str = "acme",
    title: str = "Software Engineer",
    name: str = "Dana Reyes",
) -> Traveler:
    return Traveler(
        id="trv_001",
        name=name,
        email="dana.reyes@example.com",
        client_id=client_id,
        title=title,
    )


def make_segment(
    origin: str = "BOS",
    destination: str = "ORD",
    cabin: str = "economy",
    duration_hours: float = 2.5,
) -> Segment:
    depart = datetime(2026, 10, 14, 9, 0)
    return Segment(
        origin=origin,
        destination=destination,
        depart_at=depart,
        arrive_at=depart + timedelta(hours=duration_hours),
        carrier="AA",
        flight_number="AA1234",
        cabin=cabin,
    )


def make_itinerary(
    price_usd: float = 450.0,
    traveler: Traveler | None = None,
    segment: Segment | None = None,
) -> Itinerary:
    return Itinerary(
        id="itn_001",
        traveler=traveler or make_traveler(),
        segment=segment or make_segment(),
        price_usd=price_usd,
    )
