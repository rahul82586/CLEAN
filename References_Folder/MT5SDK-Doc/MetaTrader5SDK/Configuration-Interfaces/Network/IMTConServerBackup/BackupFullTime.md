[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupFullTime

[Previous](BackupPath.md) | [Next](BackupPeriod.md)

# IMTConServerBackup::BackupFullTime

Get the time of creating full backup copies.

C++
    
    
    UINT  IMTConServerBackup::BackupFullTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerBackup.BackupFullTime()

Python (Manager API)
    
    
    MTConServerBackup.BackupFullTime

### Return Value

Time of creating full backup copies in minutes that have elapsed since 00:00.

# IMTConServerBackup::BackupFullTime

Set the time of creating full backup copies.

C++
    
    
    MTAPIRES  IMTConServerBackup::BackupFullTime(
       const UINT  time      // Backup creation time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.BackupFullTime(
       uint        time      // Backup creation time
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupFullTime

### Parameters

**time**  
[in] Time of full backup creation.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Time of backup creation is specified in minutes elapsed since 00:00.
