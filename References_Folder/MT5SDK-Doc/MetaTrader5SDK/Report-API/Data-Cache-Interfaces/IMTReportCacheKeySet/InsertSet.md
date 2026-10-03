[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / InsertSet

[Previous](InsertArray.md) | [Next](Remove.md)

# IMTReportCacheKeySet::InsertSet

Add a key set to the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::InsertSet(
       const IMTReportCacheKeySet*  keyset      // Set of keys
       )

### Parameters

**keyset**  
[in] TheIMTReportCacheKeySetobject, which describes the set of keys to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
