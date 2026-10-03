[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / International

[Previous](Description.md) | [Next](Category.md)

# IMTConSymbol::International

Get the international name of a symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::International()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.International()

Python (Manager API)
    
    
    MTConSymbol.International

### Return Value

If successful, it returns a pointer to a string with the international name of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::International

Set the international name of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::International(
       LPCWSTR  intern      // International symbol name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.International(
       string   intern      // International symbol name
       )

Python (Manager API)
    
    
    MTConSymbol.International

### Parameters

**intern**  
[in] The international symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the international name of a symbol is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
