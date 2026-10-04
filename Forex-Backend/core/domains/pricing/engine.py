"""Client quote transformation — MT5's spread semantics, in one pure module.

Before M7 the matching engine filled every order at the RAW feed price: group
`SpreadDiff` was quarantined out of the wire format and never applied, symbol
`Spread`/`SpreadBalance` were stored but read by nothing, and the broker earned
nothing on spread. This module is the single place a raw (bid, ask) becomes the
price a CLIENT of a given group sees.

Semantics, from the MT5 Administrator guide in the reference corpus:

* Symbol settings, Common (Platform-Setup.md, "Spread — spread size in
  points", and IMTConSymbol/SpreadBalance.md): a non-zero `Spread` makes the
  spread FIXED. `SpreadBalance` is a SINGLE signed int (the SDK declares
  `int SpreadBalance`), a shift from the EQUAL distribution of `Spread`
  between Bid and Ask. The guide states the three cases exactly:

      feed spread == symbol spread : NewBid = Bid + B*P
      feed spread != symbol spread : NewBid = (Ask+Bid)/2 - floor(S/2)*P
      floating (S == 0)            : both prices shift by B*P

  and NewAsk = NewBid + S*P in the first two, so the client spread is exactly
  `Spread` points regardless of the feed's own spread. Odd `Spread` splits
  floor(S/2) below and ceil(S/2) above, per the guide's own example: "if the
  spread is 3, the zero spread balance corresponds to the ratio -1 Bid/+2 Ask".
  `Spread = 0` means FLOATING *and* still shifts by the balance — a floating
  symbol with a non-zero balance is marked up, which the previous code did not do.

* Group symbol settings, Common: "Spread difference — difference of a symbol
  spread for a certain group of users from the basic spread of the symbol;
  Difference balance — balance of spread difference distribution between bid
  and ask prices... if you set 3 as the spread difference, then the
  distribution can be the following: 3 bid / 0 ask, 2 bid / 1 ask". So
  `SpreadDiffBalance` points of the difference lower the client BID and the
  remainder raise the client ASK. And: "Price transformation settings for a
  group are applied AFTER applying base settings of a symbol."

* A group override value of MT5's `"default"` sentinel (None in the domain)
  INHERITS the symbol's setting — it never means zero.

The ECN translation example in the guide (client 1.14059 ↔ ECN 1.14053 via
2 points spread balance + 4 points ECN markup) is the same transform; the ECN
markup layer itself is deferred with the ECN work.
"""
from dataclasses import dataclass, replace
from decimal import Decimal
from typing import Any, Optional, Tuple

__all__ = [
    "SpreadSettings",
    "resolve_spread_settings",
    "client_quote",
    "pattern_matches",
]


@dataclass(frozen=True)
class SpreadSettings:
    """The effective spread configuration for one (symbol, group) pair.

    All values are in POINTS (multiples of the symbol's tick_size, which is
    MT5's Point). `fixed_*` come from the symbol's Spread/SpreadBalance;
    `spread_diff*` are the group-after-symbol transform.
    """

    fixed_spread: int = 0          # symbol Spread; 0 = floating
    fixed_balance: int = 0         # symbol SpreadBalance: points of the fixed spread on the bid side
    spread_diff: int = 0           # effective SpreadDiff (group override wins)
    spread_diff_balance: int = 0   # effective SpreadDiffBalance (points of the diff on the bid side)

    def has_effect(self) -> bool:
        return bool(self.fixed_spread or self.spread_diff)


def pattern_matches(pattern: Optional[str], symbol_name: str) -> bool:
    """MT5-style symbol mask: empty or '*' matches everything; a trailing '*'
    matches a prefix; otherwise exact. (The full mask language also supports
    '!' negation — not exercised by any configured override yet, documented
    rather than guessed.)
    """
    if not pattern or pattern == "*":
        return True
    if pattern.endswith("*"):
        return symbol_name.startswith(pattern[:-1])
    return symbol_name == pattern


