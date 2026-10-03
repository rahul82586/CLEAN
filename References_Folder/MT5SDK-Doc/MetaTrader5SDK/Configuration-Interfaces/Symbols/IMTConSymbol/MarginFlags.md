[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginFlags

[Previous](VolumeLimitExt.md) | [Next](MarginInitial.md)

# IMTConSymbol::MarginFlags

Get the additional margin check modes.

C++
    
    
    UINT  IMTConSymbol::MarginFlags()  const

.NET (Gateway/Manager API)
    
    
    EnMarginFlags  CIMTConSymbol.MarginFlags()

Python (Manager API)
    
    
    MTConSymbol.MarginFlags

### Return Value

One of the values of the [IMTConSymbol::EnMarginFlags (#enmarginflags)](Enumerations.md#enmarginflags) enumeration.

# IMTConSymbol::MarginFlags

Set the additional margin check modes.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginFlags(
       const UINT     mode      // Margin checking mode
       )

.NET (Gateway/Manager API)s
    
    
    MTRetCode  CIMTConSymbol.MarginFlags(
       EnMarginFlags  mode      // Margin checking mode
       )

Python (Manager API)
    
    
    MTConSymbol.MarginFlags

### Parameters

**mode**  
[in] Margin checking mode is passed using theIMTConSymbol::EnMarginFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
