[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupPeriod

[Previous](BackupFullTime.md) | [Next](BackupTTL.md)

# IMTConServerBackup::BackupPeriod

Get the frequency of backup creation.

C++
    
    
    UINT  IMTConServerBackup::BackupPeriod()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerBackup.BackupPeriod()

Python (Manager API)
    
    
    MTConServerBackup.BackupPeriod

### Return Value

A value of the [IMTConServer::EnBackupPeriod (#enbackupperiod)](Enumerations.md#enbackupperiod) enumeration.

# IMTConServerBackup::BackupPeriod

Set the frequency of backup creation.

C++
    
    
    MTAPIRES  IMTConServerBackup::BackupPeriod(
       const UINT  period      // Frequency of backup creation
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.BackupPeriod(
       uint        period      // Frequency of backup creation
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupPeriod

### Parameters

**period**  
[in] The frequency of backup creation is passed using theIMTConServerBackup::EnBackupPeriodenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
