[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionDelete

[Previous](PositionUnsubscribe.md) | [Next](PositionDeleteByTicket.md)

# IMTServerAPI::PositionDelete

Delete a trade position.
    
    
    MTAPIRES  IMTServerAPI::PositionDelete(
       const UINT64  login,      // User's login
       LPCWSTR       symbol      // Symbol
       )

### Parameters

**login**  
[in] The login of a user whose position should be deleted.

**symbol**  
[in] The symbol, for which a position should be deleted.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Common-errors.md) response code. Otherwise, an error code will be returned.

### Note

A position can be deleted only from the plugins that run on the same trade server where the position was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
