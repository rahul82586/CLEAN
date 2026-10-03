[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportPassword

[Previous](SQLExportLogin.md) | [Next](SQLExportFolder.md)

# IMTConServerBackup::SQLExportPassword

Getting the password for connecting to an SQL database.

C++
    
    
    LPCWSTR  IMTConServerBackup::SQLExportPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServerBackup.SQLExportPassword()

Python (Manager API)
    
    
    MTConServerBackup.SQLExportPassword

### Return Value

The password for connecting to an SQL database.

# IMTConServerBackup::SQLExportPassword

Setting the password for connecting to an SQL database.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportPassword(
       LPCWSTR  password    // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportPassword(
       string   password    // Password
       )

Python (Manager API)
    
    
    MTConServerBackup.SQLExportPassword

### Parameters

**password**  
[in] The password for connecting to an SQL database.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
