"""
Market Data Engine - Central Price & DOM Distribution Hub

Single source of truth for all live market data, order books (DOM), tick statistics,
and bar aggregations across the trading platform.

Architectural Rule: Pure domain orchestrator in core/, zero framework imports.
"""
import asyncio
import logging
from typing import Any, Dict, List, Optional

from core.domains.market_data.bar_aggregator import BarAggregator
from core.domains.market_data.quote_freshness import (
    DEFAULT_MAX_TICK_AGE_SECONDS,
    resolve_max_tick_age_seconds,
)
from core.domains.market_data.models import BarTimeframe, BookLevel, OrderBook, Tick, TickStat
from core.events.domain_events import BookUpdated, DomainEvent, EventType, TickReceived
from core.ports.interfaces import IBarRepository, IEventBus, ISymbolRepository

logger = logging.getLogger(__name__)


class MarketDataEngine:
    """
    Central hub for market data processing.
    Receives ticks from feeds, maintains in-memory order books, updates statistics,
    dispatches ticks to bar aggregators, caches to Redis, and publishes domain events.
    """
    #: D6: how old a tick may be and still be ingested. Default matches M7's
    #: PRICING_MAX_TICK_AGE_SECONDS so ingestion and pricing agree; 0 disables.
    DEFAULT_MAX_TICK_AGE_SECONDS = DEFAULT_MAX_TICK_AGE_SECONDS

    def __init__(
        self,
        event_bus: IEventBus,
        symbol_repo: Optional[ISymbolRepository] = None,
        redis_cache: Optional[Any] = None,
        bar_repository: Optional[IBarRepository] = None,
        max_tick_age_seconds: Optional[float] = None
    ):
        self.event_bus = event_bus
        self.symbol_repo = symbol_repo
        self.redis_cache = redis_cache
        #: Strong references to in-flight Redis mirror tasks. The event loop only keeps a
        #: weak reference to a running task, so without this a pending write can be
        #: collected before it runs and the entry silently never appears.
        self._cache_tasks: set = set()

        self.bar_repository = bar_repository
        self.max_tick_age_seconds = self._resolve_max_tick_age(max_tick_age_seconds)
        #: per-symbol counters so a rejected feed is visible without flooding the log
        self._stale_dropped: Dict[str, int] = {}

        # In-memory state
        self.ticks: Dict[str, Tick] = {}  # Symbol -> Latest Tick
        self.books: Dict[str, OrderBook] = {}  # Symbol -> OrderBook
        self.stats: Dict[str, TickStat] = {}  # Symbol -> TickStat
        self.bar_aggregators: Dict[str, Dict[BarTimeframe, BarAggregator]] = {}  # Symbol -> {Timeframe -> Aggregator}

    def _get_or_create_aggregators(self, symbol: str) -> Dict[BarTimeframe, BarAggregator]:
        """Ensure bar aggregators exist for all 9 timeframes for a given symbol."""
        if symbol not in self.bar_aggregators:
            self.bar_aggregators[symbol] = {
                tf: BarAggregator(
                    symbol=symbol,
                    timeframe=tf,
                    event_bus=self.event_bus,
                    bar_repository=self.bar_repository
                )
                for tf in BarTimeframe
            }
        return self.bar_aggregators[symbol]

    @classmethod
    def _resolve_max_tick_age(cls, explicit: Optional[float]) -> float:
        """D6: delegate to the one resolver RiskEngine uses too, so the ingestion
        guard and the valuation guard cannot drift apart again."""
        return resolve_max_tick_age_seconds(explicit)

    def _is_stale(self, tick: Tick) -> bool:
        """Quote filtration: reject a tick older than `max_tick_age_seconds`.

        D6: this was a hard-coded 10.0s. MT5 stamps a tick with the BROKER's quote
        time, so the measured age carries the terminal's lag and any clock offset
        between the broker and this host. Measured against a real terminal over a
        public tunnel, ages ran 0.4s-12.7s - so on a thin Friday evening every
        tick exceeded 10s and the engine held no price at all, while the socket
        stayed happily connected. 497 of 497 ticks were dropped and the only
        evidence was a logger.debug line.
        """
        if not tick or not tick.timestamp:
            return True
        limit = self.max_tick_age_seconds
        if not limit or limit <= 0:
            return False
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        tick_ts = tick.timestamp
        if tick_ts.tzinfo is None:
            tick_ts = tick_ts.replace(tzinfo=timezone.utc)
        age = (now - tick_ts).total_seconds()
        if age <= limit:
            return False
        self._report_stale(tick, age, limit)
        return True

    def _report_stale(self, tick: Tick, age: float, limit: float) -> None:
        """Make a rejected feed visible.

        The first drop per symbol logs at WARNING with the actual age, then every
        200th. Without this an operator cannot distinguish "no ticks arriving"
        from "ticks arriving and being rejected" - and the second one looks
        exactly like a healthy, connected, useless feed.
        """
        symbol = getattr(tick, "symbol", "?")
        n = self._stale_dropped.get(symbol, 0) + 1
        self._stale_dropped[symbol] = n
        if n == 1 or n % 200 == 0:
            logger.warning(
                "dropped %s tick(s) for %s as stale: newest age %.1fs exceeds "
                "MARKET_DATA_MAX_TICK_AGE_SECONDS=%.1f. The feed IS delivering - the "
                "quotes are older than the limit. Raise the limit (M7's pricing guard "
                "defaults to 60s) or check the broker terminal's clock.",
                n, symbol, age, limit,
            )

    def _is_noise(self, tick: Tick) -> bool:
        """
        Quote filtration check for price noise/bad quotes.
        # TODO: Phase 11 - Implement spike filter & min pip step threshold per symbol.
        """
        return False

    async def process_tick(self, tick: Tick) -> None:
        """
        Main tick pipeline:
        1. Validate & filter tick
        2. Store in-memory latest tick
        3. Update symbol statistics
        4. Update DOM timestamp if book present
        5. Dispatch to bar aggregators across all timeframes
        6. Persist to Redis cache (if configured)
        7. Publish TICK_RECEIVED domain event
        """
        if self._is_stale(tick) or self._is_noise(tick):
            # _is_stale already logged the actionable detail at WARNING (rate
            # limited); this stays at debug for the noise-filter path.
            logger.debug(f"Tick filtered for symbol {tick.symbol}")
            return

        symbol = tick.symbol

        # Update latest tick in-memory state
        self.ticks[symbol] = tick

        # Update symbol statistics
        self._update_stats(tick)

        # Update order book timestamp if book exists for symbol
        if symbol in self.books:
            self.books[symbol].updated_at = tick.timestamp

        # Dispatch tick to bar aggregators for all timeframes
        aggregators = self._get_or_create_aggregators(symbol)
        for aggregator in aggregators.values():
            await aggregator.process_tick(tick)

        # Mirror the tick into Redis, for readers that do NOT share this process's
        # memory.
        #
        # Not awaited. A Redis round trip per tick serialises ingestion: with several
        # symbols at 20 ticks/s the loop cannot outrun a 1 ms write, and one slow Redis
        # response stalls every symbol behind it. The write is fire-and-forget with the
        # exception logged - a cache must never be able to break price ingestion.
        #
        # The 60s TTL the cache applies is deliberately kept: it is the mechanism that
        # makes a stale entry EXPIRE. The in-memory map has no such bound.
        if self.redis_cache:
            self._mirror_tick_to_cache(tick)

        # Publish domain event for downstream consumers (Risk Engine, OMS, WebSockets)
        event = TickReceived(
            aggregate_id=symbol,
            payload={
                "symbol": symbol,
                "bid": str(tick.bid),
                "ask": str(tick.ask),
                "spread": str(tick.spread),
                "mid": str(tick.mid),
                "timestamp": tick.timestamp.isoformat(),
                "source": tick.source
            }
        )
        # AWAITED, deliberately.
        #
        # Every local subscriber runs here: the margin pipeline, SlTpWorker, the book
        # matcher. Making this fire-and-forget raised the observed tick rate from
        # 1.00/s to roughly the feed's own rate, and broke six tests - stop loss and
        # take profit stopped firing, resting orders stopped filling. Those consumers
        # must see the price as it is at the moment they are called, not whenever their
        # scheduled task happens to run.
        #
        # The serial wait is what holds ingestion to ~1/s against a 19.7/s feed. That gap
        # is real; bounding it is a job for the coalescing window, which already limits
        # how often the database side revalues, not for decoupling consumers from price.
        await self.event_bus.publish(event)

    async def process_book_update(self, symbol: str, bids: List[BookLevel], asks: List[BookLevel]) -> None:
        """
        Process a full Depth of Market (DOM) order book update.
        Called when a liquidity provider or feed sends a market depth snapshot.
        """

        sorted_bids = sorted(bids, key=lambda lvl: lvl.price, reverse=True)
        sorted_asks = sorted(asks, key=lambda lvl: lvl.price)

        book = OrderBook(
            symbol=symbol,
            bids=sorted_bids,
            asks=sorted_asks
        )
        self.books[symbol] = book

        # Extract top of book as a tick and pass through main tick pipeline
        if book.best_bid and book.best_ask:
            tick = book.to_tick()
            await self.process_tick(tick)

        # Publish book update domain event
        event = BookUpdated(
            aggregate_id=symbol,
            payload={
                "symbol": symbol,
                "bid_levels": len(sorted_bids),
                "ask_levels": len(sorted_asks),
                "best_bid": str(book.best_bid.price) if book.best_bid else None,
                "best_ask": str(book.best_ask.price) if book.best_ask else None,
                "spread": str(book.spread) if book.spread else None
            }
        )
        await self.event_bus.publish(event)

    def _mirror_tick_to_cache(self, tick: Tick) -> None:
        """Queue a Redis write for this tick, without awaiting it.

        The task is held in `self._cache_tasks` until it completes. Without a strong
        reference the event loop may garbage-collect a pending task before it runs, which
        would silently drop writes - the failure mode would look like "Redis is randomly
        empty", not like an error.
        """
        try:
            task = asyncio.create_task(self.redis_cache.cache_tick(tick))
        except Exception as exc:                          # noqa: BLE001
            logger.error("could not schedule the Redis tick mirror for %s: %s",
                         tick.symbol, exc)
            return
        self._cache_tasks.add(task)
        task.add_done_callback(self._cache_tasks.discard)

        def _report(finished: "asyncio.Task") -> None:    # noqa: ANN001
            if finished.cancelled():
                return
            error = finished.exception()
            if error is not None:
                logger.error("Failed to cache tick in Redis: %s", error)

        task.add_done_callback(_report)

    def get_cached_ticks(self) -> Dict[str, Dict[str, Any]]:
        """The Redis view of every cached tick, for a reader outside this process.

        Returns {} when no cache is wired or the read fails, so a caller falls back to its
        own source rather than seeing an exception. This is the READ side of a cache that
        was previously written and never read - the write existed only to serve callers
        that could not reach the engine's memory.
        """
        if self.redis_cache is None:
            return {}
        getter = getattr(self.redis_cache, "get_all_ticks", None)
        if getter is None:
            return {}

        async def _read() -> Dict[str, Dict[str, Any]]:
            try:
                result = getter()
                if hasattr(result, "__await__"):
                    result = await result
                return dict(result or {})
            except Exception as exc:                      # noqa: BLE001
                logger.error("could not read cached ticks from Redis: %s", exc)
                return {}

        return asyncio.ensure_future(_read())             # type: ignore[return-value]

    def get_latest_tick(self, symbol: str) -> Optional[Tick]:
        """Get the latest cached tick for a symbol."""
        return self.ticks.get(symbol)

    def get_book(self, symbol: str) -> Optional[OrderBook]:
        """Get the current order book (DOM) for a symbol."""
        return self.books.get(symbol)

    def get_stats(self, symbol: str) -> Optional[TickStat]:
        """Get tick statistics for a symbol."""
        return self.stats.get(symbol)

    def _update_stats(self, tick: Tick) -> None:
        """Update per-symbol tick execution statistics."""
        if tick.symbol not in self.stats:
            self.stats[tick.symbol] = TickStat(symbol=tick.symbol)

        stat = self.stats[tick.symbol]
        stat.tick_count += 1
        stat.bid_count += 1
        stat.ask_count += 1
        stat.last_bid = tick.bid
        stat.last_ask = tick.ask
        stat.last_spread = tick.spread
        stat.last_update = tick.timestamp

        if stat.min_spread is None or tick.spread < stat.min_spread:
            stat.min_spread = tick.spread
        if stat.max_spread is None or tick.spread > stat.max_spread:
            stat.max_spread = tick.spread
