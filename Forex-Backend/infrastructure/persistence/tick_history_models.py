"""
TickHistory SQLAlchemy model.

Temporary 24-hour ring buffer.  The table is pruned on every flush so it
never grows beyond one day of ticks regardless of symbol count or rate.

This is an intentionally lightweight schema - no FKs, no partitioning.
A future architecture decision will decide the permanent store (TimescaleDB,
ClickHouse, Parquet files, etc.) and migrate from this table.
"""
from sqlalchemy import BigInteger, Column, DateTime, Index, Numeric, String, func

from infrastructure.persistence.database import Base


class TickHistoryModel(Base):
    """One row per tick.  Pruned to 24 h on every batch flush."""

    __tablename__ = "tick_history"

    # Surrogate PK using DB sequence - avoids UUID cost on every insert.
    id = Column(BigInteger, primary_key=True, autoincrement=True)

    symbol = Column(String(32), nullable=False, index=True)
    bid = Column(Numeric(20, 8), nullable=False)
    ask = Column(Numeric(20, 8), nullable=False)
    spread = Column(Numeric(20, 8), nullable=True)
    source = Column(String(32), nullable=True)

    # Broker quote timestamp (from the tick itself, not insert time).
    timestamp = Column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        # Most queries filter by symbol + time window.
        Index("ix_tick_history_symbol_ts", "symbol", "timestamp"),
        # Prune query only needs a time index.
        Index("ix_tick_history_ts", "timestamp"),
    )
