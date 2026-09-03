"""Per-client policy implementations."""

from policy.engine import Policy, registry
from policy.models import Itinerary


class AcmePolicy(Policy):
    """Acme Corp: economy cabin only, and no more than $800 per trip."""

    name = "Acme Corp"

    MAX_PRICE = 800.0

    def evaluate(self, itinerary: Itinerary) -> bool:
        if itinerary.segment.cabin != "economy":
            return False
        if itinerary.price_usd > self.MAX_PRICE:
            return False
        return True


registry.register("acme", AcmePolicy())
