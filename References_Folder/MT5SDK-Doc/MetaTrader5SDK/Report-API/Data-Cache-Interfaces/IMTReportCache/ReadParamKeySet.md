[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadParamKeySet

[Previous](ReadParamData.md) | [Next](ReadValue.md)

# IMTReportCache::ReadParamKeySet

Get the value of the ["KeySet" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::ReadParamKeySet(
       IMTReportCacheKeySet*  keys      // Set of keys
       )

### Parameters

**keys**  
[out] TheIMTReportCacheKeySetobject which describes the value of the "KeySet" parameter. The object must be previously created using theIMTReportAPI::KeySetCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
