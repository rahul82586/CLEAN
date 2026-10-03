[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Deals](../Deals.md) / DealGet

[Previous](../Deals.md) | [Next](DealGetTotal.md)

# MTWebAPI::DealGet

Get a deal by a ticket.
    
    
    MTAPIRES  MTWebAPI::DealGet(
       int     $ticket,     // Deal ticket
       MTDeal  &$deal       // Deal
       )

### Parameters

**$ticket**  
[in] Deal ticket.

**& $deal**  
[out] The MTDeal structure that describes a trade deal. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
