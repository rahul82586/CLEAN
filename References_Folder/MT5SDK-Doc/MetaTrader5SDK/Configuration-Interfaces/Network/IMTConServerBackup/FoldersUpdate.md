[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersUpdate

[Previous](FoldersAdd.md) | [Next](FoldersDelete.md)

# IMTConServerBackup::FoldersUpdate

Edit a custom folder in the backup list.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersUpdate(
       const UINT           pos,      // Folder position
       IMTConBackupFolder*  folder    // Folder object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersUpdate(
       uint                 pos,      // Folder position
       CIMTConBackupFolder  folder    // Folder object
       )

Python (Manager API)
    
    
    MTConServerBackup.FoldersUpdate(
       pos,                 # Folder position
       folder               # Folder object
       )

### Parameters

**pos**  
[in] Position of a folder in the list starting from 0.

**folder**  
[in] Custom folder objectIMTConBackupFolder.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.
