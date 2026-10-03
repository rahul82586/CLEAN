[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByTickets

[Previous](PositionGetByLoginsSymbol.md) | [Next](PositionSelectByGroup.md)

# IMTServerAPI::PositionGetByTickets

Receive trading positions by the list of tickets.
    
    
    MTAPIRES  IMTServerAPI::PositionGetByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// The number of tickets
       IMTPositionArray*  positions     // Position array
       )

### Parameters

**tickets**  
[in] List of order tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**positions**  
[out] An object of positions array. The 'positions' object must be first created usingIMTServerAPI::PositionCreateArray.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of positions with the specified tickets to the 'positions' object.
