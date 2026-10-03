[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / InsertArray

[Previous](Insert.md) | [Next](InsertSet.md)

# IMTReportCacheKeySet::InsertArray

Add an array of keys to the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::InsertArray(
       const UINT64*  keys,     // Array of keys
       const UINT     total     // Number of keys
       )

### Parameters

**keys**  
[in] The array of keys you want to add.

**total**  
[in] The number of keys in the array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
