[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteEnd

[Previous](WriteBegin.md) | [Next](WriteParamFrom.md)

# IMTReportCache::WriteEnd

Finish writing data to the cache.
    
    
    MTAPIRES  IMTReportCache::WriteEnd(
       bool  apply      // Flag for saving changes
       )

### Parameters

**apply**  
[in] The flag for saving changes in the cache. If true, all changes made to the cache between the lastIMTReportCache::WriteBegincall and this method call will be saved. If false, no changes will be saved.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Only one report instance can be writing data to cache at a time.
