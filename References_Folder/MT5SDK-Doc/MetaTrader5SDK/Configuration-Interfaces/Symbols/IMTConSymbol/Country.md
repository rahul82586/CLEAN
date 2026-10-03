[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Country

[Previous](Industry.md) | [Next](Basis.md)

# IMTConSymbol::Country

Get the country of the company whose shares are traded on the stock exchange.

C++
    
    
    LPCWSTR  IMTConSymbol::Country()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Country()

Python (Manager API)
    
    
    MTConSymbol.Country

### Return Value

If successful, a pointer to a string with the country name is returned. Otherwise, NULL is returned.

# IMTConSymbol::Country

Set the country of the company whose shares are traded on the stock exchange.

C++
    
    
    MTAPIRES  IMTConSymbol::Country(
       LPCWSTR  country    // country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Country(
       string   country    // country
       )

Python (Manager API)
    
    
    MTConSymbol.Country

### Parameters

**country**  
[in] Country name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
