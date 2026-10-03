[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByLogins

[Previous](PositionGetByGroupSymbol.md) | [Next](PositionGetByLoginsSymbol.md)

# IMTServerAPI::PositionGetByLogins

Receive trading positions by the list of logins.
    
    
    MTAPIRES  IMTServerAPI::PositionGetByLogins(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       IMTPositionArray*  positions     // An object of positions array
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**positions**  
[out] An object of positions array. The 'positions' object must be first created usingIMTServerAPI::PositionCreateArray.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'positions' object the data of all open positions belonging to the specified accounts.
