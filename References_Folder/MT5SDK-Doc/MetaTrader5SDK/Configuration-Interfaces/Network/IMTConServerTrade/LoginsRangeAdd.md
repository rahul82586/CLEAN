[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / LoginsRangeAdd

[Previous](OvermonthTimePrev.md) | [Next](LoginsRangeUpdate.md)

# IMTConServerTrade::LoginsRangeAdd

Add a range of [logins](../../../Database-Interfaces/Users.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::LoginsRangeAdd(
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.LoginsRangeAdd(
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.LoginsRangeAdd(
       range               # Range object
       )

### Parameters

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
