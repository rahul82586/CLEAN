"""MT5 trade/request return codes, verbatim from the MetaQuotes SDK docs.

WHY THIS MODULE EXISTS
----------------------
Before this file, every retcode in the API layer was an inline integer literal
(``10011``, ``10013``, ``10014``, ``10015``, ``10021``) with the MT5 constant
name only as a trailing comment. That drifted: ``api/routers/manager/trading.py``
returned ``10011`` for an invalid account with the comment
``# TRADE_RETCODE_INVALID_ACCOUNT``, but per the SDK docs 10011 is
``MT_RET_REQUEST_ERROR`` ("Common error of request"). Invalid account is an
*authentication* code (1001), not a trade-request code. A wrong retcode is not a
cosmetic bug: it is the only machine-readable thing an LP/bridge client gets back.

SOURCE OF TRUTH
---------------
``References_Folder/MT5SDK-Doc/MetaTrader5SDK/Return-Codes/Trade-Requests.md``
``References_Folder/MT5SDK-Doc/MetaTrader5SDK/Return-Codes/Authentication.md``
``References_Folder/MT5SDK-Doc/MetaTrader5SDK/Return-Codes/Common-errors.md``
``References_Folder/MT5SDK-Doc/MetaTrader5SDK/Return-Codes/Successful-completion.md``

NOTE ON NAMING: the SDK calls these ``MT_RET_REQUEST_*`` / ``MT_RET_AUTH_*``.
The MQL5 client-side spelling ``TRADE_RETCODE_*`` does NOT appear in this corpus,
so it is deliberately not used here.

The numeric values are the wire contract with MT5-side clients. Do not renumber
them to "tidy up" - a client switching on 10019 expects "not enough money".
"""
from enum import IntEnum


class Retcode(IntEnum):
    """MT5 return codes (``MT_RET_*``). Values are the documented wire numbers."""

    # --- Successful completion (Return-Codes/Successful-completion.md) ------
    OK = 0                              # MT_RET_OK

    # --- Common errors (Return-Codes/Common-errors.md) ---------------------
    ERR_FREQUENT = 12                   # MT_RET_ERR_FREQUENT - too frequent requests
    ERR_NOTFOUND = 13                   # MT_RET_ERR_NOTFOUND - not found

    # --- Authentication / connection (Return-Codes/Authentication.md) ------
    # These are what an unknown/disabled ACCOUNT must return. A trade-request
    # code is the wrong family here.
    AUTH_ACCOUNT_INVALID = 1001         # MT_RET_AUTH_ACCOUNT_INVALID
    AUTH_ACCOUNT_DISABLED = 1002        # MT_RET_AUTH_ACCOUNT_DISABLED
    AUTH_SERVER_BUSY = 1018             # MT_RET_AUTH_SERVER_BUSY
    AUTH_ACCOUNT_UNKNOWN = 1020         # MT_RET_AUTH_ACCOUNT_UNKNOWN

    # --- Trade requests (Return-Codes/Trade-Requests.md) -------------------
    REQUEST_ACCEPTED = 10002            # MT_RET_REQUEST_ACCEPTED
    REQUEST_REQUOTE = 10004             # MT_RET_REQUEST_REQUOTE
    REQUEST_REJECT = 10006              # MT_RET_REQUEST_REJECT
    REQUEST_DONE = 10009                # MT_RET_REQUEST_DONE
    REQUEST_ERROR = 10011               # MT_RET_REQUEST_ERROR (common error)
    REQUEST_TIMEOUT = 10012             # MT_RET_REQUEST_TIMEOUT
    REQUEST_INVALID = 10013             # MT_RET_REQUEST_INVALID
    INVALID_VOLUME = 10014              # MT_RET_REQUEST_INVALID_VOLUME
    INVALID_PRICE = 10015               # MT_RET_REQUEST_INVALID_PRICE
    INVALID_STOPS = 10016               # MT_RET_REQUEST_INVALID_STOPS
    TRADE_DISABLED = 10017              # MT_RET_REQUEST_TRADE_DISABLED
    MARKET_CLOSED = 10018               # MT_RET_REQUEST_MARKET_CLOSED
    NO_MONEY = 10019                    # MT_RET_REQUEST_NO_MONEY
    PRICE_CHANGED = 10020               # MT_RET_REQUEST_PRICE_CHANGED
    PRICE_OFF = 10021                   # MT_RET_REQUEST_PRICE_OFF (no price)
    TOO_MANY = 10024                    # MT_RET_REQUEST_TOO_MANY
    AT_DISABLED_SERVER = 10026          # MT_RET_REQUEST_AT_DISABLED_SERVER
    LOCKED = 10028                      # MT_RET_REQUEST_LOCKED
    FROZEN = 10029                      # MT_RET_REQUEST_FROZEN (freeze level)
    INVALID_FILL = 10030                # MT_RET_REQUEST_INVALID_FILL
    LIMIT_ORDERS = 10033                # MT_RET_REQUEST_LIMIT_ORDERS
    LIMIT_VOLUME = 10034                # MT_RET_REQUEST_LIMIT_VOLUME
    LIMIT_POSITIONS = 10040             # MT_RET_REQUEST_LIMIT_POSITIONS
    LONG_ONLY = 10042                   # MT_RET_REQUEST_LONG_ONLY
    SHORT_ONLY = 10043                  # MT_RET_REQUEST_SHORT_ONLY
    CLOSE_ONLY = 10044                  # MT_RET_REQUEST_CLOSE_ONLY
    PROHIBITED_BY_FIFO = 10045          # MT_RET_REQUEST_PROHIBITED_BY_FIFO
    HEDGE_PROHIBITED = 10046            # MT_RET_REQUEST_HEDGE_PROHIBITED


