[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByLoginsSymbol

[Previous](PositionRequestByLogins.md) | [Next](PositionRequestByTickets.md)

# IMTAdminAPI::PositionRequestByLoginsSymbol

Request open positions from the server by list of logins and symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionRequestByLoginsSymbol(
       const UINT64*      logins,       // logins
       const UINT         logins_total, // number of logins
       LPCWSTR            symbol,       // symbol
       IMTPositionArray*  positions     // object of positions array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionRequestByLoginsSymbol(
       ulong[]            logins,       // logins
       string             symbol,       // symbol
       CIMTPositionArray  positions     // object of positions array
       )

Python
    
    
    AdminAPI.PositionRequestByLoginsSymbol(
       logins,            # logins
       symbol             # symbol
       )
    
    
    AdminAPI.PositionRequestByLoginsSymbolCSV(
       logins,            # logins
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )
    
    
    AdminAPI.PositionRequestByLoginsSymbolNumPy(
       logins,            # logins
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**symbol**  
[in] The symbol, for which you need to get positions. You can specify multiple symbols separated by commas.

**positions**  
[out] An object of positions array. Positions object must be first created usingIMTAdminAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
