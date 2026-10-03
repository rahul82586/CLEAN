[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGetByTickets

[Previous](OrderGetByLogins.md) | [Next](OrderGetBySymbol.md)

# IMTManagerAPI::OrderGetByTickets

Receive currently open orders by the list of tickets.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGetByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTOrderArray*     orders        // Array of orders
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGetByTickets(
       ulong[]            tickets,      // Tickets
       CIMTOrderArray     orders        // Array of orders
       )

Python
    
    
    ManagerAPI.OrderGetByTickets(
       tickets            # Tickets
       )
    
    
    ManagerAPI.OrderGetByTicketsCSV(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.OrderGetByTicketsNumPy(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )

### Parameters

**tickets**  
[in] The list of order tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTManagerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies to the 'orders' object the data of open orders with the specified tickets. The method works only if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
