[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / SymbolAssets

[Previous](SymbolPerfomance.md) | [Next](Server.md)

# IMTConFund::SymbolAssets

Get the name of the symbol used for displaying the fund yield.

C++
    
    
    LPCWSTR  IMTConFund::SymbolAssets()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFund.SymbolAssets()

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFund](../IMTConFund.md) object.

# IMTConFund::SymbolAssets

Set the name of the symbol used for displaying the fund yield.

C++
    
    
    MTAPIRES  IMTConFund::SymbolAssets(
       LPCWSTR  symbol    // Symbol name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.SymbolAssets(
       srting   symbol    // Symbol name
       )

### Parameters

**name**  
[in] The name of the symbol used for displaying the fund yield.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
