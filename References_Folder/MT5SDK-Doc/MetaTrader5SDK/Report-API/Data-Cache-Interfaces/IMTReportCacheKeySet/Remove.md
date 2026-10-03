[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Remove

[Previous](InsertSet.md) | [Next](RemoveArray.md)

# IMTReportCacheKeySet::Remove

Delete a key from the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::Remove(
       const UINT64  key      // Key
       )

### Parameters

**key**  
[in] the key which you want to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
