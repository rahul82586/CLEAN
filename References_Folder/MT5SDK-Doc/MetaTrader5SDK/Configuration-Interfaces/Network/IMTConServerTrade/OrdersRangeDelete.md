[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OrdersRangeDelete

[Previous](OrdersRangeUpdate.md) | [Next](OrdersRangeClear.md)

# IMTConServerTrade::OrdersRangeDelete

Delete a range of [orders](../../../Database-Interfaces/Trade/Orders.md) by the index.

C++
    
    
    MTAPIRES  IMTConServerTrade::OrdersRangeDelete(
       const UINT  pos      // Position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OrdersRangeDelete(
       uint        pos      // Position of the range
       )

Python (Manager API)
    
    
    MTConServerTrade.OrdersRangeDelete(
       pos         # Position of the range
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
