[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetByTicket

[Previous](PositionGetByLogins.md) | [Next](PositionGetByTickets.md)

# IMTManagerAPI::PositionGetByTicket

Get an open trade position by the ticket.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGetByTicket(
       const UINT64  ticket,       // Ticket
       IMTPosition*  position      // Position object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGetByTicket(
       ulong         ticket,       // Ticket
       CIMTPosition  position      // Position object
       )

Python
    
    
    ManagerAPI.PositionGetByTicket(
       int           ticket        # Ticket
       )

### Parameters

**ticket**  
[in] The ticket of a position. Corresponds toIMTPosition::Position.

**position**  
[out] An object of a trade position. The 'position' object must be first created using theIMTManagerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position with specified ticket to the position object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
