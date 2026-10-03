[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / OrderFlags

[Previous](IEFlagsDefault.md) | [Next](OrderFlagsDefault.md)

# IMTConGroupSymbol::OrderFlags

Gets the flags of order types allowed for the symbol.

C++
    
    
    UINT  IMTConGroupSymbol::OrderFlags()  const

.NET (Gateway/Manager API)
    
    
    EnOrderFlags  CIMTConGroupSymbol.OrderFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.OrderFlags

### Return Value

The flags are passed using the [IMTConSymbol::EnOrderFlags (#enorderflags)](../../Symbols/IMTConSymbol/Enumerations.md#enorderflags) enumeration.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::OrderFlags

Sets the flags of order types allowed for the symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::OrderFlags(
       const UINT  flags      // Order flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.OrderFlags(
       EnOrderFlags flags      // Order flags
       )

Python (Manager API)
    
    
    MTConGroupSymbol.OrderFlags

### Parameters

**flags**  
[in] The flags are passed using theIMTConSymbol::EnOrderFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method operates with individual symbol settings for groups.
