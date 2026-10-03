[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Path

[Previous](Symbol.md) | [Next](ISIN.md)

# IMTConSymbol::Path

Get the path to the symbol, including the name of the symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::Path()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Path()

Python (Manager API)
    
    
    MTConSymbol.Path

### Return Value

If successful, it returns a pointer to a string with a path to the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Path

Set the path to the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::Path(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Path(
       string   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConSymbol.Path

### Parameters

**path**  
[in] A path to the symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A symbol name should be included into the path to the symbol.
