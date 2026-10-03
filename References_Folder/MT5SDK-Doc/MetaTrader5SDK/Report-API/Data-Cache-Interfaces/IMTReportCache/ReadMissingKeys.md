[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadMissingKeys

[Previous](ReadValues.md) | [Next](ReadDictionaryPos.md)

# IMTReportCache::ReadMissingKeys

Get the list of missing keys in cache.
    
    
    MTAPIRES  IMTReportCache::ReadMissingKeys(
       const IMTReportCacheKeySet*  keys,             // The set of keys to check
       IMTReportCacheKeySet*        missing_keys      // The set of missing keys
       )

### Parameters

**keys**  
[in] TheIMTReportCacheKeySetobject which describes the set of keys to be checked in the cache.

**missing_keys**  
[out] TheIMTReportCacheKeySetobject to which the missing keys are added. The object must be previously created using theIMTReportAPI::KeySetCreatemethod.

### Return Value

If the method is successfully executed and missing keys are found, the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) code is returned. If there are no missing keys, [MT_RET_OK_NONE](../../../Return-Codes/Successful-completion.md) is returned.

### Note

To check if there are any missing keys without retrieving the list of such keys specify the NULL value for the missing_keys parameter.
