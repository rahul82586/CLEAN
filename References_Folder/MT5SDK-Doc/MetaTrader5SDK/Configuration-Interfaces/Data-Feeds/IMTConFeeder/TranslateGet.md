[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateGet

[Previous](TranslateNext.md) | [Next](StateConnected.md)

# IMTConFeeder::TranslateGet

Get a setting of conversion of data transmitted by the data feed by the symbol.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateGet(
       LPCWSTR                 symbol,     // Symbol name
       IMTConFeederTranslate*  param       // An object of data conversion setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateGet(
       string                  symbol,     // Symbol name
       CIMTConFeederTranslate  param       // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConFeeder.TranslateGet(
       symbol                  # Symbol name
       )

### Parameters

**symbol**  
[in] Symbol name.

**param**  
[out] An object of data conversion setting. The 'param' object must first be created using theIMTAdminAPI::FeederTranslateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConFeederTranslate::Symbol()](../IMTConFeederTranslate/Symbol.md) value is used as the symbol.
