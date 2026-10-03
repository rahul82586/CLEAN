[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateNext

[Previous](TranslateTotal.md) | [Next](TranslateGet.md)

# IMTConFeeder::TranslateNext

Get a setting of conversion of data transmitted by the data feed by the index.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateNext(
       const UINT              pos,       // Position of the data feed
       IMTConFeederTranslate*  param      // An object of data conversion setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateNext(
       uint                    pos,       // Position of the data feed
       CIMTConFeederTranslate  param      // An object of data conversion setting
       )

Python (Manager API)
    
    
    MTConFeeder.TranslateNext(
       pos                     # Position of the data feed
       )

### Parameters

**pos**  
[in] Position of a data feed, starting with 0.

**param**  
[out] An object of data conversion setting. The 'param' object must first be created using theIMTAdminAPI::FeederTranslateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the conversion settings of a data feed with a specified index to the param object.
