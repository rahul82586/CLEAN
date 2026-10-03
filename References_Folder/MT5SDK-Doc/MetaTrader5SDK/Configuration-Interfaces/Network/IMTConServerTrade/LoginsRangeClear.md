[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / LoginsRangeClear

[Previous](LoginsRangeDelete.md) | [Next](LoginsRangeShift.md)

# IMTConServerTrade::LoginsRangeClear

Clear the range of [logins](../../../Database-Interfaces/Users.md).

C++
    
    
    MTAPIRES  IMTConServerTrade::LoginsRangeClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.LoginsRangeClear()

Python (Manager API)
    
    
    MTConServerTrade.LoginsRangeClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of ranges of all the logins of the server.
