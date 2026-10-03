[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OrdersRangeNext

[Previous](OrdersRangeTotal.md) | [Next](DealsRangeAdd.md)

# IMTConServerTrade::OrdersRangeNext

Get a range of [orders](../../../Database-Interfaces/Trade/Orders.md) by the index.

C++
    
    
    MTAPIRES  IMTConServerTrade::OrdersRangeNext(
       const UINT          pos,       // Position of the range
       IMTConServerRange*  range      // Range object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OrdersRangeNext(
       uint                pos,       // Position of the range
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.OrdersRangeNext(
       pos,                # Position of the range
       range               # Range object
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**range**  
[out] An object of the range. The 'range' object must first be created using theIMTAdminAPI::NetServerRangeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the range of orders with a specified index to the range object.
