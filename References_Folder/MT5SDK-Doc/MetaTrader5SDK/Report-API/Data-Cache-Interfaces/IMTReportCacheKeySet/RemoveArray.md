[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / RemoveArray

[Previous](Remove.md) | [Next](RemoveSet.md)

# IMTReportCacheKeySet::RemoveArray

Delete an array of keys from the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::RemoveArray(
       const UINT64*  keys,     // Array of keys
       const UINT     total     // Number of keys
       )

### Parameters

**keys**  
[in] The array of keys you want to delete.

**total**  
[in] The number of keys in the array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
