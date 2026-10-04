"""Floating leverage tiers — MT5's dynamic leverage, which had no implementation at all.

MT5 (`Platform-Setup/Leverages.md`):

    "rules are checked and applied top to bottom. If the same instrument matches multiple
     rules, only the first applicable rule will be used."

    Range — how a tier's band is measured:
        Volume                  total volume of open positions for ALL Symbols in the rule
        Volume per symbol        the same, per individual symbol
        Notional value          total value of open positions, converted to Currency
                                (or the group's deposit currency when Currency is empty)
        Notional value per symbol

    "The minimum value is set automatically based on the value of the previous range" —
    tiers are contiguous: each declares a maximum, and the next starts where it ended.

    "Set both margin ratios explicitly. Unlike symbol settings, here the zero maintenance
     margin does not indicate that the initial margin ratio will be used instead. The zero
     value means that no margin will be charged."

    "Floating leverage settings only work for groups with the 'for Retail Forex, CFD,
     Futures' calculation type (hedging and netting). The settings do not apply for groups
     with exchange calculation type."

    "It allows you to change leverage by applying an ADDITIONAL COEFFICIENT to the initial
     and maintenance margin values calculated in accordance with the symbol settings."

That last sentence decides the design: a tier does NOT replace the margin formula. It
multiplies the margin the symbol settings already produced. So this module computes the two
RATES a tier grants and the caller multiplies - nothing in `basic_margin` changes.

WHY A SEPARATE MODULE
---------------------
The engine is pure: it takes already-measured volumes/notionals and returns the rates. It
has no dependency on the database or the symbol model, so it can be verified directly
against MT5's stated rules, and the wiring decision (which measure, which currency) stays
with the caller - the only place that can convert a currency.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Sequence, Tuple

ZERO = Decimal("0")
ONE = Decimal("1")

__all__ = [
    "TierRange",
    "LeverageTier",
    "LeverageRule",
    "LeverageProfile",
    "LeverageTierResult",
    "pattern_matches",
    "select_rates",
]


class TierRange(Enum):
    """What a tier's band is measured against (MT5's `Range` parameter).

    The values are internal strings, not wire values: MT5 exposes this as a UI choice and
    the reference export carries no field for it, so there is nothing to round-trip and no
    wire numbering to match.
    """

    VOLUME = "volume"
    VOLUME_PER_SYMBOL = "volume_per_symbol"
    NOTIONAL = "notional"
    NOTIONAL_PER_SYMBOL = "notional_per_symbol"


def pattern_matches(pattern: Optional[str], symbol_name: str) -> bool:
    """MT5-style symbol mask, matching the pricing engine's existing rule.

    Empty or '*' matches everything; a trailing '*' matches a prefix; otherwise exact.
    Reusing the same rule as `core.domains.pricing.engine.pattern_matches` matters: a
    leverage rule and a spread override written with the same mask must cover the same
    symbols, or two settings on one instrument disagree about their own scope.
    """
    if not pattern or pattern == "*":
        return True
    if pattern.endswith("*"):
        return symbol_name.startswith(pattern[:-1])
    return symbol_name == pattern


@dataclass
class LeverageTier:
    """One band: everything up to `to`, with the two rates it grants.

    `to` is the band's MAXIMUM, per MT5 ("Specify the maximum values in the To field"). The
    minimum is the previous tier's maximum, so it is not stored. `None` means unbounded, and
    a tier with no maximum necessarily swallows everything after it, so it must be last.
    """

    to: Optional[Decimal]
    initial_rate: Decimal = ONE
    maintenance_rate: Decimal = ONE


@dataclass
class LeverageRule:
    """One rule: a symbol mask, a measure, and the tiers to apply.

    Rules are evaluated TOP TO BOTTOM and only the first applicable one is used, so the order
    of the list IS the semantics - the same property the routing rules have.
    """

    name: str = ""
    symbols: str = ""                 # mask, MT5's "Symbol" field
    range_type: TierRange = TierRange.VOLUME
    currency: str = ""                # notional target; empty = the group's currency
    tiers: List[LeverageTier] = field(default_factory=list)


@dataclass
class LeverageProfile:
    """A named set of rules, attachable to a group."""

    name: str = ""
    rules: List[LeverageRule] = field(default_factory=list)


@dataclass
class LeverageTierResult:
    """A tier evaluation's outcome, with enough detail to explain itself.

    A broker that cannot show WHY a coefficient was applied cannot defend a margin call,
    which is the same reason `MarginBreakdown` carries its own decomposition.

    BOTH rates are carried, not one, because MT5 sets them explicitly and independently:
    "Set both margin ratios explicitly. Unlike symbol settings, here the zero maintenance
    margin does not indicate that the initial margin ratio will be used instead."

    A zero rate means NO MARGIN IS CHARGED. That falls out of the multiplication naturally,
    and is deliberately different from symbol settings, where a zero maintenance rate means
    "use the initial rate".
    """

    initial_rate: Decimal = ONE
    maintenance_rate: Decimal = ONE
    rule_name: str = ""
    tier_index: Optional[int] = None
    measured: Optional[Decimal] = None
    applied: bool = False

    def initial_margin(self, base_initial: Decimal) -> Decimal:
        """Apply the initial rate to a margin already computed from the symbol settings."""
        return base_initial * self.initial_rate

    def maintenance_margin(self, base_maintenance: Decimal) -> Decimal:
        return base_maintenance * self.maintenance_rate


def select_rates(
    profile: Optional[LeverageProfile],
    *,
    symbol_name: str,
    volumes: Dict[str, Decimal],
    notionals: Optional[Dict[str, Decimal]] = None,
    is_exchange_group: bool = False,
) -> LeverageTierResult:
    """The margin rate pair for one symbol, or (1, 1) when no rule applies.

    Returns rates of exactly 1 with `applied=False` whenever nothing matches, so a caller
    can multiply unconditionally without a special case. That also makes the behaviour with
    no profile configured bit-for-bit identical to the code before this module existed -
    which is what makes the change safe to land before any profile is created.

    Args:
        volumes:   symbol -> open volume in lots, for THIS account.
        notionals: symbol -> open value, ALREADY converted to the rule's currency. The engine
                   does not convert: conversion needs market rates, and the caller is the only
                   place that has them.
        is_exchange_group: MT5 states the tiers "do not apply for groups with exchange
                   calculation type", so the caller passes True and gets (1, 1) back rather
                   than the engine guessing from a field it cannot see.
    """
    if profile is None or is_exchange_group:
        return LeverageTierResult()

    for rule in profile.rules:
        if not pattern_matches(rule.symbols, symbol_name):
            continue

        covered = [name for name in volumes if pattern_matches(rule.symbols, name)]
        if not covered:
            continue

        measured = _measure(rule, covered, symbol_name, volumes, notionals)
        if measured is None:
            continue

        index, tier = _first_tier(rule.tiers, measured)
        if tier is None:
            # The rule covers this symbol but no band reaches the measurement. Falling
            # through to the NEXT rule would contradict "only the first applicable rule is
            # used", so the neutral pair is returned and `applied` says it did not apply.
            return LeverageTierResult(rule_name=rule.name, measured=measured, applied=False)

        return LeverageTierResult(
            initial_rate=tier.initial_rate,
            maintenance_rate=tier.maintenance_rate,
            rule_name=rule.name,
            tier_index=index,
            measured=measured,
            applied=True,
        )

    return LeverageTierResult()


def _measure(
    rule: LeverageRule,
    covered: Sequence[str],
    symbol_name: str,
    volumes: Dict[str, Decimal],
    notionals: Optional[Dict[str, Decimal]],
) -> Optional[Decimal]:
    """The value a rule's bands are compared against.

    The per-symbol variants measure EACH symbol separately, which is exactly what makes a
    rule written as "Forex\\*" apply per instrument rather than to the account total.
    """
    if rule.range_type is TierRange.VOLUME:
        return sum((volumes.get(name, ZERO) for name in covered), ZERO)

    if rule.range_type is TierRange.VOLUME_PER_SYMBOL:
        return volumes.get(symbol_name, ZERO)

    if notionals is None:
        # A notional rule with no conversion available. Returning None skips the rule, which
        # is honest: a notional measurement cannot be derived from a volume.
        return None

    if rule.range_type is TierRange.NOTIONAL:
        return sum((notionals.get(name, ZERO) for name in covered), ZERO)

    if rule.range_type is TierRange.NOTIONAL_PER_SYMBOL:
        return notionals.get(symbol_name, ZERO)

    return None


def _first_tier(tiers: Sequence[LeverageTier], measured: Decimal) -> Tuple[Optional[int], Optional[LeverageTier]]:
    """The first band whose maximum covers `measured`, or (None, None).

    "The minimum value is set automatically based on the value of the previous range", so
    the bands are contiguous and the FIRST match is right - the same reading as MT5's
    "only the first applicable rule", applied one level down.
    """
    for index, tier in enumerate(tiers):
        if tier.to is None:
            return index, tier                # unbounded: covers everything above
        if measured <= tier.to:
            return index, tier
    return None, None


def parse_profile(raw: Any) -> Optional[LeverageProfile]:
    """Build a LeverageProfile from the JSONB shape stored on the group.

    R27: the profile lives in `groups.mt5_extra["leverage_tiers"]`, which is JSONB, so every
    value arrives as a string or a number. Tolerant on TYPE, strict on SHAPE - an unreadable
    profile returns None and the caller logs, because a half-applied tier table would silently
    mis-price every account on the group, which is worse than not applying tiers at all.

    The field names are the dataclasses' own (`to`, `range_type`), not MT5's UI labels, so a
    reader can follow the mapping without a second table.
    """
    if not raw:
        return None
    if isinstance(raw, LeverageProfile):
        return raw
    if not isinstance(raw, dict):
        return None

    rules: List[LeverageRule] = []
    for rule_raw in (raw.get("rules") or []):
        if not isinstance(rule_raw, dict):
            continue
        tiers: List[LeverageTier] = []
        for tier_raw in (rule_raw.get("tiers") or []):
            if not isinstance(tier_raw, dict):
                continue
            raw_to = tier_raw.get("to")
            tiers.append(
                LeverageTier(
                    # `None` means unbounded, which is also what an absent maximum means:
                    # MT5 requires such a tier to be last, and the selector enforces that.
                    to=Decimal(str(raw_to)) if raw_to not in (None, "", "inf") else None,
                    initial_rate=Decimal(str(tier_raw.get("initial_rate", 1) or 1)),
                    maintenance_rate=Decimal(str(tier_raw.get("maintenance_rate", 1) or 1)),
                )
            )
        raw_range = str(rule_raw.get("range_type", "") or "").strip().lower()
        try:
            range_type = TierRange(raw_range) if raw_range else TierRange.VOLUME
        except ValueError:
            range_type = TierRange.VOLUME
        rules.append(
            LeverageRule(
                name=str(rule_raw.get("name", "") or ""),
                symbols=str(rule_raw.get("symbols", "") or ""),
                range_type=range_type,
                currency=str(rule_raw.get("currency", "") or ""),
                tiers=tiers,
            )
        )
    return LeverageProfile(name=str(raw.get("name", "") or ""), rules=rules) if rules else None
