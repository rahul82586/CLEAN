[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteParamKeySet

[Previous](WriteParamData.md) | [Next](WriteValue.md)

# IMTReportCache::WriteParamKeySet

Set the value for the ["KeySet" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::WriteParamKeySet(
       const IMTReportCacheKeySet*  keys,     // Set of keys
       const bool                   merge     // Flag for merging changes
       )

### Parameters

**keys**  
[in] TheIMTReportCacheKeySetobject which describes keys being added.

**merge**  
[in] Flag for merging changes. If "true", only new keys form the passed set will be added to the parameter. If "false", all the keys in the parameter will be overwritten by the passed ones.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
