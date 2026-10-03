[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetByTickets

[Previous](PositionGetByTicket.md) | [Next](PositionGetBySymbol.md)

# IMTManagerAPI::PositionGetByTickets

Receive open positions by the list of tickets.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGetByTickets(
       const UINT64*      tickets,      // Tickets
       const UINT         tickets_total,// Number of tickets
       IMTPositionArray*  positions     // An array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGetByTickets(
       ulong[]            tickets,      // Tickets
       CIMTPositionArray  positions     // An array of positions
       )

Python
    
    
    ManagerAPI.PositionGetByTickets(
       tickets            # Tickets
       )
    
    
    ManagerAPI.PositionGetByTicketsCSV(
       tickets,           # Tickets
       fields             # Comma-separated list of required fields
       )
    
    
    ManagerAPI.PositionGetByTicketsNumPy(
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

This method copies data of positions with the specified tickets to the 'positions' object. The method works only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
