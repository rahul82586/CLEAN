[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByGroupSymbol

[Previous](PositionGetByGroup.md) | [Next](PositionGetByLogins.md)

# IMTServerAPI::PositionGetByGroupSymbol

Get open positions from the server by group and symbol.
    
    
    MTAPIRES  IMTAdminAPI::PositionGetByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       IMTPositionArray*  positions      // object of positions array
       )

### Parameters

**group**  
[in] The groups for which the positions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group 'demoforex'.

**symbol**  
[in] The symbol, for which you need to get positions. You can specify multiple symbols separated by commas as well as symbol masks. The maximum length of the string is 127 characters.

**positions**  
[out] Positions array object. The 'positions' object must first be created using theIMTAdminAPI::PositionCreateArraymethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
