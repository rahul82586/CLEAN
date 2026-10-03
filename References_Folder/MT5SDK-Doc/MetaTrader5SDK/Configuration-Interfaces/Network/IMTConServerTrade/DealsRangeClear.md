[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeClear

[Previous](DealsRangeDelete.md) | [Next](DealsRangeShift.md)

# IMTConServerTrade::DealsRangeClear

Clear the range of [deals](../../../Database-Interfaces/Trade/Deals.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DealsRangeClear()

Python (Manager API)
    
    
    MTConServerTrade.DealsRangeClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of ranges of all the deals of the server.
