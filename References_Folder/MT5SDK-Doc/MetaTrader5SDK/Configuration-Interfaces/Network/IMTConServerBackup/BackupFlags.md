[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupFlags

[Previous](BackupTTL.md) | [Next](BackupLastSync.md)

# IMTConServerBackup::BackupFlags

Gets backup flags.

C++
    
    
    UINT64  IMTConServerBackup::BackupFlags()  const

.NET (Gateway/Manager API)
    
    
    EnBackupFlags  IMTConServerBackup::BackupFlags()

Python (Manager API)
    
    
    MTConServerBackup.BackupLastSync

### Return Value

A value from the [IMTConServerBackup::EnBackupFlags (#enbackupflags)](Enumerations.md#enbackupflags) enumeration.

# IMTConServerBackup::BackupFlags

Sets backup flags.

C++
    
    
    MTAPIRES  IMTConServerBackup::BackupFlags(
       const UINT64   flags     // Backup flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.BackupFlags(
       EnBackupFlags  flags     // Backup flags
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupLastSync

### Parameters

**flags**  
[in] Backup flags are passed using theIMTConServerBackup::EnBackupFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
