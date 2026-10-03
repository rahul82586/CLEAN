[🏠 Document Start](../README.md) / [Return Codes](README.md) / Trade management

[Previous](User-management.md) | [Next](Report-Generation.md)

# Trade management

This group of codes is returned by the server when working with [a database of trades](../Manager-API/Administrator-Interface/Trade-Databases.md):

Constant | Value | Description  
MT_RET_TRADE_LIMIT_REACHED | 4001 | Reached the limit on the number of orders or deals.  
MT_RET_TRADE_ORDER_EXIST | 4002 | The order already exists.  
MT_RET_TRADE_ORDER_EXHAUSTED | 4003 | The range of orders has been exhausted.  
MT_RET_TRADE_DEAL_EXHAUSTED | 4004 | The range of deals has been exhausted.  
MT_RET_TRADE_MAX_MONEY | 4005 | Reached the limit on the amount of money.  
MT_RET_TRADE_DEAL_EXIST | 4006 | A deal with this ticket already exists on this trade server.  
MT_RET_TRADE_ORDER_PROHIBITED | 4007 | The order identifier is reserved for use on another trade server.  
MT_RET_TRADE_DEAL_PROHIBITED | 4008 | The deal identifier is reserved for use on another trade server.  
MT_RET_TRADE_SPLIT_VOLUME | 4009 | The position volume will become zero after the split operation. The error is used in the following methods:

  * [IMTServerAPI::PositionSplit](../Server-API/Main-API-Interface/Trade/Positions/PositionSplit.md)
  * [IMTAdmin::PositionSplit](../Manager-API/Administrator-Interface/Trade-Databases/Positions/PositionSplit.md)
  * [IMTManager::PositionSplit](../Manager-API/Manager-Interface/Trade-Databases/Positions/PositionSplit.md)

If the split operation will cause a position volume to become zero, the split will not be performed, and the MT_RET_TRADE_SPLIT_VOLUME error code will be added to the 'results' return array.
