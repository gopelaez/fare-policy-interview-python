from policy.engine import registry

import policy.clients  # noqa: F401  (registers the policies)

from tests.fixtures import make_itinerary, make_segment


def test_cheap_economy_trip_is_allowed():
    itinerary = make_itinerary(price_usd=450.0)
    assert registry.for_client("acme").evaluate(itinerary) is True


def test_expensive_trip_is_denied():
    itinerary = make_itinerary(price_usd=1200.0)
    assert registry.for_client("acme").evaluate(itinerary) is False


def test_business_class_is_denied():
    itinerary = make_itinerary(segment=make_segment(cabin="business"))
    assert registry.for_client("acme").evaluate(itinerary) is False
