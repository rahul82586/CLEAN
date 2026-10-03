[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportLogin

[Previous](SQLExportServer.md) | [Next](SQLExportPassword.md)

# IMTConServerBackup::SQLExportLogin

Getting the login for connecting to an SQL database.

C++
    
    
    LPCWSTR  IMTConServerBackup::SQLExportLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServerBackup.SQLExportLogin()

Python (Manager API)
    
    
    MTConServerBackup.SQLExportLogin

### Return Value

The login for connecting to an SQL database.

# IMTConServerBackup::SQLExportLogin

Setting the login for connecting to an SQL database.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportLogin(
       LPCWSTR  login       // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportLogin(
       string   login       // Login
       )

Python (Manager API)
    
    
    MTConServerBackup.SQLExportLogin

### Parameters

**login**  
[in] The login for connecting to an SQL database.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Notes

The account with which you are connecting, must have the permission to create/edit/delete tables and data.
