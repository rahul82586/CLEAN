"""Risk-service unit tests."""


# ---------------------------------------------------------------------------
# MT5 per-symbol "Max quote delay"
#
# Trade.md: "time (in seconds) of delay in the receipt of quotes, after which trading
# will be automatically disabled for this symbol. As quotes start coming again, trade
# will be enabled automatically."
#
# The setting was stored (QuotesTimeout) and exposed on the Trade tab, but nothing read
# it during validation, so a symbol whose feed had stopped still accepted orders at a
# 14-hour-old price.
#
# The checks are driven through the helper rather than a full order, because the helper
# is where the decision lives and a full order would drag in the session, holiday and
# margin steps - each of which could mask the result.
# ---------------------------------------------------------------------------


class _Tick:
    def __init__(self, age_seconds, from_now):
        from datetime import timedelta
        self.timestamp = from_now - timedelta(seconds=age_seconds)


class _Symbol:
    def __init__(self, name="ETHUSD", quotes_timeout=None, extra=None):
        self.name = name
        self.quotes_timeout = quotes_timeout
        self.mt5_extra = extra or {}


class _Engine:
    """A market-data engine returning one tick, or none."""

    def __init__(self, age_seconds=None, now=None):
        self._tick = None if age_seconds is None else _Tick(age_seconds, now)

    def get_latest_tick(self, symbol):          # noqa: ARG002
        return self._tick


def _service(age_seconds=None, now=None):
    from application.services.risk_service import PreTradeRiskService
    service = PreTradeRiskService.__new__(PreTradeRiskService)
    service.market_data_engine = _Engine(age_seconds, now)
    return service


def _now():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)


def test_a_quote_older_than_its_delay_refuses_trading():
    import asyncio
    service = _service(age_seconds=600, now=_now())
    reason = asyncio.run(service._check_max_quote_delay(_Symbol(quotes_timeout=60), _now()))
    assert reason is not None
    assert "Max quote delay" in reason


def test_a_quote_inside_its_delay_is_allowed():
    import asyncio
    service = _service(age_seconds=5, now=_now())
    assert asyncio.run(
        service._check_max_quote_delay(_Symbol(quotes_timeout=60), _now())
    ) is None


def test_recovery_needs_no_reset_once_the_quote_is_fresh_again():
    """"As quotes start coming again, trade will be enabled automatically."

    Same symbol, same configuration - only the tick age changes. Nothing is stored
    between the two calls, so there is no state to clear.
    """
    import asyncio
    symbol = _Symbol(quotes_timeout=60)

    stale = _service(age_seconds=600, now=_now())
    assert asyncio.run(stale._check_max_quote_delay(symbol, _now())) is not None

    fresh = _service(age_seconds=1, now=_now())
    assert asyncio.run(fresh._check_max_quote_delay(symbol, _now())) is None


def test_zero_delay_disables_the_check():
    """0 means no limit. Read literally it would refuse every symbol within a second."""
    import asyncio
    service = _service(age_seconds=86400, now=_now())
    assert asyncio.run(
        service._check_max_quote_delay(_Symbol(quotes_timeout=0), _now())
    ) is None


def test_the_wire_name_in_mt5_extra_is_honoured():
    """The value arrives from MT5 as `QuotesTimeout` in the quarantine."""
    import asyncio
    service = _service(age_seconds=600, now=_now())
    symbol = _Symbol(quotes_timeout=None, extra={"QuotesTimeout": 30})
    assert asyncio.run(service._check_max_quote_delay(symbol, _now())) is not None


def test_no_tick_at_all_is_refused_when_a_delay_is_configured():
    """MT5 disables trading on a symbol whose quotes have not arrived; "never arrived"
    is the extreme case of that, not an exemption."""
    import asyncio
    service = _service(age_seconds=None, now=_now())
    assert asyncio.run(
        service._check_max_quote_delay(_Symbol(quotes_timeout=15), _now())
    ) is not None
