"""MT5's margin thresholds, in PERCENT - defined ONCE.

R11: these existed as FIVE different literals. The `MarginProfile` dataclass defaulted to
80/50 while the loader, the persistence mapper and the live MT5 export all said 50/30, so an
account whose group failed to load was stopped out at 50% instead of 30% - it kept trading 20
percentage points past the configured floor. Falling back to a MORE PERMISSIVE number is the
wrong direction for a risk system.

The live export carries `MarginCall "50.00"` and `MarginStopOut "30.00"`; these constants are
those numbers.

This module is a LEAF on purpose: it imports nothing from the package, so `account.py` and
`value_objects.py` can both read it without a circular import.
"""
from decimal import Decimal

#: MT5 MarginCall, percent. (live export: "50.00")
DEFAULT_MARGIN_CALL_LEVEL = Decimal("50")

#: MT5 MarginStopOut, percent. (live export: "30.00")
DEFAULT_STOP_OUT_LEVEL = Decimal("30")
