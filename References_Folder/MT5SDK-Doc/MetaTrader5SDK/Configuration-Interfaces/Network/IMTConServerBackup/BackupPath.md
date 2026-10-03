[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupPath

[Previous](MasterServer.md) | [Next](BackupFullTime.md)

# IMTConServerBackup::BackupPath

Get the path to save backups.

C++
    
    
    LPCWSTR  IMTConServerBackup::BackupPath()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServerBackup.BackupPath()

Python (Manager API)
    
    
    MTConServerBackup.BackupPath

### Return Value

If successful, it returns a pointer to a string with the backup saving path. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServerBackup](../IMTConServerBackup.md) object.

# IMTConServerBackup::BackupPath

Set the path to save backups.

C++
    
    
    MTAPIRES  IMTConServerBackup::BackupPath(
       LPCWSTR  path      // Path
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.BackupPath(
       string   path      // Path
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupPath

### Parameters

**path**  
[in] Path to save backups.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The path length is limited to 256 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
