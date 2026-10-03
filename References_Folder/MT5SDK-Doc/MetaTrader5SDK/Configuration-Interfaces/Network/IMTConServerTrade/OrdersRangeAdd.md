[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OrdersRangeAdd

[Previous](LoginsRangeNext.md) | [Next](OrdersRangeUpdate.md)

# IMTConServerTrade::OrdersRangeAdd

Add a range of [orders](../../../Database-Interfaces/Trade/Orders.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::OrdersRangeAdd(
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OrdersRangeAdd(
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.OrdersRangeAdd(
       range               # Range object
       )

### Parameters

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
