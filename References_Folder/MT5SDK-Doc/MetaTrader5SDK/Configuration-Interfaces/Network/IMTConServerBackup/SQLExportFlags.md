[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportFlags

[Previous](SQLExportMode.md) | [Next](SQLExportPeriod.md)

# IMTConServerBackup::SQLExportFlags

Getting additional settings of data export to an SQL database.

C++
    
    
    UINT64  IMTConServerBackup::SQLExportFlags()  const

.NET (Gateway/Manager API)
    
    
    EnSQLExportFlags  IMTConServerBackup.SQLExportFlags()

Python (Manager API)
    
    
    MTConServerBackup.SQLExportFlags

### Return Value

One of the values of the [IMTConServer::EnSQLExportFlags (#ensqlexportflags)](Enumerations.md#ensqlexportflags) enumeration.

# IMTConServerBackup::SQLExportFlags

Setting additional settings of data export to an SQL database.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportFlags(
       const UINT64      period  // Export flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportFlags(
       EnSQLExportFlags  period  // Export flags
       )

Python (Manager API)
    
    
    MTConServerBackup.SQLExportFlags

### Parameters

**period**  
[in] TheIMTConServerBackup::EnSQLExportFlagsenumeration is used for passing additional settings.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
