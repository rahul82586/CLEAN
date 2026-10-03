[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / FillFlags

[Previous](ExecModeDefault.md) | [Next](FillFlagsDefault.md)

# IMTConGroupSymbol::FillFlags

Get types of filling allowed for a symbol in this group.

C++
    
    
    UINT  IMTConGroupSymbol::FillFlags()  const

.NET (Gateway/Manager API)
    
    
    EnFillingFlags  CIMTConGroupSymbol.FillFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.FillFlags

### Return Value

One of the values of the [IMTConSymbol::EnFillingFlags (#enfillingflags)](../../Symbols/IMTConSymbol/Enumerations.md#enfillingflags) enumeration.

# IMTConGroupSymbol::FillFlags

Set types of filling allowed for a symbol in this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::FillFlags(
       const UINT      flags  // Filling type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.FillFlags(
       EnFillingFlags  flags  // Filling type
       )

Python (Manager API)
    
    
    MTConGroupSymbol.FillFlags

### Parameters

**flags**  
[in] To pass the mode of filling, theIMTConSymbol::EnFillingFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
