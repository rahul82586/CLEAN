[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeDelete

[Previous](DealsRangeUpdate.md) | [Next](DealsRangeClear.md)

# IMTConServerTrade::DealsRangeDelete

Deletes a range of [deals](../../../Database-Interfaces/Trade/Deals.md) at the specified index.

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeDelete(
       const UINT  pos      // Position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DealsRangeDelete(
       uint        pos      // Position of the range
       )

Python (Manager API)
    
    
    MTConServerTrade.DealsRangeDelete(
       pos         # Position of the ran
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
