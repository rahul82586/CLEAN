[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Source

[Previous](Basis.md) | [Next](Page.md)

# IMTConSymbol::Source

Get the name of the source symbol whose quotes should be used for the current financial instrument.

C++
    
    
    LPCWSTR  IMTConSymbol::Source()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Source()

Python (Manager API)
    
    
    MTConSymbol.Source

### Return Value

If successful, it returns a pointer to a string with the name of the source symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Source

Set the name of the source symbol whose quotes should be used for the current financial instrument.

C++
    
    
    MTAPIRES  IMTConSymbol::Source(
       LPCWSTR  source      // A name of the source symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Source(
       string   source      // A name of the source symbol
       )

Python (Manager API)
    
    
    MTConSymbol.Source

### Parameters

**source**  
[in] Source symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name of a symbol that exists in the platform ([IMTConSymbol::Symbol](Symbol.md)) is specified as the source.
