"""Swap rollover and MT5's holiday rule.

The rule quoted at the top of the source is MT5's own worked example, so these assertions
are against published behaviour rather than an interpretation of it.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest


class _Flags:
    """Stands in for SymbolSwapFlags, which is an IntFlag."""

    def __init__(self, value):
        self.value = value


class _Holiday:
    def __init__(self, day):
        self.date = day
        self.symbols = []
        self.mode = None


class _HolidayRepo:
    def __init__(self, days):
        self._days = days

    def get_all(self):
        return [_Holiday(d) for d in self._days]


class _Symbol:
    def __init__(self, name="EURUSD", swap_3day=3, consider_holidays=True):
        self.name = name
        self.swap_3day = swap_3day
        # CONSIDER_HOLIDAYS = 1
        self.swap_flags = _Flags(1 if consider_holidays else 0)


def _worker(holidays=None):
    from application.services.swap_worker import SwapWorker

    worker = SwapWorker.__new__(SwapWorker)
    worker.holiday_repo = _HolidayRepo(holidays) if holidays is not None else None
    return worker


def _a_tuesday():
    """A Tuesday, so the weekday rule alone gives 1."""
    d = date(2026, 10, 6)                      # a Tuesday
    assert d.weekday() == 1, "the fixed date must be a Tuesday"
    return datetime(d.year, d.month, d.day, 22, 0, tzinfo=timezone.utc)


def test_mt5s_worked_example():
    """Wednesday holiday, Tuesday multiplier 1, Wednesday 3 -> Tuesday charges 4, Wed 0."""
    tuesday = _a_tuesday()
    wednesday = tuesday + timedelta(days=1)

    worker = _worker(holidays=[wednesday.date()])
    # swap_3day uses MT5's SUNDAY-FIRST index, so a Wednesday triple day is 3.
    # Python's weekday() would give 2 and silently mean Monday.
    wednesday_mt5_index = (wednesday.date().weekday() + 1) % 7
    assert wednesday_mt5_index == 3, "the fixed date must be a Wednesday"
    symbol = _Symbol(swap_3day=wednesday_mt5_index)

    assert worker._day_multiplier(symbol, tuesday) == Decimal("4"), (
        "MT5: 'a sum of the multipliers of the current day and of the holiday'"
    )
    assert worker._day_multiplier(symbol, wednesday) == Decimal("0"), (
        "MT5: 'No swap will be charged on Wednesday as it is a holiday.'"
    )


def test_a_symbol_that_did_not_opt_in_is_untouched():
    tuesday = _a_tuesday()
    wednesday = tuesday + timedelta(days=1)

    worker = _worker(holidays=[wednesday.date()])
    symbol = _Symbol(consider_holidays=False)
    assert worker._day_multiplier(symbol, tuesday) == Decimal("1")
    assert worker._day_multiplier(symbol, wednesday) == Decimal("3")


def test_an_unknown_holiday_list_leaves_the_weekday_rule_alone():
    """No repository means "cannot tell", NOT "no holidays" - behaviour must not change."""
    tuesday = _a_tuesday()
    wednesday = tuesday + timedelta(days=1)

    worker = _worker(holidays=None)
    symbol = _Symbol()
    assert worker._day_multiplier(symbol, tuesday) == Decimal("1")
    assert worker._day_multiplier(symbol, wednesday) == Decimal("3")


def test_consecutive_holidays_sum_onto_the_day_before():
    """MT5: 'The coefficients are applied similarly if you have multiple holidays in a row.'"""
    tuesday = _a_tuesday()
    wednesday = tuesday + timedelta(days=1)
    thursday = wednesday + timedelta(days=1)
    friday = thursday + timedelta(days=1)

    worker = _worker(holidays=[wednesday.date(), thursday.date()])
    # triple day = Monday (MT5 index 1), so Wednesday and Thursday each contribute 1
    symbol = _Symbol(swap_3day=1)

    # Tuesday charges its own 1 plus Wednesday's 1 plus Thursday's 1
    assert worker._day_multiplier(symbol, tuesday) == Decimal("3")
    assert worker._day_multiplier(symbol, wednesday) == Decimal("0")
    assert worker._day_multiplier(symbol, thursday) == Decimal("0")
    # Friday is past the run, so it is a normal day again
    assert worker._day_multiplier(symbol, friday) == Decimal("1")


def test_weekends_still_charge_nothing():
    saturday = datetime(2026, 10, 10, 22, 0, tzinfo=timezone.utc)
    assert saturday.weekday() == 5, "the fixed date must be a Saturday"
    worker = _worker(holidays=[])
    assert worker._day_multiplier(_Symbol(), saturday) == Decimal("0")
