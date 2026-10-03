[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Clear

[Previous](Assign.md) | [Next](Type.md)

# IMTConServer::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConServer::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
