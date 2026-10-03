[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / ColorBackground

[Previous](Color.md) | [Next](Digits.md)

# IMTConSymbol::ColorBackground

Get the color of the symbol background in the "Market Watch" window of the terminals.

C++
    
    
    COLORREF  IMTConSymbol::ColorBackground()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.ColorBackground()

Python (Manager API)
    
    
    MTConSymbol.ColorBackground

### Return Value

The color of the symbol background in the "Market Watch" window of the terminals.

# IMTConSymbol::ColorBackground

Set the color of the symbol background in the "Market Watch" window of the terminals.

C++
    
    
    MTAPIRES  IMTConSymbol::ColorBackground(
       const COLORREF  color      // The color of the symbol background
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.ColorBackground(
       uint            color      // The color of the symbol background
       )

Python (Manager API)
    
    
    MTConSymbol.ColorBackground

### Parameters

**color**  
[in] The color of the symbol background.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
