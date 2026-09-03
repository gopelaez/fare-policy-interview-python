# Fare Policy Engine

A small slice of a corporate travel booking system.

Companies that book travel through us each have a **travel policy** — rules about
what their employees are allowed to book. Before a trip is ticketed, we check the
proposed itinerary against that company's policy.

Right now there is exactly one client, Acme Corp, whose policy is simple: economy
cabin only, and nothing over $800.

## Setup

```bash
pip install pytest
python -m pytest
```

Three tests should pass.

## Layout

```
policy/
  models.py    domain objects (Traveler, Segment, Itinerary)
  engine.py    Policy base class + a registry keyed by client
  clients.py   per-client policy implementations
tests/
  fixtures.py  helpers for building test data
  test_acme.py
```

## How this session works

We're going to onboard more clients together. I'll hand you their policies one at
a time and you implement them.

A few things worth saying up front:

- **Nothing here is sacred.** The existing code is a starting point, not a
  constraint. If you want to change the models, the base class, the return types,
  the whole approach — do it. Restructuring is expected, not a sign you got
  something wrong earlier.
- **Think out loud.** I care more about how you're reasoning than about what
  compiles.
- **Ask me questions.** I'll be describing policies the way a travel manager
  would describe them, which means informally. If something is ambiguous, say so.
- **Use AI however you normally would.** Keep it on screen so I can follow along.
