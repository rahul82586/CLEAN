[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / OrderFlags

[Previous](TradeFlags.md) | [Next](FaceValue.md)

# IMTConSymbol::OrderFlags

Gets the flags of order types allowed for the symbol.

C++
    
    
    UINT  IMTConSymbol::OrderFlags()  const

.NET (Gateway/Manager API)
    
    
    EnOrderFlags  CIMTConSymbol.OrderFlags()

Python (Manager API)
    
    
    MTConSymbol.OrderFlags

### Return Value

A value of the [IMTConSymbol::EnOrderFlags (#enorderflags)](Enumerations.md#enorderflags) enumeration.

# IMTConSymbol::OrderFlags

Sets the flags of order types allowed for the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::OrderFlags(
       const UINT    flags    // Order flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.OrderFlags(
       EnOrderFlags  flags    // Order flags
       )

Python (Manager API)
    
    
    MTConSymbol.OrderFlags

### Parameters

**flags**  
[in] The flags are passed using theIMTConSymbol::EnOrderFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
