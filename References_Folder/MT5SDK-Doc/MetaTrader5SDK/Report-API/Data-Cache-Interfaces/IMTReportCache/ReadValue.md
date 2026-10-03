[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadValue

[Previous](ReadParamKeySet.md) | [Next](ReadValues.md)

# IMTReportCache::ReadValue

Get the cache value with the specified key.
    
    
    MTAPIRES  IMTReportCache::ReadValue(
       const UINT64          key,       // Key
       IMTReportCacheValue*  value      // Description of the value
       )

### Parameters

**key**  
[in] The key for which data will be retrieved.

**value**  
[out] TheIMTReportCacheValueobject to which the key value is placed. The object must be previously created using theIMTReportReportCache::ValueCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
