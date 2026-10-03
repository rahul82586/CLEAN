[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Color

[Previous](CurrencyMarginDigitsSet.md) | [Next](ColorBackground.md)

# IMTConSymbol::Color

Get the color of the symbol in the "Market Watch" window of the terminals.

C++
    
    
    COLORREF  IMTConSymbol::Color()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.Color()

Python (Manager API)
    
    
    MTConSymbol.Color

### Return Value

The color of the symbol in the "Market Watch" window of the terminals.

### Note

This method is reserved for future use and is not currently implemented.

# IMTConSymbol::Color

Set the color of the symbol in the "Market Watch" window of the terminals.

C++
    
    
    MTAPIRES  IMTConSymbol::Color(
       const COLORREF  color      // Color of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Color(
       uint            color      // Color of the symbol
       )

Python (Manager API)
    
    
    MTConSymbol.Color

### Parameters

**color**  
[in] The color of the symbols.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is reserved for future use and is not currently implemented.
