[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportFolder

[Previous](SQLExportPassword.md) | [Next](SQLExportLastSync.md)

# IMTConServerBackup::SQLExportFolder

Getting the name of the SQL database, to which data is exported.

C++
    
    
    LPCWSTR  IMTConServerBackup::SQLExportFolder()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServerBackup.SQLExportFolder()

Python (Manager API)
    
    
    MTConServerBackup.SQLExportFolder

### Return Value

The name of the SQL database, to which data is exported.

# IMTConServerBackup::SQLExportFolder

Setting the name of the SQL database, to which data is exported.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportFolder(
       LPCWSTR  folder      // The name of the database
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportFolder(
       string   folder      // The name of the database
       )

Python (Manager API)
    
    
    MTConServerBackup.SQLExportFolder

### Parameters

**folder**  
[in] The name of the SQL database, to which data is exported.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A database should be created in advance.
