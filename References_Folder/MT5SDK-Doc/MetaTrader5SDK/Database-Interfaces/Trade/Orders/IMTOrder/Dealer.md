[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Dealer

[Previous](Login.md) | [Next](Symbol.md)

# IMTOrder::Dealer

Get the login of a dealer, who has processed an order.

C++
    
    
    UINT64  IMTOrder::Dealer()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTOrder.Dealer()

Python
    
    
    MTOrder.Dealer()

### Return Value

The login of a dealer, who has processed an order. If an order was processed automatically by the server, 0 is returned.

# IMTOrder::Dealer

Set the login of a dealer, who has processed an order.

C++
    
    
    MTAPIRES  IMTOrder::Dealer(
       const UINT64  dealer      // Dealer
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Dealer(
       ulong         dealer      // Dealer
       )

Python
    
    
    MTOrder.Dealer()

### Parameters

**dealer**  
[in] The login of a dealer, who has processed an order. 0 means that the order was processed automatically by the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
