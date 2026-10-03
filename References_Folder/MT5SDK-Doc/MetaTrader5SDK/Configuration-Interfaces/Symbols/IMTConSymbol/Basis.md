[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Basis

[Previous](Country.md) | [Next](Source.md)

# IMTConSymbol::Basis

Gets the underlying asset of a derivative financial instrument.

C++
    
    
    LPCWSTR  IMTConSymbol::Basis()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Basis()

Python (Manager API)
    
    
    MTConSymbol.Basis

### Return Value

If successful, it returns a pointer to a string with the name of the name of the basic asset. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

To use the string after the object removal (call of the [IMTConSymbol::Release](Release.md) method of this object), a copy of it should be created.

The name of a symbol that exists in the platform ([IMTConSymbol::Symbol](Symbol.md)) is specified as the basic asset.

# IMTConSymbol::Basis

Sets the underlying asset of a derivative financial instrument.

C++
    
    
    MTAPIRES  IMTConSymbol::Basis(
       LPCWSTR  basis      // Symbol name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Basis(
       string   basis      // Symbol name
       )

Python (Manager API)
    
    
    MTConSymbol.Basis

### Parameters

**basis**  
[in] A name of the basic symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name of a symbol that exists in the platform ([IMTConSymbol::Symbol](Symbol.md)) is specified as the basic asset.
