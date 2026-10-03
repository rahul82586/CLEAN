[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderBackupList

[Previous](OrderCancelBatch.md) | [Next](OrderBackupRequest.md)

# IMTAdminAPI::OrderBackupList

Request the dates of backup databases of orders for the specified time range.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupList(
       const INT64  from,              // Beginning of period
       const INT64  to,                // End of period
       INT64*&      backups,           // An array of dates of backups
       UINT&        backups_total      // The number of dates of backups
       )

.NET
    
    
    long[]  CIMTAdminAPI.OrderBackupList(
       long           from,            // Beginning of period
       long           to,              // End of period
       out MTRetCode  res              // Response code
       )

Python
    
    
    AdminAPI.OrderBackupList(
       from,          # Beginning of period
       to             # End of period
       )

### Parameters

**from**  
[in] The beginning of the period for which you need to get the list of backup copies. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get the list of backup copies. The date is specified in seconds that have elapsed since 01.01.1970.

**backups**  
[out] An array of backup creation dates.

**backups_total**  
[out] The number of received dates of backups.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After using, the backups array must be released using the [IMTAdminAPI::Free](../../Common-Functions/Free.md) method.

# IMTAdminAPI::OrderBackupList

Request the dates of backup databases of orders for the specified time range from the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupList(
       const UINT64 server,            // Server ID
       const INT64  from,              // Beginning of period
       const INT64  to,                // End of period
       INT64*&      backups,           // An array of dates of backups
       UINT&        backups_total      // The number of dates of backups
       )

.NET
    
    
    long[]  CIMTAdminAPI.OrderBackupList(
       ulong          server,          // Server ID
       long           from,            // Beginning of period
       long           to,              // End of period
       out MTRetCode  res              // Response code
       )

Python
    
    
    AdminAPI.OrderBackupList(
       server,        # Server ID
       from,          # Beginning of period
       to             # End of period
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**from**  
[in] The beginning of the period for which you need to get the list of backup copies. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get the list of backup copies. The date is specified in seconds that have elapsed since 01.01.1970.

**backups**  
[out] An array of backup creation dates.

**backups_total**  
[out] The number of received dates of backups.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After using, the backups array must be released using the [IMTAdminAPI::Free](../../Common-Functions/Free.md) method.