#: Human-readable text, matching the SDK's "Description" column. Used for the
#: ``message`` field so a caller is not left decoding a bare number.
DESCRIPTIONS = {
    Retcode.OK: "Request fulfilled",
    Retcode.ERR_FREQUENT: "Too frequent requests",
    Retcode.ERR_NOTFOUND: "Not found",
    Retcode.AUTH_ACCOUNT_INVALID: "Invalid account",
    Retcode.AUTH_ACCOUNT_DISABLED: "Account disabled",
    Retcode.AUTH_SERVER_BUSY: "The server is busy",
    Retcode.AUTH_ACCOUNT_UNKNOWN: "Unknown account",
    Retcode.REQUEST_ACCEPTED: "Request accepted",
    Retcode.REQUEST_REQUOTE: "Requote in response to the request",
    Retcode.REQUEST_REJECT: "Request rejected",
    Retcode.REQUEST_DONE: "Request fulfilled",
    Retcode.REQUEST_ERROR: "Common error of request",
    Retcode.REQUEST_TIMEOUT: "Request timed out",
    Retcode.REQUEST_INVALID: "Invalid request",
    Retcode.INVALID_VOLUME: "Invalid volume",
    Retcode.INVALID_PRICE: "Invalid price",
    Retcode.INVALID_STOPS: "Wrong stop levels or price",
    Retcode.TRADE_DISABLED: "Trade is disabled",
    Retcode.MARKET_CLOSED: "Market is closed",
    Retcode.NO_MONEY: "Not enough money",
    Retcode.PRICE_CHANGED: "Price has changed",
    Retcode.PRICE_OFF: "No price",
    Retcode.TOO_MANY: "Too many trade requests",
    Retcode.AT_DISABLED_SERVER: "Autotrading disabled on the server",
    Retcode.LOCKED: "Request blocked by the dealer",
    Retcode.FROZEN: "Modification failed: order or position is close to market",
    Retcode.INVALID_FILL: "Fill mode is not supported",
    Retcode.LIMIT_ORDERS: "Reached the limit on the number of orders",
    Retcode.LIMIT_VOLUME: "Reached the volume limit",
    Retcode.LIMIT_POSITIONS: "Reached the limit on the number of positions",
    Retcode.LONG_ONLY: "Only long positions are allowed",
    Retcode.SHORT_ONLY: "Only short positions are allowed",
    Retcode.CLOSE_ONLY: "Only position closing is allowed",
    Retcode.PROHIBITED_BY_FIFO: "Position closing is prohibited by FIFO rule",
    Retcode.HEDGE_PROHIBITED: "Hedging is prohibited",
}


def describe(code: "Retcode | int") -> str:
    """Return the SDK description for a code, or a safe fallback.

    Never raises: a logging/marshalling helper that can blow up is worse than a
    generic string.
    """
    try:
        return DESCRIPTIONS[Retcode(int(code))]
    except (ValueError, KeyError, TypeError):
        return f"Unknown return code {code}"


def is_success(code: "Retcode | int") -> bool:
    """True only for a fulfilled/accepted request (MT_RET_OK / DONE / ACCEPTED)."""
    try:
        value = int(code)
    except (ValueError, TypeError):
        return False
    return value in (int(Retcode.OK), int(Retcode.REQUEST_DONE), int(Retcode.REQUEST_ACCEPTED))


__all__ = ["Retcode", "DESCRIPTIONS", "describe", "is_success"]
