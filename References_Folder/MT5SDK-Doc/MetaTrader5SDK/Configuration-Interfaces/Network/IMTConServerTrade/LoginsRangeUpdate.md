[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / LoginsRangeUpdate

[Previous](LoginsRangeAdd.md) | [Next](LoginsRangeDelete.md)

# IMTConServerTrade::LoginsRangeUpdate

Update the range of [logins](../../../Database-Interfaces/Users.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::LoginsRangeUpdate(
       const UINT          pos,       // Position of the range
       IMTConServerRange*  range      // Range object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.LoginsRangeUpdate(
       uint                pos,       // Position of the range
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.LoginsRangeUpdate(
       pos,                # Position of the range
       range               # Range object
       )

### Parameters

**pos**  
[in] Position of the range of logins in the list, starting with 0.

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
