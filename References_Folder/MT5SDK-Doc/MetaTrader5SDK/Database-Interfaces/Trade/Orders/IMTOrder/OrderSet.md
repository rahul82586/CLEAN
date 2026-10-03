[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / OrderSet

[Previous](Order.md) | [Next](ExternalID.md)

# IMTOrder::OrderSet

Sets the order ticket.

C++
    
    
    MTAPIRES  IMTOrder::OrderSet(
       const UINT64  order      // Order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.OrderSet(
       ulong         order      // Order ticket
       )

Python
    
    
    MTOrder.Order()

### Parameters

**order**  
[in] Order ticket.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method should only be used for recovering databases of orders using the [IMTAdminAPI::OrderBackupRestore](../../../../Manager-API/Administrator-Interface/Trade-Databases/Orders/OrderBackupRestore.md) method.
