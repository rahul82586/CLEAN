[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Symbol

[Previous](Clear.md) | [Next](Path.md)

# IMTConSymbol::Symbol

Get the symbol name.

C++
    
    
    LPCWSTR  IMTConSymbol::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Symbol()

Python (Manager API)
    
    
    MTConSymbol.Symbol

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Symbol

Set the symbol name.

C++
    
    
    MTAPIRES  IMTConSymbol::Symbol(
       LPCWSTR  symbol      // Symbol name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Symbol(
       string   symbol      // Symbol name
       )

Python (Manager API)
    
    
    MTConSymbol.Symbol

### Parameters

**symbol**  
[in] Symbol name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the symbol name is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
