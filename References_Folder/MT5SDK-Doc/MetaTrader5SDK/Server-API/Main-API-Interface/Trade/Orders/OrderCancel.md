[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderCancel

[Previous](OrderDeleteBatch.md) | [Next](OrderCancelBatch.md)

# IMTServerAPI::OrderCancel

Move an open trading order to history.
    
    
    MTAPIRES  IMTServerAPI::OrderCancel(
       const UINT64  ticket      // order ticket
       )

### Parameters

**ticket**  
[in] Order number (ticket).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When an order is transferred, its state changes to [IMTOrder::ORDER_STATE_CANCELED (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate). Such orders are not executed or triggered, and no margin is charged for them.
