[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / FoldersShift

[Previous](FoldersClear.md) | [Next](FoldersTotal.md)

# IMTConServerBackup::FoldersShift

Change the position of the backuped custom folder in the list.

C++
    
    
    MTAPIRES  IMTConServerBackup::FoldersShift(
       const UINT  pos,       // Folder position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.FoldersShift(
       uint        pos,       // Folder position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServerBackup.FoldersShift(
       pos,        # Folder position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Folder position starting from 0.

**shift**  
[in] Shift relative to the current position. A negative value indicates shift towards the list beginning, and a negative one shifts the value towards the end.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates successful execution. Otherwise, an error code is returned.
