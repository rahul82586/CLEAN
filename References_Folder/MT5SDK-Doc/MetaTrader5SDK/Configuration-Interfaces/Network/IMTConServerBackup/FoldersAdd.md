[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersAdd

[Previous](SQLExportLastSync.md) | [Next](FoldersUpdate.md)

# IMTConServerBackup::FoldersAdd

Add a custom folder to the backup list.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersAdd(
       IMTConBackupFolder*  folder    // Folder object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersAdd(
       CIMTConBackupFolder  folder    // Folder object
       )

Python (Manager API)
    
    
    MTConServerBackup.FoldersAdd(
       folder               # Folder object
       )

### Parameters

**folder**  
[in] Custom folder objectIMTConBackupFolder.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.
