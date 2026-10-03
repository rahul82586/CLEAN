[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeUpdate

[Previous](DealsRangeAdd.md) | [Next](DealsRangeDelete.md)

# IMTConServerTrade::DealsRangeUpdate

Update the range of [deals](../../../Database-Interfaces/Trade/Deals.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeUpdate(
       const UINT          pos,       // Position of the range
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  IMTConServerTrade::DealsRangeUpdate(
       uint                pos,       // Position of the range
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade::DealsRangeUpdate(
       pos,                # Position of the range
       range               # Range object
       )

### Parameters

**pos**  
[in] Position of the range of deals in the list, starting with 0.

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
