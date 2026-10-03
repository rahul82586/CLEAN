[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersDelete

[Previous](FoldersUpdate.md) | [Next](FoldersClear.md)

# IMTConServerBackup::FoldersDelete

Delete a custom folder from the backup list.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersDelete(
       const UINT  pos      // Folder position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersDelete(
       uint        pos      // Folder position
       )

Python (Manager API)
    
    
    MTConServerBackup.FoldersDelete(
       pos         # Folder position
       )

### Parameters

**pos**  
[in] Folder position starting from 0.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.

### Note

If the object is not found, the [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error code is returned.
