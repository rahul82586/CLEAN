[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteMissingKeys

[Previous](WriteValue.md) | [Next](WriteDictionaryString.md)

# IMTReportCache::WriteMissingKeys

Add missing keys to the cache.
    
    
    MTAPIRES  IMTReportCache::WriteMissingKeys(
       const IMTReportCacheKeySet*  keys      // Set of keys
       )

### Parameters

**keys**  
[in] TheIMTReportCacheKeySetobjects which describes the keys to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method only adds missing keys from the set. The values of existing keys are not replaced.
