[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestByTickets

[Previous](OrderRequestByLoginsSymbol.md) | [Next](OrderAdd.md)

# IMTAdminAPI::OrderRequestByTickets

Request from the server open orders by the list of tickets.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequestByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTOrderArray*     orders        // Array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequestByTickets(
       ulong[]            tickets,      // Tickets
       CIMTOrderArray     orders        // Array of orders
       )

Python
    
    
    AdminAPI.OrderRequestByTickets(
       tickets            # Tickets
       )
    
    
    AdminAPI.OrderRequestByTicketsCSV(
       tickets,           # Tickets
       fields             # comma-separated list of required fields
       )
    
    
    AdminAPI.OrderRequestByTicketsNumPy(
       tickets,           # Tickets
       fields             # comma-separated list of required fields
       )

### Parameters

**tickets**  
[in] List of order tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of orders with the specified tickets to the 'orders' object.
