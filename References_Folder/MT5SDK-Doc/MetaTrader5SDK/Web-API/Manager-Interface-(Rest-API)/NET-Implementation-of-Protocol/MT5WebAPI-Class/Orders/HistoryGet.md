[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Orders](../Orders.md) / HistoryGet

[Previous](OrderGetPage.md) | [Next](HistoryGetTotal.md)

# MT5WebAPI.HistoryGet

Get a closed order by the ticket.
    
    
    MTRetCode  MT5WebAPI.HistoryGet(
       ulong        ticket,    // Ticket
       out MTOrder  order      // Order
       )

### Parameters

**ticket**  
[in] Order ticket.

**order**  
[out] The MTOrder structure that describes a trade order. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
