[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / LoginsRangeDelete

[Previous](LoginsRangeUpdate.md) | [Next](LoginsRangeClear.md)

# IMTConServerTrade::LoginsRangeDelete

Delete a range of [logins](../../../Database-Interfaces/Users.md) by the index.

C++
    
    
    MTAPIRES  IMTConServerTrade::LoginsRangeDelete(
       const UINT  pos      // Position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.LoginsRangeDelete(
       uint        pos      // Position of the range
       )

Python (Manager API)
    
    
    MTConServerTrade.LoginsRangeDelete(
       pos         # Position of the range
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
