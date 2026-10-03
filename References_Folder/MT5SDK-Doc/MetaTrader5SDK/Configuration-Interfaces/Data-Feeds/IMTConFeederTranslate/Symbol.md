[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederTranslate](../IMTConFeederTranslate.md) / Symbol

[Previous](Source.md) | [Next](BidMarkup.md)

# IMTConFeederTranslate::Symbol

Get the name of a [symbol](../../Symbols.md) in the trading platform.

C++
    
    
    LPCWSTR  IMTConFeederTranslate::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederTranslate.Symbol()

Python (Manager API)
    
    
    MTConFeederTranslate.Symbol

### Return Value

If successful, it returns a pointer to a string with the symbol name if the trading platform. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeederTranslate](../IMTConFeederTranslate.md) object.

# IMTConFeederTranslate::Symbol

Set the symbol name in the trading platform.

C++
    
    
    MTAPIRES  IMTConFeederTranslate::Symbol(
       LPCWSTR  symbol      // The name of a symbol in the trading platform
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederTranslate.Symbol(
       srting   symbol      // The name of a symbol in the trading platform
       )

Python (Manager API)
    
    
    MTConFeederTranslate.Symbol

### Parameters

**symbol**  
[in] The name of a symbol in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
