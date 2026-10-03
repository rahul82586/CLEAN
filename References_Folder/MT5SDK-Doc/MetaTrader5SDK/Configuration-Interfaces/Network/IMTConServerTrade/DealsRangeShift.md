[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeShift

[Previous](DealsRangeClear.md) | [Next](DealsRangeTotal.md)

# IMTConServerTrade::DealsRangeShift

Move the range of [deals](../../../Database-Interfaces/Trade/Deals.md) in the list.

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeShift(
       const UINT  pos,       // Position of the range
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DealsRangeShift(
       uint        pos,       // Position of the range
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServerTrade.DealsRangeShift(
       pos,        # Position of the range
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