def resolve_spread_settings(symbol: Any, group: Any) -> SpreadSettings:
    """Symbol base settings, then the first matching group override on top.

    None on an override field means MT5's "default" sentinel: inherit the
    symbol's value. A missing symbol or group degrades to whatever is known —
    pricing must never crash a fill because a cache entry is absent.
    """
    settings = SpreadSettings(
        fixed_spread=_as_int(getattr(symbol, "spread", 0)),
        fixed_balance=_as_int(getattr(symbol, "spread_balance", 0)),
        spread_diff=_as_int(getattr(symbol, "spread_diff", 0)),
        spread_diff_balance=_as_int(getattr(symbol, "spread_diff_balance", 0)),
    ) if symbol is not None else SpreadSettings()

    if group is None or symbol is None:
        return settings

    symbol_name = getattr(symbol, "name", "")
    for override in getattr(group, "symbol_overrides", None) or []:
        if not pattern_matches(getattr(override, "symbol_pattern", ""), symbol_name):
            continue
        diff = getattr(override, "spread_diff", None)
        balance = getattr(override, "spread_diff_balance", None)
        if diff is not None:
            settings = replace(settings, spread_diff=_as_int(diff))
        if balance is not None:
            settings = replace(settings, spread_diff_balance=_as_int(balance))
        break  # first matching override wins

    return settings


def client_quote(
    raw_bid: Decimal,
    raw_ask: Decimal,
    *,
    point: Decimal,
    settings: SpreadSettings,
) -> Tuple[Decimal, Decimal]:
    """Transform a raw feed quote into the client quote for these settings.

    The three documented fixed-spread cases are decided by comparing the FEED's
    own spread with the symbol's: MT5 anchors on the raw bid when they agree and
    on the feed MIDPOINT when they differ. Order of operations is the guide's -
    the symbol's base spread first, the group's spread difference after.

    The client ask can never end below the client bid (a negative spread is not a
    thing); the clamp is the only silent adjustment and it can only trigger on a
    negative SpreadDiff larger than the raw spread.
    """
    bid = Decimal(str(raw_bid))
    ask = Decimal(str(raw_ask))
    point = Decimal(str(point))
    if point <= 0:
        return bid, ask  # an unconfigurable point means no transform is possible

    symbol_spread = _as_int(settings.fixed_spread)
    balance = _as_int(settings.fixed_balance)

    if symbol_spread > 0:
        # Odd spreads split floor below / ceil above so bid + ask == spread
        # exactly; the guide's "spread 3, balance 0 -> -1 Bid/+2 Ask".
        below = Decimal(symbol_spread // 2)
        feed_spread_points = (ask - bid) / point
        if feed_spread_points == symbol_spread:
            # Feed spread already equals the symbol's: shift the bid by the
            # balance and keep the ask `spread` above it.
            bid = bid + Decimal(balance) * point
            ask = bid + Decimal(symbol_spread) * point
        else:
            # Different feed spread: anchor on the MIDPOINT, then lay the fixed
            # spread around it.
            mid = (ask + bid) / Decimal(2)
            bid = mid - below * point
            ask = bid + Decimal(symbol_spread) * point
    elif balance:
        # Floating spread (0) with a balance: "prices are shifted by the same
        # Spread Balance value" - BOTH sides move, the feed's width is kept.
        shift = Decimal(balance) * point
        bid = bid + shift
        ask = ask + shift

    if settings.spread_diff:
        # The group layer widens the spread by exactly `spread_diff` points and
        # puts `spread_diff_balance` of them on the bid side. Applied to the
        # SPREAD, not to the bid's existing distance from something else.
        total = Decimal(_as_int(settings.spread_diff))
        on_bid = Decimal(_as_int(settings.spread_diff_balance))
        bid = bid - on_bid * point
        ask = ask + (total - on_bid) * point

    if ask < bid:
        ask = bid
    if bid <= 0:
        raise ValueError(
            f"client bid is not positive ({bid}) after spread transformation — "
            "check SpreadDiff/SpreadBalance configuration"
        )
    return bid, ask


def _as_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0
