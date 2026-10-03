[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequest

[Previous](OrderCreateArray.md) | [Next](OrderRequestOpen.md)

# IMTAdminAPI::OrderRequest

Request a trade order from a server by the ticket.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequest(
       const UINT64  ticket,     // Ticket
       IMTOrder*     order       // An order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequest(
       ulong         ticket,     // Ticket
       CIMTOrder     order       // An order objec
       )

Python
    
    
    AdminAPI.OrderRequest(
       ticket        # Ticket
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

**order**  
[out] An object of a trade order. The order object must be first created using theIMTAdminAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of an order with the specified ticket to the order object.
