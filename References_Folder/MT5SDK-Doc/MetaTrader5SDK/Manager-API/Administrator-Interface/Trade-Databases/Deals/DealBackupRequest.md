[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealBackupRequest

[Previous](DealBackupList.md) | [Next](DealBackupRestore.md)

# IMTAdminAPI::DealBackupRequest

Request a deal from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealBackupRequest(
       const INT64   backup,     // Backup date
       const UINT64  ticket,     // Deal number
       IMTDeal*      deal        // An object of a deal
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealBackupRequest(
       long          backup,     // Backup date
       ulong         ticket,     // Deal number
       CIMTDeal      deal        // An object of a deal
       )

Python
    
    
    AdminAPI.DealBackupRequest(
       backup,       # Backup date
       ticket        # Deal number
       )

### Parameters

**backup**  
[in] The date of creation of the backup to which the requested deal belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::DealBackupListmethod.

**ticket**  
[in] Deal number.

**deal**  
[out] An object of a deal. The deal object must be first created using theIMTAdminAPI::DealCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

# IMTAdminAPI::DealBackupRequest

Request an array of deals from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealBackupRequest(
       const INT64    backup,     // Backup date
       const UINT64   login,      // Login
       const INT64    from,       // Beginning of period
       const INT64    to,         // End of period
       IMTDealArray*  deals       // An object of the array of deals
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealBackupRequest(
       long           backup,     // Backup date
       ulong          login,      // Login
       long           from,       // Beginning of period
       long           to,         // End of period
       CIMTDealArray  deals       // An object of the array of deals
       )

Python
    
    
    AdminAPI.DealBackupRequest(
       backup,        # Backup date
       login,         # Login
       from,          # Beginning of period
       to             # End of period
       )

### Parameters

**backup**  
[in] The date of creation of the backup to which the requested deal belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::DealBackupListmethod.

**login**  
[in] The login of a user whose deals we want to obtain.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**deals**  
[out] An object of the array of deals. The deals object must be first created using theIMTAdminAPI::DealCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

# IMTAdminAPI::DealBackupRequest

Request a deal from a backup database from the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealBackupRequest(
       const UINT64  server,     // Server ID
       const INT64   backup,     // Backup date
       const UINT64  ticket,     // Deal number
       IMTDeal*      deal        // An object of a deal
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealBackupRequest(
       ulong         server,     // Server ID
       long          backup,     // Backup date
       ulong         ticket,     // Deal number
       CIMTDeal      deal        // An object of a deal
       )

Python
    
    
    AdminAPI.DealBackupRequest(
       server,       # Server ID
       backup,       # Backup date
       ticket        # Deal number
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**backup**  
[in] The date of creation of the backup to which the requested deal belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::DealBackupListmethod.

**ticket**  
[in] Deal number.

**deal**  
[out] An object of a deal. The deal object must be first created using theIMTAdminAPI::DealCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

# IMTAdminAPI::DealBackupRequest

Request an array of deals from a backup database from the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealBackupRequest(
       const UINT64   server,     // Server ID
       const INT64    backup,     // Backup date
       const UINT64   login,      // Login
       const INT64    from,       // Beginning of period
       const INT64    to,         // End of period
       IMTDealArray*  deals       // An object of the array of deals
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealBackupRequest(
       ulong          server,     // Server ID
       long           backup,     // Backup date
       ulong          login,      // Login
       long           from,       // Beginning of period
       long           to,         // End of period
       CIMTDealArray  deals       // An object of the array of deals
       )

Python
    
    
    AdminAPI.DealBackupRequest(
       server,        # Server ID
       backup,        # Backup date
       login,         # Login
       from,          # Beginning of period
       to             # End of period
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**backup**  
[in] The date of creation of the backup to which the requested deal belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::DealBackupListmethod.

**login**  
[in] The login of a user whose deals we want to obtain.

**from**  
[in] The beginning of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

**deals**  
[out] An object of the array of deals. The deals object must be first created using theIMTAdminAPI::DealCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).
