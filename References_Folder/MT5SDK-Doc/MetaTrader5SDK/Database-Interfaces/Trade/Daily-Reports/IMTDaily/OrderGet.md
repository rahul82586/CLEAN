[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / OrderGet

[Previous](OrderNext.md) | [Next](../IMTDailyArray.md)

# IMTDaily::OrderGet

Get a [trade order](../../Orders.md) by a ticket.

C++
    
    
    MTAPIRES  IMTDaily::OrderGet(
       UINT64        ticket,       // Order ticket
       IMTOrder*     order         // An order object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.OrderGet(
       ulong         ticket,       // Order ticket
       CIMTOrder     order         // An order object
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

**position**  
[out] An object of a trade order. The 'order' object must be first created using theIMTManagerAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies parameters of a trade order with the specified ticket to the order object.
