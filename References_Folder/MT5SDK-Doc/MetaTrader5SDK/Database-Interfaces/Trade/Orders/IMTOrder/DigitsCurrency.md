[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / DigitsCurrency

[Previous](Digits.md) | [Next](ContractSize.md)

# IMTOrder::DigitsCurrency

Get the number of decimal places the deposit currency of the client who has placed the order.

C++
    
    
    UINT  IMTOrder::DigitsCurrency()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTOrder.DigitsCurrency()

Python
    
    
    MTOrder.DigitsCurrency()

### Return Value

The number of decimal places the deposit currency of the client who has placed the order.

# IMTOrder::DigitsCurrency

Set the number of decimal places the deposit currency of the client who has placed the order.

C++
    
    
    MTAPIRES  IMTOrder::DigitsCurrency(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.DigitsCurrency(
       uint        digits      // Decimal places
       )

Python
    
    
    MTOrder.DigitsCurrency()

### Parameters

**digits**  
[in] The number of decimal places the deposit currency of the client who has placed the order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
