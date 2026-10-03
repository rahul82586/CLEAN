[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / TranslateDelete

[Previous](TranslateUpdate.md) | [Next](TranslateClear.md)

# IMTConFeeder::TranslateDelete

Remove a setting of conversion of data transmitted by the data feed by the index.

C++
    
    
    MTAPIRES  IMTConFeeder::TranslateDelete(
       const UINT  pos      // Setting position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.TranslateDelete(
       uint        pos      // Setting position
       )

Python (Manager API)
    
    
    MTConFeeder.TranslateDelete(
       pos         # Setting position
       )

### Parameters

**pos**  
[in] Setting position, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
