[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Digits

[Previous](ColorBackground.md) | [Next](Point.md)

# IMTConSymbol::Digits

Get the number of decimal places in the price of the symbol.

C++
    
    
    UINT  IMTConSymbol::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.Digits()

Python (Manager API)
    
    
    MTConSymbol.Digits

### Return Value

The number of decimal places in the price of the symbol.

# IMTConSymbol::Digits

Set the number of decimal places in the price of the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::Digits(
       UINT  digits      // Number of decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Digits(
       uint  digits      // Number of decimal places
       )

Python (Manager API)
    
    
    MTConSymbol.Digits

### Parameters

**digits**  
[in] The number of decimal places in the price of the symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
