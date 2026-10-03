[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteValue

[Previous](WriteParamKeySet.md) | [Next](WriteMissingKeys.md)

# IMTReportCache::WriteValue

Write the value for a key in the cache.
    
    
    MTAPIRES  IMTReportCache::WriteValue(
       const UINT64  key,        // Key
       const void*   value,      // Value
       const UINT    size        // Size
       )

### Parameters

**key**  
[in] The key to write data for. If there is no such key, it will be added.

**value**  
[in] The key value.

**size**  
[in] Value size in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
