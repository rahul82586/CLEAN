"""The plugin contract.

WHAT THIS IS FOR
----------------
A gateway, a feed or a reporter must be addable WITHOUT editing anything in `core/`,
`application/` or `api/`. MT5 does this with `IMTConPlugin`: the master reads a configuration,
and a plugin is addressed by `module` + `port` + `parameters` - never by a code change.

So the whole contract is these three interfaces. A plugin implements one, and `master.py`
starts it with `python -m <module> --port N --config '<json>'`.

WHY SEPARATE TYPES RATHER THAN ONE
----------------------------------
`gateway`, `feed` and `report` are genuinely different capabilities, and conflating them is
what produced the current situation: the MT5 LP box on port 8000 is BOTH a feed and a
gateway in one process, which is why it can only subscribe 6 symbols at a time and why changing
its feed provider means changing its code.

Splitting them is what lets a feed come from one provider while orders route to another.

    IFeed      quotes only, one-way. No orders. Safe to run many.
    IGateway   quotes AND orders, two-way. One per LP.
    IReporter  reads state, writes nothing.

A GATEWAY MAY ALSO BE A FEED - but it is not required to be. MT5 keeps them separate for
exactly the reason above, and a plugin that only quotes has no business being able to place an
order.

WHAT A PLUGIN NEVER DOES
------------------------
* it never imports from `core.domains` to compute risk - risk stays in the core process;
* it never writes the account, position or order tables - it reports what happened and the
  core books it;
* it never invents a price - a missing quote is `None`, not zero.

That last one is not a style rule. A gateway that reports a zero price because it lost its feed
produces a fill at zero, and no amount of downstream validation recovers the account.

HOW A PLUGIN REPORTS A FILL
----------------------------
The plugin answers the question "did the venue take this order?" and returns that. It does not
book it. `ExecutionOrchestrator` books it. Keeping booking in one place is what makes the fill
path testable without a venue.

IMPLEMENTATION NOTE
-------------------
These are `typing.Protocol` classes, not ABCs, so a plugin needs no import from this package to
be valid - it needs only the right method names. That matters because the point is to let a
third party write a gateway without depending on our internals; requiring an ABC import would
make our package a dependency of theirs.

Import this module only for type checking and for `describe_capabilities`.
"""
from __future__ import annotations

from typing import Any, AsyncIterator, Dict, List, Optional, Protocol, runtime_checkable

#: The capability names `plugins.yaml` may use in a `type:` field.
CAPABILITIES = ("gateway", "feed", "report", "core")


@runtime_checkable
class IFeed(Protocol):
    """Quotes only. One-way. No order method exists on this interface on purpose.

    A feed that cannot place an order cannot be the reason an order reached the wrong venue,
    which is the property that lets many feeds run safely at once.
    """

    async def stream_quotes(self) -> AsyncIterator[Any]:
        """Yield quote objects continuously, reconnecting on failure.

        The contract is deliberately weak on shape: a quote is anything with `symbol`, `bid`,
        `ask` and `timestamp_ns`. Normalising it is the core's job (`market_data.feed_access`),
        so a vendor's own field names never leak into the risk engine.
        """
        ...


@runtime_checkable
class IGateway(Protocol):
    """Quotes AND orders. Two-way.

    This is the MT5 Gateway: it talks to an external trading system, so it places orders and
    it also returns prices. `get_quote` is optional in practice - a gateway that only executes
    is legitimate - so implementations may return `None` from it, and the core treats that as
    "this venue does not quote", not as a zero price.
    """

    async def place_order(
        self,
        symbol: str,
        side: str,
        volume: float,
        price: Optional[float] = None,
        *,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Send an order and report what the venue did.

        Returns a dict with at least `status`, and `venue_order_id` when accepted. `status`
        MUST be one of MT5's fill states - FILLED / PARTIAL / REJECTED / TIMEOUT / UNKNOWN -
        because the caller branches on it.

        `UNKNOWN` is a real, load-bearing answer, not a cop-out: it means the request left and
        the outcome is not yet known. The caller must then treat the position as exposed and
        reconcile, rather than assume it failed. A gateway that collapses UNKNOWN into
        REJECTED hides a live hedge from the broker.
        """
        ...

    async def close_position(
        self, symbol: str, venue_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Close a position at this venue. Same status vocabulary as `place_order`."""
        ...

    async def get_positions(self, login: Optional[str] = None) -> List[Dict[str, Any]]:
        """Positions the venue currently holds. Used to reconcile after an UNKNOWN."""
        ...

    async def health(self) -> Dict[str, Any]:
        """Connection state. Must never raise - an unreachable venue is a report, not an error.

        The supervisor needs this to decide whether to re-route, so an exception here would
        turn a degraded venue into an unhandled crash in the master.
        """
        ...


@runtime_checkable
class IReporter(Protocol):
    """Reads state, writes nothing."""

    async def report(self, window: str) -> Dict[str, Any]:
        ...


def describe_capabilities(obj: Any) -> List[str]:
    """Which contract an object satisfies. Used by the master to check a plugin.

    Checked structurally, so it works for any object with the right methods - including one
    written by a third party that has never imported this package.
    """
    return [
        name
        for name, proto in (
            ("feed", IFeed),
            ("gateway", IGateway),
            ("report", IReporter),
        )
        if isinstance(obj, proto)
    ]