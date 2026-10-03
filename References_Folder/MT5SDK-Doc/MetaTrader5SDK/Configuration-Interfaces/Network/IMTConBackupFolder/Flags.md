[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Flags

[Previous](Filter.md) | [Next](../IMTConServerAccess.md)

# IMTConBackupFolder::BackupFlags

Get additional folder backup settings.

C++
    
    
    UINT64  IMTConBackupFolder::BackupFlags()  const

.NET (Gateway/Manager API)
    
    
    EnBackupFlags  CIMTConBackupFolder.BackupFlags()

Python (Manager API)
    
    
    MTConBackupFolder.BackupFlags

### Return Value

A value of the [IMTConBackupFolder::EnBackupFlags (#enbackupflags)](Enumerations.md#enbackupflags) enumeration.

# IMTConBackupFolder::BackupFlags

Set additional folder backup settings.

C++
    
    
    MTAPIRES  IMTConBackupFolder::BackupFlags(
       const UINT64   flags     // Backup flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConBackupFolder.BackupFlags(
       EnBackupFlags  flags     // Backup flags
       )

Python (Manager API)
    
    
    MTConBackupFolder.BackupFlags

### Parameters

**flags**  
[in] TheIMTConBackupFolder::EnBackupFlagsenumeration is used to pass the flags.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
