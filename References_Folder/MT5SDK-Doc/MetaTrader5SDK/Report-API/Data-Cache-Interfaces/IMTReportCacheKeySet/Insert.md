[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Insert

[Previous](Reserve.md) | [Next](InsertArray.md)

# IMTReportCacheKeySet::Insert

Add a key to the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::Insert(
       const UINT64  key      // Key
       )

### Parameters

**key**  
[in] The key to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
