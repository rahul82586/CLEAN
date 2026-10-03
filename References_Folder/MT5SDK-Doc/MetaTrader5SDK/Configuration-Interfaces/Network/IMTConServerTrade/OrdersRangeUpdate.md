[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OrdersRangeUpdate

[Previous](OrdersRangeAdd.md) | [Next](OrdersRangeDelete.md)

# IMTConServerTrade::OrdersRangeUpdate

Update the range of [orders](../../../Database-Interfaces/Trade/Orders.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::OrdersRangeUpdate(
       const UINT          pos,       // Position of the range
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OrdersRangeUpdate(
       uint                pos,       // Position of the range
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.OrdersRangeUpdate(
       pos,                # Position of the range
       range               # Range
       )

### Parameters

**pos**  
[in] Position of the range of orders in the list, starting with 0.

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
