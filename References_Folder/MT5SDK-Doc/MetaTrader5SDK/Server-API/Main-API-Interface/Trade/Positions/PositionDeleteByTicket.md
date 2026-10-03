[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionDeleteByTicket

[Previous](PositionDelete.md) | [Next](PositionUpdate.md)

# IMTServerAPI::PositionDeleteByTicket

Delete a trade position by ticket.
    
    
    MTAPIRES  IMTServerAPI::PositionDeleteByTicket(
       const UINT64  ticket      // Position ticket
       )

### Parameters

**ticket**  
[in] The ticket of a position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Common-errors.md) response code. Otherwise, an error code will be returned.

### Note

A position can be deleted only from the plugins that run on the same trade server where the position was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
