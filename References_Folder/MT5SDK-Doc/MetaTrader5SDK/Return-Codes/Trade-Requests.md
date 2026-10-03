[🏠 Document Start](../README.md) / [Return Codes](README.md) / Trade Requests

[Previous](Price-Data.md) | [Next](Dealer.md)

# Trade Requests

These codes are returned by the server during operations with [trade requests](../Manager-API/Administrator-Interface/Trade-Databases.md):

Constant | Value | Description  
MT_RET_REQUEST_INWAY | 10001 | Request is on the way.  
MT_RET_REQUEST_ACCEPTED | 10002 | Request accepted.  
MT_RET_REQUEST_PROCESS | 10003 | Request processed.  
MT_RET_REQUEST_REQUOTE | 10004 | Requote in response to the request.  
MT_RET_REQUEST_PRICES | 10005 | Prices in response to the request.  
MT_RET_REQUEST_REJECT | 10006 | Request rejected.  
MT_RET_REQUEST_CANCEL | 10007 | Request canceled.  
MT_RET_REQUEST_PLACED | 10008 | An order placed as a result of the request.  
MT_RET_REQUEST_DONE | 10009 | Request fulfilled.  
MT_RET_REQUEST_DONE_PARTIAL | 10010 | Request partially fulfilled.  
MT_RET_REQUEST_ERROR | 10011 | Common error of request.  
MT_RET_REQUEST_TIMEOUT | 10012 | Request timed out.  
MT_RET_REQUEST_INVALID | 10013 | Invalid request.  
MT_RET_REQUEST_INVALID_VOLUME | 10014 | Invalid volume.  
MT_RET_REQUEST_INVALID_PRICE | 10015 | Invalid price.  
MT_RET_REQUEST_INVALID_STOPS | 10016 | Wrong stop levels or price.  
MT_RET_REQUEST_TRADE_DISABLED | 10017 | Trade is disabled.  
MT_RET_REQUEST_MARKET_CLOSED | 10018 | Market is closed.  
MT_RET_REQUEST_NO_MONEY | 10019 | Not enough money.  
MT_RET_REQUEST_PRICE_CHANGED | 10020 | Price has changed.  
MT_RET_REQUEST_PRICE_OFF | 10021 | No price.  
MT_RET_REQUEST_INVALID_EXP | 10022 | Invalid order expiration.  
MT_RET_REQUEST_ORDER_CHANGED | 10023 | Order has been changed.  
MT_RET_REQUEST_TOO_MANY | 10024 | Too many trade requests. For example, this error can be returned in response to an attempt to send more than 128 trade requests from one Manager API instance.  
MT_RET_REQUEST_NO_CHANGES | 10025 | Request does not contain changes.  
MT_RET_REQUEST_AT_DISABLED_SERVER | 10026 | Autotrading disabled on the server.  
MT_RET_REQUEST_AT_DISABLED_CLIENT | 10027 | Autotrading disabled on the client side.  
MT_RET_REQUEST_LOCKED | 10028 | Request blocked by the dealer.  
MT_RET_REQUEST_FROZEN | 10029 | Modification failed due to order or position being close to market.  
MT_RET_REQUEST_INVALID_FILL | 10030 | Fill mode is not supported.  
MT_RET_REQUEST_CONNECTION | 10031 | No connection.  
MT_RET_REQUEST_ONLY_REAL | 10032 | Allowed only for real accounts.  
MT_RET_REQUEST_LIMIT_ORDERS | 10033 | Reached the limit on the number of orders.  
MT_RET_REQUEST_LIMIT_VOLUME | 10034 | Reached the volume limit.  
MT_RET_REQUEST_INVALID_ORDER | 10035 | Invalid or prohibited order type.  
MT_RET_REQUEST_POSITION_CLOSED | 10036 | Position is already closed. For example, this error appears when attempting to modify the stop levels of an already closed position.  
MT_RET_REQUEST_EXECUTION_SKIPPED | 10037 | Used for internal purposes.  
MT_RET_REQUEST_INVALID_CLOSE_VOLUME | 10038 | Volume to be closed exceeds the current volume of the position.  
MT_RET_REQUEST_CLOSE_ORDER_EXIST | 10039 | Order to close the position already exists. The error may appear in the hedging mode:

  * when trying to closed a position with an opposite one in case there's already an order to close that position
  * when trying to close the entire position or a part of it in case the total volume of existing orders to close it and the newly placed order exceeds the current volume of the position

  
MT_RET_REQUEST_LIMIT_POSITIONS | 10040 | The number of open positions simultaneously present on an account can be limited by the settings of a group. After a limit is reached, the server returns the MT_TRADE_RETCODE_REQUEST_LIMIT_POSITIONS error when attempting to place an order. The limitation operates differently depending on the position accounting type:

  * Netting — number of open positions is considered. When a limit is reached, the platform disables placing new orders whose execution may increase the number of open positions. In fact, the platform allows placing orders only for the symbols that already have open positions. The current pending orders are not considered since their execution may lead to changes in the current positions but it cannot increase their number.
  * Hedging — pending orders are considered together with open positions, since a pending order activation always leads to opening a new position. When a limit is reached, the platform disables placing both new market orders for opening positions and pending orders.

  
MT_RET_REQUEST_REJECT_CANCEL | 10041 | Request rejected, order canceled. This code is returned when the action [IMTConRoute::ACTION_CANCEL_ORDER (#enrouteaction)](../Configuration-Interfaces/Routing/IMTConRoute/Enumerations.md#enrouteaction) in a routing rule is applied.  
MT_RET_REQUEST_LONG_ONLY | 10042 | The request is rejected, because the "Only long positions are allowed" rule is set for the symbol ([IMTConSymbol::TRADE_LONGONLY (#entrademode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entrademode)).  
MT_RET_REQUEST_SHORT_ONLY | 10043 | The request is rejected, because the "Only short positions are allowed" rule is set for the symbol ([IMTConSymbol::TRADE_SHORTONLY (#entrademode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entrademode)).  
MT_RET_REQUEST_CLOSE_ONLY | 10044 | The request is rejected, because the "Only position closing is allowed" rule is set for the symbol ([IMTConSymbol::TRADE_CLOSEONLY (#entrademode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entrademode)).  
MT_RET_REQUEST_PROHIBITED_BY_FIFO | 10045 | Position closure is not allowed by the FIFO rule. It is used for the groups with the enabled [IMTConGroup::TRADEFLAGS_FIFO_CLOSE (#entradeflags)](../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags) option, according to which all positions should be closed strictly in the order in which they were opened: the oldest one should be closed first, then the next one, etc.  
MT_RET_REQUEST_HEDGE_PROHIBITED | 10046 | Opening of a position or placing of a pending order is not possible because hedge positions are prohibited. The error is returned if a user tries to execute a trading operation in the case the [IMTConGroup::TRADEFLAGS_HEDGE_PROHIBIT (#entradeflags)](../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags) flag is enabled for the group and the user already has an opposite order or position for the same symbol.
