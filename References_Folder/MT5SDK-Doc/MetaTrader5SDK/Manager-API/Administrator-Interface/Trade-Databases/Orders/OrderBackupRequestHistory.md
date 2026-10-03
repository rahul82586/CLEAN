[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderBackupRequestHistory

[Previous](OrderBackupRequestOpen.md) | [Next](OrderBackupRestore.md)

# IMTAdminAPI::OrderBackupRequestHistory

Request closed orders from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupRequestHistory(
       const INT64     backup,     // Backup date
       const UINT64    login,      // Login
       const INT64     from,       // Beginning of period
       const INT64     to,         // End of period
       IMTOrderArray*  orders      // An object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderBackupRequestHistory(
       long            backup,     // Backup date
       ulong           login,      // Login
       long            from,       // Beginning of period
       long            to,         // End of period
       CIMTOrderArray  orders      // An object of the array of orders
       )

Python
    
    
    AdminAPI.OrderBackupRequestHistory(
       backup,         # Backup date
       login,          # Login
       from,           # Beginning of period
       to              # End of period
       )

### Parameters

**backup**  
[in] The date of creation of the backup to which the requested order belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::OrderBackupListmethod.

**login**  
[in] The login of the client, whose closed orders you need to get.

**from**  
[in] The beginning of the period you want to receive orders for. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds that have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

# IMTAdminAPI::OrderBackupRequestHistory

Request closed orders from a backup database of the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupRequestHistory(
       const UINT64    server,     // Server ID
       const INT64     backup,     // Backup date
       const UINT64    login,      // Login
       const INT64     from,       // Beginning of period
       const INT64     to,         // End of period
       IMTOrderArray*  orders      // An object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderBackupRequestHistory(
       ulong           server,     // Server ID
       long            backup,     // Backup date
       ulong           login,      // Login
       long            from,       // Beginning of period
       long            to,         // End of period
       CIMTOrderArray  orders      // An object of the array of orders
       )

Python
    
    
    AdminAPI.OrderBackupRequestHistory(
       server,         # Server ID
       backup,         # Backup date
       login,          # Login
       from,           # Beginning of period
       to              # End of period
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**backup**  
[in] The date of creation of the backup to which the requested order belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::OrderBackupListmethod.

**login**  
[in] The login of the client, whose closed orders you need to get.

**from**  
[in] The beginning of the period you want to receive orders for. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get orders. The date is specified in seconds that have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
