[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetBySymbol

[Previous](PositionGetByTickets.md) | [Next](PositionRequest.md)

# IMTManagerAPI::PositionGetBySymbol

Receive open positions by the groups and login.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGetBySymbol(
       LPCWSTR            group,        // Group mask
       LPCWSTR            symbol,       // Symbol
       IMTPositionArray*  positions     // Array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGetBySymbol(
       String^            group,        // Group mask
       String^            symbol,       // Symbol
       CIMTPositionArray  positions     // Array of positions
       )

Python
    
    
    ManagerAPI.PositionGetBySymbol(
       group,             # Group mask
       symbol             # Symbol
       )
    
    
    ManagerAPI.PositionGetBySymbolCSV(
       group,             # Group mask
       symbol,            # Symbol
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionGetBySymbolNumPy(
       group,             # Group mask
       symbol,            # Symbol
       fields             # Comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the positions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The 'nullptr' value means "all groups".

**symbol**  
[in] The symbol, for which you need to get positions.

**positions**  
[out] An object of positions array. The 'positions' object should be first created usingIMTManagerAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method works only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
