[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyMargin

[Previous](CurrencyProfitDigitsSet.md) | [Next](CurrencyMarginDigits.md)

# IMTConSymbol::CurrencyMargin

Get the margin currency of a symbol.

C++
    
    
    LPCWSTR  IMTConSymbol::CurrencyMargin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.CurrencyMargin()

Python (Manager API)
    
    
    MTConSymbol.CurrencyMargin

### Return Value

If successful, it returns a pointer to a string with the name of the margin currency of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::CurrencyMargin

Set the margin currency of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::CurrencyMargin(
       LPCWSTR  currency      // Margin currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CurrencyMargin(
       string   currency      // Margin currency
       )

Python (Manager API)
    
    
    MTConSymbol.CurrencyMargin

### Parameters

**currency**  
[in] The symbol margin currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of currency name is 16 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
