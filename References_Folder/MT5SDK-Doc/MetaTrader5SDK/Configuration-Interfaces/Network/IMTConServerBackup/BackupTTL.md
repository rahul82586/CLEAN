[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupTTL

[Previous](BackupPeriod.md) | [Next](BackupFlags.md)

# IMTConServerBackup::BackupTTL

Get the period of backup keeping.

C++
    
    
    UINT  IMTConServerBackup::BackupTTL()  const

.NET (Gateway/Manager API)
    
    
    EnBackupTTL  CIMTConServerBackup.BackupTTL()

Python (Manager API)
    
    
    MTConServerBackup.BackupTTL

### Return Value

A value of the [IMTConServerBackup::EnBackupTTL (#enbackupttl)](Enumerations.md#enbackupttl) enumeration.

# IMTConServerBackup::BackupTTL

Set the period of backup keeping.

C++
    
    
    MTAPIRES  IMTConServerBackup::BackupTTL(
       const UINT   period     // Time to keep backups
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.BackupTTL(
       EnBackupTTL  period     // Time to keep backups
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupTTL

### Parameters

**period**  
[in] Backup storing period is passed using theIMTConServerBackup::EnBackupTTLenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
