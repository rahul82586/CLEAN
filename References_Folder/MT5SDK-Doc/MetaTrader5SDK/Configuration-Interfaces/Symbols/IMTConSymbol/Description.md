[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Description

[Previous](ISIN.md) | [Next](International.md)

# IMTConSymbol::Description

Get the description of a symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Description()

Python (Manager API)
    
    
    MTConSymbol.Description

### Return Value

If successful, it returns a pointer to a string with the description of a symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

To use the string after the object removal (call of the [IMTConSymbol::Release](Release.md) method of this object), a copy of it should be created.

# IMTConSymbol::Description

Set the description of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::Description(
       LPCWSTR  descr      // Description of a symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Description(
       string   descr      // Description of a symbol
       )

Python (Manager API)
    
    
    MTConSymbol.Description

### Parameters

**descr**  
[in] The symbol description.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of symbol description is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
