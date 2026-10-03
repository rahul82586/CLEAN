[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / ISIN

[Previous](Path.md) | [Next](Description.md)

# IMTConSymbol::ISIN

Get the international identification code (ISIN) of the symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::ISIN()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.ISIN()

Python (Manager API)
    
    
    MTConSymbol.ISIN

### Return Value

If successful, it returns a pointer to a string with the ISIN. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::ISIN

Set the international identification code (ISIN) of the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::ISIN(
       LPCWSTR  isin      // ISIN
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.ISIN(
       string   isin      // ISIN
       )

Python (Manager API)
    
    
    MTConSymbol.ISIN

### Parameters

**isin**  
[in] ISIN.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the ISIN is 16 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
