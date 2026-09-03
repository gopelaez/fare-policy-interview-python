"""Travel policy evaluation."""

from policy.models import Itinerary


class Policy:
    """Base class for a client's travel policy.

    Subclasses implement `evaluate` to decide whether an itinerary
    may be booked under this client's rules.
    """

    name: str = "unnamed"

    def evaluate(self, itinerary: Itinerary) -> bool:
        raise NotImplementedError


class PolicyRegistry:
    def __init__(self):
        self._policies: dict[str, Policy] = {}

    def register(self, client_id: str, policy: Policy) -> None:
        self._policies[client_id] = policy

    def for_client(self, client_id: str) -> Policy:
        if client_id not in self._policies:
            raise KeyError(f"No policy registered for client {client_id!r}")
        return self._policies[client_id]


registry = PolicyRegistry()
