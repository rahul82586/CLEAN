[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionBackupRestore

[Previous](PositionBackupRequest.md) | [Next](PositionCheck.md)

# IMTAdminAPI::PositionBackupRestore

Restore a position from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionBackupRestore(
       IMTPosition*  position      // A position to restore
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionBackupRestore(
       CIMTPosition  position      // A position to restore
       )

Python
    
    
    AdminAPI.PositionBackupRestore(
       MTPosition    position      # A position to restore
       )

### Parameters

**position**  
[in] An object of the position to restore.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Restored positions are not deleted from the backup copy When restoring a position, [deals](../Deals.md) that resulted in that position are not recovered.
