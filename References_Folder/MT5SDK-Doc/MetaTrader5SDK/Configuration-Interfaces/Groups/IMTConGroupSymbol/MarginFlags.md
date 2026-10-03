[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginFlags

[Previous](VolumeLimitExtDefault.md) | [Next](MarginFlagsDefault.md)

# IMTConGroupSymbol::MarginFlags

Gets additional modes of symbol margin checking for the group.

C++
    
    
    UINT  IMTConGroupSymbol::MarginFlags()  const

.NET (Gateway/Manager API)
    
    
    EnMarginFlags  CIMTConGroupSymbol.MarginFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginFlags

### Return Value

One of the values of the [IMTConSymbol::EnMarginFlags (#enmarginflags)](../../Symbols/IMTConSymbol/Enumerations.md#enmarginflags) enumeration.

# IMTConGroupSymbol::MarginFlags

Sets additional modes of symbol margin checking for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginFlags(
       const UINT     mode   // Margin checking mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginFlags(
       EnMarginFlags  mode   // Margin checking mode
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginFlags

### Parameters

**mode**  
[in] Margin checking mode is passed using theIMTConSymbol::EnMarginFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
