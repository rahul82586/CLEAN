[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByTickets

[Previous](PositionRequestByLoginsSymbol.md) | [Next](PositionUpdate.md)

# IMTAdminAPI::PositionRequestByTickets

Request from the server open positions by the list of tickets.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionRequestByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTPositionArray*  positions     // An array of positions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionRequestByTickets(
       ulong[]            tickets,      // Tickets
       CIMTPositionArray  positions     // An array of positions
       )

Python
    
    
    AdminAPI.PositionRequestByTickets(
       tickets            # Tickets
       )
    
    
    AdminAPI.PositionRequestByTicketsCSV(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )
    
    
    AdminAPI.PositionRequestByTicketsNumPy(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )

### Parameters

**tickets**  
[in] List of position tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**positions**  
[out] An object of positions array. Positions object must be first created usingIMTAdminAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of positions with the specified tickets to the 'positions' object.
