[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / ExpirFlags

[Previous](FillFlags.md) | [Next](Spread.md)

# IMTConSymbol::ExpirFlags

Get the available type of order expiration for a symbol.

C++
    
    
    UINT  IMTConSymbol::ExpirFlags()  const

.NET (Gateway/Manager API)
    
    
    EnExpirationFlags  CIMTConSymbol.ExpirFlags()

Python (Manager API)
    
    
    MTConSymbol.ExpirFlags

### Return Value

A value of the [IMTConSymbol::EnExpirationFlags (#enexpirationflags)](Enumerations.md#enexpirationflags) enumeration.

# IMTConSymbol::ExpirFlags

Set the available types of order execution for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::ExpirFlags(
       const UINT         flags  // The flags of order expiration types
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.ExpirFlags(
       EnExpirationFlags  flags  // The flags of order expiration types
       )

Python (Manager API)
    
    
    MTConSymbol.ExpirFlags

### Parameters

**flags**  
[in] To pass the order expiration types, theIMTConSymbol::EnExpirationFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
