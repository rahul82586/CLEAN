[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / Clear

[Previous](Assign.md) | [Next](DemoMode.md)

# IMTConServerTrade::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConServerTrade::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
