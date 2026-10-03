[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateUpdate

[Previous](TranslateAdd.md) | [Next](TranslateDelete.md)

# IMTConFeeder::TranslateUpdate

Update the data conversion settings of the data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateUpdate(
       const UINT                    pos,       // Setting position
       const IMTConFeederTranslate*  param      // An object of a data feed parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateUpdate(
       uint                          pos,       // Setting position
       CIMTConFeederTranslate        param      // An object of a data feed parameter
       )

Python (Manager API)
    
    
    MTConFeeder.TranslateUpdate(
       pos,                          # Setting position
       param                         # An object of a data feed parameter
       )
    
    
    MTConFeeder.TranslateSet(
       param                         # A list of objects of a data feed parameters
       )

### Parameters

**pos**  
[in] Setting position, starting with 0.

**param**  
[in] An object of data conversion setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
