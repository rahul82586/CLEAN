[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByGroupSymbol

[Previous](PositionRequestByGroup.md) | [Next](PositionRequestByLogins.md)

# IMTAdminAPI::PositionRequestByGroupSymbol

Request open positions from the server by group and symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionRequestByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       IMTPositionArray*  positions      // object of positions array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionRequestByGroupSymbol(
       string             mask,          // group
       string             symbol,        // symbol
       CIMTPositionArray  positions      // object of positions array
       )

Python
    
    
    AdminAPI.PositionRequestByGroupSymbol(
       group,             # group
       symbol             # symbol
       )
    
    
    AdminAPI.PositionRequestByGroupSymbolCSV(
       group,             # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )
    
    
    AdminAPI.PositionRequestByGroupSymbolNumPy(
       group,             # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the positions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**symbol**  
[in] The symbol, for which you need to get positions. You can specify multiple symbols separated by commas.

**positions**  
[out] An object of the array of trade positions. The 'positions' object must be first created usingIMTAdminAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
