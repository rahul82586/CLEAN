[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / REFlags

[Previous](RETimeoutDefault.md) | [Next](REFlagsDefault.md)

# IMTConGroupSymbol::REFlags

Gets request execution flags for this group.

C++
    
    
    UINT  IMTConGroupSymbol::REFlags()  const

.NET (Gateway/Manager API)
    
    
    EnREFlags  CIMTConGroupSymbol.REFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.REFlags

### Return Value

A value of the [IMTConGroupSymbol::EnREFlags (#enreflags)](Enumerations.md#enreflags) enumeration.

# IMTConGroupSymbol::REFlags

Sets request execution flags for this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::REFlags(
       const UINT  flags      // Flags of request execution
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.REFlags(
       EnREFlags   flags      // Flags of request execution
       )

Python (Manager API)
    
    
    MTConGroupSymbol.REFlags

### Parameters

**flags**  
[in] The request execution flags. To pass the options, theIMTConGroupSymbol::EnREFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
