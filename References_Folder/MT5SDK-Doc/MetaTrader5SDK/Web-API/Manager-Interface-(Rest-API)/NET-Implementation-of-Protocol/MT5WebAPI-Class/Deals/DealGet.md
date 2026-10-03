[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Deals](../Deals.md) / DealGet

[Previous](../Deals.md) | [Next](DealGetTotal.md)

# MT5WebAPI.DealGet

Get a deal by a ticket.
    
    
    MTRetCode  MT5WebAPI.DealGet(
       ulong       ticket,    // Deal ticket
       out MTDeal  deal       // Deal
       )

### Parameters

**ticket**  
[in] Deal ticket.

**deal**  
[out] The MTDeal structure that describes a trade deal. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
