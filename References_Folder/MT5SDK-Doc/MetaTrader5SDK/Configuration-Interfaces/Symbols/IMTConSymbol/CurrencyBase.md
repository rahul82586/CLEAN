[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyBase

[Previous](Page.md) | [Next](CurrencyBaseDigits.md)

# IMTConSymbol::CurrencyBase

Get the base currency of a symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::CurrencyBase()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.CurrencyBase()

Python (Manager API)
    
    
    MTConSymbol.CurrencyBase

### Return Value

If successful, it returns a pointer to a string with the name of the symbol's base currency. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::CurrencyBase

Set the base currency of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::CurrencyBase(
       LPCWSTR  currency      // Base currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CurrencyBase(
       stirng   currency      // Base currency
       )

Python (Manager API)
    
    
    MTConSymbol.CurrencyBase

### Parameters

**currency**  
[in] The base currency of a symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of currency name is 16 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
