[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealGetByTickets

[Previous](DealGetByLoginsSymbol.md) | [Next](DealSelectByGroup.md)

# IMTServerAPI::DealGetByTickets

Receive deals by the list of tickets.
    
    
    MTAPIRES  IMTServerAPI::DealGetByTickets(
       const UINT64* tickets,      // Tickets
       const UINT    tickets_total,// Number of tickets
       IMTDealArray* deals         // Array of deals
       )

### Parameters

**tickets**  
[in] Array of tickets of the deals which you want to receive.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**deals**  
[out] An object of the deals array. The 'deals' object must be first created usingIMTServerAPI::DealCreateArray.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies deals with the specified tickets into the 'deals' object.
