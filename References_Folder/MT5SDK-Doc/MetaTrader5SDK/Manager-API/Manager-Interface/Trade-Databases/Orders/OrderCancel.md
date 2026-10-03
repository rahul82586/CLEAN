[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCancel

[Previous](OrderDeleteBatch.md) | [Next](OrderCancelBatch.md)

# IMTManagerAPI::OrderCancel

Move an open trading order to history.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderCancel(
       const UINT64  ticket      // order ticket
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderCancel(
       ulong         ticket      // order number
       )

Python
    
    
    ManagerAPI.OrderCancel(
       ticket        # order number
       )

### Parameters

**ticket**  
[in] Order number (ticket).

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error code will be returned.

### Note

When an order is transferred, its state changes to [IMTOrder::ORDER_STATE_CANCELED (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate). Such orders are not executed or triggered, and no margin is charged for them.
