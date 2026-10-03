[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / HistoryRequestByTickets

[Previous](HistoryRequest.md) | [Next](HistoryRequestByLogins.md)

# IMTAdminAPI::HistoryRequestByTickets

Request from the server the closed orders (history) related to the list of tickets.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistoryRequestByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTOrderArray*     orders        // Array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistoryRequestByTickets(
       ulong[]            tickets,      // Tickets
       CIMTOrderArray     orders        // Array of orders
       )

Python
    
    
    AdminAPI.HistoryRequestByTickets(
       tickets            # Tickets
       )
    
    
    AdminAPI.HistoryRequestByTicketsCSV(
       tickets,           # Tickets
       fields             # Array of orders
       )
    
    
    AdminAPI.HistoryRequestByTicketsNumPy(
       tickets,           # Tickets
       fields             # Array of orders
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
