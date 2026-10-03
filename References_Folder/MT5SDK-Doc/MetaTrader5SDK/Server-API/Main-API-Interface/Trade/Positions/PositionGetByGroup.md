[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByGroup

[Previous](PositionGetByTicket.md) | [Next](PositionGetByGroupSymbol.md)

# IMTServerAPI::PositionGetByGroup

Get trading positions for a client group.
    
    
    MTAPIRES  IMTServerAPI::PositionGetByGroup(
       LPCWSTR            group,         // Group
       IMTPositionArray*  positions      // An object of positions array
       )

### Parameters

**group**  
[in] The groups for which the positions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

**positions**  
[out] An object of the array of trade positions. The 'position' object must be first created usingIMTServerAPI::PositionCreateArray.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'positions' object the data of all open positions belonging to clients in the specified groups.
