[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadValues

[Previous](ReadValue.md) | [Next](ReadMissingKeys.md)

# IMTReportCache::ReadValues

Get multiple values from cache using a set of keys.
    
    
    MTAPIRES  IMTReportCache::ReadValues(
       const IMTReportCacheKeySet*  keys,      // Set of keys
       IMTReportCacheValue*         value      // Values
       )

### Parameters

**keys**  
[in] TheIMTReportCacheKeySet, which described the set of keys for which you want to request data.

**value**  
[out] Values as theIMTReportCacheValueobject. The object must be previously created using theIMTReportReportCache::ValueCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
