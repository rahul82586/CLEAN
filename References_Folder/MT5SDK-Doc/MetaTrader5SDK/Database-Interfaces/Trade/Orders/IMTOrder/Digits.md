[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Digits

[Previous](Symbol.md) | [Next](DigitsCurrency.md)

# IMTOrder::Digits

Get the number of decimal places in the price of an order.

C++
    
    
    UINT  IMTOrder::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.Digits()

Python
    
    
    MTOrder.Digits()

### Return Value

The number of decimal places in the price of an order.

# IMTOrder::Digits

Set the number of decimal places in the price of an order.

C++
    
    
    MTAPIRES  IMTOrder::Digits(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Digits(
       uint        digits      // Decimal places
       )

Python
    
    
    MTOrder.Digits()

### Parameters

**digits**  
[in] The number of decimal places in the price of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
