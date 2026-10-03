[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGetByTicket

[Previous](PositionGet.md) | [Next](PositionGetByGroup.md)

# IMTServerAPI::PositionGetByTicket

Get a trade position by the ticket.
    
    
    MTAPIRES  IMTServerAPI::PositionGetByTicket(
       const UINT64  ticket,       // Ticket
       IMTPosition*  position      // Position object
       )

### Parameters

**ticket**  
[in] The ticket of a position. Corresponds toIMTPosition::Position.

**position**  
[out] An object of a trade position. The position object must be first created using theIMTServerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position with the specified ticket to the position object.
