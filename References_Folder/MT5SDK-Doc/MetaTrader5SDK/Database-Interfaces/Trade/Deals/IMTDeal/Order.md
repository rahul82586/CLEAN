[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Order

[Previous](Dealer.md) | [Next](Action.md)

# IMTDeal::Order

Get the ticket of the order, as a result of which a deal was executed.

C++
    
    
    UINT64  IMTDeal::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.Order()

### Return Value

The ticket of the order, as a result of which a deal was executed.

# IMTDeal::Order

Sets the ticket of the order, as a result of which a deal was executed.

C++
    
    
    MTAPIRES  IMTDeal::Order(
       const UINT64  order      // Order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Order(
       ulong         order      // Order ticket
       )

### Parameters

**order**  
[in] The ticket of the order, as a result of which a deal was executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
