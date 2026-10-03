[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Masks

[Previous](Folder.md) | [Next](Filter.md)

# IMTConBackupFolder::Masks

Get a list or a wildcard pattern of files to back up.

C++
    
    
    LPCWSTR  IMTConBackupFolder::Masks()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConBackupFolder.Masks()

Python (Manager API)
    
    
    MTConBackupFolder.Masks

### Return Value

If successful, a pointer to a string with the list or wildcard pattern is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServerBackup](../IMTConServerBackup.md) object.

# IMTConBackupFolder::Masks

Set a list or a wildcard pattern of files to back up.

C++
    
    
    MTAPIRES  IMTConBackupFolder::Masks(
       LPCWSTR  masks      // list of files or wildcard pattern
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConBackupFolder.Masks(
       string   masks      // list of files or wildcard pattern
       )

Python (Manager API)
    
    
    MTConBackupFolder.Masks

### Parameters

**path**  
[in] A comma separated list of backed-up files. File names can be described using wildcard patterns. If the list is specified, only listed files matching the mask are copied. Otherwise, all files from the directory will be copied.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the wildcard pattern is 256 characters (with the newline character). If a string of a greater length is assigned, it will be cut to this length.
