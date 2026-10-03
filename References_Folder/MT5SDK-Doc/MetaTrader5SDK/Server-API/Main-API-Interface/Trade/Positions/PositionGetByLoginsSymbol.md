[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByLoginsSymbol

[Previous](PositionGetByLogins.md) | [Next](PositionGetByTickets.md)

# IMTServerAPI::PositionRequestByLoginsSymbol

Get open positions from the server by list of logins and symbol.
    
    
    MTAPIRES  IMTServerAPI::PositionGetByLoginsSymbol(
       const UINT64*      logins,       // logins
       const UINT         logins_total, // number of logins
       LPCWSTR            symbol,       // symbol
       IMTPositionArray*  positions     // object of positions array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**symbol**  
[in] The symbol, for which you need to get positions. You can specify multiple symbols separated by commas as well as symbol masks. The maximum length of the string is 127 characters.

**positions**  
[out] Positions array object. Positions object must first be created using theIMTAdminAPI::PositionCreateArraymethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
