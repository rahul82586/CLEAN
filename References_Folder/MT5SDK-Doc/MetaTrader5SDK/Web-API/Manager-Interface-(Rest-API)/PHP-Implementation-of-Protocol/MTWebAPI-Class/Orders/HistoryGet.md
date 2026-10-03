[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Orders](../Orders.md) / HistoryGet

[Previous](OrderGetPage.md) | [Next](HistoryGetTotal.md)

# MTWebAPI::HistoryGet

Get a closed order by the ticket.
    
    
    MTAPIRES  MTWebAPI::HistoryGet(
       int      $ticket,     // Ticket
       MTOrder  &$order      // Order
       )

### Parameters

**$ticket**  
[in] Order ticket.

**& $order**  
[out] The MTOrder structure that describes a trade order. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
