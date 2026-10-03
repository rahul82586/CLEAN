[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionBackupRequest

[Previous](PositionBackupList.md) | [Next](PositionBackupRestore.md)

# IMTAdminAPI::PositionBackupRequest

Request an array of positions from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionBackupRequest(
       const INT64        backup,         // Backup date
       const UINT64       login,          // Login
       IMTPositionArray*  positions       // An object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionBackupRequest(
       long               backup,         // Backup date
       ulong              login,          // Login
       CIMTPositionArray  positions       // An object of the array of positions
       )

Python
    
    
    AdminAPI.PositionBackupRequest(
       backup,            # Backup date
       login              # Login
       )

### Parameters

**backup**  
[in] The date of creation of the backup to which the requested position belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::PositionBackupListmethod.

**login**  
[in] The login of a user whose deals we want to obtain.

**positions**  
[out] An object of positions array. The positions object must be first created using theIMTAdminAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Backup copies are snapshots of the database of positions at certain time moments.

# IMTAdminAPI::PositionBackupRequest

Request an array of positions from a backup database of the specified server.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionBackupRequest(
       const UINT64       server,         // Server ID
       const INT64        backup,         // Backup date
       const UINT64       login,          // Login
       IMTPositionArray*  positions       // An object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionBackupRequest(
       ulong              server,         // Server ID
       long               backup,         // Backup date
       ulong              login,          // Login
       CIMTPositionArray  positions       // An object of the array of positions
       )

Python
    
    
    AdminAPI.PositionBackupRequest(
       server,            # Server ID
       backup,            # Backup date
       login              # Login
       )

### Parameters

**server**  
[in] The identifier of the server from which the information should be requested.

**backup**  
[in] The date of creation of the backup to which the requested position belongs. The date is specified in seconds that have elapsed since 01.01.1970. Dates of backups can be obtained using theIMTAdminAPI::PositionBackupListmethod.

**login**  
[in] The login of a user whose deals we want to obtain.

**positions**  
[out] An object of positions array. The positions object must be first created using theIMTAdminAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Backup copies are snapshots of the database of positions at certain time moments.
