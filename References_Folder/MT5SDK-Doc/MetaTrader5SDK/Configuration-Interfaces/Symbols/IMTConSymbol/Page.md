[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Page

[Previous](Source.md) | [Next](CurrencyBase.md)

# IMTConSymbol::Page

Get the address of the web page of a symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::Page()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Page()

Python (Manager API)
    
    
    MTConSymbol.Page

### Return Value

If successful, it returns a pointer to a string with the address of the symbol web page. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Page

Set the address of the web page of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::Page(
       LPCWSTR  source      // The web page address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Page(
       string   source      // The web page address
       )

Python (Manager API)
    
    
    MTConSymbol.Page

### Parameters

**source**  
[in] The address of the symbol web page.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the address is 256 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
