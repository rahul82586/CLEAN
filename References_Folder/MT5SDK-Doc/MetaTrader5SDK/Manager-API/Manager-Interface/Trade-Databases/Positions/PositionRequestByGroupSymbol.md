[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByGroupSymbol

[Previous](PositionRequestByGroup.md) | [Next](PositionRequestByLogins.md)

# IMTManagerAPI::PositionRequestByGroupSymbol

Request open positions from the server by group and symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionRequestByGroupSymbol(
       LPCWSTR            group,         // group
       LPCWSTR            symbol,        // symbol
       IMTPositionArray*  positions      // object of positions array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionRequestByGroupSymbol(
       string             mask,          // group
       string             symbol,        // symbol
       CIMTPositionArray  positions      // object of positions array
       )

Python
    
    
    ManagerAPI.PositionRequestByGroupSymbol(
       mask,              # group
       symbol             # symbol
       )
    
    
    ManagerAPI.PositionRequestByGroupSymbolCSV(
       mask,              # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionRequestByGroupSymbolNumPy(
       mask,              # group
       symbol,            # symbol
       fields             # comma-separated list of required fields
       )

### Parameters

**group**  
[in] The groups for which the positions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**symbol**  
[in] The symbol, for which you need to get positions.

**positions**  
[out] An object of the array of trade positions. The 'position' object must be first created using theIMTManagerAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
