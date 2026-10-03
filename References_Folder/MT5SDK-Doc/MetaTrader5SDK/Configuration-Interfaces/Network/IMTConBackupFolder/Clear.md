[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Clear

[Previous](Assign.md) | [Next](Folder.md)

# IMTConBackupFolder::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConBackupFolder::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConBackupFolder.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all field values ​and removes embedded objects.
