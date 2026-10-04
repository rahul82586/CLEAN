"""MT5 floating leverage tiers (Platform-Setup/Leverages.md)."""
from __future__ import annotations

from decimal import Decimal as D

import pytest

from core.domains.market_data.leverage_tiers import (
    LeverageProfile,
    LeverageRule,
    LeverageTier,
    TierRange,
    pattern_matches,
    select_rates,
)


def _profile(*rules) -> LeverageProfile:
    return LeverageProfile(name="test", rules=list(rules))


def test_no_profile_leaves_the_margin_alone():
    """With no profile configured the behaviour must be identical to before the feature."""
    result = select_rates(None, symbol_name="EURUSD", volumes={"EURUSD": D("5")})
    assert result.applied is False
    assert result.initial_rate == D("1")
    assert result.maintenance_rate == D("1")


def test_a_non_matching_symbol_is_untouched():
    """pattern_matches must gate the rule, not merely filter the measurement."""
    profile = _profile(LeverageRule(
        name="forex", symbols="GBP*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=None, initial_rate=D("0.5"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("5")})
    assert result.applied is False
    assert result.initial_rate == D("1")


def test_a_tier_scales_the_margin_by_its_rate():
    """"applying an ADDITIONAL COEFFICIENT to the ... margin values"."""
    profile = _profile(LeverageRule(
        name="big", symbols="*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=D("10"), initial_rate=D("1")),
               LeverageTier(to=None, initial_rate=D("0.5"))],
    ))
    small = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("5")})
    large = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("20")})

    assert small.initial_rate == D("1")
    assert large.initial_rate == D("0.5")
    # "additional coefficient": a symbol margin of 1000 becomes 500 in the larger band
    assert large.initial_margin(D("1000")) == D("500")


def test_bands_are_contiguous_so_the_boundary_belongs_to_the_lower_band():
    """"The minimum value is set automatically based on the value of the previous range"."""
    profile = _profile(LeverageRule(
        name="bands", symbols="*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=D("10"), initial_rate=D("1")),
               LeverageTier(to=D("50"), initial_rate=D("0.5")),
               LeverageTier(to=None, initial_rate=D("0.2"))],
    ))
    assert select_rates(profile, symbol_name="EURUSD",
                        volumes={"EURUSD": D("10")}).initial_rate == D("1")
    assert select_rates(profile, symbol_name="EURUSD",
                        volumes={"EURUSD": D("10.01")}).initial_rate == D("0.5")
    assert select_rates(profile, symbol_name="EURUSD",
                        volumes={"EURUSD": D("1000")}).initial_rate == D("0.2")


def test_the_first_matching_rule_wins_not_the_best():
    """"If the same instrument matches multiple rules, only the first applicable rule is
    used" - so a broad rule listed first must beat a narrower one listed second."""
    profile = _profile(
        LeverageRule(name="first", symbols="*", range_type=TierRange.VOLUME,
                     tiers=[LeverageTier(to=None, initial_rate=D("0.5"))]),
        LeverageRule(name="second", symbols="EURUSD", range_type=TierRange.VOLUME,
                     tiers=[LeverageTier(to=None, initial_rate=D("0.9"))]),
    )
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("1")})
    assert result.rule_name == "first"
    assert result.initial_rate == D("0.5")


def test_vs_volume_per_symbol_measures_one_instrument_not_the_total():
    """"Volume per symbol ... the volume of open positions for each individual symbol"."""
    profile = _profile(LeverageRule(
        name="per-symbol", symbols="*", range_type=TierRange.VOLUME_PER_SYMBOL,
        tiers=[LeverageTier(to=D("10"), initial_rate=D("1")),
               LeverageTier(to=None, initial_rate=D("0.5"))],
    ))
    # EURUSD alone is 5 lots, well under the 10 band, even though the book holds 60
    result = select_rates(profile, symbol_name="EURUSD",
                          volumes={"EURUSD": D("5"), "GBPUSD": D("55")})
    assert result.measured == D("5")
    assert result.initial_rate == D("1")


def test_total_volume_measures_every_covered_symbol():
    profile = _profile(LeverageRule(
        name="total", symbols="*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=D("10"), initial_rate=D("1")),
               LeverageTier(to=None, initial_rate=D("0.5"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD",
                          volumes={"EURUSD": D("5"), "GBPUSD": D("55")})
    assert result.measured == D("60")
    assert result.initial_rate == D("0.5")


def test_notional_rules_are_skipped_when_no_conversion_is_available():
    """A notional measurement cannot be derived from a volume, so the rule must be skipped
    rather than measured as zero - which would silently land in the lowest band."""
    profile = _profile(LeverageRule(
        name="notional", symbols="*", range_type=TierRange.NOTIONAL,
        tiers=[LeverageTier(to=None, initial_rate=D("0.01"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("5")},
                          notionals=None)
    assert result.applied is False
    assert result.initial_rate == D("1")


def test_a_zero_maintenance_rate_means_no_margin_unlike_symbol_settings():
    """"Unlike symbol settings, here the zero maintenance margin does not indicate that the
    initial margin ratio will be used instead. The zero value means that no margin will be
    charged." - so the two rates must stay independent."""
    profile = _profile(LeverageRule(
        name="free-maint", symbols="*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=None, initial_rate=D("1"), maintenance_rate=D("0"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("1")})
    assert result.initial_rate == D("1")          # NOT replaced by the maintenance rate
    assert result.maintenance_rate == D("0")
    assert result.maintenance_margin(D("1000")) == D("0")


def test_an_exchange_group_is_never_scaled():
    """"The settings do not apply for groups with exchange calculation type.""" 
    profile = _profile(LeverageRule(
        name="any", symbols="*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=None, initial_rate=D("0.01"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("1")},
                          is_exchange_group=True)
    assert result.applied is False
    assert result.initial_rate == D("1")


def test_a_rule_covering_no_symbols_is_skipped_not_applied_as_zero():
    profile = _profile(LeverageRule(
        name="empty", symbols="ZZZ*", range_type=TierRange.VOLUME,
        tiers=[LeverageTier(to=None, initial_rate=D("0.1"))],
    ))
    result = select_rates(profile, symbol_name="EURUSD", volumes={"EURUSD": D("5")})
    assert result.applied is False


def test_pattern_matches_agrees_with_the_pricing_engine_rule():
    """Same mask language as the spread overrides, so two settings cannot disagree."""
    assert pattern_matches(None, "EURUSD") is True
    assert pattern_matches("*", "EURUSD") is True
    assert pattern_matches("EUR*", "EURUSD") is True
    assert pattern_matches("GBP*", "EURUSD") is False
    assert pattern_matches("EURUSD", "EURUSD") is True
    assert pattern_matches("EURUSD", "EURUSDT") is False
