[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByLogins

[Previous](PositionRequestByGroupSymbol.md) | [Next](PositionRequestByLoginsSymbol.md)

# IMTManagerAPI::PositionRequestByLogins

Request from the server open positions by the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionRequestByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTPositionArray*  positions     // An object of positions array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionRequestByLogins(
       ulong[]            logins,       // Logins
       CIMTPositionArray  positions     // An object of positions array
       )

Python
    
    
    ManagerAPI.PositionRequestByLogins(
       logins             # Logins
       )
    
    
    ManagerAPI.PositionRequestByLoginsCSV(
       logins,            # Logins
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionRequestByLoginsNumPy(
       logins,            # Logins
       fields             # Comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**positions**  
[out] An object of positions array. The 'positions' object should be first created usingIMTManagerAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'positions' object the data of all open positions belonging to the specified accounts.
