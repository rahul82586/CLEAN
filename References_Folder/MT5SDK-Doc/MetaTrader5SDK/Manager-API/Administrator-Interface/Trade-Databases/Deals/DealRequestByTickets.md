[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealRequestByTickets

[Previous](DealRequestByLoginsSymbol.md) | [Next](DealRequestPage.md)

# IMTAdminAPI::DealRequestByTickets

Receive deals by the list of tickets.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealRequestByTickets(
       const UINT64* tickets,      // Tickets
       const UINT    tickets_total,// Number of tickets
       IMTDealArray* deals         // Array of deals
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealRequestByTickets(
       ulong[]       tickets,      // Tickets
       CIMTDealArray deals         // Array of deals
       )

Python
    
    
    AdminAPI.DealRequestByTickets(
       tickets       # Tickets
       )
    
    
    AdminAPI.DealRequestByTicketsCSV(
       tickets,      # Tickets
       fields        # Comma-separated list of required fields
       )
    
    
    AdminAPI.DealRequestByTicketsNumPy(
       tickets,      # Tickets
       fields        # Comma-separated list of required fields
       )

### Parameters

**tickets**  
[in] Array of tickets of the deals which you want to receive.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**deals**  
[out] An object of the deals array. The 'deals' object must be first created usingIMTAdminAPI::DealCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method copies deals with the specified tickets into the 'deals' object.
