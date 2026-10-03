[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryGetByTickets

[Previous](HistoryGetByLoginsSymbol.md) | [Next](HistorySelectByGroup.md)

# IMTServerAPI::HistoryGetByTickets

Receive closed orders (history) related to the list of tickets.
    
    
    MTAPIRES  IMTServerAPI::HistoryGetByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// The number of tickets
       IMTOrderArray*     orders        // The array of orders
       )

### Parameters

**tickets**  
[in] The list of order tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTServerAPI::OrderCreateArraymethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of orders with the specified tickets to the 'orders' object.
