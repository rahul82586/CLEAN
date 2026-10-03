[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGet

[Previous](OrderUnsubscribe.md) | [Next](OrderGetOpen.md)

# IMTManagerAPI::OrderGet

Get a currently unfulfilled order by a ticket.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderGet(
       const UINT64  ticket,     // Ticket
       IMTOrder*     order       // An order object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderGet(
       ulong         ticket,     // Ticket
       CIMTOrder     order       // An order object
       )

Python
    
    
    ManagerAPI.OrderGet(
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

This method copies data of an order with the specified ticket to the order object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_ORDERS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
