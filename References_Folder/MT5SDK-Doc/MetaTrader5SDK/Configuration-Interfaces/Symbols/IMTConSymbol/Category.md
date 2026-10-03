[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Category

[Previous](International.md) | [Next](Exchange.md)

# IMTConSymbol::Category

Get the symbol category.

C++
    
    
    LPCWSTR  IMTConSymbol::Category()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Category()

Python (Manager API)
    
    
    MTConSymbol.Category

### Return Value

If successful, the method returns a pointer to a string with the symbol category. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Category

Set the symbol category.

C++
    
    
    MTAPIRES  IMTConSymbol::Category(
       LPCWSTR  category    // Symbol category
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Category(
       string   category    // Symbol category
       )

Python (Manager API)
    
    
    MTConSymbol.Category

### Parameters

**category**  
[in] Symbol category.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Categories are intended for additional marking of financial instruments. For example, this can be the market sector to which the symbol belongs: Agriculture, Oil & Gas and others.
