"""011_tick_history

Revision ID: 011_tick_history
Revises: 010_sync_schema
Create Date: 2026-10-08 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = '011_tick_history'
down_revision = '010_sync_schema'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    if not insp.has_table('tick_history'):
        op.create_table(
            'tick_history',
            sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
            sa.Column('symbol', sa.String(length=32), nullable=False),
            sa.Column('bid', sa.Numeric(precision=20, scale=8), nullable=False),
            sa.Column('ask', sa.Numeric(precision=20, scale=8), nullable=False),
            sa.Column('spread', sa.Numeric(precision=20, scale=8), nullable=True),
            sa.Column('source', sa.String(length=32), nullable=True),
            sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
            sa.PrimaryKeyConstraint('id'),
        )
        op.create_index('ix_tick_history_symbol_ts', 'tick_history', ['symbol', 'timestamp'], unique=False)
        op.create_index('ix_tick_history_ts', 'tick_history', ['timestamp'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_tick_history_ts', table_name='tick_history')
    op.drop_index('ix_tick_history_symbol_ts', table_name='tick_history')
    op.drop_table('tick_history')
