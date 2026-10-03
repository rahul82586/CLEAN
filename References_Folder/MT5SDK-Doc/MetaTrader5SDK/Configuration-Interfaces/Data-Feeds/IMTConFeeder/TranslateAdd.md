[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateAdd

[Previous](SymbolNext.md) | [Next](TranslateUpdate.md)

# IMTConFeeder::TranslateAdd

Add a setting of conversion of data transmitted by the data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateAdd(
       IMTConFeederTranslate*  param      // An object of data conversion setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateAdd(
       CIMTConFeederTranslate  param      // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConFeeder.TranslateAdd(
       param                   # An object of data conversion setting
       )

### Parameters

**param**  
[in] An object of data conversion setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
