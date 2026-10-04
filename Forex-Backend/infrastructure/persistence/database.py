import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# JSONB renders as JSON on SQLite so create_all works against the development
# and test database; PostgreSQL keeps the native type. This used to live inside
# the M4 proof script, which meant any OTHER sqlite consumer (tests, a fresh
# `create_tables()` call) died with "can't render element of type JSONB".
from sqlalchemy.dialects.postgresql import JSONB as _PG_JSONB
from sqlalchemy.ext.compiler import compiles as _sa_compiles


@_sa_compiles(_PG_JSONB, "sqlite")
def _compile_jsonb_sqlite(type_, compiler, **kw):  # noqa: ANN001
    return "JSON"
from sqlalchemy.orm import DeclarativeBase
import logging

logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
    pass

class DatabaseManager:
    """Manages PostgreSQL async connections."""

    def __init__(self, connection_string: str):
        # Connection limits are a PLAN setting on a managed database (Neon here), not
        # something we can read from the server, so a pool that is too generous fails
        # intermittently with "exceeded the quota" on whichever process starts last.
        #
        # The previous hardcoded 20 + 10 overflow allowed up to 30 connections from a
        # SINGLE process, which two processes exhaust. These defaults are sized for one
        # API process and can be raised per deployment through the environment rather
        # than by editing this file.
        pool_size = int(os.environ.get("DB_POOL_SIZE", "5"))
        max_overflow = int(os.environ.get("DB_MAX_OVERFLOW", "5"))

        self.engine = create_async_engine(
            connection_string,
            echo=False,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=30,
            # Recycle well below the idle timeout a managed pooler applies (Neon closes
            # idle connections), so we replace a connection before the server does.
            pool_recycle=int(os.environ.get("DB_POOL_RECYCLE", "300")),
            # A pooled connection can be closed by the pooler between checkouts.
            # pre_ping detects that and transparently replaces it, instead of the next
            # query failing with a closed-connection error.
            pool_pre_ping=True,
        )
        self.session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def create_tables(self):
        """Create all tables (for development). Use Alembic for production."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def close(self):
        await self.engine.dispose()
