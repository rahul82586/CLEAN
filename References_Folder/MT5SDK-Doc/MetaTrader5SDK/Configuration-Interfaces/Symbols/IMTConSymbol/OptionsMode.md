[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / OptionsMode

[Previous](ChartMode.md) | [Next](PriceStrike.md)

# IMTConSymbol::OptionsMode

Getting the option type and style.

C++
    
    
    UINT  IMTConSymbol::OptionsMode()  const

.NET (Gateway/Manager API)
    
    
    EnOptionMode  CIMTConSymbol.OptionsMode()

Python (Manager API)
    
    
    MTConSymbol.OptionsMode

### Return Value

One of the value of the [IMTConSymbol::EnOptionMode (#enoptionmode)](Enumerations.md#enoptionmode) enumeration.

# IMTConSymbol::OptionsMode

Setting the option type and style.

C++
    
    
    MTAPIRES  IMTConSymbol::OptionsMode(
       const UINT   mode     // The option type and style
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.OptionsMode(
       EnOptionMode mode     // The option type and style
       )

Python (Manager API)
    
    
    MTConSymbol.OptionsMode()

### Parameters

**mode**  
[in] To pass the option type and style, theIMTConSymbol::EnOptionModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### 
