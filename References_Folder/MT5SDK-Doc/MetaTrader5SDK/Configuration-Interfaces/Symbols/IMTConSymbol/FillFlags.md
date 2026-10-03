[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FillFlags

[Previous](GTCMode.md) | [Next](ExpirFlags.md)

# IMTConSymbol::FillFlags

Get the types of filling allowed for a symbol in this symbol.

C++
    
    
    UINT  IMTConSymbol::FillFlags()  const

.NET (Gateway/Manager API)
    
    
    EnFillingFlags  CIMTConSymbol.FillFlags()

Python (Manager API)
    
    
    MTConSymbol.FillFlags

### Return Value

A value of the [IMTConSymbol::EnFillingFlags (#enfillingflags)](Enumerations.md#enfillingflags) enumeration.

# IMTConSymbol::FillFlags

Set the types of filling allowed for a symbol in this symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::FillFlags(
       const UINT      flags  // Flags of filling types
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FillFlags(
       EnFillingFlags  flags  // Flags of filling types
       )

Python (Manager API)
    
    
    MTConSymbol.FillFlags

### Parameters

**flags**  
[in] To pass the filling types, theIMTConSymbol::EnFillingFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
