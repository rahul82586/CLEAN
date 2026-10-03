[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / RemoveSet

[Previous](RemoveArray.md) | [Next](../../../Web-API/README.md)

# IMTReportCacheKeySet::RemoveSet

Delete a set of keys from the current set.
    
    
    MTAPIRES  IMTReportCacheKeySet::RemoveSet(
       const IMTReportCacheKeySet*  keyset      // Set of keys
       )

### Parameters

**keyset**  
[in] TheIMTReportCacheKeySetobject, which describes the set of keys to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
