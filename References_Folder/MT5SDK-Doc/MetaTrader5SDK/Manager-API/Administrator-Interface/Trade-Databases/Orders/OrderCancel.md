[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCancel

[Previous](OrderDeleteBatch.md) | [Next](OrderCancelBatch.md)

# IMTAdminAPI::OrderCancel

Move an open trading order to history.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderCancel(
       const UINT64  ticket      // order ticket
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderCancel(
       ulong         ticket      // order number
       )

Python
    
    
    AdminAPI.OrderCancel(
       ticket        # order number
       )

### Parameters

**ticket**  
[in] Order number (ticket).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When an order is transferred, its state changes to [IMTOrder::ORDER_STATE_CANCELED (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate). Such orders are not executed or triggered, and no margin is charged for them.
