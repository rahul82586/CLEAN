[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGetByTicket

[Previous](PositionGet.md) | [Next](PositionSelect.md)

# IMTReportAPI::PositionGetByTicket

Get a trade position by the ticket.
    
    
    MTAPIRES  IMTReportAPI::PositionGetByTicket(
       const UINT64  ticket,       // Position ticket
       IMTPosition*  position      // Position object
       )

### Parameters

**ticket**  
[in] The ticket of a position. Corresponds toIMTPosition::Position.

**position**  
[out] An object of a trade position. The position object must be first created using theIMTReportAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position with the specified ticket to the position object.

# 
