[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeAdd

[Previous](OrdersRangeNext.md) | [Next](DealsRangeUpdate.md)

# IMTConServerTrade::DealsRangeAdd

Add a range of [deals](../../../Database-Interfaces/Trade/Deals.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeAdd(
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DealsRangeAdd(
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.DealsRangeAdd(
       range               # Range object
       )

### Parameters

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
