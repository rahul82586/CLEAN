[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / SymbolPerfomance

[Previous](Symbol.md) | [Next](SymbolAssets.md)

# IMTConFund::SymbolPerfomance

Get the name of the symbol used for displaying the current value of assets.

C++
    
    
    LPCWSTR  IMTConFund::SymbolPerfomance()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFund.SymbolPerfomance()

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFund](../IMTConFund.md) object.

# IMTConFund::SymbolPerfomance

Set the name of the symbol used for displaying the current value of assets.

C++
    
    
    MTAPIRES  IMTConFund::SymbolPerfomance(
       LPCWSTR  symbol    // Symbol name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.SymbolPerfomance(
       srting   symbol    // Symbol name
       )

### Parameters

**name**  
[in] The name of the symbol used for displaying the current value of assets.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
