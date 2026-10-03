[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetByLogins

[Previous](PositionGetByGroup.md) | [Next](PositionGetByTicket.md)

# IMTManagerAPI::PositionGetByLogins

Receive open positions by the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGetByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTPositionArray*  positions     // An object of positions array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGetByLogins(
       ulong[]            logins,       // Logins
       CIMTPositionArray  positions     // An object of positions array
       )

Python
    
    
    ManagerAPI.PositionGetByLogins(
       logins             # Logins
       )
    
    
    ManagerAPI.PositionGetByLoginsCSV(
       logins,            # Logins
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionGetByLoginsNumPy(
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

The method copies to the 'positions' object the data of all open positions belonging to the specified accounts. The method works only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
