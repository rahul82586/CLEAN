[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Folder

[Previous](Clear.md) | [Next](Masks.md)

# IMTConBackupFolder::Folder

Get the path to the backed-up user folder.

C++
    
    
    LPCWSTR  IMTConBackupFolder::Folder()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConBackupFolder.Folder()

Python (Manager API)
    
    
    MTConBackupFolder.Folder

### Return Value

If successful, it returns a pointer to a string with the folder path. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServerBackup](../IMTConServerBackup.md) object.

# IMTConBackupFolder::Folder

Set the path to the backed-up user folder.

C++
    
    
    MTAPIRES  IMTConBackupFolder::Folder(
       LPCWSTR  folder    // Path
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConBackupFolder.Folder(
       string   folder    // Path
       )

Python (Manager API)
    
    
    MTConBackupFolder.Folder

### Parameters

**path**  
[in] Path to the backed-up user folder.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Paths are specified relative to the installation directory of the primary server.
