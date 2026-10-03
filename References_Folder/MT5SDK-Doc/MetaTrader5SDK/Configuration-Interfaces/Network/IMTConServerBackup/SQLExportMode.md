[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportMode

[Previous](BackupLastArchive.md) | [Next](SQLExportFlags.md)

# IMTConServerBackup::SQLExportMode

Gets the mode of data export to an SQL database.

C++
    
    
    UINT  IMTConServerBackup::BackupPeriod()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerBackup.BackupPeriod()

Python (Manager API)
    
    
    MTConServerBackup.BackupPeriod

### Return Value

One of the values of the [IMTConServer::EnSQLExportMode (#ensqlexportmode)](Enumerations.md#ensqlexportmode) enumeration.

# IMTConServerBackup::SQLExportMode

Sets the mode of data export to an SQL database.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportMode(
       const UINT  mode        // Export mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportMode(
       uint        mode        // Export mode
       )

Python (Manager API)
    
    
    MTConServerBackup.BackupPeriod

### Parameters

**mode**  
[in] TheIMTConServerBackup::EnSQLExportModeenumeration is used to pass the mode of data export to SQL.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
