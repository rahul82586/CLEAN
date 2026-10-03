[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderBackupRequest

[Previous](OrderBackupList.md) | [Next](OrderBackupRequestOpen.md)

# IMTAdminAPI::OrderBackupRequest

Request an order from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupRequest(
       const INT64   backup,     // Backup date
       const UINT64  ticket,     // Order number
       IMTOrder*     order       // An order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderBackupRequest(
       long          backup,     // Backup date
       ulong         ticket,     // Order number
       CIMTOrder     order       // An order objec
       )

Python
    
    
    AdminAPI.OrderBackupRequest(
       backup,       # Backup date
       ticket        # Order number
       )

### Parameters

**backup**  
[in] The date of creation of the backup to which the requested order belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::OrderBackupListmethod.

**ticket**  
[in] Order number.

**order**  
[out] An object of a trade order. The order object must be first created using theIMTAdminAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

# IMTAdminAPI::OrderBackupRequest

Request an order from a backup database from the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupRequest(
       const UINT64  server,     // Server ID
       const INT64   backup,     // Backup date
       const UINT64  ticket,     // Order number
       IMTOrder*     order       // An order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderBackupRequest(
       ulong         server,     // Server ID
       long          backup,     // Backup date
       ulong         ticket,     // Order number
       CIMTOrder     order       // An order objec
       )

Python
    
    
    AdminAPI.OrderBackupRequest(
       server,       # Server ID
       backup,       # Backup date
       ticket        # Order number
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**backup**  
[in] The date of creation of the backup to which the requested order belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::OrderBackupListmethod.

**ticket**  
[in] Order number.

**order**  
[out] An object of a trade order. The order object must be first created using theIMTAdminAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
