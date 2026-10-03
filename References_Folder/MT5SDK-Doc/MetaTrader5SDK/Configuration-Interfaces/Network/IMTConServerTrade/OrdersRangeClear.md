[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OrdersRangeClear

[Previous](OrdersRangeDelete.md) | [Next](OrdersRangeShift.md)

# IMTConServerTrade::OrdersRangeClear

Clear the range of [orders](../../../Database-Interfaces/Trade/Orders.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::OrdersRangeClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OrdersRangeClear()

Python (Manager API)
    
    
    MTConServerTrade.OrdersRangeClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of ranges of orders of the server.
