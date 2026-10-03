[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / DigitsCurrency

[Previous](Digits.md) | [Next](ContractSize.md)

# IMTPosition::DigitsCurrency

Get the number of decimal places the deposit currency of the client who has opened the position.

C++
    
    
    UINT  IMTPosition::DigitsCurrency()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTPosition.DigitsCurrency()

### Return Value

The number of decimal places the deposit currency of the client who has opened the position.

# IMTPosition::DigitsCurrency

Set the number of decimal places the deposit currency of the client who has opened the position.

C++
    
    
    MTAPIRES  IMTPosition::DigitsCurrency(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.DigitsCurrency(
       uint        digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places the deposit currency of the client who has opened the position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
