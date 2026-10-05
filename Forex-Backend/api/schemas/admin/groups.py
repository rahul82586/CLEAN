"""Admin-plane request schemas for the Group object (identity plane, step 4).

Conventions carried from the rest of the API (ENDPOINTS.md §0):
* every decimal accepts a STRING (JSON floats lose trailing zeros, and this is
  money) - Pydantic coerces "50.00" and 50 alike into Decimal;
* margin thresholds are PERCENT (MT5 convention);
* `account_type` is omitted by default and DERIVED from the name - an explicit
  value that contradicts the name is refused by the handler (400), not by
  validation, so the reason arrives in the domain's words.
"""
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

# N10: the constants live in core.domains.accounts.thresholds;
# the duplicate import from account.py shadowed the one below.
from core.domains.accounts.thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)


class GroupCreateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str = Field(..., description="MT5 group path, e.g. real\\real (or real/real)")
    account_type: Optional[str] = Field(
        None,
        description="Omit to derive from the name (MT5 rule). Explicit values may not "
        "contradict the derivation, except contest-on-demo.",
    )
    currency: str = "USD"
    leverage_default: int = 100
    leverage_max: int = 500
    margin_call_level: Decimal = DEFAULT_MARGIN_CALL_LEVEL  # R11
    stop_out_level: Decimal = DEFAULT_STOP_OUT_LEVEL  # R11
    trade_allowed: bool = True


class GroupUpdateRequest(BaseModel):
    """Partial update - only supplied fields change; an update that changes
    nothing is refused (MT_RET_REQUEST_NO_CHANGES). The name is the path key
    and can never be updated."""

    model_config = ConfigDict(extra="forbid")

    currency: Optional[str] = None
    currency_digits: Optional[int] = None
    leverage_default: Optional[int] = None
    leverage_max: Optional[int] = None
    margin_call_level: Optional[Decimal] = None
    stop_out_level: Optional[Decimal] = None
    limit_orders: Optional[int] = None
    limit_positions: Optional[int] = None
    limit_symbols: Optional[int] = None
    trade_allowed: Optional[bool] = None
    allowed_symbols: Optional[List[str]] = None
    is_active: Optional[bool] = None
