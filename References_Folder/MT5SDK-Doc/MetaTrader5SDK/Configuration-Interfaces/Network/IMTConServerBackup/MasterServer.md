[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / MasterServer

[Previous](Clear.md) | [Next](BackupPath.md)

# IMTConServerBackup::MasterServer

Get the ID of the server to make a backup of.

C++
    
    
    UINT64  IMTConServerBackup::MasterServer()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerBackup.MasterServer()

Python (Manager API)
    
    
    MTConServerBackup.MasterServer

### Return Value

ID of the server to backup.

# IMTConServerBackup::MasterServer

Set the ID of the server to make a backup of.

C++
    
    
    MTAPIRES  IMTConServerBackup::MasterServer(
       const UINT64  id      // ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.MasterServer(
       ulong         id      // ID
       )

Python (Manager API)
    
    
    MTConServerBackup.MasterServer

### Parameters

**id**  
[in] ID of the server to backup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
