[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersClear

[Previous](FoldersDelete.md) | [Next](FoldersShift.md)

# IMTConServerBackup::FoldersClear

Clear the list of custom folders for which backup is enabled.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersClear()

Python (Manager API)
    
    
    MTConServerBackup.FoldersClear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.

### Note

The method deletes all custom folders from the backup list.
