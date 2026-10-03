[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / ExpirFlags

[Previous](FillFlagsDefault.md) | [Next](ExpirFlagsDefault.md)

# IMTConGroupSymbol::ExpirFlags

Get the type of order expiration allowed for a symbol in this group.

C++
    
    
    UINT  IMTConGroupSymbol::ExpirFlags()  const

.NET (Gateway/Manager API)
    
    
    EnExpirationFlags  CIMTConGroupSymbol.ExpirFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.ExpirFlags

### Return Value

One of the values of the [IMTConSymbol::EnExpirationFlags (#enexpirationflags)](../../Symbols/IMTConSymbol/Enumerations.md#enexpirationflags) enumeration.

# IMTConGroupSymbol::ExpirFlags

Set the type of order expiration allowed for a symbol in this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::ExpirFlags(
       const UINT         flags  // Expiration types
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.ExpirFlags(
       EnExpirationFlags  flags  // Expiration types
       )

Python (Manager API)
    
    
    MTConGroupSymbol.ExpirFlags

### Parameters

**flags**  
[in] To pass the expiration type, theIMTConSymbol::EnExpirationFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
