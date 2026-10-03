[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByLogins

[Previous](PositionRequestByGroupSymbol.md) | [Next](PositionRequestByLoginsSymbol.md)

# IMTAdminAPI::PositionRequestByLogins

Request from the server open positions by the list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTPositionArray*  positions     // An object of positions array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionRequestByLogins(
       ulong[]            logins,       // Logins
       CIMTPositionArray  positions     // An object of positions array
       )

Python
    
    
    AdminAPI.PositionRequestByLogins(
       logins             # Logins
       )
    
    
    AdminAPI.PositionRequestByLoginsCSV(
       logins,            # Logins
       fields             # comma-separated list of required fields
       )
    
    
    AdminAPI.PositionRequestByLoginsNumPy(
       logins,            # Logins
       fields             # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**positions**  
[out] An object of positions array. Positions object must be first created usingIMTAdminAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'positions' object the data of all open positions belonging to the specified accounts.
