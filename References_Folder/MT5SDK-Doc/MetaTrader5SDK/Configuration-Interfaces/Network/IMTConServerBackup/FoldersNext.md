[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersNext

[Previous](FoldersTotal.md) | [Next](../IMTConBackupFolder.md)

# IMTConServerBackup::FoldersNext

Get a custom folder for which backup is enabled by index.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersNext(
       const UINT           pos,      // Folder position
       IMTConBackupFolder*  folder    // Range object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersNext(
       uint                 pos,      // Folder position
       CIMTConBackupFolder  folder    // Folder object
       )

Python (Manager API)
    
    
    MTConServerBackup.FoldersNext(
       pos,                 # Folder position
       folder               # Folder object
       )

### Parameters

**pos**  
[in] Folder position starting from 0.

**folder**  
[out] Custom folder object. The object must first be created using theIMTServerAPI::NetServerBackupFolderCreateorIMTAdminAPI::NetServerBackupFolderCreatemethod.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.

### Note

The method copies the description of the folder with the specified index to the folder object.
