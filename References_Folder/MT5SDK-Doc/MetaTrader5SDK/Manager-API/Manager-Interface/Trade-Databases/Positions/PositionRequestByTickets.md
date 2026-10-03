[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequestByTickets

[Previous](PositionRequestByLoginsSymbol.md) | [Next](PositionUpdate.md)

# IMTManagerAPI::PositionRequestByTickets

Request from the server open positions by the list of tickets.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionRequestByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTPositionArray*  positions     // An array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionRequestByTickets(
       ulong[]            tickets,      // Tickets
       CIMTPositionArray  positions     // An array of positions
       )

Python
    
    
    ManagerAPI.PositionRequestByTickets(
       tickets            # Tickets
       )
    
    
    ManagerAPI.PositionRequestByTicketsCSV(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionRequestByTicketsNumPy(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )

### Parameters

**tickets**  
[in] List of position tickets.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**positions**  
[out] An object of positions array. The 'positions' object should be first created usingIMTManagerAPI::PositionCreateArray.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of positions with the specified tickets to the 'positions' object.
