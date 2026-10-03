[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / Clear

[Previous](Assign.md) | [Next](MasterServer.md)

# IMTConServerBackup::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConServerBackup::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
