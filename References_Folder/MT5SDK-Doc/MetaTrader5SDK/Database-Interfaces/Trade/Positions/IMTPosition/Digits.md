[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Digits

[Previous](Action.md) | [Next](DigitsCurrency.md)

# IMTPosition::Digits

Get the number of decimal places in the price of a position.

C++
    
    
    UINT  IMTPosition::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTPosition.Digits()

### Return Value

The number of decimal places in the price of a position.

# IMTPosition::Digits

Set the number of decimal places in the price of a position.

C++
    
    
    MTAPIRES  IMTPosition::Digits(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Digits(
       uint        digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places in the price of a position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
