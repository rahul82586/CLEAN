[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequest

[Previous](OrderGetBySymbol.md) | [Next](OrderRequestOpen.md)

# IMTManagerAPI::OrderRequest

Request a trade order from a server by the ticket.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderRequest(
       const UINT64  ticket,     // Ticket
       IMTOrder*     order       // An order object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderRequest(
       ulong         ticket,     // Ticket
       CIMTOrder     order       // An order objec
       )

OrderGetBySymbol
    
    
    ManagerAPI.OrderRequest(
       int           ticket      # Ticket
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

**order**  
[out] An object of a trade order. The 'order' object must be first created using theIMTManagerAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of an order (no matter already fulfilled or not) with the specified ticket to the order object.
